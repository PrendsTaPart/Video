# Génère l'intro cinématographique de l'accueil (HyperFrames) en 16:9 et en 9:16.
# python3 gen.py  ->  index.html (1920x1080) et mobile/index.html (1080x1920)
import math, os

CARDS = ["foodeatup-caisse-mobile", "rapidocrm", "application-haccp", "plan-it", "rapidomeet", "foodeatup-menu-digital",
         "citycar", "foodeatup-kds", "braindcode", "publisher-bot", "rapidoin", "salle-live", "alto", "foodeatup-fidelite"]

FMT = {
    "landscape": dict(W=1920, H=1080, out="index.html", phone=(330, 690), phoneY=120, cap_y=880, cap_size=58, R=760,
                      cardW=470, cardH=294, ys=(-230, 0, 230), home="assets/accueil-desktop.jpg", dive=3.5, clip=34,
                      persp=1700),
    "portrait": dict(W=1080, H=1920, out="mobile/index.html", phone=(410, 860), phoneY=470, cap_y=130, cap_size=66, R=560,
                     cardW=420, cardH=262, ys=(-260, 40, 330), home="assets/accueil-mobile.jpg", dive=2.75, clip=6,
                     persp=1500),
}


def build(f):
    W, H = f["W"], f["H"]
    pw, ph = f["phone"]
    px, py = (W - pw) / 2, f["phoneY"]
    cx, cy = W / 2, py + ph / 2
    n = len(CARDS)
    arms = []
    for i, s in enumerate(CARDS):
        ang = i * 360 / n
        y = f["ys"][i % 3]
        arms.append(f'''          <div class="arm" id="a{i}" data-ang="{ang:.1f}" data-y="{y}"><div class="card" id="k{i}"><img src="assets/d-{s}.jpg" alt="{s}" /></div></div>''')
    arms = "\n".join(arms)
    caps = [
        ("c1", 0.7, 3.4, "Un soir. Un <mark>téléphone</mark>.", ""),
        ("c2", 4.4, 4.0, "Une idée. Puis une <mark>autre</mark>.", "Une caisse, un CRM, une appli d'hygiène…"),
        ("c3", 9.0, 4.5, "46 projets. 130+ <mark>vidéos</mark>.", "Construits avec l'IA, sans bureau."),
        ("c4", 14.3, 2.6, "Tout ce que vous voyez ici est né sur mon <mark>téléphone</mark>.", ""),
    ]
    caps_html = "\n".join(
        f'''      <div id="{c}" class="clip cap" data-start="{s}" data-duration="{d}" data-track-index="{5 + k}"><div class="capin"><h1>{t}</h1>{f"<p>{sub}</p>" if sub else ""}</div></div>'''
        for k, (c, s, d, t, sub) in enumerate(caps))
    return f'''<!doctype html>
<html lang="fr">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width={W}, height={H}" />
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script>
    <style>
      :root {{ --ground: #05080d; --navy: #0b2f57; --ink: #fff; --mute: #aeb8c2; --accent: #ffa500; --blue: #0a7bff; --font-display: Poppins, sans-serif; }}
      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      html, body {{ width: {W}px; height: {H}px; overflow: hidden; background: var(--ground); }}
      #root {{ position: relative; width: {W}px; height: {H}px; overflow: hidden; font-family: var(--font-display); color: var(--ink); }}
      .clip {{ position: absolute; inset: 0; }}
      #bg {{ background: radial-gradient(ellipse at 50% 55%, #0c1d33 0%, var(--ground) 70%); }}
      #sweep {{ position: absolute; left: -40%; top: -20%; width: 60%; height: 140%; background: linear-gradient(100deg, rgba(10,123,255,0) 0%, rgba(10,123,255,.22) 45%, rgba(255,255,255,.10) 50%, rgba(10,123,255,.22) 55%, rgba(10,123,255,0) 100%); }}
      #floor {{ position: absolute; left: 0; right: 0; bottom: 0; height: 35%; background: radial-gradient(ellipse at 50% 0%, rgba(10,123,255,.18), rgba(0,0,0,0) 60%); }}
      #stage {{ perspective: {f["persp"]}px; perspective-origin: 50% 45%; }}
      #world {{ position: absolute; inset: 0; transform-style: preserve-3d; }}
      #ring {{ position: absolute; left: {cx}px; top: {cy}px; width: 0; height: 0; transform-style: preserve-3d; }}
      .arm {{ position: absolute; left: 0; top: 0; transform-style: preserve-3d; }}
      .card {{ position: absolute; left: {-f["cardW"] / 2}px; top: {-f["cardH"] / 2}px; width: {f["cardW"]}px; height: {f["cardH"]}px; border-radius: 18px; overflow: hidden; background: #111; box-shadow: 0 30px 70px rgba(0,0,0,.6), 0 0 0 2px rgba(255,255,255,.08); backface-visibility: hidden; }}
      .card img {{ width: 100%; height: 100%; object-fit: cover; object-position: top; }}
      #phoneWrap {{ position: absolute; left: {px}px; top: {py}px; width: {pw}px; height: {ph}px; transform-style: preserve-3d; }}
      #phone {{ position: absolute; inset: 0; border-radius: {pw * .13:.0f}px; background: linear-gradient(145deg, #39404c, #07090c 55%, #1b2029); padding: {pw * .022:.0f}px; box-shadow: 0 60px 140px rgba(0,0,0,.75), inset 0 0 0 2px rgba(255,255,255,.10); }}
      #screen {{ position: relative; width: 100%; height: 100%; border-radius: {pw * .112:.0f}px; overflow: hidden; background: #000; }}
      #screen img {{ position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: top; }}
      #glass {{ position: absolute; inset: 0; background: linear-gradient(120deg, rgba(255,255,255,.18) 0%, rgba(255,255,255,0) 35%); }}
      #punch {{ position: absolute; left: 50%; top: {pw * .045:.0f}px; width: {pw * .045:.0f}px; height: {pw * .045:.0f}px; margin-left: {-pw * .0225:.0f}px; border-radius: 50%; background: #05070a; box-shadow: 0 0 0 3px #11151b; z-index: 5; }}
      #home {{ background: #0f1a23; }}
      #home img {{ width: 100%; height: 100%; object-fit: cover; }}
      .cap {{ display: flex; justify-content: center; }}
      .capin {{ position: absolute; top: {f["cap_y"]}px; width: {W * .86:.0f}px; text-align: center; }}
      .cap h1 {{ font-size: {f["cap_size"]}px; font-weight: 800; letter-spacing: -1.5px; line-height: 1.12; text-shadow: 0 6px 30px rgba(0,0,0,.8); }}
      .cap p {{ margin-top: 14px; font-size: {f["cap_size"] * .52:.0f}px; font-weight: 600; color: var(--mute); text-shadow: 0 4px 20px rgba(0,0,0,.9); }}
      mark {{ background: var(--accent); color: #0b1520; border-radius: 14px; padding: 0 14px; text-shadow: none; }}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="20" data-width="{W}" data-height="{H}">
      <div id="bg" class="clip" data-start="0" data-duration="20" data-track-index="0"><div id="sweep"></div><div id="floor"></div></div>
      <div id="stage" class="clip" data-start="0" data-duration="19" data-track-index="1" data-layout-allow-overlap data-layout-allow-overflow>
        <div id="world">
          <div id="ring">
{arms}
          </div>
          <div id="phoneWrap">
            <div id="phone"><div id="screen"><div id="punch"></div>
              <img id="scrApp" src="assets/m-caisse.jpg" alt="FoodEatUp Caisse Mobile" />
              <img id="scrHome" src="assets/accueil-mobile.jpg" alt="Accueil du site" />
              <div id="glass"></div>
            </div></div>
          </div>
        </div>
      </div>
{caps_html}
      <div id="home" class="clip" data-start="16.6" data-duration="3.4" data-track-index="9"><img id="homeImg" src="{f["home"]}" alt="Accueil de michael.foodeatup.fr" /></div>
    </div>
    <script>
      window.__timelines = window.__timelines || {{}};
      const tl = gsap.timeline({{ paused: true }});
      const E = "power3.out", IO = "power3.inOut";
      const N = {n}, R = {f["R"]};

      // Lumière qui balaie la scène
      tl.fromTo("#sweep", {{ xPercent: 0 }}, {{ xPercent: 330, duration: 9, ease: "sine.inOut" }}, 0);
      tl.to("#sweep", {{ xPercent: 0, duration: 9, ease: "sine.inOut" }}, 9);

      // Acte 1 : le téléphone sort de l'ombre en tournant, écran éteint
      tl.fromTo("#phoneWrap", {{ rotationY: -68, rotationX: 14, z: -900, opacity: 0.35 }}, {{ rotationY: -18, rotationX: 6, z: 0, opacity: 1, duration: 3.6, ease: E }}, 0);
      tl.fromTo("#scrApp", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.5 }}, 3.9);
      tl.fromTo("#scrHome", {{ opacity: 0 }}, {{ opacity: 0, duration: 0.01 }}, 0);
      tl.to("#phoneWrap", {{ rotationY: 14, rotationX: 4, duration: 5, ease: "sine.inOut" }}, 3.6);

      // Acte 2 et 3 : les projets s'envolent du téléphone et forment un anneau autour de lui
      for (let i = 0; i < N; i++) {{
        const a = document.getElementById("a" + i);
        gsap.set(a, {{ rotationY: +a.dataset.ang, y: +a.dataset.y }});
        tl.fromTo("#k" + i, {{ z: 0, scale: 0.12, opacity: 0 }}, {{ z: R, scale: 1, opacity: 1, duration: 1.1, ease: E }}, 4.6 + i * 0.32);
      }}
      tl.fromTo("#ring", {{ rotationY: 0 }}, {{ rotationY: -150, duration: 10, ease: "none" }}, 4.6);
      tl.to("#phoneWrap", {{ rotationY: -10, rotationX: 2, duration: 4.4, ease: "sine.inOut" }}, 8.6);

      // Acte 4 : l'anneau s'ouvre, l'écran passe sur l'accueil du site, la caméra plonge dans le téléphone
      tl.to(".card", {{ z: R * 2.4, opacity: 0, duration: 1.0, ease: "power2.in", stagger: 0.02 }}, 13.3);
      tl.to("#scrHome", {{ opacity: 1, duration: 0.6 }}, 14.3);
      tl.to("#phoneWrap", {{ rotationY: 0, rotationX: 0, duration: 1.2, ease: IO }}, 14.2);
      tl.to("#phoneWrap", {{ scale: {f["dive"]} * 0.6, duration: 1.6, ease: "power2.in" }}, 15.0);
      tl.to("#phoneWrap", {{ opacity: 0, duration: 0.35 }}, 16.75);
      tl.to("#bg", {{ opacity: 0.4, duration: 2 }}, 15.2);

      // Acte 5 : l'accueil réel prend tout l'écran, puis le site s'affiche
      tl.fromTo("#home", {{ clipPath: "inset(2% {f["clip"]}% 2% {f["clip"]}% round 70px)" }}, {{ clipPath: "inset(0% 0% 0% 0% round 0px)", duration: 1.1, ease: "power3.inOut" }}, 16.6);
      tl.fromTo("#homeImg", {{ scale: 1.12 }}, {{ scale: 1, duration: 2.4, ease: "power2.out" }}, 16.6);

      // Légendes : entrée et sortie
      [["#c1", 0.7, 3.4], ["#c2", 4.4, 4.0], ["#c3", 9.0, 4.5], ["#c4", 14.3, 2.6]].forEach(([c, s, d]) => {{
        tl.fromTo(c + " .capin", {{ y: 30, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.55, ease: E }}, s + 0.05);
        tl.to(c + " .capin", {{ y: -20, opacity: 0, duration: 0.35, ease: "power2.in" }}, s + d - 0.4);
      }});

      window.__timelines["main"] = tl;
      tl.seek(0);
    </script>
  </body>
</html>
'''


for k, f in FMT.items():
    os.makedirs(os.path.dirname(f["out"]) or ".", exist_ok=True)
    open(f["out"], "w").write(build(f))
    print("écrit", f["out"])
