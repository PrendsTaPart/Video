#!/usr/bin/env python3
"""Compose FoodEatUp 5-min tutorial frames (1080x1920, light brand theme).
Stills: intro, 18 steps, outro. Phase bases (avatar overlaid later by ffmpeg)."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

W,H=1080,1920
BG=(247,249,251); BLUE=(30,134,255); ORANGE=(247,148,30)
NAVY=(23,42,69); INK=(45,55,68); MUTED=(120,133,150); WHITE=(255,255,255)
FD="assets/fonts"
def F(n,s): return ImageFont.truetype(os.path.join(FD,n),s)
P800=lambda s:F("Poppins-800.ttf",s); P700=lambda s:F("Poppins-700.ttf",s)
P600=lambda s:F("Poppins-600.ttf",s); P400=lambda s:F("Poppins-400.ttf",s)
os.makedirs("frames",exist_ok=True)

logo=Image.open("assets/logo/foodeatup.png").convert("RGBA")
logo_wm=logo.crop((60,120,1420,410))   # wordmark+chef, drop tagline

# avatar PiP geometry (shared with assemble)
PW,PH,PX,PY=440,560,580,600
border=Image.open("assets/avatar/border.png").convert("RGBA")

def bg_base():
    im=Image.new("RGBA",(W,H),BG+(255,))
    g=Image.new("RGBA",(W,H),(0,0,0,0)); gd=ImageDraw.Draw(g)
    gd.ellipse([W-360,-160,W+160,360],fill=BLUE+(22,))
    gd.ellipse([-160,H-360,360,H+160],fill=ORANGE+(20,))
    im.alpha_composite(g.filter(ImageFilter.GaussianBlur(80)))
    return im

def header(im,pill_text,pill_col):
    lw=300; lh=int(logo_wm.height*lw/logo_wm.width)
    im.alpha_composite(logo_wm.resize((lw,lh),Image.LANCZOS),(70,92))
    d=ImageDraw.Draw(im); f=P700(38)
    tw=d.textbbox((0,0),pill_text,font=f)[2]; pw,ph=tw+52,64; px,py=W-70-pw,100
    d.rounded_rectangle([px,py,px+pw,py+ph],32,fill=pill_col+(255,))
    d.text((px+pw/2,py+ph/2),pill_text,font=f,fill=WHITE,anchor="mm")

def wrap(d,text,font,maxw):
    out=[]
    for para in text.split("\n"):
        cur=""
        for w in para.split():
            t=(cur+" "+w).strip()
            if d.textbbox((0,0),t,font=font)[2]<=maxw: cur=t
            else: out.append(cur); cur=w
        out.append(cur)
    return out

def caption(im,text,col=BLUE,y=1560):
    d=ImageDraw.Draw(im); f=P700(44); maxw=900
    lines=wrap(d,text,f,maxw); lh=58; th=lh*len(lines); pad=36
    tw=max(d.textbbox((0,0),l,font=f)[2] for l in lines)
    pw=min(tw+pad*2,W-80); ph=th+pad*2-6; px=(W-pw)//2
    d.rounded_rectangle([px,y,px+pw,y+ph],36,fill=col+(240,))
    yy=y+pad-3
    for l in lines: d.text((W/2,yy+lh/2),l,font=f,fill=WHITE,anchor="mm"); yy+=lh

def fit(img,bw,bh):
    r=min(bw/img.width,bh/img.height); return img.resize((int(img.width*r),int(img.height*r)),Image.LANCZOS)

def screencard(im,imgs):
    # white rounded card with browser bar, fit screenshots inside
    x,y,w,h=70,560,940,760
    card=Image.new("RGBA",(w,h),(0,0,0,0)); ImageDraw.Draw(card).rounded_rectangle([0,0,w-1,h-1],28,fill=WHITE+(255,))
    sh=Image.new("RGBA",(w+80,h+80),(0,0,0,0))
    ImageDraw.Draw(sh).rounded_rectangle([40,50,40+w,50+h],28,fill=(23,42,69,60))
    im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(22)),(x-40,y-40))
    im.alpha_composite(card,(x,y))
    d=ImageDraw.Draw(im)
    for i,cx in enumerate([x+34,x+70,x+106]):
        d.ellipse([cx-9,y+27,cx+9,y+45],fill=[(255,95,86),(255,189,46),(39,201,63)][i]+(255,))
    d.line([x+150,y+36,x+w-40,y+36],fill=(225,230,238),width=0)
    # image area
    ax,ay,aw,ah=x+24,y+72,w-48,h-96
    if len(imgs)==1:
        im2=fit(imgs[0],aw,ah); im.alpha_composite(im2,(ax+(aw-im2.width)//2,ay+(ah-im2.height)//2))
    else:
        gap=20; cw=(aw-gap)//2
        for i,g in enumerate(imgs[:2]):
            im2=fit(g,cw,ah); ox=ax+i*(cw+gap)+(cw-im2.width)//2; oy=ay+(ah-im2.height)//2
            im.alpha_composite(im2,(ox,oy))

def title_block(im,eyebrow,title,ey_col=ORANGE):
    d=ImageDraw.Draw(im)
    d.text((70,250),eyebrow.upper(),font=P700(38),fill=ey_col,anchor="lm")
    f=P800(62); lines=wrap(d,title,f,940); y=300
    for l in lines: d.text((70,y+38),l,font=f,fill=NAVY,anchor="lm"); y+=76

def load(p):
    if not p.startswith("assets/"): p="assets/"+p
    return Image.open(p).convert("RGBA")

PHASES={1:"Votre compte & votre boutique",2:"Fondations de configuration",3:"Connecter votre IA",
4:"Remplir votre contenu avec l'IA",5:"Votre équipe (RH)",6:"Hygiène & conformité (HACCP)",7:"Exploitation & pilotage"}

STEPS=[
("s11",1,1,"Créer votre compte","Email, mot de passe, profil & abonnement",["screens/s11b.png","screens/s11.png"]),
("s12",2,1,"Créer votre établissement","« Créer un établissement » — web uniquement",["screens/s12.png"]),
("s21",3,2,"Configurer votre TVA","Vos taux : 20%, 10%, 5,5%",["screens/s21.png"]),
("s22",4,2,"Créer vos catégories","Entrées, plats, desserts, boissons…",["screens/s22.png"]),
("s31",5,3,"Connecter FoodEatUp à votre IA","MCP · Claude, Mistral, ChatGPT, WhatsApp",["screens/s31.png"]),
("s41",6,4,"Importer votre carte","PDF ou photo : tous vos produits, par l'IA",["screens/s41.png"]),
("s42",7,4,"Créer vos ingrédients","Unité, prix, stock, seuil d'alerte",["screens/s42.png"]),
("s43",8,4,"Créer vos recettes","Coût matière + prix de vente conseillé",["screens/s43.png"]),
("s44",9,4,"Composer « Ma carte »","Glisser-déposer, activer / masquer",["screens/s44.png"]),
("s45",10,4,"Ajouter vos fournisseurs","Coordonnées, conditions, produits",["screens/s45.png"]),
("s51",11,5,"Employés, rôles & QR","Permissions par module + pointage",["screens/s51.png","screens/s51b.png"]),
("s52",12,5,"Plannings, pointages & congés","Horaires, heures, absences",["screens/s52.png","screens/s52b.png"]),
("s61",13,6,"Équipements & températures","Chambres froides, alertes de seuil",["screens/s61.png"]),
("s62",14,6,"Étiquettes DLC & traçabilité","Lots + contrôle à réception",["gen/p6.jpg"]),
("s63",15,6,"Plan de nettoyage & checklists","Export PDF pour vos contrôles",["screens/s63.png","screens/s63b.png"]),
("s71",16,7,"Stocks, courses & production","Déduction auto des ingrédients",["screens/s71.png"]),
("s72",17,7,"Clients, devis & factures","TVA, remises, acompte — en 1 clic",["screens/s72.png"]),
("s73",18,7,"PrediBot & bilan","Prédictions + synthèse financière",["gen/p7.jpg"]),
]

# ---- intro ----
im=bg_base(); header(im,"5 min",BLUE)
d=ImageDraw.Draw(im)
d.text((W/2,300),"TUTORIEL",font=P700(44),fill=ORANGE,anchor="mm")
d.text((W/2,390),"FoodEatUp",font=P800(120),fill=BLUE,anchor="mm")
for i,l in enumerate(wrap(d,"Configurez votre restaurant\nen 5 minutes, piloté par l'IA",P600(44),920)):
    d.text((W/2,500+i*58),l,font=P600(44),fill=INK,anchor="mm")
ill=fit(load("assets/gen/intro.jpg"),760,760); im.alpha_composite(ill,((W-ill.width)//2,640))
caption(im,"18 étapes · 7 phases",y=1560)
im.convert("RGB").save("frames/intro.png"); print("intro")

# ---- phase bases (avatar overlaid later) ----
for p,name in PHASES.items():
    im=bg_base(); header(im,f"PHASE {p}/7",ORANGE)
    d=ImageDraw.Draw(im)
    d.text((70,250),f"PHASE {p}",font=P800(64),fill=ORANGE,anchor="lm")
    for i,l in enumerate(wrap(d,name,P800(58),480)):
        d.text((70,340+i*70),l,font=P800(58),fill=NAVY,anchor="lm")
    ill=fit(load(f"assets/gen/p{p}.jpg"),470,760); im.alpha_composite(ill,(60,560))
    # avatar border placeholder
    im.alpha_composite(border,(PX,PY))
    caption(im,name,y=1470)
    im.convert("RGB").save(f"frames/phase{p}.png"); print("phase",p)

# ---- steps ----
for sid,n,p,title,cap,imgs in STEPS:
    im=bg_base(); header(im,f"{n}/18",BLUE)
    title_block(im,f"Étape {n} · Phase {p}",title)
    screencard(im,[load(x) for x in imgs])
    caption(im,cap,y=1560)
    im.convert("RGB").save(f"frames/{sid}.png"); print(sid)

# ---- outro ----
im=bg_base(); header(im,"Academy",ORANGE)
d=ImageDraw.Draw(im)
d.text((W/2,290),"BRAINDCODE ACADEMY",font=P700(40),fill=ORANGE,anchor="mm")
for i,l in enumerate(wrap(d,"Réservez votre démo\nou un coaching IA",P800(70),920)):
    d.text((W/2,380+i*84),l,font=P800(70),fill=BLUE,anchor="mm")
ill=fit(load("assets/gen/cta.jpg"),720,720); im.alpha_composite(ill,((W-ill.width)//2,600))
# url pill
url="foodeatup.com"; f=P700(52); tw=d.textbbox((0,0),url,font=f)[2]; pw,ph=tw+90,108; px=(W-pw)//2; py=1400
d.rounded_rectangle([px,py,px+pw,py+ph],54,fill=BLUE+(255,)); d.text((W/2,py+ph/2),url,font=f,fill=WHITE,anchor="mm")
caption(im,"FoodEatUp — un produit BraindCode",col=ORANGE,y=1580)
im.convert("RGB").save("frames/outro.png"); print("outro")
print("ALL FRAMES DONE")
