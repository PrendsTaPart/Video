"""Film d'accueil FoodEatUp : vrais écrans en 3D, voix Adam (eleven_v4) comme fil conducteur."""
import html

D = 0.4  # décalage de la voix
FIN = 33.0

# (texte, début, fin) — fins de phrases relevées par silencedetect sur voix.mp3
SOUS = [
    ("Midi. Le coup de feu commence.", 0.0, 2.0),
    ("Vous dites : « Table sept, deux magrets. »", 2.0, 4.30),
    ("La commande part en cuisine, sur le bon poste.", 4.30, 8.17),
    ("Le stock se met à jour.", 8.17, 9.78),
    ("La marge se recalcule.", 9.78, 11.48),
    ("« Frigo trois, quatre degrés. »", 11.48, 14.04),
    ("Le relevé HACCP est enregistré.", 14.04, 16.38),
    ("« Une table de six samedi, vingt heures. »", 16.38, 17.39),
    ("C'est réservé.", 17.39, 18.6),
    ("Et votre post du plat du jour est prêt.", 18.6, 20.0),
    ("Caisse, cuisine, salle, hygiène, communication : tout suit.", 20.16, 24.16),
    ("Tout seul.", 24.16, 25.0),
    ("Une vingtaine d'applications, à votre voix.", 25.0, 27.43),
    ("FoodEatUp. Dites-le. C'est fait.", 27.43, 29.6),
]

# scènes : (id, début, fin, fond, contenu html)
def tel(img, cls=""):
    return f'<div class="tel {cls}"><div class="vitre"><img src="assets/{img}" alt=""></div><div class="encoche"></div></div>'

def tab(img, cls=""):
    return f'<div class="tab {cls}"><div class="vitre"><img src="assets/{img}" alt=""></div></div>'

def pc(img, cls=""):
    return f'<div class="pc {cls}"><div class="ecran"><div class="vitre"><img src="assets/{img}" alt=""></div></div><div class="socle"></div></div>'

def bulle(txt, cls=""):
    return f'<div class="bulle {cls}"><span class="micro"></span>{html.escape(txt)}</div>'

def badge(txt, cls=""):
    return f'<div class="badge {cls}">✓ {html.escape(txt)}</div>'

SCENES = [
    ("sc0", 0.0, 2.1, "bg-hero-service.webp",
     '<div class="heure">12:00</div><h1 class="gros">Midi.<br><em>Le coup de feu.</em></h1>'),
    ("sc1", 2.0, 4.5, "bg-caisse.webp",
     tel("salle.webp", "t-g") + bulle("Table sept, deux magrets.", "b-d")),
    ("sc2", 4.4, 8.3, "bg-cuisine.webp",
     tel("commande.webp", "t-g2") + '<div class="fleche">→</div>' + tel("kds.webp", "t-d2") + badge("Poste chaud", "bd-1")),
    ("sc3", 8.2, 11.6, "bg-stock.webp",
     pc("fabrication.webp", "pc-c") + badge("Stock à jour", "bd-2") + badge("Marge recalculée", "bd-3")),
    ("sc4", 11.5, 16.5, "bg-haccp.webp",
     tel("jarvis.webp", "t-g3") + tel("temperature.webp", "t-d3") + bulle("Frigo trois, quatre degrés.", "b-h") + badge("Relevé HACCP enregistré", "bd-4")),
    ("sc5", 16.4, 18.7, "bg-reservation.webp",
     tel("resa.webp", "t-c") + bulle("Une table de six, samedi 20 h.", "b-r") + badge("Réservé", "bd-5")),
    ("sc6", 18.6, 20.2, "bg-reseaux-sociaux.webp",
     tab("menu.webp", "tab-c") + badge("Post du plat du jour prêt", "bd-6")),
    ("sc7", 20.1, 27.5, "bg-equipe.webp",
     '<div class="orbite" id="orbite">'
     + tel("commande.webp", "o o1") + tab("menu.webp", "o o2") + pc("predibot.webp", "o o3")
     + tel("temperature.webp", "o o4") + tab("recette.webp", "o o5") + tab("fidelite.webp", "o o7")
     + '</div><div class="mots">' + "".join(f'<span class="mot" id="m{i}">{m}</span>' for i, m in enumerate(
         ["Caisse", "Cuisine", "Salle", "Hygiène", "Communication"])) + '</div>'
     '<div class="vingt" id="vingt"><b>20</b> applications, à votre voix</div>'),
    ("sc8", 27.4, FIN, None,
     '<img class="logo-fin" src="assets/logo.png" alt="FoodEatUp"><p class="slogan">Dites-le. <em>C\'est fait.</em></p>'
     '<p class="cta">Essai gratuit · foodeatup.com</p>'),
]

