#!/usr/bin/env python3
"""
Génère la composition HyperFrames (index.html) d'un tutoriel Rapido à partir de :
  <episode>/tuto.json                 configuration (titre, chapitres, zones à zoomer…)
  <episode>/paragraphes.json          débuts de paragraphe de la voix (s)
  <episode>/audio/transcript.json     transcription mot à mot (npx hyperframes transcribe)
  <episode>/captures/ecran.mp4        capture Playwright recalée (t=0 = début de la voix)
Usage : python3 build-tutoriel.py tutoriels-rapido/CRM02
Puis : cd tutoriels-rapido/CRM02 && npx hyperframes render --output ../../videos/tutoriels-rapido/CRM02.mp4
"""
import html
import json
import os
import re
import sys

EP = sys.argv[1]
cfg = json.load(open(os.path.join(EP, 'tuto.json')))
paras = json.load(open(os.path.join(EP, 'paragraphes.json')))
words = json.load(open(os.path.join(EP, cfg['transcript'])))

COLORS = {
    'crm': ('#4CAF50', '#9BE15D', 'RapidoCRM'),
    'cms': ('#03A9F5', '#6EE7FF', 'RapidoCMS'),
    'rh': ('#7E57C2', '#C084FC', 'RapidoRH'),
    'suite': ('#03A9F5', '#C084FC', 'Suite Rapido'),
}
A, B, PRODUCT = COLORS[cfg['product']]
INTRO = float(cfg.get('intro', 3.0))
OUTRO = float(cfg.get('outro', 4.5))
VOICE_END = float(paras['end']) + 0.4
TOTAL = round(INTRO + VOICE_END + OUTRO, 3)
W, H = 1920, 1080
FX, FY, FW, FH = 80, 56, 1760, 990          # cadre de l'écran filmé
K = FW / 1920                                 # échelle capture → cadre

esc = html.escape

# Copie des ressources partagées DANS le projet (le rendu ignore les fichiers hors du dossier)
import shutil
G = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(EP, 'assets', 'fonts'), exist_ok=True)
shutil.copy(os.path.join(G, 'vendor', 'gsap.min.js'), os.path.join(EP, 'assets', 'gsap.min.js'))
shutil.copy(os.path.join(G, 'logo_icon.png'), os.path.join(EP, 'assets', 'logo_icon.png'))
for f in os.listdir(os.path.join(G, 'vendor', 'fonts')):
    if f.endswith('.woff2'):
        shutil.copy(os.path.join(G, 'vendor', 'fonts', f), os.path.join(EP, 'assets', 'fonts', f))
# Voix normalisée à -16 LUFS (norme YouTube / podcasts), copiée dans assets/
import subprocess
VOICE_SRC = os.path.join(EP, cfg['voice'])
VOICE = 'assets/voix-16lufs.mp3'
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', VOICE_SRC, '-af', 'loudnorm=I=-16:TP=-1.5:LRA=11', '-ar', '44100', '-b:a', '192k', os.path.join(EP, VOICE)], check=True)
FONTS = open(os.path.join(G, 'vendor', 'fonts', 'fonts.css')).read().replace('src: url(', 'src: url(assets/fonts/')

# ---------------------------------------------------------------- sous-titres
def fix(text):
    for a, b in cfg.get('fixes', {}).items():
        text = text.replace(a, b)
    return text

chunks, cur = [], []
for i, w in enumerate(words):
    cur.append(w)
    t = w['text']
    nxt = words[i + 1] if i + 1 < len(words) else None
    gap = (nxt['start'] - w['end']) if nxt else 9
    end_punct = re.search(r'[.!?…:;,]$', t)
    sentence_end = re.search(r'[.!?…]$', t)
    nxt_closes = nxt is not None and re.search(r'[.!?…,]$', nxt['text'])
    if sentence_end and len(cur) == 1 and chunks and len(chunks[-1]) < 7:
        chunks[-1].append(w)          # mot orphelin de fin de phrase : on le raccroche au bloc précédent
        cur = []
        continue
    full = len(cur) >= 6 and not (len(cur) < 7 and nxt_closes)
    if full or (len(cur) >= 2 and (end_punct or gap > 0.35)) or nxt is None:
        chunks.append(cur)
        cur = []
