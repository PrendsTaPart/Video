#!/usr/bin/env bash
# Monte le clip musical de la saison 2 à partir de la conduite.
#
#   ./scripts/clip-montage.sh
#
# Attend :
#   clip-musical/conduite.json          rendue par scripts/clip-timeline.py
#   clip-musical/chanson/*.mp3          la chanson
#   renders/ep{NN}/source/*.mp4         les soixante plans
#
# Produit : clip-musical/dist/clip-c-est-ma-maison-9x16.mp4
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
W="$ROOT/clip-musical/work"; D="$ROOT/clip-musical/dist"
mkdir -p "$W/coupes" "$D"

CHANSON="$ROOT/$(node -p "require('$ROOT/clip-musical/conduite.json').chanson")"
DUREE=$(node -p "require('$ROOT/clip-musical/conduite.json').duree_s")
N=$(node -p "require('$ROOT/clip-musical/conduite.json').coupes")

echo "→ $N coupes"
: > "$W/liste.txt"
for i in $(seq 0 $((N - 1))); do
  read -r SRC DEB DUR RAL SEC IMG < <(node -p "
    const c = require('$ROOT/clip-musical/conduite.json').plans[$i];
    [c.source, c.fenetre_debut, c.fenetre_duree, c.ralenti, c.section, c.images].join(' ')")
  OUT="$W/coupes/c$(printf '%04d' "$i").mkv"
  if [ "$RAL" = "1" ]; then
    # Coupe normale : on découpe et on met à l'échelle, rien d'autre.
    VF="scale=1080:1920:flags=lanczos,fps=30,format=yuv420p"
  else
    # Coupe ralentie — le pont et l'outro. La source est à 24 i/s : étirée sans
    # rien d'autre, elle avance par à-coups (à 2,19× elle tombe à 11 images par
    # seconde réelles). `minterpolate` en mode « blend » fabrique les images
    # manquantes en fondu : c'est plus doux qu'un figé, et sur un plan qui dure
    # vingt secondes sans coupe, c'est exactement le rendu qu'on veut.
    VF="setpts=$RAL*PTS,minterpolate=fps=30:mi_mode=blend,scale=1080:1920:flags=lanczos,format=yuv420p"
  fi
  RALENTI_LU="$RAL"
  # `-ss` et `-t` sont placés AVANT `-i` : ils limitent la lecture de la source.
  # Après `-i`, `-t` tronque la sortie — et le pont ralenti sortait alors à 9,5 s
  # au lieu de 20,8, sans que rien ne le signale.
  #
  # La longueur de la coupe se donne en IMAGES et non en secondes. Une coupe de
  # 0,65 s demandée en secondes sortait à 0,70 : ffmpeg arrondit à l'image
  # supérieure sur une source à 24 i/s, et les cent trente et un arrondis
  # faisaient 4,77 s de retard — au refrain final, l'image ne tombait plus du
  # tout sur la musique. `-frames:v` rend un compte exact, et la conduite a
  # calculé ce compte sur la ligne de temps absolue.
  #
  # On lit un peu plus long que nécessaire (0,4 s) pour que le filtre `fps` ait
  # toujours de quoi remplir le compte demandé.
  if [ "$RALENTI_LU" = "1" ]; then
    LIRE=$(awk -v d="$DUR" 'BEGIN{printf "%.3f", d+0.4}')
  else
    LIRE="$DUR"   # une coupe ralentie lit exactement sa fenêtre, sinon la vitesse est fausse
  fi
  ffmpeg -y -nostdin -loglevel error -ss "$DEB" -t "$LIRE" -i "$ROOT/$SRC" \
    -an -vf "$VF" -frames:v "$IMG" -c:v libx264 -preset slow -crf 18 "$OUT"
  printf "file 'coupes/c%04d.mkv'\n" "$i" >> "$W/liste.txt"
  [ $((i % 20)) -eq 0 ] && echo "   $i/$N  ($SEC)"
done

echo "→ collage"
# Matroska sans piste son d'un bout à l'autre : la seule piste audio du clip est
# la chanson, posée en une fois à la fin. Aucun arrondi de trame ne peut donc
# décaler l'image, contrairement au collage de segments sonorisés.
ffmpeg -y -nostdin -loglevel error -f concat -safe 0 -i "$W/liste.txt" -c copy "$W/image.mkv"
IMAGE_TOTALE=$({ ffmpeg -hide_banner -nostdin -i "$W/image.mkv" 2>&1 || true; } \
  | grep -oE "Duration: [0-9:.]+" | head -1 | cut -d' ' -f2 | awk -F: '{printf "%.3f", $1*3600+$2*60+$3}')
echo "   image $IMAGE_TOTALE s / chanson $DUREE s"

echo "→ la chanson, l'ouverture et le fondu final"
SORTIE_FONDU=$(awk -v d="$DUREE" 'BEGIN{printf "%.3f", d-2.5}')
ffmpeg -y -nostdin -loglevel error -i "$W/image.mkv" -i "$CHANSON" \
  -vf "fade=t=in:st=0:d=1.2,fade=t=out:st=$SORTIE_FONDU:d=2.5" \
  -af "afade=t=out:st=$SORTIE_FONDU:d=2.5,aresample=48000,aformat=channel_layouts=stereo" \
  -map 0:v -map 1:a -c:v libx264 -preset slow -crf 18 -c:a aac -b:a 192k \
  -shortest -movflags +faststart "$W/monte.mp4"

echo "→ niveau"
# La chanson sort de Suno déjà masterisée ; on ne la renormalise pas, on la
# rapproche seulement du niveau de la saison pour qu'un clip ne hurle pas après
# un épisode. Jamais vers le haut : le gain est plafonné à 0 dB.
CIBLE=-15.7
ACTUEL=$(ffmpeg -hide_banner -nostdin -nostats -i "$W/monte.mp4" -af ebur128=framelog=quiet -f null - 2>&1 \
  | grep -m1 -A1 "Integrated" | tail -1 | grep -oE -- "-?[0-9.]+")
GAIN=$(node -p "Math.min(0, ($CIBLE) - ($ACTUEL)).toFixed(2)")
echo "   $ACTUEL LUFS → ${GAIN} dB → cible $CIBLE"
ffmpeg -y -nostdin -loglevel error -i "$W/monte.mp4" -af "volume=${GAIN}dB" \
  -c:v copy -c:a aac -b:a 192k -movflags +faststart "$D/clip-c-est-ma-maison-9x16.mp4"

echo "→ vignette : la première image du refrain final"
T=$(node -p "require('$ROOT/clip-musical/conduite.json').plans.find(p=>p.section==='refrain-final').t")
ffmpeg -y -nostdin -loglevel error -ss "$T" -i "$D/clip-c-est-ma-maison-9x16.mp4" \
  -frames:v 1 "$D/clip-c-est-ma-maison-vignette.png"

echo "✅ $D/clip-c-est-ma-maison-9x16.mp4"
ffmpeg -hide_banner -nostdin -i "$D/clip-c-est-ma-maison-9x16.mp4" 2>&1 \
  | grep -E "Duration|Stream #0" | sed 's/^/   /' || true
