#!/usr/bin/env bash
# Monte un épisode de 30,0 s à partir d'assets DÉJÀ produits.
# Aucune génération : ni Higgsfield, ni HeyGen, ni image. Uniquement ffmpeg local.
#
#   ./build-episode.sh EP001
#
# Attendus :
#   assets/hooks/EPxxx.mp4       clip Higgsfield récupéré (7 s utiles)
#   assets/avatar/EPxxx.mp4      segment HeyGen déposé à la main (<= 12 s, avec audio)
#   assets/software/EPxxx.mp4    10 s extraites d'un tuto Drive
#   build/EPxxx_A.mp4            segment A monté (hook + texte + punchline)
# Les gabarits templates/COMMUN_sting_BC.mp4 et templates/COMMUN_E.mp4 (13 s au
# total) sont identiques sur les 150 : ne jamais les régénérer par épisode.
set -euo pipefail

EP="${1:?usage: build-episode.sh EPxxx [--segment-d]}"
# --segment-d : monte le segment D seul et s'arrête. Sert à valider le cadrage
# avant que le hook Higgsfield soit disponible.
SEUL_D="${2:-}"
R="$(cd "$(dirname "$0")/.." && pwd)"

SABLE="0xFAF6E3"   # fond de charte FoodEatUp, relevé sur le master de référence
LOGO_X=795         # position du badge, identique sur toute la durée
LOGO_Y=57
AV_CROP_Y=30       # décalage du crop avatar : garde la toque, coupe bas sur le buste
AV_H=960           # avatar : 2,5/5 de l'écran
SOFT_H=768         # logiciel : 2/5
BAND_H=192         # bandeau de marque : 0,5/5, le logo y est centré
BED_GAIN=0.224     # -13 dB : cale la musique sur le plancher -28 dBFS de la référence
SFX_GAIN=2.0       # +6 dB : whoosh audible sous la voix

# --- Calage de l'avatar sur le créneau de 10 s --------------------------------
# L'avatar fait rarement 10,000 s. Deux cas, deux traitements :
#   plus court -> dernière frame clonée, la musique tient le fond
#   plus long  -> atempo sur la plage de parole utile (hauteur préservée)
# On mesure la parole réelle, pas la durée du fichier : HeyGen laisse du silence
# en tête et en queue, et l'accélérer serait accélérer du vide.
LECTURE="$(ffmpeg -v error -i "$R/assets/avatar/$EP.mp4" -ac 1 -ar 16000 -f s16le - 2>/dev/null | python3 -c "
import sys,struct,math
d=sys.stdin.buffer.read();n=len(d)//2;s=struct.unpack('<%dh'%n,d[:n*2])
SR,W=16000,800
lv=[]
for i in range(0,n,W):
    ch=s[i:i+W]
    if len(ch)<W//2: break
    r=math.sqrt(sum(x*x for x in ch)/len(ch))
    lv.append(20*math.log10(r/32768+1e-12))
idx=[i for i,v in enumerate(lv) if v>-45]
print(f'{idx[0]*0.05:.2f} {(idx[-1]+1)*0.05:.2f}' if idx else '0 0')")"
DEBUT="$(echo "$LECTURE" | cut -d' ' -f1)"
FIN="$(echo "$LECTURE" | cut -d' ' -f2)"
UTILE="$(python3 -c "print(f'{max(0.1,$FIN-$DEBUT):.3f}')")"
TEMPO="$(python3 -c "print(f'{max(1.0,$UTILE/10.0):.4f}')")"
echo "  avatar : parole ${DEBUT}s → ${FIN}s (${UTILE}s utiles), atempo ${TEMPO}"

# --- Segment D : avatar 45 % (864 px) au-dessus du logiciel 55 % (1056 px) -----
# Le screencast n'est JAMAIS rogné : il est padé sur le fond sable.
# L'avatar est plus court que 10 s -> dernière frame clonée, audio complété en silence.
# La voix change ici (ElevenLabs -> HeyGen) : fondu sable de 0,35 s + whoosh sur la coupe.
# Le lit musical couvre les 10 s, sinon le segment sonne mort face aux voisins.
ffmpeg -v error \
 -i "$R/assets/avatar/$EP.mp4" \
 -i "$R/assets/software/$EP.mp4" \
 -i "$R/templates/logo_foodeatup.png" \
 -i "$R/templates/bgm.mp3" \
 -i "$R/templates/sfx_transition.mp3" \
 -filter_complex "\
 [0:v]trim=start=$DEBUT,setpts=(PTS-STARTPTS)/$TEMPO,fps=30,\
crop=1080:$AV_H:0:$AV_CROP_Y,tpad=stop_mode=clone:stop_duration=3,\
trim=0:10,setpts=PTS-STARTPTS[top];\
 [1:v]fps=30,scale=1080:$SOFT_H:force_original_aspect_ratio=decrease,\
pad=1080:$SOFT_H:(ow-iw)/2:(oh-ih)/2:color=$SABLE[mid];\
 color=c=$SABLE:s=1080x$BAND_H:r=30,trim=0:10[band];\
 [top][mid][band]vstack=inputs=3[stack];\
 [stack][2:v]overlay=(W-w)/2:H-$BAND_H+(($BAND_H-h)/2):format=auto[ov];\
 [ov]fade=t=in:st=0:d=0.35:color=$SABLE,\
fade=t=out:st=9.70:d=0.30:color=$SABLE,format=yuv420p[v];\
 [0:a]atrim=start=$DEBUT,asetpts=PTS-STARTPTS,aresample=48000,\
atempo=$TEMPO,apad,atrim=0:10,asetpts=PTS-STARTPTS,volume=1.0[voice];\
 [3:a]aresample=48000,atrim=16:26,asetpts=PTS-STARTPTS,volume=$BED_GAIN,\
afade=t=in:st=0:d=0.3[bed];\
 [4:a]aresample=48000,volume=$SFX_GAIN,apad,atrim=0:10,asetpts=PTS-STARTPTS[wh];\
 [voice][bed][wh]amix=inputs=3:duration=first:dropout_transition=0:normalize=0[a]" \
 -map "[v]" -map "[a]" -t 10 \
 -c:v libx264 -preset medium -crf 18 -r 30 -c:a aac -b:a 192k \
 "$R/build/${EP}_D.mp4" -y

if [ "$SEUL_D" = "--segment-d" ]; then
  echo "$EP -> build/${EP}_D.mp4 (segment D seul)"
  exit 0
fi

# --- Assemblage : A (7) + sting/B/C (9) + D (10) + E (4) = 30,0 s -------------
cat > "$R/build/${EP}_list.txt" <<EOF
file '$R/build/${EP}_A.mp4'
file '$R/templates/COMMUN_sting_BC.mp4'
file '$R/build/${EP}_D.mp4'
file '$R/templates/COMMUN_E.mp4'
EOF

ffmpeg -v error -f concat -safe 0 -i "$R/build/${EP}_list.txt" \
 -filter_complex "[0:a]loudnorm=I=-14:TP=-1.5:LRA=11,apad[a]" \
 -map 0:v -map "[a]" -t 30 \
 -c:v libx264 -preset slow -crf 20 -r 30 -pix_fmt yuv420p \
 -c:a aac -b:a 192k -ar 48000 -movflags +faststart \
 "$R/dist/tiktok/$EP.mp4" -y

echo "$EP -> dist/tiktok/$EP.mp4"
"$R/scripts/qc-episode.sh" "$EP"
