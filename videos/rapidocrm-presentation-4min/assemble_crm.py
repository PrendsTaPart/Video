#!/usr/bin/env python3
"""Assemble RapidoCRM 16:9 (1920x1080, ~4min). Sting 3 oiseaux (plans 2 & 14), Mika live,
chat Claude machine à écrire (3 astuces) + oiseau vert, séquences d'écrans Ken Burns, BGM."""
import os, subprocess, glob
os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.makedirs("wcrm",exist_ok=True); os.makedirs("renders",exist_ok=True)
BASE="/home/user/Video"; STO=f"{BASE}/videos/stories-foodeatup-30j"
MIKA=f"{STO}/assets/avatar/mika.mp4"; BGM=f"{STO}/audio/bgm.mp3"; CHIME=f"{BASE}/videos/serie-30-e01/assets/sfx/chime.mp3"
STING="composition/logo-sting"
FPS=30; W,H=1920,1080
VENC=["-c:v","libx264","-preset","medium","-crf","20","-pix_fmt","yuv420p","-r",str(FPS),"-c:a","aac","-b:a","192k","-ar","44100","-ac","2"]
def dur(f): return float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f]).strip())
def run(cmd,name):
    r=subprocess.run(cmd,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
    if r.returncode!=0: print("ERR",name,r.stderr.decode()[-1400:]); raise SystemExit(1)
    print("ok",name,round(dur(cmd[-1]),2))
def voa(idx,d,head=0.3): return f"[{idx}:a]adelay={int(head*1000)}|{int(head*1000)},apad=whole_dur={d:.3f},aresample=44100,aformat=channel_layouts=stereo[a]"

def kb(png,d,i,out):
    z="min(zoom+0.0006,1.06)" if i%2==0 else "if(eq(on,0),1.06,max(zoom-0.0006,1.0))"
    run(["ffmpeg","-y","-loop","1","-t",f"{d:.3f}","-i",png,"-vf",f"scale={W*2}:{H*2},zoompan=z='{z}':d={int(d*FPS)}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s={W}x{H}:fps={FPS},setsar=1"]+VENC[:-8]+["-an","-frames:v",str(int(d*FPS)),out],os.path.basename(out))
def seq(pngs,vo,out):
    d=dur(vo)+0.8; each=d/len(pngs); parts=[]
    for i,p in enumerate(pngs): o=f"wcrm/_{os.path.basename(out)}_{i}.mp4"; kb(p,each,i,o); parts.append(o)
    lst=f"wcrm/_{os.path.basename(out)}.txt"; open(lst,"w").write("".join(f"file '{os.path.basename(x)}'\n" for x in parts))
    run(["ffmpeg","-y","-f","concat","-safe","0","-i",lst,"-c","copy",f"wcrm/_{os.path.basename(out)}v.mp4"],"seqv")
    dv=dur(f"wcrm/_{os.path.basename(out)}v.mp4")
    run(["ffmpeg","-y","-i",f"wcrm/_{os.path.basename(out)}v.mp4","-i",vo,"-filter_complex",voa(1,dv,0.2),"-map","0:v","-map","[a]","-t",f"{dv:.3f}"]+VENC+[out],os.path.basename(out))
def mika(png,vo,out,diam,ox,oy,off=8):
    d=dur(vo)+0.7
    fc=(f"[0:v]scale={W}:{H},setsar=1[bg];[1:v]crop=560:560:80:40,scale={diam}:{diam},setsar=1[mk];[mk][2:v]alphamerge[mkc];[bg][mkc]overlay={ox}:{oy}:format=auto,fade=t=in:d=0.3[v];"+voa(3,d))
    run(["ffmpeg","-y","-loop","1","-t",f"{d:.3f}","-i",png,"-ss",str(off),"-t",f"{d:.3f}","-i",MIKA,"-loop","1","-i",f"masks/c{diam}.png","-i",vo,"-filter_complex",fc,"-map","[v]","-map","[a]","-t",f"{d:.3f}"]+VENC+[out],os.path.basename(out))
def chat(k,vo,out):
    n=int(open(f"frames/chat/{k}_n.txt").read()); TF=7.0; dt=n/TF
    run(["ffmpeg","-y","-framerate",str(TF),"-i",f"frames/chat/{k}_%03d.png","-vf",f"scale={W}:{H},setsar=1,fps={FPS}","-t",f"{dt:.3f}"]+VENC[:-8]+["-an","-frames:v",str(int(dt*FPS)),f"wcrm/_{k}a.mp4"],k+"a")
    run(["ffmpeg","-y","-loop","1","-t","2.0","-i",f"frames/chat/{k}_check.png","-vf",f"scale={W}:{H},setsar=1,fps={FPS}"]+VENC[:-8]+["-an","-frames:v",str(int(2*FPS)),f"wcrm/_{k}b.mp4"],k+"b")
    open(f"wcrm/_{k}l.txt","w").write(f"file '_{k}a.mp4'\nfile '_{k}b.mp4'\n"); run(["ffmpeg","-y","-f","concat","-safe","0","-i",f"wcrm/_{k}l.txt","-c","copy",f"wcrm/_{k}v.mp4"],k+"v")
    dv=dur(f"wcrm/_{k}v.mp4")
    fc=(f"[1:a]adelay=300|300,apad=whole_dur={dv:.3f}[vo];[2:a]adelay={int(dt*1000)}|{int(dt*1000)},volume=0.6[d];[vo][d]amix=inputs=2:normalize=0,apad=whole_dur={dv:.3f},aformat=channel_layouts=stereo[a]")
    run(["ffmpeg","-y","-i",f"wcrm/_{k}v.mp4","-i",vo,"-i",CHIME,"-filter_complex",fc,"-map","0:v","-map","[a]","-t",f"{dv:.3f}"]+VENC+[out],os.path.basename(out))
def norm_sting(src,out):
    run(["ffmpeg","-y","-i",f"{STING}/{src}.mp4","-filter_complex",f"[0:v]scale={W}:{H},setsar=1,fps={FPS}[v];[0:a]aresample=44100,aformat=channel_layouts=stereo[a]","-map","[v]","-map","[a]"]+VENC+[out],out)

A="audio"
norm_sting("sting-crm-in","wcrm/sting_in.mp4"); norm_sting("sting-crm-out","wcrm/sting_out.mp4")
kb("frames/p1.png",dur(f"{A}/c1.mp3")+0.8,0,"wcrm/_p1v.mp4"); dv=dur("wcrm/_p1v.mp4")
run(["ffmpeg","-y","-i","wcrm/_p1v.mp4","-i",f"{A}/c1.mp3","-filter_complex",voa(1,dv),"-map","0:v","-map","[a]","-t",f"{dv:.3f}"]+VENC+["wcrm/p1.mp4"],"p1")
mika("frames/p3.png",f"{A}/c3.mp3","wcrm/p3.mp4",560,100,420)
seq(["frames/p4a.png","frames/p4b.png","frames/p4c.png"],f"{A}/c4.mp3","wcrm/p4.mp4")
seq(["frames/p5a.png","frames/p5b.png","frames/p5c.png"],f"{A}/c5.mp3","wcrm/p5.mp4")
seq(["frames/p6.png"],f"{A}/c6.mp3","wcrm/p6.mp4")
chat("a1",f"{A}/c6a.mp3","wcrm/p6a.mp4")
seq(["frames/p7a.png","frames/p7b.png"],f"{A}/c7.mp3","wcrm/p7.mp4")
chat("a2",f"{A}/c7a.mp3","wcrm/p7a.mp4")
seq(["frames/p8a.png","frames/p8b.png","frames/p8c.png","frames/p8d.png"],f"{A}/c8.mp3","wcrm/p8.mp4")
seq(["frames/p9a.png","frames/p9b.png"],f"{A}/c9.mp3","wcrm/p9.mp4")
chat("a3",f"{A}/c9a.mp3","wcrm/p9a.mp4")
seq(["frames/p10a.png","frames/p10b.png","frames/p10c.png"],f"{A}/c10.mp3","wcrm/p10.mp4")
# sting out + hook de fin VO (c11) overlaid
dso=dur("wcrm/sting_out.mp4"); dv=dur(f"{A}/c11.mp3")+0.6
run(["ffmpeg","-y","-i","wcrm/sting_out.mp4","-i",f"{A}/c11.mp3","-filter_complex",f"[0:v]tpad=stop_mode=clone:stop_duration={max(0,dv-dso):.3f}[v];[0:a]aresample=44100[st];[1:a]adelay=200|200,apad=whole_dur={dv:.3f}[vo];[st][vo]amix=inputs=2:normalize=0,aformat=channel_layouts=stereo[a]","-map","[v]","-map","[a]","-t",f"{dv:.3f}"]+VENC+["wcrm/p14.mp4"],"p14")

order=["p1","sting_in","p3","p4","p5","p6","p6a","p7","p7a","p8","p9","p9a","p10","p14"]
open("wcrm/all.txt","w").write("".join(f"file '{p}.mp4'\n" for p in order))
run(["ffmpeg","-y","-f","concat","-safe","0","-i","wcrm/all.txt","-c","copy","wcrm/master.mp4"],"master")
TOT=dur("wcrm/master.mp4")
fc=(f"[1:a]atrim=0:{TOT:.3f},asetpts=N/SR/TB,volume=0.04,afade=t=in:st=0:d=1.2,afade=t=out:st={TOT-1.8:.3f}:d=1.8[bg];[0:a][bg]amix=inputs=2:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[a]")
run(["ffmpeg","-y","-i","wcrm/master.mp4","-stream_loop","-1","-i",BGM,"-filter_complex",fc,"-map","0:v","-map","[a]","-c:v","copy","-c:a","aac","-b:a","192k","-movflags","+faststart","renders/rapidocrm-4min.mp4"],"FINAL")
print("DONE",round(dur("renders/rapidocrm-4min.mp4"),1),"s")
