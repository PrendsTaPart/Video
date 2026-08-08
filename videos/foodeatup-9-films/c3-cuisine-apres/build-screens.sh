#!/usr/bin/env bash
# Bobines d'écran de C3 · Cuisine après le service.
#
# Mêmes règles que C1 et C2 (NOTES §5 bis.4 et §7) :
#   - une bobine par scène, plus longue que la scène (marge >= 0,15 s) ;
#   - découpe entre 10 % et 65 % de la source, la fin des tutoriels étant un
#     carton marketing ;
#   - coupes franches, pas de fondus enchaînés (NOTES §7.2) ;
#   - 1920x828 -> crop 1920x672 (bandeau incrusté) -> 1560x546 ;
#   - 30 fps, image-clé toutes les 30 images, +faststart.
set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
SRC="$HERE/assets/screens"
OUT="$HERE/../../../studio-video/assets/screens/c3"
TMP="$HERE/work/screens"

mkdir -p "$OUT" "$TMP"

enc=(-c:v libx264 -preset medium -crf 20 -pix_fmt yuv420p
     -r 30 -g 30 -keyint_min 30 -sc_threshold 0 -movflags +faststart)

seg() { # <sortie> <source> <in> <duree>
  ffmpeg -nostdin -v error -ss "$3" -t "$4" -i "$SRC/$2.mp4" \
    -vf "crop=1920:672:0:0,scale=1560:546,fps=30,setsar=1" \
    -an "${enc[@]}" "$TMP/$1.mp4" -y
}

concat_c() { # <sortie> <segments...>
  local out=$1; shift
  local list="$TMP/$out.txt"; : > "$list"
  for s in "$@"; do echo "file '$TMP/$s.mp4'" >> "$list"; done
  ffmpeg -nostdin -v error -f concat -safe 0 -i "$list" "${enc[@]}" "$OUT/$out.mp4" -y
}

# Les bornes viennent des timings réels de la voix (assets/transcript.json).
seg s2  DLC          6.0  16.35   # 2,99 -> 19,08 : les DLC sur les restes
seg s3  ETIQUETTES  22.0   5.75   # 19,08 -> 24,59 : « j'imprime mes étiquettes »
seg s4  STOCK       10.0   9.10   # 24,59 -> 33,46 : pertes et mouvements
seg s5  TRACA       14.0   4.80   # 33,46 -> 38,03 : la traçabilité se referme
seg s7  NETTOYAGE   12.0   6.10   # 45,17 -> 51,05 : les zones de nettoyage
seg s8  PHOTO-IA     4.0  10.70   # 51,05 -> 61,55 : le plan clé du film
seg s9a CONFORMITE  18.0   2.30   # 61,55 -> 65,81 : conformité, puis
seg s9b TEMPERATURE 15.0   2.25   #                  dernier relevé
seg s10 POINTAGE     7.0   5.45   # 65,81 -> 71,00 : la sortie

for n in 2 3 4 5 7 8 10; do cp "$TMP/s$n.mp4" "$OUT/SCENE-$n.mp4"; done
# La voix nomme les deux en enfilade : on coupe sur chaque nom.
concat_c SCENE-9 s9a s9b

echo "--- durée obtenue / durée de scène (la bobine doit dépasser) ---"
declare -A SCENE=([SCENE-2]=16.09 [SCENE-3]=5.51 [SCENE-4]=8.87 [SCENE-5]=4.57
                  [SCENE-7]=5.88 [SCENE-8]=10.50 [SCENE-9]=4.26 [SCENE-10]=5.19)
for f in "$OUT"/SCENE-*.mp4; do
  n=$(basename "$f" .mp4)
  d=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$f")
  awk -v n="$n" -v d="$d" -v s="${SCENE[$n]}" \
    'BEGIN{printf "  %-10s %7.2f s  (scène %5.2f s)  %s\n", n, d, s, (d>=s+0.15 ? "ok" : "MARGE INSUFFISANTE")}'
done
