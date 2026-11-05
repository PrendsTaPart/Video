#!/bin/bash
# Rendu de toute une série : outils-tutos/rendre.sh <dossier de la série>
# Sortie : <série>/sortie/<cle>-tuto.mp4. Saute ce qui est déjà rendu.
cd "$1"; mkdir -p sortie rendus
for d in projets/*/; do c=$(basename $d)
  [ -f sortie/$c-tuto.mp4 ] && continue
  (cd $d && npx -y hyperframes@0.9.5 render -o ../../rendus/$c.mp4 > ../../rendus/$c.log 2>&1) || { echo "ECHEC $c"; continue; }
  ffmpeg -y -loglevel error -i rendus/$c.mp4 -c:v libx264 -crf 24 -preset slow -c:a aac -b:a 128k -movflags +faststart sortie/$c-tuto.mp4 && rm -f rendus/$c.mp4 && echo "OK $c"
done; echo FINI