if cur:
    chunks.append(cur)

subs = []
for c in chunks:
    text = fix(' '.join(x['text'] for x in c)).strip()
    text = re.sub(r'[.!?]+$', '', text).strip()          # jamais de point final
    start = INTRO + c[0]['start']
    end = INTRO + c[-1]['end'] + 0.12
    subs.append((start, end, text))
# pas de chevauchement
for i in range(len(subs) - 1):
    if subs[i][1] > subs[i + 1][0]:
        subs[i] = (subs[i][0], subs[i + 1][0] - 0.02, subs[i][2])

# ---------------------------------------------------------------- chapitres
chapters = []
for i, ch in enumerate(cfg['chapters']):
    start = INTRO + float(paras[ch['at']])
    nxt = INTRO + float(paras[cfg['chapters'][i + 1]['at']]) if i + 1 < len(cfg['chapters']) else INTRO + float(paras.get('outro', paras['end']))
    chapters.append(dict(ch, start=start, end=nxt, n=i + 1))

def cam_for(zone, zoom):
    x, y, w, h = zone
    cx, cy = (x + w / 2) * K, (y + h / 2) * K
    tx = min(0, max(FW - FW * zoom, FW / 2 - cx * zoom))
    ty = min(0, max(FH - FH * zoom, FH / 2 - cy * zoom))
    return round(tx, 1), round(ty, 1)

title_html = esc(cfg['title'])
if cfg.get('em') and cfg['em'] in cfg['title']:
    title_html = title_html.replace(esc(cfg['em']), f"<em>{esc(cfg['em'])}</em>")

