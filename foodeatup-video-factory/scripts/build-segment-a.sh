#!/usr/bin/env bash
# Monte le segment A : hook Higgsfield + texte incrusté + punchline à 5,0 s.
#
#   ./build-segment-a.sh EP003 "Ta marge, en ce moment."
#
# Attendus : assets/hooks/EPxxx.mp4 et assets/vo/punchlines/EPxxx.mp3
set -euo pipefail

EP="${1:?usage: build-segment-a.sh EPxxx \"texte du hook\"}"
TEXTE="${2:?texte du hook manquant}"
R="$(cd "$(dirname "$0")/.." && pwd)"

POLICE="$R/templates/Poppins-800.ttf"
LOGO_X=795; LOGO_Y=57
PUNCH=5.0          # le beat comique du clip tombe ici
T_IN=0.8; T_OUT=3.5   # fenêtre du hook incrusté

# Le clip garde son ambiance, mais s'efface sous la punchline : sidechaincompress
# fait plonger le clip dès que la voix parle, et le laisse revenir après.
ffmpeg -v error \
 -i "$R/assets/hooks/$EP.mp4" \
 -i "$R/assets/vo/punchlines/$EP.mp3" \
 -i "$R/templates/logo_foodeatup.png" \
 -filter_complex "\
 [0:v]trim=0:7,setpts=PTS-STARTPTS,fps=30,\
scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920[v];\
 [v]drawtext=fontfile='$POLICE':text='$TEXTE':fontsize=62:fontcolor=white:\
borderw=6:bordercolor=black@0.8:x=(w-text_w)/2:y=h*0.13:\
enable='between(t,$T_IN,$T_OUT)'[vt];\
 [vt][2:v]overlay=$LOGO_X:$LOGO_Y:format=auto,format=yuv420p[vo];\
 [0:a]atrim=0:7,asetpts=PTS-STARTPTS,aresample=48000[a0];\
 [1:a]aresample=48000,adelay=$(python3 -c "print(int($PUNCH*1000))")|$(python3 -c "print(int($PUNCH*1000))"),\
volume=1.7,apad,atrim=0:7,asetpts=PTS-STARTPTS[a1];\
 [a1]asplit=2[punch][cle];\
 [a0][cle]sidechaincompress=threshold=0.06:ratio=8:attack=8:release=260[duck];\
 [duck][punch]amix=inputs=2:duration=first:dropout_transition=0:normalize=0[a]" \
 -map "[vo]" -map "[a]" -t 7 \
 -c:v libx264 -preset medium -crf 18 -r 30 -c:a aac -b:a 192k -ar 48000 \
 "$R/build/${EP}_A.mp4" -y

echo "$EP -> build/${EP}_A.mp4 ($(ffprobe -v error -show_entries format=duration -of csv=p=0 "$R/build/${EP}_A.mp4")s)"
