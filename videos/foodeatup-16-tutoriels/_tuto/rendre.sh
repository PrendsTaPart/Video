#!/usr/bin/env bash
# Rend les seize tutoriels, un par un, dans leur dossier `out/`.
#
# Un par un et non en parallèle : le rendu tient déjà quatre cœurs, et deux
# navigateurs sans tête qui se disputent la mémoire vidéo produisent des
# rendus plus lents *et* des images manquantes.
#
# Chaque film est vérifié aussitôt rendu — durée et nombre d'images. Un rendu
# tronqué se voit à la seconde près sur ces deux chiffres, et ne se voit pas du
# tout si on ne les regarde pas.
set -uo pipefail

STUDIO="/home/user/Video/studio-video"
SERIE="/home/user/Video/videos/foodeatup-16-tutoriels"
cd "$STUDIO"

ok=0; ko=0
for sous in t01 t02 t03 t04 t05 t06 t07 t08 t09 t10 t11 t12 t13 t14 t15 t16; do
  attendu=$(python3 -c "import json;print(json.load(open('$SERIE/$sous/assets/timing.json'))['total'])")
  mkdir -p "$SERIE/$sous/out"

  if ! npx hyperframes render -c "compositions/$sous.html" \
        --video-frame-format png -o "$SERIE/$sous/out/$sous.mp4" >/dev/null 2>&1; then
    echo "  ✗ $sous : rendu en échec"; ko=$((ko+1)); continue
  fi

  mp4="$SERIE/$sous/out/$sous.mp4"
  duree=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$mp4")
  images=$(ffprobe -v error -select_streams v:0 -count_frames \
           -show_entries stream=nb_read_frames -of csv=p=0 "$mp4")
  printf "  ✓ %s  %6.2f s (attendu %6.2f)  %5s images  %s\n" \
    "$sous" "$duree" "$attendu" "$images" "$(du -h "$mp4" | cut -f1)"
  ok=$((ok+1))
done

echo
echo "$ok rendus, $ko échecs."
