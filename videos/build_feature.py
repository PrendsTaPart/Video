#!/usr/bin/env python3
"""Dark 'product-tour' feature video frames (1080x1920, TikTok-safe layout).
Run with cwd = project dir; FEATURE env selects the config.
Screenshots (black bg) float on a near-black canvas with a sky-blue glow."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

W, H = 1080, 1920
BG0     = (5, 7, 13)
ACCENT  = (41, 169, 242)
ACCENT2 = (91, 197, 255)
WHITE   = (255, 255, 255)
MUTED   = (150, 170, 196)
GREYDOT = (60, 74, 96)

DOTS_Y = 1360
CAP_Y  = 1432

FD = "assets/fonts"
def F(n, s): return ImageFont.truetype(os.path.join(FD, n), s)
P800=lambda s:F("Poppins-800.ttf",s); P700=lambda s:F("Poppins-700.ttf",s)
P600=lambda s:F("Poppins-600.ttf",s); P400=lambda s:F("Poppins-400.ttf",s)

mark = Image.open("assets/logo/origami.png").convert("RGBA")

def bg_base():
    im = Image.new("RGBA",(W,H),BG0+(255,))
    glow = Image.new("RGBA",(W,H),(0,0,0,0)); gd=ImageDraw.Draw(glow)
    gd.ellipse([W//2-620,120,W//2+620,1000], fill=ACCENT+(46,))
    gd.ellipse([W//2-380,1500,W//2+380,2050], fill=(80,60,200,26))
    glow=glow.filter(ImageFilter.GaussianBlur(120))
    im.alpha_composite(glow)
    return im

def logo(im, x, y, mh):
    mw=int(mark.width*mh/mark.height)
    m=mark.resize((mw,mh),Image.LANCZOS); im.alpha_composite(m,(x,y))
    d=ImageDraw.Draw(im)
    f=P700(int(mh*0.62))
    tx=x+mw+18; ty=y+mh//2
    d.text((tx,ty),"Rapido",font=f,fill=WHITE,anchor="lm")
    wr=d.textbbox((tx,ty),"Rapido",font=f,anchor="lm")[2]
    d.text((wr,ty),"CMS",font=f,fill=ACCENT2,anchor="lm")

def header(im, counter):
    logo(im,70,92,64)
    d=ImageDraw.Draw(im); f=P700(40)
    tw=d.textbbox((0,0),counter,font=f)[2]
    pw,ph=tw+56,68; px,py=W-70-pw,96
    d.rounded_rectangle([px,py,px+pw,py+ph],34,fill=ACCENT+(255,))
    d.text((px+pw/2,py+ph/2),counter,font=f,fill=WHITE,anchor="mm")

def wrap(d,text,font,maxw):
    out=[]
    for para in text.split("\n"):
        words=para.split(); cur=""
        for w in words:
            t=(cur+" "+w).strip()
            if d.textbbox((0,0),t,font=font)[2]<=maxw: cur=t
            else:
                if cur: out.append(cur)
                cur=w
        out.append(cur)
    return out

def caption(im,text):
    d=ImageDraw.Draw(im); f=P700(46); maxw=900
    lines=wrap(d,text,f,maxw); lh=62; th=lh*len(lines); pad=40
    tw=max(d.textbbox((0,0),l,font=f)[2] for l in lines)
    pw=min(tw+pad*2,W-80); ph=th+pad*2-8; px=(W-pw)//2
    d.rounded_rectangle([px,CAP_Y,px+pw,CAP_Y+ph],40,fill=ACCENT+(240,))
    y=CAP_Y+pad-4
    for l in lines:
        d.text((W/2,y+lh/2),l,font=f,fill=WHITE,anchor="mm"); y+=lh

def dots(im,active,n):
    aw,dw,gap=46,16,26
    widths=[aw if i==active else dw for i in range(n)]
    total=sum(widths)+gap*(n-1); x=(W-total)//2
    d=ImageDraw.Draw(im)
    for i in range(n):
        w=widths[i]; col=ACCENT if i==active else GREYDOT
        d.rounded_rectangle([x,DOTS_Y,x+w,DOTS_Y+16],8,fill=col+(255,)); x+=w+gap

def hero(im, path, cy):
    img=Image.open(path).convert("RGBA")
    boxw,boxh=1010,720
    r=min(boxw/img.width, boxh/img.height)
    nw,nh=int(img.width*r),int(img.height*r)
    img=img.resize((nw,nh),Image.LANCZOS)
    x=(W-nw)//2; y=cy-nh//2
    # blue glow behind
    g=Image.new("RGBA",(W,H),(0,0,0,0)); gd=ImageDraw.Draw(g)
    gd.ellipse([x-60,y-40,x+nw+60,y+nh+40],fill=ACCENT+(60,))
    g=g.filter(ImageFilter.GaussianBlur(90)); im.alpha_composite(g)
    im.alpha_composite(img,(x,y))

def eyebrow_headline(im, eyebrow, headline):
    d=ImageDraw.Draw(im)
    d.text((W/2,250),eyebrow.upper(),font=P700(36),fill=ACCENT2,anchor="mm")
    f=P800(66); lines=wrap(d,headline,f,940); lh=80; y=320
    for l in lines:
        d.text((W/2,y+lh/2),l,font=f,fill=WHITE,anchor="mm"); y+=lh

# ---------------- CONFIGS ----------------
CFG = {
 "calendrier": {
   "title":"Le Calendrier","sub":"Planifie et publie sur tous tes réseaux",
   "hook":"Publier partout, sans y penser tous les jours.",
   "frames":[
     {"eyebrow":"Vue d'ensemble","headline":"Tout ton contenu,\nun seul calendrier","hero":"assets/ui/full.jpg",
      "caption":"LinkedIn, Facebook, Instagram — au même endroit"},
     {"eyebrow":"Planification","headline":"Programme tes posts\nà l'avance","hero":"assets/ui/calendar.png",
      "caption":"Choisis la date, l'heure, le réseau. C'est publié tout seul."},
     {"eyebrow":"Résultats","headline":"Mesure ce qui\nfonctionne","hero":"assets/ui/stats.png",
      "caption":"Interactions, engagement, abonnements — en un coup d'œil"},
   ],
   "cta_caption":"Planifie ton mois — cms.rapidosoftware.com",
 },
 "editeur": {
   "title":"L'Éditeur","sub":"Cartes de visite, NFC et affiches — sans designer",
   "hook":"Tes supports pros, créés en quelques clics.",
   "frames":[
     {"eyebrow":"L'éditeur RapidoCMS","headline":"Un éditeur,\ntous tes supports","hero":"assets/ui/screen.png",
      "caption":"Cartes de visite, cartes NFC, affiches et posts"},
     {"eyebrow":"Modèles","headline":"Des templates\nprêts à l'emploi","hero":"assets/ui/templates.png",
      "caption":"Pioche un modèle, personnalise, exporte."},
     {"eyebrow":"Sans designer","headline":"Conçois dans\nl'éditeur","hero":"assets/ui/designer.png",
      "caption":"Carte de visite, carte NFC, affiche — en quelques clics"},
   ],
   "cta_caption":"Crée ta première carte — cms.rapidosoftware.com",
 },
}

FEATURE=os.environ["FEATURE"]; c=CFG[FEATURE]
os.makedirs("frames",exist_ok=True)
nslides=len(c["frames"])
N=nslides+2  # intro + slides + cta

# intro
im=bg_base(); d=ImageDraw.Draw(im)
mh=150; mw=int(mark.width*mh/mark.height)
im.alpha_composite(mark.resize((mw,mh),Image.LANCZOS),((W-mw)//2,470))
d.text((W/2,700),"RapidoCMS",font=P700(58),fill=WHITE,anchor="mm")
d.text((W/2,860),c["title"],font=P800(118),fill=ACCENT2,anchor="mm")
for i,l in enumerate(wrap(d,c["sub"],P600(46),900)):
    d.text((W/2,980+i*60),l,font=P600(46),fill=MUTED,anchor="mm")
caption(im,c["hook"]); im.convert("RGB").save("frames/f0.png"); print("f0 intro")

# content slides
for i,fr in enumerate(c["frames"]):
    im=bg_base(); header(im,f"{i+1}/{nslides}")
    eyebrow_headline(im,fr["eyebrow"],fr["headline"])
    hero(im,fr["hero"],930)
    dots(im,i,nslides); caption(im,fr["caption"])
    im.convert("RGB").save(f"frames/f{i+1}.png"); print("f%d"%(i+1),fr["hero"])

# cta
im=bg_base(); d=ImageDraw.Draw(im)
mh=140; mw=int(mark.width*mh/mark.height)
im.alpha_composite(mark.resize((mw,mh),Image.LANCZOS),((W-mw)//2,430))
d.text((W/2,650),"RapidoCMS",font=P700(56),fill=WHITE,anchor="mm")
for i,l in enumerate(wrap(d,"Essaye RapidoCMS\ngratuitement",P800(96),960)):
    d.text((W/2,820+i*104),l,font=P800(96),fill=ACCENT2,anchor="mm")
# url pill
url="cms.rapidosoftware.com"; f=P700(50)
tw=d.textbbox((0,0),url,font=f)[2]; pw,ph=tw+90,110; px=(W-pw)//2; py=1120
d.rounded_rectangle([px,py,px+pw,py+ph],55,fill=ACCENT+(255,))
d.text((W/2,py+ph/2),url,font=f,fill=WHITE,anchor="mm")
caption(im,c["cta_caption"]); im.convert("RGB").save(f"frames/f{nslides+1}.png"); print("cta")
print("TOTAL FRAMES",N)
