#!/usr/bin/env python3
"""Assemble : intro logo FoodEatUp + demo complète, avec voix off placée par agent + BGM ducké."""
import os, subprocess, glob
os.chdir(os.path.dirname(os.path.abspath(__file__)))
BASE="/home/user/Video"; BGM=f"{BASE}/videos/stories-foodeatup-30j/audio/bgm.mp3"
FPS=30
def dur(f): return float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f]).strip())
def run(c,n):
    r=subprocess.run(c,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
    if r.returncode!=0: print("ERR",n,r.stderr.decode()[-800:]); raise SystemExit(1)
    print("ok",n)

INTRO=dur("work/intro.mp4")
# cumulative start time (within demo) of each part, in filename order
parts=sorted(glob.glob("work/seg/[0-9]*_*.mp4"))
starts=[]; acc=0.0
for p in parts: starts.append(acc); acc+=dur(p)
DEMO=acc
# command counts per agent -> first part index
counts=[5,1,2,5,5,8]  # GEN,HACCP,GF,RH,stock,prod
firstpart=[]; idx=0
for c in counts: firstpart.append(idx*2 if False else idx); idx+=c
# firstpart holds command-index of each agent's first cmd; convert to part index (=cmd_index*2)
agent_cmdidx=[0,5,6,8,13,18]
agent_parts=[i*2 for i in agent_cmdidx]
agent_start=[INTRO+starts[p] for p in agent_parts]   # +intro offset
VO=["intro","gen","haccp","gf","rh","stock","prod","outro"]
vd={v:dur(f"audio/vo_{v}.mp3") for v in VO}
TOT=INTRO+DEMO

# VO placement times (final timeline), staggered so no overlap
place={}
place["intro"]=0.4
t=[max(agent_start[i], (place["intro"]+vd["intro"]+0.4) if i==0 else 0) for i in range(6)]
names=["gen","haccp","gf","rh","stock","prod"]
prev_end=place["intro"]+vd["intro"]
for i,nm in enumerate(names):
    st=max(agent_start[i], prev_end+0.3)
    place[nm]=st; prev_end=st+vd[nm]
place["outro"]=max(TOT-vd["outro"]-0.6, prev_end+0.3)

# 1) video: concat intro + demo silent (re-encode once for uniform params)
open("work/vlist.txt","w").write(f"file '{os.path.abspath('work/intro.mp4')}'\nfile '{os.path.abspath('work/seg/silent.mp4')}'\n")
run(["ffmpeg","-y","-f","concat","-safe","0","-i","work/vlist.txt",
     "-c:v","libx264","-preset","veryfast","-crf","21","-pix_fmt","yuv420p","-r",str(FPS),"-an","work/full_video.mp4"],"video")

# 2) audio: VO clips delayed + mixed, over BGM bed
inputs=["-stream_loop","-1","-i",BGM]
for v in VO: inputs+=["-i",f"audio/vo_{v}.mp3"]
fc=f"[0:a]volume=0.11,afade=t=in:st=0:d=1.0,afade=t=out:st={TOT-1.6:.2f}:d=1.6[bg];"
labels=["[bg]"]
for i,v in enumerate(VO):
    ms=int(place[v]*1000)
    fc+=f"[{i+1}:a]adelay={ms}|{ms},volume=1.35[v{i}];"
    labels.append(f"[v{i}]")
fc+="".join(labels)+f"amix=inputs={len(labels)}:normalize=0:dropout_transition=0,atrim=0:{TOT:.2f},loudnorm=I=-15:TP=-1.5:LRA=11[a]"
run(["ffmpeg","-y"]+inputs+["-filter_complex",fc,"-map","[a]","-ac","2","-ar","44100","work/full_audio.m4a"],"audio")

os.makedirs("composition/renders",exist_ok=True)
run(["ffmpeg","-y","-i","work/full_video.mp4","-i","work/full_audio.m4a","-map","0:v","-map","1:a",
     "-c:v","copy","-c:a","aac","-b:a","192k","-shortest","-movflags","+faststart",
     "composition/renders/predibot-vo-logo.mp4"],"mux")
print("DONE",round(dur("composition/renders/predibot-vo-logo.mp4"),1),"s")
print("VO times:",{k:round(v,1) for k,v in place.items()})
print("agent starts:",[round(x,1) for x in agent_start])
