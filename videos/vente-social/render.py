#!/usr/bin/env python3
"""Reusable renderer for Studio Vente Social clips.
Usage: python3 render.py <frame.png> <vo.mp3> <out.mp4> [med]
  med  -> overlay a live circular Mika medallion at 80,300 d230 (T1 layout)
  (absent) -> static frame with subtle Ken Burns push-in (T2/T3)
9:16 or 1:1 auto (frame size drives canvas)."""
import os, subprocess, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
FPS=30; HEAD=0.8; TAIL=1.4
STO="/home/user/Video/videos/stories-foodeatup-30j"
MIKA=f"{STO}/assets/avatar/mika.mp4"; MASK=f"{STO}/assets/avatar/circle-mask.png"; BGM=f"{STO}/audio/bgm.mp3"
def dur(f): return float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f]).strip())
def size(f):
    o=subprocess.check_output(["ffprobe","-v","error","-select_streams","v","-show_entries","stream=width,height","-of","csv=p=0:s=x",f]).decode().strip()
    w,h=o.split("x"); return int(w),int(h)

frame,vo,out=sys.argv[1],sys.argv[2],sys.argv[3]
med = "med" in sys.argv[4:]
W,H=size(frame); d=dur(vo)+HEAD+TAIL; DF=int(round(d*FPS)); OFF=6
audio=(f"[3:a]adelay={int(HEAD*1000)}|{int(HEAD*1000)},apad=whole_dur={d:.3f},aresample=44100,aformat=channel_layouts=stereo[vo];"
       f"[4:a]atrim=0:{d:.3f},asetpts=N/SR/TB,volume=0.06,afade=t=in:st=0:d=1.0,afade=t=out:st={d-1.4:.3f}:d=1.4[bg2];"
       f"[vo][bg2]amix=inputs=2:normalize=0:dropout_transition=0,loudnorm=I=-14:TP=-1.5:LRA=11[a]")
if med:
    fc=(f"[0:v]scale={W}:{H},setsar=1[bg];[1:v]crop=480:480:120:80,scale=230:230,setsar=1[mk];"
        f"[mk][2:v]alphamerge[mkc];[bg][mkc]overlay=80:300:format=auto,fade=t=in:d=0.3,fade=t=out:st={d-0.6:.3f}:d=0.6[v];"
        + audio)
    cmd=["ffmpeg","-y","-loop","1","-t",f"{d:.3f}","-i",frame,"-ss",str(OFF),"-t",f"{d:.3f}","-i",MIKA,
         "-loop","1","-i",MASK,"-i",vo,"-stream_loop","-1","-i",BGM]
else:
    fc=(f"[0:v]scale={W*2}:{H*2},zoompan=z='min(zoom+0.0004,1.06)':d={DF}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s={W}x{H}:fps={FPS},"
        f"fade=t=in:d=0.3,fade=t=out:st={d-0.6:.3f}:d=0.6,setsar=1[v];"
        + audio.replace("[3:a]","[1:a]").replace("[4:a]","[2:a]"))
    cmd=["ffmpeg","-y","-i",frame,"-i",vo,"-stream_loop","-1","-i",BGM]
    # remap: 0=frame,1=vo,2=bgm  → adjust audio labels already done above
cmd+=["-filter_complex",fc,"-map","[v]","-map","[a]","-t",f"{d:.3f}",
      "-c:v","libx264","-preset","medium","-crf","20","-pix_fmt","yuv420p","-r",str(FPS),
      "-c:a","aac","-b:a","192k","-ar","44100","-ac","2",out]
r=subprocess.run(cmd,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
if r.returncode!=0: print("ERR",r.stderr.decode()[-1500:]); raise SystemExit(1)
print("DONE",out,round(dur(out),1),"s")
