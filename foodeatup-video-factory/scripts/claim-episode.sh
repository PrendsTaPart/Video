#!/usr/bin/env bash
# Réserve un épisode pour cette session. Le verrou, c'est le push : deux sessions
# qui réservent le même épisode en même temps produisent un push rejeté pour la
# seconde, qui repart chercher un autre épisode.
#
#   ./claim-episode.sh            réserve le premier épisode libre
#   ./claim-episode.sh EP042      réserve un épisode précis
#
# Variable d'environnement FEU_OWNER : identifiant de la session (défaut : user@host).
set -euo pipefail

R="$(cd "$(dirname "$0")/.." && pwd)"
OWNER="${FEU_OWNER:-$(git config user.email 2>/dev/null || echo inconnu)}"
BASE="${FEU_BASE:-$(git -C "$R" rev-parse --abbrev-ref HEAD)}"

git -C "$R" fetch origin "$BASE" --quiet

EP="${1:-}"
if [ -z "$EP" ]; then
  EP="$("$R/scripts/next-episode.sh")"
  [ -n "$EP" ] || { echo "Aucun épisode libre."; exit 1; }
fi

CLAIM="$R/state/claims/$EP.json"
if [ -e "$CLAIM" ]; then
  echo "$EP est déjà réservé par $(python3 -c "import json,sys;print(json.load(open('$CLAIM'))['owner'])")"
  exit 1
fi

mkdir -p "$R/state/claims"
cat > "$CLAIM" <<EOF
{
  "episode": "$EP",
  "owner": "$OWNER",
  "branche": "ep/$EP",
  "reserve_le": "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
}
EOF

git -C "$R" add "state/claims/$EP.json"
git -C "$R" commit -q -m "Réserve $EP pour $OWNER"

# Le push est le point d'arbitrage. S'il est rejeté, quelqu'un a réservé avant nous.
if ! git -C "$R" push -q origin "HEAD:$BASE" 2>/dev/null; then
  echo "Réservation perdue (un autre poste a poussé avant). On annule et on recommence."
  git -C "$R" reset -q --hard HEAD~1
  git -C "$R" pull -q --rebase origin "$BASE"
  exec "$0" ${1:+"$1"}
fi

git -C "$R" checkout -q -B "ep/$EP"
echo "$EP réservé par $OWNER — branche ep/$EP"
echo
python3 - "$R/state/episodes/$EP.json" <<'PY'
import json, sys
e = json.load(open(sys.argv[1], encoding="utf-8"))
print(f"  {e['id']} — {e['titre']}  (saison {e['saison']})")
print(f"  module     : {e['module']} › {e['chapitre']}")
print(f"  drive      : https://drive.google.com/drive/folders/{e['module_drive_id']}")
print(f"  hook       : {e['hook']}")
print(f"  punchline  : {e['vo_punchline']}")
print(f"  heygen     : {e['heygen_script'][:70]}…")
PY
