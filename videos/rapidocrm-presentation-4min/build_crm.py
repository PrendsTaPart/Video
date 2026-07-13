#!/usr/bin/env python3
"""Compositeur RapidoCRM (16:9, 1920x1080). Charte #383838 / vert #4CAF50 / violet #7E57C2 (titres section).
Cadres d'écran bordés vert. Lower-thirds : titre vert (texte noir), sous-titre outils MCP violet. Arial→Liberation Sans."""
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
HERE=os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
BASE="/home/user/Video"; LIB="/usr/share/fonts/truetype/liberation"; SC="assets/screens/rapidocrm"; GEN="assets-generes"
AB=lambda s:ImageFont.truetype(f"{LIB}/LiberationSans-Bold.ttf",s); AR=lambda s:ImageFont.truetype(f"{LIB}/LiberationSans-Regular.ttf",s)
GREY=(56,56,56); GREEN=(76,175,80); VIOLET=(126,87,194); BLUE=(3,169,245); WHITE=(255,255,255); INK=(24,26,28); SKY=(166,208,255)
CLAUDE=Image.open(f"{GEN}/logo-claude.png").convert("RGBA")
MISTRAL=Image.open(f"{GEN}/logo-mistral.jpg").convert("RGBA")
BIRD=Image.open(f"{GEN}/rapidocrm-logo.png").convert("RGBA")
W,H=1920,1080
os.makedirs("frames",exist_ok=True); os.makedirs("frames/chat",exist_ok=True); os.makedirs("masks",exist_ok=True)
def cover(im,w=W,h=H):
    r=max(w/im.width,h/im.height); im=im.resize((int(im.width*r),int(im.height*r)),Image.LANCZOS)
    x=(im.width-w)//2; y=(im.height-h)//2; return im.crop((x,y,x+w,y+h))
def load(p): return Image.open(p).convert("RGBA")
def fit(img,bw,bh):
    r=min(bw/img.width,bh/img.height); return img.resize((max(1,int(img.width*r)),max(1,int(img.height*r))),Image.LANCZOS)
def wrap(dr,t,f,mw):
    out=[];cur=""
    for wd in t.split():
        s=(cur+" "+wd).strip()
        if dr.textbbox((0,0),s,font=f)[2]<=mw: cur=s
        else: out.append(cur); cur=wd
    out.append(cur); return out
def base(halo=True):
    im=Image.new("RGBA",(W,H),GREY+(255,))
    if halo:
        g=Image.new("RGBA",(W,H),(0,0,0,0)); ImageDraw.Draw(g).ellipse([W-720,-260,W+160,520],fill=GREEN+(28,)); im.alpha_composite(g.filter(ImageFilter.GaussianBlur(130)))
    return im
