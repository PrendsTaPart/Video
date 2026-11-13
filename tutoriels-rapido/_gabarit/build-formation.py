#!/usr/bin/env python3
"""
Génère la composition HyperFrames d'une FORMATION métier (motion design, sans capture d'écran).
Entrées : <EP>/tuto.json (paragraphs + slides), <EP>/paragraphes.json, <EP>/audio/transcript.json, <EP>/audio/voix.mp3
Types de diapositive (« slides ») : title, points, steps, compare, prompt, takeaway.
  { "at": "clé", "type": "points", "title": "…", "em": "mot", "items": ["…", "…"] }
  { "at": "clé", "type": "compare", "title": "…", "left": ["Avant", "…"], "right": ["Après", "…"] }
  { "at": "clé", "type": "prompt", "title": "…", "prompt": "…", "answer": ["…", "…"] }
Usage : python3 build-formation.py tutoriels-rapido/F21
"""
import html
import json
import os
import re
import shutil
import subprocess
import sys

EP = sys.argv[1]
cfg = json.load(open(os.path.join(EP, 'tuto.json')))
paras = json.load(open(os.path.join(EP, 'paragraphes.json')))
words = json.load(open(os.path.join(EP, cfg.get('transcript', 'audio/transcript.json'))))
G = os.path.dirname(os.path.abspath(__file__))
esc = html.escape

COLORS = {'crm': ('#4CAF50', '#9BE15D', 'RapidoCRM'), 'cms': ('#03A9F5', '#6EE7FF', 'RapidoCMS'),
          'rh': ('#7E57C2', '#C084FC', 'RapidoRH'), 'suite': ('#03A9F5', '#C084FC', 'Suite Rapido')}
A, B, PRODUCT = COLORS[cfg.get('product', 'suite')]
GRAD = 'linear-gradient(100deg,#9BE15D,#6EE7FF 50%,#C084FC)' if cfg.get('product', 'suite') == 'suite' else f'linear-gradient(100deg,{A},{B})'
INTRO, OUTRO = float(cfg.get('intro', 3.0)), float(cfg.get('outro', 4.5))
VOICE_END = float(paras['end']) + 0.4
TOTAL = round(INTRO + VOICE_END + OUTRO, 3)

# ressources dans le projet
os.makedirs(os.path.join(EP, 'assets', 'fonts'), exist_ok=True)
shutil.copy(os.path.join(G, 'vendor', 'gsap.min.js'), os.path.join(EP, 'assets', 'gsap.min.js'))
shutil.copy(os.path.join(G, 'logo_icon.png'), os.path.join(EP, 'assets', 'logo_icon.png'))
for f in os.listdir(os.path.join(G, 'vendor', 'fonts')):
    if f.endswith('.woff2'):
        shutil.copy(os.path.join(G, 'vendor', 'fonts', f), os.path.join(EP, 'assets', 'fonts', f))
FONTS = open(os.path.join(G, 'vendor', 'fonts', 'fonts.css')).read().replace('src: url(', 'src: url(assets/fonts/')
VOICE = 'assets/voix-16lufs.mp3'
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', os.path.join(EP, cfg.get('voice', 'audio/voix.mp3')), '-af', 'loudnorm=I=-16:TP=-1.5:LRA=11',
                '-ar', '44100', '-b:a', '192k', os.path.join(EP, VOICE)], check=True)

# sous-titres : texte exact du script, calé sur la transcription
sys.path.insert(0, G)
from subs import build_subs
subs = build_subs(cfg, words, INTRO)

def with_em(text, em):
    h = esc(text)
    return h.replace(esc(em), f'<em>{esc(em)}</em>') if em and em in text else h

slides = sorted(cfg['slides'], key=lambda s: float(paras[s['at']]))
for i, s in enumerate(slides):
    s['start'] = INTRO + float(paras[s['at']])
    s['end'] = INTRO + float(paras[slides[i + 1]['at']]) if i + 1 < len(slides) else INTRO + VOICE_END

