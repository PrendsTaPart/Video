#!/usr/bin/env python3
"""Explainer 'loop engineering' façon enfant de 5 ans — images RapidoCMS + avatar Mika + VO + sous-titres."""
import os, subprocess, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter
os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.makedirs("work/b", exist_ok=True)
BASE="/home/user/Video"; FD=f"{BASE}/videos/rapidocms-presentation-4min/assets/fonts"
MIKA=f"{BASE}/videos/stories-foodeatup-30j/assets/avatar/mika.mp4"
BGM=f"{BASE}/videos/stories-foodeatup-30j/audio/bgm.mp3"
W,H=1920,1080; FPS=30
BLUE=(30,155,240); ORANGE=(255,150,40); INK=(30,40,60); WHITE=(255,255,255)
def F(n,s): return ImageFont.truetype(f"{FD}/{n}",s)
VENC=["-c:v","libx264","-preset","medium","-crf","20","-pix_fmt","yuv420p","-r",str(FPS)]
def dur(f): return float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f]).strip())
def run(c,n):
    r=subprocess.run(c,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
    if r.returncode: print("ERR",n,r.stderr.decode()[-800:]); raise SystemExit(1)
    print("ok",n,round(dur(c[-1]),2))

# --- circle mask for Mika medallion ---
DM=300
m=Image.new("L",(DM,DM),0); ImageDraw.Draw(m).ellipse([0,0,DM,DM],fill=255); m.save("work/mask.png")

# --- caption PNG (wrapped, big, outlined) ---
def wrap(dr,t,f,mw):
    out=[];cur=""
    for w in t.split():
        s=(cur+" "+w).strip()
        if dr.textbbox((0,0),s,font=f)[2]<=mw: cur=s
        else: out.append(cur);cur=w
    out.append(cur);return out
def caption(txt,out,fs=74,col=WHITE,oc=(20,40,80)):
    im=Image.new("RGBA",(W,260),(0,0,0,0)); d=ImageDraw.Draw(im); f=F("Poppins-800.ttf",fs)
    lines=wrap(d,txt,f,W-260); lh=fs+16; y=(260-lh*len(lines))//2+lh//2
    for ln in lines:
        for dx in range(-6,7,2):
            for dy in range(-6,7,2): d.text((W/2+dx,y+dy),ln,font=f,fill=oc+(255,),anchor="mm")
        d.text((W/2,y),ln,font=f,fill=col+(255,),anchor="mm"); y+=lh
    im.save(f"work/b/{out}.png")

# --- rotating loop ring (for the '5 étapes' beat) ---
ring=Image.new("RGBA",(700,700),(0,0,0,0)); dr=ImageDraw.Draw(ring)
for a in range(0,360,30):
    x=350+300*math.cos(math.radians(a)); y=350+300*math.sin(math.radians(a))
    dr.ellipse([x-16,y-16,x+16,y+16],fill=(ORANGE if (a//30)%2 else BLUE)+(230,))
ring.save("work/b/ring.png")

# beats: (vo, image, caption, big_mika)
BEATS=[
 ("v1","img1-robot","Le loop engineering, expliqué en tout simple",True),
 ("v2","img2-manege","Un loop, ça tourne en rond… comme un manège !",False),
 ("v3","img3-arrose","Un petit robot qui arrose la plante, chaque matin",False),
 ("v4","img6-boucle","Il regarde, réfléchit, fait, vérifie… et recommence !",False),
 ("v5","img4-apprend","Tu lui montres UNE fois. Après, il continue tout seul",False),
 ("v6","img5-nuit","Même quand tu dors, il travaille pour toi !",False),
 ("v7","img1-robot","Apprendre à un robot à tourner en rond, tout seul. Magique !",True),
]
parts=[]
for i,(vo,img,cap,big) in enumerate(BEATS):
    caption(cap,f"cap{i}")
    d=dur(f"work/vo_{vo}.mp3")+0.7; DF=int(d*FPS); out=f"work/b/beat{i}.mp4"
    ring_fc=""
    if img=="img6-boucle":
        ring_fc=f"[3:v]scale=760:760,rotate=a=t*0.6:c=none:ow=760:oh=760[rg];[bg2][rg]overlay=(W-w)/2:(H-h)/2-30[bg3];"
    else:
        ring_fc="[bg2]null[bg3];"
    mika_sz=520 if big else 300
    inp=["-loop","1","-t",f"{d:.2f}","-i",f"assets-generes/{img}.jpg","-i",MIKA,"-i","work/mask.png","-i","work/b/ring.png",
         "-i",f"work/b/cap{i}.png","-i",f"work/vo_{vo}.mp3"]
    fc=(
      f"[0:v]scale={W*2}:{H*2}:force_original_aspect_ratio=increase,crop={W*2}:{H*2},"
      f"zoompan=z='min(zoom+0.0009,1.10)':d={DF}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s={W}x{H}:fps={FPS},setsar=1,fade=t=in:d=0.4[bg2];"
      +ring_fc+
      # Mika medallion
      f"[1:v]scale={mika_sz}:-2,crop={mika_sz}:{mika_sz}:0:40,setsar=1[mkc];"
      f"[2:v]scale={mika_sz}:{mika_sz}[mm];[mkc][mm]alphamerge[mk];"
      +(f"[bg3][mk]overlay=(W-w)/2:H-h-150[bg4];" if big else f"[bg3][mk]overlay=70:70[bg4];")+
      # caption bottom
      f"[bg4][4:v]overlay=0:H-300[v];"
      f"[5:a]adelay=250|250,apad=whole_dur={d:.2f}[a]"
    )
    run(["ffmpeg","-y"]+inp+["-filter_complex",fc,"-map","[v]","-map","[a]","-t",f"{d:.2f}"]+VENC+["-c:a","aac","-b:a","192k",out],f"beat{i}")
    parts.append(out)

open("work/b/list.txt","w").write("".join(f"file '{os.path.basename(p)}'\n" for p in parts))
run(["ffmpeg","-y","-f","concat","-safe","0","-i","work/b/list.txt","-c","copy","work/b/silent.mp4"],"concat")
TOT=dur("work/b/silent.mp4")
fc=f"[1:a]volume=0.14,afade=t=in:st=0:d=1,afade=t=out:st={TOT-1.5:.2f}:d=1.5[bg];[0:a][bg]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-15:TP=-1.5:LRA=11[a]"
run(["ffmpeg","-y","-i","work/b/silent.mp4","-stream_loop","-1","-i",BGM,"-filter_complex",fc,"-map","0:v","-map","[a]","-c:v","copy","-c:a","aac","-b:a","192k","-shortest","-movflags","+faststart","composition/renders/loop-engineering-enfant.mp4"],"FINAL")
print("DONE",round(dur("composition/renders/loop-engineering-enfant.mp4"),1),"s")
