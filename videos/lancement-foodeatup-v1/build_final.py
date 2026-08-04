#!/usr/bin/env python3
"""V1 FINAL FoodEatUp — charte officielle. Frames bakées 9 plans (les stings 2 & 10 sont des clips).
Charte : fond #0F1A23 dominant, bleu #007BFF, orange #FFA500, crème #FCF9E6. Texte noir sur fond coloré.
Filigrane mark ∞ haut-gauche. (Goodly indispo → Poppins.)"""
import os, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
HERE=os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
BASE="/home/user/Video"; FD=f"{BASE}/videos/rapidocms-presentation-4min/assets/fonts"
LOGO=f"{BASE}/studio-video/assets/brand/logo"; SCR=f"{BASE}/assets/screens/foodeatup"; GEN="assets-generes"
def F(n,s): return ImageFont.truetype(os.path.join(FD,n),s)
P800=lambda s:F("Poppins-800.ttf",s); P700=lambda s:F("Poppins-700.ttf",s); P600=lambda s:F("Poppins-600.ttf",s)
ANTH=(15,26,35); BLUE=(0,123,255); ORANGE=(255,165,0); CREAM=(252,249,230); WHITE=(255,255,255); INK=(35,31,32); SKY=(166,208,255)
CLAUDE=Image.open(f"{BASE}/videos/rapidocms-presentation-4min/assets/rapidocms/logo-claude.png").convert("RGBA")
MARK=Image.open(f"{LOGO}/foodeatup-mark-eight.png").convert("RGBA")
W,H=1080,1920
os.makedirs("ffin",exist_ok=True); os.makedirs("ffin/p5type",exist_ok=True); os.makedirs("masks",exist_ok=True)
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
def anth_bg(halo=True):
    im=Image.new("RGBA",(W,H),ANTH+(255,))
    if halo:
        g=Image.new("RGBA",(W,H),(0,0,0,0)); ImageDraw.Draw(g).ellipse([W//2-360,700,W//2+360,1420],fill=SKY+(30,))
        im.alpha_composite(g.filter(ImageFilter.GaussianBlur(140)))
    return im
def watermark(im):
    m=MARK.resize((70,140),Image.LANCZOS); a=m.split()[3].point(lambda p:int(p*0.4)); m.putalpha(a)
    im.alpha_composite(m,(60,300))
def browser(im,imgpath,box,rad=24,frame=BLUE):
    x,y,w,h=box; c=Image.new("RGBA",(w,h),(0,0,0,0)); ImageDraw.Draw(c).rounded_rectangle([0,0,w-1,h-1],rad,fill=WHITE+(255,),outline=frame+(255,),width=6)
    sh=Image.new("RGBA",(w+80,h+80),(0,0,0,0)); ImageDraw.Draw(sh).rounded_rectangle([40,52,40+w,52+h],rad,fill=(0,0,0,120))
    im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(26)),(x-40,y-40)); im.alpha_composite(c,(x,y))
    d=ImageDraw.Draw(im)
    for i,cx in enumerate([x+30,x+64,x+98]): d.ellipse([cx-8,y+22,cx+8,y+38],fill=[(255,95,86),(255,189,46),(39,201,63)][i]+(255,))
    m=fit(load(imgpath),w-40,h-78); im.alpha_composite(m,(x+(w-m.width)//2,y+54+(h-78-m.height)//2))
def pill(d,txt,cx,cy,fs,bg=BLUE,fg=INK,padx=42,pady=22):
    f=P700(fs); w=d.textbbox((0,0),txt,font=f)[2]; d.rounded_rectangle([cx-w//2-padx,cy-pady-fs//2,cx+w//2+padx,cy+pady+fs//2],40,fill=bg+(255,)); d.text((cx,cy),txt,font=f,fill=fg,anchor="mm")
def carton(im,txt,bg=BLUE,fg=INK):
    d=ImageDraw.Draw(im); f=P800(66); w=d.textbbox((0,0),txt,font=f)[2]; y=1500
    d.rounded_rectangle([(W-w)//2-46,y-16,(W+w)//2+46,y+100],30,fill=bg+(240,)); d.text((W/2,y+42),txt,font=f,fill=fg,anchor="mm")
def mask(diam):
    m=Image.new("L",(diam,diam),0); ImageDraw.Draw(m).ellipse([0,0,diam-1,diam-1],fill=255); m.save(f"masks/circle{diam}.png")

# P1 hook — image chaos brute
cover(load(f"{GEN}/img1-chaos.jpg")).convert("RGB").save("ffin/p1.png")

# P3 Mika (fond anthracite + halo) + carton
im=anth_bg(); watermark(im); carton(im,"Ça, c'était avant.")
im.convert("RGB").save("ffin/p3.png"); mask(560)

# P4 split papier|écran (charte)
im=Image.new("RGBA",(W,H),ANTH+(255,))
left=cover(load(f"{GEN}/img1-chaos.jpg").convert("L").convert("RGBA"),W//2,H); im.paste(left,(0,0))
d=ImageDraw.Draw(im); d.rectangle([W//2,0,W,H],fill=ANTH+(255,))
browser(im,f"{SCR}/checklist-hygiene.png",(W//2+40,560,W//2-90,760))
d.line([W//2,0,W//2,H],fill=BLUE+(255,),width=8); watermark(im)
carton(im,"Fini le papier.")
im.convert("RGB").save("ffin/p4.png")

# P5 chat Claude machine à écrire (SR-01 substitut)
PROMPT="Importe ma carte : crée tous mes produits."
def chat(nch,check=False):
    im=cover(load(f"{GEN}/img4-chat-bg.jpg")); watermark(im); d=ImageDraw.Draw(im)
    d.text((70,320),"DÉMO · UNE PHRASE",font=P700(34),fill=ORANGE,anchor="lm")
    cl=fit(CLAUDE,210,60); d.rounded_rectangle([70,380,320,456],16,fill=(30,42,54,255)); im.alpha_composite(cl,(90,388))
    f=P600(44); shown=PROMPT[:nch]; lines=wrap(d,shown,f,860) if shown else [""]; bh=max(len(lines),1)*58+56
    d.rounded_rectangle([70,490,1010,490+bh],26,fill=(28,40,52,255),outline=BLUE+(255,),width=3); yy=525
    for l in lines: d.text((100,yy),l,font=f,fill=(235,242,250),anchor="lm"); yy+=58
    cy=490+bh+50
    if check:
        d.ellipse([70,cy,132,cy+62],fill=ORANGE+(255,)); d.line([86,cy+32,100,cy+46],fill=INK,width=8); d.line([100,cy+46,126,cy+16],fill=INK,width=8)
        d.text((156,cy+31),"Créé par votre IA",font=P700(42),fill=ORANGE,anchor="lm")
    return im
seq=list(range(0,len(PROMPT)+1,2))+[len(PROMPT)]
for i,n in enumerate(seq): chat(n).convert("RGB").save(f"ffin/p5type/{i:03d}.png")
chat(len(PROMPT),check=True).convert("RGB").save("ffin/p5check.png")

# P6 produit + flash (SR-02 substitut)
im=cover(load(f"{GEN}/img4-chat-bg.jpg")); watermark(im); browser(im,f"{SCR}/ajout-produit.png",(80,470,920,1000))
d=ImageDraw.Draw(im); d.ellipse([70,300,126,356],fill=ORANGE+(255,)); d.line([84,328,96,340],fill=INK,width=7); d.line([96,340,120,314],fill=INK,width=7)
d.text((150,328),"Créé par votre IA",font=P700(40),fill=ORANGE,anchor="lm")
im.convert("RGB").save("ffin/p6.png")

# P7 carrousel 4 modules (charte : lower-third bleu, texte noir)
mods=[("configuration-recette","Recettes & coûts"),("mes-productions","Stocks"),("pointage","Planning & équipe"),("checklist-hygiene","HACCP")]
for i,(scr,label) in enumerate(mods):
    im=anth_bg(halo=False); g=Image.new("RGBA",(W,H),(0,0,0,0)); ImageDraw.Draw(g).ellipse([W-420,-140,W+120,360],fill=BLUE+(40,)); im.alpha_composite(g.filter(ImageFilter.GaussianBlur(90)))
    watermark(im); browser(im,f"{SCR}/{scr}.png",(90,540,900,820))
    d=ImageDraw.Draw(im); pill(d,label.upper(),W//2,1440,34,bg=BLUE,fg=INK)
    d.text((W/2,380),"Vous pilotez. L'IA exécute.",font=P800(52),fill=WHITE,anchor="mm")
    im.convert("RGB").save(f"ffin/p7_{i}.png")

# P8 OFFRE (charte : fond anthracite/bleu, -50% orange)
im=cover(load(f"{GEN}/img2-offre-v2.jpg")); sc=Image.new("RGBA",(W,H),ANTH+(120,)); im.alpha_composite(sc); watermark(im); d=ImageDraw.Draw(im)
pill(d,"OFFRE BÊTA-TESTEUR",W//2,470,36,bg=ORANGE,fg=INK,padx=44)
d.text((W/2,830),"-50%",font=P800(300),fill=ORANGE,anchor="mm")
d.text((W/2,1015),"sur votre abonnement",font=P700(46),fill=WHITE,anchor="mm")
pill(d,"30 places bêta",W//2,1200,52,bg=BLUE,fg=INK,padx=52)
d.text((W/2,1330),"Jusqu'au 31 août 2026",font=P700(44),fill=SKY,anchor="mm")
d.text((W/2,1420),"6 mois · 1 call/mois + témoignage à 3 mois",font=P600(34),fill=(190,208,235),anchor="mm")
im.convert("RGB").save("ffin/p8.png")

# P9 hook de fin (sérénité + Mika + CTA)
im=cover(load(f"{GEN}/img3-serenite.jpg")); sc=Image.new("RGBA",(W,H),ANTH+(96,)); im.alpha_composite(sc); watermark(im); d=ImageDraw.Draw(im)
d.text((W/2,1330),"30 places. Pas une de plus.",font=P800(56),fill=WHITE,anchor="mm")
pill(d,"Réservez votre place",W//2,1470,46,bg=ORANGE,fg=INK,padx=52)
pill(d,"Lien en bio",W//2,1590,44,bg=WHITE,fg=INK,padx=52)
im.convert("RGB").save("ffin/p9.png"); mask(300)
print("V1 FINAL frames OK; p5 type:",len(seq))
