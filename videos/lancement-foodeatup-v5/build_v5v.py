#!/usr/bin/env python3
"""V5 déclinaison 9:16 (1080x1920, ~30s) : plans 1, sting, séquence refus (4x2s), SR, sommet, offre.
Réutilise VO + FLOW de la V5 16:9. Sound design : voix nue p1/p7, tics, dings, sting."""
import os, subprocess
from PIL import Image, ImageDraw, ImageFont, ImageFilter
HERE=os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
BASE="/home/user/Video"; FD=f"{BASE}/videos/rapidocms-presentation-4min/assets/fonts"
LOGO=f"{BASE}/studio-video/assets/brand/logo"; SCR=f"{BASE}/assets/screens/foodeatup"
BGM=f"{BASE}/videos/stories-foodeatup-30j/audio/bgm.mp3"; CHIME=f"{BASE}/videos/serie-30-e01/assets/sfx/chime.mp3"
STING=f"{BASE}/videos/lancement-foodeatup-v1/composition/logo-sting/sting-in.mp4"
def F(n,s): return ImageFont.truetype(os.path.join(FD,n),s)
P800=lambda s:F("Poppins-800.ttf",s); P700=lambda s:F("Poppins-700.ttf",s); P600=lambda s:F("Poppins-600.ttf",s)
ANTH=(15,26,35); BLUE=(0,123,255); ORANGE=(255,165,0); CREAM=(252,249,230); WHITE=(255,255,255); INK=(35,31,32); RED=(224,49,49); SKY=(166,208,255)
MARK=Image.open(f"{LOGO}/foodeatup-mark-eight.png").convert("RGBA")
W,H=1080,1920; FPS=30
os.makedirs("fv",exist_ok=True); os.makedirs("wv",exist_ok=True); os.makedirs("renders",exist_ok=True)
VENC=["-c:v","libx264","-preset","medium","-crf","20","-pix_fmt","yuv420p","-r",str(FPS),"-c:a","aac","-b:a","192k","-ar","44100","-ac","2"]
def dur(f): return float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f]).strip())
def run(cmd,n):
    r=subprocess.run(cmd,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
    if r.returncode!=0: print("ERR",n,r.stderr.decode()[-1300:]); raise SystemExit(1)
def wrap(dr,t,f,mw):
    o=[];c=""
    for w in t.split():
        s=(c+" "+w).strip()
        if dr.textbbox((0,0),s,font=f)[2]<=mw: c=s
        else: o.append(c); c=w
    o.append(c); return o
def cover(im,w=W,h=H):
    r=max(w/im.width,h/im.height); im=im.resize((int(im.width*r),int(im.height*r)),Image.LANCZOS)
    x=(im.width-w)//2; y=(im.height-h)//2; return im.crop((x,y,x+w,y+h))
def wm(im):
    m=MARK.resize((44,88),Image.LANCZOS); a=m.split()[3].point(lambda p:int(p*0.4)); m.putalpha(a); im.alpha_composite(m,(56,250))
def manifesto(txt,out,fs=82,fg=CREAM,accent=None):
    im=Image.new("RGBA",(W,H),ANTH+(255,)); g=Image.new("RGBA",(W,H),(0,0,0,0)); ImageDraw.Draw(g).ellipse([W//2-420,H//2-460,W//2+420,H//2+460],fill=SKY+(22,)); im.alpha_composite(g.filter(ImageFilter.GaussianBlur(150)))
    wm(im); d=ImageDraw.Draw(im); f=P800(fs); lines=wrap(d,txt,f,W-180); lh=fs+20; y=(H-lh*len(lines))//2
    for l in lines: d.text((W/2,y+lh/2),l,font=f,fill=fg,anchor="mm"); y+=lh
    if accent: d.rectangle([W//2-80,y+16,W//2+80,y+24],fill=accent+(255,))
    im.convert("RGB").save(f"fv/{out}.png")
manifesto("Non. Je ne vais pas licencier votre chef de partie.","p1",fs=90,fg=WHITE)
manifesto("Personne n'est devenu cuisinier pour remplir un tableau de températures.","p7",fs=76,fg=CREAM,accent=ORANGE)
# FLOW refus verticaux + croix
for slug,label in [("flow02-dresser","Dresser"),("flow03-sentir","Sentir"),("flow04-rassurer","Rassurer"),("flow05-connaitre","Connaître")]:
    im=cover(Image.open(f"assets-generes/{slug}.jpg").convert("RGBA")); sc=Image.new("RGBA",(W,H),(6,10,18,90)); im.alpha_composite(sc); wm(im); d=ImageDraw.Draw(im)
    cx,cy,r=W-170,300,66; d.ellipse([cx-r,cy-r,cx+r,cy+r],outline=RED+(255,),width=12); d.line([cx-32,cy-32,cx+32,cy+32],fill=RED+(255,),width=13); d.line([cx-32,cy+32,cx+32,cy-32],fill=RED+(255,),width=13)
    d.text((90,1560),label,font=P800(96),fill=WHITE,anchor="lm"); im.convert("RGB").save(f"fv/not_{slug[4:6]}.png")
# SR verticaux
def sr(screen,label,out,pdf=False):
    im=Image.new("RGBA",(W,H),ANTH+(255,)); wm(im); d=ImageDraw.Draw(im); bx,by,bw,bh=80,560,920,860
    d.rounded_rectangle([bx,by,bx+bw,by+bh],24,outline=BLUE+(255,),width=8,fill=WHITE+(255,))
    for i,cxx in enumerate([bx+32,bx+66,bx+100]): d.ellipse([cxx-9,by+22,cxx+9,by+40],fill=[(255,95,86),(255,189,46),(39,201,63)][i]+(255,))
    if pdf:
        d.rounded_rectangle([bx+300,by+280,bx+620,by+620],16,fill=(245,247,250,255),outline=(210,215,225,255),width=3)
        d.text((bx+460,by+400),"PDF",font=P800(96),fill=BLUE,anchor="mm"); d.text((bx+460,by+510),"conforme",font=P700(40),fill=INK,anchor="mm")
    else:
        s=Image.open(f"{SCR}/{screen}").convert("RGBA"); rr=min((bw-40)/s.width,(bh-80)/s.height); s=s.resize((int(s.width*rr),int(s.height*rr)),Image.LANCZOS)
        im.alpha_composite(s,(bx+(bw-s.width)//2,by+56+(bh-80-s.height)//2))
    d=ImageDraw.Draw(im); d.ellipse([90,300,158,368],fill=ORANGE+(255,)); d.line([106,334,120,348],fill=INK,width=9); d.line([120,348,146,314],fill=INK,width=9)
    d.text((186,334),label,font=P800(60),fill=ORANGE,anchor="lm"); im.convert("RGB").save(f"fv/{out}.png")
sr("checklist-hygiene.png","Le tableau","sr1"); sr("ajout-produit.png","La carte","sr2"); sr(None,"Le PDF","sr3",pdf=True)
# offre verticale
im=Image.new("RGBA",(W,H),ANTH+(255,)); g=Image.new("RGBA",(W,H),(0,0,0,0)); ImageDraw.Draw(g).ellipse([W-460,-160,W+140,440],fill=BLUE+(40,)); im.alpha_composite(g.filter(ImageFilter.GaussianBlur(120))); wm(im); d=ImageDraw.Draw(im)
d.text((W/2,720),"-50%",font=P800(300),fill=ORANGE,anchor="mm")
f=P700(52); t="30 places bêta"; w=d.textbbox((0,0),t,font=f)[2]; d.rounded_rectangle([W//2-w//2-46,980,W//2+w//2+46,1076],44,fill=BLUE+(255,)); d.text((W/2,1028),t,font=f,fill=INK,anchor="mm")
d.text((W/2,1170),"Jusqu'au 31 août 2026",font=P700(44),fill=SKY,anchor="mm")
d.text((W/2,1300),"Lien en bio",font=P800(60),fill=WHITE,anchor="mm"); im.convert("RGB").save("fv/p9.png")
print("V5v frames OK")

# ---- assemble ----
def ass(text,d,path):
    words=text.split(); cues=[words[i:i+4] for i in range(0,len(words),4)]; n=max(1,len(cues)); step=d/n
    def tf(t): h=int(t//3600);m=int((t%3600)//60);s=t%60; return f"{h:d}:{m:02d}:{s:05.2f}"
    hdr=("[Script Info]\nScriptType: v4.00+\nPlayResX: 1080\nPlayResY: 1920\n\n[V4+ Styles]\n"
      "Format: Name,Fontname,Fontsize,PrimaryColour,OutlineColour,BackColour,Bold,BorderStyle,Outline,Shadow,Alignment,MarginL,MarginR,MarginV,Encoding\n"
      "Style: D,Poppins,56,&H00FFFFFF,&H00202020,&H64000000,-1,1,5,1,2,80,80,240,1\n\n[Events]\nFormat: Layer,Start,End,Style,Name,MarginL,MarginR,MarginV,Effect,Text\n")
    ev=[f"Dialogue: 0,{tf(i*step)},{tf(max((i+1)*step-0.05,i*step+0.2))},D,,0,0,0,,{' '.join(c)}" for i,c in enumerate(cues)]
    open(path,"w").write(hdr+"\n".join(ev)+"\n")
def still(png,vo,out,extra=0.7,sub=None):
    d=dur(vo)+extra
    S=""
    if sub: ass(sub,d,f"wv/{out}.ass"); S=f",subtitles=wv/{out}.ass:fontsdir='{FD}'"
    fc=f"[0:v]scale={W}:{H},setsar=1,fade=t=in:d=0.3{S}[v];[1:a]adelay=250|250,apad=whole_dur={d:.3f},aformat=channel_layouts=stereo[a]"
    run(["ffmpeg","-y","-loop","1","-t",f"{d:.3f}","-i",png,"-i",vo,"-filter_complex",fc,"-map","[v]","-map","[a]","-t",f"{d:.3f}"]+VENC+[f"wv/{out}.mp4"],out)
still("fv/p1.png","audio/v1.mp3","p1",extra=1.2)
run(["ffmpeg","-y","-i",STING,"-filter_complex",f"[0:v]scale={W}:{H},setsar=1,fps={FPS}[v];[0:a]aresample=44100,aformat=channel_layouts=stereo[a]","-map","[v]","-map","[a]"]+VENC+["wv/sting.mp4"],"sting")
# séquence refus 4x
d5=dur("audio/v5.mp3")+0.5; each=d5/4
for i,fr in enumerate(["not_02","not_03","not_04","not_05"]):
    z="min(zoom+0.0009,1.06)" if i%2==0 else "if(eq(on,0),1.06,max(zoom-0.0009,1.0))"
    run(["ffmpeg","-y","-loop","1","-t",f"{each:.3f}","-i",f"fv/{fr}.png","-vf",f"scale={W*2}:{H*2},zoompan=z='{z}':d={int(each*FPS)}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s={W}x{H}:fps={FPS},setsar=1,fade=t=in:d=0.12"]+VENC[:-8]+["-an","-frames:v",str(int(each*FPS)),f"wv/p5_{i}.mp4"],f"p5_{i}")
open("wv/p5l.txt","w").write("".join(f"file 'p5_{i}.mp4'\n" for i in range(4)))
run(["ffmpeg","-y","-f","concat","-safe","0","-i","wv/p5l.txt","-c","copy","wv/p5v.mp4"],"p5v"); d5v=dur("wv/p5v.mp4")
ass("Elle ne dresse pas. Elle ne sent pas. Elle ne rassure pas. Elle ne connaît pas votre cliente.",d5v,"wv/p5.ass")
tic="".join(f"[2:a]atrim=0:0.12,adelay={int(i*each*1000)}|{int(i*each*1000)},volume=0.4[t{i}];" for i in range(4)); tm="".join(f"[t{i}]" for i in range(4))
fc=(f"[0:v]subtitles=wv/p5.ass:fontsdir='{FD}'[v];[1:a]adelay=250|250,apad=whole_dur={d5v:.3f}[vo];{tic}{tm}amix=inputs=4:normalize=0[tt];[vo][tt]amix=inputs=2:normalize=0,aformat=channel_layouts=stereo[a]")
run(["ffmpeg","-y","-i","wv/p5v.mp4","-i","audio/v5.mp3","-i",CHIME,"-filter_complex",fc,"-map","[v]","-map","[a]","-t",f"{d5v:.3f}"]+VENC+["wv/p5.mp4"],"p5")
# SR 3x
d6=dur("audio/v6.mp3")+0.8; e6=d6/3
for i,fr in enumerate(["sr1","sr2","sr3"]):
    run(["ffmpeg","-y","-loop","1","-t",f"{e6:.3f}","-i",f"fv/{fr}.png","-vf",f"scale={W}:{H},setsar=1,fade=t=in:d=0.1"]+VENC[:-8]+["-an","-frames:v",str(int(e6*FPS)),f"wv/p6_{i}.mp4"],f"p6_{i}")
open("wv/p6l.txt","w").write("".join(f"file 'p6_{i}.mp4'\n" for i in range(3)))
run(["ffmpeg","-y","-f","concat","-safe","0","-i","wv/p6l.txt","-c","copy","wv/p6v.mp4"],"p6v"); d6v=dur("wv/p6v.mp4")
ass("Elle remplit le tableau. Elle range la carte. Elle sort le PDF.",d6v,"wv/p6.ass")
ding="".join(f"[2:a]adelay={int(i*e6*1000)}|{int(i*e6*1000)},volume=0.6[d{i}];" for i in range(3)); dm="".join(f"[d{i}]" for i in range(3))
fc=(f"[0:v]subtitles=wv/p6.ass:fontsdir='{FD}'[v];[1:a]adelay=200|200,apad=whole_dur={d6v:.3f}[vo];{ding}{dm}amix=inputs=3:normalize=0[dd];[vo][dd]amix=inputs=2:normalize=0,aformat=channel_layouts=stereo[a]")
run(["ffmpeg","-y","-i","wv/p6v.mp4","-i","audio/v6.mp3","-i",CHIME,"-filter_complex",fc,"-map","[v]","-map","[a]","-t",f"{d6v:.3f}"]+VENC+["wv/p6.mp4"],"p6")
still("fv/p7.png","audio/v7.mp3","p7",extra=1.4)
still("fv/p9.png","audio/v9.mp3","p9",extra=1.0,sub="Trente places. Pas une de plus. Le lien est en bio.")
order=["p1","sting","p5","p6","p7","p9"]; open("wv/all.txt","w").write("".join(f"file '{p}.mp4'\n" for p in order))
run(["ffmpeg","-y","-f","concat","-safe","0","-i","wv/all.txt","-c","copy","wv/master.mp4"],"master")
TOT=dur("wv/master.mp4"); acc=0; w1=(0,0); w7=(0,0)
for p in order:
    dd=dur(f"wv/{p}.mp4")
    if p=="p1": w1=(acc,acc+dd)
    if p=="p7": w7=(acc,acc+dd)
    acc+=dd
fc=(f"[1:a]atrim=0:{TOT:.3f},asetpts=N/SR/TB,volume='if(between(t,{w1[0]:.2f},{w1[1]:.2f})+between(t,{w7[0]:.2f},{w7[1]:.2f}),0.012,0.05)':eval=frame,afade=t=in:st=0:d=1.0,afade=t=out:st={TOT-1.5:.3f}:d=1.5[bg];[0:a][bg]amix=inputs=2:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[a]")
run(["ffmpeg","-y","-i","wv/master.mp4","-stream_loop","-1","-i",BGM,"-filter_complex",fc,"-map","0:v","-map","[a]","-c:v","copy","-c:a","aac","-b:a","192k","-movflags","+faststart","renders/foodeatup-v5-objection-9x16.mp4"],"FINAL")
print("DONE",round(dur("renders/foodeatup-v5-objection-9x16.mp4"),1),"s")
