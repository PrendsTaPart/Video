#!/usr/bin/env bash
# Bobines d'écran de S3 · Salle après le service.
#
# Le film le plus pauvre en captures de la série : trois de ses sept étapes
# relèvent du module Caisse POS, qui n'est pas tourné. Elles ne sont pas pour
# autant escamotées —
#   - les deux clôtures de caisse passent sur un PLAN TOURNÉ (l'imprimante
#     thermique qui déroule le ticket Z), parce que le ticket Z est un objet
#     physique et qu'un plan réel vaut mieux qu'un schéma ;
#   - les écarts de caisse passent en schéma animé, parce que le sujet est un
#     rapprochement de chiffres, que rien ne filme.
#
# AVIS n'est utilisable que jusqu'à ~26 s (60 % de la source) : son carton de
# prompt Claude arrive avant la limite habituelle des 65 %. Vérifié.
#
# Règles communes : bobine plus longue que sa scène, coupes franches,
# 1920x828 -> 1920x672 -> 1560x546, 30 fps, image-clé toutes les 30 images.
set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
SRC="$HERE/assets/screens"
OUT="$HERE/../../../studio-video/assets/screens/s3"
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
seg s4a NETTOYAGE 12.0  3.10   # 22,77 -> 28,88 : les zones de nettoyage,
seg s4b POINTAGE   7.0  3.30   #                  puis la coupure pointée
seg s6  AVIS       6.0 10.15   # 36,68 -> 46,60 : les avis de la journée
seg s7  POINTAGE  20.0  5.10   # 46,60 -> 51,50 : la sortie pointée

concat_c SCENE-4 s4a s4b
cp "$TMP/s6.mp4" "$OUT/SCENE-6.mp4"
cp "$TMP/s7.mp4" "$OUT/SCENE-7.mp4"

echo "--- durée obtenue / durée de scène (la bobine doit dépasser) ---"
declare -A SCENE=([SCENE-4]=6.11 [SCENE-6]=9.92 [SCENE-7]=4.90)
for f in "$OUT"/SCENE-*.mp4; do
  n=$(basename "$f" .mp4)
  d=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$f")
  awk -v n="$n" -v d="$d" -v s="${SCENE[$n]}" \
    'BEGIN{printf "  %-9s %7.2f s  (scène %5.2f s)  %s\n", n, d, s, (d>=s+0.15 ? "ok" : "MARGE INSUFFISANTE")}'
done