# ---------------------------------------------------------------- HTML
parts = []
add = parts.append
add(f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width={W}, height={H}">
<script src="assets/gsap.min.js"></script>
<style>
{FONTS}
  :root {{ --a:{A}; --b:{B}; --grad:linear-gradient(100deg,{A},{B}); }}
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  html, body {{ width:{W}px; height:{H}px; overflow:hidden; background:#05060A; font-family:'Geist',sans-serif; color:#fff; }}
  .clip {{ position:absolute; inset:0; }}
  .bg {{ position:absolute; inset:0; background:#05060A; overflow:hidden; }}
  .halo {{ position:absolute; border-radius:50%; filter:blur(120px); }}
  .h1 {{ width:900px; height:800px; right:-260px; top:-300px; background:var(--a); opacity:.45; }}
  .h2 {{ width:700px; height:600px; left:-260px; bottom:-320px; background:var(--b); opacity:.28; }}
  .grid {{ position:absolute; inset:0; background-image:linear-gradient(rgba(255,255,255,.05) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.05) 1px,transparent 1px); background-size:56px 56px; -webkit-mask-image:radial-gradient(ellipse 70% 70% at 50% 40%,#000 20%,transparent 75%); }}
  #frame {{ position:absolute; left:{FX}px; top:{FY}px; width:{FW}px; height:{FH}px; border-radius:22px; overflow:hidden; background:#f3f4f7;
           box-shadow:0 50px 120px -30px rgba(0,0,0,.9),0 0 0 1px rgba(255,255,255,.12),0 0 120px -30px var(--a); }}
  #cam {{ position:absolute; left:0; top:0; width:{FW}px; height:{FH}px; transform-origin:0 0; }}
  #cam video {{ position:absolute; inset:0; width:100%; height:100%; object-fit:cover; }}
  .hl {{ position:absolute; border-radius:18px; border:3px solid var(--a); box-shadow:0 0 0 9999px rgba(5,6,10,.28),0 0 40px -6px var(--a); opacity:0; }}
  .chap {{ position:absolute; left:{FX + 28}px; top:{FY + 26}px; display:flex; align-items:center; gap:14px; padding:12px 22px 12px 12px; border-radius:999px;
          background:rgba(10,12,18,.82); backdrop-filter:blur(12px); border:1px solid rgba(255,255,255,.14); font-size:26px; font-weight:600; opacity:0; z-index:5; }}
  .chap b {{ width:40px; height:40px; border-radius:50%; display:grid; place-items:center; background:var(--grad); color:#05060A; font-family:'Geist Mono',monospace; font-size:19px; }}
  .sub {{ position:absolute; inset:auto 0 58px 0; text-align:center; z-index:6; }}
  .sub span {{ display:inline-block; padding:10px 26px; border-radius:16px; background:rgba(5,6,10,.86); font-size:40px; font-weight:700; letter-spacing:-.01em; white-space:nowrap; box-shadow:0 10px 30px rgba(0,0,0,.4); }}
  .bar {{ position:absolute; left:{FX}px; bottom:22px; width:{FW}px; height:5px; border-radius:5px; background:rgba(255,255,255,.12); overflow:hidden; z-index:6; }}
  .bar i {{ position:absolute; inset:0; background:var(--grad); transform-origin:left; transform:scaleX(0); }}
  .brand {{ position:absolute; right:{FX + 24}px; top:{FY + 28}px; display:flex; align-items:center; gap:10px; padding:10px 18px; border-radius:999px; background:rgba(10,12,18,.82); border:1px solid rgba(255,255,255,.14); font-size:22px; font-weight:600; z-index:5; }}
  .brand img {{ width:30px; }}
  /* intro / outro */
  .card {{ display:flex; flex-direction:column; justify-content:center; padding:0 150px; z-index:10; }}
  .card .top {{ display:flex; align-items:center; gap:20px; }}
  .num {{ font-family:'Geist Mono',monospace; font-size:32px; padding:10px 24px; border-radius:999px; background:var(--grad); color:#05060A; }}
  .kick {{ font-size:28px; font-weight:600; letter-spacing:.18em; text-transform:uppercase; color:rgba(255,255,255,.7); }}
  .card h1 {{ text-wrap:balance; margin-top:40px; font-size:128px; line-height:.95; font-weight:800; letter-spacing:-.045em; max-width:1500px; }}
  .card h1 em, .card h2 em {{ font-family:'Instrument Serif',serif; font-style:italic; font-weight:400; background:var(--grad); -webkit-background-clip:text; background-clip:text; color:transparent; padding-right:.06em; }}
  .card .logo {{ position:absolute; left:150px; bottom:90px; display:flex; align-items:center; gap:14px; font-size:30px; font-weight:600; color:rgba(255,255,255,.75); }}
  .card .logo img {{ width:48px; }}
  .card h2 {{ font-size:110px; line-height:1; font-weight:800; letter-spacing:-.045em; }}
  .card p {{ margin-top:30px; font-size:40px; color:rgba(255,255,255,.75); }}
</style>
</head>
<body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{TOTAL}" data-width="{W}" data-height="{H}">
  <div class="bg"><div class="halo h1"></div><div class="halo h2"></div><div class="grid"></div></div>

  <div id="frame">
    <div id="cam">
      <video id="cap" class="clip" src="{cfg['capture']}" muted data-start="{INTRO}" data-duration="{round(VOICE_END + OUTRO, 3)}" data-track-index="1"></video>
''')
for ch in chapters:
    x, y, w, h = ch['zone']
    add(f'      <div class="hl" id="hl{ch["n"]}" style="left:{x*K:.0f}px;top:{y*K:.0f}px;width:{w*K:.0f}px;height:{h*K:.0f}px"></div>\n')
add('''    </div>
  </div>
  <div class="brand"><img src="assets/logo_icon.png" alt="">''' + PRODUCT + '''</div>
''')
for ch in chapters:
    add(f'  <div class="chap" id="ch{ch["n"]}"><b>{ch["n"]}</b>{esc(ch["label"])}</div>\n')
for i, (s, e, t) in enumerate(subs):
    add(f'  <div class="sub clip" id="s{i}" data-start="{s:.3f}" data-duration="{max(0.2, e - s):.3f}" data-track-index="7"><span>{esc(t)}</span></div>\n')
add(f'''  <div class="bar"><i id="bar"></i></div>
  <audio id="voice" src="{VOICE}" data-start="{INTRO}" data-duration="{VOICE_END}" data-track-index="10" data-volume="1"></audio>

  <div class="clip card" id="intro" data-start="0" data-duration="{INTRO + 0.6}" data-track-index="8">
    <div class="bg"><div class="halo h1"></div><div class="halo h2"></div><div class="grid"></div></div>
    <div style="position:relative">
      <div class="top"><span class="num">{esc(cfg['id'])}</span><span class="kick">{esc(cfg['kicker'])}</span></div>
      <h1>{title_html}</h1>
    </div>
    <div class="logo"><img src="assets/logo_icon.png" alt="">RapidoSoftware&nbsp;/&nbsp;<b style="color:#fff">{PRODUCT}</b></div>
  </div>

  <div class="clip card" id="outro" data-start="{INTRO + VOICE_END - 0.3}" data-duration="{OUTRO + 0.3}" data-track-index="9" style="align-items:center;text-align:center">
    <div class="bg"><div class="halo h1"></div><div class="halo h2"></div><div class="grid"></div></div>
    <div style="position:relative">
      <h2>Merci d'avoir <em>regardé</em></h2>
      <p>{esc(cfg.get('end_cta', 'rapidosoftware.com'))}</p>
    </div>
    <div class="logo" style="left:50%;transform:translateX(-50%)"><img src="assets/logo_icon.png" alt="">RapidoSoftware&nbsp;/&nbsp;<b style="color:#fff">{PRODUCT}</b></div>
  </div>
</div>
<script>
  window.__timelines = window.__timelines || {{}};
  const tl = gsap.timeline({{ paused: true }});
  // Intro
  tl.from('#intro .top', {{ y: 40, opacity: 0, duration: .7, ease: 'expo.out' }}, .15)
    .from('#intro h1', {{ y: 60, opacity: 0, duration: .9, ease: 'expo.out' }}, .3)
    .from('#intro .logo', {{ opacity: 0, duration: .6 }}, .6)
    .to('#intro', {{ opacity: 0, scale: 1.04, duration: .6, ease: 'power2.in' }}, {INTRO})
    .from('#frame', {{ scale: .92, opacity: 0, duration: .9, ease: 'expo.out' }}, {INTRO - .2});
  // Progression
  tl.to('#bar', {{ scaleX: 1, duration: {VOICE_END}, ease: 'none' }}, {INTRO});
''')
for ch in chapters:
    tx, ty = cam_for(ch['zone'], ch['zoom'])
    d = ch['end'] - ch['start']
    add(f"  tl.to('#cam', {{ scale: {ch['zoom']}, x: {tx}, y: {ty}, duration: 1.2, ease: 'power3.inOut' }}, {ch['start']:.3f})\n")
    add(f"    .fromTo('#hl{ch['n']}', {{ opacity: 0, scale: .97 }}, {{ opacity: 1, scale: 1, duration: .5, ease: 'back.out(2)' }}, {ch['start'] + 0.8:.3f})\n")
    add(f"    .to('#hl{ch['n']}', {{ opacity: 0, duration: .35 }}, {ch['end'] - 0.2:.3f})\n")
    add(f"    .fromTo('#ch{ch['n']}', {{ opacity: 0, x: -30 }}, {{ opacity: 1, x: 0, duration: .5, ease: 'expo.out' }}, {ch['start'] + 0.2:.3f})\n")
    add(f"    .to('#ch{ch['n']}', {{ opacity: 0, x: -20, duration: .3 }}, {ch['end'] - 0.25:.3f});\n")
last_end = chapters[-1]['end'] if chapters else INTRO
add(f"  tl.to('#cam', {{ scale: 1, x: 0, y: 0, duration: 1.2, ease: 'power3.inOut' }}, {last_end:.3f});\n")
add(f"""  // Outro
  tl.from('#outro h2', {{ y: 60, opacity: 0, duration: .9, ease: 'expo.out' }}, {INTRO + VOICE_END:.3f})
    .from('#outro p', {{ y: 30, opacity: 0, duration: .7, ease: 'expo.out' }}, {INTRO + VOICE_END + 0.25:.3f});
  window.__timelines['main'] = tl;
</script>
</body>
</html>
""")
open(os.path.join(EP, 'index.html'), 'w').write(''.join(parts))
print(f'index.html : {TOTAL:.1f} s, {len(chapters)} chapitres, {len(subs)} sous-titres')
