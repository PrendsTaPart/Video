#!/usr/bin/env python3
"""Logo sting FoodEatUp — asset réutilisable. Entrée (1,5s : l'infini se forme, clin d'œil chef)
+ Sortie (2s : l'infini se rouvre, offre). Charte : fond #0F1A23, bleu #007BFF, orange #FFA500.
Frames PIL → clips ffmpeg. (Police Goodly indisponible → Poppins en substitut.)"""
import os, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter
HERE=os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
BASE="/home/user/Video"; FD=f"{BASE}/videos/rapidocms-presentation-4min/assets/fonts"
LOGO=f"{BASE}/studio-video/assets/brand/logo"
P700=lambda s:ImageFont.truetype(os.path.join(FD,"Poppins-700.ttf"),s)
P600=lambda s:ImageFont.truetype(os.path.join(FD,"Poppins-600.ttf"),s)
ANTH=(15,26,35); BLUE=(0,123,255); ORANGE=(255,165,0); WHITE=(255,255,255); CREAM=(252,249,230)
W,H=1080,1920; CX,CY=540,860
mascot=Image.open(f"{LOGO}/foodeatup-logo-mascot.png").convert("RGBA")
eight=Image.open(f"{LOGO}/foodeatup-mark-eight.png").convert("RGBA")
def scaled(im,w):
    r=w/im.width; return im.resize((w,int(im.height*r)),Image.LANCZOS)
MASC=scaled(mascot,600); EIGHT=scaled(eight,120)
os.makedirs("in",exist_ok=True); os.makedirs("out",exist_ok=True)
def bg():
    im=Image.new("RGBA",(W,H),ANTH+(255,)); g=Image.new("RGBA",(W,H),(0,0,0,0))
    ImageDraw.Draw(g).ellipse([CX-360,CY-360,CX+360,CY+360],fill=(166,208,255,26)); im.alpha_composite(g.filter(ImageFilter.GaussianBlur(120))); return im
def ease(t): return t*t*(3-2*t)
def paste_c(im,ov,cx,cy,a=255):
    if a<255:
        ov=ov.copy(); al=ov.split()[3].point(lambda p:int(p*a/255)); ov.putalpha(al)
    im.alpha_composite(ov,(int(cx-ov.width/2),int(cy-ov.height/2)))
def wink(im,cx,cy,strength):  # flash orange = clin d'œil
    if strength<=0: return
    g=Image.new("RGBA",(W,H),(0,0,0,0)); r=int(70+40*strength)
    ImageDraw.Draw(g).ellipse([cx-r,cy-r,cx+r,cy+r],fill=ORANGE+(int(150*strength),))
    im.alpha_composite(g.filter(ImageFilter.GaussianBlur(40)))

# ---------- ENTRÉE (45 frames / 1.5s) ----------
NIN=45
for f in range(NIN):
    t=f/(NIN-1); im=bg(); d=ImageDraw.Draw(im)
    if t<0.34:  # cercles convergent
        p=ease(t/0.34); spread=int(300*(1-p)); rad=54
        for sx in (-1,1):
            x=CX+sx*spread
            d.ellipse([x-rad,CY-rad,x+rad,CY+rad],outline=BLUE+(255,),width=14)
        if p>0.7: paste_c(im,EIGHT,CX,CY,int(255*(p-0.7)/0.3))
    elif t<0.62:  # mascotte s'assemble (scale in)
        p=ease((t-0.34)/0.28); paste_c(im,EIGHT,CX,CY,int(255*(1-p)))
        w=int(MASC.width*(0.8+0.2*p)); paste_c(im,scaled(mascot,w),CX,CY,int(255*p))
    else:  # logo posé + clin d'œil + baseline
        paste_c(im,MASC,CX,CY,255)
        wp=t if t<0.7 else 0
        wink(im,CX-70,CY,max(0,1-abs((t-0.66)/0.06)) if 0.60<t<0.72 else 0)
        if t>0.72:
            a=int(255*ease((t-0.72)/0.28)); f2=P600(38)
            txt="Une infinité de solutions pour gérer votre restaurant"
            lay=Image.new("RGBA",(W,H),(0,0,0,0)); dl=ImageDraw.Draw(lay)
            dl.text((CX,CY+150),txt,font=f2,fill=(166,208,255,255),anchor="mm")
            al=lay.split()[3].point(lambda p:int(p*a/255)); lay.putalpha(al); im.alpha_composite(lay)
    im.convert("RGB").save(f"in/{f:03d}.png")

# ---------- SORTIE (60 frames / 2s) ----------
NOUT=60
for f in range(NOUT):
    t=f/(NOUT-1); im=bg()
    if t<0.28:  # logo apparait
        p=ease(t/0.28); w=int(MASC.width*(0.82+0.18*p)); paste_c(im,scaled(mascot,w),CX,CY,int(255*p))
    else:
        pulse=1+0.06*math.sin((t-0.28)/0.72*math.pi*2)  # une respiration
        paste_c(im,scaled(mascot,int(MASC.width*pulse)),CX,CY,255)
        if t>0.34:
            a=int(255*ease(min(1,(t-0.34)/0.25))); d=ImageDraw.Draw(im)
            lay=Image.new("RGBA",(W,H),(0,0,0,0)); dl=ImageDraw.Draw(lay)
            dl.text((CX,CY+170),"-50%",font=P700(150),fill=ORANGE+(255,),anchor="mm")
            dl.text((CX,CY+320),"30 places bêta · jusqu'au 31 août 2026",font=P600(40),fill=(255,255,255,255),anchor="mm")
            al=lay.split()[3].point(lambda p:int(p*a/255)); lay.putalpha(al); im.alpha_composite(lay)
        if 0.86<t<0.98: wink(im,CX-70,CY,max(0,1-abs((t-0.92)/0.06)))
    im.convert("RGB").save(f"out/{f:03d}.png")
print("sting frames OK: in",NIN,"out",NOUT)
