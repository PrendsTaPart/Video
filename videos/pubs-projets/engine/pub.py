# Moteur des épisodes « Mes 30 projets en publicité » (HyperFrames, 1080x1920).
# Usage : python3 pub.py <dossier épisode>   (lit spec.json + cfg.json, écrit index.html)
# Une scène par ligne du script, calée sur la voix (cfg.json de build_cfg.py).
import json, sys, os, html

D = sys.argv[1]
S = json.load(open(os.path.join(D, "spec.json")))
C = json.load(open(os.path.join(D, "cfg.json")))
W = C["words"]
NL = max(w[2] for w in W) + 1
T0 = [min(w[1] for w in W if w[2] == l) for l in range(NL)]
DUR = round(C["dur"] + 1.2, 2)
T1 = T0[1:] + [DUR]
th = S["theme"]
BG, BG2, ACC, ACC2 = th["bg"], th.get("bg2", "#05080d"), th["accent"], th.get("accent2", "#FFA500")
KW = set(k.lower() for k in S.get("kw", []))


def esc(s):
    return html.escape(s, quote=False)


def mark(s):  # *mot* -> surligné
    out, on = "", False
    for part in s.split("*"):
        out += (f"<mark>{esc(part)}</mark>" if on else esc(part))
        on = not on
    return out


clips, anims = [], []
track = [10]


def clip(cid, start, dur, inner, cls=""):
    track[0] += 1
    clips.append(f'<div id="{cid}" class="clip {cls}" data-start="{start:.2f}" data-duration="{dur:.2f}" data-track-index="{track[0]}">{inner}</div>')


def A(js):
    anims.append(js)


