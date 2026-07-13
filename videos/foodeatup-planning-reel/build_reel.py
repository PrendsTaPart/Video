#!/usr/bin/env python3
"""Reel FoodEatUp « Planning Équipe » (9:16, ~40s). Charte bleu #007bff.
Plans : intro.mp4 → avatar(placeholder) → démo add_planning.webm en cadre → avatar(placeholder) → outro.
Sous-titres FR burnés. Placeholders avatar à remplacer par la photo dès réception (fichier)."""
import os, subprocess
from PIL import Image, ImageDraw, ImageFont, ImageFilter
HERE=os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
BASE="/home/user/Video"; FD=f"{BASE}/videos/rapidocms-presentation-4min/assets/fonts"
LOGO=f"{BASE}/studio-video/assets/brand/logo"; BGM=f"{BASE}/videos/stories-foodeatup-30j/audio/bgm.mp3"
def F(n,s): return ImageFont.truetype(os.path.join(FD,n),s)
P800=lambda s:F("Poppins-800.ttf",s); P700=lambda s:F("Poppins-700.ttf",s); P600=lambda s:F("Poppins-600.ttf",s)
BLUE=(0,123,255); WHITE=(255,255,255); INK=(28,32,48); LIGHT=(240,245,252)
W,H=1080,1920; FPS=30
MASC=Image.open(f"{LOGO}/foodeatup-logo-mascot.png").convert("RGBA")
os.makedirs("work",exist_ok=True); os.makedirs("frames",exist_ok=True); os.makedirs("subs",exist_ok=True)
VENC=["-c:v","libx264","-preset","medium","-crf","20","-pix_fmt","yuv420p","-r",str(FPS),"-c:a","aac","-b:a","192k","-ar","44100","-ac","2"]
def dur(f): return float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f]).strip())
def run(cmd,n):
    r=subprocess.run(cmd,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
    if r.returncode!=0: print("ERR",n,r.stderr.decode()[-1400:]); raise SystemExit(1)
    print("ok",n,round(dur(cmd[-1]),2))
def grad(c1=BLUE,c2=WHITE):
    im=Image.new("RGB",(W,H),c2); top=Image.new("RGB",(W,H),c1); m=Image.new("L",(W,H),0)
    for y in range(H): ImageDraw.Draw(m).line([(0,y),(W,y)],fill=int(255*max(0,1-y/(H*0.9))))
    return Image.composite(top,im,m).convert("RGBA")
def logo(im,y=150,w=360):
    m=MASC.resize((w,int(MASC.height*w/MASC.width)),Image.LANCZOS); im.alpha_composite(m,((W-m.width)//2,y))
def srt(text,d,path):  # émet de l'ASS (placement bas fiable, contour bleu)
    path=path.replace(".srt",".ass"); w=text.replace(":"," :").split(); cues=[w[i:i+4] for i in range(0,len(w),4)]; n=max(1,len(cues)); step=d/n
    def f(t):
        h=int(t//3600);m=int((t%3600)//60);s=t%60; return f"{h:d}:{m:02d}:{s:05.2f}"
    hdr=("[Script Info]\nScriptType: v4.00+\nPlayResX: 1080\nPlayResY: 1920\n\n[V4+ Styles]\n"
         "Format: Name,Fontname,Fontsize,PrimaryColour,SecondaryColour,OutlineColour,BackColour,Bold,Italic,Underline,StrikeOut,ScaleX,ScaleY,Spacing,Angle,BorderStyle,Outline,Shadow,Alignment,MarginL,MarginR,MarginV,Encoding\n"
         "Style: D,Poppins,62,&H00FFFFFF,&H00FFFFFF,&H00FF7B00,&H64000000,-1,0,0,0,100,100,0,0,1,6,2,2,70,70,250,1\n\n"
         "[Events]\nFormat: Layer,Start,End,Style,Name,MarginL,MarginR,MarginV,Effect,Text\n")
    ev=[f"Dialogue: 0,{f(i*step)},{f(max((i+1)*step-0.05,i*step+0.2))},D,,0,0,0,,{' '.join(c)}" for i,c in enumerate(cues)]
    open(path,"w").write(hdr+"\n".join(ev)+"\n")
def SUB(name): return f"subtitles=subs/{name}.ass:fontsdir='{FD}'"

# ---- Plan A : intro.mp4 en 9:16 (fond flou + intro fit) + VO s1
dA=6.316; srt("FoodEatUp. La gestion de votre établissement simplifiée.",dA,"subs/a.srt")
fc=(f"[0:v]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},boxblur=20:2,eq=brightness=-0.05[bg];"
    f"[0:v]scale={W}:-1[fg];[bg][fg]overlay=(W-w)/2:(H-h)/2,{SUB('a')},setsar=1[v];"
    f"[0:a]volume=0.25[ia];[1:a]adelay=200|200,volume=1.3[vo];[ia][vo]amix=inputs=2:normalize=0:duration=first[a]")
run(["ffmpeg","-y","-i","assets/intro.mp4","-i","audio/s1.mp3","-filter_complex",fc,"-map","[v]","-map","[a]","-t",f"{dA:.3f}"]+VENC+["work/pA.mp4"],"pA")

# ---- Plan avatar placeholder (réutilisable)
def avatar_ph(vo,txt,cta,out,srtname):
    d=dur(vo)+0.6; im=grad(); d2=ImageDraw.Draw(im)
    # médaillon vide (à remplacer par la photo)
    cx,cy,r=W//2,760,300; d2.ellipse([cx-r,cy-r,cx+r,cy+r],fill=WHITE+(255,),outline=BLUE+(255,),width=10)
    d2.text((cx,cy-30),"AVATAR",font=P700(48),fill=(180,200,225),anchor="mm"); d2.text((cx,cy+30),"(photo à venir)",font=P600(30),fill=(190,205,225),anchor="mm")
    logo(im,140,300)
    if cta:
        f=P700(46); w=d2.textbbox((0,0),cta,font=f)[2]; d2.rounded_rectangle([(W-w)//2-44,1360,(W+w)//2+44,1452],40,fill=BLUE+(255,)); d2.text((W/2,1406),cta,font=f,fill=WHITE,anchor="mm")
    im.convert("RGB").save(f"frames/{out}.png"); srt(txt,d,f"subs/{srtname}.srt")
    fc=(f"[0:v]scale={W}:{H},{SUB(srtname)},setsar=1,fade=t=in:d=0.3[v];"
        f"[1:a]adelay=200|200,apad=whole_dur={d:.3f},aformat=channel_layouts=stereo[a]")
    run(["ffmpeg","-y","-loop","1","-t",f"{d:.3f}","-i",f"frames/{out}.png","-i",vo,"-filter_complex",fc,"-map","[v]","-map","[a]","-t",f"{d:.3f}"]+VENC+[f"work/{out}.mp4"],out)
avatar_ph("audio/s2.mp3","Aujourd'hui, on vous montre comment organiser le planning de votre équipe en quelques clics.","","pB","b")
avatar_ph("audio/s4.mp3","Fini le casse-tête des plannings papier ou Excel. Votre équipe reste organisée, où que vous soyez.","Essayez FoodEatUp","pD","d")

# ---- Plan C : démo webm dans cadre navigateur sur fond bleu
dC=dur("audio/s3.mp3")+1.2; srt("Créez un planning. Ajoutez votre équipe, définissez les horaires, validez en temps réel.",dC,"subs/c.srt")
# bg avec cadre
im=grad(); logo(im,120,300); d2=ImageDraw.Draw(im)
d2.text((W/2,470),"Planning Équipe",font=P800(64),fill=WHITE,anchor="mm")
fx,fy,fw,fh=40,600,1000,600
d2.rounded_rectangle([fx,fy,fx+fw,fy+fh],28,fill=WHITE+(255,))
for i,cxx in enumerate([fx+34,fx+70,fx+106]): d2.ellipse([cxx-9,fy+24,cxx+9,fy+42],fill=[(255,95,86),(255,189,46),(39,201,63)][i]+(255,))
im.convert("RGB").save("frames/pC_bg.png")
sp=46.4/(dC-0.3)  # accélère le webm pour tenir le plan
vw=fw-40; vh=int(vw*952/1920)
fc=(f"[0:v]scale={W}:{H},setsar=1[bg];[1:v]setpts=PTS/{sp:.4f},scale={vw}:{vh},setsar=1[wm];"
    f"[bg][wm]overlay={fx+20}:{fy+64},{SUB('c')}[v];"
    f"[2:a]adelay=300|300,apad=whole_dur={dC:.3f},aformat=channel_layouts=stereo[a]")
run(["ffmpeg","-y","-loop","1","-t",f"{dC:.3f}","-i","frames/pC_bg.png","-i","assets/add_planning.webm","-i","audio/s3.mp3",
     "-filter_complex",fc,"-map","[v]","-map","[a]","-t",f"{dC:.3f}"]+VENC+["work/pC.mp4"],"pC")

# ---- Plan E : outro logo + URL
dE=dur("audio/s5.mp3")+1.4; im=grad(BLUE,(230,240,252)); logo(im,720,460); d2=ImageDraw.Draw(im)
d2.text((W/2,1180),"foodeatup.com",font=P800(72),fill=WHITE,anchor="mm")
f=P700(46); cta="Lien en bio"; w=d2.textbbox((0,0),cta,font=f)[2]; d2.rounded_rectangle([(W-w)//2-44,1300,(W+w)//2+44,1392],40,fill=WHITE+(255,)); d2.text((W/2,1346),cta,font=f,fill=BLUE,anchor="mm")
im.convert("RGB").save("frames/pE.png")
fc=(f"[0:v]scale={W}:{H},setsar=1,fade=t=in:d=0.3[v];[1:a]adelay=200|200,apad=whole_dur={dE:.3f},aformat=channel_layouts=stereo[a]")
run(["ffmpeg","-y","-loop","1","-t",f"{dE:.3f}","-i","frames/pE.png","-i","audio/s5.mp3","-filter_complex",fc,"-map","[v]","-map","[a]","-t",f"{dE:.3f}"]+VENC+["work/pE.mp4"],"pE")

# ---- concat + BGM
order=["pA","pB","pC","pD","pE"]; open("work/all.txt","w").write("".join(f"file '{p}.mp4'\n" for p in order))
run(["ffmpeg","-y","-f","concat","-safe","0","-i","work/all.txt","-c","copy","work/master.mp4"],"master")
TOT=dur("work/master.mp4")
fc=(f"[1:a]atrim=0:{TOT:.3f},asetpts=N/SR/TB,volume=0.05,afade=t=in:st=0:d=1.0,afade=t=out:st={TOT-1.6:.3f}:d=1.6[bg];[0:a][bg]amix=inputs=2:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[a]")
run(["ffmpeg","-y","-i","work/master.mp4","-stream_loop","-1","-i",BGM,"-filter_complex",fc,"-map","0:v","-map","[a]","-c:v","copy","-c:a","aac","-b:a","192k","-movflags","+faststart","renders/foodeatup-planning-reel-9x16.mp4"],"FINAL")
print("DONE",round(dur("renders/foodeatup-planning-reel-9x16.mp4"),1),"s")
