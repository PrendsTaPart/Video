#!/usr/bin/env python3
"""Étape 4 — génère les compositions HyperFrames (1080×1920, 30 fps) depuis storyboard.json.

    python3 bd-video/scripts/build_montage.py ep01          # un épisode
    python3 bd-video/scripts/build_montage.py film          # le film complet
    python3 bd-video/scripts/build_montage.py all

Pour chaque vidéo : montage/<nom>/index.html + timeline.json (début/fin de chaque plan, utilisé
par mix_audio.py). La durée d'un plan = durée réelle de sa voix (audio/vo/<id>.mp3) + respiration ;
sans voix, une durée estimée (animatique). Rendu : npx hyperframes render dans montage/<nom>/.

Zones sûres TikTok/Reels : rien d'essentiel dans les 220 px du haut, 420 px du bas, 140 px à droite.
"""
import html
import json
import os
import subprocess
import sys

ROOT = os.path.join(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip(), "bd-video")
W, H, FPS = 1080, 1920, 30
SAFE_TOP, SAFE_BOTTOM, SAFE_RIGHT, MARGIN = 220, 420, 140, 56
TRANS = 0.4          # durée d'une transition de case à case
PAD = 0.35           # respiration après une réplique
shots = json.load(open(os.path.join(ROOT, "storyboard.json")))
panels = {p["file"]: p for p in json.load(open(os.path.join(ROOT, "panels", "index.json")))}

EPISODES = {
    "ep01": {"parts": ["Prologue", "Partie 1 · Une journée sans FoodEatUp"], "hero": "panels/p15-c1.jpg",
             "hook": "Pourquoi tenir un restaurant est-il si épuisant ?", "intro_card": ("PROLOGUE", "Vingt ans de coups de feu")},
    "ep02": {"parts": ["Partie 2 · La même journée, avec FoodEatUp"], "hero": "panels/p51-c1.jpg",
             "hook": "Ce soir, je dîne avec ma famille."},
    "ep03": {"parts": ["Partie 3 · La brigade passe à l'écran"], "hero": "panels/p57-c2.png",
             "hook": "Une seule saisie, et tout le restaurant communique."},
    "ep04": {"parts": ["Partie 4 · Expansion & franchise"], "hero": "panels/p73-c2.png",
             "hook": "Ce soir-là, la brigade augmentée est devenue une famille."},
    "ep05": {"parts": ["Partie 5 · Le laboratoire et les agents"], "hero": "panels/p77-c2.png",
             "hook": "L'IA propose, l'humain décide."},
    "ep06": {"parts": ["Partie 6 · Une infinité de solutions", "Épilogue", "Fermeture"], "hero": "panels/p82-c1.png",
             "hook": "Les solutions sont infinies."},
    "film": {"parts": None, "a_suivre": True, "hero": "panels/p01-c1.jpg", "hook": "D'une cuisine épuisée à une famille de restaurants."},
}
# Pages dont l'image de page entière porte déjà le texte : on la montre telle quelle (pas de calque texte).
PAGE_AS_IMAGE = {2, 3, 4, 54, 63, 74, 82, 88}
# Cadrage des cartes personnages (coordonnées Figma de la page 794×1123) pour zoomer carte par carte.
CARDS = {3: [(64, 160), (405, 160), (64, 391), (405, 391), (64, 622), (405, 622), (64, 853), (405, 853)],
         4: [(64, 170), (405, 170), (64, 401), (405, 401), (64, 640), (64, 806)]}


def vo_duration(sid):
    path = os.path.join(ROOT, "audio", "vo", f"{sid}.mp3")
    if not os.path.exists(path):
        return None
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path],
                         capture_output=True, text=True).stdout.strip()
    return float(out) if out else None


def esc(t):
    return html.escape(t, quote=True)


def chars(t):
    """Texte découpé en lettres pour l'effet machine à écrire (mots insécables)."""
    out = []
    for word in t.split(" "):
        out.append('<span class="w">' + "".join(f'<span class="ch">{esc(c)}</span>' for c in word) + "</span>")
    return " ".join(out)


def select(name):
    cfg = EPISODES[name]
    if cfg["parts"] is None:
        return shots, cfg
    return [s for s in shots if s["part"] in cfg["parts"]], cfg


