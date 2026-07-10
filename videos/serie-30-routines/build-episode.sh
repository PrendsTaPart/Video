#!/usr/bin/env bash
# build-episode.sh — usine série "30 routines" : compositing Mika + montage final.
# Prérequis dans le projet: mika/mika-in.mp4 (hook), mika/mika-out.mp4 (outro réutilisé),
#   body.mp4 (rendu narrateur HyperFrames), assets/bgm/track.mp3, deliverable/.
# Usage:
#   PROJ=/path EP=03 ELABEL=E3/30 HOOK="texte hook" OUTRO="texte outro" \
#   TEASER1="DEMAIN" TEASER2="skills, agents, garde-fous" OUT=deliverable/xxx.mp4 \
#   bash build-episode.sh
set -euo pipefail
: "${PROJ:?}"; : "${EP:?}"; : "${ELABEL:?}"; : "${HOOK:?}"; : "${OUTRO:?}"; : "${TEASER1:?}"; : "${TEASER2:?}"; : "${OUT:?}"; : "${BODY:?}"
cd "$PROJ"
TTF=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf
SUB="/tmp/ep${EP}subs"; mkdir -p "$SUB"
V="-c:v libx264 -pix_fmt yuv420p -profile:v high -preset medium -crf 19 -r 30"
A="-c:a aac -ar 48000 -ac 2 -b:a 192k"
STYLE="FontName=DejaVu Sans,Fontsize=15,PrimaryColour=&H00FFFFFF,OutlineColour=&H1FF2675A,BorderStyle=3,Outline=9,Shadow=0,Bold=1,Alignment=2,MarginV=95"
# SRT generator: ~4 words/cue, tiny gap between cues to avoid box-doubling
srt(){ python3 - "$1" "$2" "$3" <<'PY'
import sys,subprocess
mp4,txt,out=sys.argv[1],sys.argv[2],sys.argv[3]
d=float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",mp4]).decode().strip())
w=txt.split(); cues=[w[i:i+4] for i in range(0,len(w),4)]; n=len(cues); step=d/n
def f(t):
    h=int(t//3600);m=int((t%3600)//60);s=int(t%60);ms=int(round((t-int(t))*1000));ms=min(ms,999)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"
out_s=[]
for i,c in enumerate(cues):
    st=i*step; en=(i+1)*step-0.06
    out_s.append(f"{i+1}\n{f(st)} --> {f(max(en,st+0.2))}\n{' '.join(c)}\n")
open(out,"w").write("\n".join(out_s))
PY
}
srt mika/mika-in.mp4 "$HOOK" "$SUB/hook.srt"
srt mika/mika-out.mp4 "$OUTRO" "$SUB/outro.srt"
# hook composite
ffmpeg -y -f lavfi -i "color=c=0xEDF1FB:s=1080x1920:d=$(ffprobe -v error -show_entries format=duration -of csv=p=0 mika/mika-in.mp4)" -i mika/mika-in.mp4 \
  -filter_complex "[1:v]crop=1080:608:0:656[b];[0:v][b]overlay=0:540[o];[o]subtitles=$SUB/hook.srt:force_style='$STYLE'[v]" -map "[v]" -map 1:a $V $A /tmp/ep${EP}-hook.mp4 -loglevel error
# outro composite + teaser
ffmpeg -y -f lavfi -i "color=c=0xEDF1FB:s=1080x1920:d=$(ffprobe -v error -show_entries format=duration -of csv=p=0 mika/mika-out.mp4)" -i mika/mika-out.mp4 \
  -filter_complex "[1:v]crop=1080:608:0:656[b];[0:v][b]overlay=0:540[o];[o]drawtext=fontfile=$TTF:text='$TEASER1':x=(w-tw)/2:y=210:fontsize=52:fontcolor=0x5a67f2,drawtext=fontfile=$TTF:text='$TEASER2':x=(w-tw)/2:y=290:fontsize=44:fontcolor=0x1b2a41,subtitles=$SUB/outro.srt:force_style='$STYLE'[v]" -map "[v]" -map 1:a $V $A /tmp/ep${EP}-outro.mp4 -loglevel error
# normalize body + concat
ffmpeg -y -i "$BODY" -vf scale=1080:1920 $V $A /tmp/ep${EP}-body.mp4 -loglevel error
printf "file '/tmp/ep%s-hook.mp4'\nfile '/tmp/ep%s-body.mp4'\nfile '/tmp/ep%s-outro.mp4'\n" $EP $EP $EP > /tmp/ep${EP}-concat.txt
ffmpeg -y -f concat -safe 0 -i /tmp/ep${EP}-concat.txt -c copy /tmp/ep${EP}-montage.mp4 -loglevel error
TOTAL=$(ffprobe -v error -show_entries format=duration -of csv=p=0 /tmp/ep${EP}-montage.mp4)
# overlays + bgm
ffmpeg -y -i /tmp/ep${EP}-montage.mp4 -stream_loop -1 -i assets/bgm/track.mp3 \
  -filter_complex "[0:v]drawtext=fontfile=$TTF:text='BraindCode':x=40:y=40:fontsize=40:fontcolor=0x1b2a41:box=1:boxcolor=0xffffff@0.55:boxborderw=16,drawtext=fontfile=$TTF:text='$ELABEL':x=w-tw-40:y=40:fontsize=40:fontcolor=0xffffff:box=1:boxcolor=0x5a67f2@0.9:boxborderw=16[v];[1:a]volume=0.09,afade=t=in:st=0:d=1.0,afade=t=out:st=$(python3 -c "print(round($TOTAL-1.8,2))"):d=1.8[bg];[0:a][bg]amix=inputs=2:duration=first:normalize=0[a]" \
  -map "[v]" -map "[a]" $V -c:a aac -ar 48000 -ac 2 -b:a 192k /tmp/ep${EP}-preloud.mp4 -loglevel error
mkdir -p "$(dirname "$OUT")"
ffmpeg -y -i /tmp/ep${EP}-preloud.mp4 -af "loudnorm=I=-14:TP=-1.5:LRA=11" -c:v copy -c:a aac -ar 48000 -ac 2 -b:a 192k -movflags +faststart "$OUT" -loglevel error
echo "OK $OUT $(ffprobe -v error -show_entries format=duration -of csv=p=0 "$OUT")"