css = """
@font-face { font-family:"Inter"; src:url("assets/Inter-600.woff2"); font-weight:600; }
@font-face { font-family:"Inter"; src:url("assets/Inter-800.woff2"); font-weight:800; }
* { margin:0; padding:0; box-sizing:border-box; }
html, body { width:1920px; height:1080px; overflow:hidden; background:#0F1A23; }
#root { position:relative; width:1920px; height:1080px; overflow:hidden; font-family:"Inter",sans-serif; color:#FCF9E6; background:#0F1A23; }
.scene { position:absolute; inset:0; opacity:0; perspective:2200px; perspective-origin:50% 45%; }
.fond { position:absolute; inset:-60px; background-size:cover; background-position:center; filter:blur(10px) brightness(.38) saturate(1.1); }
.voile { position:absolute; inset:0; background:radial-gradient(900px 700px at 50% 50%, rgba(0,123,255,.18), transparent 70%), linear-gradient(180deg, rgba(15,26,35,.2), rgba(15,26,35,.75)); }
.cam { position:absolute; inset:0; transform-style:preserve-3d; }
.tel { position:absolute; width:380px; height:822px; border-radius:58px; background:#05090D; padding:13px; box-shadow:0 50px 120px rgba(0,0,0,.65), 0 0 0 3px #2A3A47 inset; transform-style:preserve-3d; }
.tel .vitre, .tab .vitre, .pc .vitre { width:100%; height:100%; overflow:hidden; background:#16242F; }
.tel .vitre { border-radius:46px; }
.tel img, .tab img, .pc img { width:100%; height:100%; object-fit:cover; object-position:top; display:block; }
.encoche { position:absolute; left:50%; top:24px; width:110px; height:28px; margin-left:-55px; border-radius:20px; background:#05090D; }
.tab { position:absolute; width:900px; height:600px; border-radius:40px; background:#05090D; padding:18px; box-shadow:0 50px 120px rgba(0,0,0,.65), 0 0 0 3px #2A3A47 inset; }
.tab .vitre { border-radius:24px; }
.pc { position:absolute; width:1080px; }
.pc .ecran { height:675px; background:#05090D; border-radius:26px 26px 6px 6px; padding:18px; box-shadow:0 50px 120px rgba(0,0,0,.65), 0 0 0 3px #2A3A47 inset; }
.pc .vitre { border-radius:10px; }
.pc .socle { height:26px; margin:0 -70px; background:linear-gradient(#3a4b58,#1a2731); border-radius:0 0 30px 30px; }
.bulle { position:absolute; display:flex; align-items:center; gap:22px; background:#FCF9E6; color:#0F1A23; font-size:42px; font-weight:800; padding:24px 36px; white-space:nowrap; border-radius:40px 40px 40px 8px; box-shadow:0 30px 70px rgba(0,0,0,.45); }
.micro { width:64px; height:64px; border-radius:999px; background:#FFA500; flex-shrink:0; position:relative; }
.micro::after { content:""; position:absolute; left:23px; top:14px; width:18px; height:28px; border-radius:10px; background:#0F1A23; box-shadow:0 14px 0 -6px #0F1A23; }
.badge { position:absolute; background:#007BFF; color:#fff; font-size:38px; font-weight:800; padding:20px 32px; border-radius:24px; box-shadow:0 26px 60px rgba(0,123,255,.45); white-space:nowrap; }
.heure { position:absolute; left:50%; top:220px; transform:translateX(-50%); font-size:64px; font-weight:800; color:#FFA500; letter-spacing:.1em; background:rgba(5,9,13,.7); padding:10px 34px; border-radius:22px; }
.gros { position:absolute; left:0; right:0; top:360px; text-align:center; font-size:170px; font-weight:800; line-height:1; letter-spacing:-.03em; }
.gros em, .slogan em { font-style:normal; color:#FFA500; }
.fleche { position:absolute; left:930px; top:460px; font-size:120px; font-weight:800; color:#FFA500; }
.t-g { left:420px; top:150px; } .b-d { left:880px; top:420px; }
.t-g2 { left:400px; top:150px; } .t-d2 { left:1140px; top:150px; } .bd-1 { left:1460px; top:820px; }
.pc-c { left:420px; top:150px; } .bd-2 { left:1260px; top:250px; } .bd-3 { left:1200px; top:720px; }
.t-g3 { left:260px; top:150px; } .t-d3 { left:690px; top:150px; } .b-h { left:1110px; top:330px; } .bd-4 { left:1120px; top:620px; }
.t-c { left:500px; top:150px; } .b-r { left:960px; top:350px; } .bd-5 { left:1040px; top:620px; }
.tab-c { left:510px; top:200px; } .bd-6 { left:1110px; top:850px; }
.orbite { position:absolute; left:960px; top:470px; width:0; height:0; transform-style:preserve-3d; }
.o { transform-origin:center; }
.mots { position:absolute; left:0; right:0; top:80px; display:flex; justify-content:center; gap:22px; }
.mot { font-size:44px; font-weight:800; padding:14px 30px; border-radius:999px; background:rgba(252,249,230,.1); border:2px solid rgba(252,249,230,.2); opacity:0; }
.mot.on { background:#FFA500; color:#1d1300; border-color:#FFA500; }
.vingt { position:absolute; left:0; right:0; bottom:140px; text-align:center; font-size:64px; font-weight:800; opacity:0; z-index:4; text-shadow:0 10px 40px rgba(0,0,0,.6); }
.vingt b { color:#FFA500; font-size:96px; }
#sc8 { background:radial-gradient(1000px 700px at 50% 45%, #1a6fd6, #0F1A23 75%); }
.logo-fin { position:absolute; left:50%; top:300px; height:150px; margin-left:-260px; width:520px; object-fit:contain; background:#fff; padding:22px 36px; border-radius:36px; }
.slogan { position:absolute; left:0; right:0; top:540px; text-align:center; font-size:120px; font-weight:800; letter-spacing:-.02em; }
.cta { position:absolute; left:0; right:0; top:730px; text-align:center; font-size:42px; font-weight:600; color:rgba(252,249,230,.8); }
.onde { position:absolute; right:80px; bottom:58px; display:flex; align-items:center; gap:8px; z-index:6; height:70px; }
.onde i { display:block; width:9px; height:20px; border-radius:6px; background:#FFA500; }
.sub { position:absolute; left:0; right:0; bottom:54px; text-align:center; font-size:46px; font-weight:800; color:#fff; z-index:5; opacity:0; }
.sub span { background:rgba(5,9,13,.85); padding:10px 28px; border-radius:18px; }
.logo-coin { position:absolute; right:70px; top:56px; height:56px; background:#fff; padding:9px 16px; border-radius:16px; z-index:6; }
"""

