#!/usr/bin/env python3
"""After the full render, swap in the real MCP link: rebuild only the s31 clip
(step 5) with the updated frame, then re-concat + re-BGM. Reuses the 26 other clips."""
import os, subprocess
os.chdir(os.path.dirname(os.path.abspath(__file__)))
FPS=30; HEAD=0.35; TAIL=0.6
def dur(f): return float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f]).strip())
VENC=["-c:v","libx264","-preset","medium","-crf","20","-pix_fmt","yuv420p","-r",str(FPS),
      "-c:a","aac","-b:a","192k","-ar","44100","-ac","2"]
# 1) regenerate frames (build_fe169.py now has the real link)
subprocess.run(["python3","build_fe169.py"],check=True,stdout=subprocess.DEVNULL)
# 2) rebuild work/s31.mp4 (SEQ index 8 -> even -> zoom-in)
png="frames/s31.png"; vo="audio/s31.mp3"; d=dur(vo)+HEAD+TAIL; DF=int(round(d*FPS))
zin="min(zoom+0.0006,1.05)"
fc=(f"[0:v]scale=3840:2160,zoompan=z='{zin}':d={DF}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x1080:fps={FPS},"
    f"fade=t=in:d=0.25,setsar=1[v];"
    f"[1:a]adelay={int(HEAD*1000)}|{int(HEAD*1000)},apad=whole_dur={d:.3f},aresample=44100,aformat=channel_layouts=stereo[a]")
subprocess.run(["ffmpeg","-y","-i",png,"-i",vo,"-filter_complex",fc,"-map","[v]","-map","[a]","-t",f"{d:.3f}"]+VENC+["work/s31.mp4"],
    check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
# 3) re-concat + re-BGM
subprocess.run(["ffmpeg","-y","-f","concat","-safe","0","-i","work/list.txt","-c","copy","work/master.mp4"],
    check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
TOT=dur("work/master.mp4")
fc=(f"[1:a]atrim=0:{TOT:.3f},asetpts=N/SR/TB,volume=0.06,afade=t=in:st=0:d=1.5,afade=t=out:st={TOT-2:.3f}:d=2[bg];"
    f"[0:a][bg]amix=inputs=2:normalize=0:dropout_transition=0,loudnorm=I=-14:TP=-1.5:LRA=11[a]")
subprocess.run(["ffmpeg","-y","-i","work/master.mp4","-stream_loop","-1","-i","audio/bgm.mp3",
    "-filter_complex",fc,"-map","0:v","-map","[a]","-c:v","copy","-c:a","aac","-b:a","192k",
    "deliverable/foodeatup-tutoriel-5min.mp4"],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
print("FINAL",round(dur("deliverable/foodeatup-tutoriel-5min.mp4"),1),"s")
