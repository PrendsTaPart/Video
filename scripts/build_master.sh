#!/usr/bin/env bash
# /ep-montage (partie 1) — Concatène A_hook + B_corps + outro Remotion, mixe la VO,
# normalise le loudness à -14 LUFS, brûle les sous-titres. Produit le master 40s 9:16.
#
# Prérequis : normalize.sh déjà lancé (build/A_hook.norm.mp4, build/B_corps.norm.mp4),
# outro Remotion déjà rendu (build/outro_c.mp4), VO alignée (build_voice_track.py déjà lancé
# → build/vo_mix.wav), sous-titres générés (build/subs.srt).
#
# Usage :
#   bash scripts/build_master.sh <episode-dir>
set -euo pipefail

EP_DIR="${1:?Usage: build_master.sh <episode-dir> (ex: episodes/ep01-la-rentree)}"
BUILD_DIR="$EP_DIR/build"
EXPORT_DIR="$EP_DIR/exports"
mkdir -p "$EXPORT_DIR"

A="$BUILD_DIR/A_hook.norm.mp4"
B="$BUILD_DIR/B_corps.norm.mp4"
C="$BUILD_DIR/outro_c.mp4"
VO="$BUILD_DIR/vo_mix.wav"
SUBS="$BUILD_DIR/subs.srt"

for f in "$A" "$B" "$C" "$VO"; do
  [[ -f "$f" ]] || { echo "❌ Manquant : $f — lance les étapes précédentes du pipeline d'abord."; exit 1; }
done

CONCAT_LIST="$BUILD_DIR/concat_list.txt"
printf "file '%s'\nfile '%s'\nfile '%s'\n" \
  "$(realpath "$A")" "$(realpath "$B")" "$(realpath "$C")" > "$CONCAT_LIST"

VIDEO_CONCAT="$BUILD_DIR/video_concat.mp4"
ffmpeg -y -f concat -safe 0 -i "$CONCAT_LIST" -c copy "$VIDEO_CONCAT"

# Mix VO sur la vidéo concaténée, loudnorm -14 LUFS (norme réseaux sociaux)
MIXED="$BUILD_DIR/mixed.mp4"
ffmpeg -y -i "$VIDEO_CONCAT" -i "$VO" \
  -filter_complex "[1:a]loudnorm=I=-14:TP=-1.5:LRA=11[aout]" \
  -map 0:v -map "[aout]" -c:v copy -c:a aac -b:a 192k -shortest "$MIXED"

MASTER="$EXPORT_DIR/master_40s_9x16.mp4"
if [[ -f "$SUBS" ]]; then
  ffmpeg -y -i "$MIXED" -vf "subtitles=$SUBS:force_style='FontName=Arial,FontSize=18,PrimaryColour=&HFFFFFF&,BorderStyle=3,Outline=2,Shadow=1'" \
    -c:a copy "$MASTER"
else
  echo "⚠️  Pas de $SUBS trouvé — master généré SANS sous-titres brûlés. À corriger avant publication."
  cp "$MIXED" "$MASTER"
fi

echo "✅ Master : $MASTER"