body, anim = [], []
for i, s in enumerate(slides):
    sid = f'sl{i}'
    d = s['end'] - s['start']
    title = f'<h2>{with_em(s.get("title", ""), s.get("em"))}</h2>' if s.get('title') else ''
    t = s['type']
    if t == 'title':
        inner = f'<div class="kick">{esc(s.get("kicker", ""))}</div><h1>{with_em(s["title"], s.get("em"))}</h1>'
    elif t == 'points':
        inner = title + '<div class="points">' + ''.join(f'<div class="pt"><b>{n + 1}</b><span>{esc(x)}</span></div>' for n, x in enumerate(s['items'])) + '</div>'
    elif t == 'steps':
        inner = title + '<div class="steps"><i class="line"></i>' + ''.join(f'<div class="st"><b>{n + 1}</b><span>{esc(x)}</span></div>' for n, x in enumerate(s['items'])) + '</div>'
    elif t == 'compare':
        col = lambda c, k: f'<div class="col {k}"><h3>{esc(c[0])}</h3>' + ''.join(f'<p>{esc(x)}</p>' for x in c[1:]) + '</div>'
        inner = title + '<div class="cmp">' + col(s['left'], 'l') + col(s['right'], 'r') + '</div>'
    elif t == 'prompt':
        inner = title + f'<div class="chat"><div class="q"><span class="typed" data-text="{esc(s["prompt"])}"></span></div>' + \
            '<div class="a"><span class="glyph">✳</span><div>' + ''.join(f'<p>{esc(x)}</p>' for x in s.get('answer', [])) + '</div></div></div>'
    else:  # takeaway
        inner = f'<div class="take">{with_em(s["title"], s.get("em"))}</div>'
    body.append(f'  <div class="slide clip" id="{sid}" data-start="{s["start"]:.3f}" data-duration="{d + 0.5:.3f}" data-track-index="2"><div class="inner">{inner}</div></div>\n')
    st = s['start']
    anim.append(f"  tl.from('#{sid} .inner > *', {{ y: 40, opacity: 0, duration: .8, ease: 'expo.out', stagger: .12 }}, {st + 0.05:.3f});")
    n_items = len(s.get('items', [])) or (len(s.get('right', [])) - 1 if t == 'compare' else 0)
    if t in ('points', 'steps') and n_items:
        gap = min(1.6, max(0.5, (d * 0.7) / n_items))
        sel = '.pt' if t == 'points' else '.st'
        anim.append(f"  tl.from('#{sid} {sel}', {{ x: -40, opacity: 0, duration: .6, ease: 'back.out(1.6)', stagger: {gap:.2f} }}, {st + 0.6:.3f});")
        if t == 'steps':
            anim.append(f"  tl.from('#{sid} .line', {{ scaleX: 0, duration: {min(d * 0.7, n_items * gap):.2f}, ease: 'none' }}, {st + 0.6:.3f});")
    if t == 'compare':
        anim.append(f"  tl.from('#{sid} .col.l p', {{ opacity: 0, x: -30, stagger: .25, duration: .5 }}, {st + 0.6:.3f})")
        anim.append(f"    .from('#{sid} .col.r', {{ opacity: 0, scale: .94, duration: .7, ease: 'back.out(1.6)' }}, {st + d * 0.45:.3f})")
        anim.append(f"    .from('#{sid} .col.r p', {{ opacity: 0, x: 30, stagger: .25, duration: .5 }}, {st + d * 0.45 + 0.3:.3f});")
    if t == 'prompt':
        n = len(s['prompt'])
        anim.append(f"  (function(){{ const el = document.querySelector('#{sid} .typed'); const txt = el.dataset.text; const o = {{ n: 0 }};")
        anim.append(f"    tl.to(o, {{ n: txt.length, duration: {min(3.2, n * 0.035, max(1.0, d * 0.32)):.2f}, ease: 'none', onUpdate: () => {{ el.textContent = txt.slice(0, Math.round(o.n)); }} }}, {st + 0.6:.3f}); }})();")
        anim.append(f"  tl.from('#{sid} .a', {{ opacity: 0, y: 20, duration: .6, ease: 'expo.out' }}, {st + 0.8 + min(3.2, n * 0.035, max(1.0, d * 0.32)):.3f})")
        anim.append(f"    .from('#{sid} .a p', {{ opacity: 0, y: 10, stagger: .35, duration: .4 }}, {st + 1.1 + min(3.2, n * 0.035, max(1.0, d * 0.32)):.3f});")
    anim.append(f"  tl.to('#{sid} .inner', {{ opacity: 0, y: -20, duration: .35, ease: 'power2.in' }}, {s['end'] - 0.3:.3f});")

