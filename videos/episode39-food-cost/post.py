import json,subprocess
d="v39";c=json.load(open(f"{d}/cfg.json"));P=c["P"];dur=c["dur"]
M="/home/user/Video/videos/planit-academy/assets/audio/musique-produit.mp3"
run=lambda *a: subprocess.run(["ffmpeg","-y","-v","error",*a],check=True)
a5,b5,a6,b6=P[5]+.35,P[6],P[6]+.35,P[7]
run("-i",f"{d}/frames.mp4","-i",f"{d}/clip5.mp4","-i",f"{d}/clip6.mp4","-filter_complex",
 f"[1:v]setpts=PTS-STARTPTS+{a5}/TB[c5];[2:v]setpts=PTS-STARTPTS+{a6}/TB[c6];"
 f"[0:v][c5]overlay=46:520:enable='between(t,{a5},{b5})':eof_action=pass[v1];[v1][c6]overlay=46:440:enable='between(t,{a6},{b6})':eof_action=pass[v]",
 "-map","[v]","-c:v","libx264","-crf","19","-pix_fmt","yuv420p",f"{d}/frames2.mp4")
ms=int(c["off"]*1000)
run("-stream_loop","4","-i",M,"-t",str(dur),"-ar","48000","-ac","2",f"{d}/bed.wav")
run("-i",f"{d}/vo.mp3","-i",f"{d}/bed.wav","-filter_complex",
 f"[0:a]aresample=48000,adelay={ms}|{ms},apad=whole_dur={dur},asplit[v1][v2];[1:a]volume=0.18,afade=t=out:st={dur-2.5}:d=2.5[mu];[mu][v1]sidechaincompress=threshold=0.03:ratio=8:attack=20:release=400[du];[v2][du]amix=inputs=2:normalize=0:duration=first,loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000[o]",
 "-map","[o]","-t",str(dur),f"{d}/mix.wav")
out=f"{d}/episode39-food-cost-{round(dur)}s.mp4"
run("-i",f"{d}/frames2.mp4","-i",f"{d}/mix.wav","-c:v","copy","-c:a","aac","-b:a","192k","-shortest","-movflags","+faststart",out)
def ts(x):
    ms=int(round(x*1000));h,ms=divmod(ms,3600000);m,ms=divmod(ms,60000);s,ms=divmod(ms,1000);return f"{h:02}:{m:02}:{s:02},{ms:03}"
W=c["words"];G=[];g=[]
for k,w in enumerate(W):
    g.append(k)
    if len(g)>=6 or w[0][-1] in ".,:;?!": G.append(g);g=[]
if g:G.append(g)
cues=[(W[g[0]][1],(W[G[i+1][0]][1] if i+1<len(G) else W[g[-1]][1]+.8)," ".join(W[k][0] for k in g)) for i,g in enumerate(G)]
open(f"{d}/episode39-sous-titres.srt","w").write("\n".join(f"{i+1}\n{ts(a)} --> {ts(b)}\n{t}\n" for i,(a,b,t) in enumerate(cues)))
print(out)
