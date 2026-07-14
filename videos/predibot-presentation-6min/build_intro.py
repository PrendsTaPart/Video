#!/usr/bin/env python3
"""Logo FoodEatUp au début : reveal mascotte + baseline, sur charte anthracite."""
import os, subprocess
from PIL import Image, ImageDraw, ImageFont, ImageFilter
os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.makedirs("work", exist_ok=True)
BASE="/home/user/Video"; FD=f"{BASE}/videos/rapidocms-presentation-4min/assets/fonts"
LOGO=f"{BASE}/studio-video/assets/brand/logo"
W,H=1920,1080; FPS=30
ANTH=(15,26,35); SKY=(166,208,255); ORANGE=(255,165,0)
def F(n,s): return ImageFont.truetype(f"{FD}/{n}",s)
# still frame: mascot centered + baseline + soft blue halo
im=Image.new("RGBA",(W,H),ANTH+(255,))
g=Image.new("RGBA",(W,H),(0,0,0,0)); ImageDraw.Draw(g).ellipse([W//2-440,H//2-320,W//2+440,H//2+300],fill=SKY+(26,))
im.alpha_composite(g.filter(ImageFilter.GaussianBlur(150)))
m=Image.open(f"{LOGO}/foodeatup-logo-mascot.png").convert("RGBA")
mw=560; m=m.resize((mw,int(m.height*mw/m.width)),Image.LANCZOS)
im.alpha_composite(m,((W-m.width)//2,(H-m.height)//2-70))
d=ImageDraw.Draw(im)
d.text((W/2,H//2+230),"Une infinité de solutions pour gérer votre restaurant",font=F("Poppins-600.ttf",38),fill=SKY,anchor="mm")
d.rectangle([W//2-70,H//2+285,W//2+70,H//2+292],fill=ORANGE+(255,))
im.convert("RGB").save("work/intro_logo.png")
# 3s: fade in + gentle zoom
run=lambda c: subprocess.run(c,check=True,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
D=3.0; DF=int(D*FPS)
run(["ffmpeg","-y","-loop","1","-t",f"{D}","-i","work/intro_logo.png",
     "-vf",f"scale={W*2}:{H*2},zoompan=z='min(zoom+0.0007,1.06)':d={DF}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s={W}x{H}:fps={FPS},setsar=1,fade=t=in:d=0.5,fade=t=out:st={D-0.5}:d=0.5",
     "-c:v","libx264","-preset","medium","-crf","20","-pix_fmt","yuv420p","-r",str(FPS),"-frames:v",str(DF),"work/intro.mp4"])
print("intro OK", subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0","work/intro.mp4"]).decode().strip())
