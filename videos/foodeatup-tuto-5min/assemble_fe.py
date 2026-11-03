#!/usr/bin/env python3
"""Assemble FoodEatUp 5-min tutorial: 27 segments (stills + 7 avatar phase bumpers)
-> per-clip render -> concat -> BGM + loudnorm."""
import os, subprocess, json
os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.makedirs("work", exist_ok=True)
FPS=30; HEAD=0.35; TAIL=0.6
PW,PH,PX,PY=440,560,580,600
MIKA="assets/avatar/mika.mp4"; MASK="assets/avatar/mask.png"

def dur(f):
    return float(subprocess.check_output(["ffprobe","-v","error","-show_entries",
        "format=duration","-of","csv=p=0",f]).strip())

# order: (name, kind, frame_png, vo, avatar_offset)
AV=[4,14,24,36,48,60,72]
SEQ=[
 ("intro","still","frames/intro.png","audio/s00.mp3",None),
 ("phase1","phase","frames/phase1.png","audio/s10.mp3",AV[0]),
 ("s11","still","frames/s11.png","audio/s11.mp3",None),
 ("s12","still","frames/s12.png","audio/s12.mp3",None),
 ("phase2","phase","frames/phase2.png","audio/s20.mp3",AV[1]),
 ("s21","still","frames/s21.png","audio/s21.mp3",None),
 ("s22","still","frames/s22.png","audio/s22.mp3",None),
 ("phase3","phase","frames/phase3.png","audio/s30.mp3",AV[2]),
 ("s31","still","frames/s31.png","audio/s31.mp3",None),
 ("phase4","phase","frames/phase4.png","audio/s40.mp3",AV[3]),
 ("s41","still","frames/s41.png","audio/s41.mp3",None),
 ("s42","still","frames/s42.png","audio/s42.mp3",None),
 ("s43","still","frames/s43.png","audio/s43.mp3",None),
 ("s44","still","frames/s44.png","audio/s44.mp3",None),
 ("s45","still","frames/s45.png","audio/s45.mp3",None),
 ("phase5","phase","frames/phase5.png","audio/s50.mp3",AV[4]),
 ("s51","still","frames/s51.png","audio/s51.mp3",None),
 ("s52","still","frames/s52.png","audio/s52.mp3",None),
 ("phase6","phase","frames/phase6.png","audio/s60.mp3",AV[5]),
 ("s61","still","frames/s61.png","audio/s61.mp3",None),
 ("s62","still","frames/s62.png","audio/s62.mp3",None),
 ("s63","still","frames/s63.png","audio/s63.mp3",None),
 ("phase7","phase","frames/phase7.png","audio/s70.mp3",AV[6]),
 ("s71","still","frames/s71.png","audio/s71.mp3",None),
 ("s72","still","frames/s72.png","audio/s72.mp3",None),
 ("s73","still","frames/s73.png","audio/s73.mp3",None),
 ("outro","still","frames/outro.png","audio/s99.mp3",None),
]

VENC=["-c:v","libx264","-preset","medium","-crf","20","-pix_fmt","yuv420p",
      "-r",str(FPS),"-c:a","aac","-b:a","192k","-ar","44100","-ac","2"]

listf=open("work/list.txt","w")
for name,kind,png,vo,off in SEQ:
    d=dur(vo)+HEAD+TAIL
    out=f"work/{name}.mp4"
    aud=(f"[{'3' if kind=='phase' else '1'}:a]adelay={int(HEAD*1000)}|{int(HEAD*1000)},"
         f"apad=whole_dur={d:.3f},aresample=44100,aformat=channel_layouts=stereo[a]")
    if kind=="still":
        fc=f"[0:v]scale=1080:1920,setsar=1,fade=t=in:d=0.25[v];{aud}"
        cmd=["ffmpeg","-y","-loop","1","-t",f"{d:.3f}","-i",png,"-i",vo,
             "-filter_complex",fc,"-map","[v]","-map","[a]","-t",f"{d:.3f}"]+VENC+[out]
    else:
        fc=(f"[0:v]scale=1080:1920,setsar=1[bg];"
            f"[1:v]crop=720:916:0:40,scale={PW}:{PH},setsar=1[avs];"
            f"[avs][2:v]alphamerge[ava];"
            f"[bg][ava]overlay={PX}:{PY}:format=auto,fade=t=in:d=0.25[v];{aud}")
        cmd=["ffmpeg","-y","-loop","1","-t",f"{d:.3f}","-i",png,
             "-ss",str(off),"-t",f"{d:.3f}","-i",MIKA,
             "-loop","1","-i",MASK,"-i",vo,
             "-filter_complex",fc,"-map","[v]","-map","[a]","-t",f"{d:.3f}"]+VENC+[out]
    r=subprocess.run(cmd,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
    if r.returncode!=0:
        print("ERR",name,r.stderr.decode()[-1500:]); raise SystemExit(1)
    listf.write(f"file '{name}.mp4'\n"); print("clip",name,round(d,2))
listf.close()

subprocess.run(["ffmpeg","-y","-f","concat","-safe","0","-i","work/list.txt",
    "-c","copy","work/master.mp4"],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
TOT=dur("work/master.mp4"); print("master",round(TOT,2))

fc=(f"[1:a]atrim=0:{TOT:.3f},asetpts=N/SR/TB,volume=0.06,"
    f"afade=t=in:st=0:d=1.5,afade=t=out:st={TOT-2:.3f}:d=2[bg];"
    f"[0:a][bg]amix=inputs=2:normalize=0:dropout_transition=0,"
    f"loudnorm=I=-14:TP=-1.5:LRA=11[a]")
subprocess.run(["ffmpeg","-y","-i","work/master.mp4","-stream_loop","-1","-i","audio/bgm.mp3",
    "-filter_complex",fc,"-map","0:v","-map","[a]","-c:v","copy","-c:a","aac","-b:a","192k",
    "deliverable/foodeatup-tuto-5min.mp4"],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
print("DONE -> deliverable/foodeatup-tuto-5min.mp4",round(dur("deliverable/foodeatup-tuto-5min.mp4"),1),"s")