def build(name):
    sel, cfg = select(name)
    has_voice = any(vo_duration(s["id"]) for s in sel if s["type"] != "titre")

    # 1) Durées et regroupement par case (une image par case, les répliques défilent dessus).
    groups = []
    for s in sel:
        d = vo_duration(s["id"]) if s["type"] != "titre" else None
        s = dict(s, dur=round((d + PAD) if d else s["duration_est"], 2), has_vo=bool(d))
        if s["page"] in (3, 4) and s.get("card"):
            s["dur"] = 3.2
        key = (s["page"], s["case"])
        if groups and groups[-1]["key"] == key:
            groups[-1]["shots"].append(s)
        else:
            groups.append({"key": key, "part": s["part"], "image": s["image"], "page": s["page"], "shots": [s]})

    t = 0.0
    timeline = []
    body, script = [], []
    track_img = 1

    # 2) Accroche 0–2 s : la case forte de la partie + une phrase de la BD.
    hook_d = 2.2
    body.append(f'''<div id="hook" class="clip scene" data-start="0" data-duration="{hook_d}" data-track-index="9">
  <div class="fill navy"></div><img id="hook-img" class="cover" src="{cfg['hero']}" alt="">
  <div class="shade"></div><div id="hook-txt" class="hook">{esc(cfg['hook'])}</div></div>''')
    script.append(f'tl.fromTo("#hook-img",{{scale:1.18}},{{scale:1.0,duration:{hook_d},ease:"power2.out"}},0);')
    script.append('tl.fromTo("#hook-txt",{scale:0.6,opacity:0},{scale:1,opacity:1,duration:0.35,ease:"back.out(2)"},0.15);')
    t = hook_d

    # 3) Carton d'ouverture (épisode 1 : « Prologue »).
    if cfg.get("intro_card"):
        a, b = cfg["intro_card"]
        d = 2.4
        body.append(f'''<div id="intro" class="clip scene" data-start="{t:.3f}" data-duration="{d}" data-track-index="8">
  <div class="fill navy"></div><img class="cover dim" src="{sel[0]['image']}" alt=""><div class="partcard"><div class="kicker">{esc(a)}</div><div class="ptitle">{esc(b)}</div></div></div>''')
        script.append(f'tl.fromTo("#intro .partcard",{{y:80,opacity:0}},{{y:0,opacity:1,duration:0.5,ease:"power3.out"}},{t:.3f});')
        t += d

    prev_part = None
    for gi, g in enumerate(groups):
        gid = f"g{gi:03d}"
        # Film complet : carton « À suivre… » entre deux parties (la page qui tourne se fait dessous).
        if cfg.get("a_suivre") and prev_part not in (None, "Ouverture") and g["part"] != prev_part:
            d = 1.4
            body.append(f'''<div id="{gid}-next" class="clip scene" data-start="{t:.3f}" data-duration="{d}" data-track-index="8">
  <div class="fill navy"></div><div class="partcard next"><div class="ptitle">À suivre…</div></div></div>''')
            script.append(f'tl.fromTo("#{gid}-next .partcard",{{scale:0.7,opacity:0}},{{scale:1,opacity:1,duration:0.35,ease:"back.out(2)"}},{t:.3f});')
            script.append(f'tl.to("#{gid}-next",{{opacity:0,duration:{TRANS}}},{t + d - TRANS:.3f});')
            t += d
        g_start = max(0.0, t - (TRANS if gi else 0))
        g_dur = sum(s["dur"] for s in g["shots"]) + (TRANS if gi else 0)
        page_turn = prev_part is not None and g["part"] != prev_part
        prev_part = g["part"]
        use_page = g["page"] in PAGE_AS_IMAGE
        img = f"pages/p{g['page']:02d}.png" if use_page else g["image"]
        meta = panels.get(img)
        landscape = bool(meta and meta["source_px"][0] > meta["source_px"][1])
        cls = "page" if use_page else ("land" if landscape else "port")
        body.append(f'''<div id="{gid}" class="clip scene" data-start="{g_start:.3f}" data-duration="{g_dur:.3f}" data-track-index="{track_img}">
  <div class="fill navy"></div>{'<img class="blur" src="'+img+'" alt="">' if cls == "land" else ''}
  <div class="turn" id="{gid}-turn"><img id="{gid}-img" class="art {cls}" src="{img}" alt=""></div></div>''')
        # Entrée : page qui tourne entre deux parties, glissé de case à case sinon.
        if gi:
            if page_turn:
                script.append(f'tl.fromTo("#{gid}-turn",{{rotationY:-95,transformOrigin:"0% 50%"}},{{rotationY:0,duration:{TRANS+0.3},ease:"power2.out"}},{g_start:.3f});')
            else:
                script.append(f'tl.fromTo("#{gid}-turn",{{xPercent:100}},{{xPercent:0,duration:{TRANS},ease:"power3.out"}},{g_start:.3f});')
        # Mouvement lent sur l'image (Ken Burns), sens alterné d'une case à l'autre.
        if cls == "port":
            y0, y1 = (0, -60) if gi % 2 else (-60, 0)
            script.append(f'tl.fromTo("#{gid}-img",{{scale:1.0,y:{y0}}},{{scale:1.08,y:{y1},duration:{g_dur:.3f},ease:"none"}},{g_start:.3f});')
        elif cls == "land":
            span = round(1300 * 1376 / 768 - W)
            x0, x1 = (0, -span) if gi % 2 == 0 else (-span, 0)
            script.append(f'tl.fromTo("#{gid}-img",{{x:{x0}}},{{x:{x1},duration:{g_dur:.3f},ease:"sine.inOut"}},{g_start:.3f});')
        elif g["page"] in CARDS:
            # Zoom carte par carte sur les pages personnages.
            k = 0
            tt = t
            for s in g["shots"]:
                if s.get("card") and k < len(CARDS[g["page"]]):
                    cx, cy = CARDS[g["page"]][k]
                    k += 1
                    sc = 2.6
                    px = (cx + 162) * W / 794
                    py = (cy + 107) * W / 794 + (H - 1123 * W / 794) / 2
                    script.append(f'tl.to("#{gid}-img",{{scale:{sc},x:{W/2-px:.0f}*{sc},y:{H/2-py:.0f}*{sc},duration:0.6,ease:"power2.inOut"}},{tt:.3f});')
                tt += s["dur"]
        else:
            script.append(f'tl.fromTo("#{gid}-img",{{scale:1.0}},{{scale:1.12,duration:{g_dur:.3f},ease:"none"}},{g_start:.3f});')
        track_img = 2 if track_img == 1 else 1

        # Calques texte : cartouche (reste jusqu'à la fin de la case), bulles une par une, titres.
        recit_track, bubble_track = 3, 4
        for si, s in enumerate(g["shots"]):
            sid = s["id"].replace("-", "_")
            s_start = t
            timeline.append({"id": s["id"], "start": round(s_start, 3), "dur": s["dur"], "type": s["type"],
                             "voice": s.get("voice"), "has_vo": s["has_vo"], "part": s["part"], "page": s["page"]})
            type_d = max(0.6, (s["dur"] - PAD) * 0.85)
            if s["type"] == "recit":
                rest = round(sum(x["dur"] for x in g["shots"][si:]), 3)
                body.append(f'''<div id="{sid}" class="clip cartouche" data-start="{s_start:.3f}" data-duration="{rest}" data-track-index="{recit_track}">{chars(s["text"])}</div>''')
                script.append(f'tl.fromTo("#{sid}",{{y:-30,opacity:0}},{{y:0,opacity:1,duration:0.3,ease:"power2.out"}},{s_start:.3f});')
                script.append(f'tl.fromTo("#{sid} .ch",{{opacity:0}},{{opacity:1,duration:0.01,stagger:{type_d/max(1,len(s["text"])):.4f}}},{s_start+0.15:.3f});')
                recit_track = 5 if recit_track == 3 else 3
            elif s["type"] == "bulle":
                av = s.get("avatar") or ""
                body.append(f'''<div id="{sid}" class="clip bulle" data-start="{s_start:.3f}" data-duration="{s['dur']}" data-track-index="{bubble_track}">
  <div class="who"><img class="pastille" src="{av}" alt=""><span>{esc(s['speaker'])}</span></div>
  <div class="said">{chars(s["text"])}</div></div>''')
                script.append(f'tl.fromTo("#{sid}",{{scale:0.4,opacity:0,transformOrigin:"15% 100%"}},{{scale:1,opacity:1,duration:0.28,ease:"back.out(2.2)"}},{s_start:.3f});')
                script.append(f'tl.fromTo("#{sid} .ch",{{opacity:0}},{{opacity:1,duration:0.01,stagger:{type_d/max(1,len(s["text"])):.4f}}},{s_start+0.2:.3f});')
                bubble_track = 6 if bubble_track == 4 else 4
            elif not use_page:  # titre posé sur un dessin
                body.append(f'''<div id="{sid}" class="clip titlecard" data-start="{s_start:.3f}" data-duration="{s['dur']}" data-track-index="7"><div class="ptitle">{esc(s["text"])}</div></div>''')
                script.append(f'tl.fromTo("#{sid}",{{y:60,opacity:0}},{{y:0,opacity:1,duration:0.4,ease:"power3.out"}},{s_start:.3f});')
            t += s["dur"]

    # 4) Fin : logo, signature, appel à l'action.
    end_d = 4.0
    body.append(f'''<div id="endcard" class="clip scene" data-start="{t:.3f}" data-duration="{end_d}" data-track-index="8">
  <div class="fill navy"></div><div class="end"><img id="end-logo" src="assets/logos/foodeatup-wordmark-blanc.png" alt="FoodEatUp">
  <div id="end-sig" class="sig">Une seule saisie, pas dix.</div><div id="end-cta" class="cta">Testez FoodEatUp · Lien en bio</div></div></div>''')
    script.append(f'tl.fromTo("#end-logo",{{scale:0.7,opacity:0}},{{scale:1,opacity:1,duration:0.5,ease:"back.out(1.8)"}},{t+0.1:.3f});')
    script.append(f'tl.fromTo("#end-sig",{{y:40,opacity:0}},{{y:0,opacity:1,duration:0.4}},{t+0.6:.3f});')
    script.append(f'tl.fromTo("#end-cta",{{y:40,opacity:0}},{{y:0,opacity:1,duration:0.4}},{t+1.0:.3f});')
    total = round(t + end_d, 3)

    doc = f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width={W}, height={H}">
