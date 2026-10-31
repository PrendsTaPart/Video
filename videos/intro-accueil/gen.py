# Génère l'intro cinématographique de l'accueil (HyperFrames) en 16:9 et en 9:16.
# python3 gen.py  ->  index.html (1920x1080) et mobile/index.html (1080x1920)
import math, os

CARDS = ["foodeatup-caisse-mobile", "rapidocrm", "application-haccp", "plan-it", "rapidomeet", "foodeatup-menu-digital",
         "citycar", "foodeatup-kds", "braindcode", "publisher-bot", "rapidoin", "salle-live", "alto", "foodeatup-fidelite"]

FMT = {
    "landscape": dict(W=1920, H=1080, out="index.html", phone=(330, 690), phoneY=120, cap_y=880, cap_size=58, R=760,
                      cardW=470, cardH=294, ys=(-230, 0, 230), home="assets/accueil-desktop.jpg", dive=3.5, clip=34, chatzoom=1.22, chatx=330, chaty=40, c2css="left: 140px; top: 330px; width: 760px; text-align: left;", av=(20, 640, 440), capcss="left: 480px; width: 1360px;",
                      persp=1700),
    "portrait": dict(W=1080, H=1920, out="mobile/index.html", phone=(410, 860), phoneY=470, cap_y=130, cap_size=66, R=560,
                     cardW=420, cardH=262, ys=(-260, 40, 330), home="assets/accueil-mobile.jpg", dive=2.75, clip=6, chatzoom=1.0, chatx=0, chaty=0, c2css="", av=(-30, 1460, 470), capcss="",
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
        ("c2", 4.4, 4.2, "Je décris. <mark>Claude</mark> construit.", "Une caisse, un CRM, une appli d'hygiène…"),
        ("c3", 9.2, 4.2, "46 projets. 130+ <mark>vidéos</mark>.", "Construits avec l'IA, sans bureau."),
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
      #screen > img {{ position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: top; }}
      #glass {{ position: absolute; inset: 0; background: linear-gradient(120deg, rgba(255,255,255,.18) 0%, rgba(255,255,255,0) 35%); }}
      #punch {{ position: absolute; left: 50%; top: {pw * .045:.0f}px; width: {pw * .045:.0f}px; height: {pw * .045:.0f}px; margin-left: {-pw * .0225:.0f}px; border-radius: 50%; background: #05070a; box-shadow: 0 0 0 3px #11151b; z-index: 5; }}
      #chat {{ position: absolute; inset: 0; background: #f5f4ee; color: #1f1e1d; font-family: Inter, sans-serif; padding: {pw * .17:.0f}px {pw * .05:.0f}px 0; font-size: {pw * .042:.1f}px; line-height: 1.38; }}
      #chat .hd {{ display: flex; align-items: center; justify-content: center; gap: 8px; padding-bottom: {pw * .03:.0f}px; border-bottom: 1px solid #e3e0d6; }}
      #chat .hd img {{ height: {pw * .055:.0f}px; }}
      #chat .rec {{ position: absolute; right: {pw * .05:.0f}px; top: {pw * .095:.0f}px; font-size: {pw * .026:.1f}px; color: #5f5b52; border: 1px solid #b9b3a5; border-radius: 99px; padding: 1px 8px; }}
      #ubub {{ margin: {pw * .05:.0f}px 0 0 auto; width: 82%; background: #e8e4d8; border-radius: {pw * .045:.0f}px; padding: {pw * .03:.0f}px {pw * .04:.0f}px; }}
      #rep {{ margin-top: {pw * .045:.0f}px; }}
      #rep .w {{ display: inline-block; margin-right: .28em; font-style: normal; }}
      #art {{ margin-top: {pw * .04:.0f}px; border: 1px solid #ddd8cb; border-radius: {pw * .04:.0f}px; overflow: hidden; background: #fff; box-shadow: 0 6px 18px rgba(0,0,0,.08); }}
      #art .ah {{ display: flex; justify-content: space-between; align-items: center; padding: {pw * .025:.0f}px {pw * .035:.0f}px; font-weight: 700; font-size: {pw * .036:.1f}px; }}
      #art .ah span {{ font-weight: 600; font-size: {pw * .03:.1f}px; color: #9a3d22; background: #fbe9e2; border-radius: 99px; padding: 1px 8px; }}
      #art .shot {{ height: {pw * .5:.0f}px; overflow: hidden; }}
      #art .shot img {{ position: static; width: 100%; height: auto; display: block; }}
      #inp {{ position: absolute; left: {pw * .05:.0f}px; right: {pw * .05:.0f}px; bottom: {pw * .07:.0f}px; display: flex; align-items: center; justify-content: space-between; background: #fff; border: 1px solid #ddd8cb; border-radius: {pw * .06:.0f}px; padding: {pw * .03:.0f}px {pw * .04:.0f}px; color: #6b665c; }}
      #inp b {{ width: {pw * .075:.0f}px; height: {pw * .075:.0f}px; border-radius: 50%; background: #d97757; display: inline-block; }}
      .cap .capin {{ {f["capcss"]} }}
      .cap#c2 .capin {{ {f["c2css"]} }}
      #av {{ position: absolute; left: {f["av"][0]}px; top: {f["av"][1]}px; width: {f["av"][2]}px; height: {f["av"][2]}px; }}
      #av img {{ position: absolute; inset: 0; width: 100%; height: 100%; object-fit: contain; filter: drop-shadow(0 20px 40px rgba(0,0,0,.55)); }}
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
              <div id="chat">
                <div class="hd"><img src="assets/logo-claude.webp" alt="Claude" /></div><span class="rec">reconstitution</span>
                <div id="ubub">Construis-moi une caisse pour mon restaurant, sur le téléphone de mes équipiers.</div>
                <div id="rep"><i class="w" id="w0">Je</i><i class="w" id="w1">m'en</i><i class="w" id="w2">occupe.</i><i class="w" id="w3">Commande</i><i class="w" id="w4">à</i><i class="w" id="w5">table,</i><i class="w" id="w6">envoi</i><i class="w" id="w7">en</i><i class="w" id="w8">cuisine,</i><i class="w" id="w9">addition</i><i class="w" id="w10">même</i><i class="w" id="w11">sans</i><i class="w" id="w12">réseau.</i><i class="w" id="w13">Voici</i><i class="w" id="w14">ta</i><i class="w" id="w15">caisse</i><i class="w" id="w16">:</i></div>
                <div id="art"><div class="ah">FoodEatUp Caisse Mobile<span>Aperçu</span></div><div class="shot"><img src="assets/d-foodeatup-caisse-mobile.jpg" alt="Écran réel de FoodEatUp Caisse Mobile" /></div></div>
                <div id="inp">Répondre à Claude…<b></b></div>
              </div>
              <img id="scrHome" src="assets/accueil-mobile.jpg" alt="Accueil du site" />
              <div id="glass"></div>
            </div></div>
          </div>
        </div>
      </div>
{caps_html}
      <div id="home" class="clip" data-start="16.6" data-duration="3.4" data-track-index="9"><img id="homeImg" src="{f["home"]}" alt="Accueil de michael.foodeatup.fr" /></div>
      <audio id="voix1" src="assets/voix/v1.wav" data-start="0.7" data-duration="2.05" data-track-index="21" data-volume="1"></audio>
      <audio id="voix2" src="assets/voix/v2.wav" data-start="4.3" data-duration="2.23" data-track-index="22" data-volume="1"></audio>
      <audio id="voix3" src="assets/voix/v3.wav" data-start="6.6" data-duration="2.89" data-track-index="23" data-volume="1"></audio>
      <audio id="voix4" src="assets/voix/v4.wav" data-start="9.5" data-duration="3.38" data-track-index="24" data-volume="1"></audio>
      <audio id="voix5" src="assets/voix/v5.wav" data-start="14.3" data-duration="2.45" data-track-index="25" data-volume="1"></audio>
      <audio id="voix6" src="assets/voix/v6.wav" data-start="17.3" data-duration="1.08" data-track-index="26" data-volume="1"></audio>
      <div id="avatar" class="clip" data-start="0" data-duration="19.4" data-track-index="10" data-layout-allow-overflow><div id="av"><img id="p1" src="assets/avatar-02-salut.png" alt="Avatar 3D de Michael" /><img id="p2" src="assets/avatar-08-idee.png" alt="Avatar 3D de Michael" /><img id="p3" src="assets/avatar-06-ordinateur.png" alt="Avatar 3D de Michael" /><img id="p4" src="assets/avatar-10-celebration.png" alt="Avatar 3D de Michael" /><img id="p5" src="assets/avatar-04-presentation.png" alt="Avatar 3D de Michael" /><img id="p6" src="assets/avatar-01-bienvenue.png" alt="Avatar 3D de Michael" /></div></div>
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
      tl.fromTo("#chat", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.5 }}, 3.7);
      tl.fromTo("#ubub", {{ y: 24, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.45, ease: E }}, 4.2);
      document.querySelectorAll("#rep .w").forEach((w, j) => tl.fromTo(w, {{ opacity: 0 }}, {{ opacity: 1, duration: 0.12 }}, 4.9 + j * 0.07));
      tl.fromTo("#art", {{ y: 30, opacity: 0, scale: 0.94 }}, {{ y: 0, opacity: 1, scale: 1, duration: 0.55, ease: E }}, 6.15);
      tl.fromTo("#art .shot img", {{ clipPath: "inset(0% 0% 100% 0%)" }}, {{ clipPath: "inset(0% 0% 0% 0%)", duration: 0.8, ease: "power2.out" }}, 6.4);
      tl.fromTo("#scrHome", {{ opacity: 0 }}, {{ opacity: 0, duration: 0.01 }}, 0);
      tl.to("#phoneWrap", {{ rotationY: -6, rotationX: 0, scale: {f["chatzoom"]}, x: {f["chatx"]}, y: {f["chaty"]}, duration: 0.9, ease: IO }}, 3.6);
      tl.to("#phoneWrap", {{ rotationY: 12, rotationX: 4, scale: 1, x: 0, y: 0, duration: 1.2, ease: IO }}, 7.0);

      // Acte 2 et 3 : les projets s'envolent du téléphone et forment un anneau autour de lui
      for (let i = 0; i < N; i++) {{
        const a = document.getElementById("a" + i);
        gsap.set(a, {{ rotationY: +a.dataset.ang, y: +a.dataset.y }});
        tl.fromTo("#k" + i, {{ z: 0, scale: 0.12, opacity: 0 }}, {{ z: R, scale: 1, opacity: 1, duration: 1.1, ease: E }}, 7.1 + i * 0.26);
      }}
      tl.fromTo("#ring", {{ rotationY: 0 }}, {{ rotationY: -130, duration: 9, ease: "none" }}, 7.1);
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
      [["#c1", 0.7, 3.4], ["#c2", 4.4, 4.2], ["#c3", 9.2, 4.2], ["#c4", 14.3, 2.6]].forEach(([c, s, d]) => {{
        tl.fromTo(c + " .capin", {{ y: 30, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.55, ease: E }}, s + 0.05);
        tl.to(c + " .capin", {{ y: -20, opacity: 0, duration: 0.35, ease: "power2.in" }}, s + d - 0.4);
      }});


      // Avatar 3D de Michael : il présente l'histoire, une pose par acte
      const P = [["#p1", 0.3], ["#p2", 3.9], ["#p3", 7.0], ["#p4", 9.2], ["#p5", 14.2], ["#p6", 16.7]];
      gsap.set(["#p2", "#p3", "#p4", "#p5", "#p6"], {{ opacity: 0 }});
      tl.fromTo("#av", {{ y: 260, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.7, ease: "back.out(1.4)" }}, 0.3);
      P.slice(1).forEach(([id, t], k) => {{
        tl.to(P[k][0], {{ opacity: 0, duration: 0.25 }}, t);
        tl.fromTo(id, {{ opacity: 0, scale: 0.92, y: 18 }}, {{ opacity: 1, scale: 1, y: 0, duration: 0.35, ease: "back.out(2)" }}, t);
      }});
      tl.fromTo("#av", {{ rotation: 0 }}, {{ rotation: 2, duration: 1.6, ease: "sine.inOut", yoyo: true, repeat: 9 }}, 1.0);
      tl.to("#av", {{ y: 320, opacity: 0, duration: 0.6, ease: "power2.in" }}, 18.7);
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
