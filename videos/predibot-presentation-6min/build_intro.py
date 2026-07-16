#!/usr/bin/env python3
"""Logo FoodEatUp au début — thème WhatsApp sable + vert."""
import os, subprocess
from PIL import Image, ImageDraw, ImageFont, ImageFilter
os.chdir(os.path.dirname(os.path.abspath(__file__)))
BASE="/home/user/Video"; FD=f"{BASE}/videos/rapidocms-presentation-4min/assets/fonts"
LOGO=f"{BASE}/studio-video/assets/brand/logo"
W,H=1920,1080; FPS=30
SAND=(233,224,205); SANDHI=(245,239,227); GREEN=(37,211,102); DGREEN=(7,94,84); INK=(17,27,33)
def F(n,s): return ImageFont.truetype(f"{FD}/{n}",s)
def sandbg():
    im=Image.new("RGBA",(W,H),SAND+(255,)); g=Image.new("L",(1,H),0)
    for y in range(H): g.putpixel((0,y),int(255*(y/H)))
    top=Image.new("RGBA",(W,H),SANDHI+(255,)); top.putalpha(g.resize((W,H)).point(lambda p:255-p)); im.alpha_composite(top)
    gl=Image.new("RGBA",(W,H),(0,0,0,0)); ImageDraw.Draw(gl).ellipse([W//2-560,H//2-380,W//2+560,H//2+320],fill=GREEN+(30,))
    im.alpha_composite(gl.filter(ImageFilter.GaussianBlur(180))); return im
im=sandbg()
m=Image.open(f"{LOGO}/foodeatup-logo-horizontal.png").convert("RGBA")
mw=760; m=m.resize((mw,int(m.height*mw/m.width)),Image.LANCZOS)
im.alpha_composite(m,((W-m.width)//2,(H-m.height)//2-70))
d=ImageDraw.Draw(im)
d.text((W/2,H//2+180),"Une infinité de solutions pour gérer votre restaurant",font=F("Poppins-700.ttf",44),fill=DGREEN,anchor="mm")
d.rectangle([W//2-80,H//2+235,W//2+80,H//2+244],fill=GREEN+(255,))
im.convert("RGB").save("work/intro_logo.png")
D=3.0; DF=int(D*FPS)
r=subprocess.run(["ffmpeg","-y","-loop","1","-t",f"{D}","-i","work/intro_logo.png",
     "-vf",f"scale={W*2}:{H*2},zoompan=z='min(zoom+0.0007,1.06)':d={DF}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s={W}x{H}:fps={FPS},setsar=1,fade=t=in:d=0.5,fade=t=out:st={D-0.5}:d=0.5",
     "-c:v","libx264","-preset","medium","-crf","20","-pix_fmt","yuv420p","-r",str(FPS),"-frames:v",str(DF),"work/intro.mp4"],stderr=subprocess.PIPE)
if r.returncode: print(r.stderr.decode()[-500:]); raise SystemExit(1)
print("intro OK")
