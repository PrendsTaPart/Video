#!/usr/bin/env python3
"""
Génère index.html — vidéo « Chaînes », variante boulangerie, séquences 1 à 4.

Contrat HyperFrames « Send to HyperFrames » (single-file import) :
  - une racine live data-composition-id="main" + data-width/height/start/duration
  - chaque scène : data-start + data-duration, scènes jointives sans trou
  - timeline GSAP paused, construite synchroniquement, sur window.__timelines["main"]
  - 100 % déterministe : aucun Date.now(), aucun Math.random(), aucun rAF/setTimeout
  - polices ET images inlinées en base64 data: URI (aucun chemin relatif ne survit)
  - runtime/GSAP/shaders depuis le CDN jsdelivr (ne PAS inliner)

Régénérer :  python3 build.py
"""

import base64
import pathlib

HERE = pathlib.Path(__file__).parent
IMG = HERE / "assets" / "img"
FONTS = HERE.parent / "_fonts"
OUT = HERE / "index.html"

# ---------------------------------------------------------------- charte C0
CREME = "#FCF9E6"
MARINE = "#0F1A23"
ACCENT = "#007BFF"
BLEU_SYS = "#147AFF"
ORANGE = "#FFA500"  # alertes uniquement

# ------------------------------------------------- données séquence 2 (barres)
# Longueurs RELATIVES, sans axe ni pourcentage affiché : SOURCES.md ne contient
# aucun chiffre [SOURCÉ], donc l'écart est MONTRÉ, jamais quantifié.
# Suite figée en dur — le déterminisme du rendu interdit Math.random().
BAR_LABELS = [f"Magasin {i:02d}" for i in range(1, 13)]
BAR_EQUAL = 55.0
BAR_TARGET = [38, 46, 41, 63, 44, 52, 79, 47, 43, 58, 49, 45]
I_MIN = BAR_TARGET.index(min(BAR_TARGET))   # Magasin 01
I_MAX = BAR_TARGET.index(max(BAR_TARGET))   # Magasin 07

# Repère de délai générique (cycle comptable), pas une mesure du prospect.
# Se retire d'un mot si vous le jugez trop affirmatif — voir SOURCES.md.
FRISE_LABELS = ("Jour 1", "Jour 45")

# Lignes du tableau de bord siège — séquence 1.
ROW_FILLED = "CA consolidé"
ROWS_EMPTY = [
    "Invendus par magasin",
    "Coût matière par magasin",
    "Écart production / vente",
    "Marge par référence",
    "Taux de rupture avant 11 h",
]

# ------------------------------------------------------- scènes (jointives)
# Une scène = une séquence du brief. Volontairement longues (10-15 s) : chaque
# séquence est UNE animation continue à révélation progressive (le tableau se
# remplit, les barres se déforment). Les découper redémarrerait l'animation.
S1, D1 = 0.0, 15.0    # séq 1 — tableau de bord siège
S2, D2 = 15.0, 13.0   # séq 2a — les 12 barres          [ANCRE SHADER 1]
S3, D3 = 28.0, 5.0    # séq 2b — « L'écart » en gros    [ANCRE SHADER 2]
S4, D4 = 33.0, 12.0   # séq 3 — les douze carnets
S5, D5 = 45.0, 10.0   # séq 4 — la frise du délai
TOTAL = 55.0
XF = 0.5              # durée du shader
XF_TIME = S3 - XF / 2 # 27.75


def b64(path: pathlib.Path) -> str:
    return base64.b64encode(path.read_bytes()).decode()


def font_face(family: str, path: pathlib.Path, wmin: int, wmax: int) -> str:
    return f"""    @font-face {{
      font-family: "{family}";
      font-weight: {wmin} {wmax};
      font-style: normal;
      font-display: block;
      src: url(data:font/woff2;base64,{b64(path)}) format("woff2");
    }}"""


