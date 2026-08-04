#!/usr/bin/env python3
"""Compositeur V1 Lancement FoodEatUp — frames 16:9 (1920x1080) pour LinkedIn (60 s).
Même récit, plan 2 fondateur rallongé (Mika/Mo caméra). Mouvement + Mika live + audio via assemble_launch169.py."""
import os, glob
from PIL import Image, ImageDraw, ImageFont, ImageFilter
HERE=os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
BASE="/home/user/Video"; FD=f"{BASE}/videos/rapidocms-presentation-4min/assets/fonts"
def F(n,s): return ImageFont.truetype(os.path.join(FD,n),s)
P800=lambda s:F("Poppins-800.ttf",s); P700=lambda s:F("Poppins-700.ttf",s); P600=lambda s:F("Poppins-600.ttf",s)
BLUE=(11,110,253); ORANGE=(247,148,30); WHITE=(255,255,255); NAVY=(20,24,46); GREEN=(39,201,99)
CLAUDE=Image.open(f"{BASE}/videos/rapidocms-presentation-4min/assets/rapidocms/logo-claude.png").convert("RGBA")
W,H=1920,1080
os.makedirs("frames169",exist_ok=True); os.makedirs("frames169/p4type",exist_ok=True); os.makedirs("masks",exist_ok=True)
SCR=f"{BASE}/assets/screens/foodeatup"; GEN="assets-generes"
def cover(im,w=W,h=H):
    r=max(w/im.width,h/im.height); im=im.resize((int(im.width*r),int(im.height*r)),Image.LANCZOS)
    x=(im.width-w)//2; y=(im.height-h)//2; return im.crop((x,y,x+w,y+h))
def load(p): return Image.open(p).convert("RGBA")
def wrap(dr,t,f,mw):
    out=[];cur=""
    for wd in t.split():
        s=(cur+" "+wd).strip()
        if dr.textbbox((0,0),s,font=f)[2]<=mw: cur=s
        else: out.append(cur); cur=wd
    out.append(cur); return out
def fit(img,bw,bh):
    r=min(bw/img.width,bh/img.height); return img.resize((max(1,int(img.width*r)),max(1,int(img.height*r))),Image.LANCZOS)
