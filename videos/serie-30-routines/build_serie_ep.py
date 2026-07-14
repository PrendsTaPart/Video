#!/usr/bin/env python3
"""Compositeur d'épisode — Série « 30 routines » (1080x1920, ~30s, local gratuit).
Beats : hook Mika → la routine → le prompt (chat) → le résultat → outro Mika + CTA.
BraindCode + label épisode, sous-titres ASS burnés, médaillon Mika (générique) hook/outro, BGM.
Usage : python3 build_serie_ep.py <NUM>"""
import os, subprocess, sys, textwrap
from PIL import Image, ImageDraw, ImageFont, ImageFilter
HERE=os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
BASE="/home/user/Video"; FD=f"{BASE}/videos/rapidocms-presentation-4min/assets/fonts"
MIKA=f"{BASE}/videos/stories-foodeatup-30j/assets/avatar/mika.mp4"; BGM=f"{BASE}/videos/stories-foodeatup-30j/audio/bgm.mp3"
def F(n,s): return ImageFont.truetype(os.path.join(FD,n),s)
P800=lambda s:F("Poppins-800.ttf",s); P700=lambda s:F("Poppins-700.ttf",s); P600=lambda s:F("Poppins-600.ttf",s)
NAVY=(16,20,44); CYAN=(0,209,255); VIO=(139,110,246); WHITE=(255,255,255); INK=(20,22,40); DIM=(150,160,200)
W,H=1080,1920; FPS=30
VENC=["-c:v","libx264","-preset","medium","-crf","20","-pix_fmt","yuv420p","-r",str(FPS),"-c:a","aac","-b:a","192k","-ar","44100","-ac","2"]

EP={
 10:{"title":"Le brief du lundi","cta":"Abonne-toi","prompt":"Mon brief du lundi",
     "subs":{"in":"Le lundi matin ne devrait jamais commencer dans le brouillard.",
     "routine":"Le brief du lundi, c'est ta semaine en une page : trésorerie, ventes, pipeline, et les 3 priorités des 7 prochains jours.",
     "prompt":"Tu demandes : Mon brief du lundi.",
     "cas":"Léa ouvre son ordi : 90 couverts la semaine passée, 2 mois d'avance de cash, cette semaine lancer les réservations de groupe. Fini la réunion d'une heure.",
     "out":"Ta boîte a un cerveau. Demain, on lui apprend à VENDRE. Nouvelle saison, abonne-toi."}},
 11:{"title":"Trouve 20 prospects","cta":"Lien en bio","prompt":"Prospecte les boulangeries de Lyon",
     "subs":{"in":"Pendant que tu bois ton café, ton pipeline se remplit tout seul.",
     "routine":"La prospection automatique cherche tes futurs clients là où ils sont : elle scanne, qualifie, dédoublonne et range dans ton CRM.",
     "prompt":"Tu dis : Prospecte les boulangeries de Lyon.",
     "cas":"En 10 minutes : 20 établissements trouvés sur Maps, avec adresse, téléphone et note. Zéro doublon. Le pipeline de Léa vient de se remplir.",
     "out":"La routine complète est dans notre plugin, lien en bio. Demain : le cold email qui obtient vraiment des réponses."}},
 12:{"title":"Le cold email qui répond","cta":"À demain","prompt":"Écris un cold email à cette entreprise",
     "subs":{"in":"Le cold email copié-collé est mort. Voici son remplaçant.",
     "routine":"L'IA lit le prospect avant d'écrire — son site, son actu, son métier — puis rédige un email personnalisé, structuré pour donner envie de répondre.",
     "prompt":"Tu dis : Écris un cold email à cette entreprise.",
     "cas":"Pour Léa : un email qui parle du menu du midi de la boulangerie ciblée, pas un texte générique. Résultat : 3 premières réponses.",
     "out":"Envoie ça à un commercial qui galère. À demain, pour savoir enfin où en sont tes deals."}},
}
import json as _json
_jf=os.path.join(HERE,"episodes.json")
if os.path.exists(_jf):
    for k,v in _json.load(open(_jf)).items(): EP[int(k)]=v