def build() -> str:
    ff_fredoka = font_face("Fredoka", FONTS / "Fredoka-Variable.woff2", 300, 700)
    ff_baloo = font_face("Baloo 2", FONTS / "Baloo2-Variable.woff2", 400, 800)
    carnet_uri = f"data:image/png;base64,{b64(IMG / 'carnet.png')}"
    fournee_uri = f"data:image/png;base64,{b64(IMG / 'fournee.png')}"
    logo_uri = f"data:image/png;base64,{b64(IMG / 'logo-horizontal.png')}"

    # --- séquence 1 : les lignes du tableau ---
    rows = [
        f'<div class="row row-filled" id="row-ca">'
        f'<span class="row-label">{ROW_FILLED}</span>'
        f'<span class="row-value" id="row-ca-val"></span></div>'
    ]
    for i, label in enumerate(ROWS_EMPTY):
        rows.append(
            f'<div class="row row-empty" id="row-e{i}">'
            f'<span class="row-label">{label}</span>'
            f'<span class="row-dash">&mdash;</span></div>'
        )
    rows_html = "\n          ".join(rows)

    # --- séquence 2 : les 12 barres ---
    bars = []
    for i, label in enumerate(BAR_LABELS):
        cls = "bar-fill"
        if i == I_MIN:
            cls += " is-min"
        elif i == I_MAX:
            cls += " is-max"
        bars.append(
            f'<div class="bar-row" id="barrow-{i}">'
            f'<span class="bar-label">{label}</span>'
            f'<span class="bar-track"><span class="{cls}" id="bar-{i}"></span></span>'
            f"</div>"
        )
    bars_html = "\n          ".join(bars)

    # --- séquence 3 : les 12 carnets ---
    carnets = "\n          ".join(
        f'<div class="carnet" id="carnet-{i}"></div>' for i in range(12)
    )

    # --- séquence 4 : l'empilement des fournées ---
    # Chaque fournée se pose PLUS HAUT que la précédente et légèrement décalée :
    # sans ces offsets les 5 plateaux se superposent au pixel près et l'empilement
    # ne se voit pas du tout (constaté au contrôle visuel : un seul plateau à l'écran).
    stacks = "\n          ".join(
        f'<div class="fournee" id="fournee-{i}" '
        f'style="bottom:{i * 38}px; margin-left:{-130 + (10 if i % 2 else -10)}px;"></div>'
        for i in range(5)
    )

    # ---------------------------------------------------------------- JS
    js_bars = "\n      ".join(
        f'tl.to("#bar-{i}", {{ width: "{BAR_TARGET[i]}%", duration: 0.75, '
        f'ease: "power2.inOut" }}, {S2 + 3.4 + i * 0.32:.2f});'
        for i in range(12)
    )
    js_rows = "\n      ".join(
        f'tl.from("#row-e{i}", {{ autoAlpha: 0, x: -24, duration: 0.5, '
        f'ease: "power2.out" }}, {S1 + 5.2 + i * 0.55:.2f});'
        for i in range(len(ROWS_EMPTY))
    )
    js_carnets = "\n      ".join(
        f'tl.from("#carnet-{i}", {{ autoAlpha: 0, y: 34, scale: 0.86, duration: 0.55, '
        f'ease: "back.out(1.4)" }}, {S4 + 0.3 + i * 0.16:.2f});'
        for i in range(12)
    )
    js_stack = "\n      ".join(
        f'tl.from("#fournee-{i}", {{ autoAlpha: 0, y: -30, duration: 0.45, '
        f'ease: "power2.out" }}, {S5 + 2.2 + i * 0.42:.2f});'
        for i in range(5)
    )

    return f"""<!doctype html>
<html lang="fr" style="overflow:hidden; margin:0">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1920, height=1080" />
    <title>FoodEatUp — Chaînes — Boulangerie — séquences 1 à 4</title>
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@hyperframes/core/dist/hyperframe.runtime.iife.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@hyperframes/shader-transitions/dist/index.global.js"></script>
    <style>
{ff_fredoka}
{ff_baloo}

      :root {{
        --creme: {CREME};
        --marine: {MARINE};
        --accent: {ACCENT};
        --bleu-sys: {BLEU_SYS};
        --orange: {ORANGE};
        --muted: rgba(15, 26, 35, 0.34);
        --hair: rgba(15, 26, 35, 0.12);
        --font-display: "Fredoka", sans-serif;
        --font-body: "Baloo 2", sans-serif;
      }}

      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      html, body {{
        width: 1920px; height: 1080px; overflow: hidden;
        background: var(--creme); color: var(--marine);
      }}

      .scene {{
        position: absolute; top: 0; left: 0;
        width: 1920px; height: 1080px; overflow: hidden;
        background: var(--creme);
      }}
      /* Empilement explicite. SANS ça, la scène sortante reste visible SOUS la
         suivante : GSAP promeut les éléments animés en calques de composition, et
         un calque promu se rasterise au-dessus du fond d'une scène frère
         postérieure — alors même que l'ordre DOM, les styles calculés et
         elementFromPoint disent tous l'inverse. Constaté sur les séquences 3 et 4,
         qui laissaient « L'écart » (s3) transparaître par-dessous. */
      #s1 {{ z-index: 1; }}
      #s2 {{ z-index: 2; }}
      #s3 {{ z-index: 3; }}
      #s4 {{ z-index: 4; }}
      #s5 {{ z-index: 5; }}
      .scene-content {{
        width: 100%; height: 100%; position: relative; z-index: 1;
        display: flex; flex-direction: column;
        justify-content: center; align-items: center;
      }}

      .kicker {{
        font-family: var(--font-body); font-weight: 600; font-size: 26px;
        letter-spacing: 0.22em; text-transform: uppercase; color: var(--muted);
      }}
      .display {{ font-family: var(--font-display); font-weight: 600; line-height: 1.04; }}
      .body {{ font-family: var(--font-body); font-weight: 400; }}

      /* ---------------- séquence 1 : tableau de bord siège ---------------- */
      .board {{
        width: 1180px; background: #fff; border-radius: 22px;
        border: 1px solid var(--hair);
        box-shadow: 0 30px 70px rgba(15, 26, 35, 0.09);
        padding: 46px 54px 52px;
      }}
      .board-head {{
        display: flex; align-items: baseline; gap: 18px;
        padding-bottom: 26px; border-bottom: 1px solid var(--hair); margin-bottom: 12px;
      }}
      .board-title {{ font-family: var(--font-display); font-weight: 600; font-size: 40px; }}
      .board-scope {{
        font-family: var(--font-body); font-weight: 600; font-size: 22px;
        color: var(--muted); letter-spacing: 0.1em; text-transform: uppercase;
      }}
      .row {{
        display: flex; align-items: center; justify-content: space-between;
        padding: 25px 4px; border-bottom: 1px solid var(--hair);
      }}
      .row:last-child {{ border-bottom: none; }}
      .row-label {{ font-family: var(--font-body); font-weight: 600; font-size: 31px; }}
      .row-empty .row-label {{ color: var(--muted); font-weight: 400; }}
      .row-dash {{ font-family: var(--font-body); font-size: 34px; color: var(--muted); }}
      /* Valeur volontairement non chiffrée : aucun chiffre n'est [SOURCÉ]. */
      .row-value {{
        display: block; width: 210px; height: 34px; border-radius: 8px;
        background: var(--marine); transform-origin: right center;
      }}
      .cursor {{ position: absolute; left: 0; top: 0; width: 30px; height: 30px; }}

      /* ---------------- séquence 2 : les douze barres ---------------- */
      .bars {{ width: 1200px; display: flex; flex-direction: column; gap: 15px; }}
      .bar-row {{ display: flex; align-items: center; gap: 26px; }}
      .bar-label {{
        width: 210px; flex: none; text-align: right;
        font-family: var(--font-body); font-weight: 600; font-size: 25px; color: var(--muted);
        font-variant-numeric: tabular-nums;
      }}
      .bar-track {{
        flex: 1; height: 30px; background: rgba(15, 26, 35, 0.07);
        border-radius: 15px; overflow: hidden; display: block;
      }}
      .bar-fill {{
        display: block; height: 100%; width: {BAR_EQUAL}%;
        background: var(--bleu-sys); border-radius: 15px;
      }}

      /* ---------------- séquence 3 : les douze carnets ---------------- */
      .carnets {{
        display: grid; grid-template-columns: repeat(6, 250px);
        gap: 34px 30px; justify-content: center;
      }}
      .carnet {{
        width: 250px; height: 220px;
        background-image: url({carnet_uri});
        background-size: contain; background-repeat: no-repeat; background-position: center;
      }}

      /* ---------------- séquence 4 : la frise du délai ---------------- */
      .frise {{ width: 1380px; position: relative; height: 4px; background: var(--hair); }}
      .frise-prog {{
        position: absolute; left: 0; top: 0; height: 4px; width: 0;
        background: var(--marine); transform-origin: left center;
      }}
      .frise-cap {{
        position: absolute; top: -13px; width: 4px; height: 30px; background: var(--marine);
      }}
      .frise-label {{
        position: absolute; top: 30px;
        font-family: var(--font-body); font-weight: 600; font-size: 25px; color: var(--muted);
      }}
      .stack {{ position: relative; width: 560px; height: 390px; margin-bottom: 78px; }}
      .fournee {{
        position: absolute; left: 50%; width: 260px; height: 206px;
        background-image: url({fournee_uri});
        background-size: contain; background-repeat: no-repeat; background-position: bottom center;
      }}
      .logo {{
        position: absolute; right: 74px; bottom: 62px;
        width: 200px; height: 53px;
        background-image: url({logo_uri});
        background-size: contain; background-repeat: no-repeat; background-position: right bottom;
      }}
    </style>
  </head>
  <body>
    <div id="main" data-composition-id="main"
         data-width="1920" data-height="1080"
         data-start="0" data-duration="{TOTAL}">

      <!-- ============ SÉQUENCE 1 ({S1}-{S1 + D1}s) — le chiffre qui manque ============ -->
      <div class="scene clip" id="s1" data-start="{S1}" data-duration="{D1}" data-track-index="0">
        <div class="scene-content">
          <div class="board" id="board">
            <div class="board-head">
              <span class="board-title">Tableau de bord</span>
              <span class="board-scope">Siège &middot; 12 magasins</span>
            </div>
          {rows_html}
          </div>
        </div>
        <svg class="cursor" id="cursor" viewBox="0 0 24 24" fill="none">
          <path d="M4 2 L4 20 L9 15.5 L12.5 22 L15.5 20.5 L12 14.5 L19 14 Z"
                fill="{MARINE}" stroke="#fff" stroke-width="1.2" stroke-linejoin="round"/>
        </svg>
      </div>

      <!-- ============ SÉQUENCE 2a ({S2}-{S2 + D2}s) — l'écart révélé [ANCRE 1] ============ -->
      <div class="scene clip" id="s2" data-start="{S2}" data-duration="{D2}" data-track-index="0"
           style="opacity:0;">
        <div class="scene-content">
          <div class="kicker" id="s2-kicker" style="margin-bottom:38px;">
            Taux d'invendus &middot; m&ecirc;me production, m&ecirc;mes horaires
          </div>
          <div class="bars">
          {bars_html}
          </div>
        </div>
      </div>

      <!-- ============ SÉQUENCE 2b ({S3}-{S3 + D3}s) — « L'écart » [ANCRE 2] ============ -->
      <div class="scene clip" id="s3" data-start="{S3}" data-duration="{D3}" data-track-index="0"
           style="opacity:0;">
        <div class="scene-content">
          <div class="kicker" id="s3-kicker">Magasin 01 &nbsp;&mdash;&nbsp; Magasin 07</div>
          <div class="display" id="s3-word" style="font-size:250px; margin:12px 0 22px;">
            L'&eacute;cart
          </div>
          <div class="body" id="s3-sub" style="font-size:44px; color:rgba(15,26,35,0.62);">
            Personne dans l'entreprise ne saurait le donner.
          </div>
        </div>
      </div>

      <!-- ============ SÉQUENCE 3 ({S4}-{S4 + D4}s) — pourquoi personne ne le voit ============ -->
      <div class="scene clip" id="s4" data-start="{S4}" data-duration="{D4}" data-track-index="0"
           style="visibility:hidden;">
        <div class="scene-content">
          <div class="carnets" id="carnets">
          {carnets}
          </div>
          <div class="display" id="s4-line" style="font-size:76px; margin-top:56px;">
            Douze habitudes. Aucune comparable.
          </div>
        </div>
      </div>

      <!-- ============ SÉQUENCE 4 ({S5}-{S5 + D5}s) — le coût du délai ============ -->
      <div class="scene clip" id="s5" data-start="{S5}" data-duration="{D5}" data-track-index="0"
           style="visibility:hidden;">
        <div class="scene-content">
          <div class="stack" id="stack">
          {stacks}
          </div>
          <div class="frise" id="frise">
            <div class="frise-prog" id="frise-prog"></div>
            <div class="frise-cap" style="left:0;"></div>
            <div class="frise-cap" style="right:0;"></div>
            <div class="frise-label" style="left:0;">{FRISE_LABELS[0]}</div>
            <div class="frise-label" style="right:0;">{FRISE_LABELS[1]}</div>
          </div>
          <div class="display" id="s5-line"
               style="font-size:60px; margin-top:96px; text-align:center; line-height:1.22;">
            Vous l'apprenez maintenant.<br />
            <span style="color:rgba(15,26,35,0.55);">
              &Ccedil;a a commenc&eacute; il y a plusieurs semaines.
            </span>
          </div>
        </div>
        <div class="logo" id="s5-logo"></div>
      </div>
    </div>

    <script>
      window.__timelines = window.__timelines || {{}};
      var tl = gsap.timeline({{ paused: true }});

      /* --- visibilité : s1/s4/s5 non-ancres (autoAlpha) ; s2/s3 ancres shader --- */
      tl.set("#s1", {{ autoAlpha: 0 }}, {S2});
      tl.set("#s2", {{ opacity: 1 }}, {S2});          /* 1re ancre : à montrer explicitement */
      /* s3 = 2e ancre — HyperShader gère son opacité, ne rien lui écrire ici. */
      tl.set("#s4", {{ autoAlpha: 1 }}, {S4}); tl.set("#s4", {{ autoAlpha: 0 }}, {S5});
      tl.set("#s5", {{ autoAlpha: 1 }}, {S5});

      /* ================= SÉQUENCE 1 — le tableau de bord siège ================= */
      tl.from("#board", {{ autoAlpha: 0, y: 40, duration: 0.9, ease: "power3.out" }}, {S1 + 0.2});
      tl.from("#row-ca", {{ autoAlpha: 0, x: -24, duration: 0.6, ease: "power2.out" }}, {S1 + 1.5});
      /* la seule ligne renseignée se remplit */
      tl.from("#row-ca-val", {{ scaleX: 0, duration: 0.8, ease: "expo.out" }}, {S1 + 2.2});
      {js_rows}
      /* le curseur survole les lignes grises — rien ne s'ouvre */
      tl.set("#cursor", {{ x: 1180, y: 560, autoAlpha: 0 }}, {S1 + 8.6});
      tl.to("#cursor", {{ autoAlpha: 1, duration: 0.3, ease: "sine.out" }}, {S1 + 8.6});
      tl.to("#cursor", {{ x: 700, y: 632, duration: 1.1, ease: "power2.inOut" }}, {S1 + 9.1});
      tl.to("#cursor", {{ y: 706, duration: 0.7, ease: "power2.inOut" }}, {S1 + 10.4});
      tl.to("#cursor", {{ y: 780, duration: 0.7, ease: "power2.inOut" }}, {S1 + 11.3});
      tl.to("#cursor", {{ autoAlpha: 0, duration: 0.4, ease: "sine.in" }}, {S1 + 12.4});
      /* respiration lente du tableau (activité de plan), puis ~2 s de silence visuel */
      tl.to("#board", {{ y: -6, duration: 1.6, ease: "sine.inOut", yoyo: true, repeat: 1 }}, {S1 + 4.0});

      /* ================= SÉQUENCE 2a — les douze barres ================= */
      tl.from("#s2-kicker", {{ autoAlpha: 0, y: -18, duration: 0.6, ease: "power2.out" }}, {S2 + 0.2});
      tl.from(".bar-row", {{
        autoAlpha: 0, x: -30, duration: 0.5, ease: "power2.out",
        stagger: {{ each: 0.11, from: "start" }}
      }}, {S2 + 0.5});
      /* toutes alignées au départ : même prix de vente, même production.
         Puis chaque barre se déforme, une par une. */
      {js_bars}
      /* la plus basse et la plus haute se surlignent */
      tl.to("#bar-{I_MIN}", {{ backgroundColor: "{ACCENT}", duration: 0.5, ease: "power2.out" }}, {S2 + 8.9});
      tl.to("#bar-{I_MAX}", {{ backgroundColor: "{ORANGE}", duration: 0.5, ease: "power2.out" }}, {S2 + 9.3});
      tl.to("#barrow-{I_MIN} .bar-label", {{ color: "{MARINE}", duration: 0.5 }}, {S2 + 8.9});
      tl.to("#barrow-{I_MAX} .bar-label", {{ color: "{MARINE}", duration: 0.5 }}, {S2 + 9.3});
      /* pas d'exit tween : le shader EST la sortie de cette scène */

      /* ================= SÉQUENCE 2b — « L'écart » ================= */
      /* trois secondes sans voix off : le plan qui doit rester en tête */
      tl.from("#s3-kicker", {{ autoAlpha: 0, duration: 0.5, ease: "power2.out" }}, {S3 + 0.25});
      tl.from("#s3-word", {{ autoAlpha: 0, yPercent: 22, duration: 0.8, ease: "power4.out" }}, {S3 + 0.4});
      tl.from("#s3-sub", {{ autoAlpha: 0, y: 22, duration: 0.6, ease: "power2.out" }}, {S3 + 1.2});
      tl.to("#s3-word", {{ y: -7, duration: 1.5, ease: "sine.inOut", yoyo: true, repeat: 1 }}, {S3 + 1.6});

      /* ================= SÉQUENCE 3 — les douze carnets ================= */
      {js_carnets}
      /* ils se referment */
      tl.to(".carnet", {{
        scaleX: 0.46, opacity: 0.5, duration: 0.7, ease: "power2.inOut",
        stagger: {{ each: 0.07, from: "start" }}
      }}, {S4 + 5.4});
      tl.from("#s4-line", {{ autoAlpha: 0, y: 26, duration: 0.7, ease: "power3.out" }}, {S4 + 7.4});
      tl.to("#s4-line", {{ y: -5, duration: 1.4, ease: "sine.inOut", yoyo: true, repeat: 1 }}, {S4 + 8.6});

      /* ================= SÉQUENCE 4 — la frise du délai ================= */
      tl.from("#frise", {{ scaleX: 0, transformOrigin: "left center", duration: 0.8, ease: "power2.out" }}, {S5 + 0.2});
      tl.to("#frise-prog", {{ width: "100%", duration: 3.4, ease: "none" }}, {S5 + 1.0});
      /* au jour 1, une fournée de trop, discrète — puis l'empilement grandit */
      {js_stack}
      tl.from("#s5-line", {{ autoAlpha: 0, y: 26, duration: 0.7, ease: "power3.out" }}, {S5 + 5.4});
      tl.from("#s5-logo", {{ autoAlpha: 0, duration: 0.6, ease: "sine.out" }}, {S5 + 6.4});
      tl.to("#s5-line", {{ y: -5, duration: 1.4, ease: "sine.inOut", yoyo: true, repeat: 1 }}, {S5 + 6.8});

      /* --- une seule chaîne shader contiguë : s2 -> s3, la révélation de l'écart --- */
      window.HyperShader.init({{
        bgColor: "{CREME}",
        scenes: ["s2", "s3"],
        timeline: tl,
        transitions: [{{ time: {XF_TIME}, shader: "cinematic-zoom", duration: {XF} }}],
      }});

      /* cale la durée de la timeline sur data-duration (le dernier tween finit
         à {S5 + 6.8 + 2.8:.1f}s ; sans ce repère, GSAP annonce {S5 + 6.8 + 2.8:.1f}s au lieu de {TOTAL}s) */
      tl.set("#main", {{}}, {TOTAL});

      window.__timelines["main"] = tl;
    </script>
  </body>
</html>
"""


if __name__ == "__main__":
    html = build()
    OUT.write_text(html, encoding="utf-8")
    kb = len(html.encode()) / 1024
    print(f"écrit {OUT}  —  {kb:.0f} Ko")
    print(f"durée totale {TOTAL}s · 5 scènes · shader s2→s3 à {XF_TIME}s")
