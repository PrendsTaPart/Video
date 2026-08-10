#!/usr/bin/env python3
"""Génère les projets d'assemblage des vidéos tutoriels.

Structure (validée sur v01-fidelite, + voix off ajoutée le 2026-08-10) :

    HOOK       0 → 3 s          carton chiffré + voix off qui lit le hook
    PROBLÈME   3 → 3+P          plan Higgsfield MUET + voix off qui pose la douleur
    DÉMO       … → …+D          logiciel en bas + avatar HeyGen par-dessus qui présente
    PUNCHLINE  … → …+5,2 s      carton logo + voix off de la punchline

Trois couches audio, donc du son du début à la fin :
  1. les voix off (hook, problème)          — ElevenLabs, voix Adam FR
  2. la voix de l'avatar / de la punchline  — piste des mp4 correspondants
  3. un lit d'ambiance continu              — sous tout le reste, ~20 dB sous la voix

Les plans Higgsfield sont montés SANS piste audio (ils n'en ont pas : produits pour le
film héros 16:9 dont le son est monté à part).
"""
import pathlib
import shutil
import subprocess

ROOT = pathlib.Path("/home/user/Video")
BASE = ROOT / "videos/foodeatup-cas-concrets"
MOTION = BASE / "motion"
AUDIO = MOTION / "assets/audio/norm"
INBOX = BASE / "_heygen-inbox"
PROB = pathlib.Path(
    "/tmp/claude-0/-home-user-Video/7b547880-00a2-54cd-816c-b0b5d5dfda3c/scratchpad/prob"
)
BED = ROOT / "videos/planit-product-launch/assets/music/planit-ambient-pad.mp3"

# slug, n, plan_probleme, duree_probleme, projet_tuto, media_start, clip_avatar, duree_avatar
VIDEOS = [
    ("t01-ingredients", "01",
     "hero-directeur-sept-onglets-916.mp4", 8.0,
     "foodeatup-ingredients-tuto", 85, "gen-1_1786317231351.mp4", 10.22),
    ("t02-recettes", "02",
     "hero-chef-carnet-dlc-916.mp4", 6.0,
     "foodeatup-recettes-tuto", 74, "gen-2_1786317254794.mp4", 12.14),
    ("t03-fournisseurs", "03",
     "hero-directeur-sept-onglets-916.mp4", 8.0,
     "foodeatup-fournisseurs-tuto", 44, "gen-3_1786317280068.mp4", 9.24),
    ("t04-mes-commandes", "04",
     "hero-serveur-trois-tablettes-916.mp4", 6.0,
     "foodeatup-mes-commandes-tuto", 20, "gen-4_1786317311124.mp4", 9.24),
    ("t05-mcp-claude", "05",
     "hero-directeur-bureau-matin-916.mp4", 8.0,
     "foodeatup-mcp-tuto", 30, "gen-5_1786325920661.mp4", 9.35),
    ("t06-employes", "06",
     "hero-brigade-deux-langues-916.mp4", 8.0,
     "foodeatup-employes-tuto", 38, "gen-6_1786325937242.mp4", 9.47),
]

HOOK = 3.0
PUNCH = 5.2
QUEUE = 2.0      # temps où le logiciel reste seul après la réplique de l'avatar
BED_VOL = 0.45   # le pad est déjà à -31,8 dB : ça le pose ~20 dB sous la voix

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
      <!-- ================= IMAGE ================= -->

      <!-- HOOK 0–{hook} s -->
      <video id="seg-hook" class="clip full" data-start="0" data-duration="{hook}"
             data-track-index="0" src="assets/hook/hook.mp4" muted playsinline></video>

      <!-- PROBLÈME {p0}–{d0} s — plan MUET (aucune piste audio dans la source) -->
      <video id="seg-probleme" class="clip full" data-start="{p0}" data-duration="{pdur}"
             data-track-index="0" data-media-start="0"
             src="assets/higgsfield/probleme.mp4" muted playsinline></video>

      <!-- DÉMO {d0}–{u0} s : logiciel en bas, avatar par-dessus qui le présente -->
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

      <!-- PUNCHLINE {u0}–{total} s -->
      <video id="seg-punchline" class="clip full" data-start="{u0}" data-duration="{punch}"
             data-track-index="0" data-media-start="0"
             src="assets/punchline/punchline.mp4" muted playsinline></video>

      <!-- ================= SON ================= -->

      <!-- lit d'ambiance continu, sous tout le reste -->
      <audio id="bed" src="assets/audio/bed.mp3"
             data-start="0" data-duration="{total}" data-media-start="0"
             data-track-index="8" data-volume="{bed_vol}"></audio>

      <!-- voix off du hook -->
      <audio id="vo-hook" src="assets/audio/vo-hook.mp3"
             data-start="0.05" data-duration="{vo_hook}" data-media-start="0"
             data-track-index="10" data-volume="1"></audio>

      <!-- voix off du bloc problème -->
      <audio id="vo-prob" src="assets/audio/vo-prob.mp3"
             data-start="{vp0}" data-duration="{vo_prob}" data-media-start="0"
             data-track-index="11" data-volume="1"></audio>

      <!-- voix de l'avatar -->
      <audio id="vo-avatar" src="assets/audio/vo-avatar.mp3"
             data-start="{a0}" data-duration="{adur}" data-media-start="0"
             data-track-index="12" data-volume="1"></audio>

      <!-- voix off de la punchline (déjà dans le mp4 du carton) -->
      <audio id="vo-punch" src="assets/audio/vo-punch.mp3"
             data-start="{u0}" data-duration="{punch}" data-media-start="0"
             data-track-index="12" data-volume="1"></audio>
    </div>

    <script>
      window.__timelines = window.__timelines || {{}};

      gsap.set("#demo-screen", {{ opacity: 0, y: -12 }});
      gsap.set("#demo-accent", {{ xPercent: -50, scaleX: 0, transformOrigin: "50% 50%" }});
      gsap.set("#demo-avatar", {{ opacity: 0, scale: 1.04, transformOrigin: "50% 0%" }});

      // temps ABSOLUS sur le timeline racine (le bloc démo commence à {d0} s)
      const D = {d0};
      const tl = gsap.timeline({{ paused: true }});
      tl.to("#demo-screen", {{ opacity: 1, y: 0, duration: 0.5, ease: "power2.out" }}, D);
      tl.to("#demo-accent", {{ xPercent: -50, scaleX: 1, duration: 0.4, ease: "power2.out" }}, D + 0.4);
      tl.to("#demo-avatar", {{ opacity: 1, scale: 1, duration: 0.4, ease: "power2.out" }}, D + 0.3);
      tl.to("#demo-avatar", {{ opacity: 0, duration: 0.5, ease: "power2.in" }}, D + 0.3 + {adur} - 0.5);
      // le lit d'ambiance se retire doucement sur la toute fin
      tl.to("#bed", {{ volume: 0, duration: 1.0, ease: "power1.in" }}, {total} - 1.0);

      window.__timelines["{slug}"] = tl;
    </script>
  </body>
