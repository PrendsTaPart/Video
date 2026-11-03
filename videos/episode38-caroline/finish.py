import json,subprocess
d="v38"; c=json.load(open(f"{d}/cfg.json")); dur=c["dur"]; L=c["lines"]
M="/home/user/Video/videos/planit-academy/assets/audio/musique-produit.mp3"
run=lambda *a: subprocess.run(["ffmpeg","-y","-v","error",*a],check=True)
# sonnerie (440+480 Hz, 0,8 s on / 0,4 s off) de 4,0 s au décroché
ring_end=L[4]["t0"]-0.2
run("-f","lavfi","-i",f"sine=f=440:d={dur}","-f","lavfi","-i",f"sine=f=480:d={dur}","-filter_complex",
 f"[0][1]amix=2,volume='if(between(t,4,{ring_end})*lt(mod(t-4,1.2),0.8),0.35,0)':eval=frame,aresample=48000[r]","-map","[r]","-ac","1",f"{d}/ring.wav")
# clic de décroché + pops sur notifications
pops=[L[4]["t0"]-0.15,L[6]["t0"]+0.15,L[8]["t0"]+0.15,L[10]["t0"]+1.0,L[10]["t0"]+2.4]
ex="+".join(f"between(t,{p:.2f},{p+0.06:.2f})*sin(2*PI*(900-6000*(t-{p:.2f}))*t)" for p in pops)
run("-f","lavfi","-i",f"aevalsrc='0.5*({ex})':s=48000:d={dur}",f"{d}/pops.wav")
run("-stream_loop","4","-i",M,"-t",str(dur),"-ar","48000","-ac","2",f"{d}/bed.wav")
run("-i",f"{d}/vo.wav","-i",f"{d}/bed.wav","-i",f"{d}/ring.wav","-i",f"{d}/pops.wav","-filter_complex",
 f"[0:a]aresample=48000,asplit[v1][v2];[1:a]volume=0.16,afade=t=out:st={dur-2.5}:d=2.5[mu];[mu][v1]sidechaincompress=threshold=0.03:ratio=8:attack=20:release=400[du];"
 f"[v2][du][2:a][3:a]amix=inputs=4:normalize=0:duration=first,loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000[o]","-map","[o]","-t",str(dur),f"{d}/mix.wav")
run("-i",f"{d}/frames.mp4","-i",f"{d}/mix.wav","-c:v","copy","-c:a","aac","-b:a","192k","-shortest","-movflags","+faststart",f"{d}/episode38-caroline-{round(dur)}s.mp4")
def ts(x):
    ms=int(round(x*1000));h,ms=divmod(ms,3600000);m,ms=divmod(ms,60000);s,ms=divmod(ms,1000);return f"{h:02}:{m:02}:{s:02},{ms:03}"
names={"chef":"Le chef","caro":"Caroline","cli":"Client"}
open(f"{d}/episode38-sous-titres.srt","w").write("\n".join(f"{k+1}\n{ts(l['t0'])} --> {ts(l['t1'])}\n{names[l['sp']]} : {l['txt']}\n" for k,l in enumerate(L)))
print("ok",dur)
