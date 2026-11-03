#!/usr/bin/env python3
"""Render one story MP4 (9:16, ~10-15s): branded frame + live circular Mika medallion + VO + BGM."""
import os, subprocess, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.makedirs("renders",exist_ok=True)
FPS=30; HEAD=0.8; TAIL=1.2
MIKA="assets/avatar/mika.mp4"; MASK="assets/avatar/circle-mask.png"
OFF={"S01":4,"S02":10,"S03":16,"S04":22,"S05":28,"S06":34,"S07":40,"S08":46,"S09":52,"S10":58}
def dur(f): return float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f]).strip())

def build(sid):
    png=f"frames/{sid}.png"; vo=f"audio/{sid}.mp3"; d=dur(vo)+HEAD+TAIL; off=OFF.get(sid,4)
    out=f"renders/{sid}.mp4"
    fc=(f"[0:v]scale=1080:1920,setsar=1[bg];"
        f"[1:v]crop=480:480:120:80,scale=230:230,setsar=1[mk];"
        f"[mk][2:v]alphamerge[mkc];"
        f"[bg][mkc]overlay=80:310:format=auto,fade=t=in:d=0.3[v];"
        f"[3:a]adelay={int(HEAD*1000)}|{int(HEAD*1000)},apad=whole_dur={d:.3f},aresample=44100,aformat=channel_layouts=stereo[vo];"
        f"[4:a]atrim=0:{d:.3f},asetpts=N/SR/TB,volume=0.07,afade=t=out:st={d-1.2:.3f}:d=1.2[bg2];"
        f"[vo][bg2]amix=inputs=2:normalize=0:dropout_transition=0,loudnorm=I=-14:TP=-1.5:LRA=11[a]")
    cmd=["ffmpeg","-y","-loop","1","-t",f"{d:.3f}","-i",png,
         "-ss",str(off),"-t",f"{d:.3f}","-i",MIKA,"-loop","1","-i",MASK,
         "-i",vo,"-stream_loop","-1","-i","audio/bgm.mp3",
         "-filter_complex",fc,"-map","[v]","-map","[a]","-t",f"{d:.3f}",
         "-c:v","libx264","-preset","medium","-crf","20","-pix_fmt","yuv420p","-r",str(FPS),
         "-c:a","aac","-b:a","192k","-ar","44100","-ac","2",out]
    r=subprocess.run(cmd,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
    if r.returncode!=0: print("ERR",sid,r.stderr.decode()[-1200:]); return
    print("rendered",sid,round(d,1),"s")

for sid in (sys.argv[1:] or ["S01","S02","S03","S04","S05"]): build(sid)
