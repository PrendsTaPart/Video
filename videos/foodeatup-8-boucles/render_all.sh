#!/usr/bin/env bash
# Rend en série les vidéos dont la voix off est complète.
#
# En série et non en parallèle : la capture Playwright est déjà gourmande en CPU
# (une capture d'écran par frame), et lancer plusieurs Chromium ne fait que se
# disputer les mêmes cœurs — pour un temps total identique, mais des logs
# entremêlés et un pic mémoire inutile.
#
# Usage : ./render_all.sh <slug> [<slug>…]        (masters)
#         FORMAT=reel ./render_all.sh <slug>…     (déclinaisons verticales)
set -euo pipefail
cd "$(dirname "$0")"

FORMAT="${FORMAT:-master}"
if [ "$FORMAT" = "reel" ]; then SUF="-reel"; else SUF=""; fi

for slug in "$@"; do
  dossier=$(python3 -c "
import json,sys
m=json.load(open('boucles.json'))
print(next(v['dossier'] for v in m['videos'] if v['slug']=='$slug'))")

  echo "=== $slug ($FORMAT) ==="
  rm -rf "work/${slug}${SUF}"
  node capture.cjs --html "${dossier}/index${SUF}.html" --out "work/${slug}${SUF}" \
    | tail -1
  python3 build.py --slug "$slug" --format "$FORMAT"
  # Les frames pèsent ~2 Go par vidéo : on les jette dès le MP4 encodé, sinon
  # l'espace disque de la session part avant la fin de la série.
  rm -rf "work/${slug}${SUF}"
done

echo "TERMINÉ : $*"
