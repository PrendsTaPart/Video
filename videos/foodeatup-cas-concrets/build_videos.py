#!/usr/bin/env python3
"""Génère les projets d'assemblage des vidéos tutoriels (structure validée sur v01)."""
import pathlib
import shutil
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[2]
BASE = ROOT / "videos/foodeatup-cas-concrets"
MOTION = BASE / "motion"
INBOX = BASE / "_heygen-inbox"
HERO = ROOT / "hero-video/assets/video"
PROB = BASE / ".cache/probleme-916"

# Les plans de hero-video/ sont en 1280x720 paysage (produits pour le film 16:9). Pour les
# monter en 9:16 sans les recadrer — ce qui couperait justement ce qui les rend lisibles —
# on les place au centre d'un fond flouté et assombri tiré du plan lui-même (pillarbox).
# Solution d'attente : un plan nativement vertical reste préférable. Voir SCRIPTS-HEYGEN-30.md.
PILLARBOX = (
    "[0:v]scale=-2:1920,crop=1080:1920,boxblur=32:3,eq=brightness=-0.14:saturation=0.55[bg];"
    "[0:v]scale=1080:-2[fg];[bg][fg]overlay=(W-w)/2:(H-h)/2,format=yuv420p"
)


def make_pillarbox(name):
    """Fabrique (une fois) la version 9:16 d'un plan hero-video. Retourne le chemin."""
    PROB.mkdir(parents=True, exist_ok=True)
    out = PROB / f"{name}-916.mp4"
    if out.exists():
        return out
    subprocess.run(
        ["ffmpeg", "-y", "-i", str(HERO / f"{name}.mp4"), "-filter_complex", PILLARBOX,
         "-c:v", "libx264", "-crf", "18", "-preset", "medium", "-an", str(out)],
        check=True, capture_output=True)
    return out

# slug, hook_render, plan_hero (sans extension), probleme_dur, tuto_projet, media_start, avatar_src, avatar_dur
VIDEOS = [
    ("t01-ingredients", "hook-t01.mp4",
     "hero-directeur-sept-onglets", 8.0,
     "foodeatup-ingredients-tuto", 85, "gen-1_1786317231351.mp4", 10.22),
    ("t02-recettes", "hook-t02.mp4",
     "hero-chef-carnet-dlc", 6.0,
     "foodeatup-recettes-tuto", 74, "gen-2_1786317254794.mp4", 12.14),
    ("t03-fournisseurs", "hook-t03.mp4",
     "hero-directeur-sept-onglets", 8.0,
     "foodeatup-fournisseurs-tuto", 44, "gen-3_1786317280068.mp4", 9.24),
    ("t04-mes-commandes", "hook-t04.mp4",
     "hero-serveur-trois-tablettes", 6.0,
     "foodeatup-mes-commandes-tuto", 20, "gen-4_1786317311124.mp4", 9.24),
]

DEMO = 14.0
PUNCH = 5.2