h = []
h.append('<!doctype html>\n<html lang="fr"><head><meta charset="UTF-8" /><meta name="viewport" content="width=1920, height=1080" />')
h.append('<script src="assets/gsap.min.js"></script>\n<style>' + css + '</style></head><body>')
h.append(f'<div id="root" data-composition-id="main" data-start="0" data-duration="{FIN}" data-width="1920" data-height="1080">')
h.append(f'<audio id="voix" src="assets/voix.mp3" data-start="{D}" data-duration="29.65" data-track-index="10" data-volume="1"></audio>')
for sid, a, b, fond, contenu in SCENES:
    f = f'<div class="fond" style="background-image:url(assets/{fond})"></div><div class="voile"></div>' if fond else ''
    h.append(f'<div class="scene" id="{sid}">{f}<div class="cam">{contenu}</div></div>')
h.append('<img class="logo-coin" id="logoc" src="assets/logo.png" alt="">')
h.append('<div class="onde" id="onde">' + "".join('<i></i>' for _ in range(14)) + '</div>')
for i, (t, a, b) in enumerate(SOUS):
    h.append(f'<div class="sub" id="s{i}"><span>{html.escape(t)}</span></div>')
h.append('</div>\n<script>\nwindow.__timelines = window.__timelines || {};\nconst tl = gsap.timeline({ paused:true });')

