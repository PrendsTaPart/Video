#!/usr/bin/env python3
"""Studio de vente — 3 templates paramétrables (previews).
T1 Problème→Solution · T2 Démo 1 phrase (chat Claude) · T3 Fondateur/LinkedIn.
Chaque template = fonction(cfg) -> frame PNG. Paramètres : accent, hook, capture, prompt, cta, produit."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os
BASE="/home/user/Video"
os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.makedirs("preview",exist_ok=True)
FD=f"{BASE}/videos/rapidocms-presentation-4min/assets/fonts"
def F(n,s): return ImageFont.truetype(os.path.join(FD,n),s)
P800=lambda s:F("Poppins-800.ttf",s); P700=lambda s:F("Poppins-700.ttf",s); P600=lambda s:F("Poppins-600.ttf",s)
WHITE=(255,255,255); NAVY=(28,30,52); INK=(70,72,92); DARK=(16,16,30)
MIKA=Image.open(f"{BASE}/videos/stories-foodeatup-30j/assets/avatar/mika-still.png").convert("RGBA")
CLAUDE=Image.open(f"{BASE}/videos/rapidocms-presentation-4min/assets/rapidocms/logo-claude.png").convert("RGBA")
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
def load(p): return Image.open(p if p.startswith("/") else BASE+"/"+p).convert("RGBA")
def circle(img,d):
    img=img.resize((d,d),Image.LANCZOS); m=Image.new("L",(d,d),0); ImageDraw.Draw(m).ellipse([0,0,d-1,d-1],fill=255)
    o=Image.new("RGBA",(d,d),(0,0,0,0)); o.paste(img,(0,0),m); return o
def med(im,x,y,d,accent):
    c=circle(MIKA.crop((120,80,600,560)),d); ring=Image.new("RGBA",(d+20,d+20),(0,0,0,0))
    ImageDraw.Draw(ring).ellipse([0,0,d+19,d+19],outline=accent+(255,),width=8); im.alpha_composite(ring,(x-10,y-10)); im.alpha_composite(c,(x,y))
def card(im,imgs,box,rad=28):
    x,y,w,h=box; c=Image.new("RGBA",(w,h),(0,0,0,0)); ImageDraw.Draw(c).rounded_rectangle([0,0,w-1,h-1],rad,fill=WHITE+(255,))
    sh=Image.new("RGBA",(w+80,h+80),(0,0,0,0)); ImageDraw.Draw(sh).rounded_rectangle([40,52,40+w,52+h],rad,fill=(20,20,40,60))
    im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(24)),(x-40,y-40)); im.alpha_composite(c,(x,y))
    d=ImageDraw.Draw(im)
    for i,cx in enumerate([x+30,x+64,x+98]): d.ellipse([cx-8,y+24,cx+8,y+40],fill=[(255,95,86),(255,189,46),(39,201,63)][i]+(255,))
    m=fit(load(imgs[0]),w-40,h-80); im.alpha_composite(m,(x+(w-m.width)//2,y+56+(h-80-m.height)//2))
def pill(im,txt,y,accent,W,fs=44):
    d=ImageDraw.Draw(im); f=P700(fs); lines=wrap(d,txt,f,W-160); lh=fs+14; th=lh*len(lines); pad=34
    tw=max(d.textbbox((0,0),l,font=f)[2] for l in lines); pw=min(tw+pad*2,W-70); ph=th+pad*2-8; px=(W-pw)//2
    d.rounded_rectangle([px,y,px+pw,y+ph],36,fill=accent+(240,)); yy=y+pad-4
    for l in lines: d.text((W/2,yy+lh/2),l,font=f,fill=WHITE,anchor="mm"); yy+=lh

def bg(W,H,accent):
    im=Image.new("RGBA",(W,H),(248,249,252,255)); g=Image.new("RGBA",(W,H),(0,0,0,0)); gd=ImageDraw.Draw(g)
    gd.ellipse([W-360,-160,W+160,340],fill=accent+(26,)); im.alpha_composite(g.filter(ImageFilter.GaussianBlur(80))); return im

# ---------- T1 : Problème → Solution (9:16) ----------
def T1(cfg):
    W,H=1080,1920; a=cfg["accent"]; im=bg(W,H,a); d=ImageDraw.Draw(im)
    med(im,80,300,230,a)
    f=P800(52)
    for i,l in enumerate(wrap(d,cfg["hook"],f,600)): d.text((340,330+i*62),l,font=f,fill=NAVY,anchor="lm")
    card(im,[cfg["capture"]],(90,620,900,720))
    d.text((W/2,1400),cfg["produit"].upper()+" · "+cfg.get("feature",""),font=P700(30),fill=a,anchor="mm")
    pill(im,cfg["cta"],1470,a,W)
    im.convert("RGB").save(cfg.get("out","preview/T1-probleme-solution.png")); print("T1")

# ---------- T2 : Démo 1 phrase (chat Claude, 9:16) ----------
def T2(cfg):
    W,H=1080,1920; a=cfg["accent"]; im=Image.new("RGBA",(W,H),DARK+(255,)); d=ImageDraw.Draw(im)
    g=Image.new("RGBA",(W,H),(0,0,0,0)); ImageDraw.Draw(g).ellipse([-200,-200,420,420],fill=a+(55,)); im.alpha_composite(g.filter(ImageFilter.GaussianBlur(120)))
    d.text((70,150),"DÉMO · UNE PHRASE",font=P700(34),fill=(230,150,60),anchor="lm")
    d.text((70,214),cfg["title"],font=P800(54),fill=WHITE,anchor="lm")
    cl=fit(CLAUDE,200,56); d.rounded_rectangle([70,320,310,392],16,fill=(40,40,64,255)); im.alpha_composite(cl,(88,328))
    f=P600(38); lines=wrap(d,cfg["prompt"],f,880); bh=len(lines)*50+50
    d.rounded_rectangle([70,430,1010,430+bh],24,fill=(48,48,80,255)); yy=460
    for l in lines: d.text((100,yy),l,font=f,fill=(226,226,244),anchor="lm"); yy+=50
    cy=430+bh+40; d.ellipse([70,cy,126,cy+56],fill=(72,168,80,255)); d.line([86,cy+28,98,cy+42],fill=WHITE,width=7); d.line([98,cy+42,124,cy+14],fill=WHITE,width=7)
    d.text((150,cy+28),"Exécuté par votre IA",font=P700(40),fill=(120,220,140),anchor="lm")
    card(im,[cfg["result"]],(90,cy+110,900,610))
    pill(im,cfg["cta"],1740,a,W,fs=38)
    im.convert("RGB").save(cfg.get("out","preview/T2-demo-1phrase.png")); print("T2")

# ---------- T3 : Fondateur / LinkedIn (1:1) ----------
def T3(cfg):
    W,H=1080,1080; a=cfg["accent"]; im=bg(W,H,a); d=ImageDraw.Draw(im)
    m=fit(MIKA.crop((120,40,600,700)),470,700); mk=Image.new("RGBA",(m.width,m.height),(0,0,0,0)); mk.paste(m,(0,0))
    msk=Image.new("L",m.size,0); ImageDraw.Draw(msk).rounded_rectangle([0,0,m.width-1,m.height-1],40,fill=255)
    im.paste(m,(70,190),msk)
    d.text((610,210),cfg["produit"].upper(),font=P700(32),fill=a,anchor="lm")
    f=P800(56)
    for i,l in enumerate(wrap(d,cfg["punchline"],f,420)): d.text((610,270+i*68),l,font=f,fill=NAVY,anchor="lm")
    fs=P600(34)
    for i,l in enumerate(wrap(d,cfg.get("sub",""),fs,430)): d.text((610,560+i*46),l,font=fs,fill=INK,anchor="lm")
    d.rounded_rectangle([610,760,610+d.textbbox((0,0),cfg['cta'],font=P700(38))[2]+72,840],40,fill=a+(255,))
    d.text((646,800),cfg["cta"],font=P700(38),fill=WHITE,anchor="lm")
    d.text((70,960),"— Mo, fondateur",font=P600(30),fill=INK,anchor="lm")
    im.convert("RGB").save(cfg.get("out","preview/T3-fondateur.png")); print("T3")

if __name__=="__main__":
    BLUE=(11,110,253); SKY=(41,171,226); VIOLET=(123,97,196)
    T1({"accent":BLUE,"produit":"FoodEatUp","feature":"Importer la carte","hook":"Vous saisissez vos plats un par un ?!","capture":"assets/screens/foodeatup/ajout-produit.png","cta":"Réservez votre démo · lien en bio"})
    T2({"accent":SKY,"produit":"RapidoCMS","title":"Un mois de posts","prompt":"10 posts, 3 réseaux, un par jour à 10h.","result":"videos/rapidocms-presentation-4min/assets/rapidocms/calendrier-planification.png","cta":"Réservez votre démo · lien en bio"})
    T3({"accent":VIOLET,"produit":"Écosystème Rapido","punchline":"L'IA ne gère pas seule.\nVous pilotez, elle exécute.","sub":"4 MCP, un back-office piloté en parlant. Prix PME.","cta":"Réservez une démo"})
