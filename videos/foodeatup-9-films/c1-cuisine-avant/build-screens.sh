#!/usr/bin/env bash
# Bobines d'écran de C1 · Cuisine avant le service.
#
# Une bobine par scène, à la durée EXACTE de la scène. C'est la règle qui a
# fait rater le premier montage : dès qu'un clip s'arrête, HyperFrames cesse
# de le peindre et c'est le fond #0F1A23 du cadre qui reste — la moitié des
# plans étaient un rectangle noir. Quand une scène est plus longue qu'un
# extrait lisible, on enchaîne un deuxième écran, on n'étire pas le premier.
#
# Découpe : uniquement entre 10 % et 65 % de la source. Les tutoriels se
# terminent tous par un carton marketing ou une carte de prompt Claude.
#
# Recadrage : les rushes sont en 1920x828 avec un bandeau de sous-titre
# incrusté en bas. On coupe 156 px par le bas -> 1920x672, puis 1560x546
# pour coller à la largeur du cadre tablette (1560 px, cf. NOTES §5 bis.2).
# ECRAN-02 est le seul en 1920x1020 (capture navigateur) : on y prend une
# fenêtre de 672 px sous le chrome du navigateur.
#
# Encodage : 30 fps, une image-clé toutes les 30 images, +faststart.
# NON NÉGOCIABLE. HyperFrames se déplace image par image dans les vidéos
# incrustées ; avec le GOP par défaut (250) les images-clés tombent toutes
# les 6 à 10 s, le décodeur ne peut pas se positionner et le cadre gèle ou
# reste éteint. C'est ce qui a produit les plans noirs de la scène 2 au
# premier rendu — le lint ne le voit pas, seul le log de rendu le signale
# (« has sparse keyframes »).
set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
SRC="$HERE/assets/screens"
OUT="$HERE/../../../studio-video/assets/screens/c1"
TMP="$HERE/work/screens"
XF=0.35 # fondu enchaîné entre deux écrans d'une même scène

mkdir -p "$OUT" "$TMP"

# GOP de 30 images = une image-clé toutes les secondes : HyperFrames peut se
# positionner n'importe où sans que le cadre gèle.
enc=(-c:v libx264 -preset medium -crf 20 -pix_fmt yuv420p
     -r 30 -g 30 -keyint_min 30 -sc_threshold 0 -movflags +faststart)

# seg <sortie> <source> <in> <duree> [crop_y]
seg() {
  local out=$1 src=$2 ss=$3 d=$4 cy=${5:-0}
  ffmpeg -nostdin -v error -ss "$ss" -t "$d" -i "$SRC/$src.mp4" \
    -vf "crop=1920:672:0:$cy,scale=1560:546,fps=30,setsar=1" \
    -an "${enc[@]}" "$TMP/$out.mp4" -y
}

# --- Scène 2 · ouverture de poste (12,77 s) --------------------------------
# « Je pointe. Je récupère mes tâches. Je relève mes températures. »
seg s2a ECRAN-01 7.0  4.49
seg s2b ECRAN-02 10.0 4.49 260
seg s2c ECRAN-03 13.0 4.60

# --- Scène 3 · réception (16,13 s) -----------------------------------------
# « Je valide. Je scanne l'EAN et la DLC. La facture part au scan. »
seg s3a ECRAN-04 21.0 4.50
seg s3b ECRAN-05 18.0 6.33
seg s3c ECRAN-06 34.0 6.20

# --- Scène 4 · Jarvis vocal (9,78 s) ---------------------------------------
seg s4a ECRAN-07 10.0 10.00

# --- Scène 5 · production (8,47 s) -----------------------------------------
# « Mes fiches techniques du jour. Ma production. »
seg s5a ECRAN-08 16.0 4.41
seg s5b ECRAN-09 9.0  4.56

# --- Scène 6 · étiquetage (10,15 s) ----------------------------------------
seg s6a ECRAN-10 22.0 10.35

# --- Scène 7 · validation (8,97 s) -----------------------------------------
# « Je valide ma production, je sonde mes plats. »
seg s7a ECRAN-11 8.0  4.66
seg s7b ECRAN-12 18.0 4.81

# Fondu enchaîné entre écrans : la coupe franche entre deux interfaces
# différentes se lit comme un bug ; 350 ms suffisent à la faire passer.
xfade3() { # <sortie> <a> <b> <c> <dA> <dB>
  ffmpeg -nostdin -v error -i "$TMP/$2.mp4" -i "$TMP/$3.mp4" -i "$TMP/$4.mp4" \
    -filter_complex \
    "[0][1]xfade=transition=fade:duration=$XF:offset=$(echo "$5-$XF" | bc)[ab];\
     [ab][2]xfade=transition=fade:duration=$XF:offset=$(echo "$5+$6-2*$XF" | bc)" \
    "${enc[@]}" "$OUT/$1.mp4" -y
}
xfade2() { # <sortie> <a> <b> <dA>
  ffmpeg -nostdin -v error -i "$TMP/$2.mp4" -i "$TMP/$3.mp4" \
    -filter_complex "[0][1]xfade=transition=fade:duration=$XF:offset=$(echo "$4-$XF" | bc)" \
    "${enc[@]}" "$OUT/$1.mp4" -y
}

xfade3 SCENE-2 s2a s2b s2c 4.49 4.49
xfade3 SCENE-3 s3a s3b s3c 4.50 6.33
cp "$TMP/s4a.mp4" "$OUT/SCENE-4.mp4"
xfade2 SCENE-5 s5a s5b 4.41
cp "$TMP/s6a.mp4" "$OUT/SCENE-6.mp4"
xfade2 SCENE-7 s7a s7b 4.66

echo "--- durées obtenues (doivent égaler les data-duration des scènes) ---"
for f in "$OUT"/SCENE-*.mp4; do
  printf "%-12s " "$(basename "$f")"
  ffprobe -v error -show_entries format=duration -of csv=p=0 "$f"
done
