#!/bin/bash
# Rend les six vidéos dans out/, puis extrait trois images clés de chacune dans out/controle/.
set -e
cd "$(dirname "$0")"
NAV="${REMOTION_BROWSER:-/opt/pw-browsers/chromium_headless_shell-1243/chrome-headless-shell-linux64/chrome-headless-shell}"
mkdir -p out/controle
rendu() { # composition fichier
  npx remotion render src/index.ts "$1" "out/$2.mp4" --browser-executable="$NAV" --concurrency=4 --log=error
  d=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "out/$2.mp4")
  for p in 0.12 0.5 0.9; do
    t=$(python3 -c "print(round($d*$p,2))")
    ffmpeg -v error -y -ss "$t" -i "out/$2.mp4" -frames:v 1 -q:v 3 "out/controle/$2-$p.jpg"
  done
  echo "$2.mp4 ok ($d s)"
}
rendu noel-menu-9x16 villa-beach-noel-menu-1080x1920
rendu nouvel-an-menu-9x16 villa-beach-nouvel-an-menu-1080x1920
rendu noel-teaser-9x16 villa-beach-noel-teaser-1080x1920
rendu nouvel-an-teaser-9x16 villa-beach-nouvel-an-teaser-1080x1920
rendu noel-menu-4x5 villa-beach-noel-menu-1080x1350
rendu nouvel-an-menu-4x5 villa-beach-nouvel-an-menu-1080x1350
