#!/usr/bin/env bash
# Bobines d'écran de D1 · Direction avant le service.
#
# Le film le plus dense de la série : 14 étapes en 72 secondes. Il tient
# parce que les étapes s'enchaînent par blocs — achats, réception,
# comptabilité, équipe — et que chaque bobine enchaîne deux ou trois écrans
# du même bloc plutôt que d'en isoler un.
#
# Une seule étape n'a aucune fiche (le traitement des congés, 10h50) : elle
# passe en schéma animé, comme sur S1 et S2.
#
# Règles communes : bobine plus longue que sa scène, découpe entre 10 % et
# 65 % de la source (plafond, pas garantie — vérifier), coupes franches,
# 1920x828 -> 1920x672 -> 1560x546, 30 fps, image-clé toutes les 30 images.
set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
SRC="$HERE/assets/screens"
OUT="$HERE/../../../studio-video/assets/screens/d1"
TMP="$HERE/work/screens"

mkdir -p "$OUT" "$TMP"

enc=(-c:v libx264 -preset medium -crf 20 -pix_fmt yuv420p
     -r 30 -g 30 -keyint_min 30 -sc_threshold 0 -movflags +faststart)

seg() {
  ffmpeg -nostdin -v error -ss "$3" -t "$4" -i "$SRC/$2.mp4" \
    -vf "crop=1920:672:0:0,scale=1560:546,fps=30,setsar=1" \
    -an "${enc[@]}" "$TMP/$1.mp4" -y
}

concat_c() {
  local out=$1; shift
  local list="$TMP/$out.txt"; : > "$list"
  for s in "$@"; do echo "file '$TMP/$s.mp4'" >> "$list"; done
  ffmpeg -nostdin -v error -f concat -safe 0 -i "$list" "${enc[@]}" "$OUT/$out.mp4" -y
}

# Bornes issues des timings réels de la voix (assets/transcript.json).
seg s2a PREDIBOT     8.0  6.10   #  7,67 -> 19,51 : PrediBot annonce,
seg s2b STOCKVISION  8.0  6.10   #                  StockVision prévoit
seg s3a BESOINS      8.0  4.10   # 19,51 -> 27,41 : les besoins déduits,
seg s3b COURSES     10.0  4.10   #                  la liste qui se remplit
seg s4a FOURNISSEUR 10.0  2.75   # 27,41 -> 35,27 : commande fournisseur,
seg s4b LIVRAISONS   6.0  2.75   #                  suivi des livraisons,
seg s4c BL          12.0  2.75   #                  validation du BL
seg s5a FACTURES    10.0  3.90   # 35,27 -> 42,75 : les factures classées,
seg s5b RELIER      10.0  3.90   #                  reliées aux livraisons
seg s6a TACHES       8.0  4.30   # 42,75 -> 50,95 : les tâches assignées,
seg s6b PLANNING    10.0  4.30   #                  le planning publié
seg s8  POINTAGES    6.0  7.80   # 55,71 -> 63,27 : les pointages vérifiés

concat_c SCENE-2 s2a s2b
concat_c SCENE-3 s3a s3b
concat_c SCENE-4 s4a s4b s4c
concat_c SCENE-5 s5a s5b
concat_c SCENE-6 s6a s6b
cp "$TMP/s8.mp4" "$OUT/SCENE-8.mp4"

echo "--- durée obtenue / durée de scène (la bobine doit dépasser) ---"
declare -A SCENE=([SCENE-2]=11.84 [SCENE-3]=7.90 [SCENE-4]=7.86
                  [SCENE-5]=7.48 [SCENE-6]=8.20 [SCENE-8]=7.56)
for f in "$OUT"/SCENE-*.mp4; do
  n=$(basename "$f" .mp4)
  d=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$f")
  awk -v n="$n" -v d="$d" -v s="${SCENE[$n]}" \
    'BEGIN{printf "  %-9s %7.2f s  (scène %5.2f s)  %s\n", n, d, s, (d>=s+0.15 ? "ok" : "MARGE INSUFFISANTE")}'
done
