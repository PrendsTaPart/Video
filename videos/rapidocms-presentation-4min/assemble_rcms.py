#!/usr/bin/env python3
"""Assemble RapidoCMS 4min 16:9. Ken Burns on stills, Mika medallion on 'intro', concat + BGM."""
import os, subprocess
os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.makedirs("work",exist_ok=True); os.makedirs("deliverable",exist_ok=True)
FPS=30; HEAD=0.35; TAIL=0.6
PW,PH,PX,PY=470,660,180,340
MIKA="assets/avatar/mika.mp4"; MASK="../foodeatup-tutoriel-5min/assets/avatar/mask.png"
def dur(f): return float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f]).strip())
VENC=["-c:v","libx264","-preset","medium","-crf","20","-pix_fmt","yuv420p","-r",str(FPS),"-c:a","aac","-b:a","192k","-ar","44100","-ac","2"]
SEQ=["hook","intro","reseaux","mcp","astuce1","generer","astuce2","planifier","astuce3","campagnes","astuce4","pilotage","outro"]
AVATAR={"intro":8}
listf=open("work/list.txt","w")
for i,sid in enumerate(SEQ):
    png=f"frames/{sid}.png"; vo=f"audio/{sid}.mp3"; d=dur(vo)+HEAD+TAIL; DF=int(round(d*FPS)); out=f"work/{sid}.mp4"
    if sid in AVATAR:
        off=AVATAR[sid]
        fc=(f"[0:v]scale=1920:1080,setsar=1[bg];[1:v]crop=720:1011:0:30,scale={PW}:{PH},setsar=1[av];"
            f"[av][2:v]alphamerge[ava];[bg][ava]overlay={PX}:{PY}:format=auto,fade=t=in:d=0.25[v];"
            f"[3:a]adelay={int(HEAD*1000)}|{int(HEAD*1000)},apad=whole_dur={d:.3f},aresample=44100,aformat=channel_layouts=stereo[a]")
        cmd=["ffmpeg","-y","-loop","1","-t",f"{d:.3f}","-i",png,"-ss",str(off),"-t",f"{d:.3f}","-i",MIKA,"-loop","1","-i",MASK,"-i",vo,
             "-filter_complex",fc,"-map","[v]","-map","[a]","-t",f"{d:.3f}"]+VENC+[out]
    else:
        zin="min(zoom+0.0006,1.05)" if i%2==0 else "if(eq(on,0),1.05,max(zoom-0.0006,1.0))"
        fc=(f"[0:v]scale=3840:2160,zoompan=z='{zin}':d={DF}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x1080:fps={FPS},fade=t=in:d=0.25,setsar=1[v];"
            f"[1:a]adelay={int(HEAD*1000)}|{int(HEAD*1000)},apad=whole_dur={d:.3f},aresample=44100,aformat=channel_layouts=stereo[a]")
        cmd=["ffmpeg","-y","-i",png,"-i",vo,"-filter_complex",fc,"-map","[v]","-map","[a]","-t",f"{d:.3f}"]+VENC+[out]
    r=subprocess.run(cmd,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
    if r.returncode!=0: print("ERR",sid,r.stderr.decode()[-1200:]); raise SystemExit(1)
    listf.write(f"file '{sid}.mp4'\n"); print("clip",sid,round(d,1))
listf.close()
subprocess.run(["ffmpeg","-y","-f","concat","-safe","0","-i","work/list.txt","-c","copy","work/master.mp4"],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
TOT=dur("work/master.mp4"); print("master",round(TOT,1))
fc=(f"[1:a]atrim=0:{TOT:.3f},asetpts=N/SR/TB,volume=0.06,afade=t=in:st=0:d=1.2,afade=t=out:st={TOT-1.8:.3f}:d=1.8[bg];"
    f"[0:a][bg]amix=inputs=2:normalize=0:dropout_transition=0,loudnorm=I=-14:TP=-1.5:LRA=11[a]")
subprocess.run(["ffmpeg","-y","-i","work/master.mp4","-stream_loop","-1","-i","assets/bgm.mp3","-filter_complex",fc,
    "-map","0:v","-map","[a]","-c:v","copy","-c:a","aac","-b:a","192k","deliverable/rapidocms-mcp-4min.mp4"],
    check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
print("DONE",round(dur("deliverable/rapidocms-mcp-4min.mp4"),1),"s")
