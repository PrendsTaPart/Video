#!/usr/bin/env python3
"""Assemble V5 16:9 — manifeste + séquence refus (croix) + SR validations + sting.
Sound design : voix nue (p1,p7), tics sur la séquence, dings sur les validations, BGM ducké."""
import os, subprocess
os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.makedirs("work",exist_ok=True); os.makedirs("renders",exist_ok=True)
BASE="/home/user/Video"; BGM=f"{BASE}/videos/stories-foodeatup-30j/audio/bgm.mp3"; CHIME=f"{BASE}/videos/serie-30-e01/assets/sfx/chime.mp3"
W,H=1920,1080; FPS=30
VENC=["-c:v","libx264","-preset","medium","-crf","20","-pix_fmt","yuv420p","-r",str(FPS),"-c:a","aac","-b:a","192k","-ar","44100","-ac","2"]
def dur(f): return float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f]).strip())
def run(cmd,n):
    r=subprocess.run(cmd,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
    if r.returncode!=0: print("ERR",n,r.stderr.decode()[-1400:]); raise SystemExit(1)
    print("ok",n,round(dur(cmd[-1]),2))
def voa(idx,d,head=0.3): return f"[{idx}:a]adelay={int(head*1000)}|{int(head*1000)},apad=whole_dur={d:.3f},aresample=44100,aformat=channel_layouts=stereo[a]"
def still(png,vo,out,extra=0.9,zoom=False,warm=False):
    d=dur(vo)+extra; DF=int(d*FPS)
    if zoom:
        v=f"[0:v]scale={W*2}:{H*2},zoompan=z='min(zoom+0.0006,1.07)':d={DF}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s={W}x{H}:fps={FPS},setsar=1,fade=t=in:d=0.3[v];"
    else:
        v=f"[0:v]scale={W}:{H},setsar=1,fade=t=in:d=0.35[v];"
    run(["ffmpeg","-y","-loop","1","-t",f"{d:.3f}","-i",png,"-i",vo,"-filter_complex",v+voa(1,d),"-map","[v]","-map","[a]","-t",f"{d:.3f}"]+VENC+[out],os.path.basename(out))

# P1 manifeste (voix nue) — lead 0.4 + tail 1.4
still("frames/p1.png","audio/v1.mp3","work/p1.mp4",extra=1.8)
# P2 brigade
still("frames/p2.png","audio/v2.mp3","work/p2.mp4",extra=0.8,zoom=True)
# sting (flash) + chime
run(["ffmpeg","-y","-loop","1","-t","0.9","-i","frames/sting.png","-loop","1","-t","0.7","-i","frames/sting_flash.png","-i",CHIME,
     "-filter_complex",f"[0:v]scale={W}:{H},setsar=1,fade=t=in:d=0.3[a0];[1:v]scale={W}:{H},setsar=1[a1];[a0][a1]concat=n=2:v=1:a=0[v];[2:a]adelay=700|700,volume=0.5,apad=whole_dur=1.6[a]",
     "-map","[v]","-map","[a]","-t","1.6"]+VENC+["work/sting.mp4"],"sting")
# P4 manifeste
still("frames/p4.png","audio/v4.mp3","work/p4.mp4",extra=0.9)
# P5 séquence refus (4 sous-plans + tic par plan)
d5=dur("audio/v5.mp3")+0.6; each=d5/4
for i,fr in enumerate(["not_02","not_03","not_04","not_05"]):
    z="min(zoom+0.0009,1.06)" if i%2==0 else "if(eq(on,0),1.06,max(zoom-0.0009,1.0))"
    run(["ffmpeg","-y","-loop","1","-t",f"{each:.3f}","-i",f"frames/{fr}.png","-vf",f"scale={W*2}:{H*2},zoompan=z='{z}':d={int(each*FPS)}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s={W}x{H}:fps={FPS},setsar=1,fade=t=in:d=0.12"]+VENC[:-8]+["-an","-frames:v",str(int(each*FPS)),f"work/p5_{i}.mp4"],f"p5_{i}")
open("work/p5l.txt","w").write("".join(f"file 'p5_{i}.mp4'\n" for i in range(4)))
run(["ffmpeg","-y","-f","concat","-safe","0","-i","work/p5l.txt","-c","copy","work/p5v.mp4"],"p5v")
d5v=dur("work/p5v.mp4")
tic="".join(f"[2:a]atrim=0:0.12,adelay={int(i*each*1000)}|{int(i*each*1000)},volume=0.4[t{i}];" for i in range(4))
tmix="".join(f"[t{i}]" for i in range(4))
fc=(f"[1:a]adelay=300|300,apad=whole_dur={d5v:.3f}[vo];{tic}{tmix}amix=inputs=4:normalize=0[tics];"
    f"[vo][tics]amix=inputs=2:normalize=0,apad=whole_dur={d5v:.3f},aformat=channel_layouts=stereo[a]")
run(["ffmpeg","-y","-i","work/p5v.mp4","-i","audio/v5.mp3","-i",CHIME,"-filter_complex",fc,"-map","0:v","-map","[a]","-t",f"{d5v:.3f}"]+VENC+["work/p5.mp4"],"p5")
# P6 SR validations (3 sous-plans + ding)
d6=dur("audio/v6.mp3")+0.9; e6=d6/3
for i,fr in enumerate(["sr1","sr2","sr3"]):
    run(["ffmpeg","-y","-loop","1","-t",f"{e6:.3f}","-i",f"frames/{fr}.png","-vf",f"scale={W}:{H},setsar=1,fade=t=in:d=0.1"]+VENC[:-8]+["-an","-frames:v",str(int(e6*FPS)),f"work/p6_{i}.mp4"],f"p6_{i}")
open("work/p6l.txt","w").write("".join(f"file 'p6_{i}.mp4'\n" for i in range(3)))
run(["ffmpeg","-y","-f","concat","-safe","0","-i","work/p6l.txt","-c","copy","work/p6v.mp4"],"p6v")
d6v=dur("work/p6v.mp4")
ding="".join(f"[2:a]adelay={int(i*e6*1000)}|{int(i*e6*1000)},volume=0.6[d{i}];" for i in range(3))
dmix="".join(f"[d{i}]" for i in range(3))
fc=(f"[1:a]adelay=200|200,apad=whole_dur={d6v:.3f}[vo];{ding}{dmix}amix=inputs=3:normalize=0[dings];"
    f"[vo][dings]amix=inputs=2:normalize=0,apad=whole_dur={d6v:.3f},aformat=channel_layouts=stereo[a]")
run(["ffmpeg","-y","-i","work/p6v.mp4","-i","audio/v6.mp3","-i",CHIME,"-filter_complex",fc,"-map","0:v","-map","[a]","-t",f"{d6v:.3f}"]+VENC+["work/p6.mp4"],"p6")
# P7 sommet (silence/voix nue)
still("frames/p7.png","audio/v7.mp3","work/p7.mp4",extra=1.6)
# P8 brigade détendue
still("frames/p8.png","audio/v8.mp3","work/p8.mp4",extra=1.0,zoom=True)
# P9 sting sortie + offre
still("frames/p9.png","audio/v9.mp3","work/p9.mp4",extra=1.2)

order=["p1","p2","sting","p4","p5","p6","p7","p8","p9"]
open("work/all.txt","w").write("".join(f"file '{p}.mp4'\n" for p in order))
run(["ffmpeg","-y","-f","concat","-safe","0","-i","work/all.txt","-c","copy","work/master.mp4"],"master")
TOT=dur("work/master.mp4")
# fenêtres voix nue = p1 et p7 (BGM ~0)
acc=0; w1=(0,0); w7=(0,0)
for p in order:
    dd=dur(f"work/{p}.mp4")
    if p=="p1": w1=(acc,acc+dd)
    if p=="p7": w7=(acc,acc+dd)
    acc+=dd
fc=(f"[1:a]atrim=0:{TOT:.3f},asetpts=N/SR/TB,"
    f"volume='if(between(t,{w1[0]:.2f},{w1[1]:.2f})+between(t,{w7[0]:.2f},{w7[1]:.2f}),0.012,0.05)':eval=frame,"
    f"afade=t=in:st=0:d=1.2,afade=t=out:st={TOT-1.6:.3f}:d=1.6[bg];"
    f"[0:a][bg]amix=inputs=2:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[a]")
run(["ffmpeg","-y","-i","work/master.mp4","-stream_loop","-1","-i",BGM,"-filter_complex",fc,"-map","0:v","-map","[a]","-c:v","copy","-c:a","aac","-b:a","192k","-movflags","+faststart","renders/foodeatup-v5-objection-16x9.mp4"],"FINAL")
print("DONE",round(dur("renders/foodeatup-v5-objection-16x9.mp4"),1),"s")