html_out = f'''<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=1920, height=1080">
<script src="assets/gsap.min.js"></script>
<style>
{FONTS}
  :root {{ --a:{A}; --b:{B}; --grad:{GRAD}; }}
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  html, body {{ width:1920px; height:1080px; overflow:hidden; background:#05060A; font-family:'Geist',sans-serif; color:#fff; }}
  .clip {{ position:absolute; inset:0; }}
  .bg {{ position:absolute; inset:0; overflow:hidden; }}
  .halo {{ position:absolute; border-radius:50%; filter:blur(130px); }}
  .h1 {{ width:900px; height:800px; right:-260px; top:-300px; background:var(--a); opacity:.42; }}
  .h2 {{ width:760px; height:640px; left:-280px; bottom:-340px; background:var(--b); opacity:.28; }}
  .grid {{ position:absolute; inset:0; background-image:linear-gradient(rgba(255,255,255,.05) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.05) 1px,transparent 1px); background-size:56px 56px; -webkit-mask-image:radial-gradient(ellipse 70% 70% at 50% 40%,#000 20%,transparent 75%); }}
  em {{ font-family:'Instrument Serif',serif; font-style:italic; font-weight:400; background:var(--grad); -webkit-background-clip:text; background-clip:text; color:transparent; padding-right:.06em; }}
  .slide .inner {{ position:absolute; inset:110px 150px 190px; display:flex; flex-direction:column; justify-content:center; }}
  .slide h1 {{ font-size:118px; line-height:.96; font-weight:800; letter-spacing:-.045em; text-wrap:balance; }}
  .slide h2 {{ font-size:86px; line-height:1; font-weight:800; letter-spacing:-.04em; margin-bottom:56px; text-wrap:balance; }}
  .kick {{ font-family:'Geist Mono',monospace; font-size:26px; letter-spacing:.16em; text-transform:uppercase; color:rgba(255,255,255,.65); margin-bottom:28px; }}
  .points {{ display:grid; grid-template-columns:1fr 1fr; gap:22px; }}
  .pt {{ display:flex; gap:22px; align-items:center; padding:26px 30px; border-radius:24px; background:rgba(255,255,255,.05); border:1px solid rgba(255,255,255,.12); font-size:40px; font-weight:500; line-height:1.25; }}
  .pt b, .st b {{ flex:none; width:62px; height:62px; border-radius:50%; display:grid; place-items:center; background:var(--grad); color:#05060A; font-family:'Geist Mono',monospace; font-size:28px; }}
  .steps {{ position:relative; display:flex; gap:28px; }}
  .steps .line {{ position:absolute; left:31px; right:31px; top:31px; height:3px; background:var(--grad); transform-origin:left; }}
  .st {{ position:relative; flex:1; display:flex; flex-direction:column; gap:22px; font-size:38px; font-weight:500; line-height:1.25; }}
  .cmp {{ display:grid; grid-template-columns:1fr 1fr; gap:30px; }}
  .col {{ padding:36px; border-radius:28px; border:1px solid rgba(255,255,255,.12); background:rgba(255,255,255,.04); }}
  .col.r {{ border-color:var(--a); background:color-mix(in srgb,var(--a) 14%,transparent); box-shadow:0 0 60px -20px var(--a); }}
  .col h3 {{ font-size:30px; font-family:'Geist Mono',monospace; letter-spacing:.12em; text-transform:uppercase; margin-bottom:22px; color:rgba(255,255,255,.7); }}
  .col.r h3 {{ color:var(--b); }}
  .col p {{ font-size:38px; line-height:1.35; margin-top:14px; }}
  .chat {{ width:1300px; border-radius:28px; background:#262624; border:1px solid rgba(255,255,255,.12); padding:36px; display:flex; flex-direction:column; gap:26px; box-shadow:0 40px 100px -30px rgba(0,0,0,.9); }}
  .chat .q {{ align-self:flex-end; max-width:85%; background:#141413; border:1px solid rgba(255,255,255,.1); border-radius:20px; padding:20px 26px; font-size:32px; line-height:1.4; min-height:84px; }}
  .chat .a {{ display:flex; gap:20px; font-size:30px; line-height:1.45; color:#f5f4ef; }}
  .chat .a p {{ margin-bottom:10px; }}
  .glyph {{ color:#d97757; font-size:36px; }}
  .take {{ font-size:96px; line-height:1.02; font-weight:800; letter-spacing:-.04em; text-align:center; text-wrap:balance; }}
  .sub {{ position:absolute; inset:auto 0 70px 0; text-align:center; z-index:6; }}
  .sub span {{ display:inline-block; padding:10px 26px; border-radius:16px; background:rgba(5,6,10,.86); font-size:40px; font-weight:700; white-space:nowrap; }}
  .bar {{ position:absolute; left:150px; right:150px; bottom:34px; height:5px; border-radius:5px; background:rgba(255,255,255,.12); overflow:hidden; z-index:6; }}
  .bar i {{ position:absolute; inset:0; background:var(--grad); transform-origin:left; transform:scaleX(0); }}
  .brand {{ position:absolute; right:60px; top:44px; display:flex; align-items:center; gap:10px; padding:10px 18px; border-radius:999px; background:rgba(10,12,18,.82); border:1px solid rgba(255,255,255,.14); font-size:22px; font-weight:600; z-index:5; }}
  .brand img {{ width:30px; }}
  .card {{ display:flex; flex-direction:column; justify-content:center; padding:0 150px; z-index:10; }}
  .card .top {{ display:flex; align-items:center; gap:20px; }}
  .num {{ font-family:'Geist Mono',monospace; font-size:32px; padding:10px 24px; border-radius:999px; background:var(--grad); color:#05060A; }}
  .card h1 {{ margin-top:40px; font-size:122px; line-height:.95; font-weight:800; letter-spacing:-.045em; max-width:1600px; text-wrap:balance; }}
  .card .logo {{ position:absolute; left:150px; bottom:90px; display:flex; align-items:center; gap:14px; font-size:30px; font-weight:600; color:rgba(255,255,255,.75); }}
  .card .logo img {{ width:48px; }}
  .card h2 {{ font-size:110px; font-weight:800; letter-spacing:-.045em; }}
  .card p {{ margin-top:30px; font-size:40px; color:rgba(255,255,255,.75); }}
</style></head>
<body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{TOTAL}" data-width="1920" data-height="1080">
  <div class="bg"><div class="halo h1"></div><div class="halo h2"></div><div class="grid"></div></div>
  <div class="brand"><img src="assets/logo_icon.png" alt="">{cfg.get('brand', 'Formation Rapido')}</div>
{''.join(body)}'''
for i, (s0, e0, t0) in enumerate(subs):
    html_out += f'  <div class="sub clip" id="s{i}" data-start="{s0:.3f}" data-duration="{max(0.2, e0 - s0):.3f}" data-track-index="7"><span>{esc(t0)}</span></div>\n'
