#!/usr/bin/env bash
# Mixage final : musique (en retrait) + voix off ElevenLabs si présente, puis mux
# avec la vidéo muette rendue par HyperFrames.
#   - voix : assets/voice/voix-off.wav (une seule piste, calée sur data/timeline.json)
#   - musique : assets/music/musique-travail.wav (ou la musique définitive, même nom)
# Sans voix : la musique est mixée seule à -16 LUFS (version de travail).
# Avec voix : la musique est baissée de ~12 dB et « duckée » sous la voix
# (sidechain), voix normalisée, mix final à -14 LUFS (cible Reels/TikTok).
set -euo pipefail
cd "$(dirname "$0")/.."
VIDEO=${1:-renders/video-muette.mp4}
OUT=${2:-renders/reveillon-villa-beach_9x16_version-de-travail.mp4}
MUSIC=assets/music/musique-travail.wav
VOICE=assets/voice/voix-off.wav

if [[ -f "$VOICE" ]]; then
  ffmpeg -v error -y -i "$VIDEO" -i "$MUSIC" -i "$VOICE" -filter_complex "
    [2:a]aformat=sample_rates=48000:channel_layouts=stereo,highpass=f=80,acompressor=threshold=-20dB:ratio=3:attack=5:release=120,loudnorm=I=-15:TP=-2:LRA=7,asplit=2[vo][sc];
    [1:a]aformat=sample_rates=48000:channel_layouts=stereo,volume=-12dB[mu];
    [mu][sc]sidechaincompress=threshold=0.03:ratio=8:attack=20:release=350[duck];
    [duck][vo]amix=inputs=2:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=9[a]" \
    -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k -shortest -movflags +faststart "$OUT"
else
  ffmpeg -v error -y -i "$VIDEO" -i "$MUSIC" -filter_complex "
    [1:a]aformat=sample_rates=48000:channel_layouts=stereo,loudnorm=I=-16:TP=-1.5:LRA=9[a]" \
    -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k -shortest -movflags +faststart "$OUT"
fi
echo "$OUT"
