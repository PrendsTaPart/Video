#!/usr/bin/env bash
# Monte un épisode de 37,5 s à partir d'assets DÉJÀ produits.
# Aucune génération : ni Higgsfield, ni HeyGen, ni image. Uniquement ffmpeg local.
#
#   ./build-episode.sh EP001
#
# Attendus :
#   assets/hooks/EPxxx.mp4       clip Higgsfield récupéré (9,5 s utiles)
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
RESPIR=0.6         # respiration avant 26,0 s : l'avatar doit avoir fini de parler
                   # avant que la voix de fin démarre, sinon les deux se marchent dessus
# Coque d'appareil : le screencast s'incruste dans une tablette. Les épisodes
# du module Caisse POS prennent la variante posée sur un tiroir-caisse.
MODULE="$(python3 -c "import json;print(json.load(open('$R/state/episodes/$EP.json'))['module'])" 2>/dev/null || echo "")"
case "$MODULE" in
  "Caisse POS") COQUE=tablette-caisse; COQ_Y=85;  ECR_Y=111 ;;
  *)            COQUE=tablette;        COQ_Y=151; ECR_Y=177 ;;
esac
COQ_X=34; ECR_X=60           # trou d'écran à (26,26) dans une coque de 1012 de large
ECR_W=960; ECR_H=414         # ratio exact du screencast 1920x828
echo "  coque  : $COQUE (module $MODULE)"

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
FENETRE="$(python3 -c "print(f'{10.0-$RESPIR:.2f}')")"
TEMPO="$(python3 -c "print(f'{max(1.0,$UTILE/$FENETRE):.4f}')")"
echo "  avatar : parole ${DEBUT}s → ${FIN}s (${UTILE}s utiles), fenêtre ${FENETRE}s, atempo ${TEMPO}"
# Au-delà de 1,12 l'accélération s'entend nettement. On monte quand même —
# un épisode livré vaut mieux qu'un épisode bloqué — mais on le dit.
python3 -c "
t=$TEMPO
if t>1.12:
    print(f'  ATTENTION : atempo {t:.3f}, le script HeyGen est trop long pour la fenêtre.')
    print(f'  Correction réelle = re-rendu avec un script plus court, pas une accélération.')
"

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
 -loop 1 -t 10 -i "$R/templates/$COQUE.png" \
 -filter_complex "\
 [0:v]trim=start=$DEBUT,setpts=(PTS-STARTPTS)/$TEMPO,fps=30,\
crop=1080:$AV_H:0:$AV_CROP_Y,tpad=stop_mode=clone:stop_duration=3,\
trim=0:10,setpts=PTS-STARTPTS[top];\
 color=c=$SABLE:s=1080x$SOFT_H:r=30,trim=0:10,setpts=PTS-STARTPTS[fond];\
 [1:v]fps=30,scale=$ECR_W:$ECR_H[ecran];\
 [fond][ecran]overlay=$ECR_X:$ECR_Y[avec];\
 [5:v]fps=30,format=rgba[coque];\
 [avec][coque]overlay=$COQ_X:$COQ_Y[mid];\
 color=c=$SABLE:s=1080x$BAND_H:r=30,trim=0:10[band];\
 [top][mid][band]vstack=inputs=3[stack];\
 [stack][2:v]overlay=(W-w)/2:H-$BAND_H+(($BAND_H-h)/2):format=auto[ov];\
 [ov]fade=t=in:st=0:d=0.35:color=$SABLE,\
fade=t=out:st=9.70:d=0.30:color=$SABLE,format=yuv420p[v];\
 [0:a]atrim=start=$DEBUT,asetpts=PTS-STARTPTS,aresample=48000,\
atempo=$TEMPO,apad,atrim=0:10,asetpts=PTS-STARTPTS,volume=1.0[voice];\
 [3:a]aresample=48000,atrim=16:26,asetpts=PTS-STARTPTS,volume=$BED_GAIN,\
afade=t=in:st=0:d=0.3,afade=t=out:st=9.40:d=0.60[bed];\
 [4:a]aresample=48000,volume=$SFX_GAIN,apad,atrim=0:10,asetpts=PTS-STARTPTS[wh];\
 [voice][bed][wh]amix=inputs=3:duration=first:dropout_transition=0:normalize=0[a]" \
 -map "[v]" -map "[a]" -t 10 \
 -c:v libx264 -preset medium -crf 18 -r 30 -c:a aac -b:a 192k \
 "$R/build/${EP}_D.mp4" -y

# Le mixage de D somme la voix, le lit et le whoosh sans normalisation : il
# écrêtait à +2,8 dBTP. On le cale sur le niveau des gabarits.
"$R/scripts/normaliser-segment.sh" "$R/build/${EP}_D.mp4" -21 -9

if [ "$SEUL_D" = "--segment-d" ]; then
  echo "$EP -> build/${EP}_D.mp4 (segment D seul)"
  exit 0
fi

# Le segment A sort à des niveaux très variables selon le clip Higgsfield.
# Sans ce calage, le hook passait 12 dB sous l'avatar.
"$R/scripts/normaliser-segment.sh" "$R/build/${EP}_A.mp4" -21 -9

# --- Assemblage : A (9,5) + sting/B/C (9) + D (10) + E (4) = 32,5 s -----------
# puis le sting de marque (5 s) est collé derrière -> 37,5 s au total.
cat > "$R/build/${EP}_list.txt" <<EOF
file '$R/build/${EP}_A.mp4'
file '$R/templates/COMMUN_sting_BC.mp4'
file '$R/build/${EP}_D.mp4'
file '$R/templates/COMMUN_E.mp4'
EOF

