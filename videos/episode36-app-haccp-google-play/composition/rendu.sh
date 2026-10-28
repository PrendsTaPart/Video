#!/bin/bash
# Épisode 36 v2 : rendu, incrustation des extraits de l'épisode 2 (dimanche), mixage et short.
set -e
cd "$(dirname "$0")"
DIM=/home/user/Video/videos/dimanche-4-apps-1-jeu/renders/dimanche-4-apps-1-jeu_1080x1920.mp4
[ -f v36b/frames_raw.mp4 ] && cp v36b/frames_raw.mp4 v36b/frames.mp4 || node render.js v36b 30 > v36b/render.log 2>&1
ffmpeg -y -v error -i v36b/frames.mp4 -i "$DIM" -filter_complex "\
[1:v]split=4[s1][s2][s3][s4];\
[s1]trim=19.0:22.0,setpts=PTS-STARTPTS+0/TB,scale=600:1072[a];\
[s2]trim=71.5:74.65,setpts=PTS-STARTPTS+3.0/TB,scale=600:1072[b];\
[s3]trim=31:34.7,setpts=PTS-STARTPTS+49.95/TB,scale=462:828,format=yuva420p,fade=t=in:st=49.95:d=0.3:alpha=1[c];\
[s4]trim=7.5:11.2,setpts=PTS-STARTPTS+49.95/TB,scale=462:828,format=yuva420p,fade=t=in:st=49.95:d=0.3:alpha=1[d];\
[0:v][a]overlay=240:226:eof_action=pass[x1];[x1][b]overlay=240:226:eof_action=pass[x2];\
[x2][c]overlay=54:244:eof_action=pass[x3];[x3][d]overlay=564:244:eof_action=pass,format=yuv420p[v]" \
 -map "[v]" -c:v libx264 -preset medium -crf 19 -pix_fmt yuv420p v36b/frames_ov.mp4
[ -f v36b/frames_raw.mp4 ] || mv v36b/frames.mp4 v36b/frames_raw.mp4; mv v36b/frames_ov.mp4 v36b/frames.mp4
segs=$(python3 -c "
import json;c=json.load(open('v36b/cfg.json'));P=c['P']+[c['dur']-0.08]
print(','.join(f'{P[i]:.2f}-{P[i+1]:.2f}' for i in [0,1,2,4,6,10]))")
python3 finish.py v36b /home/user/Video/videos/planit-academy/assets/audio/musique-produit.mp3 episode36 "$segs" > v36b/finish.log 2>&1
echo "done $segs"
