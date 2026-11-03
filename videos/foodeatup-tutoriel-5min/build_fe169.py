#!/usr/bin/env python3
"""Compose FoodEatUp tutorial frames 16:9 (1920x1080), light FoodEatUp theme.
Stills: intro, 18 steps, outro. Phase bases (avatar overlaid later by ffmpeg)."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
W,H=1920,1080
BG=(247,249,251); BLUE=(11,110,253); ORANGE=(247,148,30)
NAVY=(23,42,69); INK=(60,72,92); MUTED=(120,133,150); WHITE=(255,255,255)
SLOGAN="Une infinité de solutions pour gérer votre restaurant"
FD="assets/fonts"
def F(n,s): return ImageFont.truetype(os.path.join(FD,n),s)
P800=lambda s:F("Poppins-800.ttf",s); P700=lambda s:F("Poppins-700.ttf",s)
P600=lambda s:F("Poppins-600.ttf",s); P400=lambda s:F("Poppins-400.ttf",s)
os.makedirs("frames",exist_ok=True)

logo=Image.open("assets/logo/foodeatup.png").convert("RGBA")
logo_wm=logo.crop((60,120,1420,410))
PW,PH,PX,PY=470,660,180,340
border=Image.open("assets/avatar/border.png").convert("RGBA")

def bg_base():
    im=Image.new("RGBA",(W,H),BG+(255,)); g=Image.new("RGBA",(W,H),(0,0,0,0)); gd=ImageDraw.Draw(g)
    gd.ellipse([W-460,-200,W+220,320],fill=BLUE+(20,))
    gd.ellipse([-220,H-380,360,H+180],fill=ORANGE+(18,))
    im.alpha_composite(g.filter(ImageFilter.GaussianBlur(90))); return im

def header(im,pill,col):
    lw=300; lh=int(logo_wm.height*lw/logo_wm.width)
    im.alpha_composite(logo_wm.resize((lw,lh),Image.LANCZOS),(60,48))
    d=ImageDraw.Draw(im); f=P700(36)
    tw=d.textbbox((0,0),pill,font=f)[2]; pw,ph=tw+50,62; px,py=W-60-pw,52
    d.rounded_rectangle([px,py,px+pw,py+ph],31,fill=col+(255,)); d.text((px+pw/2,py+ph/2),pill,font=f,fill=WHITE,anchor="mm")

def wrap(d,t,f,mw):
    out=[]
    for para in t.split("\n"):
        cur=""
        for w in para.split():
            s=(cur+" "+w).strip()
            if d.textbbox((0,0),s,font=f)[2]<=mw: cur=s
            else: out.append(cur); cur=w
        out.append(cur)
    return out

def fit(img,bw,bh):
    r=min(bw/img.width,bh/img.height); return img.resize((max(1,int(img.width*r)),max(1,int(img.height*r))),Image.LANCZOS)

def load(p):
    if not p.startswith("assets"): p="assets/"+p
    return Image.open(p).convert("RGBA")

def browsercard(im,imgs,box):
    x,y,w,h=box
    card=Image.new("RGBA",(w,h),(0,0,0,0)); ImageDraw.Draw(card).rounded_rectangle([0,0,w-1,h-1],26,fill=WHITE+(255,))
    sh=Image.new("RGBA",(w+80,h+80),(0,0,0,0)); ImageDraw.Draw(sh).rounded_rectangle([40,52,40+w,52+h],26,fill=(23,42,69,55))
    im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(24)),(x-40,y-40)); im.alpha_composite(card,(x,y))
    d=ImageDraw.Draw(im)
    for i,cx in enumerate([x+32,x+66,x+100]): d.ellipse([cx-9,y+25,cx+9,y+43],fill=[(255,95,86),(255,189,46),(39,201,63)][i]+(255,))
    ax,ay,aw,ah=x+22,y+64,w-44,h-86
    if len(imgs)==1:
        im2=fit(imgs[0],aw,ah); im.alpha_composite(im2,(ax+(aw-im2.width)//2,ay+(ah-im2.height)//2))
    else:
        gap=18; cw=(aw-gap)//2
        for i,g in enumerate(imgs[:2]):
            im2=fit(g,cw,ah); im.alpha_composite(im2,(ax+i*(cw+gap)+(cw-im2.width)//2,ay+(ah-im2.height)//2))

def textpanel(im,eyebrow,title,sub):
    d=ImageDraw.Draw(im); x=80
    d.text((x,300),eyebrow.upper(),font=P700(34),fill=ORANGE,anchor="lm")
    f=P800(58); y=350
    for l in wrap(d,title,f,690): d.text((x,y+36),l,font=f,fill=NAVY,anchor="lm"); y+=72
    d.rounded_rectangle([x,y+6,x+90,y+16],5,fill=BLUE+(255,)); y+=52
    fs=P600(36)
    for l in wrap(d,sub,fs,700): d.text((x,y+24),l,font=fs,fill=INK,anchor="lm"); y+=52

# ---------- data ----------
PHASES={1:"Compte & boutique",2:"Fondations",3:"Connecter votre IA",4:"Contenu par l'IA",
5:"Équipe (RH)",6:"Hygiène & HACCP",7:"Exploitation & pilotage"}
STEPS=[
("s11",1,1,"Créer votre compte","Email, mot de passe, profil & abonnement.",["screens/foodeatup/modifier-profil.png","screens/foodeatup/connexion.png"]),
("s12",2,1,"Créer votre établissement","« Créer un établissement » — sur le web uniquement.",["screens/foodeatup/ajout-boutique.png"]),
("s21",3,2,"Configurer votre TVA","Vos taux : 20 %, 10 %, 5,5 %.",["screens/foodeatup/ajouter-tva.png"]),
("s22",4,2,"Créer vos catégories","Entrées, plats, desserts, boissons…",["screens/foodeatup/ajouter-categorie.png"]),
("s41",6,4,"Importer votre carte","PDF ou photo : tous vos produits, par l'IA.",["screens/foodeatup/ajout-produit.png"]),
("s42",7,4,"Créer vos ingrédients","Unité, prix, stock, seuil d'alerte.",["screens/foodeatup/ajouter-ingredient.png"]),
("s43",8,4,"Recettes & coût matière","Prix de vente conseillé selon votre marge.",["screens/foodeatup/configuration-recette.png"]),
("s44",9,4,"Composer « Ma carte »","Glisser-déposer, activer / masquer.",["screens/foodeatup/ajouter-plat.png"]),
("s45",10,4,"Ajouter vos fournisseurs","Coordonnées, conditions, produits fournis.",["screens/foodeatup/ajout-fournisseur.png"]),
("s51",11,5,"Employés, rôles & QR","Permissions par module + pointage QR.",["screens/foodeatup/ajout-employe.png","screens/foodeatup/qr-code-pointage.png"]),
("s52",12,5,"Plannings, pointages & congés","Horaires, heures, absences.",["screens/foodeatup/pointage.png","screens/foodeatup/demande-absence.png"]),
("s61",13,6,"Équipements & températures","Chambres froides, alertes de seuil.",["screens/foodeatup/ajouter-equipement.png"]),
("s62",14,6,"Étiquettes DLC & traçabilité","Lots + contrôle à réception.",["assets-generes/p6.jpg"]),
("s63",15,6,"Nettoyage & checklists","Export PDF pour vos contrôles.",["screens/foodeatup/zone-nettoyage.png","screens/foodeatup/checklist-hygiene.png"]),
("s71",16,7,"Stocks, courses & production","Déduction auto des ingrédients.",["screens/foodeatup/mes-productions.png"]),
("s72",17,7,"Clients, devis & factures","TVA, remises, acompte — en 1 clic.",["screens/foodeatup/ajouter-client.png"]),
("s73",18,7,"PrediBot & bilan","Prédictions + synthèse financière.",["assets-generes/p7.jpg"]),
]

def logo_row(im, y):
    """Chapter 3 : connecteurs IA + FoodEatUp mark."""
    d=ImageDraw.Draw(im)
    items=[]
    cl=load("logo/claude.png"); items.append(fit(cl,240,60))
    mi=load("logo/mistral.jpg"); items.append(fit(mi,150,80))
    x=80
    for it in items:
        im.alpha_composite(it,(x,y-it.height//2)); x+=it.width+40
    # OpenAI + WhatsApp text chips
    for txt in ["OpenAI","WhatsApp"]:
        f=P700(34); tw=d.textbbox((0,0),txt,font=f)[2]; pw=tw+44
        d.rounded_rectangle([x,y-30,x+pw,y+30],30,outline=(200,210,224,255),width=3)
        d.text((x+pw/2,y),txt,font=f,fill=NAVY,anchor="mm"); x+=pw+28

def link_pill(im,y):
    d=ImageDraw.Draw(im); txt="MCP :  https://foodeatup.com/api/mcp"; f=P700(34)
    tw=d.textbbox((0,0),txt,font=f)[2]; pw,ph=tw+56,64; x=80
    d.rounded_rectangle([x,y,x+pw,y+ph],32,fill=BLUE+(255,)); d.text((x+pw/2,y+ph/2),txt,font=f,fill=WHITE,anchor="mm")

# ---- intro ----
im=bg_base(); header(im,"5 min",BLUE); d=ImageDraw.Draw(im)
d.text((520,300),"TUTORIEL COMPLET",font=P700(40),fill=ORANGE,anchor="lm")
d.text((520,400),"FoodEatUp",font=P800(120),fill=BLUE,anchor="lm")
for i,l in enumerate(wrap(d,SLOGAN,P600(40),820)): d.text((520,510+i*54),l,font=P600(40),fill=INK,anchor="lm")
d.text((520,650),"18 étapes · 7 phases · piloté par l'IA",font=P700(38),fill=NAVY,anchor="lm")
ill=fit(load("assets-generes/intro.jpg"),620,760); im.alpha_composite(ill,(1250,150))
im.convert("RGB").save("frames/intro.png"); print("intro")

# ---- phase bases ----
for p,name in PHASES.items():
    im=bg_base(); header(im,f"PHASE {p}/7",ORANGE); d=ImageDraw.Draw(im)
    d.text((W/2,150),f"PHASE {p}",font=P800(60),fill=ORANGE,anchor="mm")
    for i,l in enumerate(wrap(d,name,P800(66),1200)): d.text((W/2,240+i*76),l,font=P800(66),fill=NAVY,anchor="mm")
    im.alpha_composite(border,(PX,PY))
    ill=fit(load(f"assets-generes/p{p}.jpg"),520,660); im.alpha_composite(ill,(1250,340))
    d.text((W/2,1010),SLOGAN,font=P600(32),fill=MUTED,anchor="mm")
    im.convert("RGB").save(f"frames/phase{p}.png"); print("phase",p)

# ---- steps ----
for sid,n,p,title,sub,imgs in STEPS:
    im=bg_base(); header(im,f"{n}/18",BLUE)
    textpanel(im,f"Étape {n} · Phase {p}",title,sub)
    browsercard(im,[load(x) for x in imgs],(840,150,1010,810))
    im.convert("RGB").save(f"frames/{sid}.png"); print(sid)

# ---- MCP step (s31) special ----
im=bg_base(); header(im,"5/18",BLUE)
textpanel(im,"Étape 5 · Phase 3","Connecter votre IA","Le MCP FoodEatUp, connecté à Claude, Mistral ou OpenAI. Et même WhatsApp.")
browsercard(im,[load("assets-generes/p3.jpg")],(840,150,1010,690))
logo_row(im,930); link_pill(im,700)
im.convert("RGB").save("frames/s31.png"); print("s31 mcp")

# ---- outro ----
im=bg_base(); header(im,"Academy",ORANGE); d=ImageDraw.Draw(im)
d.text((110,320),"BRAINDCODE ACADEMY",font=P700(38),fill=ORANGE,anchor="lm")
for i,l in enumerate(wrap(d,"Réservez votre démo\nou un coaching IA",P800(68),660)): d.text((110,400+i*80),l,font=P800(68),fill=BLUE,anchor="lm")
for i,l in enumerate(wrap(d,SLOGAN,P600(36),620)): d.text((110,610+i*50),l,font=P600(36),fill=INK,anchor="lm")
url="foodeatup.com"; f=P700(48); tw=d.textbbox((0,0),url,font=f)[2]; pw,ph=tw+80,100
d.rounded_rectangle([110,730,110+pw,830],50,fill=BLUE+(255,)); d.text((110+pw/2,780),url,font=f,fill=WHITE,anchor="mm")
ill=fit(load("assets-generes/cta.jpg"),620,780); im.alpha_composite(ill,(1200,150))
im.convert("RGB").save("frames/outro.png"); print("outro")
print("ALL 16:9 FRAMES DONE")
