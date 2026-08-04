#!/usr/bin/env python3
"""Assemble RapidoRH vertical (1080x1920). Live Mika medallion on chapter frames,
Ken Burns on intro/astuces. Concat + BGM."""
import os, subprocess
os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.makedirs("work",exist_ok=True); os.makedirs("deliverable",exist_ok=True)
FPS=30; HEAD=0.4; TAIL=0.8
MIKA="assets/avatar/mika.mp4"; MASK="assets/avatar/circle-mask.png"
def dur(f): return float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f]).strip())
VENC=["-c:v","libx264","-preset","medium","-crf","20","-pix_fmt","yuv420p","-r",str(FPS),"-c:a","aac","-b:a","192k","-ar","44100","-ac","2"]
SEQ=["intro","compte","organisation","mcp","astuce1","equipe","astuce2","projets","astuce3","quotidien","astuce4","outro"]
MED={"compte","organisation","mcp","equipe","projets","quotidien","outro"}
OFF={"compte":4,"organisation":12,"mcp":20,"equipe":30,"projets":40,"quotidien":52,"outro":64}
listf=open("work/list.txt","w")
for i,sid in enumerate(SEQ):
    png=f"frames/{sid}.png"; vo=f"audio/{sid}.mp3"; d=dur(vo)+HEAD+TAIL; DF=int(round(d*FPS)); out=f"work/{sid}.mp4"
    if sid in MED:
        off=OFF.get(sid,4)
        fc=(f"[0:v]scale=1080:1920,setsar=1[bg];[1:v]crop=480:480:120:80,scale=230:230,setsar=1[mk];"
            f"[mk][2:v]alphamerge[mkc];[bg][mkc]overlay=80:310:format=auto,fade=t=in:d=0.25[v];"
            f"[3:a]adelay={int(HEAD*1000)}|{int(HEAD*1000)},apad=whole_dur={d:.3f},aresample=44100,aformat=channel_layouts=stereo[a]")
        cmd=["ffmpeg","-y","-loop","1","-t",f"{d:.3f}","-i",png,"-ss",str(off),"-t",f"{d:.3f}","-i",MIKA,"-loop","1","-i",MASK,"-i",vo,
             "-filter_complex",fc,"-map","[v]","-map","[a]","-t",f"{d:.3f}"]+VENC+[out]
    else:
        zin="min(zoom+0.0006,1.05)" if i%2==0 else "if(eq(on,0),1.05,max(zoom-0.0006,1.0))"
        fc=(f"[0:v]scale=2160:3840,zoompan=z='{zin}':d={DF}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x1920:fps={FPS},fade=t=in:d=0.25,setsar=1[v];"
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
subprocess.run(["ffmpeg","-y","-i","work/master.mp4","-stream_loop","-1","-i","audio/bgm.mp3","-filter_complex",fc,
    "-map","0:v","-map","[a]","-c:v","copy","-c:a","aac","-b:a","192k","deliverable/rapidorh-mcp-tiktok.mp4"],
    check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
print("DONE",round(dur("deliverable/rapidorh-mcp-tiktok.mp4"),1),"s")
