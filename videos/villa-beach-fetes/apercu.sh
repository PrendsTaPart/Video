#!/bin/bash
# bash apercu.sh <dossier> composition:image ... : rend des images fixes et une planche contact.
D="$1"; shift; mkdir -p "$D"
B=$(ls -d /opt/pw-browsers/chromium_headless_shell-1243/*/chrome-headless-shell)
for c in "$@"; do id=${c%%:*}; fr=${c##*:}; npx remotion still src/index.ts "$id" "$D/$id-$fr.png" --frame="$fr" --browser-executable="$B" --log=error; done
python3 - "$D" "$@" <<'PY'
import sys
from PIL import Image
d=sys.argv[1]; fs=[f"{d}/{c.split(':')[0]}-{c.split(':')[1]}.png" for c in sys.argv[2:]]
ims=[Image.open(f).convert('RGB') for f in fs]
h=480; ims=[im.resize((int(im.width*h/im.height),h)) for im in ims]
W=Image.new('RGB',(sum(i.width for i in ims),h)); x=0
for im in ims: W.paste(im,(x,0)); x+=im.width
W.save(f"{d}/planche.jpg")
PY
