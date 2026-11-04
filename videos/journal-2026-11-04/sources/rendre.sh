#!/bin/bash
cd "$(dirname "$0")"
for n in "$@"; do
  rm -rf proj/$n; python3 gen/build.py specs/$n.json proj/$n || continue
  (cd proj/$n && npx -y hyperframes@0.9.5 render -o ../$n.brut.mp4 > ../$n.log 2>&1) || { echo "ECHEC $n"; continue; }
  ffmpeg -y -loglevel error -i proj/$n.brut.mp4 -c:v libx264 -crf 23 -preset medium -pix_fmt yuv420p -af loudnorm=I=-14:TP=-1.5:LRA=11 -c:a aac -b:a 160k -ar 48000 -movflags +faststart final/$n.mp4 && rm -f proj/$n.brut.mp4
  echo "OK $n $(du -h final/$n.mp4|cut -f1)"
done
