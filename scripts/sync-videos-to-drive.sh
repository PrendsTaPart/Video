#!/usr/bin/env bash
# Synchronise tous les MP4 livrables du dépôt vers Google Drive (fichiers réels, pas des liens).
# Prérequis : rclone installé + un remote configuré (ex: `rclone config` -> nom "gdrive").
#
# Usage :
#   REMOTE=gdrive DEST="RapidoSoftware - Videos" bash scripts/sync-videos-to-drive.sh
#
# Astuce : pour tout récupérer, lance-le une fois par branche de feature
#   (les projets vivent sur des branches différentes) :
#     for b in claude/hyperframes-reels-studio-9f0b63 feature/video-rapidorh-4min \
#              feature/video-rapidocms-4min feature/video-tutoriel-foodeatup-5min; do
#       git checkout "$b" && REMOTE=gdrive DEST="RapidoSoftware - Videos" bash scripts/sync-videos-to-drive.sh
#     done
set -euo pipefail
REMOTE="${REMOTE:?Définis REMOTE=<nom_du_remote_rclone>}"
DEST="${DEST:-RapidoSoftware - Videos}"
ROOT="$(git rev-parse --show-toplevel)"
cd "$ROOT"
command -v rclone >/dev/null || { echo "rclone introuvable : https://rclone.org/install/"; exit 1; }

# Collecte des livrables finaux (exclut work/, avatars, mika-assets)
mapfile -t FILES < <(find videos -type f -name '*.mp4' \
  \( -path '*/deliverable/*' -o -path '*/renders/*' \) \
  -not -path '*/work/*' -not -path '*/mika/*' -not -path '*/mika-assets/*' \
  -not -path '*/assets/avatar/*' | sort)

echo "Fichiers à synchroniser : ${#FILES[@]}"
for f in "${FILES[@]}"; do
  # dossier de destination = nom du projet (2e segment du chemin)
  proj="$(echo "$f" | cut -d/ -f2)"
  echo "  → $f  =>  $REMOTE:$DEST/$proj/"
  rclone copy "$f" "$REMOTE:$DEST/$proj/" --progress
done
echo "✅ Terminé. Ouvre Google Drive → « $DEST »."
