#!/usr/bin/env python3
"""Assemble V1 Lancement FoodEatUp 16:9 (1920x1080, LinkedIn ~60s). Plan 2 fondateur rallongé
(Mika live grand), même récit, ton posé. VO l1-l7."""
import os, subprocess, glob
os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.makedirs("work169",exist_ok=True); os.makedirs("renders",exist_ok=True)
BASE="/home/user/Video"; STO=f"{BASE}/videos/stories-foodeatup-30j"
MIKA=f"{STO}/assets/avatar/mika.mp4"; BGM=f"{STO}/audio/bgm.mp3"; CHIME=f"{BASE}/videos/serie-30-e01/assets/sfx/chime.mp3"
FPS=30; VENC=["-c:v","libx264","-preset","medium","-crf","20","-pix_fmt","yuv420p","-r",str(FPS),
    "-c:a","aac","-b:a","192k","-ar","44100","-ac","2"]
def dur(f): return float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f]).strip())
def run(cmd,name):
    r=subprocess.run(cmd,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
    if r.returncode!=0: print("ERR",name,r.stderr.decode()[-1400:]); raise SystemExit(1)
    print("ok",name,round(dur(cmd[-1]),2))
def voa(src,d,head=0.35):
    return (f"[{src}]adelay={int(head*1000)}|{int(head*1000)},apad=whole_dur={d:.3f},aresample=44100,aformat=channel_layouts=stereo[a]")
W,H=1920,1080
# P1
d=dur("audio/l1.mp3")+0.6
fc=(f"[0:v]scale={W*2}:{H*2},zoompan=z='min(zoom+0.0006,1.08)':d={int(d*FPS)}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s={W}x{H}:fps={FPS},setsar=1,fade=t=in:d=0.4[v];"+voa("1:a",d))
run(["ffmpeg","-y","-loop","1","-t",f"{d:.3f}","-i","frames169/p1.png","-i","audio/l1.mp3","-filter_complex",fc,"-map","[v]","-map","[a]","-t",f"{d:.3f}"]+VENC+["work169/p1.mp4"],"p1")
# P2 fondateur : Mika live grand (620) gauche
d=dur("audio/l2.mp3")+0.7; off=6
fc=(f"[0:v]scale={W}:{H},setsar=1[bg];[1:v]crop=560:560:80:40,scale=620:620,setsar=1[mk];[mk][2:v]alphamerge[mkc];"
    f"[bg][mkc]overlay=200:230:format=auto,fade=t=in:d=0.3[v];"+voa("3:a",d))
run(["ffmpeg","-y","-loop","1","-t",f"{d:.3f}","-i","frames169/p2.png","-ss",str(off),"-t",f"{d:.3f}","-i",MIKA,"-loop","1","-i","masks/circle620.png","-i","audio/l2.mp3","-filter_complex",fc,"-map","[v]","-map","[a]","-t",f"{d:.3f}"]+VENC+["work169/p2.mp4"],"p2")
# P3
d=dur("audio/l3.mp3")+0.6
fc=(f"[0:v]scale={W}:{H},setsar=1,fade=t=in:d=0.3[v];"+voa("1:a",d))
run(["ffmpeg","-y","-loop","1","-t",f"{d:.3f}","-i","frames169/p3.png","-i","audio/l3.mp3","-filter_complex",fc,"-map","[v]","-map","[a]","-t",f"{d:.3f}"]+VENC+["work169/p3.mp4"],"p3")
# P4 machine à écrire
ntype=len(glob.glob("frames169/p4type/*.png")); TF=6.5; dt=ntype/TF
run(["ffmpeg","-y","-framerate",str(TF),"-i","frames169/p4type/%03d.png","-vf",f"scale={W}:{H},setsar=1,fps={FPS}","-t",f"{dt:.3f}"]+VENC[:-8]+["-an","work169/p4a.mp4"],"p4a")
run(["ffmpeg","-y","-loop","1","-t","1.8","-i","frames169/p4check.png","-vf",f"scale={W}:{H},setsar=1,fps={FPS}"]+VENC[:-8]+["-an","-t","1.8","work169/p4b.mp4"],"p4b")
run(["ffmpeg","-y","-loop","1","-t","3.0","-i","frames169/p4cut.png","-vf",f"scale={W}:{H},setsar=1,fps={FPS}"]+VENC[:-8]+["-an","-t","3.0","work169/p4c.mp4"],"p4c")
open("work169/p4list.txt","w").write("file 'p4a.mp4'\nfile 'p4b.mp4'\nfile 'p4c.mp4'\n")
run(["ffmpeg","-y","-f","concat","-safe","0","-i","work169/p4list.txt","-c","copy","work169/p4v.mp4"],"p4v")
d=dur("work169/p4v.mp4")
fc=(f"[1:a]adelay=300|300,apad=whole_dur={d:.3f}[vo];[2:a]adelay={int(dt*1000)}|{int(dt*1000)},volume=0.6[dg];"
    f"[vo][dg]amix=inputs=2:normalize=0:dropout_transition=0,apad=whole_dur={d:.3f},aformat=channel_layouts=stereo[a]")
run(["ffmpeg","-y","-i","work169/p4v.mp4","-i","audio/l4.mp3","-i",CHIME,"-filter_complex",fc,"-map","0:v","-map","[a]","-t",f"{d:.3f}"]+VENC+["work169/p4.mp4"],"p4")
# P5 carrousel 4 (1.75s chacun)
for i in range(4):
    zin="min(zoom+0.0006,1.05)" if i%2==0 else "if(eq(on,0),1.05,max(zoom-0.0006,1.0))"
    run(["ffmpeg","-y","-loop","1","-t","1.75","-i",f"frames169/p5_{i}.png","-vf",
         f"scale={W*2}:{H*2},zoompan=z='{zin}':d={int(1.75*FPS)}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s={W}x{H}:fps={FPS},setsar=1"]+VENC[:-8]+["-an","-t","1.75",f"work169/p5_{i}.mp4"],f"p5_{i}")
open("work169/p5list.txt","w").write("".join(f"file 'p5_{i}.mp4'\n" for i in range(4)))
run(["ffmpeg","-y","-f","concat","-safe","0","-i","work169/p5list.txt","-c","copy","work169/p5v.mp4"],"p5v")
d=dur("work169/p5v.mp4"); fc=voa("1:a",d,0.15)
run(["ffmpeg","-y","-i","work169/p5v.mp4","-i","audio/l5.mp3","-filter_complex",fc,"-map","0:v","-map","[a]","-t",f"{d:.3f}"]+VENC+["work169/p5.mp4"],"p5")
# P6 offre pulse
d=dur("audio/l6.mp3")+0.7
fc=(f"[0:v]scale={W*2}:{H*2},zoompan=z='1.04+0.02*sin(on/5)':d={int(d*FPS)}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s={W}x{H}:fps={FPS},setsar=1,fade=t=in:d=0.3[v];"+voa("1:a",d))
run(["ffmpeg","-y","-loop","1","-t",f"{d:.3f}","-i","frames169/p6.png","-i","audio/l6.mp3","-filter_complex",fc,"-map","[v]","-map","[a]","-t",f"{d:.3f}"]+VENC+["work169/p6.mp4"],"p6")
# P7 sérénité + Mika 360
d=dur("audio/l7.mp3")+1.0; off=20
fc=(f"[0:v]scale={W}:{H},setsar=1[bg];[1:v]crop=480:480:120:80,scale=360:360,setsar=1[mk];[mk][2:v]alphamerge[mkc];"
    f"[bg][mkc]overlay=300:360:format=auto,fade=t=in:d=0.3[v];"+voa("3:a",d))
run(["ffmpeg","-y","-loop","1","-t",f"{d:.3f}","-i","frames169/p7.png","-ss",str(off),"-t",f"{d:.3f}","-i",MIKA,"-loop","1","-i","masks/circle360.png","-i","audio/l7.mp3","-filter_complex",fc,"-map","[v]","-map","[a]","-t",f"{d:.3f}"]+VENC+["work169/p7.mp4"],"p7")
# concat + BGM (montée offre)
plans=["p1","p2","p3","p4","p5","p6","p7"]
open("work169/all.txt","w").write("".join(f"file '{p}.mp4'\n" for p in plans))
run(["ffmpeg","-y","-f","concat","-safe","0","-i","work169/all.txt","-c","copy","work169/master.mp4"],"master")
TOT=dur("work169/master.mp4"); acc=0; os6=0
for p in plans:
    if p=="p6": os6=acc
    acc+=dur(f"work169/{p}.mp4")
oe6=os6+dur("work169/p6.mp4")
fc=(f"[1:a]atrim=0:{TOT:.3f},asetpts=N/SR/TB,volume='if(between(t,{os6:.2f},{oe6:.2f}),0.10,0.045)':eval=frame,"
    f"afade=t=in:st=0:d=1.0,afade=t=out:st={TOT-1.6:.3f}:d=1.6[bg];[0:a][bg]amix=inputs=2:normalize=0:dropout_transition=0,loudnorm=I=-14:TP=-1.5:LRA=11[a]")
run(["ffmpeg","-y","-i","work169/master.mp4","-stream_loop","-1","-i",BGM,"-filter_complex",fc,"-map","0:v","-map","[a]","-c:v","copy","-c:a","aac","-b:a","192k","-movflags","+faststart","renders/lancement-foodeatup-v1-16x9.mp4"],"FINAL")
print("DONE",round(dur("renders/lancement-foodeatup-v1-16x9.mp4"),1),"s")
