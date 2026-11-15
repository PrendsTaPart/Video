"""Construit un épisode : durées des segments (calées sur les silences de la voix),
tournage synchronisé, sous-titres, cartes, montage H.264/AAC faststart, manifeste.
Usage : python3 -I build.py RHV2-01"""
import hashlib, json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ID = sys.argv[1]
OUT = os.path.join(HERE, 'out', ID)
AUDIO = os.path.join(HERE, 'audio', f'{ID}.mp3')
INTRO, OUTRO = 2.5, 3.0


def run(cmd, **kw):
    return subprocess.run(cmd, check=True, capture_output=True, text=True, cwd=HERE, **kw)


eps = json.loads(run(['node', '-e', 'const E=require("./episodes");console.log(JSON.stringify(Object.fromEntries(Object.entries(E).map(([k,v])=>[k,{...v,segments:v.segments.map(s=>s.t)}]))))']).stdout)
ep = eps[ID]
segs = ep['segments']
dur = float(run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', AUDIO]).stdout)

# Silences de la narration → frontières de segments.
err = subprocess.run(['ffmpeg', '-v', 'info', '-i', AUDIO, '-af', 'silencedetect=noise=-32dB:d=0.22', '-f', 'null', '-'], capture_output=True, text=True).stderr
starts = [float(x) for x in re.findall(r'silence_start: ([\d.]+)', err)]
ends = [float(x) for x in re.findall(r'silence_end: ([\d.]+)', err)]
mids = [(a + b) / 2 for a, b in zip(starts, ends)]
total_chars = sum(len(s) for s in segs)
bounds, acc = [], 0
for s in segs[:-1]:
    acc += len(s)
    guess = dur * acc / total_chars
    near = min(mids, key=lambda m: abs(m - guess)) if mids else guess
    bounds.append(near if abs(near - guess) < 2.0 else guess)
cuts = [0.0] + bounds + [dur]
durations = [round(max(1.5, cuts[i + 1] - cuts[i]), 3) for i in range(len(segs))]
os.makedirs(OUT, exist_ok=True)
json.dump(durations, open(os.path.join(OUT, 'durations.json'), 'w'))

if '--no-record' not in sys.argv:
    print(run(['node', 'record.js', ID, os.path.join(OUT, 'durations.json')], timeout=600).stdout.strip())
cap = json.load(open(os.path.join(OUT, 'capture.json')))
run(['node', 'cards.js', ID])

# Sous-titres : chaque segment découpé en phrases, ≤ 2 lignes, temps au prorata.
def ts(t):
    h, r = divmod(t, 3600); m, s = divmod(r, 60)
    return f'{int(h):02}:{int(m):02}:{int(s):02},{int(round((s % 1) * 1000)):03}'

srt, n = [], 1
for i, s in enumerate(segs):
    parts = [p.strip() for p in re.split(r'(?<=[.!?:])\s+', s) if p.strip()]
    chunks = []
    for p in parts:
        words, line = p.split(), ''
        for w in words:
            if len(line) + len(w) + 1 > 84 and line:
                chunks.append(line); line = w
            else:
                line = (line + ' ' + w).strip()
        chunks.append(line)
    a, b = cuts[i], cuts[i + 1]
    cl = sum(len(c) for c in chunks)
    t = a
    for c in chunks:
        d = (b - a) * len(c) / cl
        txt = c if len(c) <= 42 else c[:c.rfind(' ', 0, len(c) // 2 + 8)] + '\n' + c[c.rfind(' ', 0, len(c) // 2 + 8) + 1:]
        srt.append(f'{n}\n{ts(INTRO + t)} --> {ts(INTRO + t + d - 0.05)}\n{txt}\n'); n += 1; t += d
open(os.path.join(OUT, f'{ID}.srt'), 'w').write('\n'.join(srt))

body = dur + 0.8
total = INTRO + body + OUTRO
style = "FontName=Inter,FontSize=17,PrimaryColour=&H00FFFFFF,BackColour=&H90301A4B,BorderStyle=4,Outline=0,Shadow=0,MarginV=26"
fc = (f"[0:v]scale=1280:720,setsar=1,fps=30,format=yuv420p[i];"
      f"[1:v]trim=start={cap['offset']:.3f}:duration={body:.3f},setpts=PTS-STARTPTS,scale=1280:720,setsar=1,fps=30,format=yuv420p[m];"
      f"[2:v]scale=1280:720,setsar=1,fps=30,format=yuv420p[o];"
      f"[i][m][o]concat=n=3:v=1:a=0[v0];[v0]subtitles={ID}.srt:force_style='{style}'[v];"
      f"[3:a]adelay={int(INTRO * 1000)}|{int(INTRO * 1000)},apad,atrim=0:{total:.3f},loudnorm=I=-16:TP=-1.5:LRA=11[a]")
mp4 = os.path.join(OUT, f'tutoriel-rapido-{ID}.mp4')
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-loop', '1', '-t', str(INTRO), '-i', 'intro.png', '-i', 'capture.webm', '-loop', '1', '-t', str(OUTRO), '-i', 'outro.png', '-i', AUDIO,
     '-filter_complex', fc, '-map', '[v]', '-map', '[a]', '-c:v', 'libx264', '-preset', 'medium', '-crf', '22', '-c:a', 'aac', '-b:a', '128k', '-ar', '48000',
     '-movflags', '+faststart', '-t', f'{total:.3f}', mp4], check=True, cwd=OUT, timeout=900)
os.replace(os.path.join(OUT, 'intro.png'), os.path.join(OUT, f'tutoriel-rapido-{ID}.png'))
probe = json.loads(run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration,size:stream=codec_name,width,height', '-of', 'json', mp4]).stdout)
sha = hashlib.sha256(open(mp4, 'rb').read()).hexdigest()
m, s = divmod(round(float(probe['format']['duration'])), 60)
manifest = {
    'id': ID, 'slug': ep['slug'], 'titre': ep['titre'], 'accent': ep['accent'], 'niveau': ep['niveau'], 'description': ep['description'], 'chapitres': ep['chapitres'],
    'script': segs, 'duree': f'{m}:{s:02}', 'duree_s': float(probe['format']['duration']), 'taille_octets': int(probe['format']['size']),
    'flux': probe['streams'], 'sha256': sha, 'voix': {'fournisseur': 'ElevenLabs', 'voice_id': 'TGAegA0zNRi8I6nUdq3i', 'nom': 'Adam - Instructor', 'modele': 'eleven_v4',
    'texte_sha256': hashlib.sha256(' '.join(segs).encode()).hexdigest()}, 'segments_s': durations, 'capture': {'source': 'produit réel RapidoRH (branche V2, serveur local)', 'donnees': 'entreprise de démonstration fictive', 'erreurs': cap['errs']},
    'statut': 'produit', 'url_video': None, 'url_miniature': None,
}
json.dump(manifest, open(os.path.join(OUT, 'manifest.json'), 'w'), ensure_ascii=False, indent=1)
print(json.dumps({k: manifest[k] for k in ('id', 'duree', 'taille_octets', 'sha256')}, ensure_ascii=False), 'erreurs:', cap['errs'])
