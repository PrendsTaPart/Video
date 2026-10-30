"""Incruste les vidéos de démonstration (Drive) dans frames.mp4, mixe voix + musique, écrit le MP4 final et les sous-titres.
Usage : python3 post.py <dossier des vidéos Drive>   (les fichiers sont listés dans sources.md)"""
import json, re, subprocess, sys
V = sys.argv[1].rstrip('/') + '/'
c = json.load(open('cfg.json')); dur = c['dur']
CLIPS = json.loads(re.search(r'window\.CLIPS = (\[.*?\]);', open('scenes.js').read(), re.S).group(1).replace("'", '"'))
X, Y, W, H = 74, 186, 1376, 774          # zone #stage dans la page 1920×1080
run = lambda *a: subprocess.run(['ffmpeg', '-y', '-v', 'error', *a], check=True)
inp, flt, last = ['-i', 'frames.mp4'], [], '0:v'
for k, (f, t0, t1, ss, sp) in enumerate(CLIPS):
    inp += ['-i', V + f]; ln = t1 - t0
    flt.append(f"[{k+1}:v]trim={ss}:{ss + ln * sp},setpts=(PTS-STARTPTS)/{sp}+{t0}/TB,"
               f"scale={W}:{H}:force_original_aspect_ratio=decrease,pad={W}:{H}:(ow-iw)/2:(oh-ih)/2:color=0x0f1424,"
               f"format=yuva420p,fade=t=in:st={t0}:d=0.3:alpha=1,fade=t=out:st={t1 - 0.3}:d=0.3:alpha=1[c{k}]")
    nxt = f'x{k}'; flt.append(f"[{last}][c{k}]overlay={X}:{Y}:eof_action=pass[{nxt}]"); last = nxt
flt.append(f"[{last}]format=yuv420p[v]")
run(*inp, '-filter_complex', ';'.join(flt), '-map', '[v]', '-c:v', 'libx264', '-preset', 'medium', '-crf', '19', 'frames_ov.mp4')
M = '../planit-academy/assets/audio/musique-produit.mp3'
run('-i', 'voix/voix.mp3', '-stream_loop', '-1', '-i', M, '-filter_complex',
    f"[0:a]aresample=48000,apad=whole_dur={dur}[vo];[vo]asplit[v1][v2];"
    f"[1:a]aresample=48000,atrim=0:{dur},volume=0.2,afade=t=in:d=1.5,afade=t=out:st={dur - 3}:d=3[mu];"
    "[mu][v1]sidechaincompress=threshold=0.03:ratio=8:attack=20:release=400[du];"
    "[v2][du]amix=inputs=2:normalize=0:duration=first,loudnorm=I=-14:TP=-1.5:LRA=11[a]",
    '-map', '[a]', '-t', str(dur), '-ac', '2', 'mix.wav')
run('-i', 'frames_ov.mp4', '-i', 'mix.wav', '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k',
    '-shortest', '-movflags', '+faststart', 'soutenance-rapidocrm-demo.mp4')
ts = lambda s: f"{int(s // 3600):02}:{int(s % 3600 // 60):02}:{int(s % 60):02},{int(round(s % 1 * 1000)):03}"
open('soutenance-rapidocrm-sous-titres.srt', 'w').write('\n'.join(f"{i+1}\n{ts(l['t0'])} --> {ts(l['t1'])}\n{l['txt']}\n" for i, l in enumerate(c['lines'])))
print('ok')