N=int(sys.argv[1]); E=EP[N]; P=f"{BASE}/videos/serie-30-e{N:02d}"; A=f"{P}/audio"
os.makedirs(f"{P}/frames",exist_ok=True); os.makedirs(f"{P}/work",exist_ok=True); os.makedirs(f"{P}/deliverable",exist_ok=True); os.makedirs(f"{P}/subs",exist_ok=True)
_m=Image.new("L",(300,300),0); ImageDraw.Draw(_m).ellipse([0,0,299,299],fill=255); _m.save(f"{P}/work/mask300.png")
def dur(f): return float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f]).strip())
def run(cmd,n):
    r=subprocess.run(cmd,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
    if r.returncode!=0: print("ERR",n,r.stderr.decode()[-1200:]); raise SystemExit(1)
def bg():
    im=Image.new("RGBA",(W,H),NAVY+(255,)); g=Image.new("RGBA",(W,H),(0,0,0,0))
    ImageDraw.Draw(g).ellipse([W-520,-160,W+180,520],fill=CYAN+(30,)); ImageDraw.Draw(g).ellipse([-220,H-560,360,H+120],fill=VIO+(34,))
    im.alpha_composite(g.filter(ImageFilter.GaussianBlur(150))); d=ImageDraw.Draw(im)
    d.text((60,80),"BraindCode",font=P700(40),fill=WHITE,anchor="lm")
    lab=f"E{N} / 30"; f=P700(34); w=d.textbbox((0,0),lab,font=f)[2]; d.rounded_rectangle([W-60-w-36,60,W-60,116],14,fill=VIO+(255,)); d.text((W-60-18,88),lab,font=f,fill=WHITE,anchor="rm")
    return im
def wrap(dr,t,f,mw):
    out=[];cur=""
    for wd in t.split():
        s=(cur+" "+wd).strip()
        if dr.textbbox((0,0),s,font=f)[2]<=mw: cur=s
        else: out.append(cur); cur=wd
    out.append(cur); return out
def head(im,kicker,title,ky=560):
    d=ImageDraw.Draw(im); d.text((W/2,ky),kicker,font=P700(40),fill=CYAN,anchor="mm")
    f=P800(78)
    for i,l in enumerate(wrap(d,title,f,900)): d.text((W/2,ky+90+i*92),l,font=f,fill=WHITE,anchor="mm")
# beat frames
im=bg(); head(im,"30 ROUTINES",E["title"],ky=980); im.convert("RGB").save(f"{P}/frames/in.png")   # hook (Mika ajouté à l'assemble)
im=bg(); head(im,"LA ROUTINE",E["title"]); im.convert("RGB").save(f"{P}/frames/routine.png")
im=bg(); d=ImageDraw.Draw(im); d.text((W/2,520),"LE PROMPT",font=P700(40),fill=CYAN,anchor="mm")
f=P700(52); lines=wrap(d,f'« {E["prompt"]} »',f,860); bh=len(lines)*66+70; d.rounded_rectangle([90,640,990,640+bh],28,fill=(34,40,74,255),outline=CYAN+(255,),width=3)
yy=690
for l in lines: d.text((130,yy),l,font=f,fill=WHITE,anchor="lm"); yy+=66
cy=640+bh+50; d.ellipse([90,cy,150,cy+60],fill=CYAN+(255,)); d.line([106,cy+30,120,cy+44],fill=INK,width=8); d.line([120,cy+44,144,cy+16],fill=INK,width=8)
d.text((172,cy+30),"Exécuté par l'IA",font=P700(40),fill=CYAN,anchor="lm"); im.convert("RGB").save(f"{P}/frames/prompt.png")
im=bg(); head(im,"LE RÉSULTAT","",ky=560)
im.convert("RGB").save(f"{P}/frames/cas.png")
im=bg(); d=ImageDraw.Draw(im)
f=P700(52); cta=E["cta"]; w=d.textbbox((0,0),cta,font=f)[2]; d.rounded_rectangle([W//2-w//2-46,1360,W//2+w//2+46,1456],44,fill=CYAN+(255,)); d.text((W/2,1408),cta,font=f,fill=INK,anchor="mm")
d.text((W/2,1520),f"Épisode {N} / 30",font=P600(34),fill=DIM,anchor="mm"); im.convert("RGB").save(f"{P}/frames/out.png")

# ASS subtitles
def ass(text,d,path):
    words=text.split(); cues=[words[i:i+4] for i in range(0,len(words),4)]; n=max(1,len(cues)); step=d/n
    def tf(t): h=int(t//3600);m=int((t%3600)//60);s=t%60; return f"{h:d}:{m:02d}:{s:05.2f}"
    hdr=("[Script Info]\nScriptType: v4.00+\nPlayResX: 1080\nPlayResY: 1920\n\n[V4+ Styles]\n"
      "Format: Name,Fontname,Fontsize,PrimaryColour,OutlineColour,BackColour,Bold,BorderStyle,Outline,Shadow,Alignment,MarginL,MarginR,MarginV,Encoding\n"
      "Style: D,Poppins,58,&H00FFFFFF,&H00C08A00,&H64000000,-1,1,5,1,2,80,80,210,1\n\n[Events]\nFormat: Layer,Start,End,Style,Name,MarginL,MarginR,MarginV,Effect,Text\n")
    ev=[f"Dialogue: 0,{tf(i*step)},{tf(max((i+1)*step-0.05,i*step+0.2))},D,,0,0,0,,{' '.join(c)}" for i,c in enumerate(cues)]
    open(path,"w").write(hdr+"\n".join(ev)+"\n")

def beat(name,med=False,off=8):
    vo=f"{A}/{name}.mp3"; d=dur(vo)+(0.9 if med else 0.6); png=f"{P}/frames/{name}.png"; sub=f"{P}/subs/{name}.ass"; ass(E["subs"][name],d,sub)
    S=f"subtitles={sub}:fontsdir='{FD}'"
    if med:
        fc=(f"[0:v]scale={W}:{H},setsar=1[b];[1:v]crop=480:480:120:80,scale=300:300,setsar=1[mk];[mk][2:v]alphamerge[mc];"
            f"[b][mc]overlay=390:470:format=auto,{S},fade=t=in:d=0.3[v];[3:a]adelay=250|250,apad=whole_dur={d:.3f},aformat=channel_layouts=stereo[a]")
        cmd=["ffmpeg","-y","-loop","1","-t",f"{d:.3f}","-i",png,"-ss",str(off),"-t",f"{d:.3f}","-i",MIKA,"-loop","1","-i",f"{P}/work/mask300.png","-i",vo,"-filter_complex",fc,"-map","[v]","-map","[a]","-t",f"{d:.3f}"]+VENC+[f"{P}/work/{name}.mp4"]
    else:
        fc=f"[0:v]scale={W}:{H},setsar=1,{S},fade=t=in:d=0.3[v];[1:a]adelay=250|250,apad=whole_dur={d:.3f},aformat=channel_layouts=stereo[a]"
        cmd=["ffmpeg","-y","-loop","1","-t",f"{d:.3f}","-i",png,"-i",vo,"-filter_complex",fc,"-map","[v]","-map","[a]","-t",f"{d:.3f}"]+VENC+[f"{P}/work/{name}.mp4"]
    run(cmd,name); print("beat",name,round(d,1))
for b,m in [("in",True),("routine",False),("prompt",False),("cas",False),("out",True)]: beat(b,med=m)
open(f"{P}/work/list.txt","w").write("".join(f"file '{b}.mp4'\n" for b in ["in","routine","prompt","cas","out"]))
run(["ffmpeg","-y","-f","concat","-safe","0","-i",f"{P}/work/list.txt","-c","copy",f"{P}/work/master.mp4"],"master")
TOT=dur(f"{P}/work/master.mp4")
out=f"{P}/deliverable/serie-30-e{N:02d}.mp4"
fc=(f"[1:a]atrim=0:{TOT:.3f},asetpts=N/SR/TB,volume=0.05,afade=t=in:st=0:d=1.0,afade=t=out:st={TOT-1.6:.3f}:d=1.6[bg];[0:a][bg]amix=inputs=2:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[a]")
run(["ffmpeg","-y","-i",f"{P}/work/master.mp4","-stream_loop","-1","-i",BGM,"-filter_complex",fc,"-map","0:v","-map","[a]","-c:v","copy","-c:a","aac","-b:a","192k","-movflags","+faststart",out],"FINAL")
print("DONE E%d"%N,round(dur(out),1),"s ->",out)
