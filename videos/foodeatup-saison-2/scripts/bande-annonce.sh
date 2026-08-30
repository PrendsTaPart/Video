#!/usr/bin/env bash
# Monte la bande-annonce de la saison 2 : carton d'ouverture + 30 extraits + carton de fin.
#
#   ./scripts/bande-annonce.sh
#
# Attend :
#   renders/ep{NN}/source/ep{NN}-scene{1,2}.mp4     les soixante plans de la saison
#   renders/bande-annonce/work/carton-{ouverture,fin}.mp4   rendus par bande-annonce.mjs
#   renders/bande-annonce/work/vo/vo.wav            la voix off de la bande-annonce, normalisée
#
# Produit : renders/bande-annonce/foodeatup-saison-2-bande-annonce.mp4
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DIR="$ROOT/renders/bande-annonce"; W="$DIR/work"; SFX="$ROOT/assets/sfx"
X="$W/extraits"; mkdir -p "$X"

# Durée d'un extrait. Trente extraits à 0,70 s font 21 s : assez pour reconnaître
# un gag, trop court pour que l'œil s'installe — c'est le rythme d'une annonce.
EXT=0.70
# `bc` répond « .675 » sans le zéro de tête et ffmpeg refuse cette durée :
# on calcule le départ du fondu de sortie une fois pour toutes, en awk.
FADEOUT=$(awk -v e="$EXT" 'BEGIN{printf "%.3f", e-0.025}')

