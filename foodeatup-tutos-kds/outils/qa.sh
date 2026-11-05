#!/bin/bash
# Contrôle qualité : résolution, durée, audio, 4 images en planche.
f=sortie/$1-tuto.mp4; o=${2:-/tmp}/qa-$1.jpg
ffprobe -v error -show_entries stream=codec_type,width,height:format=duration -of compact $f | tr '\n' ' '
ffmpeg -i $f -af volumedetect -f null - 2>&1 | grep -o "mean_volume: .*"
d=$(ffprobe -v error -show_entries format=duration -of csv=p=0 $f)
i=0; for t in 2 $(echo "$d*0.35"|bc) $(echo "$d*0.7"|bc) $(echo "$d-1.2"|bc); do ffmpeg -y -loglevel error -ss $t -i $f -frames:v 1 -vf scale=640:-1 /tmp/qa_$i.jpg; i=$((i+1)); done
ffmpeg -loglevel error -y -i /tmp/qa_0.jpg -i /tmp/qa_1.jpg -i /tmp/qa_2.jpg -i /tmp/qa_3.jpg -filter_complex "[0][1][2][3]xstack=inputs=4:layout=0_0|w0_0|0_h0|w0_h0" $o
