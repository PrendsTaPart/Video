#!/usr/bin/env bash
# Rend chaque tutoriel : check HyperFrames puis rendu MP4 et vignette JPG dans rendus/.
set -e
cd "$(dirname "$0")"
mkdir -p rendus
for s in ${@:-premier-lancement quartier autour-de-moi recette scanner moi}; do
  (cd "$s" && npx --yes hyperframes@0.9.41 check >/dev/null && npx --yes hyperframes@0.9.41 render -o "../rendus/$s.mp4")
  # Plafond audio du guide (FOODEATUP-TUTORIELS-WORKFLOW.md) : limiteur sans renormalisation, image copiée telle quelle.
  ffmpeg -loglevel error -y -i "rendus/$s.mp4" -c:v copy -af "alimiter=limit=0.6:level=disabled" -c:a aac -b:a 160k -movflags +faststart "rendus/$s.tmp.mp4"
  mv "rendus/$s.tmp.mp4" "rendus/$s.mp4"
  ffmpeg -loglevel error -y -ss 4 -i "rendus/$s.mp4" -frames:v 1 -vf scale=540:-1 -q:v 3 "rendus/$s.jpg"
  echo "OK $s"
done
