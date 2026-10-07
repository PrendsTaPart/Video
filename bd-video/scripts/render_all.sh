#!/usr/bin/env bash
# Rendu HyperFrames local + mixage audio, épisode par épisode.
#   bash bd-video/scripts/render_all.sh ep02 ep03 … film
set -euo pipefail
ROOT="$(git rev-parse --show-toplevel)/bd-video"
export HYPERFRAMES_BROWSER_PATH="${HYPERFRAMES_BROWSER_PATH:-$(ls -d /opt/pw-browsers/chromium_headless_shell-*/*/headless_shell | head -1)}"
mkdir -p "$ROOT/renders/episodes" "$ROOT/renders/film" "$ROOT/previews"
for name in "$@"; do
  dir=episodes; [ "$name" = film ] && dir=film
  out="$ROOT/renders/$dir/$name"
  echo "[$(date +%T)] rendu $name"
  (cd "$ROOT/montage/$name" && npx hyperframes render --quiet --crf 20 -o "$out-video.mp4" .)
  python3 "$ROOT/scripts/mix_audio.py" "$name" "$out-video.mp4" "$out.mp4"
  ffmpeg -v error -y -i "$out.mp4" -vf scale=720:-2 -c:v libx264 -crf 24 -preset veryfast -c:a copy \
    -movflags +faststart "$ROOT/previews/$name-720p.mp4"
  echo "[$(date +%T)] $name prêt"
done
