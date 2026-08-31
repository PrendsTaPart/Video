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
IMAGES=$(node -p "require('$ROOT/clip-musical/conduite.json').images")

# Qualité de l'image. Les épisodes sont en CRF 18, mais ils durent trente
# secondes ; le clip en dure cent soixante-quinze et enchaîne cent trente et une
# coupes, ce qui coûte cher à encoder. En CRF 18 il sortait à 112,7 Mo et GitHub
# a refusé le dépôt — sa limite est à 100 Mo par fichier. CRF 21 le ramène sous
# la barre sans que la différence se voie sur un téléphone.
CRF=21
LIMITE_MO=100

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
    # 2 % de rab sur le ralenti : `minterpolate` rend systématiquement quelques
    # images de moins que le calcul théorique (332 demandées, 329 rendues sur
    # l'outro), et `-frames:v` ne peut pas inventer ce qui manque. On produit
    # donc un peu trop et on coupe. Deux pour cent d'écart de vitesse sur un
    # plan de vingt secondes au ralenti ne se voient pas ; trois images
    # manquantes en fin de clip, si.
    RAB=$(awk -v r="$RAL" 'BEGIN{printf "%.5f", r*1.02}')
    VF="setpts=$RAB*PTS,minterpolate=fps=30:mi_mode=blend,scale=1080:1920:flags=lanczos,format=yuv420p"
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
  # Une coupe déjà rendue au bon compte d'images est gardée : reprendre un
  # montage ne doit pas coûter dix minutes d'encodage. Le compte est vérifié,
  # pas supposé — un fichier au mauvais compte est refait.
  DEJA=0
  if [ -f "$OUT" ]; then
    EU=$(ffmpeg -nostdin -hide_banner -i "$OUT" -map 0:v -f null - 2>&1 \
         | grep -oE "frame= *[0-9]+" | tail -1 | grep -oE "[0-9]+")
    [ "${EU:-0}" = "$IMG" ] && DEJA=1
  fi
  if [ "$DEJA" = 0 ]; then
    ffmpeg -y -nostdin -loglevel error -ss "$DEB" -t "$LIRE" -i "$ROOT/$SRC" \
      -an -vf "$VF" -frames:v "$IMG" -c:v libx264 -preset slow -crf 18 "$OUT"
  fi
  printf "file 'coupes/c%04d.mkv'\n" "$i" >> "$W/liste.txt"
  [ $((i % 20)) -eq 0 ] && echo "   $i/$N  ($SEC)"
done

echo "→ collage et pose de la chanson"
# Le FILTRE concat, et non le démuxeur. Le démuxeur croit la durée annoncée par
# chaque conteneur : Matroska déclare chaque segment une image plus long qu'il
# n'est, et le suivant démarrait donc une image trop tard — cent trente et une
# fois, soit près de trois secondes. Mesuré à l'image : le pont commençait vers
# 98,5 s au lieu de 96,39.
#
# Le filtre, lui, met bout à bout des suites d'images et refabrique l'horloge.
# Aucune durée de conteneur n'entre dans le calcul, donc aucune dérive possible.
ENTREES=""; CHAINE=""
for i in $(seq 0 $((N - 1))); do
  ENTREES="$ENTREES -i $W/coupes/c$(printf '%04d' "$i").mkv"
  CHAINE="$CHAINE[$i:v]"
done
SORTIE_FONDU=$(awk -v d="$DUREE" 'BEGIN{printf "%.3f", d-2.5}')
# shellcheck disable=SC2086
ffmpeg -y -nostdin -loglevel error $ENTREES -i "$CHANSON" \
  -filter_complex "${CHAINE}concat=n=$N:v=1:a=0,\
fade=t=in:st=0:d=1.2,fade=t=out:st=$SORTIE_FONDU:d=2.5[v]" \
  -af "afade=t=out:st=$SORTIE_FONDU:d=2.5,aresample=48000,aformat=channel_layouts=stereo" \
  -map "[v]" -map "$N:a" -frames:v "$IMAGES" \
  -c:v libx264 -preset slow -crf "$CRF" -c:a aac -b:a 192k \
  -movflags +faststart "$W/monte.mp4"
EUES=$(ffmpeg -nostdin -hide_banner -i "$W/monte.mp4" -map 0:v -f null - 2>&1 \
       | grep -oE "frame= *[0-9]+" | tail -1 | grep -oE "[0-9]+")
echo "   $EUES images pour $IMAGES attendues"
[ "$EUES" = "$IMAGES" ] || { echo "   ✗ compte d'images faux, on s'arrête" >&2; exit 1; }

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

# Le dépôt refuse au-delà de 100 Mo : mieux vaut le savoir ici qu'au push.
MO=$(node -p "(require('fs').statSync('$D/clip-c-est-ma-maison-9x16.mp4').size/1048576).toFixed(1)")
echo "   $MO Mo (limite du dépôt : $LIMITE_MO Mo)"
node -e "if ($MO >= $LIMITE_MO) { console.error('   ✗ trop lourd pour le dépôt, augmenter CRF'); process.exit(1) }"

echo "✅ $D/clip-c-est-ma-maison-9x16.mp4"
ffmpeg -hide_banner -nostdin -i "$D/clip-c-est-ma-maison-9x16.mp4" 2>&1 \
  | grep -E "Duration|Stream #0" | sed 's/^/   /' || true
