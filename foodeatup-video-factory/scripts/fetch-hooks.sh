#!/usr/bin/env bash
# Récupère les hooks Higgsfield DÉJÀ générés vers assets/hooks/.
#
# RÉCUPÉRATION SEULE : aucune génération, aucun crédit dépensé. Les URLs
# viennent de content/hooks-higgsfield.json, produit par match-hooks.py à
# partir de l'historique Higgsfield (show_generations).
#
#   ./fetch-hooks.sh              tous les épisodes appariés
#   ./fetch-hooks.sh EP001 EP002  une sélection
#
# Quand un épisode a plusieurs prises, c'est la plus récente qui est prise.
# Pour en choisir une autre, édite content/hooks-higgsfield.json.
set -euo pipefail

R="$(cd "$(dirname "$0")/.." && pwd)"
MANIFESTE="$R/content/hooks-higgsfield.json"
mkdir -p "$R/assets/hooks"

mapfile -t CIBLES < <(
  if [ $# -gt 0 ]; then printf '%s\n' "$@"
  else python3 -c "import json;print('\n'.join(sorted(json.load(open('$MANIFESTE')))))"
  fi
)

ok=0; saute=0; ko=0
for EP in "${CIBLES[@]}"; do
  DEST="$R/assets/hooks/$EP.mp4"
  if [ -s "$DEST" ]; then
    echo "  $EP  déjà présent"
    saute=$((saute + 1)); continue
  fi

  URL="$(python3 - "$MANIFESTE" "$EP" <<'PY'
import json, sys
m = json.load(open(sys.argv[1]))
p = m.get(sys.argv[2]) or []
print(p[0]["url"] if p else "")
PY
)"
  if [ -z "$URL" ]; then
    echo "  $EP  ABSENT de l'historique Higgsfield — voir le rapport"
    ko=$((ko + 1)); continue
  fi

  if curl -sSL --fail --max-time 180 -o "$DEST.part" "$URL"; then
    mv "$DEST.part" "$DEST"
    LU="$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$DEST" 2>/dev/null || echo 0)"
    WH="$(ffprobe -v error -select_streams v -show_entries stream=width,height -of csv=p=0 "$DEST" 2>/dev/null || echo '?')"
    printf "  %s  récupéré  %ss  %s\n" "$EP" "$LU" "$WH"
    ok=$((ok + 1))
  else
    rm -f "$DEST.part"
    echo "  $EP  ÉCHEC réseau"
    ko=$((ko + 1))
  fi
done

echo
echo "récupérés : $ok | déjà là : $saute | en échec : $ko"
