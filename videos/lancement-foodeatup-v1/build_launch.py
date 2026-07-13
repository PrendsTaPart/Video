#!/usr/bin/env python3
"""Compositeur V1 Lancement FoodEatUp — génère les frames bakées des 7 plans (9:16, 1080x1920).
Overlays texte (safe zones), split-screen, scène chat Claude (machine à écrire), bloc offre.
Le mouvement (zoom, pulse) + médaillon Mika live + audio sont ajoutés par assemble_launch.py."""
import os, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
HERE=os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
BASE="/home/user/Video"
FD=f"{BASE}/videos/rapidocms-presentation-4min/assets/fonts"
def F(n,s): return ImageFont.truetype(os.path.join(FD,n),s)
P800=lambda s:F("Poppins-800.ttf",s); P700=lambda s:F("Poppins-700.ttf",s); P600=lambda s:F("Poppins-600.ttf",s)
BLUE=(11,110,253); ORANGE=(247,148,30); WHITE=(255,255,255); NAVY=(20,24,46); DARK=(14,14,26); GREEN=(39,201,99)
CLAUDE=Image.open(f"{BASE}/videos/rapidocms-presentation-4min/assets/rapidocms/logo-claude.png").convert("RGBA")
W,H=1080,1920
os.makedirs("frames",exist_ok=True); os.makedirs("frames/p4type",exist_ok=True); os.makedirs("masks",exist_ok=True)
A="assets/screens/foodeatup"; SCR=f"{BASE}/assets/screens/foodeatup"; GEN="assets-generes"

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
def browser(im,imgpath,box,rad=26):
    x,y,w,h=box; c=Image.new("RGBA",(w,h),(0,0,0,0)); ImageDraw.Draw(c).rounded_rectangle([0,0,w-1,h-1],rad,fill=WHITE+(255,))
    sh=Image.new("RGBA",(w+80,h+80),(0,0,0,0)); ImageDraw.Draw(sh).rounded_rectangle([40,52,40+w,52+h],rad,fill=(6,10,30,90))
    im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(24)),(x-40,y-40)); im.alpha_composite(c,(x,y))
    d=ImageDraw.Draw(im)
    for i,cx in enumerate([x+30,x+64,x+98]): d.ellipse([cx-8,y+22,cx+8,y+38],fill=[(255,95,86),(255,189,46),(39,201,63)][i]+(255,))
    m=fit(load(imgpath),w-36,h-74); im.alpha_composite(m,(x+(w-m.width)//2,y+52+(h-74-m.height)//2))
def pill(d,txt,cx,cy,fs,fg=WHITE,bg=BLUE,padx=40,pady=22):
    f=P700(fs); w=d.textbbox((0,0),txt,font=f)[2]; d.rounded_rectangle([cx-w//2-padx,cy-pady-fs//2,cx+w//2+padx,cy+pady+fs//2],40,fill=bg+(255,))
    d.text((cx,cy),txt,font=f,fill=fg,anchor="mm")
def carton(im,txt,accent=BLUE):
    d=ImageDraw.Draw(im); f=P800(64); w=d.textbbox((0,0),txt,font=f)[2]
    y=1500; d.rounded_rectangle([(W-w)//2-46,y-16,(W+w)//2+46,y+96],30,fill=accent+(240,))
    d.text((W/2,y+40),txt,font=f,fill=WHITE,anchor="mm")

def mask(diam):
    m=Image.new("L",(diam,diam),0); ImageDraw.Draw(m).ellipse([0,0,diam-1,diam-1],fill=255)
    m.save(f"masks/circle{diam}.png")

# ---- Plan 1 : chaos (image #1), pas de texte
cover(load(f"{GEN}/img1-chaos.jpg")).convert("RGB").save("frames/p1.png")

# ---- Plan 2 : Mika buste (fond cuisine flou) + carton
bg=cover(load(f"{GEN}/img1-chaos.jpg")).filter(ImageFilter.GaussianBlur(28))
ov=Image.new("RGBA",(W,H),(10,14,30,120)); bg.alpha_composite(ov)
carton(bg,"Et pourtant…")
bg.convert("RGB").save("frames/p2.png"); mask(560)

# ---- Plan 3 : split-screen papier | écran FoodEatUp + carton
im=Image.new("RGBA",(W,H),(240,243,250,255))
left=cover(load(f"{GEN}/img1-chaos.jpg").convert("L").convert("RGBA"),W//2,H)  # papiers, désaturé
im.paste(left,(0,0))
d=ImageDraw.Draw(im); d.rectangle([W//2,0,W,H],fill=(238,242,251,255))
browser(im,f"{SCR}/checklist-hygiene.png",(W//2+40,560,W//2-90,760))
d.line([W//2,0,W//2,H],fill=(255,255,255,255),width=8)
d.text((W//4,300),"AVANT",font=P800(48),fill=(230,230,235),anchor="mm")
carton(im,"Ça, c'était avant.")
im.convert("RGB").save("frames/p3.png")

# ---- Plan 4 : scène chat Claude (machine à écrire) sur image #4
PROMPT="Importe ma carte et crée tous mes produits"
def chat_frame(nchars, check=False):
    im=cover(load(f"{GEN}/img4-chat-bg.jpg")); d=ImageDraw.Draw(im)
    d.text((70,300),"DÉMO · UNE PHRASE",font=P700(34),fill=ORANGE,anchor="lm")
    cl=fit(CLAUDE,210,60); d.rounded_rectangle([70,360,320,436],16,fill=(38,38,60,255)); im.alpha_composite(cl,(90,368))
    f=P600(44); shown=PROMPT[:nchars]; lines=wrap(d,shown,f,860) if shown else [""]
    bh=max(len(lines),1)*58+56
    d.rounded_rectangle([70,470,1010,470+bh],26,fill=(48,48,80,255)); yy=505
    for l in lines: d.text((100,yy),l,font=f,fill=(230,230,248),anchor="lm"); yy+=58
    if not check and nchars<len(PROMPT):  # curseur
        cw=d.textbbox((0,0),lines[-1],font=f)[2]; d.rectangle([100+cw+6,yy-58,100+cw+12,yy-8],fill=WHITE)
    cy=470+bh+50
    if check:
        d.ellipse([70,cy,132,cy+62],fill=GREEN+(255,)); d.line([86,cy+32,100,cy+46],fill=WHITE,width=8); d.line([100,cy+46,126,cy+16],fill=WHITE,width=8)
        d.text((156,cy+31),"Exécuté par votre IA",font=P700(42),fill=(140,230,160),anchor="lm")
    return im
# séquence machine à écrire (~ 1 frame / 2 chars) + hold check
seq=list(range(0,len(PROMPT)+1,2))+[len(PROMPT)]
for i,n in enumerate(seq): chat_frame(n).convert("RGB").save(f"frames/p4type/{i:03d}.png")
chat_frame(len(PROMPT),check=True).convert("RGB").save("frames/p4check.png")
# cut sur capture produit (même fond sombre)
im=cover(load(f"{GEN}/img4-chat-bg.jpg")); browser(im,f"{SCR}/ajout-produit.png",(80,470,920,1000))
d=ImageDraw.Draw(im); d.ellipse([70,300,126,356],fill=GREEN+(255,)); d.line([84,328,96,340],fill=WHITE,width=7); d.line([96,340,120,314],fill=WHITE,width=7)
d.text((150,328),"Exécuté par votre IA",font=P700(40),fill=(140,230,160),anchor="lm")
im.convert("RGB").save("frames/p4cut.png")
print("p4 type frames:",len(seq))

# ---- Plan 5 : carrousel 4 modules (baké en 4 cartes)
mods=[("configuration-recette","Recettes & coûts"),("mes-productions","Stocks & productions"),
      ("pointage","Planning & équipe"),("checklist-hygiene","HACCP & conformité")]
for i,(scr,label) in enumerate(mods):
    im=Image.new("RGBA",(W,H),(244,247,252,255))
    g=Image.new("RGBA",(W,H),(0,0,0,0)); ImageDraw.Draw(g).ellipse([W-420,-140,W+120,360],fill=BLUE+(24,)); im.alpha_composite(g.filter(ImageFilter.GaussianBlur(80)))
    browser(im,f"{SCR}/{scr}.png",(90,520,900,820))
    d=ImageDraw.Draw(im); pill(d,label.upper(),W//2,1440,34,fg=WHITE,bg=BLUE)
    d.text((W/2,360),"Vous pilotez. L'IA exécute.",font=P800(52),fill=NAVY,anchor="mm")
    im.convert("RGB").save(f"frames/p5_{i}.png")

# ---- Plan 6 : BLOC OFFRE sur image #2
im=cover(load(f"{GEN}/img2-offre.jpg")); sc=Image.new("RGBA",(W,H),(6,14,40,120)); im.alpha_composite(sc)
d=ImageDraw.Draw(im)
pill(d,"OFFRE BÊTA-TESTEUR",W//2,470,36,fg=(10,20,50),bg=(255,209,102),padx=44)
# grand -50%
f=P800(300); d.text((W/2,820),"-50%",font=f,fill=WHITE,anchor="mm")
d.text((W/2,1010),"sur votre abonnement",font=P700(46),fill=(210,225,255),anchor="mm")
pill(d,"30 places bêta",W//2,1200,52,fg=WHITE,bg=BLUE,padx=52)
d.text((W/2,1330),"Jusqu'au 31 août 2026",font=P700(44),fill=(220,232,255),anchor="mm")
d.text((W/2,1420),"6 mois · 1 call/mois + témoignage à 3 mois",font=P600(34),fill=(180,200,240),anchor="mm")
im.convert("RGB").save("frames/p6.png")
# variante pulse (–50% agrandi) pour animation
im2=cover(load(f"{GEN}/img2-offre.jpg")); im2.alpha_composite(sc); d2=ImageDraw.Draw(im2)
pill(d2,"OFFRE BÊTA-TESTEUR",W//2,470,36,fg=(10,20,50),bg=(255,209,102),padx=44)
d2.text((W/2,820),"-50%",font=P800(340),fill=WHITE,anchor="mm")
d2.text((W/2,1010),"sur votre abonnement",font=P700(46),fill=(210,225,255),anchor="mm")
pill(d2,"30 places bêta",W//2,1200,52,fg=WHITE,bg=BLUE,padx=52)
d2.text((W/2,1330),"Jusqu'au 31 août 2026",font=P700(44),fill=(220,232,255),anchor="mm")
d2.text((W/2,1420),"6 mois · 1 call/mois + témoignage à 3 mois",font=P600(34),fill=(180,200,240),anchor="mm")
im2.convert("RGB").save("frames/p6pulse.png")

# ---- Plan 7 : sérénité (image #3) + CTA + (Mika live à l'assemble)
im=cover(load(f"{GEN}/img3-serenite.jpg")); sc=Image.new("RGBA",(W,H),(8,14,34,90)); im.alpha_composite(sc)
d=ImageDraw.Draw(im)
d.text((W/2,1360),"30 places. Pas une de plus.",font=P800(56),fill=WHITE,anchor="mm")
pill(d,"Réservez votre place",W//2,1500,46,fg=WHITE,bg=ORANGE,padx=52)
pill(d,"Lien en bio",W//2,1620,44,fg=(10,20,50),bg=(255,255,255),padx=52)
im.convert("RGB").save("frames/p7.png"); mask(300)
print("frames OK")
