#!/usr/bin/env bash
# Rend un épisode réservé : supprime la réservation et la pousse.
# À utiliser quand on abandonne, ou quand l'épisode est livré et fusionné.
#   ./release-episode.sh EP042
set -euo pipefail

R="$(cd "$(dirname "$0")/.." && pwd)"
EP="${1:?usage: release-episode.sh EPxxx}"
BASE="${FEU_BASE:-claude/foodeatup-video-production-8slc4o}"
CLAIM="$R/state/claims/$EP.json"

[ -e "$CLAIM" ] || { echo "$EP n'est pas réservé."; exit 0; }

OWNER="$(python3 -c "import json;print(json.load(open('$CLAIM'))['owner'])")"
git -C "$R" rm -q "state/claims/$EP.json"
git -C "$R" commit -q -m "Rend $EP (était réservé par $OWNER)"

for i in 1 2 3 4; do
  git -C "$R" push -q origin "HEAD:$BASE" && break
  echo "push rejeté, on rebase et on réessaie ($i/4)"
  git -C "$R" pull -q --rebase origin "$BASE"
  sleep $((2 ** i))
done
echo "$EP rendu."