# L'assemblage ne normalise pas : l'audio brut est recollé tel quel. La
# normalisation arrive une seule fois, tout à la fin, sur le mixage complet.
ffmpeg -v error -f concat -safe 0 -i "$R/build/${EP}_list.txt" \
 -filter_complex "[0:a]aresample=48000,apad[a]" \
 -map 0:v -map "[a]" -t 32.5 \
 -c:v libx264 -preset medium -crf 18 -r 30 -pix_fmt yuv420p \
 -c:a pcm_s16le -ar 48000 "$R/build/${EP}_court.mov" -y

# Le sting de marque ferme l'épisode. acrossfade ne croise que l'audio sur
# 0,3 s : l'image, elle, est bout à bout, donc 32,5 + 5 = 37,5 s.
ffmpeg -v error -i "$R/build/${EP}_court.mov" -i "$R/templates/sting-fin.mp4" \
 -filter_complex "\
 [0:a]aresample=48000,asetpts=PTS-STARTPTS[a0];\
 [1:a]aresample=48000,asetpts=PTS-STARTPTS[a1];\
 [a0][a1]acrossfade=d=0.3:c1=tri:c2=tri[a]" \
 -map "[a]" -c:a pcm_s16le -ar 48000 "$R/build/${EP}_mix.wav" -y

# --- Normalisation finale : gain constant + limiteur ---------------------------
# loudnorm a été essayé ici, en une passe puis en deux avec linear=true. Les deux
# retombent en mode dynamique dès que le gain demandé ferait dépasser la crête —
# ce qui est toujours le cas sur un master à -14 LUFS. Et en dynamique, loudnorm
# remonte les passages calmes : le lit musical sortait à -17 dBFS dans la
# respiration qui précède la signature, assez fort pour s'entendre comme une
# pompe. Un gain constant ne touche à aucun rapport interne du mixage.
mesure_mix() {
  ffmpeg -hide_banner -nostats -i "$1" -af ebur128=peak=true -f null - 2>&1 \
  | sed -n '/Summary/,$p' \
  | awk '/^[[:space:]]+I:/{i=$2} /Peak:/{if(p=="")p=$2} END{print i, p}'
}
# L'image est encodée UNE fois, sans son. Le calage du niveau se joue ensuite en
# remuxant l'audio par copie du flux vidéo — sinon chaque itération coûterait un
# encodage x264 en preset slow.
ffmpeg -v error -i "$R/build/${EP}_court.mov" -i "$R/templates/sting-fin.mp4" \
 -filter_complex "\
 [0:v]scale=1080:1920,setsar=1,fps=30[v0];\
 [1:v]scale=1080:1920,setsar=1,fps=30[v1];\
 [v0][v1]concat=n=2:v=1:a=0[v]" \
 -map "[v]" -t 37.5 -an \
 -c:v libx264 -preset slow -crf 20 -r 30 -pix_fmt yuv420p \
 "$R/build/${EP}_muet.mp4" -y

# La boucle se ferme sur le MASTER ENCODÉ, pas sur le WAV. L'encodage AAC fait
# remonter la crête, et de façon très inégale : sur EP007 le WAV sortait à
# -1,8 dBTP et le master aussi, sur EP002 le même WAV à -1,8 donnait -0,3 dBTP
# après AAC. Mesurer le WAV ne dit donc rien du livrable. On mesure le fichier
# qui part en ligne, et on rabaisse le plafond du limiteur tant qu'il déborde.
read -r MIX_I MIX_TP <<<"$(mesure_mix "$R/build/${EP}_mix.wav")"
GAIN_M="$(python3 -c "print(f'{-14.0-($MIX_I):.2f}')")"
PLAF=0.72
for _ in 1 2 3 4 5; do
  ffmpeg -v error -i "$R/build/${EP}_mix.wav" \
   -af "volume=${GAIN_M}dB,alimiter=limit=$PLAF:level=disabled:attack=5:release=60" \
   -ar 48000 -c:a pcm_s16le "$R/build/${EP}_mixn.wav" -y
  ffmpeg -v error -i "$R/build/${EP}_muet.mp4" -i "$R/build/${EP}_mixn.wav" \
   -map 0:v -map 1:a -t 37.5 -c:v copy \
   -c:a aac -b:a 192k -ar 48000 -movflags +faststart \
   "$R/dist/tiktok/$EP.mp4" -y
  read -r NEW_I NEW_TP <<<"$(mesure_mix "$R/dist/tiktok/$EP.mp4")"
  # -1,4 dBTP de marge : la cible QC est -1, on ne s'y colle pas.
  DEBORDE="$(python3 -c "print(1 if $NEW_TP > -1.4 else 0)")"
  ECART_I="$(python3 -c "print(1 if abs(-14.0-($NEW_I))>0.4 else 0)")"
  [ "$DEBORDE" = "0" ] && [ "$ECART_I" = "0" ] && break
  [ "$DEBORDE" = "1" ] && PLAF="$(python3 -c "print(f'{$PLAF*10**((-1.6-($NEW_TP))/20):.4f}')")"
  [ "$ECART_I" = "1" ] && GAIN_M="$(python3 -c "print(f'{$GAIN_M+(-14.0-($NEW_I)):.2f}')")"
done
echo "  mixage : $MIX_I LUFS / $MIX_TP dBTP -> $NEW_I LUFS / $NEW_TP dBTP (gain ${GAIN_M} dB, plafond $PLAF)"
rm -f "$R/build/${EP}_mix.wav" "$R/build/${EP}_mixn.wav" "$R/build/${EP}_muet.mp4"

echo "$EP -> dist/tiktok/$EP.mp4"
"$R/scripts/qc-episode.sh" "$EP"
