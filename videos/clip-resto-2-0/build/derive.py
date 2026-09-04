#!/usr/bin/env python3
"""Social derivatives, cut from the native 1080x1920 track.

  9:16  1080x1920  TikTok / Reels / Shorts  - with word-by-word lyric subtitles
  1:1   1080x1080  feed                     - no subtitles (brief)
  4:5   1080x1350  Facebook / Instagram     - no subtitles (brief)

The square and 4:5 are vertical crops of the same track, so the subject keeps
the framing it was shot with. The agent lower third is re-placed per format so
it stays inside each crop window.
"""
import os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
FONT = os.path.join(HERE, '..', 'assets', 'brand', 'Poppins-700.ttf')
DIST = os.path.join(HERE, '..', 'dist')
AUDIO = os.path.join(HERE, '..', 'assets', 'resto-2-0.mp3')
SRC = os.path.join(HERE, 'video-track-v.mp4')

AGENTS = [('Caroline', 126.39, 129.13), ('Jarvis', 129.13, 131.61),
          ('PrediBot', 131.61, 134.03), ('Iris', 134.03, 137.12)]
CREME, MARINE = '0xFCF9E6', '0x0F1A23'
# measured loudnorm pass 1 on the source
AF = ("[1:a]loudnorm=I=-14:TP=-1.5:LRA=11:measured_I=-13.92:measured_TP=-1.05:"
      "measured_LRA=6.80:measured_thresh=-24.04:offset=-0.78:linear=true,"
      "aresample=48000,apad[a]")


def agent_filters(cur, y, fs):
    """Lower third for the four agents, placed for this format."""
    out = []
    for i, (name, a, b) in enumerate(AGENTS):
        en = 'between(t,%.3f,%.3f)' % (a, b)
        fade = ("if(lt(t,%.3f),(t-%.3f)/0.25,if(gt(t,%.3f),(%.3f-t)/0.25,1))"
                % (a + 0.25, a, b - 0.25, b))
        out.append("%sdrawbox=x=0:y=%d:w=1080:h=%d:color=%s@0.55:t=fill:enable='%s'[b%d]"
                   % (cur, y - 22, fs + 52, MARINE, en, i)); cur = '[b%d]' % i
        out.append("%sdrawtext=fontfile='%s':text='%s':fontsize=%d:fontcolor=%s:"
                   "x=(w-text_w)/2:y=%d:alpha='%s':enable='%s'[c%d]"
                   % (cur, FONT, name, fs, CREME, y, fade, en, i)); cur = '[c%d]' % i
    return out, cur


def build(name, crop, y_agent, fs, subs, out):
    fc, cur = [], '[0:v]'
    if crop:
        fc.append('%scrop=1080:%d:0:%d[cr]' % (cur, crop[0], crop[1])); cur = '[cr]'
    af, cur = agent_filters(cur, y_agent, fs)
    fc += af
    if subs:
        fc.append("%ssubtitles='%s':fontsdir='%s'[sv]"
                  % (cur, os.path.join(HERE, 'lyrics.ass'),
                     os.path.join(HERE, '..', 'assets', 'brand'))); cur = '[sv]'
    fc.append('%snull[v]' % cur)
    cmd = ['ffmpeg', '-y', '-v', 'error', '-i', SRC, '-i', AUDIO,
           '-filter_complex', ';'.join(fc) + ';' + AF,
           '-map', '[v]', '-map', '[a]', '-shortest', '-frames:v', '5056',
           '-c:v', 'libx264', '-preset', 'slow', '-crf', '18', '-pix_fmt', 'yuv420p',
           '-profile:v', 'high', '-c:a', 'aac', '-b:a', '320k', '-ar', '48000',
           '-r', '30', '-movflags', '+faststart', os.path.join(DIST, out)]
    subprocess.run(cmd, check=True)
    print('%-6s -> %s' % (name, out))


TARGETS = {
    # name, crop(h, y), agent y, fontsize, subtitles, filename
    # agent name at source y=1060: below the problem captions, above the
    # solution captions, and inside every crop window
    'v':  (None,          1060, 62, True,  'FoodEatUp-Resto-2-0-vertical-1080x1920.mp4'),
    's':  ((1080, 420),    640, 54, False, 'FoodEatUp-Resto-2-0-carre-1080x1080.mp4'),
    'f':  ((1350, 285),    775, 56, False, 'FoodEatUp-Resto-2-0-4x5-1080x1350.mp4'),
}

if __name__ == '__main__':
    keys = sys.argv[1:] or list(TARGETS)
    for k in keys:
        crop, y, fs, subs, out = TARGETS[k]
        build(k, crop, y, fs, subs, out)
