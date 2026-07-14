#!/usr/bin/env python3
"""PrediBot — montage démo COMPLET : chaque commande + son résultat, bandeau WhatsApp en haut.
Groupé par agent, lower-third par commande. RGPD crops + delogo."""
import os, subprocess
from PIL import Image, ImageDraw, ImageFont
os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.makedirs("work/seg", exist_ok=True)
BASE="/home/user/Video"; FD=f"{BASE}/videos/rapidocms-presentation-4min/assets/fonts"
BGM=f"{BASE}/videos/stories-foodeatup-30j/audio/bgm.mp3"
P8=f"{FD}/Poppins-800.ttf"; P7=f"{FD}/Poppins-700.ttf"; P6=f"{FD}/Poppins-600.ttf"
W,H=1920,1080; FPS=30
VENC=["-c:v","libx264","-preset","veryfast","-crf","21","-pix_fmt","yuv420p","-r",str(FPS)]
WA="crop=1514:984:392:44,delogo=x=1058:y=890:w=430:h=70"
BR="crop=1904:930:8:100,delogo=x=1440:y=830:w=440:h=70"
def dur(f): return float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f]).strip())
def run(cmd,n):
    r=subprocess.run(cmd,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
    if r.returncode!=0: print("ERR",n,r.stderr.decode()[-800:]); raise SystemExit(1)

def _cls(src,t):
    """WA vs BR by chat-bg warmth, median over many right-side points (robust to white bubbles)."""
    subprocess.run(["ffmpeg","-y","-ss",f"{t:.2f}","-i",f"rushes/{src}.mp4","-frames:v","1","-vf","scale=960:540","work/_cl.png"],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    im=Image.open("work/_cl.png").convert("RGB")
    warms=[]
    for x in range(760,952,24):
        for y in range(110,480,30):
            r,g,b=im.getpixel((x,y)); warms.append(r-b)
    warms.sort(); med=warms[len(warms)//2]
    return "WA" if med>6 else "BR"

def pick(src,a,b):
    """Auto-detect crop and trim off transition frames: longest run containing midpoint."""
    step=0.25; ts=[]
    t=a
    while t<=b: ts.append(round(t,2)); t+=step
    cls=[_cls(src,t) for t in ts]
    mid=len(ts)//2; c=cls[mid]
    lo=mid
    while lo-1>=0 and cls[lo-1]==c: lo-=1
    hi=mid
    while hi+1<len(ts) and cls[hi+1]==c: hi+=1
    a2=ts[lo]+ (0.15 if lo>0 else 0.0); b2=ts[hi]- (0.15 if hi<len(ts)-1 else 0.0)
    if b2-a2<0.6: a2,b2=ts[lo],ts[hi]+step
    return a2,b2,(WA if c=="WA" else BR)

# ---- WhatsApp header asset (green bar + logo + PrediBot online) ----
def F(p,s): return ImageFont.truetype(p,s)
hdr=Image.new("RGBA",(1514,96),(7,94,84,255)); d=ImageDraw.Draw(hdr)
# WhatsApp logo: green circle + white phone/bubble
lx,ly,lr=58,48,30
d.ellipse([lx-lr,ly-lr,lx+lr,ly+lr],fill=(37,211,102,255))
# white speech bubble
d.ellipse([lx-19,ly-19,lx+19,ly+19],fill=(255,255,255,255))
d.polygon([(lx-14,ly+14),(lx-20,ly+22),(lx-6,ly+16)],fill=(255,255,255,255))
# green handset (two rounded strokes)
d.ellipse([lx-11,ly-11,lx+11,ly+11],outline=(37,211,102,255),width=6)
d.line([lx-6,ly-6,lx+6,ly+6],fill=(37,211,102,255),width=7)
d.text((104,26),"PrediBot",font=F(P7,34),fill=(255,255,255,255))
d.text((104,62),"en ligne",font=F(P6,22),fill=(200,240,225,255))
d.text((1514-150,36),"WhatsApp",font=F(P6,24),fill=(200,240,225,255))
hdr.save("work/wa_header.png")

# ---- segments: (agent, label, cmd(src,a,b,crop), res(src,a,b,crop)) ----
S=[
 ("GEN_MCP · Configuration","Ajouter un employe",("config",9,14.5,WA),("config",15.5,20,BR)),
 ("GEN_MCP · Configuration","Ajouter un fournisseur",("config",21.5,29,WA),("config",30,32,BR)),
 ("GEN_MCP · Configuration","Ajouter un ingredient",("config",34,44,WA),("config",45,47,BR)),
 ("GEN_MCP · Configuration","Ajouter un produit menu",("config",49,56,WA),("config",56.5,58.5,WA)),
 ("GEN_MCP · Configuration","Ajouter une recette",("config",64,75,WA),("config",77.4,79.9,BR)),
 ("MCP_HACCP · Conformite","Modifier une temperature",("haccp",3.8,8.8,WA),("haccp",11,15,BR)),
 ("MCP_GF · Fournisseurs","Liste mes commandes",("fournisseur",8.5,11.5,WA),("fournisseur",12.5,18,WA)),
 ("MCP_GF · Fournisseurs","Valider la commande 2986",("fournisseur",16,19.5,WA),("fournisseur",22.5,26,BR)),
 ("MCP_RH · Ressources humaines","Liste mes employes",("rh",3,5.5,WA),("rh",6.5,12,WA)),
 ("MCP_RH · Ressources humaines","Liste mes conges",("rh",21,23.5,WA),("rh",24.5,30,WA)),
 ("MCP_RH · Ressources humaines","Approuver le conge N45",("rh",33,35.5,WA),("rh",38.5,41,WA)),
 ("MCP_RH · Ressources humaines","Rejeter le conge 1023",("rh",36,38.5,WA),("rh",41.5,44,WA)),
 ("MCP_RH · Ressources humaines","Classement des employes",("rh",42,44.5,WA),("rh",48,54,WA)),
 ("MCP_stock · Stocks","Liste mes stocks",("stock",3,5.5,WA),("stock",6.5,12,WA)),
 ("MCP_stock · Stocks","Liste mes recettes",("stock",14.5,17,WA),("stock",17.5,21,WA)),
 ("MCP_stock · Stocks","Verifier le fournisseur louay",("stock",21,23.5,WA),("stock",24.5,27,WA)),
 ("MCP_stock · Stocks","Creer une commande fournisseur",("stock",27.5,30,WA),("stock",30.5,36,BR)),
 ("MCP_stock · Stocks","Generer le dashboard stock",("stock",48,50.5,WA),("stock",54,61.5,BR)),
 ("MCP_production · Production","Liste mes productions",("production",4.5,7.5,WA),("production",8.5,12,WA)),
 ("MCP_production · Production","Verifier ingredients (prod 1594)",("production",12.5,15.5,WA),("production",16.5,20,WA)),
 ("MCP_production · Production","Valider une production",("production",33,36,WA),("production",24.5,32,BR)),
 ("MCP_production · Production","Ajouter une production (recette 195)",("production",56,60,WA),("production",60,62,WA)),
 ("MCP_production · Production","Predire les productions",("production",60.5,63.5,WA),("production",64,72,WA)),
 ("MCP_production · Production","Analyser la rentabilite",("production",72,75,WA),("production",76,84,WA)),
 ("MCP_production · Production","Top plats (30 jours)",("production",84,87,WA),("production",84,88,WA)),
 ("MCP_production · Production","Generer le dashboard production",("production",88,91,WA),("production",104,112.5,BR)),
]

def esc(t): return t.replace(":","\\:").replace("'","’")

def render_part(idx,kind,agent,label,src,a0,b0,_crop):
    a,b,crop=pick(src,a0,b0)
    d=max(0.8,b-a); out=f"work/seg/{idx:02d}_{kind}.mp4"
    tag="Commande" if kind=="cmd" else "Resultat"
    tagcol="0xFFA500" if kind=="cmd" else "0x25D366"
    if crop==WA:
        # crop + WA header stacked on top -> screen 1514x1076
        pre=(f"[0:v]{crop},setsar=1[c];[1:v]null[h];[h][c]vstack=inputs=2[scr];")
        inp=["-ss",f"{a:.2f}","-t",f"{d:.2f}","-i",f"rushes/{src}.mp4","-i","work/wa_header.png"]
    else:
        pre=(f"[0:v]{crop},setsar=1[scr];")
        inp=["-ss",f"{a:.2f}","-t",f"{d:.2f}","-i",f"rushes/{src}.mp4","-f","lavfi","-t",f"{d:.2f}","-i",f"color=c=black:s=2x2"]
    fc=(f"color=c=0x0F1A23:s={W}x{H}:d={d:.2f}:r={FPS}[bg];"+pre+
        f"[scr]scale=-2:788:force_original_aspect_ratio=decrease,pad=iw+14:ih+14:7:7:color=0x007BFF[v];"
        f"[bg][v]overlay=(W-w)/2:36[o];"
        f"[o]drawbox=x=0:y=946:w={W}:h=134:color=0x0B1220@0.94:t=fill,"
        f"drawbox=x=0:y=946:w=12:h=134:color={tagcol}:t=fill,"
        f"drawtext=fontfile='{P6}':text='{tag}':fontcolor={tagcol}:fontsize=30:x=54:y=966,"
        f"drawtext=fontfile='{P8}':text='{esc(label)}':fontcolor=white:fontsize=46:x=54:y=1004,"
        f"drawtext=fontfile='{P7}':text='{esc(agent)}':fontcolor=0xA6D0FF:fontsize=28:x={W}-tw-40:y=40[out]")
    run(["ffmpeg","-y"]+inp+["-filter_complex",fc,"-map","[out]","-t",f"{d:.2f}"]+VENC+["-an",out],out)
    return out

parts=[]
for i,(agent,label,cmd,res) in enumerate(S):
    parts.append(render_part(i,"cmd",agent,label,*cmd))
    parts.append(render_part(i,"res",agent,label,*res))
    print("ok seg",i,label)

open("work/seg/list.txt","w").write("".join(f"file '{os.path.basename(p)}'\n" for p in parts))
run(["ffmpeg","-y","-f","concat","-safe","0","-i","work/seg/list.txt","-c","copy","work/seg/silent.mp4"],"concat")
TOT=dur("work/seg/silent.mp4")
fc=f"[1:a]volume=0.15,afade=t=in:st=0:d=1.2,afade=t=out:st={TOT-1.6:.2f}:d=1.6,loudnorm=I=-16:TP=-1.5:LRA=11[a]"
os.makedirs("composition/renders",exist_ok=True)
run(["ffmpeg","-y","-i","work/seg/silent.mp4","-stream_loop","-1","-i",BGM,"-filter_complex",fc,
     "-map","0:v","-map","[a]","-c:v","copy","-c:a","aac","-b:a","160k","-shortest","-movflags","+faststart",
     "composition/renders/predibot-demos-completes.mp4"],"final")
print("DONE",round(dur("composition/renders/predibot-demos-completes.mp4"),1),"s ·",len(S),"commandes")
