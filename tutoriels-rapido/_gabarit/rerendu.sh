#!/usr/bin/env bash
# Remonte et re-rend un épisode déjà tourné (sans refilmer) : après correction de tuto.json (zones, libellés…).
# Usage : bash _gabarit/rerendu.sh CMS08
set -euo pipefail
cd "$(dirname "$0")/.."
EP="$1"
python3 _gabarit/build-tutoriel.py "$EP"
(cd "$EP" && npx -y hyperframes render --output "../../videos/tutoriels-rapido/$EP.mp4" >/dev/null)
echo "OK $EP"
