#!/usr/bin/env bash
# Vignettes des neuf films « sans », extraites du rendu lui-même.
#
# Une vignette générée par un modèle ne serait pas la vidéo : elle promettrait
# une image que le film ne tient pas. Ici on prend une image du film, dans le
# carton d'ouverture, une seconde après l'apparition du titre — le moment où le
# plan porte à la fois son image et son texte.
#
# Les fichiers produits sont poussés sur la branche, puis déposés sur RapidoCMS
# depuis leur URL brute GitHub (cf. FOODEATUP-TUTORIELS-WORKFLOW §7).
set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
SERIE="$HERE/.."
OUT="$SERIE/_plans-sans/vignettes"
mkdir -p "$OUT"

# film -> instant d'extraction. Le carton d'ouverture commence à 4,20 s et son
# titre entre 0,7 s plus tard ; 6,4 s laisse le sous-titre monter aussi.
INSTANT=6.4

for d in "$SERIE"/[cds][0-9]s-*-sans; do
  film=$(basename "$d")
  mp4="$d/out/$film.mp4"
  [ -s "$mp4" ] || { echo "  ! $film : pas de rendu"; continue; }
  ffmpeg -nostdin -v error -ss "$INSTANT" -i "$mp4" -frames:v 1 \
    -q:v 2 "$OUT/$film-poster.jpg" -y
  printf "  + %-30s %s\n" "$film-poster.jpg" \
    "$(ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=p=0:s=x "$OUT/$film-poster.jpg")"
done
