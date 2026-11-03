#!/usr/bin/env python3
"""Logo sting RapidoCRM « les trois oiseaux » (16:9, 1920x1080).
Entrée : 3 oiseaux (bleu/violet/vert) convergent, le VERT prend la tête → logo réel + flash vert → baseline.
Sortie : logo + pulse vert + CTA. Charte : fond #383838, vert #4CAF50. Typo Arial→Liberation Sans.
Logo réel en PNG (pas de rotation — interdit brandbook). Oiseaux d'approche = proxys vectoriels."""
import os, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter
HERE=os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
BASE="/home/user/Video"; GEN=f"{BASE}/videos/rapidocrm-presentation-4min/assets-generes"
LIB="/usr/share/fonts/truetype/liberation"
AB=lambda s:ImageFont.truetype(f"{LIB}/LiberationSans-Bold.ttf",s)
AR=lambda s:ImageFont.truetype(f"{LIB}/LiberationSans-Regular.ttf",s)
GREY=(56,56,56); GREEN=(76,175,80); VIOLET=(126,87,194); BLUE=(3,169,245); WHITE=(255,255,255)
W,H=1920,1080; CX,CY=960,470
LOGO=Image.open(f"{GEN}/rapidocrm-logo.png").convert("RGBA")
def scaled(im,w):
    r=w/im.width; return im.resize((max(1,w),max(1,int(im.height*r))),Image.LANCZOS)
LG=scaled(LOGO,440)
os.makedirs("in",exist_ok=True); os.makedirs("out",exist_ok=True)
def bg():
    im=Image.new("RGBA",(W,H),GREY+(255,)); g=Image.new("RGBA",(W,H),(0,0,0,0))
    ImageDraw.Draw(g).ellipse([CX-380,CY-300,CX+380,CY+300],fill=GREEN+(24,)); im.alpha_composite(g.filter(ImageFilter.GaussianBlur(120))); return im
def ease(t): return t*t*(3-2*t)
def bird(color,size,ang):
    s=size; im=Image.new("RGBA",(s*2,s*2),(0,0,0,0)); d=ImageDraw.Draw(im)
    # origami en chevron (2 ailes)
    d.polygon([(s,s*0.5),(s*1.6,s*1.4),(s,s*1.1)],fill=color+(255,))
    d.polygon([(s,s*0.5),(s*0.4,s*1.4),(s,s*1.1)],fill=tuple(int(c*0.8) for c in color)+(255,))
    return im.rotate(ang,expand=True,resample=Image.BICUBIC)
def paste_c(im,ov,cx,cy,a=255):
    if a<255:
        ov=ov.copy(); al=ov.split()[3].point(lambda p:int(p*a/255)); ov.putalpha(al)
    im.alpha_composite(ov,(int(cx-ov.width/2),int(cy-ov.height/2)))
def flash(im,cx,cy,strength,color=GREEN):
    if strength<=0: return
    g=Image.new("RGBA",(W,H),(0,0,0,0)); r=int(120+70*strength)
    ImageDraw.Draw(g).ellipse([cx-r,cy-r,cx+r,cy+r],fill=color+(int(150*strength),))
    im.alpha_composite(g.filter(ImageFilter.GaussianBlur(50)))

# trajectoires d'approche (start x,y, angle)
paths=[(BLUE,(-200,CY-40),-15),(VIOLET,(W+200,CY-180),200),(GREEN,(W+240,CY+260),150)]
NIN=45
for f in range(NIN):
    t=f/(NIN-1); im=bg()
    if t<0.5:  # 3 oiseaux convergent (vert légèrement en retard)
        for i,(col,(sx,sy),ang) in enumerate(paths):
            delay=0.10 if col==GREEN else 0.0
            p=ease(max(0,min(1,(t-delay)/(0.5-delay))))
            x=sx+(CX-sx)*p; y=sy+(CY-sy)*p; sz=int(70-30*p)
            paste_c(im,bird(col,sz,ang),x,y,int(120+135*p))
    elif t<0.72:  # verrouillage : logo réel apparait, flash vert
        p=ease((t-0.5)/0.22)
        for col,(sx,sy),ang in paths: paste_c(im,bird(col,int(40*(1-p)+10),ang),CX,CY,int(255*(1-p)))
        paste_c(im,LG,CX,CY,int(255*p)); flash(im,CX,CY-20,max(0,1-abs((t-0.64)/0.06)))
    else:  # logo + baseline
        paste_c(im,LG,CX,CY,255)
        a=int(255*ease((t-0.72)/0.28)); lay=Image.new("RGBA",(W,H),(0,0,0,0)); dl=ImageDraw.Draw(lay)
        dl.text((CX,CY+250),"Le tout en un pour propulser votre activité !",font=AR(38),fill=WHITE+(255,),anchor="mm")
        al=lay.split()[3].point(lambda p:int(p*a/255)); lay.putalpha(al); im.alpha_composite(lay)
    im.convert("RGB").save(f"in/{f:03d}.png")

NOUT=60
for f in range(NOUT):
    t=f/(NOUT-1); im=bg()
    if t<0.25:
        p=ease(t/0.25); paste_c(im,scaled(LOGO,int(440*(0.85+0.15*p))),CX,CY,int(255*p))
    else:
        pulse=1+0.05*math.sin((t-0.25)/0.75*math.pi*2); paste_c(im,scaled(LOGO,int(440*pulse)),CX,CY,255)
        if t>0.32:
            a=int(255*ease(min(1,(t-0.32)/0.25))); lay=Image.new("RGBA",(W,H),(0,0,0,0)); dl=ImageDraw.Draw(lay)
            dl.rounded_rectangle([CX-230,CY+150,CX+230,CY+230],40,fill=GREEN+(255,))
            dl.text((CX,CY+190),"Réservez votre démo",font=AB(40),fill=WHITE,anchor="mm")
            al=lay.split()[3].point(lambda p:int(p*a/255)); lay.putalpha(al); im.alpha_composite(lay)
        if 0.85<t<0.97: flash(im,CX,CY-20,max(0,1-abs((t-0.91)/0.06)))
    im.convert("RGB").save(f"out/{f:03d}.png")
print("CRM sting frames OK: in",NIN,"out",NOUT)
