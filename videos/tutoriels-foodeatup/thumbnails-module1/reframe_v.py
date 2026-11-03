#!/usr/bin/env python3
"""Reframe portraits blancs RapidoCMS -> vertical 9:16 1080x1920, fond blanc, chef en bas, espace titre en haut."""
import sys, os
from PIL import Image
os.chdir(os.path.dirname(os.path.abspath(__file__)))
W,H=1080,1920
def reframe(src,out):
    P=Image.open(src).convert("RGB")
    # sample background color (top-left corner region) to pad seamlessly
    px=P.crop((0,0,60,60)).resize((1,1)).getpixel((0,0))
    sw=W; sh=int(P.height*W/P.width); im=P.resize((sw,sh))
    cv=Image.new("RGB",(W,H),px)
    # bottom-align with 30px bottom margin -> top band reserved for title
    y=H-sh-30
    if y<0:  # image taller than canvas: crop bottom overflow
        im=im.crop((0,0,W,H-30)); y=0
    cv.paste(im,(0,max(y,0)))
    cv.save(out,quality=92); return cv.size, px
if __name__=="__main__":
    for k in sys.argv[1:]:
        print(k, reframe(f"work/white/v{k}.jpg", f"output-vertical/thumb-v{k}.jpg"))