def browser(im,imgpath,box,rad=24):
    x,y,w,h=box; c=Image.new("RGBA",(w,h),(0,0,0,0)); ImageDraw.Draw(c).rounded_rectangle([0,0,w-1,h-1],rad,fill=WHITE+(255,))
    sh=Image.new("RGBA",(w+80,h+80),(0,0,0,0)); ImageDraw.Draw(sh).rounded_rectangle([40,52,40+w,52+h],rad,fill=(6,10,30,90))
    im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(22)),(x-40,y-40)); im.alpha_composite(c,(x,y))
    d=ImageDraw.Draw(im)
    for i,cx in enumerate([x+28,x+58,x+88]): d.ellipse([cx-7,y+20,cx+7,y+34],fill=[(255,95,86),(255,189,46),(39,201,63)][i]+(255,))
    m=fit(load(imgpath),w-32,h-66); im.alpha_composite(m,(x+(w-m.width)//2,y+48+(h-66-m.height)//2))
def pill(d,txt,cx,cy,fs,fg=WHITE,bg=BLUE,padx=38,pady=20):
    f=P700(fs); w=d.textbbox((0,0),txt,font=f)[2]; d.rounded_rectangle([cx-w//2-padx,cy-pady-fs//2,cx+w//2+padx,cy+pady+fs//2],36,fill=bg+(255,))
    d.text((cx,cy),txt,font=f,fill=fg,anchor="mm")
def lower(im,txt):
    d=ImageDraw.Draw(im); f=P700(40); w=d.textbbox((0,0),txt,font=f)[2]
    d.rounded_rectangle([80,H-150,80+w+64,H-80],20,fill=BLUE+(240,)); d.text((112,H-115),txt,font=f,fill=WHITE,anchor="lm")
def mask(diam):
    m=Image.new("L",(diam,diam),0); ImageDraw.Draw(m).ellipse([0,0,diam-1,diam-1],fill=255); m.save(f"masks/circle{diam}.png")

# P1 chaos
cover(load(f"{GEN}/img1-chaos.jpg")).convert("RGB").save("frames169/p1.png")
# P2 fondateur : Mika gauche (live) + panneau texte droite
im=cover(load(f"{GEN}/img1-chaos.jpg")).filter(ImageFilter.GaussianBlur(30)); im.alpha_composite(Image.new("RGBA",(W,H),(10,14,30,150)))
d=ImageDraw.Draw(im); d.text((980,300),"Michael — 20 ans en cuisine",font=P700(38),fill=(150,190,255),anchor="lm")
for i,l in enumerate(wrap(d,"Le pire ennemi d'un chef, c'est la paperasse.",P800(62),820)): d.text((980,380+i*78),l,font=P800(62),fill=WHITE,anchor="lm")
im.convert("RGB").save("frames169/p2.png"); mask(620)
# P3 split
im=Image.new("RGBA",(W,H),(240,243,250,255))
im.paste(cover(load(f"{GEN}/img1-chaos.jpg").convert("L").convert("RGBA"),W//2,H),(0,0))
d=ImageDraw.Draw(im); d.rectangle([W//2,0,W,H],fill=(238,242,251,255)); d.line([W//2,0,W//2,H],fill=(255,255,255,255),width=8)
browser(im,f"{SCR}/checklist-hygiene.png",(W//2+70,150,760,760)); d.text((W//4,140),"AVANT",font=P800(46),fill=(225,225,232),anchor="mm")
pill(d,"Ça, c'était avant.",W//2,H-90,42,fg=WHITE,bg=BLUE); im.convert("RGB").save("frames169/p3.png")
# P4 chat Claude (landscape)
PROMPT="Importe ma carte et crée tous mes produits"
def chat(nch,check=False):
    im=cover(load(f"{GEN}/img4-chat-bg.jpg")); d=ImageDraw.Draw(im)
    d.text((140,210),"DÉMO · UNE PHRASE",font=P700(32),fill=ORANGE,anchor="lm")
    cl=fit(CLAUDE,200,56); d.rounded_rectangle([140,260,380,326],14,fill=(38,38,60,255)); im.alpha_composite(cl,(158,268))
    f=P600(46); shown=PROMPT[:nch]; lines=wrap(d,shown,f,1400) if shown else [""]; bh=max(len(lines),1)*60+50
    d.rounded_rectangle([140,370,1780,370+bh],24,fill=(48,48,80,255)); yy=405
    for l in lines: d.text((176,yy),l,font=f,fill=(230,230,248),anchor="lm"); yy+=60
    if check:
        cy=370+bh+40; d.ellipse([140,cy,200,cy+60],fill=GREEN+(255,)); d.line([156,cy+31,170,cy+45],fill=WHITE,width=8); d.line([170,cy+45,194,cy+15],fill=WHITE,width=8)
        d.text((224,cy+30),"Exécuté par votre IA",font=P700(44),fill=(140,230,160),anchor="lm")
    return im
seq=list(range(0,len(PROMPT)+1,2))+[len(PROMPT)]
for i,n in enumerate(seq): chat(n).convert("RGB").save(f"frames169/p4type/{i:03d}.png")
chat(len(PROMPT),check=True).convert("RGB").save("frames169/p4check.png")
im=cover(load(f"{GEN}/img4-chat-bg.jpg")); browser(im,f"{SCR}/ajout-produit.png",(560,150,800,780))
d=ImageDraw.Draw(im); d.ellipse([140,180,196,236],fill=GREEN+(255,)); d.line([154,208,166,220],fill=WHITE,width=7); d.line([166,220,190,194],fill=WHITE,width=7)
d.text((220,208),"Exécuté par votre IA",font=P700(40),fill=(140,230,160),anchor="lm"); im.convert("RGB").save("frames169/p4cut.png")
# P5 carrousel 4
mods=[("configuration-recette","Recettes & coûts"),("mes-productions","Stocks & productions"),("pointage","Planning & équipe"),("checklist-hygiene","HACCP & conformité")]
for i,(scr,label) in enumerate(mods):
    im=Image.new("RGBA",(W,H),(244,247,252,255))
    g=Image.new("RGBA",(W,H),(0,0,0,0)); ImageDraw.Draw(g).ellipse([W-500,-160,W+140,420],fill=BLUE+(22,)); im.alpha_composite(g.filter(ImageFilter.GaussianBlur(80)))
    browser(im,f"{SCR}/{scr}.png",(560,150,800,780)); d=ImageDraw.Draw(im)
    d.text((140,300),"Vous pilotez.",font=P800(70),fill=NAVY,anchor="lm"); d.text((140,390),"L'IA exécute.",font=P800(70),fill=BLUE,anchor="lm")
    lower(im,label); im.convert("RGB").save(f"frames169/p5_{i}.png")
# P6 offre
im=cover(load(f"{GEN}/img2-offre.jpg")); im.alpha_composite(Image.new("RGBA",(W,H),(6,14,40,120))); d=ImageDraw.Draw(im)
pill(d,"OFFRE BÊTA-TESTEUR",W//2,220,34,fg=(10,20,50),bg=(255,209,102),padx=40)
d.text((W/2,470),"-50%",font=P800(260),fill=WHITE,anchor="mm"); d.text((W/2,640),"sur votre abonnement pendant 6 mois",font=P700(44),fill=(210,225,255),anchor="mm")
pill(d,"30 places bêta",W//2,780,48,fg=WHITE,bg=BLUE,padx=48); d.text((W/2,900),"Jusqu'au 31 août 2026 · 1 call/mois + témoignage à 3 mois",font=P600(36),fill=(190,208,245),anchor="mm")
im.convert("RGB").save("frames169/p6.png")
# P7 sérénité + CTA
im=cover(load(f"{GEN}/img3-serenite.jpg")); im.alpha_composite(Image.new("RGBA",(W,H),(8,14,34,110))); d=ImageDraw.Draw(im)
d.text((980,430),"30 places.",font=P800(80),fill=WHITE,anchor="lm"); d.text((980,530),"Pas une de plus.",font=P800(80),fill=WHITE,anchor="lm")
pill(d,"Réservez votre place",1300,700,48,fg=WHITE,bg=ORANGE,padx=50); pill(d,"Lien en bio",1300,820,44,fg=(10,20,50),bg=WHITE,padx=50)
im.convert("RGB").save("frames169/p7.png"); mask(360)
print("frames169 OK · type",len(seq))
