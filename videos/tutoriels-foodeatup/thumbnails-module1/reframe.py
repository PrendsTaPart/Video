#!/usr/bin/env python3
"""Reframe portraits RapidoCMS (1024x1536) -> thumbnails 16:9 1280x720, chef à droite, gauche vide."""
import sys, os
from PIL import Image, ImageDraw, ImageFilter
os.chdir(os.path.dirname(os.path.abspath(__file__)))
W,H=1280,720
DARK=(15,26,35); GLOWC=(22,42,60)
def canvas():
    bg=Image.new("RGB",(W,H),DARK)
    glow=Image.new("L",(W,H),0); d=ImageDraw.Draw(glow)
    d.ellipse([W*0.45,-160,W*1.15,H+160],fill=255); glow=glow.filter(ImageFilter.GaussianBlur(180))
    bg=Image.composite(Image.new("RGB",(W,H),GLOWC),bg,glow)
    # faint toque motif behind char (right-center)
    mo=Image.new("L",(W,H),0); dm=ImageDraw.Draw(mo)
    cx,cy=980,300
    dm.ellipse([cx-190,cy-60,cx+190,cy+140],fill=255)      # base
    for ox in (-120,0,120):
        dm.ellipse([cx+ox-95,cy-190,cx+ox+95,cy+10],fill=255)  # puffs
    mo=mo.filter(ImageFilter.GaussianBlur(24))
    bg=Image.composite(Image.new("RGB",(W,H),(28,46,66)),bg,mo.point(lambda p:int(p*0.16)))
    return bg

def reframe(src,out):
    P=Image.open(src).convert("RGB")
    # scale to full height
    sw=int(P.width*H/P.height); strip=P.resize((sw,H))
    # place so character (right side of portrait) sits on the right; keep strip width, anchor right
    x=W-sw+ int(sw*0.02)
    cv=canvas()
    # feather mask: transparent on left ~110px then opaque
    m=Image.new("L",(sw,H),255); dm=ImageDraw.Draw(m)
    for i in range(150):
        dm.line([(i,0),(i,H)],fill=int(255*(i/150)))
    cv.paste(strip,(x,0),m)
    # left-side darkening gradient to keep title area clean
    grad=Image.new("L",(W,H),0); dg=ImageDraw.Draw(grad)
    for i in range(0,760):
        dg.line([(i,0),(i,H)],fill=int(150*(1-i/760)))
    cv=Image.composite(Image.new("RGB",(W,H),DARK),cv,grad)
    cv.save(out,quality=92)
    return cv.size

if __name__=="__main__":
    for k in sys.argv[1:]:
        print(k, reframe(f"work/v{k}.jpg", f"output/thumb-v{k}.jpg"))