TPL = """<!doctype html>
<html lang="fr" data-resolution="portrait">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <script src="assets/vendor/gsap.min.js"></script>
    <style>
      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      html, body {{ width: 1080px; height: 1920px; overflow: hidden; background: #000; }}
      .full {{
        position: absolute; inset: 0; width: 1080px; height: 1920px; object-fit: cover;
      }}
      /* Bloc DÉMO — chaque élément est un clip MINUTÉ à part entière : un conteneur sans
         data-start serait peint sur toute la durée de la composition et recouvrirait les
         segments précédents (bug rencontré sur la vidéo 1). */
      #demo-bg {{
        position: absolute; inset: 0; width: 1080px; height: 1920px;
        background: radial-gradient(120% 70% at 50% 0%, #ffffff 0%, #fcf9e6 55%, #f4efd2 100%);
      }}
      #demo-avatar {{
        position: absolute; top: 0; left: 0; width: 1080px; height: 1250px;
        object-fit: cover; object-position: 50% 12%;
      }}
      #demo-accent {{
        position: absolute; left: 50%; top: 1290px; width: 96px; height: 6px;
        background: #ffa500; border-radius: 6px;
      }}
      /* Logiciel en bas, pleine largeur, intégralement — jamais recadré. */
      #demo-screen {{
        position: absolute; top: 1350px; left: 0; width: 1080px; height: {screen_h:.2f}px;
        box-shadow: 0 18px 40px rgba(15, 26, 35, 0.18);
      }}
    </style>
  </head>
  <body>
    <div
      id="root"
      data-composition-id="{slug}"
      data-start="0"
      data-duration="{total}"
      data-width="1080"
      data-height="1920"
    >
      <!-- HOOK 0–3 s -->
      <video id="seg-hook" class="clip full" data-start="0" data-duration="3"
             data-track-index="0" src="assets/hook/hook.mp4" muted playsinline></video>

      <!-- PROBLÈME {p0}–{p1} s -->
      <video id="seg-probleme" class="clip full" data-start="{p0}" data-duration="{pdur}"
             data-track-index="0" data-media-start="0"
             src="assets/higgsfield/probleme.mp4" muted playsinline></video>
      <!-- Pas d'élément <audio> ici : les plans de hero-video/ sont MUETS (produits pour
           le film 16:9, dont le son est monté séparément). Le bloc problème est donc
           silencieux, contrairement à la vidéo 1 dont le plan vertical avait son ambiance.
           À reprendre quand les plans verticaux avec son seront générés. -->

      <!-- DÉMO {d0}–{d1} s : logiciel en bas, avatar par-dessus qui le présente -->
      <div id="demo-bg" class="clip" data-start="{d0}" data-duration="{demo}"
           data-track-index="0"></div>
      <video id="demo-screen" class="clip" data-start="{d0}" data-duration="{demo}"
             data-track-index="1" data-media-start="{ms}"
             src="assets/solution/screen.mp4" muted playsinline></video>
      <div id="demo-accent" class="clip" data-start="{d0}" data-duration="{demo}"
           data-track-index="2"></div>
      <video id="demo-avatar" class="clip" data-start="{a0}" data-duration="{adur}"
             data-track-index="3" data-media-start="0"
             src="assets/heygen/resultat.mp4" muted playsinline></video>
      <audio id="demo-avatar-audio" src="assets/heygen/resultat.mp4"
             data-start="{a0}" data-duration="{adur}" data-media-start="0"
             data-track-index="10" data-volume="1"></audio>

      <!-- PUNCHLINE {u0}–{total} s (voix off incluse) -->
      <video id="seg-punchline" class="clip full" data-start="{u0}" data-duration="{punch}"
             data-track-index="0" data-media-start="0"
             src="assets/punchline/punchline.mp4" muted playsinline></video>
      <audio id="seg-punchline-audio" src="assets/punchline/punchline.mp4"
             data-start="{u0}" data-duration="{punch}" data-media-start="0"
             data-track-index="10" data-volume="1"></audio>
    </div>

    <script>
      window.__timelines = window.__timelines || {{}};

      gsap.set("#demo-screen", {{ opacity: 0, y: -12 }});
      gsap.set("#demo-accent", {{ xPercent: -50, scaleX: 0, transformOrigin: "50% 50%" }});
      gsap.set("#demo-avatar", {{ opacity: 0, scale: 1.04, transformOrigin: "50% 0%" }});

      // temps ABSOLUS sur le timeline racine (le segment démo commence à {d0} s)
      const D = {d0};
      const tl = gsap.timeline({{ paused: true }});
      tl.to("#demo-screen", {{ opacity: 1, y: 0, duration: 0.5, ease: "power2.out" }}, D);
      tl.to("#demo-accent", {{ xPercent: -50, scaleX: 1, duration: 0.4, ease: "power2.out" }}, D + 0.4);
      tl.to("#demo-avatar", {{ opacity: 1, scale: 1, duration: 0.4, ease: "power2.out" }}, D + 0.3);
      tl.to("#demo-avatar", {{ opacity: 0, duration: 0.5, ease: "power2.in" }}, D + 0.3 + {adur} - 0.5);

      window.__timelines["{slug}"] = tl;
    </script>
  </body>
</html>
"""


def probe(path, entries):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", entries, "-of", "csv=p=0", str(path)],
        capture_output=True, text=True).stdout.strip()
    return out


for slug, hook, prob_src, pdur, tuto, ms, avatar, adur in VIDEOS:
    proj = BASE / slug
    for sub in ("assets/hook", "assets/higgsfield", "assets/solution",
                "assets/heygen", "assets/punchline", "assets/vendor", "renders"):
        (proj / sub).mkdir(parents=True, exist_ok=True)

    shutil.copy(MOTION / "renders" / hook, proj / "assets/hook/hook.mp4")
    shutil.copy(make_pillarbox(prob_src), proj / "assets/higgsfield/probleme.mp4")
    shutil.copy(ROOT / "videos" / tuto / "assets/screen.mp4", proj / "assets/solution/screen.mp4")
    shutil.copy(INBOX / avatar, proj / "assets/heygen/resultat.mp4")
    shutil.copy(MOTION / "renders/punchline-outro.mp4", proj / "assets/punchline/punchline.mp4")
    shutil.copy(MOTION / "assets/vendor/gsap.min.js", proj / "assets/vendor/gsap.min.js")

    # hauteur d'affichage du logiciel : largeur pleine (1080) sans déformation
    wh = probe(proj / "assets/solution/screen.mp4", "stream=width,height").split("\n")[0]
    w, h = (int(x) for x in wh.split(","))
    screen_h = 1080 * h / w

    p0, d0 = 3.0, 3.0 + pdur
    u0 = d0 + DEMO
    total = round(u0 + PUNCH, 2)

    (proj / "index.html").write_text(TPL.format(
        slug=slug, total=total, p0=p0, p1=d0, pdur=pdur, d0=d0, d1=u0, demo=DEMO,
        ms=ms, a0=round(d0 + 0.3, 2), adur=adur, u0=u0, punch=PUNCH, screen_h=screen_h,
    ), encoding="utf-8")

    (proj / "meta.json").write_text(
        '{"id":"%s","name":"%s"}' % (slug, slug), encoding="utf-8")
    (proj / "hyperframes.json").write_text(
        '{"$schema":"https://hyperframes.heygen.com/schema/hyperframes.json",'
        '"paths":{"blocks":"compositions","components":"compositions/components",'
        '"assets":"assets"},"media":{"autoProxy":true},'
        '"authoringSkill":"general-video"}', encoding="utf-8")

    print(f"{slug:20s} total={total:5.1f}s  problème={pdur}s  screen_h={screen_h:.0f}px  avatar={adur}s")