J = []
for k, (sid, a, b, fond, _) in enumerate(SCENES):
    a2 = max(0, a + D) if k else 0
    b2 = b + D
    J.append(f'tl.fromTo("#{sid}",{{opacity:0}},{{opacity:1,duration:.45,ease:"power2.out"}},{a2:.2f});')
    if k < len(SCENES) - 1:
        J.append(f'tl.to("#{sid}",{{opacity:0,duration:.45}},{b2-0.2:.2f});')
    # caméra : léger travelling avant + rotation
    J.append(f'tl.fromTo("#{sid} .cam",{{scale:1.06,rotationY:-7,rotationX:3}},{{scale:1,rotationY:5,rotationX:-1,duration:{b2-a2+0.5:.2f},ease:"sine.inOut"}},{a2:.2f});')
    J.append(f'tl.fromTo("#{sid} .fond",{{scale:1.12,x:-30}},{{scale:1,x:30,duration:{b2-a2+0.5:.2f},ease:"none"}},{a2:.2f});')
    if sid != "sc7": J.append(f'tl.from("#{sid} .tel, #{sid} .tab, #{sid} .pc",{{y:220,rotationY:-28,opacity:0,duration:.9,stagger:.18,ease:"back.out(1.3)"}},{a2+0.1:.2f});')
    J.append(f'tl.from("#{sid} .bulle",{{scale:.4,opacity:0,transformOrigin:"0% 100%",duration:.55,ease:"back.out(2.2)"}},{a2+0.45:.2f});')
    J.append(f'tl.from("#{sid} .badge",{{x:120,opacity:0,duration:.5,stagger:.6,ease:"back.out(2)"}},{a2+1.1:.2f});')
    J.append(f'tl.from("#{sid} .fleche",{{x:-80,opacity:0,duration:.5,ease:"power3.out"}},{a2+0.9:.2f});')

# scène 0
J.append('tl.from("#sc0 .heure",{y:-60,opacity:0,duration:.5,ease:"back.out(2)"},0.1);')
J.append('tl.from("#sc0 .gros",{y:80,opacity:0,scale:.9,duration:.8,ease:"back.out(1.6)"},0.35);')
# orbite des appareils
a7 = 20.1 + D
pos = [(-760, -40, -200, 26), (-430, 160, 80, 12), (0, -60, 220, 0), (430, 120, 60, -12), (700, -60, -220, -26), (220, -330, -380, -6)]
for i, (x, y, z, ry) in zip([1,2,3,4,5,7], pos):
    J.append(f'tl.set("#sc7 .o{i}",{{x:{x},y:{y},z:{z},rotationY:{ry},xPercent:-50,yPercent:-50,scale:.55}},0);')
J.append(f'tl.fromTo("#sc7 .o",{{opacity:0,scale:.2}},{{opacity:1,scale:.5,duration:.8,stagger:.12,ease:"back.out(1.5)"}},{a7+0.1:.2f});')
J.append(f'tl.fromTo("#orbite",{{rotationY:-18,z:-300}},{{rotationY:16,z:0,duration:7.6,ease:"sine.inOut"}},{a7:.2f});')
for i, t in enumerate([20.2, 21.0, 21.7, 22.4, 23.1]):
    J.append(f'tl.to("#m{i}",{{opacity:1,duration:.3}},{t+D:.2f}); tl.set("#m{i}",{{className:"mot on"}},{t+D+0.1:.2f});')
J.append(f'tl.fromTo("#vingt",{{opacity:0,y:40,scale:.8}},{{opacity:1,y:0,scale:1,duration:.7,ease:"back.out(2)"}},{24.9+D:.2f});')
# fin
a8 = 27.4 + D
J.append(f'tl.from(".logo-fin",{{scale:.4,opacity:0,duration:.8,ease:"back.out(1.8)"}},{a8+0.1:.2f});')
J.append(f'tl.from(".slogan",{{y:60,opacity:0,duration:.7,ease:"back.out(1.6)"}},{a8+0.7:.2f});')
J.append(f'tl.from(".cta",{{opacity:0,duration:.6}},{a8+1.6:.2f});')
J.append(f'tl.to("#logoc, #onde",{{opacity:0,duration:.4}},{a8:.2f});')
# onde : fil conducteur de la voix
for i in range(14):
    d = 0.22 + (i * 37 % 11) / 40
    J.append(f'tl.fromTo("#onde i:nth-child({i+1})",{{height:14}},{{height:{30 + (i*53 % 40)},duration:{d:.2f},repeat:{int(29/d)},yoyo:true,ease:"sine.inOut"}},{D + (i%5)*0.04:.2f});')
# sous-titres
for i, (t, a, b) in enumerate(SOUS):
    J.append(f'tl.set("#s{i}",{{opacity:1}},{a+D:.2f}); tl.set("#s{i}",{{opacity:0}},{b+D-0.02:.2f});')
J.append(f'tl.set({{}},{{}},{FIN});\nwindow.__timelines["main"] = tl;')
h.append("\n".join(J))
h.append('</script>\n</body></html>')
open('/home/user/film-accueil/projet/index.html', 'w').write("\n".join(h))
print("ok")
