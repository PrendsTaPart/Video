#!/usr/bin/env bash
# Contrôle bloquant d'un master. Sort en 1 si un critère échoue.
#   ./qc-episode.sh EP001
set -uo pipefail

EP="${1:?usage: qc-episode.sh EPxxx}"
R="$(cd "$(dirname "$0")/.." && pwd)"
M="$R/dist/tiktok/$EP.mp4"
FAIL=0
ok(){ printf '  \033[32mOK\033[0m   %s\n' "$1"; }
ko(){ printf '  \033[31mECHEC\033[0m %s\n' "$1"; FAIL=1; }

echo "=== Contrôle $EP ==="

D=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$M")
awk -v d="$D" 'BEGIN{exit !(d>29.8 && d<30.2)}' \
  && ok "durée ${D}s (30,0 ±0,2)" || ko "durée ${D}s hors 30,0 ±0,2"

WH=$(ffprobe -v error -select_streams v -show_entries stream=width,height,r_frame_rate -of csv=p=0 "$M")
[ "$WH" = "1080,1920,30/1" ] && ok "format $WH" || ko "format $WH (attendu 1080,1920,30/1)"

EBU=$(ffmpeg -hide_banner -nostats -i "$M" -af ebur128=peak=true -f null - 2>&1)
I=$(echo "$EBU" | grep -A1 "Integrated" | grep "I:" | awk '{print $2}')
P=$(echo "$EBU" | grep -A1 "True peak" | grep "Peak:" | awk '{print $2}')
awk -v i="$I" 'BEGIN{exit !(i>-15 && i<-13)}' \
  && ok "loudness ${I} LUFS (−14 ±1)" || ko "loudness ${I} LUFS hors −14 ±1"
awk -v p="$P" 'BEGIN{exit !(p<=-1)}' \
  && ok "true peak ${P} dBTP (≤ −1)" || ko "true peak ${P} dBTP (> −1)"

# Première frame non noire : elle devient la vignette sur les 5 plateformes.
L=$(ffmpeg -v error -i "$M" -frames:v 1 -vf "scale=64:64,format=gray" -f rawvideo - 2>/dev/null \
    | python3 -c "import sys;d=sys.stdin.buffer.read();print(int(sum(d)/len(d)))")
[ "$L" -ge 12 ] && ok "première frame non noire (luminance $L)" || ko "première frame noire (luminance $L)"

# Logo présent du début à la fin. Il est haut-droite partout, sauf sur le
# segment D (16 → 26 s) où il descend dans le bandeau de marque du bas.
verifie_logo() {  # $1 = seconde, $2 = crop ffmpeg, $3 = libellé
  BL=$(ffmpeg -v error -ss "$1" -i "$M" -frames:v 1 -vf "crop=$2,scale=25:9,format=gray" \
       -f rawvideo - 2>/dev/null | python3 -c "import sys;d=sys.stdin.buffer.read();print(int(sum(d)/len(d)))")
  { [ "$BL" -gt 60 ] && [ "$BL" -lt 200 ]; } \
    && ok "logo présent à $1s ($3)" || ko "logo absent/illisible à $1s ($3, luminance $BL)"
}
for t in 1 15 29; do verifie_logo "$t" "250:93:795:57" "haut-droite"; done
verifie_logo 21 "250:93:415:1777" "bandeau bas"

[ $FAIL -eq 0 ] && echo "=== $EP CONFORME ===" || echo "=== $EP RESTE DANS build/ ==="
exit $FAIL
