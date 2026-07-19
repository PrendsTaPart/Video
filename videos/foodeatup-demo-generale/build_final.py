#!/usr/bin/env python3
"""Assemble final: xfade 8 séquences + sous-titres arrondis + VO placée + BGM -22dB + poster."""
import os, subprocess
from PIL import Image, ImageDraw, ImageFont
os.chdir(os.path.dirname(os.path.abspath(__file__)))
W,H,FPS=1920,1080,30
FD="/home/user/Video/videos/rapidocms-presentation-4min/assets/fonts"
BGM="/home/user/Video/videos/stories-foodeatup-30j/audio/bgm.mp3"
WK="work"; OUT="output"; os.makedirs(OUT,exist_ok=True); os.makedirs(f"{WK}/subs",exist_ok=True)
def F(w,s): return ImageFont.truetype(f"{FD}/Poppins-{w}.ttf",s)
VENC=["-c:v","libx264","-preset","medium","-crf","18","-pix_fmt","yuv420p","-r",str(FPS)]
def dur(f): return float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f]).strip())
def run(cmd,name):
    r=subprocess.run(cmd,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
    if r.returncode: print("ERR",name,r.stderr.decode()[-1600:]); raise SystemExit(1)
    print("ok",name)

SEQ=[f"{WK}/seq/s{i}.mp4" for i in range(8)]
D=[dur(s) for s in SEQ]; X=0.5
# global start of each clip in xfade output
S=[0.0]; running=D[0]
for k in range(1,8):
    S.append(running-X); running=running+D[k]-X
T=running
print("clip starts",[round(x,2) for x in S],"T",round(T,2))

# ---------- xfade chain ----------
trans=["fade","fade","slideleft","fade","slideleft","fade","fade"]
inp=[]
for s in SEQ: inp+=["-i",s]
fc=""; prev="[0:v]"
for k in range(1,8):
    lab=f"[x{k}]"; off=S[k]
    fc+=f"{prev}[{k}:v]xfade=transition={trans[k-1]}:duration={X}:offset={off:.3f}{lab};"
    prev=lab
fc=fc.rstrip(";")
run(["ffmpeg","-y"]+inp+["-filter_complex",fc,"-map",prev,"-t",f"{T:.2f}"]+VENC+[f"{WK}/body.mp4"],"xfade body")

# ---------- subtitle PNGs (rounded translucent box, bottom) ----------
def wrap(d,t,f,mw):
    out=[];cur=""
    for w in t.split():
        s=(cur+" "+w).strip()
        if d.textlength(s,font=f)<=mw: cur=s
        else: out.append(cur);cur=w
    out.append(cur);return out
def sub_png(text,path,fs=50):
    im=Image.new("RGBA",(W,H),(0,0,0,0)); d=ImageDraw.Draw(im); f=F("700",fs)
    lines=wrap(d,text,f,W-460); lh=int(fs*1.28)
    tw=max(d.textlength(l,font=f) for l in lines); bw=int(tw+90); bh=int(lh*len(lines)+40)
    bx=(W-bw)//2; by=H-95-bh
    d.rounded_rectangle([bx,by,bx+bw,by+bh],30,fill=(15,26,35,205))
    y=by+20
    for l in lines:
        lw=d.textlength(l,font=f); d.text(((W-lw)//2,y),l,font=f,fill=(255,255,255,255)); y+=lh
    im.save(path)

SUBS=[
 (3.3,6.4,"Gérer un restaurant : stocks, équipes, normes, clients…"),
 (6.5,9.3,"…et trop souvent, des tableurs et des cahiers."),
 (16.7,20.2,"FoodEatUp pilote vos stocks en temps réel."),
 (20.3,23.6,"Chaque vente déstocke automatiquement."),
 (34.2,37.2,"Vos factures ? Photographiez-les."),
 (37.3,40.2,"L'OCR lit, extrait et met vos prix à jour."),
 (49.7,53.2,"Le contrôle d'hygiène ? Vous êtes déjà prêt."),
 (53.3,56.6,"Tout est relevé, horodaté, exportable en un clic."),
 (65.7,68.5,"En salle comme en cuisine…"),
 (68.6,72.0,"…des écrans routent chaque ticket au bon poste."),
 (85.7,88.6,"Votre site de commande en ligne ?"),
 (88.7,91.0,"L'IA le génère en dix minutes."),
 (91.1,93.9,"Vos clients commandent, vous encaissez."),
 (99.0,101.2,"FoodEatUp."),
]
for i,(a,b,t) in enumerate(SUBS): sub_png(t,f"{WK}/subs/sub{i}.png")
# overlay all subs on body
inp=["-i",f"{WK}/body.mp4"]
for i in range(len(SUBS)): inp+=["-loop","1","-t",f"{T:.2f}","-i",f"{WK}/subs/sub{i}.png"]
fc="[0:v]setsar=1[b0];"; prev="[b0]"
for i,(a,b,t) in enumerate(SUBS,1):
    s=f"[{i}:v]format=rgba,fade=t=in:st={SUBS[i-1][0]}:d=0.25:alpha=1,fade=t=out:st={SUBS[i-1][1]-0.25}:d=0.25:alpha=1[s{i}];"
    fc+=s+f"{prev}[s{i}]overlay=0:0:enable='between(t,{SUBS[i-1][0]},{SUBS[i-1][1]})'[b{i}];"; prev=f"[b{i}]"
fc=fc.rstrip(";")
run(["ffmpeg","-y"]+inp+["-filter_complex",fc,"-map",prev,"-t",f"{T:.2f}"]+VENC+[f"{WK}/body_sub.mp4"],"subs overlay")

# ---------- audio: VO placed + BGM -22dB ----------
VO=[("b1",3.1),("b2",16.5),("b3",34.0),("b4",49.5),("b5",65.5),("b6",85.5),("b7",98.8)]
inp=[]
for vid,off in VO: inp+=["-i",f"{WK}/vo/{vid}.mp3"]
inp+=["-stream_loop","-1","-i",BGM]
fc=""
for i,(vid,off) in enumerate(VO):
    ms=int(off*1000); fc+=f"[{i}:a]adelay={ms}|{ms}[a{i}];"
fc+="".join(f"[a{i}]" for i in range(len(VO)))+f"amix=inputs={len(VO)}:normalize=0[vox];"
fc+=f"[{len(VO)}:a]volume=0.08,afade=t=out:st={T-2.5:.2f}:d=2.5[bg];"
fc+=f"[vox][bg]amix=inputs=2:normalize=0,loudnorm=I=-16:TP=-1.5:LRA=11[a]"
run(["ffmpeg","-y"]+inp+["-filter_complex",fc,"-map","[a]","-t",f"{T:.2f}","-c:a","aac","-b:a","192k",f"{WK}/audio.m4a"],"audio")

# ---------- mux + poster ----------
run(["ffmpeg","-y","-i",f"{WK}/body_sub.mp4","-i",f"{WK}/audio.m4a","-map","0:v","-map","1:a",
     "-c:v","copy","-c:a","aac","-b:a","192k","-movflags","+faststart","-shortest",f"{OUT}/demo-generale.mp4"],"mux final")
run(["ffmpeg","-y","-ss","5","-i",f"{OUT}/demo-generale.mp4","-frames:v","1","-q:v","2",f"{OUT}/demo-generale-poster.jpg"],"poster")
print("DONE",round(dur(f"{OUT}/demo-generale.mp4"),1),"s")
