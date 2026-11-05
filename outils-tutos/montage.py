#!/usr/bin/env python3
"""Montage commun des tutoriels d'applications FoodEatUp (HyperFrames 0.9.5, 1920x1080).

Chaque série (foodeatup-tutos-<app>/) fournit tutos.py (liste T) et appelle construire(cfg).
Une entrée de T : cle, titre, chef (image de chef-video), etapes (4), voix (texte ElevenLabs),
ecrans : liste de [image, x, y] — x, y = point touché (0..1) avant de passer à l'écran suivant, ou None.
Le faux curseur orange va au point touché, appuie, puis l'écran suivant apparaît.
"""
import html, json, os, re, shutil, subprocess, sys

ICI = os.path.dirname(os.path.abspath(__file__))
COMMUN = os.path.join(ICI, "..", "foodeatup-tutos-kds", "commun")  # gsap 3.12.5, Inter (OFL), logo officiel
CHEFS = "/home/user/stockvisionai/public/images/illustrations/chef-video"

# Formats d'appareil : position et taille de la vitre (zone écran) dans la vidéo.
APPAREILS = {
    "telephone": dict(x=230, y=108, w=468, h=832, rayon=50, bord=16, rayon_ext=64, texte_x=830),
    "tablette": dict(x=70, y=150, w=960, h=600, rayon=26, bord=18, rayon_ext=40, texte_x=1100),
}

def duree(f):
    return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f]).strip())

def morceaux(texte):
    out = []
    faibles = {"le", "la", "les", "de", "du", "des", "un", "une", "à", "au", "dans", "et", "en", "sur", "mon", "ma", "mes", "ton", "c'est", "puis", "par", "avec", "je", "l'", "d'"}
    for phrase in re.split(r"(?<=[.:!?,])\s+", texte):
        mots = phrase.split()
        while mots:
            n = 6 if len(mots) > 7 else len(mots)
            if len(mots) - n == 1: n -= 1
            while n > 2 and n < len(mots) and mots[n-1].lower().strip(",") in faibles: n -= 1
            out.append(" ".join(mots[:n]).rstrip("."))
            mots = mots[n:]
    return [b for b in out if b]

