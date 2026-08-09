#!/usr/bin/env bash
# Contrôle un film fraîchement rendu, puis le verse au dépôt.
#
# Le contrôle avant le commit, et non après : un rendu tronqué s'ouvre, se joue
# et s'arrête au milieu d'une phrase. Rien ne le signale — ni le code de sortie
# du moteur, ni la lecture des premières secondes. Seule la durée le dit, et il
# faut la comparer à celle que `timing.json` annonce, mesurée segment par
# segment sur la voix off.
#
# Un écart d'une image (0,033 s à trente par seconde) est le bruit normal de
# l'encodage. Au-delà, on ne commite pas.
#
# Usage : _tuto/livrer-film.sh t06
set -euo pipefail

sous="${1:?usage: livrer-film.sh <tNN>}"
SERIE="/home/user/Video/videos/foodeatup-16-tutoriels"
BRANCHE="claude/foodeatup-8-boucles-video-ad8cds"
mp4="$SERIE/$sous/out/$sous.mp4"

[ -f "$mp4" ] || { echo "✗ $sous : pas de film rendu"; exit 1; }

attendu=$(python3 -c "import json;print(json.load(open('$SERIE/$sous/assets/timing.json'))['total'])")
duree=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$mp4")
images=$(ffprobe -v error -select_streams v:0 -count_frames \
         -show_entries stream=nb_read_frames -of csv=p=0 "$mp4")

read -r verdict ligne <<<"$(python3 -c "
a, d, n = $attendu, $duree, $images
e = abs(a - d)
print(('OK' if e <= 0.05 else 'KO'),
      f'$sous · {d:.2f} s (attendu {a:.2f}, écart {e:.3f} s) · {n} images')
")"

echo "  $([ "$verdict" = OK ] && echo ✓ || echo ✗) $ligne"
[ "$verdict" = OK ] || { echo "  écart au-delà d'une image — film non versé"; exit 1; }

titre=$(python3 -c "
import sys; sys.path.insert(0, '$SERIE/_tuto')
from scripts import TUTORIELS
print(next(t['titre_fiche'] for t in TUTORIELS if t['sous'] == '$sous'))
")

cd /home/user/Video
git add "videos/foodeatup-16-tutoriels/$sous/out/$sous.mp4"
git diff --cached --quiet && { echo "  (déjà versé, rien à faire)"; exit 0; }
git commit -q -m "$sous · $titre

$ligne

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01JoNeEF4xS3nc5NjkAzEwv5"

for essai in 1 2 3 4; do
  git push origin "$BRANCHE" && exit 0
  sleep $((2 ** essai))
done
echo "  ✗ poussée en échec après quatre essais"; exit 1
