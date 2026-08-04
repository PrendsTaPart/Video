#!/usr/bin/env python3
"""Deux schémas animés : A) orchestrateur (message->hub->6 branches), B) socle multi-tenant (5 blocs + clé -> une seule base)."""
import os, subprocess, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter
os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.makedirs("work/schA", exist_ok=True); os.makedirs("work/schB", exist_ok=True)
BASE="/home/user/Video"; FD=f"{BASE}/videos/rapidocms-presentation-4min/assets/fonts"
W,H=1920,1080; FPS=30
ANTH=(15,26,35); BLUE=(0,123,255); ORANGE=(255,165,0); SKY=(166,208,255); WHITE=(255,255,255); GREY=(120,140,160)
def F(n,s): return ImageFont.truetype(f"{FD}/{n}",s)
def bg():
    im=Image.new("RGBA",(W,H),ANTH+(255,))
    g=Image.new("RGBA",(W,H),(0,0,0,0)); ImageDraw.Draw(g).ellipse([W//2-520,H//2-360,W//2+520,H//2+360],fill=SKY+(20,))
    im.alpha_composite(g.filter(ImageFilter.GaussianBlur(170))); return im
def ease(x): return 0 if x<=0 else (1 if x>=1 else (1-math.cos(math.pi*x))/2)
def enc(folder,out,frames):
    r=subprocess.run(["ffmpeg","-y","-framerate",str(FPS),"-i",f"{folder}/f%04d.png","-c:v","libx264","-preset","medium","-crf","20","-pix_fmt","yuv420p","-r",str(FPS),out],stderr=subprocess.PIPE)
    if r.returncode: print(r.stderr.decode()[-700:]); raise SystemExit(1)
    print("ok",out,frames,"frames")

# ---------- SCHEMA A : ORCHESTRATEUR ----------
AG=[("Config",BLUE),("HACCP",BLUE),("Fourn.",BLUE),("RH",BLUE),("Stock",BLUE),("Prod.",BLUE)]
cx,cy=W//2,H//2+20; R=330
nodes=[]
for i in range(6):
    a=-math.pi/2 + i*(2*math.pi/6)
    nodes.append((cx+int(R*math.cos(a)*1.35), cy+int(R*math.sin(a))))
DUR_A=18.0; NA=int(DUR_A*FPS)
for fi in range(NA):
    t=fi/FPS; im=bg(); d=ImageDraw.Draw(im)
    d.text((W/2,80),"L'orchestrateur",font=F("Poppins-800.ttf",56),fill=WHITE,anchor="mm")
    # message bubble slides in 0-2.5s
    mp=ease(t/2.5); my=int(H-120-(H-120-(cy+150))*mp)
    if t<3.2:
        bw,bh=360,90; bx=cx-bw//2; d.rounded_rectangle([bx,my,bx+bw,my+bh],24,fill=(37,211,102,255))
        d.text((cx,my+bh//2),"« Prépare ma journée »",font=F("Poppins-600.ttf",30),fill=WHITE,anchor="mm")
    # hub appears 2.5s
    hp=ease((t-2.5)/1.0)
    if hp>0:
        hr=int(70*hp + 6*math.sin(t*3))
        d.ellipse([cx-hr,cy-hr,cx+hr,cy+hr],fill=BLUE+(255,),outline=WHITE+(255,),width=4)
        d.text((cx,cy),"PrediBot",font=F("Poppins-700.ttf",26),fill=WHITE,anchor="mm")
    # branches light one by one 4s..15s
    for i,(nx,ny) in enumerate(nodes):
        st=4.0+i*1.7; p=ease((t-st)/1.2); active=(st<=t<st+1.7)
        if p<=0: continue
        ex=cx+int((nx-cx)*p); ey=cy+int((ny-cy)*p)
        col=ORANGE if active else SKY
        d.line([cx,cy,ex,ey],fill=col+(220,),width=6)
        if p>=1:
            rr=54+(6 if active else 0)
            d.ellipse([nx-rr,ny-rr,nx+rr,ny+rr],fill=(20,32,44,255),outline=(ORANGE if active else BLUE)+(255,),width=5)
            d.text((nx,ny),AG[i][0],font=F("Poppins-700.ttf",26),fill=WHITE,anchor="mm")
    if t>15.2:
        d.text((W/2,H-70),"Un orchestrateur · six sous-agents spécialisés",font=F("Poppins-600.ttf",34),fill=SKY,anchor="mm")
    im.convert("RGB").save(f"work/schA/f{fi:04d}.png")
enc("work/schA","work/orch.mp4",NA)

# ---------- SCHEMA B : SOCLE MULTI-TENANT ----------
BLOCKS=["Déclencher","Analyser","Authentifier","Agir","Formater"]
DUR_B=19.0; NB=int(DUR_B*FPS)
bw,bh,gap=300,120,40; total=5*bw+4*gap; x0=(W-total)//2; by=250
dbs=[(cx-360,720),(cx,720),(cx+360,720)]  # 3 databases
for fi in range(NB):
    t=fi/FPS; im=bg(); d=ImageDraw.Draw(im)
    d.text((W/2,80),"Le socle : une clé par restaurant",font=F("Poppins-800.ttf",52),fill=WHITE,anchor="mm")
    # blocks chain in 0.5..5s
    for i,b in enumerate(BLOCKS):
        st=0.5+i*0.8; p=ease((t-st)/0.6)
        if p<=0: continue
        bx=x0+i*(bw+gap); auth=(i==2)
        pulse=(6*math.sin(t*3)) if (auth and t>4) else 0
        col=ORANGE if (auth and t>4) else BLUE
        a=int(255*p)
        d.rounded_rectangle([bx,by-pulse,bx+bw,by+bh+pulse],20,fill=(20,32,44,a),outline=col+(a,),width=5)
        d.text((bx+bw//2,by+bh//2),b,font=F("Poppins-700.ttf",34),fill=(WHITE if p>0.6 else GREY),anchor="mm")
        if i<4 and p>=1:
            ax=bx+bw; d.line([ax,by+bh//2,ax+gap,by+bh//2],fill=SKY+(200,),width=5)
    # key enters Authentifier 6..9s
    kp=ease((t-6)/2.0)
    authx=x0+2*(bw+gap)+bw//2
    if kp>0 and t<12:
        ky=int(by+bh+120-(140)*kp); ang=t*200
        # simple key glyph
        kr=26; d.ellipse([authx-kr,ky-kr,authx+kr,ky+kr],outline=ORANGE+(255,),width=8)
        d.line([authx,ky+kr,authx,ky+kr+40],fill=ORANGE+(255,),width=8)
        d.line([authx,ky+kr+40,authx+16,ky+kr+40],fill=ORANGE+(255,),width=8)
    # 3 databases; only middle lights 9..14s
    for j,(dx,dy) in enumerate(dbs):
        lit=(j==1 and t>9.2); col=ORANGE if lit else GREY
        a=int(255)
        # cylinder
        d.ellipse([dx-70,dy-90,dx+70,dy-50],outline=col+(a,),width=5)
        d.line([dx-70,dy-70,dx-70,dy+50],fill=col+(a,),width=5); d.line([dx+70,dy-70,dx+70,dy+50],fill=col+(a,),width=5)
        d.ellipse([dx-70,dy+30,dx+70,dy+70],outline=col+(a,),width=5)
        if lit:
            g=Image.new("RGBA",(W,H),(0,0,0,0)); ImageDraw.Draw(g).ellipse([dx-110,dy-120,dx+110,dy+100],fill=ORANGE+(60,))
            im.alpha_composite(g.filter(ImageFilter.GaussianBlur(40))); d=ImageDraw.Draw(im)
        d.text((dx,dy-10),f"Resto {j+1}",font=F("Poppins-600.ttf",24),fill=(WHITE if lit else GREY),anchor="mm")
        # link authentifier -> db
        if t>9.0:
            d.line([authx,by+bh, dx, dy-90],fill=((ORANGE if lit else (60,72,84))+(160,)),width=(5 if lit else 2))
    if t>13.5:
        d.text((W/2,H-60),"Aucune logique métier codée en dur · Vos données restent les vôtres",font=F("Poppins-600.ttf",32),fill=SKY,anchor="mm")
    im.convert("RGB").save(f"work/schB/f{fi:04d}.png")
enc("work/schB","work/socle.mp4",NB)
print("SCHEMAS DONE")
