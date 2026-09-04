#!/usr/bin/env python3
"""Vertical (1080x1920) shot cut for the social derivatives.

Built from the native 9:16 rushes, not from the letterboxed 16:9 master, so the
subject keeps its full framing. The 1:1 and 4:5 cuts are vertical crops of this.
"""
import json, os, subprocess, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('a', os.path.join(HERE, 'assemble.py'))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

OUT = os.path.join(HERE, 'shots_v'); os.makedirs(OUT, exist_ok=True)
FPS = 30
VF = "[0:v]trim=start={i}:duration={d},setpts=PTS-STARTPTS,fps=30,scale=1080:1920,setsar=1[v]"

shots = m.EDL['shots']
for n, sh in enumerate(shots):
    sh['idx'] = n
    f0, f1 = round(sh['start']*FPS), round(sh['end']*FPS)
    nf = f1 - f0
    i = m.in_point(sh)
    subprocess.run(['ffmpeg','-y','-v','error','-i',os.path.join(m.RUSH, sh['ep']+'.mp4'),
        '-filter_complex', VF.format(i=i, d=nf/FPS + 0.5/FPS),
        '-map','[v]','-frames:v',str(nf),'-an','-c:v','libx264','-preset','medium','-crf','16',
        '-pix_fmt','yuv420p','-r','30','-video_track_timescale','30000',
        os.path.join(OUT,'%03d.mp4'%n)], check=True)
with open(os.path.join(HERE,'concat_v.txt'),'w') as fh:
    for n in range(len(shots)): fh.write("file 'shots_v/%03d.mp4'\n" % n)
print('%d vertical shots written' % len(shots))