for i, sc in enumerate(S["scenes"]):
    a, b = T0[i], T1[i]
    span = sc.get("span", 1)  # une scène peut couvrir plusieurs lignes
    if span == 0:
        continue
    b = T1[i + span - 1]
    d = b - a
    sid = f"s{i}"
    t = sc["t"]
    if t == "hook":
        inner = f'''<div class="hookt">{mark(sc["text"])}</div><img class="mock" id="{sid}m" src="assets/{sc["img"]}" />'''
        clip(sid, a, d, inner, "scene")
        A(f'tl.fromTo("#{sid} .hookt", {{y: 60, opacity: 0}}, {{y: 0, opacity: 1, duration: .5, ease: E}}, {a + .05:.2f});')
        A(f'tl.fromTo("#{sid}m", {{y: 700, rotationX: 35, rotationY: -20, opacity: 0}}, {{y: 0, rotationX: 0, rotationY: 0, opacity: 1, duration: 1.0, ease: E}}, {a + .25:.2f});')
        A(f'tl.to("#{sid}m", {{rotationY: 8, y: -20, duration: {d:.2f}, ease: "sine.inOut"}}, {a + 1.25:.2f});')
    elif t == "photo":
        chips = "".join(f'<div class="ko" id="{sid}k{j}">✗ {esc(x)}</div>' for j, x in enumerate(sc.get("ko", [])))
        inner = f'''<div class="photo"><img id="{sid}p" src="assets/{sc["img"]}" /></div><div class="shade"></div>
        <div class="slam" id="{sid}w">{esc(sc["word"])}</div><div class="kos">{chips}</div><div class="ia">{esc(sc.get("tag", ""))}</div>'''
        clip(sid, a, d, inner, "scene")
        A(f'tl.fromTo("#{sid}p", {{scale: 1.0, xPercent: {sc.get("pan", -18)}}}, {{scale: 1.08, xPercent: {sc.get("pan2", -30)}, duration: {d:.2f}, ease: "none"}}, {a:.2f});')
        A(f'tl.fromTo("#{sid}w", {{scale: 2.2, opacity: 0}}, {{scale: 1, opacity: 1, duration: .35, ease: "back.out(2)"}}, {a + .3:.2f});')
        for j, _ in enumerate(sc.get("ko", [])):
            tt = T0[i + 1] + .2 + j * .55 if span > 1 else a + .8 + j * .5
            A(f'tl.fromTo("#{sid}k{j}", {{x: -500, opacity: 0}}, {{x: 0, opacity: 1, duration: .4, ease: E}}, {tt:.2f});')
    elif t == "reveal":
        inner = f'''<div class="flash" id="{sid}f"></div><div class="rlogo" id="{sid}l"><img src="assets/{sc["logo"]}" /></div>
        <div class="rname" id="{sid}n">{esc(sc["nom"])}</div><img class="mock small" id="{sid}m" src="assets/{sc["img"]}" />'''
        clip(sid, a, d, inner, "scene reveal")
        A(f'tl.fromTo("#{sid}f", {{opacity: .9}}, {{opacity: 0, duration: .45}}, {a:.2f});')
        A(f'tl.fromTo("#{sid}l", {{scale: .3, opacity: 0}}, {{scale: 1, opacity: 1, duration: .55, ease: "back.out(1.8)"}}, {a + .1:.2f});')
        A(f'tl.fromTo("#{sid}n", {{y: 40, opacity: 0}}, {{y: 0, opacity: 1, duration: .45, ease: E}}, {a + .35:.2f});')
        A(f'tl.fromTo("#{sid}m", {{rotationY: -180, scale: .6, opacity: 0}}, {{rotationY: 0, scale: 1, opacity: 1, duration: 1.0, ease: E}}, {a + .3:.2f});')
    elif t == "feature":
        scr = f'<div class="shot" id="{sid}s"><img src="assets/{sc["screen"]}" /></div>' if sc.get("screen") else (f'<img class="mock feat" id="{sid}s" src="assets/{sc["mock"]}" />' if sc.get("mock") else "")
        inner = f'''<img class="icon" id="{sid}i" src="assets/{sc["icon"]}" /><div class="word" id="{sid}w">{mark(sc["word"])}</div>{scr}'''
        clip(sid, a, d, inner, "scene")
        A(f'tl.fromTo("#{sid}i", {{scale: 0, rotation: -25}}, {{scale: 1, rotation: 0, duration: .5, ease: "back.out(2)"}}, {a + .05:.2f});')
        A(f'tl.fromTo("#{sid}w", {{y: 40, opacity: 0}}, {{y: 0, opacity: 1, duration: .4, ease: E}}, {a + .25:.2f});')
        if scr:
            A(f'tl.fromTo("#{sid}s", {{y: 300, rotationX: 40, opacity: 0}}, {{y: 0, rotationX: 12, opacity: 1, duration: .8, ease: E}}, {a + .4:.2f});')
            A(f'tl.to("#{sid}s", {{rotationX: 0, scale: 1.04, duration: {max(d - 1.2, .5):.2f}, ease: "sine.inOut"}}, {a + 1.2:.2f});')
    elif t == "card":
        inner = f'''<div class="card" id="{sid}c"><img src="assets/{sc["img"]}" /></div><div class="word low" id="{sid}w">{mark(sc["word"])}</div>'''
        clip(sid, a, d, inner, "scene")
        A(f'tl.fromTo("#{sid}c", {{rotationY: 70, opacity: 0, scale: .8}}, {{rotationY: 0, opacity: 1, scale: 1, duration: .8, ease: E}}, {a + .05:.2f});')
        A(f'tl.fromTo("#{sid}w", {{y: 40, opacity: 0}}, {{y: 0, opacity: 1, duration: .4, ease: E}}, {a + .5:.2f});')
    elif t == "cta":
        inner = f'''<div class="ctal" id="{sid}l"><img src="assets/{sc["logo"]}" /></div><div class="ctat" id="{sid}t">{mark(sc["word"])}</div>
        <div class="btn" id="{sid}b">{esc(sc["btn"])}</div><div class="url" id="{sid}u">{esc(sc["url"])}</div>'''
        clip(sid, a, d, inner, "scene reveal")
        A(f'tl.fromTo("#{sid}l", {{y: -60, opacity: 0}}, {{y: 0, opacity: 1, duration: .5, ease: E}}, {a + .05:.2f});')
        A(f'tl.fromTo("#{sid}t", {{scale: .7, opacity: 0}}, {{scale: 1, opacity: 1, duration: .5, ease: "back.out(1.8)"}}, {a + .25:.2f});')
        A(f'tl.fromTo("#{sid}b", {{y: 60, opacity: 0}}, {{y: 0, opacity: 1, duration: .45, ease: E}}, {a + .6:.2f});')
        A(f'tl.to("#{sid}b", {{scale: 1.06, duration: .45, ease: "sine.inOut", yoyo: true, repeat: {int(max(d - 1.2, 1) / .45) | 1}}}, {a + 1.1:.2f});')
        A(f'tl.fromTo("#{sid}u", {{opacity: 0}}, {{opacity: 1, duration: .4}}, {a + .9:.2f});')
    elif t == "wall":
        imgs = "".join(f'<div class="tile" id="{sid}t{j}"><img src="assets/{x}" /></div>' for j, x in enumerate(sc["imgs"]))
        inner = f'''<div class="wallt" id="{sid}h">{mark(sc["text"])}</div><div class="wall">{imgs}</div>'''
        clip(sid, a, d, inner, "scene")
        A(f'tl.fromTo("#{sid}h", {{y: 50, opacity: 0}}, {{y: 0, opacity: 1, duration: .45, ease: E}}, {a + .05:.2f});')
        for j, _ in enumerate(sc["imgs"]):
            A(f'tl.fromTo("#{sid}t{j}", {{scale: 0, opacity: 0, rotationY: 90}}, {{scale: 1, opacity: 1, rotationY: 0, duration: .45, ease: "back.out(1.6)"}}, {a + .2 + j * min(.08, (d - .8) / max(len(sc["imgs"]), 1)):.2f});')
    elif t == "chips":
        items = "".join(f'<div class="chip" id="{sid}c{j}"><b>{j + 1}</b>{esc(x)}</div>' for j, x in enumerate(sc["items"]))
        inner = f'''<div class="wallt" id="{sid}h">{mark(sc["text"])}</div><div class="chips">{items}</div>'''
        clip(sid, a, d, inner, "scene")
        A(f'tl.fromTo("#{sid}h", {{y: 50, opacity: 0}}, {{y: 0, opacity: 1, duration: .45, ease: E}}, {a + .05:.2f});')
        for j, _ in enumerate(sc["items"]):
            A(f'tl.fromTo("#{sid}c{j}", {{x: -500, opacity: 0}}, {{x: 0, opacity: 1, duration: .4, ease: E}}, {a + .35 + j * .45:.2f});')

