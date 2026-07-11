#!/usr/bin/env python3
"""Story preview compositor 9:16 (1080x1920), FoodEatUp brand, story safe zones (250px top/bottom).
Mika hook medallion + hook text -> visual card -> Jour X/30 lower-third + CTA."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
W,H=1080,1920
BG=(247,249,251); BLUE=(11,110,253); ORANGE=(247,148,30); NAVY=(23,42,69); INK=(55,66,84); WHITE=(255,255,255)
FD="assets/fonts"
def F(n,s): return ImageFont.truetype(os.path.join(FD,n),s)
P800=lambda s:F("Poppins-800.ttf",s); P700=lambda s:F("Poppins-700.ttf",s); P600=lambda s:F("Poppins-600.ttf",s)
GUIDES=os.environ.get("GUIDES","1")=="1"
OUTDIR="preview" if GUIDES else "frames"
os.makedirs(OUTDIR,exist_ok=True)
logo=Image.open("assets/logo/foodeatup.png").convert("RGBA"); logo_wm=logo.crop((60,120,1420,410))
mika=Image.open("assets/avatar/mika-still.png").convert("RGBA")

def circle(img,d):
    img=img.resize((d,d),Image.LANCZOS); m=Image.new("L",(d,d),0); ImageDraw.Draw(m).ellipse([0,0,d-1,d-1],fill=255)
    out=Image.new("RGBA",(d,d),(0,0,0,0)); out.paste(img,(0,0),m); return out

def wrap(dr,t,f,mw):
    out=[];
    for para in t.split("\n"):
        cur=""
        for w in para.split():
            s=(cur+" "+w).strip()
            if dr.textbbox((0,0),s,font=f)[2]<=mw: cur=s
            else: out.append(cur); cur=w
        out.append(cur)
    return out

def fit(img,bw,bh):
    r=min(bw/img.width,bh/img.height); return img.resize((max(1,int(img.width*r)),max(1,int(img.height*r))),Image.LANCZOS)

def bg_base():
    im=Image.new("RGBA",(W,H),BG+(255,)); g=Image.new("RGBA",(W,H),(0,0,0,0)); gd=ImageDraw.Draw(g)
    gd.ellipse([W-420,-160,W+180,300],fill=BLUE+(20,)); gd.ellipse([-180,H-360,320,H+160],fill=ORANGE+(18,))
    im.alpha_composite(g.filter(ImageFilter.GaussianBlur(80))); return im

def load(p):
    if not os.path.exists(p) and os.path.exists("assets/screens/"+p): p="assets/screens/"+p
    return Image.open(p).convert("RGBA")

STORIES={
 "S01":(1,"30 jours pour maîtriser FoodEatUp.\n20 s par jour. On y va ?","La série","Suivez la série","assets-generes/intro.jpg"),
 "S02":(2,"Votre resto en ligne\nen 5 minutes ?","Étape 1 · Créer votre compte","foodeatup.com","assets/screens/modifier-profil.png"),
 "S03":(3,"La SEULE étape\nqui se fait sur le web.","Étape 2 · Créer votre boutique","foodeatup.com","assets/screens/ajout-boutique.png"),
 "S04":(4,"Vos taux de TVA,\nréglés une fois.","Étape 3 · Configurer la TVA","foodeatup.com","assets/screens/ajouter-tva.png"),
 "S05":(5,"Une carte bien rangée\ncommence ici.","Étape 4 · Créer vos catégories","foodeatup.com","assets/screens/ajouter-categorie.png"),
}

def build(sid):
    jour,hook,title,cta,visual=STORIES[sid]
    im=bg_base(); d=ImageDraw.Draw(im)
    # header logo (top, within safe)
    lw=250; lh=int(logo_wm.height*lw/logo_wm.width); im.alpha_composite(logo_wm.resize((lw,lh),Image.LANCZOS),(70,120))
    # hook: Mika medallion + text
    med=circle(mika.crop((120,80,600,560)),230)
    ring=Image.new("RGBA",(250,250),(0,0,0,0)); ImageDraw.Draw(ring).ellipse([0,0,249,249],outline=BLUE+(255,),width=8)
    im.alpha_composite(ring,(70,300)); im.alpha_composite(med,(80,310))
    f=P800(52); lines=wrap(d,hook,f,600); y=330
    for l in lines: d.text((330,y),l,font=f,fill=NAVY,anchor="lm"); y+=64
    # visual card center
    x,yv,w,h=90,600,900,720
    card=Image.new("RGBA",(w,h),(0,0,0,0)); ImageDraw.Draw(card).rounded_rectangle([0,0,w-1,h-1],32,fill=WHITE+(255,))
    sh=Image.new("RGBA",(w+80,h+80),(0,0,0,0)); ImageDraw.Draw(sh).rounded_rectangle([40,54,40+w,54+h],32,fill=(23,42,69,55))
    im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(24)),(x-40,yv-40)); im.alpha_composite(card,(x,yv))
    vis=fit(load(visual),w-48,h-48); im.alpha_composite(vis,(x+(w-vis.width)//2,yv+(h-vis.height)//2))
    # lower third: Jour X/30 pill + title
    pill=f"JOUR {jour}/30"; f2=P700(38); tw=d.textbbox((0,0),pill,font=f2)[2]; pw=tw+56
    d.rounded_rectangle([90,1380,90+pw,1450],35,fill=ORANGE+(255,)); d.text((90+pw/2,1415),pill,font=f2,fill=WHITE,anchor="mm")
    d.text((110+pw,1415),title,font=P700(40),fill=NAVY,anchor="lm")
    # CTA pill
    f3=P700(46); tw=d.textbbox((0,0),cta,font=f3)[2]; pw=tw+80;
    d.rounded_rectangle([(W-pw)//2,1500,(W+pw)//2,1600],50,fill=BLUE+(255,)); d.text((W/2,1550),cta,font=f3,fill=WHITE,anchor="mm")
    if GUIDES:
        d.line([0,250,W,250],fill=(255,0,0,60),width=2); d.line([0,1670,W,1670],fill=(255,0,0,60),width=2)
    im.convert("RGB").save(f"{OUTDIR}/{sid}.png"); print("built",sid,"->",OUTDIR)

for sid in (sys.argv[1:] or STORIES.keys()): build(sid)
