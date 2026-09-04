#!/usr/bin/env python3
"""Composite the brand overlays onto the base timeline.

  - white logomark flash, 1/8 s, on each sung "FoodEatUp" attack
  - the double-O infinity, looping once, on "huit boucles"
  - the agent name in the bridge, lower third
All cues are absolute master times; the base is constant 30 fps so they land on
the intended frame.
"""
import json, os, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
E = json.load(open(os.path.join(HERE, 'edl.json')))
FONT = os.path.join(HERE, '..', 'assets', 'brand', 'Poppins-700.ttf')

# the 152.31 attack falls inside the closing animation, which carries its own
# logo resolution — flashing there would fight it
FLASH = [t for t in E['logo_flash'] if t < 152.0]
INF = E['infinity']
AGENTS = [('Caroline', 126.39, 129.13), ('Jarvis', 129.13, 131.61),
          ('PrediBot', 131.61, 134.03), ('Iris', 134.03, 137.12)]

CREME, MARINE = '0xFCF9E6', '0x0F1A23'

inputs = ['-i', 'base.mp4']
for t in FLASH:
    inputs += ['-itsoffset', '%.3f' % t, '-i', 'fx-logoflash.mov']
for t in INF:
    inputs += ['-itsoffset', '%.3f' % t, '-i', 'fx-infinityloop.mov']

fc, cur, idx = [], '[0:v]', 1
for _ in FLASH:
    fc.append('%s[%d:v]overlay=0:0:eof_action=pass[o%d]' % (cur, idx, idx)); cur = '[o%d]' % idx; idx += 1
for _ in INF:
    fc.append('%s[%d:v]overlay=0:0:eof_action=pass[o%d]' % (cur, idx, idx)); cur = '[o%d]' % idx; idx += 1

# agent lower thirds: scrim + name, placed below the burned-in episode captions
for i, (name, a, b) in enumerate(AGENTS):
    en = "between(t,%.3f,%.3f)" % (a, b)
    fade = ("if(lt(t,%.3f),(t-%.3f)/0.25,if(gt(t,%.3f),(%.3f-t)/0.25,1))"
            % (a + 0.25, a, b - 0.25, b))
    fc.append("%sdrawbox=x=0:y=922:w=1920:h=138:color=%s@0.55:t=fill:enable='%s'[s%d]"
              % (cur, MARINE, en, i)); cur = '[s%d]' % i
    fc.append("%sdrawtext=fontfile='%s':text='%s':fontsize=64:fontcolor=%s:"
              "x=(w-text_w)/2:y=962:alpha='%s':enable='%s'[a%d]"
              % (cur, FONT, name, CREME, fade, en, i)); cur = '[a%d]' % i

fc.append('%snull[v]' % cur)
cmd = (['ffmpeg', '-y', '-v', 'error'] + inputs +
       ['-filter_complex', ';'.join(fc), '-map', '[v]', '-frames:v', '5056',
        '-c:v', 'libx264', '-preset', 'slow', '-crf', '16', '-pix_fmt', 'yuv420p',
        '-r', '30', '-video_track_timescale', '30000', 'video-track.mp4'])
print('flashes:', FLASH); print('infinity:', INF); print('agents:', [a[0] for a in AGENTS])
subprocess.run(cmd, check=True, cwd=HERE)
print('video-track.mp4 written')