</html>
"""


def dur(path):
    return float(subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", str(path)], capture_output=True, text=True).stdout.strip())


for slug, n, prob_src, pdur, tuto, ms, avatar, adur in VIDEOS:
    gen = avatar.split('_')[0].replace('-', '')  # 'gen3'
    proj = BASE / slug
    for sub in ("assets/hook", "assets/higgsfield", "assets/solution", "assets/heygen",
                "assets/punchline", "assets/audio", "assets/vendor", "renders"):
        (proj / sub).mkdir(parents=True, exist_ok=True)

    shutil.copy(MOTION / f"renders/hook-t{n}.mp4", proj / "assets/hook/hook.mp4")
    shutil.copy(PROB / prob_src, proj / "assets/higgsfield/probleme.mp4")
    shutil.copy(ROOT / "videos" / tuto / "assets/screen.mp4", proj / "assets/solution/screen.mp4")
    shutil.copy(INBOX / avatar, proj / "assets/heygen/resultat.mp4")
    shutil.copy(MOTION / "renders/punchline-outro.mp4", proj / "assets/punchline/punchline.mp4")
    shutil.copy(MOTION / "assets/vendor/gsap.min.js", proj / "assets/vendor/gsap.min.js")
    shutil.copy(AUDIO / f"vo-hook-t{n}.mp3", proj / "assets/audio/vo-hook.mp3")
    shutil.copy(AUDIO / f"vo-prob-t{n}.mp3", proj / "assets/audio/vo-prob.mp3")
    shutil.copy(AUDIO / f"vo-avatar-{gen}.mp3", proj / "assets/audio/vo-avatar.mp3")
    shutil.copy(MOTION / "assets/audio/norm/punchline-vo.mp3",
                proj / "assets/audio/vo-punch.mp3")
    shutil.copy(BED, proj / "assets/audio/bed.mp3")

    wh = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
         "stream=width,height", "-of", "csv=p=0", str(proj / "assets/solution/screen.mp4")],
        capture_output=True, text=True).stdout.strip()
    w, h = (int(x) for x in wh.split(","))
    screen_h = 1080 * h / w

    vo_hook = dur(proj / "assets/audio/vo-hook.mp3")
    vo_prob = dur(proj / "assets/audio/vo-prob.mp3")

    p0 = HOOK
    d0 = round(HOOK + pdur, 2)
    demo = round(adur + QUEUE, 2)
    u0 = round(d0 + demo, 2)
    total = round(u0 + PUNCH, 2)
    a0 = round(d0 + 0.3, 2)
    vp0 = round(p0 + 0.15, 2)

    (proj / "index.html").write_text(TPL.format(
        slug=slug, total=total, hook=HOOK, p0=p0, pdur=pdur, d0=d0, demo=demo,
        ms=ms, a0=a0, adur=adur, u0=u0, punch=PUNCH, screen_h=screen_h,
        vo_hook=round(vo_hook, 2), vo_prob=round(vo_prob, 2), vp0=vp0, bed_vol=BED_VOL,
    ), encoding="utf-8")

    (proj / "meta.json").write_text('{"id":"%s","name":"%s"}' % (slug, slug), encoding="utf-8")
    (proj / "hyperframes.json").write_text(
        '{"$schema":"https://hyperframes.heygen.com/schema/hyperframes.json",'
        '"paths":{"blocks":"compositions","components":"compositions/components",'
        '"assets":"assets"},"media":{"autoProxy":true},'
        '"authoringSkill":"general-video"}', encoding="utf-8")

    # contrôle : la voix off tient-elle dans son bloc ?
    warn = ""
    if vo_hook > HOOK + 0.4:
        warn += f"  ⚠ VO hook {vo_hook:.2f}s > bloc {HOOK}s"
    if vo_prob > pdur:
        warn += f"  ⚠ VO problème {vo_prob:.2f}s > bloc {pdur}s"
    print(f"{slug:20s} total={total:5.1f}s  hook_vo={vo_hook:.2f}  prob_vo={vo_prob:.2f}"
          f"  demo={demo:.2f}{warn}")
