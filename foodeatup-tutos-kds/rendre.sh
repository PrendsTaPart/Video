#!/bin/bash
cd "$(dirname "$0")"; mkdir -p brouillons rendus
for d in projets/*/; do c=$(basename $d)
  [ -f brouillons/$c.mp4 ] && continue
  (cd $d && npx -y hyperframes@0.9.5 render -o ../../rendus/$c.mp4 > ../../rendus/$c.log 2>&1) || { echo "ECHEC $c"; continue; }
  ffmpeg -y -loglevel error -i rendus/$c.mp4 -c:v libx264 -crf 24 -preset slow -c:a aac -b:a 128k -movflags +faststart brouillons/$c.mp4 \
   && ffmpeg -y -loglevel error -ss 7 -i brouillons/$c.mp4 -frames:v 1 -q:v 3 brouillons/$c.jpg && echo "OK $c"
done; echo FINI
