#!/usr/bin/env bash
# File d'attente de rendu des neuf films « sans », un à la fois.
#
# Séquentiel et non parallèle : chaque rendu lance déjà ses propres ouvriers
# Chrome, et deux rendus concurrents se sont une fois affamés l'un l'autre
# pendant deux heures et demie sans qu'aucun n'aboutisse.
#
# `--video-frame-format png` : les maquettes d'outils sont des aplats gris et
# du texte fin, exactement ce que la compression JPEG salit.
set -uo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
SERIE="$HERE/.."
STUDIO="$HERE/../../../studio-video"
JOURNAL="$SERIE/_plans-sans/rendus.log"
mkdir -p "$(dirname "$JOURNAL")"

FILMS=(d1s-direction-avant-sans c1s-cuisine-avant-sans c2s-cuisine-pendant-sans
       c3s-cuisine-apres-sans s1s-salle-avant-sans s2s-salle-pendant-sans
       s3s-salle-apres-sans d2s-direction-pendant-sans d3s-direction-apres-sans)

for film in "${FILMS[@]}"; do
  out="$SERIE/$film/out/$film.mp4"
  mkdir -p "$(dirname "$out")"
  echo "=== $film $(date +%H:%M:%S)" | tee -a "$JOURNAL"

  (cd "$STUDIO" && npx hyperframes render . \
      -c "compositions/$film.html" -o "$out" \
      --video-frame-format png --quality high --quiet) >>"$JOURNAL" 2>&1
  code=$?

  if [ $code -ne 0 ]; then
    echo "RENDU ÉCHOUÉ : $film (code $code)" | tee -a "$JOURNAL"
    continue
  fi

  # Contrôle immédiat : un film qui sort défectueux doit être signalé pendant
  # que la file tourne, pas découvert à la fin sur les neuf à la fois.
  (cd "$SERIE" && python3 _serie/qa-film.py "$film") 2>&1 | tee -a "$JOURNAL"
  echo "PRÊT : $film $(date +%H:%M:%S)" | tee -a "$JOURNAL"
done

echo "FILE TERMINÉE $(date +%H:%M:%S)" | tee -a "$JOURNAL"
