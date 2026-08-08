#!/usr/bin/env python3
"""Génère les 8 scènes de C1 · Cuisine avant le service.

Pourquoi un générateur plutôt que 8 fichiers écrits à la main : les huit
scènes partagent le même bloc de style, et HyperFrames jette le <head> des
sous-compositions — le CSS doit donc être répété intégralement dans chacune.
Le recopier huit fois à la main, puis seize fois de plus pour les deux films
suivants, c'est huit occasions de laisser diverger la charte. Ici la
grammaire de la série vit à un seul endroit ; les 8 autres films de
« Une journée avec FoodEatUp » réutiliseront ce fichier en changeant SCENES
et METIER.

Sortie : studio-video/compositions/c1/*.html (versionnés — HyperFrames lit
les HTML, pas ce script).
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "studio-video" / "compositions" / "c1"

# Charte du site Academy (src/styles.css), convertie depuis oklch.
# Voir NOTES.md §5 bis.1 : les films et le site partagent une seule palette.
CREAM = "#FCF9E6"
CREAM_DEEP = "#F5F0D4"
INK = "#0F1A23"
INK_SOFT = "#4C5760"
BLUE = "#007BFF"
ORANGE = "#FFA500"
BORDER = "#E1DDC7"

METIER = "#059669"  # liseré cuisine

# Le cadre occupe 1560 px sur 1920 (81 %). Les bobines sont encodées en
# 1560x546, donc aucune mise à l'échelle au rendu.
FRAME_W, FRAME_H = 1560, 546
FRAME_X = (1920 - FRAME_W) // 2
FRAME_Y = 226

STYLE = f"""
        @font-face {{
          font-family: "Fredoka";
          src: url("assets/vendor/fonts/Fredoka-Variable.woff2") format("woff2-variations");
          font-weight: 300 700; font-display: block;
        }}
        #root {{ position:absolute; inset:0; background:{CREAM}; overflow:hidden;
                 font-family:"Inter",sans-serif; }}

        /* Fond à la charte du site : le cream, plus les deux dégradés du
           hero-glow (bleu en haut à gauche, orange en haut à droite). Ils
           sont animés — un aplat immobile pendant 75 s se lit comme une
           image figée, et Michael a demandé que les fonds vivent. */
        .glow {{ position:absolute; border-radius:50%; filter:blur(10px); }}
        .glow-a {{ left:-360px; top:-420px; width:1500px; height:820px;
                   background:radial-gradient(closest-side, rgba(0,123,255,.16), rgba(0,123,255,0) 70%); }}
        .glow-b {{ right:-420px; top:-360px; width:1400px; height:760px;
                   background:radial-gradient(closest-side, rgba(255,165,0,.22), rgba(255,165,0,0) 70%); }}
        .glow-c {{ left:34%; bottom:-560px; width:1300px; height:900px;
                   background:radial-gradient(closest-side, rgba(5,150,105,.10), rgba(5,150,105,0) 70%); }}

        /* Trame de points, reprise du motif de conversation du site. Elle
           donne au fond une texture qui bouge sans jamais attirer l'œil. */
        .grid {{ position:absolute; left:-160px; top:-160px; width:2280px; height:1420px;
                 background-image:radial-gradient(circle at 1px 1px, {BORDER} 0 2px, transparent 2px);
                 background-size:48px 48px; opacity:.55; }}

        /* Liseré métier cuisine, en haut de cadre — signature de la série. */
        .metier {{ position:absolute; top:0; left:0; right:0; height:5px; background:{METIER}; }}

        .clock {{ position:absolute; top:44px; left:64px; font-family:"Fredoka",sans-serif;
                  font-weight:700; font-size:46px; color:{INK}; opacity:0; letter-spacing:.02em; }}
        .eyebrow {{ position:absolute; top:52px; left:340px; right:340px; text-align:center;
                    font-family:"Fredoka",sans-serif; font-weight:600; font-size:40px;
                    color:{INK_SOFT}; opacity:0; }}

        /* Cadre tablette incliné 6°, posé sur le plan — grammaire commune.
           Positionné en absolu, pas en translate(-50%,-50%) : GSAP réécrit
           tout le transform quand il anime scale, ce qui perdrait le centrage. */
        .frame {{ position:absolute; left:{FRAME_X}px; top:{FRAME_Y}px;
                  width:{FRAME_W}px; height:{FRAME_H}px; border-radius:24px; overflow:hidden;
                  background:{INK}; box-shadow:0 48px 110px rgba(15,26,35,.30);
                  opacity:0; transform-origin:center center; }}
        .frame video {{ position:relative; display:block; width:100%; height:100%;
                        object-fit:cover; }}
        /* Veille du cadre : ce qu'on voit sous l'écran pendant les 320 ms
           d'apparition. Un aplat marine y était lu comme un plan noir. */
        .veille {{ position:absolute; inset:0;
                   background:linear-gradient(118deg, {INK} 0%, #16283a 46%, {INK} 100%); }}
        /* Pas de skewX en CSS : GSAP anime x et réécrit tout le transform,
           l'inclinaison serait perdue. Elle est portée par le tween. */
        .veille-scan {{ position:absolute; top:-20%; left:-40%; width:38%; height:140%;
                        background:linear-gradient(90deg, rgba(0,123,255,0), rgba(0,123,255,.20), rgba(0,123,255,0)); }}

        .checks {{ position:absolute; left:0; right:0; top:{FRAME_Y + FRAME_H + 58}px;
                   display:flex; flex-direction:row; justify-content:center;
                   align-items:center; gap:26px; }}
        .check {{ display:flex; align-items:center; gap:12px; background:{ORANGE}; color:{INK};
                  font-family:"Fredoka",sans-serif; font-weight:700; font-size:30px;
                  padding:14px 28px; border-radius:999px; opacity:0; transform:scale(.8);
                  white-space:nowrap; box-shadow:0 10px 26px rgba(255,165,0,.28); }}

        .amb {{ position:absolute; inset:0; width:100%; height:100%; object-fit:cover; opacity:0; }}
        .title {{ position:absolute; left:0; right:0; bottom:132px; text-align:center;
                  font-family:"Fredoka",sans-serif; font-weight:700; font-size:76px; color:{CREAM};
                  text-shadow:0 6px 30px rgba(15,26,35,.6); opacity:0; }}
        .sub {{ position:absolute; left:0; right:0; bottom:74px; text-align:center;
                font-family:"Fredoka",sans-serif; font-weight:600; font-size:34px; color:{CREAM};
                text-shadow:0 2px 16px rgba(15,26,35,.65); opacity:0; }}
"""

def _repeat(cycle, dur):
    """Nombre de répétitions couvrant tout juste la scène.

    On évite `repeat: -1` : HyperFrames avertit qu'une boucle infinie est
    tronquée à la fenêtre déclarée. Le comportement obtenu serait le même,
    mais un compte fini rend le rendu explicitement déterministe et laisse
    le lint propre — donc lisible quand un vrai problème apparaîtra.
    """
    import math
    return max(0, math.ceil(float(dur) / cycle) - 1 + 1)


def bg_js(dur):
    """Fond vivant : les dégradés dérivent et respirent, la trame glisse.

    Ces mouvements sont dans la timeline (et non en @keyframes CSS) pour que
    le rendu reste déterministe image par image quand HyperFrames se déplace
    dans le temps.
    """
    return (
        "\n        // Fond vivant : les dégradés dérivent et respirent, la trame glisse.\n"
        f'        tl.to("#glowA", {{ x:70, y:38, scale:1.10, duration:11, ease:"sine.inOut", yoyo:true, repeat:{_repeat(11, dur)} }}, 0);\n'
        f'        tl.to("#glowB", {{ x:-56, y:44, scale:1.14, duration:9, ease:"sine.inOut", yoyo:true, repeat:{_repeat(9, dur)} }}, 0);\n'
        f'        tl.to("#glowC", {{ x:48, scale:1.08, duration:13, ease:"sine.inOut", yoyo:true, repeat:{_repeat(13, dur)} }}, 0);\n'
        f'        tl.to("#grid", {{ x:-48, y:-48, duration:16, ease:"none", repeat:{_repeat(16, dur)} }}, 0);\n'
    )

BG_HTML = """        <div class="glow glow-a" id="glowA"></div>
        <div class="glow glow-b" id="glowB"></div>
        <div class="glow glow-c" id="glowC"></div>
        <div class="grid" id="grid"></div>
"""

# La veille balaie en continu : le cadre n'est jamais un rectangle mort,
# même avant que la bobine n'apparaisse.
VEILLE_HTML = """            <div class="veille"></div>
            <div class="veille-scan" id="scan"></div>
"""
def veille_js(dur):
    return (
        '        tl.fromTo("#scan", { x:0, skewX:-12 },'
        f' {{ x:4300, skewX:-12, duration:3.4, ease:"none", repeat:{_repeat(3.4, dur)} }}, 0);\n'
    )

TEMPLATE = """<!doctype html>
<html>
  <head><meta charset="UTF-8" /></head>
  <body>
    <template>
      <style>{style}
      </style>

      <div id="root" data-composition-id="{cid}" data-width="1920" data-height="1080" data-duration="{dur}">
        <div class="metier"></div>
{body}      </div>

      <script>
        window.__timelines = window.__timelines || {{}};
        const tl = gsap.timeline({{ paused: true }});
{js}
        window.__timelines["{cid}"] = tl;
      </script>
    </template>
  </body>
</html>
"""


def scene_ecran(cid, dur, clock, eyebrow, reel, reel_dur, vid_id, checks):
    """Scène « écran » : horloge, surtitre, bobine dans le cadre, coches."""
    chips = "".join(
        f'          <div class="check" id="ck{i}"><span>✓</span>{t}</div>\n'
        for i, t in enumerate(checks)
    )
    body = (
        BG_HTML
        + f'        <div class="clock" id="clock">{clock}</div>\n'
        + f'        <div class="eyebrow" id="eyebrow">{eyebrow}</div>\n'
        + '        <div class="frame" id="frame">\n'
        + VEILLE_HTML
        # La fenêtre déclarée est celle de la SCÈNE, pas celle du fichier.
        # Le fichier est volontairement plus long (marge de sécurité), mais
        # un clip qui déclare survivre à sa propre composition est un
        # contrat mal défini — et c'est ce qui éteignait la scène 2.
        + f'          <video id="{vid_id}" src="assets/screens/c1/{reel}.mp4" muted playsinline'
        f' class="clip" data-start="0" data-duration="{float(dur):.2f}" data-track-index="2"></video>\n'
        + "        </div>\n"
        + f'        <div class="checks">\n{chips}        </div>\n'
    )
    js = (
        bg_js(dur)
        + veille_js(dur)
        + '        tl.fromTo("#clock", { opacity:0, y:-12 }, { opacity:1, y:0, duration:.4, ease:"power2.out" }, .05);\n'
        + '        tl.fromTo("#eyebrow", { opacity:0, y:-12 }, { opacity:.9, y:0, duration:.4, ease:"power2.out" }, .12);\n'
        + "        // Le cadre apparaît en 320 ms ; l'action à l'écran démarre 250 ms après.\n"
        + '        tl.fromTo("#frame", { opacity:0, scale:.94, rotateY:6 }, { opacity:1, scale:1, rotateY:6, duration:.32, ease:"back.out(1.6)" }, 0.35);\n'
    )
    for i in range(len(checks)):
        js += (
            f'        tl.fromTo("#ck{i}", {{ opacity:0, scale:.8, y:14 }},'
            f' {{ opacity:1, scale:1, y:0, duration:.24, ease:"back.out(2)" }}, {1.75 + i * .28:.2f});\n'
        )
    return TEMPLATE.format(style=STYLE, cid=cid, dur=dur, body=body, js=js)


def scene_carton(cid, dur, plate, plate_dur, vid_id, title, sub, amb_opacity, title_at, sub_at):
    """Scène « carton » : plan d'ambiance plein cadre, titre, sous-titre.

    Ces deux cartons étaient des images fixes. Ce sont maintenant des plans
    tournés (bibliothèque Higgsfield), avec les mêmes personnages que le
    reste de la série — la cuisine déserte au petit matin pour l'ouverture,
    le portrait du chef pour la clôture.
    """
    body = (
        BG_HTML
        + f'        <video class="amb clip" id="{vid_id}" src="assets/plates/c1/{plate}.mp4"'
        f' muted playsinline data-start="0" data-duration="{float(dur):.2f}"'
        ' data-track-index="2"></video>\n'
        + f'        <div class="title" id="title">{title}</div>\n'
        + f'        <div class="sub" id="sub">{sub}</div>\n'
    )
    # Le lent zoom avant ne démarre qu'après l'entrée de l'image : les deux
    # tweens porteraient sinon `scale` en même temps, et le second gagnerait.
    js = (
        bg_js(dur)
        + f'        tl.fromTo("#{vid_id}", {{ opacity:0, scale:1.06 }}, {{ opacity:{amb_opacity}, scale:1, duration:1.2, ease:"power2.out" }}, 0);\n'
        + f'        tl.to("#{vid_id}", {{ scale:1.045, duration:{max(0.5, float(dur) - 1.2):.2f}, ease:"none" }}, 1.2);\n'
        + f'        tl.fromTo("#title", {{ opacity:0, y:24 }}, {{ opacity:1, y:0, duration:.6, ease:"power2.out" }}, {title_at});\n'
        + f'        tl.fromTo("#sub", {{ opacity:0, y:14 }}, {{ opacity:.92, y:0, duration:.5, ease:"power2.out" }}, {sub_at});\n'
    )
    return TEMPLATE.format(style=STYLE, cid=cid, dur=dur, body=body, js=js)


SCENES = {
    "c1-s1-ouverture.html": scene_carton(
        "c1-s1-ouverture", "4.61", "cuisine-vide", 8.03, "vid-plate-cuisine",
        "Sept heures", "Dans quatre heures, tout doit être prêt", 1, ".9", "1.5",
    ),
    "c1-s2-ouverture-poste.html": scene_ecran(
        "c1-s2-ouverture-poste", "12.77", "07:00", "J'OUVRE MON POSTE",
        "SCENE-2", 12.90, "vid-scene-2",
        ["Entrée pointée", "Tâches du jour", "Températures relevées"],
    ),
    "c1-s3-reception.html": scene_ecran(
        "c1-s3-reception", "16.13", "07:15", "LA LIVRAISON ARRIVE",
        "SCENE-3", 16.33, "vid-scene-3",
        ["Réception validée", "EAN et DLC scannés", "Facture au scan", "Prix à jour"],
    ),
    "c1-s4-jarvis.html": scene_ecran(
        "c1-s4-jarvis", "9.78", "07:25", "JE PARLE, LE STOCK SUIT",
        "SCENE-4", 10.00, "vid-scene-4",
        ["Sortie dictée", "Stock décrémenté"],
    ),
    "c1-s5-production.html": scene_ecran(
        "c1-s5-production", "8.47", "07:30", "MA PRODUCTION DU JOUR",
        "SCENE-5", 8.63, "vid-scene-5",
        ["Fiches techniques", "Liste imprimée"],
    ),
    "c1-s6-etiquetage.html": scene_ecran(
        "c1-s6-etiquetage", "10.15", "08:30", "CHAQUE PRÉPARATION, SON ÉTIQUETTE",
        "SCENE-6", 10.36, "vid-scene-6",
        ["Étiquettes générées", "DLC et allergènes", "Historique gardé"],
    ),
    "c1-s7-validation.html": scene_ecran(
        "c1-s7-validation", "8.97", "11:00", "JE VALIDE ET JE SONDE",
        "SCENE-7", 9.16, "vid-scene-7",
        ["Production validée", "Plats sondés", "Matinée tracée"],
    ),
    "c1-s8-cta.html": scene_carton(
        "c1-s8-cta", "4.5", "chef-portrait", 6.03, "vid-plate-chef",
        "Ma matinée est tracée", "Je n'ai pas ouvert un seul classeur", ".62", ".35", ".85",
    ),
}

if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for name, html in SCENES.items():
        (OUT / name).write_text(html, encoding="utf-8")
        print("écrit", name)
