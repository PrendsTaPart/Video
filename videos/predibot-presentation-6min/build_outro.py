#!/usr/bin/env python3
"""Logo FoodEatUp à la fin : lockup + promesse + CTA, charte anthracite."""
import os, subprocess
from PIL import Image, ImageDraw, ImageFont, ImageFilter
os.chdir(os.path.dirname(os.path.abspath(__file__)))
BASE="/home/user/Video"; FD=f"{BASE}/videos/rapidocms-presentation-4min/assets/fonts"
LOGO=f"{BASE}/studio-video/assets/brand/logo"
W,H=1920,1080; FPS=30
ANTH=(15,26,35); SKY=(166,208,255); ORANGE=(255,165,0); BLUE=(0,123,255); WHITE=(255,255,255)
def F(n,s): return ImageFont.truetype(f"{FD}/{n}",s)
im=Image.new("RGBA",(W,H),ANTH+(255,))
g=Image.new("RGBA",(W,H),(0,0,0,0)); ImageDraw.Draw(g).ellipse([W//2-460,H//2-340,W//2+460,H//2+300],fill=SKY+(26,))
im.alpha_composite(g.filter(ImageFilter.GaussianBlur(150)))
m=Image.open(f"{LOGO}/foodeatup-logo-mascot.png").convert("RGBA")
mw=520; m=m.resize((mw,int(m.height*mw/m.width)),Image.LANCZOS)
im.alpha_composite(m,((W-m.width)//2,H//2-m.height-30))
d=ImageDraw.Draw(im)
d.text((W/2,H//2+70),"Six agents. Une conversation. Zéro ordinateur.",font=F("Poppins-700.ttf",50),fill=WHITE,anchor="mm")
d.text((W/2,H//2+150),"Vous pilotez, l'IA exécute.",font=F("Poppins-800.ttf",58),fill=ORANGE,anchor="mm")
# CTA pill
t="Réservez votre démo"; f=F("Poppins-700.ttf",40); w=d.textbbox((0,0),t,font=f)[2]
cx,cy=W//2,H//2+280
d.rounded_rectangle([cx-w//2-44,cy-40,cx+w//2+44,cy+40],40,fill=BLUE+(255,))
d.text((cx,cy),t,font=f,fill=WHITE,anchor="mm")
im.convert("RGB").save("work/outro_logo.png")
D=5.0; DF=int(D*FPS)
r=subprocess.run(["ffmpeg","-y","-loop","1","-t",f"{D}","-i","work/outro_logo.png",
     "-vf",f"scale={W*2}:{H*2},zoompan=z='min(zoom+0.0005,1.05)':d={DF}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s={W}x{H}:fps={FPS},setsar=1,fade=t=in:d=0.5,fade=t=out:st={D-0.6}:d=0.6",
     "-c:v","libx264","-preset","medium","-crf","20","-pix_fmt","yuv420p","-r",str(FPS),"-frames:v",str(DF),"work/outro.mp4"],stderr=subprocess.PIPE)
if r.returncode: print(r.stderr.decode()[-600:]); raise SystemExit(1)
print("outro OK", subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0","work/outro.mp4"]).decode().strip())