def page(cfg, i, n_total, v, D):
    e = html.escape
    ap = APPAREILS[cfg.get("appareil", "telephone")]
    tx = ap["texte_x"]
    fin = D + 2.6
    texte = re.sub(r"\[[^\]]*\]\s*", "", v["voix"]).strip()
    blocs = morceaux(texte); total = sum(len(b) for b in blocs)
    t, subs = 0.35, []
    for b in blocs:
        d = (D - 0.4) * len(b) / total; subs.append((round(t, 2), round(d, 2), b)); t += d
    sous = "\n".join(f'<div class="sub" id="s{k}">{e(b)}</div>' for k, (_, _, b) in enumerate(subs))
    tl_sous = "\n".join(f'tl.set("#s{k}",{{opacity:1}},{a}); tl.set("#s{k}",{{opacity:0}},{round(a+d,2)});' for k, (a, d, _) in enumerate(subs))
    ecr = v["ecrans"]; n = len(ecr)
    imgs = "".join(f'<img class="ecr" id="e{k}" src="assets/{os.path.basename(x[0])}" alt="">' for k, x in enumerate(ecr))
    seg = (D - 1.2) / n
    tl = []
    for k in range(n):
        debut = 1.0 + k * seg
        if k > 0:
            tl.append(f'tl.fromTo("#e{k}",{{opacity:0,scale:1.03}},{{opacity:1,scale:1,duration:.45,ease:"power2.out"}},{debut:.2f}); tl.to("#e{k-1}",{{opacity:0,duration:.3}},{debut:.2f});')
        point = ecr[k][1:3] if len(ecr[k]) >= 3 and ecr[k][1] is not None else None
        if point and k < n - 1:
            px, py = point[0] * ap["w"], point[1] * ap["h"]
            arrive = debut + seg * 0.45
            tl.append(f'tl.to("#cur",{{opacity:1,x:{px:.0f},y:{py:.0f},duration:.7,ease:"power2.inOut"}},{arrive:.2f});')
            tl.append(f'tl.to("#cur",{{scale:.7,duration:.12,yoyo:true,repeat:1}},{arrive+0.75:.2f}); tl.fromTo("#onde",{{x:{px:.0f},y:{py:.0f},scale:.3,opacity:.9}},{{scale:2.2,opacity:0,duration:.5,immediateRender:false}},{arrive+0.75:.2f});')
    tl.append(f'tl.to("#cur",{{opacity:0,duration:.3}},{D - 0.2:.2f});')
    etapes = "".join(f'<li class="etape" id="t{k}"><span class="num">{k+1}</span><span>{e(s)}</span></li>' for k, s in enumerate(v["etapes"]))
    pas = (D - 3.0) / len(v["etapes"])
    tl_etapes = "\n".join(f'tl.fromTo("#t{k}",{{opacity:0,x:60}},{{opacity:1,x:0,duration:.5,ease:"back.out(2)"}},{round(2.2+k*pas,2)});' for k in range(len(v["etapes"])))
    W, H = ap["w"] + 2 * ap["bord"], ap["h"] + 2 * ap["bord"]
    return f'''<!doctype html>
<html lang="fr"><head><meta charset="UTF-8" /><meta name="viewport" content="width=1920, height=1080" />
<script src="assets/gsap.min.js"></script>
<style>
@font-face {{ font-family:"Inter"; src:url("assets/Inter-600.woff2"); font-weight:600; }}
@font-face {{ font-family:"Inter"; src:url("assets/Inter-800.woff2"); font-weight:800; }}
* {{ margin:0; padding:0; box-sizing:border-box; }}
html, body {{ width:1920px; height:1080px; overflow:hidden; background:#0F1A23; }}
#root {{ position:relative; width:1920px; height:1080px; overflow:hidden; font-family:"Inter",sans-serif; color:#FCF9E6;
  background: radial-gradient(800px 700px at 22% 55%, rgba(255,165,0,.22), transparent 62%), radial-gradient(900px 600px at 90% 0%, rgba(0,123,255,.22), transparent 60%), #0F1A23; }}
.app {{ position:absolute; left:{ap["x"]}px; top:{ap["y"]}px; width:{W}px; height:{H}px; border-radius:{ap["rayon_ext"]}px; background:#05090D; padding:{ap["bord"]}px;
  box-shadow:0 40px 90px rgba(0,0,0,.55), 0 0 0 3px #2A3A47 inset; }}
.vitre {{ position:relative; width:{ap["w"]}px; height:{ap["h"]}px; border-radius:{ap["rayon"]}px; overflow:hidden; background:#16242F; }}
.ecr {{ position:absolute; inset:0; width:100%; height:100%; object-fit:cover; object-position:top; opacity:0; }}
#e0 {{ opacity:1; }}
#cur {{ position:absolute; left:-23px; top:-23px; width:46px; height:46px; border-radius:999px; background:rgba(255,165,0,.92); border:4px solid #fff; box-shadow:0 6px 18px rgba(0,0,0,.45); opacity:0; z-index:4; }}
#onde {{ position:absolute; left:-30px; top:-30px; width:60px; height:60px; border-radius:999px; border:4px solid #FFA500; opacity:0; z-index:3; }}
.logo {{ position:absolute; right:90px; top:70px; height:58px; background:#fff; padding:10px 18px; border-radius:18px; }}
.rub {{ position:absolute; left:{tx}px; top:130px; font-size:26px; font-weight:800; letter-spacing:.16em; text-transform:uppercase; color:#FFA500; }}
.titre {{ position:absolute; left:{tx}px; top:176px; right:120px; font-size:{68 if tx < 1000 else 58}px; font-weight:800; line-height:1.04; letter-spacing:-.02em; }}
ol {{ position:absolute; left:{tx}px; top:{430 if tx < 1000 else 400}px; right:{340 if tx < 1000 else 90}px; list-style:none; display:grid; gap:20px; }}
.etape {{ display:flex; align-items:center; gap:22px; background:rgba(252,249,230,.07); border:2px solid rgba(252,249,230,.12); border-radius:24px; padding:16px 24px; font-size:{33 if tx < 1000 else 29}px; font-weight:600; opacity:0; }}
.num {{ flex-shrink:0; width:56px; height:56px; border-radius:999px; background:#007BFF; color:#fff; font-weight:800; display:flex; align-items:center; justify-content:center; font-size:30px; }}
.etape:nth-child(even) .num {{ background:#FFA500; color:#1d1300; }}
.chef {{ position:absolute; right:70px; bottom:150px; width:{260 if tx < 1000 else 0}px; height:260px; border-radius:999px; object-fit:cover; background:#fff; border:8px solid #FFA500; }}
.demo {{ position:absolute; left:{ap["x"]}px; top:{ap["y"] - 40}px; width:{W}px; text-align:center; font-size:20px; font-weight:600; color:#AEB8C2; }}
.sub {{ position:absolute; left:0; right:0; bottom:34px; text-align:center; font-size:44px; font-weight:800; color:#fff;
  background:rgba(5,9,13,.85); padding:10px 26px; border-radius:18px; display:table; margin:0 auto; opacity:0; z-index:5; }}
.fin {{ position:absolute; inset:0; background:#007BFF; display:flex; flex-direction:column; align-items:center; justify-content:center; gap:28px; opacity:0; z-index:9; }}
.fin img {{ height:110px; background:#fff; padding:16px 26px; border-radius:26px; }}
.fin p {{ font-size:70px; font-weight:800; color:#fff; }}
.fin span {{ font-size:36px; font-weight:600; color:#fff; opacity:.92; }}
</style></head>
<body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{fin:.3f}" data-width="1920" data-height="1080">
  <audio id="voix" src="assets/voix.mp3" data-start="0.3" data-duration="{D:.3f}" data-track-index="10" data-volume="1"></audio>
  <div class="app" id="app"><div class="vitre">{imgs}<div id="onde"></div><div id="cur"></div></div></div>
  <p class="demo" id="demo">Démonstration · restaurant fictif</p>
  <img class="logo" id="logo" src="assets/logo.png" alt="FoodEatUp">
  <p class="rub" id="rub">{e(cfg["rubrique"])} · tutoriel {i+1}/{n_total}</p>
  <h1 class="titre" id="titre">{e(v["titre"])}</h1>
  <ol>{etapes}</ol>
  <img class="chef" id="chef" src="assets/chef.webp" alt="">
  {sous}
  <div class="fin" id="fin"><img src="assets/logo.png" alt=""><p>{e(cfg["nom_final"])}</p><span>Sur le Store FoodEatUp · tutoriel.foodeatup.com</span></div>
</div>
<script>
window.__timelines = window.__timelines || {{}};
const tl = gsap.timeline({{ paused:true }});
tl.fromTo("#app", {{ opacity:0, y:120, rotation:-3 }}, {{ opacity:1, y:0, rotation:0, duration:1, ease:"back.out(1.4)" }}, 0.1);
tl.fromTo("#demo", {{ opacity:0 }}, {{ opacity:1, duration:.5 }}, 0.8);
tl.fromTo("#logo", {{ opacity:0, y:-20 }}, {{ opacity:1, y:0, duration:.5 }}, 0.2);
tl.fromTo("#rub", {{ opacity:0, x:-30 }}, {{ opacity:1, x:0, duration:.5 }}, 0.6);
tl.fromTo("#titre", {{ opacity:0, y:40 }}, {{ opacity:1, y:0, duration:.7, ease:"back.out(1.6)" }}, 0.8);
tl.fromTo("#chef", {{ opacity:0, scale:.5 }}, {{ opacity:1, scale:1, duration:.9, ease:"elastic.out(1,.6)" }}, 1.4);
{chr(10).join(tl)}
{tl_etapes}
tl.to("#fin", {{ opacity:1, duration:.5 }}, {D + 0.5:.2f});
tl.fromTo("#fin p", {{ scale:.7 }}, {{ scale:1, duration:.7, ease:"back.out(2)" }}, {D + 0.6:.2f});
{tl_sous}
tl.set({{}}, {{}}, {fin:.3f});
window.__timelines["main"] = tl;
</script>
</body></html>
'''

