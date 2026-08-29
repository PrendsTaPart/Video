#!/usr/bin/env bash
# Monte un épisode de la saison 2 : scène 1 + scène 2 + outro (transition + animation).
#
#   ./scripts/monter-episode.sh 02
#
# Attend, dans renders/ep{NN}/ :
#   source/ep{NN}-scene1.mp4, source/ep{NN}-scene2.mp4   les deux plans Seedance réutilisés
#   work/vo/vo.wav                                        la voix off de l'épisode, normalisée
# et, partagé par toute la saison :
#   voix-off/transition-saison-2.mp3                      la punchline de transition
#
# Produit : ep{NN}-{slug}.mp4 (master), ep{NN}-outro.mp4, ep{NN}-outro-muet.mp4,
#           ep{NN}-thumb.png, scene2-last-frame.png
set -euo pipefail
NN=$(printf "%02d" "${1:?il manque le numéro d’épisode}")
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
EP="$ROOT/renders/ep$NN"; W="$EP/work"; SFX="$ROOT/assets/sfx"
SLUG=$(node -p "require('$ROOT/episodes.json').episodes.find(e=>e.num===$((10#$NN))).slug")
mkdir -p "$W"

echo "→ dernière image de la scène 2"
ffmpeg -y -loglevel error -sseof -0.1 -i "$EP/source/ep$NN-scene2.mp4" -frames:v 1 "$EP/scene2-last-frame.png"

echo "→ outro : 360 images + miniature"
node "$ROOT/scripts/render-outro.mjs" "$((10#$NN))"

# Piste audio de l'outro. Le calage est celui de la saison, identique sur les 30 épisodes :
# clap 0,40 · whoosh de la punchline 2,00 · voix de transition 2,10 · voix de l'épisode 4,60
# · ticks 4,40/4,73/5,07 · whoosh du tap 7,60 · ticks des cartes 9,33/9,67/10,00
# · whoosh 10,95 + impact 11,00
mix() { # $1 = vo | muet
  local VOIN="" VOMIX="" VOTAG="" N=12 O=0
  if [ "$1" = vo ]; then
    VOIN="-i $ROOT/voix-off/transition-saison-2.mp3 -i $W/vo/vo.wav"
    VOMIX="[1:a]loudnorm=I=-16:TP=-1.5:LRA=11,adelay=2100|2100,volume=1.15[t];[2:a]adelay=4600|4600[v];"
    VOTAG="[t][v]"; N=14; O=2
  fi
  ffmpeg -y -loglevel error -f lavfi -i "anullsrc=r=48000:cl=stereo:d=12" $VOIN \
    -i "$SFX/clap.wav" -i "$SFX/whoosh.wav" \
    -i "$SFX/tick.mp3" -i "$SFX/tick.mp3" -i "$SFX/tick.mp3" -i "$SFX/whoosh.wav" \
    -i "$SFX/tick.mp3" -i "$SFX/tick.mp3" -i "$SFX/tick.mp3" -i "$SFX/whoosh.wav" -i "$SFX/impact.mp3" \
    -filter_complex "${VOMIX}\
[$((1+O)):a]adelay=400|400[s1];[$((2+O)):a]adelay=2000|2000,volume=0.35[s2];\
[$((3+O)):a]adelay=4400|4400,volume=0.30[s3];[$((4+O)):a]adelay=4733|4733,volume=0.30[s4];[$((5+O)):a]adelay=5066|5066,volume=0.30[s5];\
[$((6+O)):a]adelay=7600|7600,volume=0.42[s6];\
[$((7+O)):a]adelay=9333|9333,volume=0.45[s7];[$((8+O)):a]adelay=9666|9666,volume=0.45[s8];[$((9+O)):a]adelay=10000|10000,volume=0.45[s9];\
[$((10+O)):a]adelay=10950|10950,volume=0.55[s10];[$((11+O)):a]adelay=11000|11000,volume=0.8[s11];\
[0:a]${VOTAG}[s1][s2][s3][s4][s5][s6][s7][s8][s9][s10][s11]amix=inputs=${N}:normalize=0:duration=first,\
alimiter=limit=0.92,aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo[out]" \
    -map "[out]" -t 12 -c:a pcm_s16le "$W/outro-$1.wav"
}
echo "→ pistes audio de l'outro"
mix vo; mix muet
# Niveau. L'outro est calé à un niveau de saison fixe (-18,5 LUFS) : l'aligner sur la scène 1
# ferait plonger la voix off sur les épisodes tournés en basse lumière. Le master, lui, est
# normalisé en fin de chaîne au standard des plateformes.
NIVEAU_OUTRO=-18.5
ACTUEL=$(ffmpeg -hide_banner -nostats -i "$W/outro-vo.wav" -af ebur128=framelog=quiet -f null - 2>&1 | grep -m1 "I:" | grep -oE -- "-?[0-9.]+ LUFS" | grep -oE -- "-?[0-9.]+")
GAIN=$(node -p "(($NIVEAU_OUTRO) - ($ACTUEL)).toFixed(2)")
echo "   outro : $ACTUEL LUFS → ${GAIN} dB → $NIVEAU_OUTRO LUFS"
ffmpeg -y -loglevel error -i "$W/outro-vo.wav" -af "volume=${GAIN}dB" -c:a pcm_s16le "$W/outro-vo-lvl.wav"

