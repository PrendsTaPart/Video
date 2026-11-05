#!/usr/bin/env python3
"""Tutoriels vidéo de l'application FoodEatUp HACCP — 1920x1080, vrais écrans de l'appli."""
import html, json, os, re, shutil, subprocess, sys
from tutos import T
ICI = os.path.dirname(os.path.abspath(__file__))
GAL = "/tmp/claude-0/-home-user/ef008aff-2ade-5433-9524-47302a7a1a32/scratchpad/galerie"
CHEFS = "/home/user/stockvisionai/public/images/illustrations/chef-video"
CHEF = {"app-haccp-decouvrir": "app-haccp.webp", "app-haccp-temperature": "mission-releve-action.webp",
        "app-haccp-jarvis": "mission-jarvis-action.webp", "app-haccp-etiquette": "mission-etiquette-action.webp",
        "app-haccp-reception": "mission-fournisseur-action.webp", "app-haccp-nettoyage": "mission-nettoyage-action.webp",
        "app-haccp-huiles": "pose-05.webp", "app-haccp-historique": "mission-releve-reussi.webp"}

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

def page(i, v, D):
    e = html.escape
    fin = D + 2.4
    texte = re.sub(r"\[[^\]]*\]\s*", "", v["voix"]).strip()
    blocs = morceaux(texte); total = sum(len(b) for b in blocs)
    t, subs = 0.35, []
    for b in blocs:
        d = (D - 0.4) * len(b) / total; subs.append((round(t, 2), round(d, 2), b)); t += d
    sous = "\n".join(f'<div class="sub" id="s{k}">{e(b)}</div>' for k, (_, _, b) in enumerate(subs))
    tl_sous = "\n".join(f'tl.set("#s{k}",{{opacity:1}},{a}); tl.set("#s{k}",{{opacity:0}},{round(a+d,2)});' for k, (a, d, _) in enumerate(subs))
    ecrans = "".join(f'<img class="ecr" id="e{k}" src="assets/{n}.png" alt="">' for k, n in enumerate(v["ecrans"]))
    n = len(v["ecrans"]); seg = (D - 1.0) / n
    tl_ecr = "\n".join(f'tl.fromTo("#e{k}",{{opacity:0,scale:1.04}},{{opacity:1,scale:1,duration:.5,ease:"power2.out"}},{round(1.0+k*seg,2)}); tl.to("#e{k-1}",{{opacity:0,duration:.35}},{round(1.0+k*seg,2)});' for k in range(1, n))
    etapes = "".join(f'<li class="etape" id="t{k}"><span class="num">{k+1}</span><span>{e(s)}</span></li>' for k, s in enumerate(v["etapes"]))
    pas = (D - 3.0) / len(v["etapes"])
    tl_etapes = "\n".join(f'tl.fromTo("#t{k}",{{opacity:0,x:60}},{{opacity:1,x:0,duration:.5,ease:"back.out(2)"}},{round(2.2+k*pas,2)});' for k in range(len(v["etapes"])))
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
.tel {{ position:absolute; left:210px; top:96px; width:500px; height:888px; border-radius:64px; background:#05090D; padding:16px;
  box-shadow:0 40px 90px rgba(0,0,0,.55), 0 0 0 3px #2A3A47 inset; }}
.vitre {{ position:relative; width:100%; height:100%; border-radius:50px; overflow:hidden; background:#16242F; }}
.ecr {{ position:absolute; inset:0; width:100%; height:100%; object-fit:cover; opacity:0; }}
#e0 {{ opacity:1; }}
.encoche {{ position:absolute; left:50%; top:14px; width:120px; height:30px; margin-left:-60px; border-radius:20px; background:#05090D; z-index:3; }}
.logo {{ position:absolute; right:90px; top:70px; height:58px; background:#fff; padding:10px 18px; border-radius:18px; }}
.rub {{ position:absolute; left:830px; top:130px; font-size:26px; font-weight:800; letter-spacing:.16em; text-transform:uppercase; color:#FFA500; }}
.titre {{ position:absolute; left:830px; top:176px; right:120px; font-size:72px; font-weight:800; line-height:1.04; letter-spacing:-.02em; }}
ol {{ position:absolute; left:830px; top:430px; right:340px; list-style:none; display:grid; gap:22px; }}
.etape {{ display:flex; align-items:center; gap:22px; background:rgba(252,249,230,.07); border:2px solid rgba(252,249,230,.12); border-radius:24px; padding:18px 24px; font-size:34px; font-weight:600; opacity:0; }}
.num {{ flex-shrink:0; width:56px; height:56px; border-radius:999px; background:#007BFF; color:#fff; font-weight:800; display:flex; align-items:center; justify-content:center; font-size:30px; }}
.etape:nth-child(even) .num {{ background:#FFA500; color:#1d1300; }}
.chef {{ position:absolute; right:70px; bottom:150px; width:260px; height:260px; border-radius:999px; object-fit:cover; background:#fff; border:8px solid #FFA500; }}
.sub {{ position:absolute; left:0; right:0; bottom:40px; text-align:center; font-size:44px; font-weight:800; color:#fff;
  background:rgba(5,9,13,.85); padding:10px 26px; border-radius:18px; display:table; margin:0 auto; opacity:0; z-index:5; }}
.fin {{ position:absolute; inset:0; background:#007BFF; display:flex; flex-direction:column; align-items:center; justify-content:center; gap:28px; opacity:0; z-index:9; }}
.fin img {{ height:110px; background:#fff; padding:16px 26px; border-radius:26px; }}
.fin p {{ font-size:70px; font-weight:800; color:#fff; }}
.fin span {{ font-size:36px; font-weight:600; color:#fff; opacity:.92; }}
</style></head>
<body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{fin:.3f}" data-width="1920" data-height="1080">
  <audio id="voix" src="assets/voix.mp3" data-start="0.3" data-duration="{D:.3f}" data-track-index="10" data-volume="1"></audio>
  <div class="tel" id="tel"><div class="vitre">{ecrans}<div class="encoche"></div></div></div>
  <img class="logo" id="logo" src="assets/logo.png" alt="FoodEatUp">
  <p class="rub" id="rub">Application HACCP · tutoriel {i+1}/{len(T)}</p>
  <h1 class="titre" id="titre">{e(v["titre"])}</h1>
  <ol>{etapes}</ol>
  <img class="chef" id="chef" src="assets/chef.webp" alt="">
  {sous}
  <div class="fin" id="fin"><img src="assets/logo.png" alt=""><p>FoodEatUp HACCP</p><span>Sur le Store FoodEatUp · tutoriel.foodeatup.com</span></div>
</div>
<script>
window.__timelines = window.__timelines || {{}};
const tl = gsap.timeline({{ paused:true }});
tl.fromTo("#tel", {{ opacity:0, y:120, rotation:-4 }}, {{ opacity:1, y:0, rotation:0, duration:1, ease:"back.out(1.4)" }}, 0.1);
tl.fromTo("#logo", {{ opacity:0, y:-20 }}, {{ opacity:1, y:0, duration:.5 }}, 0.2);
tl.fromTo("#rub", {{ opacity:0, x:-30 }}, {{ opacity:1, x:0, duration:.5 }}, 0.6);
tl.fromTo("#titre", {{ opacity:0, y:40 }}, {{ opacity:1, y:0, duration:.7, ease:"back.out(1.6)" }}, 0.8);
tl.fromTo("#chef", {{ opacity:0, scale:.5 }}, {{ opacity:1, scale:1, duration:.9, ease:"elastic.out(1,.6)" }}, 1.4);
tl.to("#tel", {{ y:-12, duration:1.6, yoyo:true, repeat:{int(fin/1.6)}, ease:"sine.inOut" }}, 1.2);
{tl_ecr}
{tl_etapes}
tl.to("#fin", {{ opacity:1, duration:.5 }}, {D + 0.5});
tl.fromTo("#fin p", {{ scale:.7 }}, {{ scale:1, duration:.7, ease:"back.out(2)" }}, {D + 0.6});
{tl_sous}
tl.set({{}}, {{}}, {fin:.3f});
window.__timelines["main"] = tl;
</script>
</body></html>
'''

for i, v in enumerate(T):
    if len(sys.argv) > 1 and v["cle"] not in sys.argv[1:]: continue
    voix = os.path.join(ICI, "voix", v["cle"] + ".mp3")
    if not os.path.exists(voix): print("pas de voix", v["cle"]); continue
    d = os.path.join(ICI, "projets", v["cle"]); a = os.path.join(d, "assets"); os.makedirs(a, exist_ok=True)
    for f in ["gsap.min.js", "Inter-600.woff2", "Inter-800.woff2", "logo.png"]:
        shutil.copy(os.path.join(ICI, "commun", f), a)
    shutil.copy(os.path.join(CHEFS, CHEF[v["cle"]]), os.path.join(a, "chef.webp"))
    for n in v["ecrans"]: shutil.copy(os.path.join(GAL, n + ".png"), a)
    shutil.copy(voix, os.path.join(a, "voix.mp3"))
    D = duree(voix)
    open(os.path.join(d, "index.html"), "w").write(page(i, v, D))
    json.dump({"$schema": "https://hyperframes.heygen.com/schema/hyperframes.json", "paths": {"assets": "assets"}}, open(os.path.join(d, "hyperframes.json"), "w"))
    json.dump({"id": v["cle"], "name": v["cle"]}, open(os.path.join(d, "meta.json"), "w"))
    print(v["cle"], round(D, 2))
