#!/bin/bash
# Rendu dans /dev/shm (disque plein) : projet, temporaires et sortie brute en mémoire.
cd "$(dirname "$0")"
W=/dev/shm/hf; mkdir -p $W/tmp final
for n in "$@"; do
  rm -rf $W/$n; python3 gen/build.py specs/$n.json $W/$n || continue
  cp $W/$n/timing.json proj/$n.timing.json
  (cd $W/$n && TMPDIR=$W/tmp npx -y hyperframes@0.9.5 render -o $W/$n.brut.mp4 > $W/$n.log 2>&1) || { echo "ECHEC $n"; tail -5 $W/$n.log; continue; }
  ffmpeg -y -loglevel error -i $W/$n.brut.mp4 -c:v libx264 -crf 23 -preset medium -pix_fmt yuv420p -af loudnorm=I=-14:TP=-1.5:LRA=11 -c:a aac -b:a 160k -ar 48000 -movflags +faststart final/$n.mp4 && rm -f $W/$n.brut.mp4
  python3 gen/srt.py proj/$n.timing.json > final/$n.srt
  rm -rf $W/$n $W/tmp/*
  echo "OK $n $(du -h final/$n.mp4|cut -f1)"
done
