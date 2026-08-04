#!/usr/bin/env python3
"""Aperçu PrediBot : démos recadrées RGPD, cadre bleu FoodEatUp + lower-third, concaténées."""
import os, subprocess
os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.makedirs("work/pv", exist_ok=True)
BASE="/home/user/Video"
FD=f"{BASE}/videos/rapidocms-presentation-4min/assets/fonts"
P7=f"{FD}/Poppins-700.ttf"; P6=f"{FD}/Poppins-600.ttf"; P8=f"{FD}/Poppins-800.ttf"
BGM=f"{BASE}/videos/stories-foodeatup-30j/audio/bgm.mp3"
W,H=1920,1080; FPS=30
VENC=["-c:v","libx264","-preset","medium","-crf","20","-pix_fmt","yuv420p","-r",str(FPS)]
def dur(f): return float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f]).strip())
def run(cmd,n):
    r=subprocess.run(cmd,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
    if r.returncode!=0: print("ERR",n,r.stderr.decode()[-900:]); raise SystemExit(1)
    print("ok",n,round(dur(cmd[-1]),2))

CLIPS=[
 ("e08a","GEN_MCP","Configuration","Commande WhatsApp : Ajoute un employe"),
 ("e08b","GEN_MCP","Configuration","Resultat dans FoodEatUp : Employes"),
 ("e08c","GEN_MCP","Configuration","Commande WhatsApp : Ajoute une recette"),
 ("e08d","GEN_MCP","Configuration","Resultat dans FoodEatUp : Mes recettes (52)"),
 ("e09","MCP_HACCP","Conformite","Commande : releve de temperature"),
 ("e10","MCP_HACCP","Conformite","Journal temperatures : 0 conforme / 4 non conformes"),
 ("e11a","MCP_GF","Fournisseurs","Commande : Valide la commande"),
 ("e11b","MCP_GF","Fournisseurs","Resultat : reception livree"),
 ("e12","MCP_RH","Ressources humaines","Conges en attente & equipe"),
 ("e13","MCP_stock","Stocks","Commande : Stocks critiques"),
 ("e14","MCP_stock","Stocks","Dashboard Stock genere"),
 ("e15a","MCP_production","Production","Prevision & rentabilite"),
 ("e15b","MCP_production","Production","Dashboard Production genere"),
]

def esc(t): return t.replace(":","\\:").replace("'","’")

parts=[]
for sid,agent,dom,sub in CLIPS:
    src=f"extraits/{sid}.mp4"; out=f"work/pv/{sid}.mp4"; d=dur(src)
    lt=f"{agent}   ·   {dom}"
    fc=(f"color=c=0x0F1A23:s={W}x{H}:d={d:.2f}:r={FPS}[bg];"
        f"[0:v]scale=-2:840:force_original_aspect_ratio=decrease,setsar=1,"
        f"pad=iw+14:ih+14:7:7:color=0x007BFF[v];"
        f"[bg][v]overlay=(W-w)/2:52[o];"
        # lower-third bar
        f"[o]drawbox=x=0:y=946:w={W}:h=134:color=0x0B1220@0.92:t=fill,"
        f"drawbox=x=0:y=946:w=10:h=134:color=0x007BFF:t=fill,"
        f"drawtext=fontfile='{P8}':text='{esc(lt)}':fontcolor=white:fontsize=44:x=54:y=974,"
        f"drawtext=fontfile='{P6}':text='{esc(sub)}':fontcolor=0xA6D0FF:fontsize=32:x=54:y=1028,"
        f"drawtext=fontfile='{P7}':text='PrediBot · apercu recadre (RGPD)':fontcolor=white@0.7:fontsize=26:x={W}-tw-40:y=40[out]")
    run(["ffmpeg","-y","-i",src,"-filter_complex",fc,"-map","[out]","-t",f"{d:.2f}"]+VENC+["-an",out],sid)
    parts.append(out)

# title card 3s
tc="work/pv/title.mp4"
fc=(f"color=c=0x0F1A23:s={W}x{H}:d=3:r={FPS}[bg];"
    f"[bg]drawtext=fontfile='{P8}':text='PrediBot':fontcolor=white:fontsize=140:x=(w-tw)/2:y=360,"
    f"drawtext=fontfile='{P6}':text='Votre restaurant tient dans une conversation':fontcolor=0xA6D0FF:fontsize=46:x=(w-tw)/2:y=540,"
    f"drawtext=fontfile='{P7}':text='Apercu des demos recadrees — 6 agents':fontcolor=0xFFA500:fontsize=40:x=(w-tw)/2:y=640[out]")
run(["ffmpeg","-y","-filter_complex",fc,"-map","[out]","-t","3"]+VENC+["-an",tc],"title")

order=[tc]+parts
open("work/pv/list.txt","w").write("".join(f"file '{os.path.basename(p)}'\n" for p in order))
run(["ffmpeg","-y","-f","concat","-safe","0","-i","work/pv/list.txt","-c","copy","work/pv/silent.mp4"],"concat")
TOT=dur("work/pv/silent.mp4")
# BGM bed low, loudnorm
fc=(f"[1:a]volume=0.16,afade=t=in:st=0:d=1.5,afade=t=out:st={TOT-1.8:.2f}:d=1.8,loudnorm=I=-16:TP=-1.5:LRA=11[a]")
os.makedirs("composition/renders",exist_ok=True)
run(["ffmpeg","-y","-i","work/pv/silent.mp4","-stream_loop","-1","-i",BGM,"-filter_complex",fc,
     "-map","0:v","-map","[a]","-c:v","copy","-c:a","aac","-b:a","160k","-shortest","-movflags","+faststart",
     "composition/renders/predibot-apercu-demos.mp4"],"FINAL")
print("DONE",round(dur("composition/renders/predibot-apercu-demos.mp4"),1),"s")