echo "→ mux des deux outros"
ffmpeg -y -loglevel error -i "$W/ep$NN-outro-sans-son.mp4" -i "$W/outro-vo-lvl.wav" -c:v copy -c:a aac -b:a 192k -shortest "$EP/ep$NN-outro.mp4"
ffmpeg -y -loglevel error -i "$W/ep$NN-outro-sans-son.mp4" -i "$W/outro-muet.wav"   -c:v copy -c:a aac -b:a 192k -shortest "$EP/ep$NN-outro-muet.mp4"

echo "→ master 1080×1920 à 30 fps"
norm() { ffmpeg -y -loglevel error -i "$1" -vf "scale=1080:1920:flags=lanczos,fps=30,format=yuv420p" \
  -c:v libx264 -preset slow -crf 18 -af "aresample=48000,aformat=channel_layouts=stereo" \
  -c:a aac -b:a 192k -video_track_timescale 15360 "$W/$2"; }
norm "$EP/source/ep$NN-scene1.mp4" n1.mp4
norm "$EP/source/ep$NN-scene2.mp4" n2.mp4
norm "$EP/ep$NN-outro.mp4"         n3.mp4
printf "file '%s'\n" n1.mp4 n2.mp4 n3.mp4 > "$W/list.txt"
ffmpeg -y -loglevel error -f concat -safe 0 -i "$W/list.txt" -c copy "$W/master-brut.mp4"

echo "→ normalisation du master à -16 LUFS (loudnorm deux passes, gain linéaire)"
MES=$(ffmpeg -hide_banner -nostats -i "$W/master-brut.mp4" \
  -af loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json -f null - 2>&1 | sed -n '/^{/,/^}/p')
read -r MI MTP MLRA MTHR < <(node -p "const m=$MES;[m.input_i,m.input_tp,m.input_lra,m.input_thresh].join(' ')")
echo "   avant : $MI LUFS / crête $MTP dBTP"
ffmpeg -y -loglevel error -i "$W/master-brut.mp4" \
  -af "loudnorm=I=-16:TP=-1.5:LRA=11:measured_I=$MI:measured_TP=$MTP:measured_LRA=$MLRA:measured_thresh=$MTHR:linear=true,aresample=48000" \
  -c:v copy -c:a aac -b:a 192k "$EP/ep$NN-$SLUG.mp4"

echo "✅ $EP/ep$NN-$SLUG.mp4"
ffmpeg -hide_banner -i "$EP/ep$NN-$SLUG.mp4" 2>&1 | grep -E "Duration|Stream #0:0" | sed 's/^/   /'
