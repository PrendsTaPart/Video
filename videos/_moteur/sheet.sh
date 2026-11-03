#!/bin/bash
# sheet.sh dir t1..tN -> dir/stills.jpg (grille 6 colonnes)
d=$1; shift; rm -f $d/still-*.png
node stills.js $d "$@" 2>&1 | grep -iv warn | tail -3
n=$#; f=""; for i in $(seq 0 $((n-1))); do f="$f -i $d/still-$i.png"; done
cols=6; rows=$(( (n+cols-1)/cols )); L=""; for i in $(seq 0 $((n-1))); do L="$L|$(( (i%cols)*360 ))_$(( (i/cols)*640 ))"; done
ffmpeg -v error -y $f -filter_complex "$(for i in $(seq 0 $((n-1))); do printf "[$i:v]scale=360:640[s$i];"; done)$(for i in $(seq 0 $((n-1))); do printf "[s$i]"; done)xstack=inputs=$n:layout=${L:1}:fill=black" $d/stills.jpg