<title>La Brigade augmentée — {name}</title>
<script src="assets/vendor/gsap.min.js"></script>
<style>
@font-face{{font-family:"Bangers";src:url("assets/fonts/bangers-latin-400-normal.woff2") format("woff2");}}
@font-face{{font-family:"Bangers";src:url("assets/fonts/bangers-latin-ext-400-normal.woff2") format("woff2");unicode-range:U+0100-024F;}}
@font-face{{font-family:"Comic Neue";font-weight:700;src:url("assets/fonts/comic-neue-latin-700-normal.woff2") format("woff2");}}
@font-face{{font-family:"Comic Neue";font-weight:400;src:url("assets/fonts/comic-neue-latin-400-normal.woff2") format("woff2");}}
:root{{--navy:#0B2545;--yellow:#FFD640;--orange:#F59B0A;--white:#FFFFFF;--cream:#FFF6DC;}}
body{{margin:0;background:var(--navy);}}
#root{{position:relative;width:{W}px;height:{H}px;overflow:hidden;}}
.clip{{position:absolute;}}
.scene{{inset:0;overflow:hidden;perspective:2200px;}}
.fill{{position:absolute;inset:0;}} .navy{{background:var(--navy);}}
.turn{{position:absolute;inset:0;}}
.art{{position:absolute;display:block;}}
.port{{left:0;top:0;width:{W}px;height:{H}px;object-fit:cover;}}
.land{{left:0;top:{(H-1300)//2 - 60}px;height:1300px;width:{round(1300*1376/768)}px;}}
.page{{left:0;top:{round((H-1123*W/794)/2)}px;width:{W}px;height:{round(1123*W/794)}px;transform-origin:50% 50%;}}
.blur{{position:absolute;inset:-80px;width:calc(100% + 160px);height:calc(100% + 160px);object-fit:cover;filter:blur(40px) brightness(.55);}}
.cover{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;}}
.dim{{opacity:.35;}}
.shade{{position:absolute;inset:0;background:linear-gradient(180deg,rgba(11,37,69,.15) 30%,rgba(11,37,69,.85) 100%);}}
.hook{{position:absolute;left:{MARGIN}px;right:{SAFE_RIGHT}px;bottom:{SAFE_BOTTOM+40}px;font-family:"Bangers";font-size:96px;line-height:1.02;color:var(--yellow);
  text-shadow:0 6px 0 var(--navy),0 0 24px rgba(0,0,0,.6);letter-spacing:1px;}}
.partcard{{position:absolute;left:{MARGIN}px;right:{SAFE_RIGHT}px;top:720px;}}
.kicker{{font-family:"Bangers";font-size:64px;color:var(--orange);letter-spacing:2px;}}
.ptitle{{font-family:"Bangers";font-size:104px;line-height:1.0;color:var(--white);letter-spacing:1px;}}
.titlecard{{left:{MARGIN}px;right:{SAFE_RIGHT}px;bottom:{SAFE_BOTTOM+60}px;background:var(--navy);border:6px solid var(--yellow);border-radius:28px;padding:28px 34px;}}
.partcard.next{{text-align:center;}}
.partcard.next .ptitle{{color:var(--yellow);}}
.titlecard .ptitle{{font-size:76px;color:var(--yellow);}}
.cartouche{{left:{MARGIN}px;right:{SAFE_RIGHT}px;top:{SAFE_TOP+20}px;background:var(--cream);border:5px solid var(--navy);border-radius:14px;padding:26px 30px;
  font-family:"Comic Neue";font-weight:700;font-size:44px;line-height:1.22;color:var(--navy);box-shadow:0 10px 0 rgba(0,0,0,.25);}}
.bulle{{left:{MARGIN}px;right:{SAFE_RIGHT}px;bottom:{SAFE_BOTTOM+20}px;background:var(--white);border:6px solid var(--navy);border-radius:44px;padding:26px 34px 32px;
  box-shadow:0 12px 0 rgba(0,0,0,.25);}}
.who{{display:flex;align-items:center;gap:16px;margin-bottom:10px;}}
.pastille{{width:72px;height:72px;border-radius:50%;border:4px solid var(--navy);object-fit:cover;background:var(--navy);}}
.who span{{font-family:"Comic Neue";font-weight:700;font-size:36px;color:var(--orange);letter-spacing:1px;}}
.said{{font-family:"Comic Neue";font-weight:700;font-size:50px;line-height:1.2;color:var(--navy);}}
.w{{display:inline-block;white-space:nowrap;}}
.end{{position:absolute;left:{MARGIN}px;right:{SAFE_RIGHT}px;top:660px;text-align:center;}}
.end img{{width:760px;display:block;margin:0 auto 60px;}}
.sig{{font-family:"Bangers";font-size:96px;color:var(--yellow);line-height:1.05;}}
.cta{{margin-top:40px;font-family:"Comic Neue";font-weight:700;font-size:50px;color:var(--white);}}
</style>
</head>
<body>
<div id="root" data-composition-id="{name}" data-start="0" data-width="{W}" data-height="{H}" data-duration="{total}" data-fps="{FPS}">
{chr(10).join(body)}
</div>
<script>
window.__timelines = window.__timelines || {{}};
const tl = gsap.timeline({{ paused: true }});
{chr(10).join(script)}
window.__timelines["{name}"] = tl;
</script>
</body>
</html>
'''
    out = os.path.join(ROOT, "montage", name)
    os.makedirs(out, exist_ok=True)
    for link in ("panels", "pages", "cast", "assets", "audio"):
        p = os.path.join(out, link)
        if not os.path.lexists(p):
            os.symlink(os.path.join("..", "..", link), p)
    open(os.path.join(out, "index.html"), "w").write(doc)
    json.dump({"name": name, "duration": total, "fps": FPS, "voice": has_voice, "hook": [0, hook_d],
               "end": [round(t, 3), end_d], "shots": timeline}, open(os.path.join(out, "timeline.json"), "w"),
              ensure_ascii=False, indent=1)
    print(f"{name}: {len(timeline)} plans, {total/60:.1f} min, voix {'réelles' if has_voice else 'estimées (animatique)'}")


if __name__ == "__main__":
    names = sys.argv[1:] or ["ep01"]
    if names == ["all"]:
        names = list(EPISODES)
    for n in names:
        build(n)
