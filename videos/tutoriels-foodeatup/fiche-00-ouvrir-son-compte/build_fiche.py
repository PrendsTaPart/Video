#!/usr/bin/env python3
"""Fiche 00 — montage vertical 1080x1920. Blocs A-K, VO Adam, médaillon statique, cartons, zooms, sous-titres, filigrane, sting."""
import os, subprocess, math, json
from PIL import Image, ImageDraw, ImageFont, ImageFilter
os.chdir(os.path.dirname(os.path.abspath(__file__)))
W,H,FPS=1080,1920,30
BLUE=(0,123,255); ORANGE=(255,165,0); INK=(15,26,35); WHITE=(255,255,255)
FD="/home/user/Video/videos/rapidocms-presentation-4min/assets/fonts"
def F(w,s): return ImageFont.truetype(f"{FD}/Poppins-{w}.ttf",s)
VENC=["-c:v","libx264","-preset","medium","-crf","20","-pix_fmt","yuv420p","-r",str(FPS)]
A="assets"; BR=f"{A}/brand"; VO="build/fiche-00/vo"; SEG="build/fiche-00/segments"; OUT="build/fiche-00/out"
os.makedirs(SEG,exist_ok=True); os.makedirs(OUT,exist_ok=True); os.makedirs("build/fiche-00/png",exist_ok=True)
PNG="build/fiche-00/png"
def dur(f): return float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f]).strip())
def run(c,n):
    r=subprocess.run(c,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
    if r.returncode: print("ERR",n,r.stderr.decode()[-1500:]); raise SystemExit(1)
    print("ok",n,round(dur(c[-1]),2))

VD={k:dur(f"{VO}/bloc-{k}.mp3") for k in "ABCDEFGHIJK"}
print("VO durations",{k:round(v,2) for k,v in VD.items()})

# ---------- shared PNGs ----------
# branded background (dark + toque motif)
def branded_bg(path):
    im=Image.new("RGB",(W,H),INK);
    glow=Image.new("L",(W,H),0); ImageDraw.Draw(glow).ellipse([W*0.5-520,H*0.30-520,W*0.5+520,H*0.30+520],fill=255)
    glow=glow.filter(ImageFilter.GaussianBlur(200))
    im=Image.composite(Image.new("RGB",(W,H),(22,42,62)),im,glow)
    mo=Image.new("L",(W,H),0); dm=ImageDraw.Draw(mo); cx,cy=W//2,int(H*0.34)
    dm.ellipse([cx-260,cy-40,cx+260,cy+240],fill=255)
    for ox in (-170,0,170): dm.ellipse([cx+ox-140,cy-260,cx+ox+140,cy+40],fill=255)
    mo=mo.filter(ImageFilter.GaussianBlur(30))
    im=Image.composite(Image.new("RGB",(W,H),(30,50,72)),im,mo.point(lambda p:int(p*0.14)))
    im.save(path)
branded_bg(f"{PNG}/bg.png")

# circular chef medallion + ring
def medallion(path,sz=640):
    src=Image.open(f"{BR}/chef-canon.png").convert("RGB")
    s=min(src.size); src=src.crop(((src.width-s)//2,0,(src.width+s)//2,s)).resize((sz,sz))
    mask=Image.new("L",(sz,sz),0); ImageDraw.Draw(mask).ellipse([0,0,sz,sz],fill=255)
    out=Image.new("RGBA",(sz+16,sz+16),(0,0,0,0)); d=ImageDraw.Draw(out)
    d.ellipse([0,0,sz+16,sz+16],fill=BLUE+(255,))
    out.paste(src,(8,8),mask); out.save(path)
medallion(f"{PNG}/medal.png")

# filigrane white logo (top-left, 25%)
def filigrane(path):
    lg=Image.open(f"{BR}/logo-foodeatup-blanc.png").convert("RGBA"); lg.thumbnail((300,120))
    im=Image.new("RGBA",(W,H),(0,0,0,0));
    al=lg.split()[3].point(lambda p:int(p*0.25)); lg.putalpha(al)
    im.paste(lg,(48,60),lg); im.save(path)
filigrane(f"{PNG}/filig.png")

# step cartons
def carton(path,txt,col=BLUE,tc=WHITE):
    f=F("800",50); tmp=ImageDraw.Draw(Image.new("RGB",(10,10))); tw=tmp.textlength(txt,font=f)
    im=Image.new("RGBA",(int(tw+70),96),(0,0,0,0)); d=ImageDraw.Draw(im)
    d.rounded_rectangle([0,0,tw+68,92],26,fill=col+(255,)); d.text((34,16),txt,font=f,fill=tc)
    im.save(path)
for i,name in [(1,"Étape 1"),(2,"Étape 2"),(3,"Étape 3"),(4,"Étape 4"),(5,"Étape 5")]:
    carton(f"{PNG}/etape{i}.png",name)
# bandeau LE TOUR DE MAIN (orange, full width top)
def bandeau(path,txt):
    im=Image.new("RGBA",(W,110),(0,0,0,0)); d=ImageDraw.Draw(im)
    d.rectangle([0,0,W,110],fill=ORANGE+(255,)); f=F("800",52); tw=d.textlength(txt,font=f)
    d.text(((W-tw)//2,28),txt,font=f,fill=(0,0,0,255)); im.save(path)
bandeau(f"{PNG}/bandeau.png","LE TOUR DE MAIN")

# subtitle png (bottom, safe zone above nothing)
def wrap(d,t,f,mw):
    out=[];cur=""
    for w in t.split():
        s=(cur+" "+w).strip()
        if d.textlength(s,font=f)<=mw: cur=s
        else: out.append(cur);cur=w
    out.append(cur);return out
def sub_png(txt,path,fs=52):
    im=Image.new("RGBA",(W,H),(0,0,0,0)); d=ImageDraw.Draw(im); f=F("700",fs)
    lines=wrap(d,txt,f,W-160)[:2]; lh=int(fs*1.3); tot=lh*len(lines)
    y0=H-300-tot
    for ln in lines:
        lw=d.textlength(ln,font=f); x=(W-lw)//2
        for dx in(-3,3):
            for dy in(-3,3): d.text((x+dx,y0+dy),ln,font=f,fill=(0,0,0,255))
        d.text((x,y0),ln,font=f,fill=WHITE+(255,)); y0+=lh
    im.save(path)

# clean block texts (for subtitles, exact script, no SSML)
CLEAN={
'A':["Première fiche du livre.","On ouvre votre compte FoodEatUp.","Quatre étapes, quatre-vingt-dix secondes.","Un seul endroit où ça coince :","l'e-mail de confirmation."],
'B':["Sortez une adresse e-mail professionnelle.","Pas votre adresse perso.","C'est ce compte qui pilotera","tout l'établissement.","Le jour où vous ajoutez un associé,","c'est de là que ça part."],
'C':["Étape une.","Sur la page de connexion,","cliquez sur Inscription."],
'D':["Étape deux.","Saisissez votre e-mail,","votre mot de passe, votre nom.","Validez."],
'E':["Étape trois.","Ouvrez votre boîte mail.","Cliquez sur le lien de vérification.","Pas là ? Regardez dans les spams,","et marquez-le Non indésirable.","Sinon vos alertes de stock","finiront au même endroit."],
'F':["Étape quatre.","Revenez sur la page de connexion.","Entrez vos identifiants.","Vous êtes dedans."],
'G':["Étape cinq, pour le jour où.","Mot de passe oublié :","le lien est sur la page de connexion.","Saisissez votre e-mail,","vous recevez un lien sécurisé,","vous en définissez un nouveau.","Trente secondes, sans appeler le support."],
'H':["Le tour de main.","Ne créez jamais ce compte","avec une adresse partagée par l'équipe.","C'est votre compte administrateur.","Il ouvre tout."],
'I':["La version minute ? Il n'y en a pas.","La connexion à votre compte","ne passe pas par l'IA,","et c'est très bien comme ça."],
'J':["Compte ouvert, e-mail confirmé,","mot de passe sous contrôle."],
'K':["Fiche numéro un : votre boutique.","Parce qu'un compte,","ce n'est pas encore un restaurant."],
}
def sub_overlays(blk,d):  # returns list of (png, t0, t1)
    lines=CLEAN[blk]; n=len(lines); res=[]
    for i,ln in enumerate(lines):
        t0=d*i/n; t1=d*(i+1)/n
        p=f"{PNG}/sub_{blk}_{i}.png"; sub_png(ln,p); res.append((p,t0,t1))
    return res

# ---------- medallion block ----------
def medal_block(blk,out,bandeau_png=None):
    d=VD[blk]; subs=sub_overlays(blk,d)
    inp=["-loop","1","-t",f"{d:.2f}","-i",f"{PNG}/bg.png",
         "-loop","1","-t",f"{d:.2f}","-i",f"{PNG}/medal.png",
         "-loop","1","-t",f"{d:.2f}","-i",f"{PNG}/filig.png"]
    idx=3; extra=[]
    if bandeau_png: inp+=["-loop","1","-t",f"{d:.2f}","-i",bandeau_png]; bnd=idx; idx+=1
    sub_idx=[]
    for p,_,_ in subs: inp+=["-loop","1","-t",f"{d:.2f}","-i",p]; sub_idx.append(idx); idx+=1
    inp+=["-i",f"{VO}/bloc-{blk}.mp3"]; aud=idx
    fc=f"[0:v]scale={W}:{H}[bg];"
    # medallion gentle breathing scale, centered upper
    fc+=f"[1:v]scale=640:640,setsar=1[md];[bg][md]overlay=(W-w)/2:280:enable=1[v1];"
    fc+="[v1][2:v]overlay=0:0[v2];"; cur="[v2]"; c=3
    if bandeau_png:
        fc+=f"{cur}[{bnd}:v]overlay=0:70[vb];"; cur="[vb]"
    for j,si in enumerate(sub_idx):
        t0,t1=subs[j][1],subs[j][2]
        fc+=f"{cur}[{si}:v]overlay=0:0:enable='between(t,{t0:.2f},{t1:.2f})'[s{j}];"; cur=f"[s{j}]"
    fc=fc.rstrip(";")
    run(["ffmpeg","-y"]+inp+["-filter_complex",fc,"-map",cur,"-map",f"{aud}:a","-t",f"{d:.2f}"]+VENC+["-c:a","aac","-b:a","192k",out],f"medal {blk}")

# ---------- screen block ----------
def screen_block(blk,out,rush_spec,carton_png,zoom_c=(0.5,0.45),blur_band=None):
    """rush_spec: list of (file,t0,t1). Concatène, crop vertical, speed->VO, overlays."""
    d=VD[blk]
    # 1) build raw screen (crop vertical + concat segments)
    parts=[]
    for i,(f,t0,t1) in enumerate(rush_spec):
        p=f"{SEG}/{blk}_raw{i}.mp4"
        vf=f"crop=1080:1920:0:190,setsar=1,fps={FPS}"
        run(["ffmpeg","-y","-ss",f"{t0}","-to",f"{t1}","-i",f,"-vf",vf,"-an"]+VENC+[p],f"{blk} raw{i}")
        parts.append(p)
    if len(parts)>1:
        lst=f"{SEG}/{blk}_list.txt"; open(lst,"w").write("".join(f"file '{os.path.basename(p)}'\n" for p in parts))
        raw=f"{SEG}/{blk}_cat.mp4"; run(["ffmpeg","-y","-f","concat","-safe","0","-i",lst,"-c","copy",raw],f"{blk} cat")
    else: raw=parts[0]
    rawd=dur(raw); factor=rawd/d
    # speed: cap 2.5; if slower than VO, min 0.7 then freeze
    vf=[]
    if factor>1: f2=min(factor,2.5); vf.append(f"setpts=PTS/{f2:.3f}")
    elif factor<1: f2=max(factor,0.7); vf.append(f"setpts=PTS/{f2:.3f}")
    else: f2=1.0
    if blur_band:  # PII blur: (y,h)
        by,bh=blur_band; vf.append(f"boxblur=18:enable=1")  # global soft; refined below via crop-blur not trivial -> band overlay instead
    # slow zoom toward button center (emphasis)
    cx,cy=zoom_c
    vf.append(f"scale={W*2}:{H*2}")
    vf.append(f"zoompan=z='min(zoom+0.0004,1.06)':d={int(d*FPS)}:x='iw*{cx}-(iw/zoom/2)':y='ih*{cy}-(ih/zoom/2)':s={W}x{H}:fps={FPS}")
    vfs=",".join(vf)
    base=f"{SEG}/{blk}_base.mp4"
    # ensure length == d (freeze tail if short)
    run(["ffmpeg","-y","-i",raw,"-vf",vfs+f",tpad=stop_mode=clone:stop_duration=3,trim=0:{d:.2f},setpts=PTS-STARTPTS","-an","-t",f"{d:.2f}"]+VENC+[base],f"{blk} base")
    # overlays: filigrane + carton + subtitles + PII band blur + audio
    subs=sub_overlays(blk,d)
    inp=["-i",base,"-loop","1","-t",f"{d:.2f}","-i",f"{PNG}/filig.png","-loop","1","-t",f"{d:.2f}","-i",carton_png]
    idx=3; sub_idx=[]
    for p,_,_ in subs: inp+=["-loop","1","-t",f"{d:.2f}","-i",p]; sub_idx.append(idx); idx+=1
    inp+=["-i",f"{VO}/bloc-{blk}.mp3"]; aud=idx
    fc="[0:v]"
    if blur_band:
        by,bh=blur_band
        fc=f"[0:v]split[b0][b1];[b1]crop={W}:{bh}:0:{by},boxblur=22[bb];[b0][bb]overlay=0:{by}[v0];[v0]"
    fc+="null[base];[base][1:v]overlay=0:0[vf1];[vf1][2:v]overlay=40:150[vc];"; cur="[vc]"
    for j,si in enumerate(sub_idx):
        t0,t1=subs[j][1],subs[j][2]
        fc+=f"{cur}[{si}:v]overlay=0:0:enable='between(t,{t0:.2f},{t1:.2f})'[s{j}];"; cur=f"[s{j}]"
    fc=fc.rstrip(";")
    run(["ffmpeg","-y"]+inp+["-filter_complex",fc,"-map",cur,"-map",f"{aud}:a","-t",f"{d:.2f}"]+VENC+["-c:a","aac","-b:a","192k",out],f"screen {blk}")
    return f2

R=lambda n:f"{A}/rushes/fiche-00/rush-{n}.mp4"
report={}
# medallion blocks
medal_block("A",f"{SEG}/segA.mp4")
medal_block("B",f"{SEG}/segB.mp4")
# screen blocks
report['C']=screen_block("C",f"{SEG}/segC.mp4",[(R(1),0,9)],f"{PNG}/etape1.png",zoom_c=(0.5,0.5))
report['D']=screen_block("D",f"{SEG}/segD.mp4",[(R(2),0,8.6)],f"{PNG}/etape2.png",zoom_c=(0.5,0.5))
report['E']=screen_block("E",f"{SEG}/segE.mp4",[(R(4),0,18.8)],f"{PNG}/etape3.png",zoom_c=(0.5,0.55))
report['F']=screen_block("F",f"{SEG}/segF.mp4",[(R(5),0,13)],f"{PNG}/etape4.png",zoom_c=(0.5,0.5))
report['G']=screen_block("G",f"{SEG}/segG.mp4",[(R(3),0,9.1),(R(4),3,11)],f"{PNG}/etape5.png",zoom_c=(0.5,0.5))
medal_block("H",f"{SEG}/segH.mp4",bandeau_png=f"{PNG}/bandeau.png")
medal_block("I",f"{SEG}/segI.mp4")
medal_block("J",f"{SEG}/segJ.mp4")
medal_block("K",f"{SEG}/segK.mp4")

# opening thumbnail 1.2s (silent) + outro sting 4s + carton fiche suivante
op=Image.open(f"{A}/thumbnails/fiche-00.png").convert("RGB").resize((W,H)); op.save(f"{PNG}/open.png")
run(["ffmpeg","-y","-loop","1","-t","1.2","-i",f"{PNG}/open.png","-f","lavfi","-t","1.2","-i","anullsrc=r=44100:cl=stereo","-vf",f"scale={W}:{H}"]+VENC+["-c:a","aac","-shortest",f"{SEG}/seg0_open.mp4"],"open")
# outro carton on sting
cf=Image.new("RGBA",(W,240),(0,0,0,0)); dd=ImageDraw.Draw(cf); f=F("800",56); t="Fiche n°01 — Monter sa boutique"
lines=wrap(dd,t,f,W-120); y=20
for ln in lines:
    lw=dd.textlength(ln,font=f); dd.text(((W-lw)//2,y),ln,font=f,fill=WHITE+(255,)); y+=76
cf.save(f"{PNG}/nextcard.png")
sd=dur(f"{BR}/sting-outro.mp4")
run(["ffmpeg","-y","-i",f"{BR}/sting-outro.mp4","-loop","1","-t",f"{sd}","-i",f"{PNG}/nextcard.png","-f","lavfi","-t",f"{sd}","-i","anullsrc=r=44100:cl=stereo",
     "-filter_complex",f"[0:v]scale={W}:{H}[v0];[v0][1:v]overlay=0:H-360:enable='gte(t,1.2)'[v]","-map","[v]","-map","2:a","-t",f"{sd}"]+VENC+["-c:a","aac","-shortest",f"{SEG}/seg_outro.mp4"],"outro")

# concat all
order=["seg0_open","segA","segB","segC","segD","segE","segF","segG","segH","segI","segJ","segK","seg_outro"]
lst=f"{SEG}/final_list.txt"; open(lst,"w").write("".join(f"file '{s}.mp4'\n" for s in order))
run(["ffmpeg","-y","-f","concat","-safe","0","-i",lst,"-c:v","libx264","-preset","medium","-crf","20","-pix_fmt","yuv420p","-r",str(FPS),
     "-c:a","aac","-b:a","192k","-movflags","+faststart",f"{OUT}/fiche-00-ouvrir-son-compte.mp4"],"FINAL")
json.dump({"vo":{k:round(v,2) for k,v in VD.items()},"speed_factors":{k:round(v,2) for k,v in report.items()}},open("build/fiche-00/report.json","w"),indent=2)
print("DONE",round(dur(f"{OUT}/fiche-00-ouvrir-son-compte.mp4"),1),"s")
