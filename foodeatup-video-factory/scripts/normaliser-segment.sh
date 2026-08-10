#!/usr/bin/env bash
# Cale un segment sur un niveau et un plafond de crête donnés, sans toucher à
# l'image.
#
#   ./normaliser-segment.sh build/EP007_D.mp4 -21 -9
#
# Pourquoi ce script existe : les segments sortaient de leurs montages respectifs
# à des niveaux sans rapport les uns avec les autres — hook à -25,6 LUFS, avatar
# à -13,3, gabarits à -21. Douze décibels d'écart entre le hook et l'avatar, et
# un segment D qui écrêtait à +2,8 dBTP, c'est-à-dire une voix distordue. Le
# montage sonnait comme quatre morceaux collés, pas comme un épisode.
#
# On n'utilise PAS loudnorm ici. loudnorm ride le gain quand il ne peut pas
# atteindre sa cible en linéaire, et ce riding remonte le lit musical dans les
# silences. Un gain constant suivi d'un limiteur préserve les rapports internes
# du mixage : la musique reste sous la voix, l'écart entre les deux ne bouge pas.
set -euo pipefail

F="${1:?usage: normaliser-segment.sh fichier.mp4 [I_cible] [plafond_dBTP]}"
CIBLE="${2:--21}"
PLAFOND="${3:--9}"

mesure() {  # -> "I TP"
  ffmpeg -hide_banner -nostats -i "$1" -af ebur128=peak=true -f null - 2>&1 \
  | sed -n '/Summary/,$p' \
  | awk '/^[[:space:]]+I:/{i=$2} /Peak:/{if(p=="")p=$2} END{print i, p}'
}

read -r I0 TP0 <<<"$(mesure "$F")"
GAIN="$(python3 -c "print(f'{$CIBLE-($I0):.2f}')")"
LIM="$(python3 -c "print(f'{10**($PLAFOND/20):.4f}')")"

TMP="${F%.*}_norm.${F##*.}"
ffmpeg -v error -i "$F" \
 -af "volume=${GAIN}dB,alimiter=limit=$LIM:level=disabled:attack=5:release=60" \
 -map 0:v -map 0:a -c:v copy -c:a aac -b:a 192k -ar 48000 "$TMP" -y

# Le limiteur mange un peu de loudness sur les transitoires. Une seule passe de
# rattrapage suffit : la perte est stable d'un épisode à l'autre.
read -r I1 TP1 <<<"$(mesure "$TMP")"
ECART="$(python3 -c "print(f'{$CIBLE-($I1):.2f}')")"
if python3 -c "import sys;sys.exit(0 if abs($ECART)>0.3 else 1)"; then
  ffmpeg -v error -i "$F" \
   -af "volume=$(python3 -c "print(f'{$GAIN+$ECART:.2f}')")dB,\
alimiter=limit=$LIM:level=disabled:attack=5:release=60" \
   -map 0:v -map 0:a -c:v copy -c:a aac -b:a 192k -ar 48000 "$TMP" -y
  read -r I1 TP1 <<<"$(mesure "$TMP")"
fi

mv "$TMP" "$F"
printf "  niveau : %s LUFS / %s dBTP -> %s LUFS / %s dBTP\n" "$I0" "$TP0" "$I1" "$TP1"
