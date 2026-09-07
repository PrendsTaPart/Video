#!/usr/bin/env bash
# Montage de la vidéo de démo pour la review TikTok for Developers.
# Un seul passage ffmpeg : découpe, cartons, gel de la dernière image,
# concaténation et incrustation des sous-titres.
#
#   ./build.sh
#
# Sortie : renders/braindcast-tiktok-demo.mp4
set -euo pipefail
cd "$(dirname "$0")"

SRC=source/Screen_Recording_20260907_144503_Chrome.mp4
OUT=renders/braindcast-tiktok-demo.mp4
FB=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf
FR=/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf

# Bornes de coupe relevées image par image sur le rush (voir README.md).
#   A  0.0 → 79.1   B  88.0 → 100.6   C  103.0 → 111.5
ffmpeg -nostdin -hide_banner -i "$SRC" -filter_complex "
[0:v]split=3[s1][s2][s3];
[s1]trim=0:79.1,setpts=PTS-STARTPTS,fps=30,scale=1080:2316,setsar=1,format=yuv420p[a];
[s2]trim=88.0:100.6,setpts=PTS-STARTPTS,fps=30,scale=1080:2316,setsar=1,format=yuv420p[b];
[s3]trim=103.0:111.5,setpts=PTS-STARTPTS,fps=30,scale=1080:2316,setsar=1,format=yuv420p,tpad=stop_mode=clone:stop_duration=3[c];
color=c=0x0E0E10:s=1080x2316:d=4:r=30,setsar=1,format=yuv420p,
 drawtext=fontfile=$FB:textfile=cards/card1.txt:fontsize=64:fontcolor=white:x=(w-text_w)/2:y=1010,
 drawtext=fontfile=$FR:textfile=cards/card1b.txt:fontsize=44:fontcolor=0x8A8A93:x=(w-text_w)/2:y=1120,
 drawtext=fontfile=$FR:textfile=cards/card1c.txt:fontsize=40:fontcolor=white:x=(w-text_w)/2:y=1240[card1];
color=c=0x0E0E10:s=1080x2316:d=5:r=30,setsar=1,format=yuv420p,
 drawtext=fontfile=$FR:textfile=cards/card2.txt:fontsize=52:fontcolor=white:line_spacing=26:x=(w-text_w)/2:y=(h-text_h)/2[card2];
[card1][a][b][c][card2]concat=n=5:v=1:a=0[cat];
[cat]subtitles=subs.ass:fontsdir=/usr/share/fonts/truetype/dejavu[outv]" \
  -map "[outv]" -an \
  -c:v libx264 -preset slow -crf 23 -pix_fmt yuv420p -movflags +faststart \
  -y "$OUT"

ls -la "$OUT"
ffprobe -v error -show_entries format=duration,size -of default=noprint_wrappers=1 "$OUT"
