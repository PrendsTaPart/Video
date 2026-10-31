#!/bin/bash
# finir.sh <dossier épisode> <N> : rend les images, mixe, encode la vidéo, le short, la miniature et les sous-titres.
set -e
D=$(cd "$1" && pwd); N=$2; cd /home/user/Video
[ -s "$D/frames.mp4" ] || node videos/_moteur/render.js "$D" 30 > "$D/render.log" 2>&1
cd "$D"; DUR=$(python3 -c "import json;print(json.load(open('cfg.json'))['dur'])")
ffmpeg -y -v error -i voix/voix.mp3 -stream_loop -1 -i ../planit-academy/assets/audio/musique-produit.mp3 -filter_complex "[0]adelay=350|350,apad,atrim=0:$DUR,asplit=2[v][sc];[1]atrim=0:$DUR,volume=0.2,afade=t=in:d=1,afade=t=out:st=$(python3 -c "print($DUR-2)"):d=2[m];[m][sc]sidechaincompress=threshold=0.03:ratio=6:attack=20:release=300[md];[v][md]amix=2:normalize=0,loudnorm=I=-14:TP=-1.5[o]" -map "[o]" -ar 48000 -ac 2 mix.wav
NOM=$(basename "$D")
ffmpeg -y -v error -i frames.mp4 -i mix.wav -map 0:v -map 1:a -c:v libx264 -crf 21 -preset slow -pix_fmt yuv420p -c:a aac -b:a 192k -shortest -movflags +faststart "$NOM.mp4"
python3 - <<PY
import json,subprocess
C=json.load(open('cfg.json'));L=C['lines']
f=lambda t:f"{int(t//3600):02}:{int(t%3600//60):02}:{int(t%60):02},{int(round(t%1*1000))%1000:03}"
open('episode$N-sous-titres.srt','w').write("\n".join(f"{i+1}\n{f(l['t0'])} --> {f(l['t1'])}\n{l['txt']}\n" for i,l in enumerate(L)))
# short ≈ 30 s : accroche + premiers temps forts + fin
segs=[(0,min(L[min(5,len(L)-2)]['t1']+.3,22))]
end=C['dur'];segs.append((L[-1]['t0']-.15,end))
fc="".join(f"[0:v]trim={a:.2f}:{b:.2f},setpts=PTS-STARTPTS[v{i}];[0:a]atrim={a:.2f}:{b:.2f},asetpts=PTS-STARTPTS[a{i}];" for i,(a,b) in enumerate(segs))
fc+="".join(f"[v{i}][a{i}]" for i in range(len(segs)))+f"concat=n={len(segs)}:v=1:a=1[v][a]"
subprocess.run(["ffmpeg","-y","-v","error","-i","$NOM.mp4","-filter_complex",fc,"-map","[v]","-map","[a]","-c:v","libx264","-crf","21","-preset","slow","-pix_fmt","yuv420p","-c:a","aac","-b:a","192k","-movflags","+faststart","episode$N-short.mp4"],check=True)
PY
[ -f thumb.png ] && mv -f thumb.png "episode$N-miniature.png"
rm -f mix.wav frames.mp4
echo "$NOM $(ffprobe -v error -show_entries format=duration -of csv=p=0 $NOM.mp4)s short $(ffprobe -v error -show_entries format=duration -of csv=p=0 episode$N-short.mp4)s"
