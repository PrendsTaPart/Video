#!/usr/bin/env python3
"""Assemble V1 FINAL FoodEatUp 9:16 — charte officielle + logo sting (plans 2 & 10)."""
import os, subprocess, glob
os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.makedirs("wfin",exist_ok=True); os.makedirs("renders",exist_ok=True)
BASE="/home/user/Video"; STO=f"{BASE}/videos/stories-foodeatup-30j"
MIKA=f"{STO}/assets/avatar/mika.mp4"; BGM=f"{STO}/audio/bgm.mp3"; CHIME=f"{BASE}/videos/serie-30-e01/assets/sfx/chime.mp3"
STING=f"composition/logo-sting"
FPS=30; VENC=["-c:v","libx264","-preset","medium","-crf","20","-pix_fmt","yuv420p","-r",str(FPS),"-c:a","aac","-b:a","192k","-ar","44100","-ac","2"]
def dur(f): return float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f]).strip())
def run(cmd,name):
    r=subprocess.run(cmd,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
    if r.returncode!=0: print("ERR",name,r.stderr.decode()[-1400:]); raise SystemExit(1)
    print("ok",name,round(dur(cmd[-1]),2))
def voa(idx,d,head=0.3):
    return (f"[{idx}:a]adelay={int(head*1000)}|{int(head*1000)},apad=whole_dur={d:.3f},aresample=44100,aformat=channel_layouts=stereo[a]")

def img_plan(png,vo,out,zoom=False,shake=False):
    d=dur(vo)+0.8; DF=int(d*FPS)
    if zoom:
        z="min(zoom+0.0007,1.09)"; xexpr="iw/2-(iw/zoom/2)"+("+8*sin(on/3)" if shake else ""); yexpr="ih/2-(ih/zoom/2)"
        v=f"[0:v]scale=2160:3840,zoompan=z='{z}':d={DF}:x='{xexpr}':y='{yexpr}':s={W}x{H}:fps={FPS},setsar=1,fade=t=in:d=0.3[v];"
    else:
        v=f"[0:v]scale={W}:{H},setsar=1,fade=t=in:d=0.3[v];"
    run(["ffmpeg","-y","-loop","1","-t",f"{d:.3f}","-i",png,"-i",vo,"-filter_complex",v+voa(1,d),"-map","[v]","-map","[a]","-t",f"{d:.3f}"]+VENC+[out],os.path.basename(out))

def med_plan(png,vo,out,diam,ox,oy,off):
    d=dur(vo)+(1.0 if diam<400 else 0.7)
    fc=(f"[0:v]scale={W}:{H},setsar=1[bg];[1:v]crop={480 if diam<400 else 560}:{480 if diam<400 else 560}:{120 if diam<400 else 80}:{80 if diam<400 else 40},scale={diam}:{diam},setsar=1[mk];"
        f"[mk][2:v]alphamerge[mkc];[bg][mkc]overlay={ox}:{oy}:format=auto,fade=t=in:d=0.3[v];"+voa(3,d))
    run(["ffmpeg","-y","-loop","1","-t",f"{d:.3f}","-i",png,"-ss",str(off),"-t",f"{d:.3f}","-i",MIKA,"-loop","1","-i",f"masks/circle{diam}.png","-i",vo,"-filter_complex",fc,"-map","[v]","-map","[a]","-t",f"{d:.3f}"]+VENC+[out],os.path.basename(out))

W,H=1080,1920
# normalise stings
for s,o in [("sting-in","sting_in"),("sting-out","sting_out")]:
    run(["ffmpeg","-y","-i",f"{STING}/{s}.mp4","-filter_complex",f"[0:v]scale={W}:{H},setsar=1,fps={FPS}[v];[0:a]aresample=44100,aformat=channel_layouts=stereo[a]","-map","[v]","-map","[a]"]+VENC+[f"wfin/{o}.mp4"],o)
# P1
img_plan("ffin/p1.png","audio/f1.mp3","wfin/p1.mp4",zoom=True,shake=True)
# P3 Mika buste
med_plan("ffin/p3.png","audio/f3.mp3","wfin/p3.mp4",560,260,470,8)
# P4 split
img_plan("ffin/p4.png","audio/f4.mp3","wfin/p4.mp4")
# P5 chat typewriter
nt=len(glob.glob("ffin/p5type/*.png")); TF=6.5; dt=nt/TF
run(["ffmpeg","-y","-framerate",str(TF),"-i","ffin/p5type/%03d.png","-vf",f"scale={W}:{H},setsar=1,fps={FPS}","-t",f"{dt:.3f}"]+VENC[:-8]+["-an","wfin/p5a.mp4"],"p5a")
run(["ffmpeg","-y","-loop","1","-t","1.4","-i","ffin/p5check.png","-vf",f"scale={W}:{H},setsar=1,fps={FPS}"]+VENC[:-8]+["-an","wfin/p5b.mp4"],"p5b")
open("wfin/p5l.txt","w").write("file 'p5a.mp4'\nfile 'p5b.mp4'\n"); run(["ffmpeg","-y","-f","concat","-safe","0","-i","wfin/p5l.txt","-c","copy","wfin/p5v.mp4"],"p5v")
d5=dur("wfin/p5v.mp4")
fc=(f"[1:a]adelay=300|300,apad=whole_dur={d5:.3f}[vo];[2:a]adelay={int(dt*1000)}|{int(dt*1000)},volume=0.6[ding];[vo][ding]amix=inputs=2:normalize=0,apad=whole_dur={d5:.3f},aformat=channel_layouts=stereo[a]")
run(["ffmpeg","-y","-i","wfin/p5v.mp4","-i","audio/f5.mp3","-i",CHIME,"-filter_complex",fc,"-map","0:v","-map","[a]","-t",f"{d5:.3f}"]+VENC+["wfin/p5.mp4"],"p5")
# P6 produit
img_plan("ffin/p6.png","audio/f6.mp3","wfin/p6.mp4",zoom=True)
# P7 carrousel
for i in range(4):
    z="min(zoom+0.0008,1.06)" if i%2==0 else "if(eq(on,0),1.06,max(zoom-0.0008,1.0))"
    run(["ffmpeg","-y","-loop","1","-t","1.1","-i",f"ffin/p7_{i}.png","-vf",f"scale=2160:3840,zoompan=z='{z}':d={int(1.1*FPS)}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s={W}x{H}:fps={FPS},setsar=1"]+VENC[:-8]+["-an","-frames:v",str(int(1.1*FPS)),f"wfin/p7_{i}.mp4"],f"p7_{i}")
open("wfin/p7l.txt","w").write("".join(f"file 'p7_{i}.mp4'\n" for i in range(4))); run(["ffmpeg","-y","-f","concat","-safe","0","-i","wfin/p7l.txt","-c","copy","wfin/p7v.mp4"],"p7v")
d7=dur("wfin/p7v.mp4")
run(["ffmpeg","-y","-i","wfin/p7v.mp4","-i","audio/f7.mp3","-filter_complex",voa(1,d7,0.15),"-map","0:v","-map","[a]","-t",f"{d7:.3f}"]+VENC+["wfin/p7.mp4"],"p7")
# P8 offre pulse
d8=dur("audio/f8.mp3")+0.8; DF8=int(d8*FPS)
fc=(f"[0:v]scale=2160:3840,zoompan=z='1.04+0.025*sin(on/5)':d={DF8}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s={W}x{H}:fps={FPS},setsar=1,fade=t=in:d=0.3[v];"+voa(1,d8))
run(["ffmpeg","-y","-loop","1","-t",f"{d8:.3f}","-i","ffin/p8.png","-i","audio/f8.mp3","-filter_complex",fc,"-map","[v]","-map","[a]","-t",f"{d8:.3f}"]+VENC+["wfin/p8.mp4"],"p8")
# P9 hook de fin Mika
med_plan("ffin/p9.png","audio/f9.mp3","wfin/p9.mp4",300,80,360,20)

# concat
order=["p1","sting_in","p3","p4","p5","p6","p7","p8","p9","sting_out"]
open("wfin/all.txt","w").write("".join(f"file '{p}.mp4'\n" for p in order))
run(["ffmpeg","-y","-f","concat","-safe","0","-i","wfin/all.txt","-c","copy","wfin/master.mp4"],"master")
TOT=dur("wfin/master.mp4"); acc=0; o8=0
for p in order:
    if p=="p8": o8=acc
    acc+=dur(f"wfin/{p}.mp4")
o8e=o8+dur("wfin/p8.mp4")
fc=(f"[1:a]atrim=0:{TOT:.3f},asetpts=N/SR/TB,volume='if(between(t,{o8:.2f},{o8e:.2f}),0.10,0.045)':eval=frame,afade=t=in:st=0:d=1.0,afade=t=out:st={TOT-1.6:.3f}:d=1.6[bg];[0:a][bg]amix=inputs=2:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[a]")
run(["ffmpeg","-y","-i","wfin/master.mp4","-stream_loop","-1","-i",BGM,"-filter_complex",fc,"-map","0:v","-map","[a]","-c:v","copy","-c:a","aac","-b:a","192k","-movflags","+faststart","renders/lancement-foodeatup-v1-FINAL-9x16.mp4"],"FINAL")
print("DONE",round(dur("renders/lancement-foodeatup-v1-FINAL-9x16.mp4"),1),"s")
