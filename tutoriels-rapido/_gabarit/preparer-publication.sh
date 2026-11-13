#!/usr/bin/env bash
# Prépare la publication d'épisodes validés : 720p + miniature, commit et push (URL raw GitHub pour l'import RapidoCMS).
# Ensuite : importer via l'outil MCP Rapidocms upload_file_tool, puis python3 _gabarit/enregistrer-publication.py EP...
set -euo pipefail
G="$(cd "$(dirname "$0")" && pwd)"
bash "$G/encode720.sh" "$@"
for EP in "$@"; do cp "$G/../$EP/miniature.png" "$G/../../videos/tutoriels-rapido/720p/$EP.png"; done
cd "$G/../.."
git add videos/tutoriels-rapido/720p "${@/#/videos/tutoriels-rapido/}" 2>/dev/null || git add videos/tutoriels-rapido
git commit -q -m "720p et miniatures : $*" && git push -q origin tutoriels-rapido
for EP in "$@"; do echo "https://raw.githubusercontent.com/PrendsTaPart/video/tutoriels-rapido/videos/tutoriels-rapido/720p/$EP.mp4"; done
