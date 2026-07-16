#!/usr/bin/env python3
"""Bumpers d'agent : image chef (Ken Burns) + médaillon avatar Michael + icône WhatsApp + lower-third + VO."""
import os, subprocess
from PIL import Image, ImageDraw, ImageFont, ImageFilter
os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.makedirs("work/bmp", exist_ok=True)
BASE="/home/user/Video"; FD=f"{BASE}/videos/rapidocms-presentation-4min/assets/fonts"
MIKA=f"{BASE}/videos/stories-foodeatup-30j/assets/avatar/mika.mp4"
WA="work/wa_flat.png"
W,H=1920,1080; FPS=30
ANTH=(15,26,35); BLUE=(0,123,255); ORANGE=(255,165,0); SKY=(166,208,255); WHITE=(255,255,255)
def F(n,s): return ImageFont.truetype(f"{FD}/{n}",s)
VENC=["-c:v","libx264","-preset","medium","-crf","20","-pix_fmt","yuv420p","-r",str(FPS)]
def dur(f): return float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f]).strip())
def run(c,n):
    r=subprocess.run(c,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
    if r.returncode: print("ERR",n,r.stderr.decode()[-900:]); raise SystemExit(1)
    print("ok",n,round(dur(c[-1]),2))

# circle mask for avatar medallion
D=360
m=Image.new("L",(D,D),0); ImageDraw.Draw(m).ellipse([0,0,D,D],fill=255)
m.save("work/circle360.png")

AG=[("gen","chef1-config","GEN_MCP","Configuration"),
    ("haccp","chef2-haccp","MCP_HACCP","Conformité"),
    ("gf","chef3-gf","MCP_GF","Fournisseurs"),
    ("rh","chef4-rh","MCP_RH","Ressources humaines"),
    ("stock","chef5-stock","MCP_stock","Stocks"),
    ("prod","chef6-prod","MCP_production","Production")]

def card(key,name,domain):
    """RGBA overlay full-frame : scrim bas + lower-third + libellé WhatsApp."""
    im=Image.new("RGBA",(W,H),(0,0,0,0)); d=ImageDraw.Draw(im)
    # bottom gradient scrim
    grad=Image.new("L",(1,H),0)
    for y in range(H):
        grad.putpixel((0,y), int(235* max(0,(y-560)/(H-560))**1.3))
    grad=grad.resize((W,H)); sc=Image.new("RGBA",(W,H),(6,10,18,255)); sc.putalpha(grad); im.alpha_composite(sc)
    # left accent + lower third
    d.rectangle([120,H-250,132,H-120],fill=ORANGE+(255,))
    d.text((160,H-250),name,font=F("Poppins-800.ttf",70),fill=WHITE)
    d.text((160,H-160),domain,font=F("Poppins-600.ttf",44),fill=SKY)
    # "Accessible depuis WhatsApp" tag centered under the icon (top-right)
    d.text((W-40,235),"Accessible depuis WhatsApp",font=F("Poppins-600.ttf",28),fill=WHITE,anchor="ra")
    im.save(f"work/bmp/card_{key}.png")

for key,chef,name,domain in AG:
    card(key,name,domain)
    vo=f"audio/vo_{key}.mp3"; d=dur(vo)+1.1; DF=int(d*FPS)
    out=f"work/bmp/{key}.mp4"
    fc=(
      # chef bg Ken Burns
      f"[0:v]scale={W*2}:{H*2}:force_original_aspect_ratio=increase,crop={W*2}:{H*2},"
      f"zoompan=z='min(zoom+0.0006,1.07)':d={DF}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s={W}x{H}:fps={FPS},setsar=1,fade=t=in:d=0.4[bgv];"
      # card overlay
      f"[3:v]format=rgba[cd];[bgv][cd]overlay=0:0[b1];"
      # avatar medallion (circle)
      f"[1:v]scale=-2:1000,crop=560:560:(iw-560)/2:60,scale=340:340,setsar=1[avr];"
      f"[4:v]scale=340:340[mk];[avr][mk]alphamerge[avc];"
      f"[b1][avc]overlay={W-500}:{H-500}[b2];"
      # blue ring around medallion
      # whatsapp icon top-right
      f"[2:v]scale=150:150[wa];[b2][wa]overlay={W-210}:70[v];"
      f"[5:a]adelay=400|400,apad=whole_dur={d:.3f}[a]"
    )
    run(["ffmpeg","-y","-loop","1","-t",f"{d:.3f}","-i",f"assets-generes/{chef}.jpg",
         "-i",MIKA,"-i",WA,"-i",f"work/bmp/card_{key}.png","-i","work/circle360.png","-i",vo,
         "-filter_complex",fc,"-map","[v]","-map","[a]","-t",f"{d:.3f}"]+VENC+["-c:a","aac","-b:a","192k",out],key)
print("BUMPERS DONE")
