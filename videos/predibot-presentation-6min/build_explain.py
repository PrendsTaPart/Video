#!/usr/bin/env python3
"""Séquence 'C'est quoi PrediBot ?' — agent connecté à votre WhatsApp qui gère FoodEatUp. Thème sable+vert."""
import os, subprocess, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter
os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.makedirs("work/ex", exist_ok=True)
FD="/home/user/Video/videos/rapidocms-presentation-4min/assets/fonts"
W,H=1920,1080; FPS=30
SAND=(233,224,205); SANDHI=(245,239,227); GREEN=(37,211,102); DGREEN=(7,94,84); TEAL=(18,140,126); INK=(17,27,33); BUBBLE=(220,248,198); WHITE=(255,255,255); GREY=(150,150,140)
def F(n,s): return ImageFont.truetype(f"{FD}/{n}",s)
def ease(x): return 0 if x<=0 else (1 if x>=1 else (1-math.cos(math.pi*x))/2)
FE=Image.open("assets-icons/fe-logo-c.png").convert("RGBA")
def sandbg():
    im=Image.new("RGBA",(W,H),SAND+(255,)); g=Image.new("L",(1,H),0)
    for y in range(H): g.putpixel((0,y),int(255*(y/H)))
    top=Image.new("RGBA",(W,H),SANDHI+(255,)); top.putalpha(g.resize((W,H)).point(lambda p:255-p)); im.alpha_composite(top)
    gl=Image.new("RGBA",(W,H),(0,0,0,0)); ImageDraw.Draw(gl).ellipse([W//2-560,H//2-360,W//2+560,H//2+360],fill=GREEN+(26,))
    im.alpha_composite(gl.filter(ImageFilter.GaussianBlur(180))); return im
def wa(d,cx,cy,r):
    d.ellipse([cx-r,cy-r,cx+r,cy+r],fill=GREEN+(255,))
    d.polygon([(cx-r*0.55,cy+r*0.5),(cx-r*0.96,cy+r*0.98),(cx-r*0.18,cy+r*0.74)],fill=GREEN+(255,))
    hr=r*0.5; d.arc([cx-hr,cy-hr,cx+hr,cy+hr],200,110,fill=WHITE,width=int(r*0.16))
    d.ellipse([cx-hr*0.92,cy-hr*0.92,cx-hr*0.2,cy-hr*0.2],fill=WHITE); d.ellipse([cx+hr*0.2,cy+hr*0.2,cx+hr*0.92,cy+hr*0.92],fill=WHITE)

# phone geometry
PX,PY,PW,PH=250,230,470,720
# foodeatup card geometry
CX,CY,CW,CH=1120,300,660,520

D=dur=float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0","audio/vo_explain.mp3"]).strip())+1.2
N=int(D*FPS)
for fi in range(N):
    t=fi/FPS; im=sandbg(); d=ImageDraw.Draw(im)
    d.text((W/2,90),"C'est quoi PrediBot ?",font=F("Poppins-800.ttf",76),fill=INK,anchor="mm")
    # phone slide-in 0-1.4
    pp=ease(t/1.4); px=int(PX-500*(1-pp))
    # phone body
    d.rounded_rectangle([px,PY,px+PW,PY+PH],46,fill=WHITE+(255,),outline=DGREEN+(255,),width=6)
    # whatsapp header
    d.rounded_rectangle([px,PY,px+PW,PY+96],46,fill=DGREEN+(255,)); d.rectangle([px,PY+50,px+PW,PY+96],fill=DGREEN+(255,))
    wa(d,px+50,PY+48,26); d.text((px+92,PY+26),"PrediBot",font=F("Poppins-700.ttf",30),fill=WHITE); d.text((px+92,PY+62),"en ligne",font=F("Poppins-600.ttf",20),fill=(200,240,225))
    # chat area (cream)
    d.rectangle([px+8,PY+100,px+PW-8,PY+PH-70],fill=(236,229,221,255))
    # incoming bubble
    if t>0.8:
        d.rounded_rectangle([px+30,PY+140,px+330,PY+250],18,fill=WHITE+(255,))
        d.text((px+48,PY+160),"Bonjour ! Je gère",font=F("Poppins-600.ttf",24),fill=INK)
        d.text((px+48,PY+196),"votre restaurant.",font=F("Poppins-600.ttf",24),fill=INK)
    # outgoing bubble (green)
    if t>1.8:
        d.rounded_rectangle([px+140,PY+300,px+PW-30,PY+400],18,fill=BUBBLE+(255,))
        d.text((px+164,PY+322),"Ajoute un",font=F("Poppins-700.ttf",26),fill=DGREEN)
        d.text((px+164,PY+356),"employé",font=F("Poppins-700.ttf",26),fill=DGREEN)
    # connection phone -> foodeatup
    ax,ay=PX+PW+10,PY+PH//2; bx,by=CX-10,CY+CH//2
    cp=ease((t-1.6)/1.2)
    if cp>0:
        ex=int(ax+(bx-ax)*cp); ey=int(ay+(by-ay)*cp)
        d.line([ax,ay,ex,ey],fill=DGREEN+(180,),width=6)
        # moving dots
        if t>2.6:
            for k in range(3):
                ph=((t*0.5+k/3.0)%1.0); dx=ax+(bx-ax)*ph; dy=ay+(by-ay)*ph
                d.ellipse([dx-12,dy-12,dx+12,dy+12],fill=GREEN+(255,))
    # foodeatup card appears 2.2+
    fp=ease((t-2.2)/1.0)
    if fp>0:
        d.rounded_rectangle([CX,CY,CX+CW,CY+CH],32,fill=WHITE+(int(255*fp),),outline=GREEN+(int(255*fp),),width=6)
        fe=FE.resize((360,int(FE.height*360/FE.width)),Image.LANCZOS)
        im.alpha_composite(fe,(CX+CW//2-180,CY+40))
        # mini dashboard bars
        if t>2.8:
            bx0=CX+90; by0=CY+300
            vals=[0.5,0.8,0.35,0.65,0.9]
            for i,v in enumerate(vals):
                bh=int(150*v); d.rounded_rectangle([bx0+i*95,by0+ (150-bh),bx0+i*95+60,by0+150],8,fill=(GREEN if i%2 else TEAL)+(255,))
            d.text((CX+CW//2,CY+CH-40),"Stocks · Équipe · Fournisseurs",font=F("Poppins-700.ttf",30),fill=DGREEN,anchor="mm")
    # subtitle
    if t>0.5:
        d.text((W/2,H-120),"Un agent connecté à votre numéro WhatsApp.",font=F("Poppins-800.ttf",46),fill=INK,anchor="mm")
        d.text((W/2,H-64),"Il gère FoodEatUp — juste en lui envoyant un message.",font=F("Poppins-700.ttf",38),fill=DGREEN,anchor="mm")
    im.convert("RGB").save(f"work/ex/f{fi:04d}.png")
r=subprocess.run(["ffmpeg","-y","-framerate",str(FPS),"-i","work/ex/f%04d.png","-c:v","libx264","-preset","medium","-crf","20","-pix_fmt","yuv420p","-r",str(FPS),"-an","work/explain.mp4"],stderr=subprocess.PIPE)
if r.returncode: print(r.stderr.decode()[-600:]); raise SystemExit(1)
print("explain OK", round(D,1),"s")
