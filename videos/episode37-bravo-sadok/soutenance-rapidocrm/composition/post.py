"""Démo de soutenance : incrustation des vidéos RapidoCRM puis deux mixages (sans voix / avec voix)."""
import json, subprocess
V = 'ep37/src/vid/'
c = json.load(open('vd/cfg.json')); P, dur = c['P'], c['dur']
D = [P[i+1]-P[i] for i in range(len(P)-1)] + [dur-P[-1]]
clips = {1: ('dashboard__video-1 Statistiques du CRM.mp4', 0), 2: ('segment.mp4', 1), 3: ('campagne.mp4', 4), 4: ('mail.mp4', 3),
         5: ('agenda.mp4', 2), 6: ('facture.mp4', 8), 7: ('formulaire.mp4', 1), 8: ('fidelite__video-1 Créer un programme fidélité.mp4', 5),
         9: ('wf-creer__video-1 Créer un workflow.mp4', 20)}
inp, flt, last = ['-i', 'vd/frames.mp4'], [], '0:v'
for k, (i, (f, ss)) in enumerate(clips.items()):
    inp += ['-i', V + f]; t0 = P[i] + 0.3; ln = D[i] - 0.6
    flt.append(f"[{k+1}:v]trim={ss}:{ss+ln},setpts=PTS-STARTPTS+{t0}/TB,scale=1300:690:force_original_aspect_ratio=decrease,"
               f"pad=1300:690:(ow-iw)/2:(oh-ih)/2:color=0x0e1116,format=yuva420p,fade=t=in:st={t0}:d=0.4:alpha=1[c{k}]")
    nxt = f'x{k}'; flt.append(f"[{last}][c{k}]overlay=110:220:eof_action=pass[{nxt}]"); last = nxt
flt.append(f"[{last}]format=yuv420p[v]")
run = lambda *a: subprocess.run(['ffmpeg', '-y', '-v', 'error', *a], check=True)
run(*inp, '-filter_complex', ';'.join(flt), '-map', '[v]', '-c:v', 'libx264', '-preset', 'medium', '-crf', '19', 'vd/frames_ov.mp4')
M = '/home/user/Video/videos/planit-academy/assets/audio/musique-produit.mp3'
run('-stream_loop', '6', '-i', M, '-t', str(dur), '-ar', '48000', '-ac', '2', 'vd/bed.wav')
# 1. Sans voix : musique seule.
run('-i', 'vd/frames_ov.mp4', '-i', 'vd/bed.wav', '-filter_complex',
    f"[1:a]volume=0.55,afade=t=in:d=1.5,afade=t=out:st={dur-3}:d=3,loudnorm=I=-16:TP=-1.5[a]",
    '-map', '0:v', '-map', '[a]', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-shortest', '-movflags', '+faststart', 'vd/rapidocrm-demo-sans-voix.mp4')
# 2. Avec voix : extraits de la voix off placés sur les scènes correspondantes.
segs = [(0.0, 10.6, 0, 0.8), (76.1, 85.0, 2, 1.0), (85.3, 96.6, 10, 1.0), (54.94, 66.9, 11, 1.5), (96.96, 106.5, 12, 1.0), (106.7, 110.7, 9, 2.0), (134.96, 136.0, 13, 1.0)]
f2 = []
for j, (a, b, sc, off) in enumerate(segs):
    ms = int((P[sc] + off) * 1000)
    f2.append(f"[0:a]atrim={a}:{b},asetpts=PTS-STARTPTS,adelay={ms}|{ms}[v{j}]")
f2.append(''.join(f'[v{j}]' for j in range(len(segs))) + f"amix=inputs={len(segs)}:normalize=0,apad=whole_dur={dur}[vo]")
f2.append('[vo]asplit[vo1][vo2]')
f2.append(f"[1:a]volume=0.35,afade=t=in:d=1.5,afade=t=out:st={dur-3}:d=3[mu]")
f2.append('[mu][vo1]sidechaincompress=threshold=0.03:ratio=8:attack=20:release=400[duck]')
f2.append('[vo2][duck]amix=inputs=2:normalize=0:duration=first,loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000[out]')
run('-i', 'vs/vo.mp3', '-i', 'vd/bed.wav', '-filter_complex', ';'.join(f2), '-map', '[out]', '-t', str(dur), 'vd/mix_voix.wav')
run('-i', 'vd/frames_ov.mp4', '-i', 'vd/mix_voix.wav', '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-shortest', '-movflags', '+faststart', 'vd/rapidocrm-demo-avec-voix.mp4')
print('ok')
