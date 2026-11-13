#!/usr/bin/env bash
# Réencode des épisodes validés en 720p pour le site (H.264 + AAC, lecture progressive « faststart »).
# Publication : pousser sur GitHub (dépôt public), puis importer chaque fichier dans la bibliothèque RapidoCMS du compte
# (outil MCP Rapidocms upload_file_tool, nom « tutoriel-rapido-<EP>.mp4 » / « .png ») → URL S3 notées dans publication.json.
# Usage : bash _gabarit/encode720.sh CRM01 CMS02 ...   → ../videos/tutoriels-rapido/720p/<EP>.mp4
set -euo pipefail
cd "$(dirname "$0")/../../videos/tutoriels-rapido"
mkdir -p 720p
for EP in "$@"; do
  ffmpeg -v error -y -i "$EP.mp4" -vf "scale=1280:720:flags=lanczos" -c:v libx264 -preset slow -crf 24 \
    -profile:v high -pix_fmt yuv420p -c:a aac -b:a 128k -movflags +faststart "720p/$EP.mp4"
  echo "$EP : $(du -h "720p/$EP.mp4" | cut -f1)"
done
