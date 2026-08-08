#!/usr/bin/env bash
# Bobines d'écran de D3 · Direction après le service.
#
# Neuf étapes en sept scènes : trois d'entre elles (facture, devis,
# e-reporting) tiennent dans une seule bobine, parce que la voix les nomme
# d'une traite — « trois documents, aucune ressaisie ».
#
# WA-FOURN est la seule source de toute la série en 1526x1032 (capture d'un
# téléphone, pas d'un navigateur) : elle a son propre recadrage, calculé pour
# garder le même rapport 2,857 que les autres.
#
# Règles communes : bobine plus longue que sa scène, découpe entre 10 % et
# 65 %, coupes franches, 1560x546, 30 fps, GOP 30.
set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
SRC="$HERE/assets/screens"
OUT="$HERE/../../../studio-video/assets/screens/d3"
TMP="$HERE/work/screens"

mkdir -p "$OUT" "$TMP"

enc=(-c:v libx264 -preset medium -crf 20 -pix_fmt yuv420p
     -r 30 -g 30 -keyint_min 30 -sc_threshold 0 -movflags +faststart)

seg() { # <sortie> <source> <in> <duree> [largeur:hauteur:x:y du recadrage]
  ffmpeg -nostdin -v error -ss "$3" -t "$4" -i "$SRC/$2.mp4" \
    -vf "crop=${5:-1920:672:0:0},scale=1560:546,fps=30,setsar=1" \
    -an "${enc[@]}" "$TMP/$1.mp4" -y
}

concat_c() {
  local out=$1; shift
  local list="$TMP/$out.txt"; : > "$list"
  for s in "$@"; do echo "file '$TMP/$s.mp4'" >> "$list"; done
  ffmpeg -nostdin -v error -f concat -safe 0 -i "$list" "${enc[@]}" "$OUT/$out.mp4" -y
}

# Bornes issues des timings réels de la voix (assets/transcript.json).
seg s2a FACTURE   12.0  3.00   #  8,51 -> 17,19 : une facture,
seg s2b DEVIS     14.0  3.00   #                  un devis,
seg s2c EREPORT   12.0  2.95   #                  l'e-reporting
seg s3  PREDIBOT   5.0  9.40   # 17,19 -> 26,32 : les questions à PrediBot
seg s4  MARKET     6.0  7.55   # 26,32 -> 33,61 : la marketplace de prompts
seg s5a WA-FOURN   8.0  4.60  1526:534:0:150   # 33,61 -> 42,49 : réceptions par
seg s5b WA-STOCK  10.0  4.60                   #   WhatsApp, puis le stock
seg s6  HACCP      8.0  8.30   # 42,49 -> 50,53 : le classeur HACCP exporté
seg s7  STATS     20.0  5.40   # 50,53 -> 55,65 : le chiffre du jour

concat_c SCENE-2 s2a s2b s2c
concat_c SCENE-5 s5a s5b
for n in 3 4 6 7; do cp "$TMP/s$n.mp4" "$OUT/SCENE-$n.mp4"; done

echo "--- durée obtenue / durée de scène (la bobine doit dépasser) ---"
declare -A SCENE=([SCENE-2]=8.68 [SCENE-3]=9.13 [SCENE-4]=7.29
                  [SCENE-5]=8.88 [SCENE-6]=8.04 [SCENE-7]=5.12)
for f in "$OUT"/SCENE-*.mp4; do
  n=$(basename "$f" .mp4)
  d=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$f")
  awk -v n="$n" -v d="$d" -v s="${SCENE[$n]}" \
    'BEGIN{printf "  %-9s %7.2f s  (scène %5.2f s)  %s\n", n, d, s, (d>=s+0.15 ? "ok" : "MARGE INSUFFISANTE")}'
done