def construire(cfg, T, cles=None):
    """cfg : dossier (série), captures (dossier des images), rubrique, nom_final, appareil."""
    for i, v in enumerate(T):
        if cles and v["cle"] not in cles: continue
        voix = os.path.join(cfg["dossier"], "voix", v["cle"] + ".mp3")
        if not os.path.exists(voix): print("pas de voix", v["cle"]); continue
        d = os.path.join(cfg["dossier"], "projets", v["cle"]); a = os.path.join(d, "assets")
        shutil.rmtree(d, ignore_errors=True); os.makedirs(a)
        for f in ["gsap.min.js", "Inter-600.woff2", "Inter-800.woff2", "logo.png"]:
            shutil.copy(os.path.join(COMMUN, f), a)
        shutil.copy(os.path.join(CHEFS, v["chef"]), os.path.join(a, "chef.webp"))
        for x in v["ecrans"]: shutil.copy(os.path.join(cfg["captures"], x[0]), a)
        shutil.copy(voix, os.path.join(a, "voix.mp3"))
        D = duree(voix)
        open(os.path.join(d, "index.html"), "w").write(page(cfg, i, len(T), v, D))
        json.dump({"$schema": "https://hyperframes.heygen.com/schema/hyperframes.json", "paths": {"assets": "assets"}}, open(os.path.join(d, "hyperframes.json"), "w"))
        json.dump({"id": v["cle"], "name": v["cle"]}, open(os.path.join(d, "meta.json"), "w"))
        print(v["cle"], round(D, 2))
