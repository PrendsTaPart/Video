#!/usr/bin/env python3
"""Montage 6 min : logo->hook->Michael->orch->socle->[bumper+demo]x6->alertes->retour->logo, VO complète + BGM."""
import os, subprocess, glob
from PIL import Image
os.chdir(os.path.dirname(os.path.abspath(__file__)))
BASE="/home/user/Video"; BGM=f"{BASE}/videos/stories-foodeatup-30j/audio/bgm.mp3"; MIKA=f"{BASE}/videos/stories-foodeatup-30j/assets/avatar/mika.mp4"; FPS=30; W,H=1920,1080
VENC=["-c:v","libx264","-preset","veryfast","-crf","21","-pix_fmt","yuv420p","-r",str(FPS)]
def dur(f): return float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f]).strip())
def run(c,n):
    r=subprocess.run(c,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
    if r.returncode: print("ERR",n,r.stderr.decode()[-900:]); raise SystemExit(1)
    print("ok",n)

# --- Michael intro (video-only, dur = vo_intro+1) ---
di=dur("audio/vo_intro.mp3")+1.0
run(["ffmpeg","-y","-loop","1","-t",f"{di:.2f}","-i","work/mika_bg.png","-i",MIKA,"-filter_complex",
     f"[1:v]scale=-2:1400,crop=640:980:(iw-640)/2:40,setsar=1[mk];[0:v][mk]overlay=200:60:shortest=0[v]",
     "-map","[v]","-t",f"{di:.2f}"]+VENC+["-an","work/mika_v.mp4"],"mika_v")

# --- retour marché (IMG-04, dur = vo_retour+1) ---
dr=dur("audio/vo_retour.mp3")+1.0; DF=int(dr*FPS)
run(["ffmpeg","-y","-loop","1","-t",f"{dr:.2f}","-i","assets-generes/img04-retour-marche.jpg","-vf",
     f"scale={W*2}:{H*2}:force_original_aspect_ratio=increase,crop={W*2}:{H*2},zoompan=z='min(zoom+0.0005,1.05)':d={DF}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s={W}x{H}:fps={FPS},setsar=1,fade=t=in:d=0.5,fade=t=out:st={dr-0.6:.2f}:d=0.6"]+VENC+["-frames:v",str(DF),"-an","work/retour.mp4"],"retour")

# --- per-agent demo chunks from seg parts ---
parts=sorted(glob.glob("work/seg/[0-9]*_*.mp4"))
ranges={"gen":(0,10),"haccp":(10,12),"gf":(12,16),"rh":(16,26),"stock":(26,36),"prod":(36,52)}
demo={}
for k,(a,b) in ranges.items():
    lst=f"work/demo_{k}.txt"; open(lst,"w").write("".join(f"file '{os.path.abspath(parts[i])}'\n" for i in range(a,b)))
    run(["ffmpeg","-y","-f","concat","-safe","0","-i",lst,"-c","copy",f"work/demo_{k}.mp4"],f"demo_{k}")
    demo[k]=f"work/demo_{k}.mp4"

# --- strip bumper audio -> video only ---
for k in ranges: run(["ffmpeg","-y","-i",f"work/bmp/{k}.mp4","-an","-c:v","copy",f"work/bmp/{k}_v.mp4"],f"bmp_{k}_v")

# --- timeline ---
SEG=[("logo","work/intro.mp4"),("hook","work/hook.mp4"),("mika","work/mika_v.mp4"),
     ("orch","work/orch.mp4"),("socle","work/socle.mp4")]
for k in ["gen","haccp","gf","rh","stock","prod"]:
    SEG.append((f"bmp_{k}",f"work/bmp/{k}_v.mp4")); SEG.append((f"demo_{k}",demo[k]))
SEG+=[("alertes","work/alertes.mp4"),("retour","work/retour.mp4"),("outro","work/outro.mp4")]

starts={}; acc=0.0
for name,f in SEG: starts[name]=acc; acc+=dur(f)
TOT=acc

# VO placement (segment -> vo file, offset)
VOMAP={"hook":("hook",0.5),"mika":("intro",0.4),"orch":("orch",1.0),"socle":("socle",1.0),
       "bmp_gen":("gen",0.4),"bmp_haccp":("haccp",0.4),"bmp_gf":("gf",0.4),"bmp_rh":("rh",0.4),
       "bmp_stock":("stock",0.4),"bmp_prod":("prod",0.4),"alertes":("alertes",0.6),
       "retour":("retour",0.4),"outro":("outro",0.6)}
place={vo:(starts[seg]+off) for seg,(vo,off) in VOMAP.items()}

# 1) concat video-only
open("work/f6list.txt","w").write("".join(f"file '{os.path.abspath(f)}'\n" for _,f in SEG))
run(["ffmpeg","-y","-f","concat","-safe","0","-i","work/f6list.txt"]+VENC+["-an","work/full6_v.mp4"],"video")

# 2) master audio
VO=list(place.keys())
inp=["-stream_loop","-1","-i",BGM]
for v in VO: inp+=["-i",f"audio/vo_{v}.mp3"]
fc=f"[0:a]volume=0.11,afade=t=in:st=0:d=1.2,afade=t=out:st={TOT-1.8:.2f}:d=1.8[bg];"
labs=["[bg]"]
for i,v in enumerate(VO):
    ms=int(place[v]*1000); fc+=f"[{i+1}:a]adelay={ms}|{ms},volume=1.35[a{i}];"; labs.append(f"[a{i}]")
fc+="".join(labs)+f"amix=inputs={len(labs)}:normalize=0:dropout_transition=0,atrim=0:{TOT:.2f},loudnorm=I=-15:TP=-1.5:LRA=11[a]"
run(["ffmpeg","-y"]+inp+["-filter_complex",fc,"-map","[a]","-ac","2","-ar","44100","work/full6_a.m4a"],"audio")

os.makedirs("composition/renders",exist_ok=True)
run(["ffmpeg","-y","-i","work/full6_v.mp4","-i","work/full6_a.m4a","-map","0:v","-map","1:a",
     "-c:v","copy","-c:a","aac","-b:a","192k","-shortest","-movflags","+faststart",
     "composition/renders/predibot-6min-final.mp4"],"mux")
print("DONE",round(dur("composition/renders/predibot-6min-final.mp4"),1),"s")
print("starts",{k:round(v,1) for k,v in starts.items()})