# Où couper dans chaque épisode. On alterne :
#   scène 1 à 5,0 s  → le milieu de l'action, un plan large
#   scène 2 à 8,0 s  → la chute, souvent un regard caméra
# Alterner évite trente gros plans à la suite. Les épisodes 12 et 16 sont forcés
# sur la scène 1 : leurs scènes 2 portent les défauts signalés (rupture de tenue,
# gros plan sur le ticket) et n'ont pas été redemandées à Higgsfield.
choisir() {
  case "$1" in
    12|16) echo "1 5.0" ;;
    *) if [ $((10#$1 % 2)) -eq 1 ]; then echo "1 5.0"; else echo "2 8.0"; fi ;;
  esac
}

echo "→ trente extraits de ${EXT}s"
: > "$W/liste.txt"
for i in $(seq -w 1 30); do
  read -r SC T < <(choisir "$i")
  SRC="$ROOT/renders/ep$i/source/ep$i-scene$SC.mp4"
  [ -f "$SRC" ] || { echo "manque $SRC" >&2; exit 1; }
  # Le fondu audio de 25 ms de chaque côté évite le clic de coupe ; l'image, elle,
  # coupe net — c'est ce qui donne le rythme.
  ffmpeg -y -nostdin -loglevel error -ss "$T" -i "$SRC" -t "$EXT" \
    -vf "scale=1080:1920:flags=lanczos,fps=30,format=yuv420p" \
    -af "aresample=48000,aformat=channel_layouts=stereo,afade=t=in:st=0:d=0.025,afade=t=out:st=$FADEOUT:d=0.025" \
    -c:v libx264 -preset slow -crf 18 -c:a aac -b:a 192k -video_track_timescale 15360 \
    "$X/e$i.mp4"
  printf "file '%s'\n" "extraits/e$i.mp4" >> "$W/liste.txt"
done

echo "→ la bobine des extraits"
ffmpeg -y -nostdin -loglevel error -f concat -safe 0 -i "$W/liste.txt" -c copy "$W/bobine.mp4"
BOB=$({ ffmpeg -hide_banner -nostdin -i "$W/bobine.mp4" 2>&1 || true; } \
  | grep -oE "Duration: [0-9:.]+" | head -1 | cut -d' ' -f2 | awk -F: '{printf "%.3f", $1*3600+$2*60+$3}')
echo "   $BOB s"

echo "→ les cartons, à l'image et au son"
# Les cartons sortent muets de Playwright : on leur colle une piste silencieuse
# pour que la concaténation garde un flux audio continu.
carton() { ffmpeg -y -nostdin -loglevel error -i "$W/carton-$1.mp4" \
  -f lavfi -i "anullsrc=r=48000:cl=stereo" -c:v copy -c:a aac -b:a 192k -shortest "$W/carton-$1-son.mp4"; }
carton ouverture; carton fin

printf "file '%s'\n" carton-ouverture-son.mp4 bobine.mp4 carton-fin-son.mp4 > "$W/final.txt"
ffmpeg -y -nostdin -loglevel error -f concat -safe 0 -i "$W/final.txt" -c copy "$W/brut.mp4"

echo "→ la voix off, posée à cheval sur les deux derniers extraits et le carton de fin"
VODUR=$({ ffmpeg -hide_banner -nostdin -i "$W/vo/vo.wav" 2>&1 || true; } \
  | grep -oE "Duration: [0-9:.]+" | head -1 | cut -d' ' -f2 | awk -F: '{printf "%.3f", $1*3600+$2*60+$3}')
TOT=$({ ffmpeg -hide_banner -nostdin -i "$W/brut.mp4" 2>&1 || true; } \
  | grep -oE "Duration: [0-9:.]+" | head -1 | cut -d' ' -f2 | awk -F: '{printf "%.3f", $1*3600+$2*60+$3}')
# La voix finit une demi-seconde avant la fin, le temps que le logo respire.
DEBUT=$(node -p "Math.round((($TOT) - 0.5 - ($VODUR)) * 1000)")
echo "   voix ${VODUR}s dans ${TOT}s → démarre à ${DEBUT}ms"

# Sous la voix, le collage des extraits descend de 11 dB : on doit entendre la
# phrase, pas la deviner. Le whoosh marque l'entrée du carton de fin.
FIN_MS=$(node -p "Math.round((2.0 + $BOB) * 1000)")
ffmpeg -y -nostdin -loglevel error -i "$W/brut.mp4" -i "$W/vo/vo.wav" -i "$SFX/whoosh.wav" \
  -filter_complex "\
[0:a]volume=enable='gte(t,${DEBUT}/1000)':volume=0.28,aresample=48000[bed];\
[1:a]adelay=${DEBUT}|${DEBUT},volume=1.05[vo];\
[2:a]adelay=${FIN_MS}|${FIN_MS},volume=0.5[wh];\
[bed][vo][wh]amix=inputs=3:normalize=0:duration=first,\
alimiter=limit=0.92,aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo[out]" \
  -map 0:v -map "[out]" -c:v copy -c:a aac -b:a 192k "$W/monte.mp4"

echo "→ normalisation à -16 LUFS (loudnorm deux passes, gain linéaire)"
MES=$(ffmpeg -hide_banner -nostdin -nostats -i "$W/monte.mp4" \
  -af loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json -f null - 2>&1 | sed -n '/^{/,/^}/p')
read -r MI MTP MLRA MTHR < <(node -p "const m=$MES;[m.input_i,m.input_tp,m.input_lra,m.input_thresh].join(' ')")
echo "   avant : $MI LUFS / crête $MTP dBTP"
ffmpeg -y -nostdin -loglevel error -i "$W/monte.mp4" \
  -af "loudnorm=I=-16:TP=-1.5:LRA=11:measured_I=$MI:measured_TP=$MTP:measured_LRA=$MLRA:measured_thresh=$MTHR:linear=true,aresample=48000" \
  -c:v copy -c:a aac -b:a 192k "$W/normalise.mp4"

# Contrôle au mètre, et non sur parole. La mesure de loudnorm et celle d'ebur128
# ne tombent pas exactement au même endroit : sur les trente épisodes l'écart est
# constant et sans conséquence, mais ici il faisait sortir la bande-annonce
# ~1 dB au-dessus d'eux — une annonce qui crie plus fort que la série qu'elle
# annonce. On rattrape le reliquat, jamais vers le haut : le gain est plafonné à
# 0 dB pour que la crête reste sous -1,5 dBTP.
APRES=$(ffmpeg -hide_banner -nostdin -nostats -i "$W/normalise.mp4" -af ebur128=framelog=quiet -f null - 2>&1 \
  | grep -m1 -A1 "Integrated" | tail -1 | grep -oE -- "-?[0-9.]+")
CIBLE=-15.7   # la moyenne ebur128 des trente masters de la saison
RETOUCHE=$(node -p "Math.min(0, ($CIBLE) - ($APRES)).toFixed(2)")
echo "   après : $APRES LUFS (ebur128) → retouche ${RETOUCHE} dB → cible $CIBLE"
ffmpeg -y -nostdin -loglevel error -i "$W/normalise.mp4" -af "volume=${RETOUCHE}dB" \
  -c:v copy -c:a aac -b:a 192k "$DIR/foodeatup-saison-2-bande-annonce.mp4"

# Vignette : l'image du carton d'ouverture une fois le titre installé.
ffmpeg -y -nostdin -loglevel error -i "$W/cartons/f0045.png" -frames:v 1 "$DIR/bande-annonce-thumb.png"

echo "✅ $DIR/foodeatup-saison-2-bande-annonce.mp4"
ffmpeg -hide_banner -nostdin -i "$DIR/foodeatup-saison-2-bande-annonce.mp4" 2>&1 | grep -E "Duration|Stream #0:0" | sed 's/^/   /' || true
