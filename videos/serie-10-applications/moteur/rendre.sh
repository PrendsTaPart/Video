#!/bin/bash
# Rend un ou plusieurs épisodes : images (Playwright) -> mixage voix + musique -> vidéo finale, SRT, miniature.
# Usage : bash moteur/rendre.sh ep01-haccp-tofu [ep02-...]
ICI="$(cd "$(dirname "$0")" && pwd)"; RAC="$(dirname "$ICI")"; MOT="$RAC/../_moteur"
for s in "$@"; do
  d="$RAC/episodes/$s"
  node "$MOT/render.js" "$d" 30 > "$d/rendu.log" 2>&1 || { echo "ÉCHEC rendu $s"; continue; }
  MUSIQUE="$RAC/../planit-academy/assets/audio/musique-produit.mp3" python3 "$MOT/fin.py" "$d" "$s" 0.2 >> "$d/rendu.log" 2>&1 || { echo "ÉCHEC mixage $s"; continue; }
  mv "$d/thumb.png" "$d/$s-miniature.png" 2>/dev/null
  rm -f "$d/frames.mp4" "$d/bed.wav" "$d/mix.wav"
  echo "OK $s $(ls "$d"/*.mp4)"
done
