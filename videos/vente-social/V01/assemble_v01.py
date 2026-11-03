#!/usr/bin/env python3
"""V01 — FoodEatUp · Problème→Solution (9:16). Static T1 frame + live circular Mika
medallion (top-left) + VO (Adam) + BGM. Same proven pipeline as assemble_story.py."""
import os, subprocess
os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.makedirs("renders", exist_ok=True)
FPS=30; HEAD=0.8; TAIL=1.4
STO="/home/user/Video/videos/stories-foodeatup-30j"
MIKA=f"{STO}/assets/avatar/mika.mp4"; MASK=f"{STO}/assets/avatar/circle-mask.png"; BGM=f"{STO}/audio/bgm.mp3"
PNG="frames/v01.png"; VO="audio/vo.mp3"; OUT="renders/v01-foodeatup-9x16.mp4"
OFF=6  # start offset into mika.mp4 for a lively segment
def dur(f): return float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f]).strip())
d=dur(VO)+HEAD+TAIL
fc=(f"[0:v]scale=1080:1920,setsar=1[bg];"
    f"[1:v]crop=480:480:120:80,scale=230:230,setsar=1[mk];"
    f"[mk][2:v]alphamerge[mkc];"
    f"[bg][mkc]overlay=80:300:format=auto,fade=t=in:d=0.3,fade=t=out:st={d-0.6:.3f}:d=0.6[v];"
    f"[3:a]adelay={int(HEAD*1000)}|{int(HEAD*1000)},apad=whole_dur={d:.3f},aresample=44100,aformat=channel_layouts=stereo[vo];"
    f"[4:a]atrim=0:{d:.3f},asetpts=N/SR/TB,volume=0.06,afade=t=in:st=0:d=1.0,afade=t=out:st={d-1.4:.3f}:d=1.4[bg2];"
    f"[vo][bg2]amix=inputs=2:normalize=0:dropout_transition=0,loudnorm=I=-14:TP=-1.5:LRA=11[a]")
cmd=["ffmpeg","-y","-loop","1","-t",f"{d:.3f}","-i",PNG,
     "-ss",str(OFF),"-t",f"{d:.3f}","-i",MIKA,"-loop","1","-i",MASK,
     "-i",VO,"-stream_loop","-1","-i",BGM,
     "-filter_complex",fc,"-map","[v]","-map","[a]","-t",f"{d:.3f}",
     "-c:v","libx264","-preset","medium","-crf","20","-pix_fmt","yuv420p","-r",str(FPS),
     "-c:a","aac","-b:a","192k","-ar","44100","-ac","2",OUT]
r=subprocess.run(cmd,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
if r.returncode!=0: print("ERR",r.stderr.decode()[-1500:]); raise SystemExit(1)
print("DONE",OUT,round(dur(OUT),1),"s")
