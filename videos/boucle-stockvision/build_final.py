#!/usr/bin/env python3
"""Assemble: frames -> body, + VO (placée) + BGM léger, mux final."""
import os, subprocess
os.chdir(os.path.dirname(os.path.abspath(__file__)))
BGM="/home/user/Video/videos/stories-foodeatup-30j/audio/bgm.mp3"
WK="work"; OUT="output"; os.makedirs(OUT,exist_ok=True)
def dur(f): return float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f]).strip())
def run(c,n):
    r=subprocess.run(c,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
    if r.returncode: print("ERR",n,r.stderr.decode()[-1400:]); raise SystemExit(1)
    print("ok",n)

# 1) frames -> body (subtitles already burned in)
run(["ffmpeg","-y","-framerate","30","-i",f"{WK}/frames/f%04d.png",
     "-c:v","libx264","-preset","slow","-crf","20","-pix_fmt","yuv420p","-r","30",f"{WK}/body.mp4"],"body")
T=dur(f"{WK}/body.mp4")

# 2) audio : VO placée + BGM -24dB
VO=[("b1",0.4),("b2",9.8),("b3",20.0),("b4",30.0),("b5",42.0),("b6",52.0)]
inp=[]
for vid,off in VO: inp+=["-i",f"{WK}/vo/{vid}.mp3"]
inp+=["-stream_loop","-1","-i",BGM]
fc=""
for i,(vid,off) in enumerate(VO):
    ms=int(off*1000); fc+=f"[{i}:a]adelay={ms}|{ms}[a{i}];"
fc+="".join(f"[a{i}]" for i in range(len(VO)))+f"amix=inputs={len(VO)}:normalize=0[vox];"
fc+=f"[{len(VO)}:a]volume=0.06,afade=t=in:st=0:d=1.5,afade=t=out:st={T-2.5:.2f}:d=2.5[bg];"
fc+=f"[vox][bg]amix=inputs=2:normalize=0,loudnorm=I=-16:TP=-1.5:LRA=11[a]"
run(["ffmpeg","-y"]+inp+["-filter_complex",fc,"-map","[a]","-t",f"{T:.2f}","-c:a","aac","-b:a","192k",f"{WK}/audio.m4a"],"audio")

# 3) mux + poster
run(["ffmpeg","-y","-i",f"{WK}/body.mp4","-i",f"{WK}/audio.m4a","-map","0:v","-map","1:a",
     "-c:v","copy","-c:a","aac","-b:a","192k","-movflags","+faststart","-shortest",f"{OUT}/boucle-stockvision.mp4"],"mux")
run(["ffmpeg","-y","-i",f"{OUT}/boucle-stockvision.mp4","-ss","4","-frames:v","1","-q:v","2",f"{OUT}/boucle-stockvision-poster.jpg"],"poster")
print("DONE",round(dur(f"{OUT}/boucle-stockvision.mp4"),1),"s")
