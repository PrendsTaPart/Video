#!/usr/bin/env python3
"""Cut the rush track for Resto 2.0.

Sources are natively 1080x1920 (vertical). The 1920x1080 master therefore uses a
uniform treatment for all 33 episodes: the vertical frame at full height over a
blurred, brand-darkened enlargement of itself. Using the same treatment
everywhere avoids mixing the pre-baked yt16- files (only 12 episodes have one)
with self-treated ones.

Each rush is 12.5 s: 0-7 s = the problem, 7-10 s = the software resolving it,
10-12.5 s = the episode end card, which must never appear in the clip.
"""
import json, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
RUSH = os.path.join(HERE, 'rushes-9x16')
OUT  = os.path.join(HERE, 'shots')
os.makedirs(OUT, exist_ok=True)

EDL = json.load(open(os.path.join(HERE, 'edl.json')))
FPS = 30

# usable content ceiling per episode (end card starts here)
CEIL = {ep: 10.0 for ep in os.listdir(RUSH)}
CEIL_DEFAULT, CEIL_EP119 = 10.0, 9.5

# Verses and pre-refrains show the problem; refrains, the bridge and the final
# refrain show the software resolving it. Keyed by shot index, so float
# comparisons on snapped onset times cannot misclassify a section boundary.
#   0-10  verse 1 + pre-refrain 1      11-18  refrain 1
#   19-26 verse 2   27-28 pre-refrain 2  29-36 refrain 2
#   37-40 bridge (agents)               41-49 final refrain
PROBLEME_IDX = set(range(0, 11)) | set(range(19, 29))

def zone(shot):
    return 'probleme' if shot['idx'] in PROBLEME_IDX else 'solution'


def in_point(shot):
    """Pick the in-point inside the rush, never crossing into the end card."""
    ep, dur = shot['ep'], shot['dur']
    ceil = CEIL_EP119 if ep == 'EP119' else CEIL_DEFAULT
    if zone(shot) == 'solution':
        # ride as late as possible: the most 'resolved' frames, end card excluded
        return max(0.3, round(ceil - dur - 0.20, 3))
    return 0.40                            # firmly inside the problem beat

VF = ("[0:v]trim=start={i}:duration={d},setpts=PTS-STARTPTS,fps=30,split=2[bg][fg];"
      "[bg]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,"
      "gblur=sigma=42,eq=brightness=-0.20:saturation=0.62,"
      "colorbalance=rs=-0.05:bs=0.08[bgo];"
      "[fg]scale=-2:1080:flags=lanczos[fgo];"
      "[bgo][fgo]overlay=(W-w)/2:0:format=auto,setsar=1[v]")

def main():
    shots = EDL['shots']
    for n, sh in enumerate(shots):
        sh['idx'] = n
        src = os.path.join(RUSH, sh['ep'] + '.mp4')
        # Quantise both cut points to the 30 fps grid and drive the shot by an
        # exact frame count. Trimming each shot to its own float duration let
        # per-shot rounding accumulate (~0.9 s over 50 shots), which would drag
        # every later cut off its onset.
        f0, f1 = round(sh['start'] * FPS), round(sh['end'] * FPS)
        nframes = f1 - f0
        i, d = in_point(sh), nframes / FPS
        dst = os.path.join(OUT, '%03d.mp4' % n)
        cmd = ['ffmpeg','-y','-v','error','-i',src,
               '-filter_complex', VF.format(i=i, d=d + 0.5/FPS),
               '-map','[v]','-frames:v', str(nframes),
               '-an','-c:v','libx264','-preset','medium','-crf','16',
               '-pix_fmt','yuv420p','-r','30', dst]
        subprocess.run(cmd, check=True)
        print('%03d %-7s %-9s in=%5.2f frames=%3d (%5.2fs)  %s' % (n, sh['ep'], zone(sh), i, nframes, d, sh['note'][:40]))
    with open(os.path.join(HERE,'concat.txt'),'w') as f:
        for n in range(len(shots)):
            f.write("file 'shots/%03d.mp4'\n" % n)
    print('\n%d shots written' % len(shots))

if __name__ == '__main__':
    main()
