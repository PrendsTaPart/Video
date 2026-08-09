#!/usr/bin/env bash
# /ep-ingest — Normalise les 2 MP4 sources (déposés manuellement depuis Higgsfield) au format
# de montage commun : 9:16, 1080x1920, fps constant, codec H.264/AAC.
#
# Usage :
#   bash scripts/normalize.sh <episode-dir>
#   bash scripts/normalize.sh episodes/ep01-la-rentree
set -euo pipefail

EP_DIR="${1:?Usage: normalize.sh <episode-dir> (ex: episodes/ep01-la-rentree)}"
SRC_DIR="$EP_DIR/sources"
BUILD_DIR="$EP_DIR/build"
FPS="${FPS:-30}"
WIDTH="${WIDTH:-1080}"
HEIGHT="${HEIGHT:-1920}"

command -v ffprobe >/dev/null || { echo "ffprobe introuvable"; exit 1; }
command -v ffmpeg >/dev/null || { echo "ffmpeg introuvable"; exit 1; }

A_HOOK="$SRC_DIR/A_hook.mp4"
B_CORPS="$SRC_DIR/B_corps.mp4"

for f in "$A_HOOK" "$B_CORPS"; do
  if [[ ! -f "$f" ]]; then
    echo "❌ Fichier manquant : $f"
    echo "   Ces 2 vidéos sont générées manuellement sur Higgsfield (voir CLAUDE.md, interdit n°1)."
    echo "   Dépose-les dans $SRC_DIR/ puis relance."
    exit 1
  fi
done

mkdir -p "$BUILD_DIR"

normalize_one() {
  local src="$1" name="$2"
  local dur width height
  dur=$(ffprobe -v error -select_streams v:0 -show_entries stream=duration \
        -of csv=p=0 "$src")
  width=$(ffprobe -v error -select_streams v:0 -show_entries stream=width \
        -of csv=p=0 "$src")
  height=$(ffprobe -v error -select_streams v:0 -show_entries stream=height \
        -of csv=p=0 "$src")
  echo "→ $name : ${dur}s, ${width}x${height}"

  ffmpeg -y -i "$src" \
    -vf "scale=${WIDTH}:${HEIGHT}:force_original_aspect_ratio=increase,crop=${WIDTH}:${HEIGHT},fps=${FPS}" \
    -c:v libx264 -pix_fmt yuv420p -preset medium -crf 18 \
    -c:a aac -b:a 192k \
    "$BUILD_DIR/${name}.norm.mp4"
}

normalize_one "$A_HOOK" "A_hook"
normalize_one "$B_CORPS" "B_corps"

echo "✅ Sources normalisées dans $BUILD_DIR/"
echo "   Vérifie manuellement contre la checklist de recette (prompts/03-PROMPTS-HIGGSFIELD.md)"
echo "   avant de lancer build_master.sh — un rendu qui rate un point est refusé."
