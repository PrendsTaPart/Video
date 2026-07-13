#!/usr/bin/env python3
"""Assemble V1 Lancement FoodEatUp 9:16 (1080x1920). Ken Burns, machine à écrire (plan4),
médaillon Mika live (plans 2 & 7), ding sur la coche, BGM avec montée sur le bloc offre."""
import os, subprocess
os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.makedirs("work",exist_ok=True); os.makedirs("renders",exist_ok=True)
BASE="/home/user/Video"; STO=f"{BASE}/videos/stories-foodeatup-30j"
MIKA=f"{STO}/assets/avatar/mika.mp4"; BGM=f"{STO}/audio/bgm.mp3"
CHIME=f"{BASE}/videos/serie-30-e01/assets/sfx/chime.mp3"
FPS=30; VENC=["-c:v","libx264","-preset","medium","-crf","20","-pix_fmt","yuv420p","-r",str(FPS),
    "-c:a","aac","-b:a","192k","-ar","44100","-ac","2"]
def dur(f): return float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f]).strip())
def run(cmd,name):
    r=subprocess.run(cmd,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
    if r.returncode!=0: print("ERR",name,r.stderr.decode()[-1400:]); raise SystemExit(1)
    print("ok",name,round(dur(cmd[-1]),2))

def voa(vo,d,head=0.35):
    return (f"[__A__]adelay={int(head*1000)}|{int(head*1000)},apad=whole_dur={d:.3f},"
            f"aresample=44100,aformat=channel_layouts=stereo[a]")

# ---- Plan 1 : image #1, zoom lent
d=dur("audio/p1.mp3")+0.6
fc=(f"[0:v]scale=2160:3840,zoompan=z='min(zoom+0.0006,1.08)':d={int(d*FPS)}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x1920:fps={FPS},setsar=1,fade=t=in:d=0.4[v];"
    +voa("audio/p1.mp3",d).replace("[__A__]","[1:a]"))
run(["ffmpeg","-y","-loop","1","-t",f"{d:.3f}","-i","frames/p1.png","-i","audio/p1.mp3","-filter_complex",fc,"-map","[v]","-map","[a]","-t",f"{d:.3f}"]+VENC+["work/p1.mp4"],"p1")

# ---- Plan 2 : Mika buste live (cercle 560) + carton, cut franc
d=dur("audio/p2.mp3")+0.7; off=8
fc=(f"[0:v]scale=1080:1920,setsar=1[bg];[1:v]crop=560:560:80:40,scale=560:560,setsar=1[mk];"
    f"[mk][2:v]alphamerge[mkc];[bg][mkc]overlay=260:470:format=auto[v];"
    +voa("audio/p2.mp3",d).replace("[__A__]","[3:a]"))
run(["ffmpeg","-y","-loop","1","-t",f"{d:.3f}","-i","frames/p2.png","-ss",str(off),"-t",f"{d:.3f}","-i",MIKA,
     "-loop","1","-i","masks/circle560.png","-i","audio/p2.mp3","-filter_complex",fc,"-map","[v]","-map","[a]","-t",f"{d:.3f}"]+VENC+["work/p2.mp4"],"p2")

# ---- Plan 3 : split, slide-in
d=dur("audio/p3.mp3")+0.7
fc=(f"[0:v]scale=1080:1920,setsar=1,fade=t=in:d=0.3[v];"+voa("audio/p3.mp3",d).replace("[__A__]","[1:a]"))
run(["ffmpeg","-y","-loop","1","-t",f"{d:.3f}","-i","frames/p3.png","-i","audio/p3.mp3","-filter_complex",fc,"-map","[v]","-map","[a]","-t",f"{d:.3f}"]+VENC+["work/p3.mp4"],"p3")

# ---- Plan 4 : machine à écrire → coche → cut produit
import glob
ntype=len(glob.glob("frames/p4type/*.png")); TYPE_FPS=6.5; d_type=ntype/TYPE_FPS
run(["ffmpeg","-y","-framerate",str(TYPE_FPS),"-i","frames/p4type/%03d.png","-vf",f"scale=1080:1920,setsar=1,fps={FPS}","-t",f"{d_type:.3f}"]+VENC[:-8]+["-an","work/p4a.mp4"],"p4a")
run(["ffmpeg","-y","-loop","1","-t","1.6","-i","frames/p4check.png","-vf",f"scale=1080:1920,setsar=1,fps={FPS}"]+VENC[:-8]+["-an","work/p4b.mp4"],"p4b")
run(["ffmpeg","-y","-loop","1","-t","2.9","-i","frames/p4cut.png","-vf",f"scale=1080:1920,setsar=1,fps={FPS}"]+VENC[:-8]+["-an","work/p4c.mp4"],"p4c")
open("work/p4list.txt","w").write("file 'p4a.mp4'\nfile 'p4b.mp4'\nfile 'p4c.mp4'\n")
run(["ffmpeg","-y","-f","concat","-safe","0","-i","work/p4list.txt","-c","copy","work/p4v.mp4"],"p4v")
d=dur("work/p4v.mp4")
# audio : VO + ding à l'apparition de la coche (t=d_type)
fc=(f"[1:a]adelay=300|300,apad=whole_dur={d:.3f}[vo];"
    f"[2:a]adelay={int(d_type*1000)}|{int(d_type*1000)},volume=0.6[ding];"
    f"[vo][ding]amix=inputs=2:normalize=0:dropout_transition=0,apad=whole_dur={d:.3f},aformat=channel_layouts=stereo[a]")
run(["ffmpeg","-y","-i","work/p4v.mp4","-i","audio/p4.mp3","-i",CHIME,"-filter_complex",fc,"-map","0:v","-map","[a]","-t",f"{d:.3f}"]+VENC+["work/p4.mp4"],"p4")

# ---- Plan 5 : carrousel 4 cartes
for i in range(4):
    zin="min(zoom+0.0008,1.06)" if i%2==0 else "if(eq(on,0),1.06,max(zoom-0.0008,1.0))"
    run(["ffmpeg","-y","-loop","1","-t","1.25","-i",f"frames/p5_{i}.png","-vf",
         f"scale=2160:3840,zoompan=z='{zin}':d={int(1.25*FPS)}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x1920:fps={FPS},setsar=1"]+VENC[:-8]+["-an",f"work/p5_{i}.mp4"],f"p5_{i}")
open("work/p5list.txt","w").write("".join(f"file 'p5_{i}.mp4'\n" for i in range(4)))
run(["ffmpeg","-y","-f","concat","-safe","0","-i","work/p5list.txt","-c","copy","work/p5v.mp4"],"p5v")
d=dur("work/p5v.mp4")
fc=voa("audio/p5.mp3",d,0.15).replace("[__A__]","[1:a]")
run(["ffmpeg","-y","-i","work/p5v.mp4","-i","audio/p5.mp3","-filter_complex",fc,"-map","0:v","-map","[a]","-t",f"{d:.3f}"]+VENC+["work/p5.mp4"],"p5")

# ---- Plan 6 : bloc offre, pulsation (zoom sinusoïdal « breathing »)
d=dur("audio/p6.mp3")+0.7; DF6=int(d*FPS)
fc=(f"[0:v]scale=2160:3840,zoompan=z='1.04+0.025*sin(on/5)':d={DF6}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x1920:fps={FPS},setsar=1,fade=t=in:d=0.3[v];"
    +voa("audio/p6.mp3",d).replace("[__A__]","[1:a]"))
run(["ffmpeg","-y","-loop","1","-t",f"{d:.3f}","-i","frames/p6.png",
     "-i","audio/p6.mp3","-filter_complex",fc,"-map","[v]","-map","[a]","-t",f"{d:.3f}"]+VENC+["work/p6.mp4"],"p6")

# ---- Plan 7 : sérénité + Mika (300) + CTA
d=dur("audio/p7.mp3")+1.0; off=20
fc=(f"[0:v]scale=1080:1920,setsar=1[bg];[1:v]crop=480:480:120:80,scale=300:300,setsar=1[mk];"
    f"[mk][2:v]alphamerge[mkc];[bg][mkc]overlay=80:360:format=auto,fade=t=in:d=0.3[v];"
    +voa("audio/p7.mp3",d).replace("[__A__]","[3:a]"))
run(["ffmpeg","-y","-loop","1","-t",f"{d:.3f}","-i","frames/p7.png","-ss",str(off),"-t",f"{d:.3f}","-i",MIKA,
     "-loop","1","-i","masks/circle300.png","-i","audio/p7.mp3","-filter_complex",fc,"-map","[v]","-map","[a]","-t",f"{d:.3f}"]+VENC+["work/p7.mp4"],"p7")

# ---- concat + BGM (montée sur l'offre)
plans=["p1","p2","p3","p4","p5","p6","p7"]
open("work/all.txt","w").write("".join(f"file '{p}.mp4'\n" for p in plans))
run(["ffmpeg","-y","-f","concat","-safe","0","-i","work/all.txt","-c","copy","work/master.mp4"],"master")
TOT=dur("work/master.mp4")
# fenêtre offre = somme des durées jusqu'à p6
acc=0; off_start=0
for p in plans:
    if p=="p6": off_start=acc
    acc+=dur(f"work/{p}.mp4")
off_end=off_start+dur("work/p6.mp4")
fc=(f"[1:a]atrim=0:{TOT:.3f},asetpts=N/SR/TB,"
    f"volume='if(between(t,{off_start:.2f},{off_end:.2f}),0.10,0.045)':eval=frame,"
    f"afade=t=in:st=0:d=1.0,afade=t=out:st={TOT-1.6:.3f}:d=1.6[bg];"
    f"[0:a][bg]amix=inputs=2:normalize=0:dropout_transition=0,loudnorm=I=-14:TP=-1.5:LRA=11[a]")
run(["ffmpeg","-y","-i","work/master.mp4","-stream_loop","-1","-i",BGM,"-filter_complex",fc,
     "-map","0:v","-map","[a]","-c:v","copy","-c:a","aac","-b:a","192k","-movflags","+faststart",
     "renders/lancement-foodeatup-v1-9x16.mp4"],"FINAL")
print("DONE",round(dur("renders/lancement-foodeatup-v1-9x16.mp4"),1),"s")
