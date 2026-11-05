#!/bin/bash
# Versions finales (avec voix) : sortie/<cle>-tuto.mp4. Rejouable : saute ce qui est déjà rendu.
cd "$(dirname "$0")"; mkdir -p sortie rendus
for d in projets/*/; do c=$(basename $d)
  [ -f voix/$c.mp3 ] || { echo "SANS VOIX $c"; continue; }
  [ -f sortie/$c-tuto.mp4 ] && continue
  (cd $d && npx -y hyperframes@0.9.5 render -o ../../rendus/$c.mp4 > ../../rendus/$c.log 2>&1) || { echo "ECHEC $c"; continue; }
  ffmpeg -y -loglevel error -i rendus/$c.mp4 -c:v libx264 -crf 24 -preset slow -c:a aac -b:a 128k -movflags +faststart sortie/$c-tuto.mp4 && rm -f rendus/$c.mp4 && echo "OK $c"
done; echo FINI
