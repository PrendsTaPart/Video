#!/usr/bin/env bash
# Remonte tous les épisodes déjà montables d'une saison, avec le montage courant.
#
#   ./scripts/remonter-saison.sh 1
#   ./scripts/remonter-saison.sh 1 EP013 EP022     # ou seulement ceux-là
#
# À quoi ça sert
# --------------
# Le montage évolue — un carton refait, une incrustation ajoutée, un raccord
# corrigé. Les masters déjà sortis, eux, ne bougent pas : ils portent l'état du
# montage au jour de leur build. Au bout de quelques semaines une saison n'est
# plus homogène, et ça se voit d'un épisode à l'autre bien plus qu'un défaut
# isolé ne se verrait dans un épisode.
#
# Ce script remonte donc une saison entière d'un coup, en repartant des assets
# d'origine. Il ne génère rien : mêmes clips, mêmes avatars, mêmes voix.
#
# Un épisode dont un asset manque est sauté et listé à la fin — la chaîne ne
# s'arrête jamais sur un épisode incomplet.
set -uo pipefail

SAISON="${1:?usage: remonter-saison.sh <numéro de saison> [EPxxx…]}"
shift || true
R="$(cd "$(dirname "$0")/.." && pwd)"
cd "$R"

if [ "$#" -gt 0 ]; then
  LISTE=("$@")
else
  mapfile -t LISTE < <(python3 -c "
import json, pathlib
eps = []
for f in sorted(pathlib.Path('state/episodes').glob('EP*.json')):
    d = json.loads(f.read_text())
    if d.get('saison') == $SAISON:
        eps.append(d['id'])
print('\n'.join(eps))")
fi

FAITS=(); SAUTES=(); ECHECS=()
for EP in "${LISTE[@]}"; do
  echo
  echo "──────── $EP ────────"
  HOOK="$(python3 -c "
import json
d = json.load(open('state/episodes/$EP.json'))
print(d.get('hook',''))" 2>/dev/null || echo "")"
  CLIP="assets/hooks/$EP.mp4"; [ -f "$CLIP" ] || CLIP="dist/hooks/$EP.mp4"
  if [ -z "$HOOK" ] || [ ! -f "$CLIP" ] || [ ! -f "assets/avatar/$EP.mp4" ] \
     || [ ! -f "assets/software/$EP.mp4" ] || [ ! -f "assets/vo/punchlines/$EP.mp3" ]; then
    echo "  sauté : un asset manque (clip, avatar, screencast ou voix)"
    SAUTES+=("$EP"); continue
  fi
  if ./scripts/build-segment-a.sh "$EP" "$HOOK" && ./scripts/build-episode.sh "$EP"; then
    FAITS+=("$EP")
  else
    ECHECS+=("$EP")
  fi
done

echo
echo "════════ saison $SAISON ════════"
echo "  remontés : ${#FAITS[@]}  ${FAITS[*]:-}"
echo "  sautés   : ${#SAUTES[@]}  ${SAUTES[*]:-}"
echo "  échecs   : ${#ECHECS[@]}  ${ECHECS[*]:-}"
[ "${#ECHECS[@]}" -eq 0 ]
