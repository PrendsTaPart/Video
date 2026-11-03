#!/usr/bin/env python3
"""Montage COMPLET : logo -> hook -> Mika -> orchestrateur -> socle -> démo(26) -> alertes -> logo, avec VO + BGM."""
import os, subprocess, glob
os.chdir(os.path.dirname(os.path.abspath(__file__)))
BASE="/home/user/Video"; BGM=f"{BASE}/videos/stories-foodeatup-30j/audio/bgm.mp3"; FPS=30
def dur(f): return float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f]).strip())
def run(c,n):
    r=subprocess.run(c,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
    if r.returncode: print("ERR",n,r.stderr.decode()[-900:]); raise SystemExit(1)
    print("ok",n)

# video-only mika
run(["ffmpeg","-y","-i","work/mika.mp4","-an","-c","copy","work/mika_v.mp4"],"mika_v")

# ordered segments (video-only)
SEG=[("work/intro.mp4"),("work/hook.mp4"),("work/mika_v.mp4"),("work/orch.mp4"),("work/socle.mp4"),
     ("work/seg/silent.mp4"),("work/alertes.mp4"),("work/outro.mp4")]
starts={}; acc=0.0
for s in SEG:
    starts[s]=acc; acc+=dur(s)
TOT=acc
demo_start=starts["work/seg/silent.mp4"]

# demo agent block start times (within demo)
parts=sorted(glob.glob("work/seg/[0-9]*_*.mp4")); ps=[]; a=0.0
for p in parts: ps.append(a); a+=dur(p)
agent_partidx=[0,10,12,16,26,36]
agent_names=["gen","haccp","gf","rh","stock","prod"]
agent_t=[demo_start+ps[i] for i in agent_partidx]

# VO placement
place={}
place["hook"]=starts["work/hook.mp4"]+0.5
place["intro"]=starts["work/mika_v.mp4"]+0.4      # Mika intro voice
place["orch"]=starts["work/orch.mp4"]+1.2
for nm,t in zip(agent_names,agent_t): place[nm]=t+0.3
place["outro"]=starts["work/outro.mp4"]+0.7
# socle & alertes : pas de VO (texte + musique)

# 1) concat video
open("work/flist.txt","w").write("".join(f"file '{os.path.abspath(s)}'\n" for s in SEG))
run(["ffmpeg","-y","-f","concat","-safe","0","-i","work/flist.txt",
     "-c:v","libx264","-preset","veryfast","-crf","21","-pix_fmt","yuv420p","-r",str(FPS),"-an","work/full_v.mp4"],"video")

# 2) audio: VO placed + BGM ducked
VO=list(place.keys())
inp=["-stream_loop","-1","-i",BGM]
for v in VO: inp+=["-i",f"audio/vo_{v}.mp3"]
fc=f"[0:a]volume=0.11,afade=t=in:st=0:d=1.2,afade=t=out:st={TOT-1.8:.2f}:d=1.8[bg];"
labs=["[bg]"]
for i,v in enumerate(VO):
    ms=int(place[v]*1000)
    fc+=f"[{i+1}:a]adelay={ms}|{ms},volume=1.35[a{i}];"; labs.append(f"[a{i}]")
fc+="".join(labs)+f"amix=inputs={len(labs)}:normalize=0:dropout_transition=0,atrim=0:{TOT:.2f},loudnorm=I=-15:TP=-1.5:LRA=11[a]"
run(["ffmpeg","-y"]+inp+["-filter_complex",fc,"-map","[a]","-ac","2","-ar","44100","work/full_a.m4a"],"audio")

os.makedirs("composition/renders",exist_ok=True)
run(["ffmpeg","-y","-i","work/full_v.mp4","-i","work/full_a.m4a","-map","0:v","-map","1:a",
     "-c:v","copy","-c:a","aac","-b:a","192k","-shortest","-movflags","+faststart",
     "composition/renders/predibot-6min.mp4"],"mux")
print("DONE",round(dur("composition/renders/predibot-6min.mp4"),1),"s")
print("segment starts:",{os.path.basename(k):round(v,1) for k,v in starts.items()})
print("VO:",{k:round(v,1) for k,v in place.items()})
