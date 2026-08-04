#!/usr/bin/env python3
"""Logo FoodEatUp à la fin — thème WhatsApp sable + vert, gros logo WhatsApp."""
import os, subprocess
from PIL import Image, ImageDraw, ImageFont, ImageFilter
os.chdir(os.path.dirname(os.path.abspath(__file__)))
BASE="/home/user/Video"; FD=f"{BASE}/videos/rapidocms-presentation-4min/assets/fonts"
LOGO=f"{BASE}/studio-video/assets/brand/logo"
W,H=1920,1080; FPS=30
SAND=(233,224,205); SANDHI=(245,239,227); GREEN=(37,211,102); DGREEN=(7,94,84); INK=(17,27,33); WHITE=(255,255,255)
def F(n,s): return ImageFont.truetype(f"{FD}/{n}",s)
def sandbg():
    im=Image.new("RGBA",(W,H),SAND+(255,)); g=Image.new("L",(1,H),0)
    for y in range(H): g.putpixel((0,y),int(255*(y/H)))
    top=Image.new("RGBA",(W,H),SANDHI+(255,)); top.putalpha(g.resize((W,H)).point(lambda p:255-p)); im.alpha_composite(top)
    gl=Image.new("RGBA",(W,H),(0,0,0,0)); ImageDraw.Draw(gl).ellipse([W//2-560,H//2-380,W//2+560,H//2+320],fill=GREEN+(30,))
    im.alpha_composite(gl.filter(ImageFilter.GaussianBlur(180))); return im
def wa(im,cx,cy,r):
    d=ImageDraw.Draw(im); d.ellipse([cx-r,cy-r,cx+r,cy+r],fill=GREEN+(255,))
    d.polygon([(cx-r*0.55,cy+r*0.5),(cx-r*0.96,cy+r*0.98),(cx-r*0.18,cy+r*0.74)],fill=GREEN+(255,))
    hr=r*0.5; d.arc([cx-hr,cy-hr,cx+hr,cy+hr],200,110,fill=WHITE,width=int(r*0.16))
    d.ellipse([cx-hr*0.92,cy-hr*0.92,cx-hr*0.2,cy-hr*0.2],fill=WHITE); d.ellipse([cx+hr*0.2,cy+hr*0.2,cx+hr*0.92,cy+hr*0.92],fill=WHITE)
im=sandbg()
m=Image.open(f"{LOGO}/foodeatup-logo-horizontal.png").convert("RGBA")
mw=620; m=m.resize((mw,int(m.height*mw/m.width)),Image.LANCZOS)
im.alpha_composite(m,((W-m.width)//2,150))
wa(im,W//2,430,64)
d=ImageDraw.Draw(im)
d.text((W/2,560),"Six agents. Une conversation. Zéro ordinateur.",font=F("Poppins-700.ttf",54),fill=INK,anchor="mm")
d.text((W/2,650),"Vous pilotez, l'IA exécute.",font=F("Poppins-800.ttf",64),fill=DGREEN,anchor="mm")
t="Réservez votre démo"; f=F("Poppins-700.ttf",42); w=d.textbbox((0,0),t,font=f)[2]
cx,cy=W//2,790
d.rounded_rectangle([cx-w//2-48,cy-42,cx+w//2+48,cy+42],42,fill=GREEN+(255,))
d.text((cx,cy),t,font=f,fill=WHITE,anchor="mm")
im.convert("RGB").save("work/outro_logo.png")
D=5.0; DF=int(D*FPS)
r=subprocess.run(["ffmpeg","-y","-loop","1","-t",f"{D}","-i","work/outro_logo.png",
     "-vf",f"scale={W*2}:{H*2},zoompan=z='min(zoom+0.0005,1.05)':d={DF}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s={W}x{H}:fps={FPS},setsar=1,fade=t=in:d=0.5,fade=t=out:st={D-0.6}:d=0.6",
     "-c:v","libx264","-preset","medium","-crf","20","-pix_fmt","yuv420p","-r",str(FPS),"-frames:v",str(DF),"work/outro.mp4"],stderr=subprocess.PIPE)
if r.returncode: print(r.stderr.decode()[-500:]); raise SystemExit(1)
print("outro OK")