html_out += f'''  <div class="bar"><i id="bar"></i></div>
  <audio id="voice" src="{VOICE}" data-start="{INTRO}" data-duration="{VOICE_END}" data-track-index="10" data-volume="1"></audio>
  <div class="clip card" id="intro" data-start="0" data-duration="{INTRO + 0.6}" data-track-index="8">
    <div class="bg"><div class="halo h1"></div><div class="halo h2"></div><div class="grid"></div></div>
    <div style="position:relative"><div class="top"><span class="num">{esc(cfg['id'])}</span><span class="kick" style="margin:0">{esc(cfg['kicker'])}</span></div>
    <h1>{with_em(cfg['title'], cfg.get('em'))}</h1></div>
    <div class="logo"><img src="assets/logo_icon.png" alt="">RapidoSoftware&nbsp;/&nbsp;<b style="color:#fff">{PRODUCT}</b></div>
  </div>
  <div class="clip card" id="outro" data-start="{INTRO + VOICE_END - 0.3}" data-duration="{OUTRO + 0.3}" data-track-index="9" style="align-items:center;text-align:center">
    <div class="bg"><div class="halo h1"></div><div class="halo h2"></div><div class="grid"></div></div>
    <div style="position:relative"><h2>Merci d'avoir <em>regardé</em></h2><p>{esc(cfg.get('end_cta', 'rapidosoftware.com'))}</p></div>
    <div class="logo" style="left:50%;transform:translateX(-50%)"><img src="assets/logo_icon.png" alt="">RapidoSoftware</div>
  </div>
</div>
<script>
  window.__timelines = window.__timelines || {{}};
  const tl = gsap.timeline({{ paused: true }});
  tl.from('#intro .top', {{ y: 40, opacity: 0, duration: .7, ease: 'expo.out' }}, .15)
    .from('#intro h1', {{ y: 60, opacity: 0, duration: .9, ease: 'expo.out' }}, .3)
    .to('#intro', {{ opacity: 0, duration: .6, ease: 'power2.in' }}, {INTRO});
  tl.to('#bar', {{ scaleX: 1, duration: {VOICE_END}, ease: 'none' }}, {INTRO});
{chr(10).join(anim)}
  tl.from('#outro h2', {{ y: 60, opacity: 0, duration: .9, ease: 'expo.out' }}, {INTRO + VOICE_END:.3f});
  window.__timelines['main'] = tl;
</script>
</body></html>
'''
open(os.path.join(EP, 'index.html'), 'w').write(html_out)
print(f'index.html : {TOTAL:.1f} s, {len(slides)} diapositives, {len(subs)} sous-titres')