def browser(im,imgpath,box,frame=GREEN,rad=22):
    x,y,w,h=box; c=Image.new("RGBA",(w,h),(0,0,0,0)); ImageDraw.Draw(c).rounded_rectangle([0,0,w-1,h-1],rad,fill=WHITE+(255,),outline=frame+(255,),width=7)
    sh=Image.new("RGBA",(w+90,h+90),(0,0,0,0)); ImageDraw.Draw(sh).rounded_rectangle([45,58,45+w,58+h],rad,fill=(0,0,0,120)); im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(30)),(x-45,y-45))
    im.alpha_composite(c,(x,y)); d=ImageDraw.Draw(im)
    for i,cx in enumerate([x+30,x+64,x+98]): d.ellipse([cx-8,y+22,cx+8,y+38],fill=[(255,95,86),(255,189,46),(39,201,63)][i]+(255,))
    m=fit(load(imgpath),w-40,h-80); im.alpha_composite(m,(x+(w-m.width)//2,y+56+(h-80-m.height)//2))
def lower(im,title,sub,accent=GREEN):
    d=ImageDraw.Draw(im); f=AB(46); tw=d.textbbox((0,0),title,font=f)[2]
    d.rounded_rectangle([80,H-190,80+tw+80,H-110],18,fill=accent+(255,)); d.text((120,H-150),title,font=f,fill=INK,anchor="lm")
    if sub: d.text((84,H-90),sub,font=AR(30),fill=(190,170,230),anchor="lm")
def card(name,screen,title,sub,accent=GREEN):
    im=base(); browser(im,f"{SC}/{screen}",(360,150,1200,720),frame=accent); lower(im,title,sub,accent)
    im.convert("RGB").save(f"frames/{name}.png")
def stepbar(im,step,labels):  # tunnel SMS
    d=ImageDraw.Draw(im); n=len(labels); x0=560; gap=260
    for i,lab in enumerate(labels):
        x=x0+i*gap; on=(i<=step); col=GREEN if on else (90,94,98)
        d.ellipse([x-22,90,x+22,134],fill=col+(255,)); d.text((x,112),str(i+1),font=AB(26),fill=WHITE if on else (150,150,150),anchor="mm")
        d.text((x,160),lab,font=AR(24),fill=WHITE if on else (140,140,140),anchor="mm")
        if i<n-1: d.line([x+26,112,x+gap-26,112],fill=(120,124,128,255),width=4)

# ---- P1 hook (flow01 cover, no text)
cover(load(f"{GEN}/flow01-hook.jpg")).convert("RGB").save("frames/p1.png")
# ---- P3 mika bg
im=base(); d=ImageDraw.Draw(im)
d.text((760,470),"RapidoCRM",font=AB(90),fill=GREEN,anchor="lm"); d.text((762,560),"Votre force de vente, pilotée par l'IA",font=AR(40),fill=WHITE,anchor="lm")
im.convert("RGB").save("frames/p3.png")
mask=Image.new("L",(560,560),0); ImageDraw.Draw(mask).ellipse([0,0,559,559],fill=255); mask.save("masks/c560.png")
mask=Image.new("L",(360,360),0); ImageDraw.Draw(mask).ellipse([0,0,359,359],fill=255); mask.save("masks/c360.png")
# ---- P4 compte
card("p4a","crm-01.png","Compte & entreprise","Gérant : nom, email",GREEN)
card("p4b","crm-02.png","Compte & entreprise","Entreprise : nom, email, SIRET",GREEN)
card("p4c","crm-03.png","Profil","",GREEN)
# ---- P5 connexions (titres violets)
card("p5a","crm-04.png","Boîte mail","IMAP · mot de passe d'application Google",VIOLET)
card("p5b","crm-05.png","Paiement","Stripe · clé secrète",VIOLET)
card("p5c","crm-06.png","SMS","Twilio · clé d'envoi",VIOLET)
# ---- P6 MCP
im=base(); d=ImageDraw.Draw(im)
d.text((W/2,300),"Connectez votre IA",font=AB(64),fill=WHITE,anchor="mm")
url="https://crm.rapidosoftware.com/mcp"; f=AB(58); tw=d.textbbox((0,0),url,font=f)[2]
d.rounded_rectangle([(W-tw)//2-50,420,(W+tw)//2+50,520],20,fill=(30,32,34,255),outline=GREEN+(255,),width=5); d.text((W/2,470),url,font=f,fill=GREEN,anchor="mm")
cl=fit(CLAUDE,300,90); mi=fit(MISTRAL,300,90)
d.text((W/2,640),"Compatible avec",font=AR(34),fill=(180,184,188),anchor="mm")
im.alpha_composite(cl,(W//2-560,700)); im.alpha_composite(mi,(W//2-120,700))
d.text((W//2+430,745),"OpenAI",font=AB(52),fill=WHITE,anchor="mm")
lower(im,"Connecteur MCP","list_commerciaux · list_entreprises · list_templates",GREEN)
im.convert("RGB").save("frames/p6.png")
# ---- P7 équipe
card("p7a","crm-09.png","Votre équipe","Objectifs : SMS, appels, RDV, contrats",GREEN)
card("p7b","crm-08.png","Votre équipe","create_commercial · update_commercial_objectifs",GREEN)
# ---- P8 tunnel SMS (4 étapes, cadre vert, stepbar)
tun=[("p8a","crm-19.png",0,"Campagne SMS · Ciblage","10 personnes touchées"),
     ("p8b","crm-33.png",1,"Campagne SMS · Modèle","create_campagne"),
     ("p8c","crm-30.png",1,"Campagne SMS · Texte","schedule_sms"),
     ("p8d","crm-31.png",2,"Campagne SMS · Validation","aperçu sur téléphone")]
for name,scr,step,title,sub in tun:
    im=base(); stepbar(im,step,["Ciblage","Texte","Validation"]); browser(im,f"{SC}/{scr}",(360,210,1200,660),frame=GREEN); lower(im,title,sub,GREEN)
    im.convert("RGB").save(f"frames/{name}.png")
# ---- P9 docs
card("p9a","crm-28.png","Devis à vos couleurs","Choix de la charte graphique",GREEN)
card("p9b","crm-29.png","Contrat automatique","create_contrat · template mail",GREEN)
# ---- P10 quotidien
card("p10a","crm-21.png","Agenda","RDV colorés",GREEN)
card("p10b","crm-23.png","Prise de RDV","Visio / Physique / Tél · rappel auto",GREEN)
card("p10c","crm-20.png","Boîte mail","get_today_schedule · pipeline",GREEN)

# ---- Chat astuces (machine à écrire) + oiseau vert
def chatframe(prompt,nch,check=False):
    im=Image.new("RGBA",(W,H),(20,22,24,255)); g=Image.new("RGBA",(W,H),(0,0,0,0)); ImageDraw.Draw(g).ellipse([-200,-200,560,560],fill=GREEN+(30,)); im.alpha_composite(g.filter(ImageFilter.GaussianBlur(150)))
    d=ImageDraw.Draw(im); d.text((160,240),"ASTUCE DU CHEF",font=AB(40),fill=GREEN,anchor="lm")
    cl=fit(CLAUDE,300,84); d.rounded_rectangle([160,310,500,410],14,fill=(36,38,42,255)); im.alpha_composite(cl,(180,320))
    f=AB(46); shown=prompt[:nch]; lines=wrap(d,shown,f,1400) if shown else [""]; bh=len(lines)*62+50
    d.rounded_rectangle([160,450,1760,450+bh],22,fill=(40,44,50,255),outline=GREEN+(255,),width=3); yy=485
    for l in lines: d.text((190,yy),l,font=f,fill=(235,240,245),anchor="lm"); yy+=62
    cy=450+bh+50
    if check:
        d.ellipse([160,cy,222,cy+62],fill=GREEN+(255,)); d.line([176,cy+32,190,cy+46],fill=WHITE,width=8); d.line([190,cy+46,216,cy+16],fill=WHITE,width=8)
        d.text((250,cy+31),"Exécuté par votre IA",font=AB(44),fill=GREEN,anchor="lm")
        b=fit(BIRD,120,120); im.alpha_composite(b,(1560,cy-20))
    return im
ASTUCES={"a1":"Confirme l'accès : liste mes commerciaux, mes entreprises et mes templates.",
         "a2":"Crée ces commerciaux avec leurs objectifs mensuels : appels, RDV, contrats.",
         "a3":"Crée une facture de 1200 euros HT, TVA 20%, puis envoie le contrat au client."}
for k,pr in ASTUCES.items():
    seq=list(range(0,len(pr)+1,3))+[len(pr)]
    for i,n in enumerate(seq): chatframe(pr,n).convert("RGB").save(f"frames/chat/{k}_{i:03d}.png")
    chatframe(pr,len(pr),check=True).convert("RGB").save(f"frames/chat/{k}_check.png")
    with open(f"frames/chat/{k}_n.txt","w") as fh: fh.write(str(len(seq)))
print("RapidoCRM frames OK")
