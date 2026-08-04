#!/usr/bin/env python3
"""Segments narratifs : hook marché, Mika intro, cartons d'alerte."""
import os, subprocess, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter
os.chdir(os.path.dirname(os.path.abspath(__file__)))
BASE="/home/user/Video"; FD=f"{BASE}/videos/rapidocms-presentation-4min/assets/fonts"
MIKA=f"{BASE}/videos/stories-foodeatup-30j/assets/avatar/mika.mp4"
W,H=1920,1080; FPS=30
ANTH=(15,26,35); BLUE=(0,123,255); ORANGE=(255,165,0); SKY=(166,208,255); WHITE=(255,255,255); RED=(224,49,49)
SAND=(233,224,205); SANDHI=(245,239,227); GREEN=(37,211,102); DGREEN=(7,94,84); INK=(17,27,33); BUBBLE=(220,248,198)
def F(n,s): return ImageFont.truetype(f"{FD}/{n}",s)
def sandbg():
    im=Image.new("RGBA",(W,H),SAND+(255,)); g=Image.new("L",(1,H),0)
    for y in range(H): g.putpixel((0,y),int(255*(y/H)))
    top=Image.new("RGBA",(W,H),SANDHI+(255,)); top.putalpha(g.resize((W,H)).point(lambda p:255-p)); im.alpha_composite(top)
    gl=Image.new("RGBA",(W,H),(0,0,0,0)); ImageDraw.Draw(gl).ellipse([W//2-560,H//2-380,W//2+560,H//2+340],fill=GREEN+(28,))
    im.alpha_composite(gl.filter(ImageFilter.GaussianBlur(180))); return im
def walogo(im,cx,cy,r):
    d=ImageDraw.Draw(im); d.ellipse([cx-r,cy-r,cx+r,cy+r],fill=GREEN+(255,))
    d.polygon([(cx-r*0.55,cy+r*0.5),(cx-r*0.96,cy+r*0.98),(cx-r*0.18,cy+r*0.74)],fill=GREEN+(255,))
    hr=r*0.5; d.arc([cx-hr,cy-hr,cx+hr,cy+hr],200,110,fill=WHITE,width=int(r*0.16))
    d.ellipse([cx-hr*0.92,cy-hr*0.92,cx-hr*0.2,cy-hr*0.2],fill=WHITE); d.ellipse([cx+hr*0.2,cy+hr*0.2,cx+hr*0.92,cy+hr*0.92],fill=WHITE)
VENC=["-c:v","libx264","-preset","medium","-crf","20","-pix_fmt","yuv420p","-r",str(FPS)]
def dur(f): return float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f]).strip())
def run(c,n):
    r=subprocess.run(c,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
    if r.returncode: print("ERR",n,r.stderr.decode()[-700:]); raise SystemExit(1)
    print("ok",n,round(dur(c[-1]),2))

def cover(im,w=W,h=H):
    r=max(w/im.width,h/im.height); im=im.resize((int(im.width*r),int(im.height*r)),Image.LANCZOS)
    x=(im.width-w)//2; y=(im.height-h)//2; return im.crop((x,y,x+w,y+h))

# ---- HOOK : marché (IMG-01) split thermomètre (IMG-02), ~12s ----
# frame A: marché + vignette + texte "Il est 11h."
im=cover(Image.open("assets-generes/img01-hook-marche.jpg").convert("RGBA"))
sc=Image.new("RGBA",(W,H),(6,10,18,90)); im.alpha_composite(sc)
im.convert("RGB").save("work/hook_a.png")
# frame B: split — left marché, right thermomètre with 8C
imL=cover(Image.open("assets-generes/img01-hook-marche.jpg").convert("RGBA"),W//2,H)
imR=cover(Image.open("assets-generes/img02-chambre-froide.jpg").convert("RGBA"),W//2,H)
comp=Image.new("RGBA",(W,H),ANTH+(255,)); comp.paste(imL,(0,0)); comp.paste(imR,(W//2,0))
d=ImageDraw.Draw(comp); d.rectangle([W//2-3,0,W//2+3,H],fill=ANTH+(255,))
# warn badge
d.rounded_rectangle([W//2+W//4-150,H-200,W//2+W//4+150,H-110],20,fill=RED+(235,))
d.text((W//2+W//4,H-155),"8°C",font=F("Poppins-800.ttf",70),fill=WHITE,anchor="mm")
comp.convert("RGB").save("work/hook_b.png")
# assemble hook: A (Ken Burns 6s) + B (5.5s)
run(["ffmpeg","-y","-loop","1","-t","6.2","-i","work/hook_a.png","-vf",
     f"scale={W*2}:{H*2},zoompan=z='min(zoom+0.0006,1.06)':d={int(6.2*FPS)}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s={W}x{H}:fps={FPS},setsar=1,fade=t=in:d=0.5"]+VENC+["-frames:v",str(int(6.2*FPS)),"work/hook_a.mp4"],"hookA")
run(["ffmpeg","-y","-loop","1","-t","5.8","-i","work/hook_b.png","-vf",f"scale={W}:{H},setsar=1,fade=t=in:d=0.4,fade=t=out:st=5.2:d=0.6"]+VENC+["-frames:v",str(int(5.8*FPS)),"work/hook_b.mp4"],"hookB")
open("work/hooklist.txt","w").write("file 'hook_a.mp4'\nfile 'hook_b.mp4'\n")
run(["ffmpeg","-y","-f","concat","-safe","0","-i","work/hooklist.txt","-c","copy","work/hook.mp4"],"hook")

# ---- MIKA intro : avatar buste gauche + halo + baseline (durée = VO intro) ----
DM=dur("audio/vo_intro.mp3")+0.8
# background card with halo + right-side text
bgc=sandbg(); walogo(bgc,1790,150,58); d=ImageDraw.Draw(bgc)
d.text((1180,380),"Jamais devant",font=F("Poppins-800.ttf",86),fill=INK)
d.text((1180,486),"un ordinateur.",font=F("Poppins-800.ttf",86),fill=INK)
d.text((1180,640),"Votre restaurant,",font=F("Poppins-700.ttf",50),fill=DGREEN)
d.text((1180,706),"dans une conversation WhatsApp.",font=F("Poppins-700.ttf",50),fill=DGREEN)
d.rectangle([1180,796,1330,806],fill=GREEN+(255,))
bgc.convert("RGB").save("work/mika_bg.png")
# overlay mika.mp4 (portrait) cropped to left, scaled
run(["ffmpeg","-y","-loop","1","-t",f"{DM:.2f}","-i","work/mika_bg.png","-i",MIKA,"-i","audio/vo_intro.mp3",
     "-filter_complex",
     f"[1:v]scale=-2:1400,crop=640:980:(iw-640)/2:40,setsar=1[mk];[0:v][mk]overlay=200:60:shortest=0[v];[2:a]adelay=500|500,apad=whole_dur={DM:.2f}[a]",
     "-map","[v]","-map","[a]","-t",f"{DM:.2f}"]+VENC+["-c:a","aac","-b:a","192k","work/mika.mp4"],"mika")

# ---- ALERTES : 3 cartons qui s'empilent, ~9s (texte + musique, pas de VO) ----
NAL=int(9*FPS)
os.makedirs("work/al",exist_ok=True)
_ALBG=sandbg().convert("RGB")
ALS=["Température anormale","Réception non contrôlée","Stock au plus bas"]
for fi in range(NAL):
    t=fi/FPS; im=_ALBG.copy().convert("RGBA"); d=ImageDraw.Draw(im)
    d.text((W/2,130),"PrediBot ne l'attend pas. Il vous le dit.",font=F("Poppins-800.ttf",62),fill=INK,anchor="mm")
    for i,txt in enumerate(ALS):
        st=0.8+i*1.6; p=0 if t<st else min(1,(t-st)/0.5)
        if p<=0: continue
        y=310+i*190; x=W//2; wdt=1040; a=int(255*p); off=int((1-p)*60)
        d.rounded_rectangle([x-wdt//2,y+off,x+wdt//2,y+134+off],26,fill=BUBBLE+(a,),outline=GREEN+(a,),width=6)
        d.ellipse([x-wdt//2+36,y+38+off,x-wdt//2+96,y+98+off],fill=GREEN+(a,))
        d.text((x-wdt//2+66,y+68+off),"!",font=F("Poppins-800.ttf",50),fill=(255,255,255,a),anchor="mm")
        d.text((x-wdt//2+140,y+67+off),txt,font=F("Poppins-700.ttf",50),fill=(17,27,33,a),anchor="lm")
    if t>6:
        d.text((W/2,H-90),"Sur le téléphone que vous avez déjà dans la main.",font=F("Poppins-700.ttf",40),fill=DGREEN,anchor="mm")
    im.convert("RGB").save(f"work/al/f{fi:04d}.png")
run(["ffmpeg","-y","-framerate",str(FPS),"-i","work/al/f%04d.png"]+VENC+["work/alertes.mp4"],"alertes")
print("WRAP DONE")