# Sous-titres karaoké : la ligne en cours, chaque mot s'allume quand il est dit
for l in range(NL):
    ws = [w for w in W if w[2] == l]
    spans = "".join(f'<span class="kw{" hot" if w[0].strip(".,:;!?…«»").lower() in KW else ""}" id="w{l}_{k}">{esc(w[0])} </span>' for k, w in enumerate(ws))
    a, b = T0[l], T1[l]
    track[0] += 1
    clips.append(f'<div id="sub{l}" class="clip sub" data-start="{a:.2f}" data-duration="{b - a:.2f}" data-track-index="{track[0]}"><div class="subin">{spans}</div></div>')
    for k, w in enumerate(ws):
        A(f'tl.fromTo("#w{l}_{k}", {{opacity: .35}}, {{opacity: 1, duration: .08}}, {w[1]:.2f});')

# Avatar 3D : présentateur sur certaines scènes
av = S.get("avatar", {})
poses = sorted(av.items(), key=lambda x: int(x[0]))
if poses:
    imgs = "".join(f'<img id="av{k}" src="assets/avatar-{p}.png" />' for k, p in poses)
    clips.append(f'<div id="avatar" class="clip" data-start="0" data-duration="{DUR:.2f}" data-track-index="90" data-layout-allow-overflow><div id="av">{imgs}</div></div>')
    shown = None
    for idx, (k, p) in enumerate(poses):
        k = int(k)
        a = T0[k]
        nxt = T0[int(poses[idx + 1][0])] if idx + 1 < len(poses) else DUR
        endk = T1[k]
        A(f'gsap.set("#av{k}", {{opacity: 0}});')
        A(f'tl.fromTo("#av{k}", {{opacity: 0, y: 260}}, {{opacity: 1, y: 0, duration: .5, ease: "back.out(1.5)"}}, {a + .15:.2f});')
        A(f'tl.to("#av{k}", {{opacity: 0, y: 260, duration: .35, ease: "power2.in"}}, {min(endk, nxt) - .35:.2f});')

voice = f'<audio id="voix" src="voix/voix.mp3" data-start="0.35" data-duration="{C["dur"] - .35:.2f}" data-track-index="95" data-volume="1"></audio>'
music = f'<audio id="musique" src="assets/musique.mp3" data-start="0" data-duration="{DUR:.2f}" data-track-index="96" data-volume="0.12"></audio>' if S.get("music", True) else ""

