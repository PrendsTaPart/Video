#!/usr/bin/env python3
"""Schémas v2 — thème WhatsApp (sable + vert), gros logo WhatsApp, texte agrandi, animation dynamique."""
import os, subprocess, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter
os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.makedirs("work/sA", exist_ok=True); os.makedirs("work/sB", exist_ok=True)
FD="/home/user/Video/videos/rapidocms-presentation-4min/assets/fonts"
W,H=1920,1080; FPS=30
SAND=(233,224,205); SANDHI=(245,239,227); BUBBLE=(220,248,198); GREEN=(37,211,102); DGREEN=(7,94,84); TEAL=(18,140,126); INK=(17,27,33); GREY=(150,150,140); WHITE=(255,255,255)
def F(n,s): return ImageFont.truetype(f"{FD}/{n}",s)
def ease(x): return 0 if x<=0 else (1 if x>=1 else (1-math.cos(math.pi*x))/2)
def bounce(x):
    if x<=0: return 0
    if x>=1: return 1
    return 1-(1-x)*(1-x)*math.cos(2.2*math.pi*x)*0.0 + (1-(1-x)*(1-x))  # ease-out-ish
def bg():
    im=Image.new("RGBA",(W,H),SAND+(255,))
    grad=Image.new("L",(1,H),0)
    for y in range(H): grad.putpixel((0,y),int(255*(y/H)))
    top=Image.new("RGBA",(W,H),SANDHI+(255,)); a=grad.resize((W,H)).point(lambda p:255-p); top.putalpha(a); im.alpha_composite(top)
    g=Image.new("RGBA",(W,H),(0,0,0,0)); ImageDraw.Draw(g).ellipse([W//2-560,H//2-380,W//2+560,H//2+380],fill=GREEN+(26,))
    im.alpha_composite(g.filter(ImageFilter.GaussianBlur(180))); return im
def wa_logo(im,cx,cy,r):
    """WhatsApp logo net : cercle vert + bulle + combiné blanc."""
    d=ImageDraw.Draw(im)
    d.ellipse([cx-r,cy-r,cx+r,cy+r],fill=GREEN+(255,))
    # tail
    d.polygon([(cx-r*0.55,cy+r*0.5),(cx-r*0.95,cy+r*0.95),(cx-r*0.2,cy+r*0.72)],fill=GREEN+(255,))
    # handset (white)
    hr=r*0.5
    d.arc([cx-hr,cy-hr,cx+hr,cy+hr],200,110,fill=WHITE,width=int(r*0.16))
    d.ellipse([cx-hr*0.9,cy-hr*0.9,cx-hr*0.2,cy-hr*0.2],fill=WHITE)  # earpiece
    d.ellipse([cx+hr*0.2,cy+hr*0.2,cx+hr*0.9,cy+hr*0.9],fill=WHITE)  # mouthpiece
def enc(folder,out,n):
    r=subprocess.run(["ffmpeg","-y","-framerate",str(FPS),"-i",f"{folder}/f%04d.png","-c:v","libx264","-preset","medium","-crf","20","-pix_fmt","yuv420p","-r",str(FPS),out],stderr=subprocess.PIPE)
    if r.returncode: print(r.stderr.decode()[-700:]); raise SystemExit(1)
    print("ok",out,n)

# ---------------- ORCHESTRATEUR ----------------
AG=["Config","HACCP","Fourn.","RH","Stock","Prod."]
cx,cy=W//2,H//2+30; R=350
nodes=[]
for i in range(6):
    a=-math.pi/2+i*(2*math.pi/6)
    nodes.append((int(cx+R*math.cos(a)*1.45),int(cy+R*math.sin(a))))
DA=20.0; NA=int(DA*FPS)
for fi in range(NA):
    t=fi/FPS; im=bg(); d=ImageDraw.Draw(im)
    d.text((W/2,72),"L'orchestrateur",font=F("Poppins-800.ttf",76),fill=INK,anchor="mm")
    # message bubble flies in
    mp=ease(t/2.2); my=int(H-140-(H-140-(cy+170))*mp)
    if t<3.0:
        bw,bh=460,104; d.rounded_rectangle([cx-bw//2,my,cx+bw//2,my+bh],26,fill=BUBBLE+(255,),outline=GREEN+(255,),width=4)
        d.text((cx,my+bh//2),"« Prépare ma journée »",font=F("Poppins-700.ttf",36),fill=DGREEN,anchor="mm")
    # branches + nodes bounce-in 3..9s
    for i,(nx,ny) in enumerate(nodes):
        st=3.0+i*0.6; p=ease((t-st)/0.7)
        if p<=0: continue
        d.line([cx,cy,nx,ny],fill=DGREEN+(150,),width=7)
    # hub = gros logo WhatsApp (breathing)
    hp=ease((t-2.2)/0.8)
    if hp>0:
        hr=int((118+7*math.sin(t*3))*hp); wa_logo(im,cx,cy,hr); d=ImageDraw.Draw(im)
    # nodes
    for i,(nx,ny) in enumerate(nodes):
        st=3.0+i*0.6; p=ease((t-st)/0.7)
        if p<1: continue
        rr=int(66*(1+0.06*math.sin(t*2+i)))
        d.ellipse([nx-rr,ny-rr,nx+rr,ny+rr],fill=GREEN+(255,),outline=WHITE+(255,),width=5)
        d.text((nx,ny),AG[i],font=F("Poppins-700.ttf",30),fill=WHITE,anchor="mm")
    # packets travel hub->node (loop) after 9s
    if t>9.0:
        for i,(nx,ny) in enumerate(nodes):
            ph=((t*0.6+i/6.0)%1.0)
            px=cx+(nx-cx)*ph; py=cy+(ny-cy)*ph
            d.ellipse([px-13,py-13,px+13,py+13],fill=DGREEN+(255,))
    if t>2.0:
        d.text((W/2,H-64),"Un orchestrateur, six spécialistes — comme une brigade.",font=F("Poppins-700.ttf",40),fill=DGREEN,anchor="mm")
    im.convert("RGB").save(f"work/sA/f{fi:04d}.png")
enc("work/sA","work/orch2.mp4",NA)

# ---------------- SOCLE ----------------
B=["Déclencher","Analyser","Authentifier","Agir","Formater"]
DB=20.0; NB=int(DB*FPS)
bw,bh,gap=310,130,34; total=5*bw+4*gap; x0=(W-total)//2; by=300
dbs=[(cx-380,760),(cx,760),(cx+380,760)]
for fi in range(NB):
    t=fi/FPS; im=bg(); d=ImageDraw.Draw(im)
    d.text((W/2,88),"Le socle : une clé par restaurant",font=F("Poppins-800.ttf",60),fill=INK,anchor="mm")
    for i,b in enumerate(B):
        st=0.5+i*0.7; p=ease((t-st)/0.55)
        if p<=0: continue
        bx=x0+i*(bw+gap); auth=(i==2 and t>4.2); pulse=int(7*math.sin(t*3)) if auth else 0
        fill=(DGREEN if auth else GREEN); yy=int(by-30*(1-p))
        d.rounded_rectangle([bx,yy-pulse,bx+bw,yy+bh+pulse],22,fill=fill+(int(255*p),),outline=WHITE+(int(255*p),),width=5)
        d.text((bx+bw//2,yy+bh//2),b,font=F("Poppins-700.ttf",38),fill=WHITE,anchor="mm")
        if i<4 and p>=1:
            ax=bx+bw; d.line([ax,yy+bh//2,ax+gap,yy+bh//2],fill=DGREEN+(220,),width=6)
    authx=x0+2*(bw+gap)+bw//2
    kp=ease((t-6)/2.0)
    if kp>0 and t<12.5:
        ky=int(by+bh+150-170*kp)
        kr=30; d.ellipse([authx-kr,ky-kr,authx+kr,ky+kr],outline=DGREEN+(255,),width=10)
        d.line([authx,ky+kr,authx,ky+kr+46],fill=DGREEN+(255,),width=10); d.line([authx,ky+kr+46,authx+20,ky+kr+46],fill=DGREEN+(255,),width=10)
    for j,(dx,dy) in enumerate(dbs):
        lit=(j==1 and t>9.2); col=GREEN if lit else GREY
        if lit:
            g=Image.new("RGBA",(W,H),(0,0,0,0)); ImageDraw.Draw(g).ellipse([dx-120,dy-130,dx+120,dy+110],fill=GREEN+(70,))
            im.alpha_composite(g.filter(ImageFilter.GaussianBlur(45))); d=ImageDraw.Draw(im)
        d.ellipse([dx-76,dy-96,dx+76,dy-54],outline=col+(255,),width=6,fill=(BUBBLE+(255,) if lit else None))
        d.line([dx-76,dy-75,dx-76,dy+55],fill=col+(255,),width=6); d.line([dx+76,dy-75,dx+76,dy+55],fill=col+(255,),width=6)
        d.ellipse([dx-76,dy+34,dx+76,dy+76],outline=col+(255,),width=6)
        d.text((dx,dy-8),f"Resto {j+1}",font=F("Poppins-700.ttf",30),fill=(DGREEN if lit else GREY),anchor="mm")
        if t>9.0: d.line([authx,by+bh,dx,dy-96],fill=((GREEN if lit else GREY)+(160,)),width=(6 if lit else 2))
    if t>3.0:
        d.text((W/2,H-56),"Vos données restent les vôtres.",font=F("Poppins-800.ttf",44),fill=DGREEN,anchor="mm")
    im.convert("RGB").save(f"work/sB/f{fi:04d}.png")
enc("work/sB","work/socle2.mp4",NB)
print("SCHEMAS2 DONE")
