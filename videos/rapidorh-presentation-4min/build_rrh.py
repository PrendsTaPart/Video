#!/usr/bin/env python3
"""RapidoRH vertical (1080x1920) frames. Violet theme. Mika medallion + card + caption;
dark 'Astuce chat Claude' frames; logo intro."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
W,H=1080,1920
BG=(248,246,252); PURPLE=(123,97,196); GREEN=(72,168,80); BLUE=(0,168,240)
NAVY=(34,28,60); INK=(70,66,92); MUTED=(140,135,160); WHITE=(255,255,255); DARK=(18,16,32)
FD="assets/fonts"
def F(n,s): return ImageFont.truetype(os.path.join(FD,n),s)
P800=lambda s:F("Poppins-800.ttf",s); P700=lambda s:F("Poppins-700.ttf",s); P600=lambda s:F("Poppins-600.ttf",s)
os.makedirs("frames",exist_ok=True)
os.makedirs("assets/fonts",exist_ok=True)
import glob
if not glob.glob("assets/fonts/*.ttf"):
    for f in glob.glob("../rapidocms-presentation-4min/assets/fonts/*.ttf"): __import__("shutil").copy(f,"assets/fonts/")
logo=Image.open("assets/rapidorh/logo-rapidorh.png").convert("RGBA")
logosoft=Image.open("assets/rapidorh/logo-rapidosoftware.png").convert("RGBA")
mika=Image.open("assets/avatar/mika-still.png").convert("RGBA")
DOTS=None
def circle(img,d):
    img=img.resize((d,d),Image.LANCZOS); m=Image.new("L",(d,d),0); ImageDraw.Draw(m).ellipse([0,0,d-1,d-1],fill=255)
    o=Image.new("RGBA",(d,d),(0,0,0,0)); o.paste(img,(0,0),m); return o
def wrap(dr,t,f,mw):
    out=[]
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
def load(p):
    if not p.startswith("assets") and not p.startswith(".."): p="assets/rapidorh/"+p
    return Image.open(p).convert("RGBA")
def bg_base():
    im=Image.new("RGBA",(W,H),BG+(255,)); g=Image.new("RGBA",(W,H),(0,0,0,0)); gd=ImageDraw.Draw(g)
    gd.ellipse([W-360,-160,W+160,360],fill=PURPLE+(26,)); gd.ellipse([-160,H-360,360,H+160],fill=GREEN+(18,))
    im.alpha_composite(g.filter(ImageFilter.GaussianBlur(80))); return im
def head(im,label):
    lw=210; lh=int(logo.height*lw/logo.width); im.alpha_composite(fit(logo,lw,80),(70,96))
    d=ImageDraw.Draw(im); f=P700(34); tw=d.textbbox((0,0),label,font=f)[2]; pw,ph=tw+52,62; px,py=W-70-pw,100
    d.rounded_rectangle([px,py,px+pw,py+ph],31,fill=PURPLE+(255,)); d.text((px+pw/2,py+ph/2),label,font=f,fill=WHITE,anchor="mm")
def medallion(im):
    med=circle(mika.crop((120,80,600,560)),230); ring=Image.new("RGBA",(250,250),(0,0,0,0))
    ImageDraw.Draw(ring).ellipse([0,0,249,249],outline=PURPLE+(255,),width=8); im.alpha_composite(ring,(70,300)); im.alpha_composite(med,(80,310))
def hooktext(im,txt,x=330,y0=330):
    d=ImageDraw.Draw(im); f=P800(50)
    for i,l in enumerate(wrap(d,txt,f,600)): d.text((x,y0+i*60),l,font=f,fill=NAVY,anchor="lm")
def card(im,imgs,box=(90,600,900,720)):
    x,y,w,h=box
    c=Image.new("RGBA",(w,h),(0,0,0,0)); ImageDraw.Draw(c).rounded_rectangle([0,0,w-1,h-1],30,fill=WHITE+(255,))
    sh=Image.new("RGBA",(w+80,h+80),(0,0,0,0)); ImageDraw.Draw(sh).rounded_rectangle([40,54,40+w,54+h],30,fill=(34,28,60,55))
    im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(24)),(x-40,y-40)); im.alpha_composite(c,(x,y))
    d=ImageDraw.Draw(im)
    for i,cx in enumerate([x+34,x+70,x+106]): d.ellipse([cx-9,y+27,cx+9,y+45],fill=[(255,95,86),(255,189,46),(39,201,63)][i]+(255,))
    ax,ay,aw,ah=x+22,y+72,w-44,h-96
    if len(imgs)==1:
        m=fit(load(imgs[0]),aw,ah); im.alpha_composite(m,(ax+(aw-m.width)//2,ay+(ah-m.height)//2))
    else:
        gap=18; cw=(aw-gap)//2
        for i,g in enumerate(imgs[:2]):
            m=fit(load(g),cw,ah); im.alpha_composite(m,(ax+i*(cw+gap)+(cw-m.width)//2,ay+(ah-m.height)//2))
def caption(im,text,col=PURPLE,y=1470):
    d=ImageDraw.Draw(im); f=P700(44); lines=wrap(d,text,f,900); lh=58; th=lh*len(lines); pad=36
    tw=max(d.textbbox((0,0),l,font=f)[2] for l in lines); pw=min(tw+pad*2,W-80); ph=th+pad*2-6; px=(W-pw)//2
    d.rounded_rectangle([px,y,px+pw,y+ph],36,fill=col+(240,)); yy=y+pad-3
    for l in lines: d.text((W/2,yy+lh/2),l,font=f,fill=WHITE,anchor="mm"); yy+=lh
def label_pill(im,txt,y=1360):
    d=ImageDraw.Draw(im); f=P700(36); tw=d.textbbox((0,0),txt,font=f)[2]; pw=tw+52; x=(W-pw)//2
    d.rounded_rectangle([x,y,x+pw,y+64],32,fill=GREEN+(255,)); d.text((W/2,y+32),txt,font=f,fill=WHITE,anchor="mm")

def chapter(sid,label,hook,cap,imgs):
    im=bg_base(); head(im,label); medallion(im); hooktext(im,hook);
    if imgs: card(im,imgs)
    caption(im,cap); im.convert("RGB").save(f"frames/{sid}.png"); print(sid)

def intro():
    im=bg_base(); head(im,"RapidoRH"); d=ImageDraw.Draw(im)
    lg=fit(logo,720,520); im.alpha_composite(lg,((W-lg.width)//2,360))
    for i,l in enumerate(wrap(d,"Gestion & planification de vos projets",P700(46),900)):
        d.text((W/2,940+i*58),l,font=P700(46),fill=NAVY,anchor="mm")
    for i,l in enumerate(wrap(d,"pour votre équipe et vos agents IA",P600(42),900)):
        d.text((W/2,1050+i*54),l,font=P600(42),fill=INK,anchor="mm")
    caption(im,"Bienvenue sur RapidoSoftware",col=PURPLE,y=1560)
    im.convert("RGB").save("frames/intro.png"); print("intro")

def mcp():
    im=bg_base(); head(im,"MCP"); medallion(im); hooktext(im,"Connectez\nvotre IA.")
    d=ImageDraw.Draw(im)
    url="rh.rapidosoftware.com/mcp/rapidorh"; f=P800(40); tw=d.textbbox((0,0),url,font=f)[2]; pw,ph=tw+56,88
    d.rounded_rectangle([(W-pw)//2,640,(W+pw)//2,640+ph],18,fill=PURPLE+(255,)); d.text((W/2,640+ph/2),url,font=f,fill=WHITE,anchor="mm")
    d.text((W/2,790),"Compatible : Claude · Mistral · OpenAI",font=P600(36),fill=INK,anchor="mm")
    x=180; y=850
    for lg,bw in [("logo-claude.png",240),("logo-mistral.jpg",150),("logo-openai.png",210)]:
        m=fit(load(lg),bw,74); im.alpha_composite(m,(x,y)); x+=m.width+40
    caption(im,"L'IA agit avec vos droits admin — accès réservé.",col=(200,90,70),y=1470)
    im.convert("RGB").save("frames/mcp.png"); print("mcp")

def astuce(sid,n,title,prompt,result):
    im=Image.new("RGBA",(W,H),DARK+(255,)); d=ImageDraw.Draw(im)
    g=Image.new("RGBA",(W,H),(0,0,0,0)); ImageDraw.Draw(g).ellipse([-200,-200,400,400],fill=PURPLE+(50,)); im.alpha_composite(g.filter(ImageFilter.GaussianBlur(120)))
    d.text((70,150),f"ASTUCE DU CHEF #{n}",font=P700(36),fill=(230,150,60),anchor="lm")
    d.text((70,215),title,font=P800(56),fill=WHITE,anchor="lm")
    cl=fit(load("logo-claude.png"),200,56); d.rounded_rectangle([70,320,70+240,320+72],16,fill=(36,32,58,255)); im.alpha_composite(cl,(88,328))
    bx,by,bw=70,430,940; f=P600(38); lines=wrap(d,prompt,f,bw-60); bh=len(lines)*50+50
    d.rounded_rectangle([bx,by,bx+bw,by+bh],24,fill=(48,42,78,255)); yy=by+30
    for l in lines: d.text((bx+30,yy),l,font=f,fill=(225,220,240),anchor="lm"); yy+=50
    cy=by+bh+40; d.ellipse([70,cy,70+56,cy+56],fill=GREEN+(255,)); d.line([86,cy+28,98,cy+42],fill=WHITE,width=7); d.line([98,cy+42,124,cy+14],fill=WHITE,width=7)
    d.text((150,cy+28),"Exécuté par votre IA",font=P700(40),fill=GREEN,anchor="lm")
    x,y,w,h=90,cy+110,900,640
    c=Image.new("RGBA",(w,h),(0,0,0,0)); ImageDraw.Draw(c).rounded_rectangle([0,0,w-1,h-1],24,fill=WHITE+(255,)); im.alpha_composite(c,(x,y))
    r=fit(load(result),w-40,h-40); im.alpha_composite(r,(x+(w-r.width)//2,y+(h-r.height)//2))
    im.convert("RGB").save(f"frames/{sid}.png"); print(sid)

def outro():
    im=bg_base(); head(im,"Academy"); medallion(im); d=ImageDraw.Draw(im)
    lg=fit(logosoft,720,300); im.alpha_composite(lg,((W-lg.width)//2,640))
    for i,l in enumerate(wrap(d,"L'écosystème Rapido,\npiloté par votre IA.",P800(56),900)): d.text((W/2,1000+i*66),l,font=P800(56),fill=NAVY,anchor="mm")
    caption(im,"Réservez votre démo — rapidosoftware.com",col=PURPLE,y=1470)
    im.convert("RGB").save("frames/outro.png"); print("outro")

intro()
chapter("compte","Compte","Créez votre\ncompte gérant.","Mot de passe : 8 caractères, 1 majuscule, 1 chiffre.",["connexion.png","creer-compte.png"])
chapter("organisation","Organisation","Structurez\nvotre équipe.","4 profils de base + rôles sur-mesure. Départements : web.",["ajouter-role-permissions.png","liste-departements.png"])
mcp()
astuce("astuce1",1,"Vérifiez la structure","Liste mes départements, mes rôles et mes employés actifs.","liste-utilisateurs.png")
chapter("equipe","Équipe","Ajoutez\nvos collaborateurs.","Chacun reçoit son invitation email, automatiquement.",["ajouter-utilisateur.png","liste-utilisateurs-2.png"])
astuce("astuce2",2,"L'équipe en 1 fois","Crée ces cinq employés d'un coup, avec leurs rôles.","liste-utilisateurs.png")
chapter("projets","Projets & Kanban","Projets, tâches\n& Kanban.","À faire · En cours · Terminé, générés automatiquement.",["creer-projet.png","kanban-taches.png"])
astuce("astuce3",3,"Un projet en 1 prompt","Crée le projet Ouverture avec son équipe et ses tâches.","kanban-taches.png")
chapter("quotidien","Quotidien","Le pilotage\nau quotidien.","Dailies, congés, pointages côté équipe. L'admin supervise.",["agenda.png","conges.png"])
astuce("astuce4",4,"L'état des lieux","Congés en attente, dailies manquants, anomalies de pointage ?","conges.png")
outro()
print("ALL RRH FRAMES DONE")