css = f"""
:root {{ --bg: {BG}; --bg2: {BG2}; --acc: {ACC}; --acc2: {ACC2}; }}
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
html, body {{ width: 1080px; height: 1920px; overflow: hidden; background: var(--bg2); }}
#root {{ position: relative; width: 1080px; height: 1920px; overflow: hidden; font-family: Poppins, sans-serif; color: #fff; perspective: 1600px; }}
.clip {{ position: absolute; inset: 0; }}
#bg {{ background: radial-gradient(ellipse at 50% 35%, color-mix(in srgb, var(--acc) 35%, var(--bg)) 0%, var(--bg) 45%, var(--bg2) 100%); }}
.scene {{ transform-style: preserve-3d; }}
mark {{ background: var(--acc2); color: #0b1520; border-radius: 16px; padding: 0 16px; }}
.hookt {{ position: absolute; left: 70px; right: 70px; top: 230px; font-size: 92px; font-weight: 800; line-height: 1.08; letter-spacing: -2px; text-align: center; text-shadow: 0 8px 30px rgba(0,0,0,.6); }}
.mock {{ position: absolute; left: 240px; top: 640px; width: 600px; height: 1067px; object-fit: contain; object-position: top; filter: drop-shadow(0 40px 60px rgba(0,0,0,.6)); }}
.mock.small {{ left: 290px; top: 760px; width: 500px; height: 889px; }}
.mock.feat {{ left: 290px; top: 760px; width: 500px; height: 889px; }}
.photo {{ position: absolute; inset: 0; overflow: hidden; }}
.photo img {{ position: absolute; top: 0; left: 50%; height: 100%; width: auto; transform-origin: 50% 50%; }}
.shade {{ position: absolute; inset: 0; background: linear-gradient(180deg, rgba(0,0,0,.55) 0%, rgba(0,0,0,.05) 35%, rgba(0,0,0,.25) 60%, rgba(0,0,0,.85) 100%); }}
.slam {{ position: absolute; left: 0; right: 0; top: 300px; text-align: center; font-size: 104px; font-weight: 900; letter-spacing: -2px; color: #fff; text-shadow: 0 10px 40px rgba(0,0,0,.8); }}
.kos {{ position: absolute; left: 90px; right: 90px; top: 1050px; display: flex; flex-direction: column; gap: 26px; }}
.ko {{ background: rgba(229,57,53,.92); border-radius: 26px; padding: 26px 34px; font-size: 50px; font-weight: 800; box-shadow: 0 20px 40px rgba(0,0,0,.45); }}
.ia {{ position: absolute; right: 30px; top: 160px; font-size: 24px; font-weight: 600; color: rgba(255,255,255,.75); background: rgba(0,0,0,.45); border-radius: 99px; padding: 6px 16px; }}
.reveal {{ background: radial-gradient(circle at 50% 30%, color-mix(in srgb, var(--acc) 55%, var(--bg)) 0%, var(--bg) 60%); }}
.flash {{ position: absolute; inset: 0; background: #fff; }}
.rlogo {{ position: absolute; left: 50%; top: 250px; width: 300px; height: 300px; margin-left: -150px; border-radius: 60px; overflow: hidden; background: #fff; box-shadow: 0 30px 70px rgba(0,0,0,.5); }}
.rlogo img {{ width: 100%; height: 100%; object-fit: contain; padding: 36px; }}
.rname {{ position: absolute; left: 0; right: 0; top: 600px; text-align: center; font-size: 82px; font-weight: 800; letter-spacing: -1.5px; }}
.icon {{ position: absolute; left: 50%; top: 240px; width: 240px; height: 240px; margin-left: -120px; }}
.word {{ position: absolute; left: 60px; right: 60px; top: 520px; text-align: center; font-size: 84px; font-weight: 800; line-height: 1.1; letter-spacing: -1.5px; }}
.word.low {{ top: 1230px; }}
.shot {{ position: absolute; left: 60px; right: 60px; top: 820px; border-radius: 30px; overflow: hidden; box-shadow: 0 40px 80px rgba(0,0,0,.6); border: 3px solid rgba(255,255,255,.12); transform-origin: 50% 0%; }}
.shot img {{ width: 100%; display: block; }}
.card {{ position: absolute; left: 140px; right: 140px; top: 240px; border-radius: 36px; overflow: hidden; box-shadow: 0 40px 80px rgba(0,0,0,.6); }}
.card img {{ width: 100%; display: block; }}
.ctal {{ position: absolute; left: 50%; top: 220px; width: 260px; height: 260px; margin-left: -130px; border-radius: 54px; overflow: hidden; background: #fff; }}
.ctal img {{ width: 100%; height: 100%; object-fit: contain; padding: 30px; }}
.ctat {{ position: absolute; left: 60px; right: 60px; top: 560px; text-align: center; font-size: 92px; font-weight: 800; line-height: 1.08; letter-spacing: -2px; }}
.btn {{ position: absolute; left: 50%; top: 900px; transform: translateX(-50%); white-space: nowrap; background: var(--acc2); color: #0b1520; font-size: 54px; font-weight: 800; border-radius: 999px; padding: 26px 60px; box-shadow: 0 20px 50px rgba(0,0,0,.45); }}
.url {{ position: absolute; left: 0; right: 0; top: 1060px; text-align: center; font-size: 40px; font-weight: 600; color: rgba(255,255,255,.85); }}
.wallt {{ position: absolute; left: 60px; right: 60px; top: 200px; text-align: center; font-size: 80px; font-weight: 800; line-height: 1.08; letter-spacing: -1.5px; }}
.wall {{ position: absolute; left: 50px; right: 50px; top: 520px; display: grid; grid-template-columns: repeat({S.get("cols", 3)}, 1fr); gap: 22px; }}
.tile {{ aspect-ratio: 1 / 1; border-radius: 28px; overflow: hidden; background: #fff; box-shadow: 0 18px 40px rgba(0,0,0,.45); }}
.tile img {{ width: 100%; height: 100%; object-fit: cover; object-position: top; }}
.chips {{ position: absolute; left: 80px; right: 80px; top: 560px; display: flex; flex-direction: column; gap: 30px; }}
.chip {{ display: flex; align-items: center; gap: 26px; background: rgba(255,255,255,.08); border: 2px solid rgba(255,255,255,.14); border-radius: 30px; padding: 28px 34px; font-size: 52px; font-weight: 700; }}
.chip b {{ display: inline-flex; width: 76px; height: 76px; border-radius: 22px; background: var(--acc2); color: #0b1520; align-items: center; justify-content: center; font-size: 44px; }}
.sub {{ z-index: 50; }}
.sub::before {{ content: ''; position: absolute; left: 0; right: 0; bottom: 0; height: 520px; background: linear-gradient(180deg, rgba(0,0,0,0), rgba(0,0,0,.78) 55%); }}
.subin {{ position: absolute; left: 60px; right: 60px; bottom: 150px; text-align: center; font-size: 50px; font-weight: 800; line-height: 1.25; text-shadow: 0 4px 18px rgba(0,0,0,.95), 0 0 2px #000; }}
.kw.hot {{ color: var(--acc2); }}
#top {{ z-index: 60; }}
#badge {{ position: absolute; left: 50%; top: 60px; transform: translateX(-50%); white-space: nowrap; display: flex; gap: 14px; align-items: center; font-size: 28px; font-weight: 800; letter-spacing: 2px; }}
#badge span {{ background: var(--acc); border-radius: 99px; padding: 8px 22px; }}
#badge i {{ font-style: normal; color: rgba(255,255,255,.85); }}
#prog {{ position: absolute; left: 0; top: 0; height: 8px; width: 1080px; background: var(--acc2); transform-origin: 0 50%; }}
#av {{ position: absolute; left: -40px; top: 1060px; width: 520px; height: 520px; z-index: 40; }}
#av img {{ position: absolute; inset: 0; width: 100%; height: 100%; object-fit: contain; filter: drop-shadow(0 20px 40px rgba(0,0,0,.6)); }}
#avatar {{ z-index: 40; }}
"""

body = "\n      ".join(clips)
anim = "\n      ".join(anims)
out = f'''<!doctype html>
<html lang="fr">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script>
    <style>{css}</style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{DUR:.2f}" data-width="1080" data-height="1920">
      <div id="bg" class="clip" data-start="0" data-duration="{DUR:.2f}" data-track-index="0"></div>
      {body}
      <div id="top" class="clip" data-start="0" data-duration="{DUR:.2f}" data-track-index="80"><div id="prog"></div><div id="badge"><span>{esc(S["badge"])}</span><i>ÉPISODE {S["ep"]}</i></div></div>
      {voice}
      {music}
    </div>
    <script>
      window.__timelines = window.__timelines || {{}};
      const tl = gsap.timeline({{ paused: true }});
      const E = "power3.out";
      tl.fromTo("#prog", {{scaleX: 0}}, {{scaleX: 1, duration: {DUR:.2f}, ease: "none"}}, 0);
      {anim}
      window.__timelines["main"] = tl;
      tl.seek(0);
    </script>
  </body>
</html>
'''
open(os.path.join(D, "index.html"), "w").write(out)
print("écrit", os.path.join(D, "index.html"), "durée", DUR, "lignes", NL)
