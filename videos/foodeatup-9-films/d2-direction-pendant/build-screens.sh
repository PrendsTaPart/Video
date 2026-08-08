#!/usr/bin/env bash
# Bobines d'écran de D2 · Direction pendant le service.
#
# Six étapes, une par scène : c'est le film le moins dense de la série, et
# c'est cohérent avec son sujet — le directeur ne fait pas des gestes pendant
# le service, il regarde ce que la machine a préparé.
#
# Règles communes (NOTES §5 bis.4 et §7) : bobine plus longue que sa scène,
# découpe entre 10 % et 65 % de la source — plafond, pas garantie, vérifier —,
# coupes franches, 1920x828 -> 1920x672 -> 1560x546, 30 fps, GOP 30.
set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
SRC="$HERE/assets/screens"
OUT="$HERE/../../../studio-video/assets/screens/d2"
TMP="$HERE/work/screens"

mkdir -p "$OUT" "$TMP"

enc=(-c:v libx264 -preset medium -crf 20 -pix_fmt yuv420p
     -r 30 -g 30 -keyint_min 30 -sc_threshold 0 -movflags +faststart)

seg() {
  ffmpeg -nostdin -v error -ss "$3" -t "$4" -i "$SRC/$2.mp4" \
    -vf "crop=1920:672:0:0,scale=1560:546,fps=30,setsar=1" \
    -an "${enc[@]}" "$OUT/$1.mp4" -y
}

# Bornes issues des timings réels de la voix (assets/transcript.json).
seg SCENE-2 IRIS      10.0  8.60   # 11,63 -> 19,98 : le calendrier d'Iris
seg SCENE-3 DORMANTS   8.0  8.90   # 19,98 -> 28,58 : les stocks dormants
seg SCENE-4 CAMPAGNE  12.0  7.60   # 28,58 -> 35,91 : la campagne écrite par l'IA
seg SCENE-5 CREDITS    6.0  5.70   # 35,91 -> 41,28 : les crédits SMS et WhatsApp
seg SCENE-6 AVIS       5.0  9.20   # 41,28 -> 50,23 : les avis Google synchronisés
seg SCENE-7 STATS      8.0  7.90   # 50,23 -> 57,89 : le service en direct

echo "--- durée obtenue / durée de scène (la bobine doit dépasser) ---"
declare -A SCENE=([SCENE-2]=8.35 [SCENE-3]=8.60 [SCENE-4]=7.33
                  [SCENE-5]=5.37 [SCENE-6]=8.95 [SCENE-7]=7.66)
for f in "$OUT"/SCENE-*.mp4; do
  n=$(basename "$f" .mp4)
  d=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$f")
  awk -v n="$n" -v d="$d" -v s="${SCENE[$n]}" \
    'BEGIN{printf "  %-9s %7.2f s  (scène %5.2f s)  %s\n", n, d, s, (d>=s+0.15 ? "ok" : "MARGE INSUFFISANTE")}'
done
