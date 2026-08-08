#!/usr/bin/env python3
"""
Socle commun aux deux variantes de la vidéo « Chaînes ».

Les séquences 1 à 4 partagent leur charte, leur squelette de scènes, leur
tableau de bord siège, leurs douze barres et leur frise. Seuls changent le KPI,
les libellés et la séquence 3 (carnets vs fiches techniques). Tout ce qui est
identique vit ici — les build.py de chaque variante n'apportent que leur
contenu propre.
"""

import base64
import pathlib

HERE = pathlib.Path(__file__).parent
FONTS = HERE.parent / "_fonts"

# ---------------------------------------------------------------- charte C0
CREME = "#FCF9E6"
MARINE = "#0F1A23"
ACCENT = "#007BFF"
BLEU_SYS = "#147AFF"
ORANGE = "#FFA500"  # alertes uniquement

# ------------------------------------------------------- découpage temporel
# Une scène = une séquence du brief. Volontairement longues (10-15 s) : chaque
# séquence est UNE animation continue à révélation progressive. Le guide
# HyperFrames plafonne à 5 s « sauf raison précise » — c'en est une : découper
# redémarrerait l'animation en cours.
S1, D1 = 0.0, 15.0    # séq 1 — tableau de bord siège
S2, D2 = 15.0, 13.0   # séq 2a — les 12 barres          [ANCRE SHADER 1]
S3, D3 = 28.0, 5.0    # séq 2b — « L'écart »            [ANCRE SHADER 2]
S4, D4 = 33.0, 12.0   # séq 3 — pourquoi personne ne le voit
S5, D5 = 45.0, 10.0   # séq 4 — le coût du délai
TOTAL = 55.0
XF = 0.5
XF_TIME = S3 - XF / 2  # 27.75

# Repère de délai générique (cycle comptable), pas une mesure du prospect.
FRISE_LABELS = ("Jour 1", "Jour 45")

CDN_GSAP = "https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"
CDN_RUNTIME = "https://cdn.jsdelivr.net/npm/@hyperframes/core/dist/hyperframe.runtime.iife.js"
CDN_SHADERS = "https://cdn.jsdelivr.net/npm/@hyperframes/shader-transitions/dist/index.global.js"


def b64(path: pathlib.Path) -> str:
    return base64.b64encode(path.read_bytes()).decode()


def data_uri(path: pathlib.Path, mime: str = "image/png") -> str:
    return f"data:{mime};base64,{b64(path)}"


def font_faces() -> str:
    """Fredoka (titres) + Baloo 2 (corps), inlinées en base64.

    La charte C0 demande « corps Inter ou Nunito » : le guide HyperFrames
    bannit explicitement ces deux polices. Résolu à l'intérieur de la charte
    elle-même — Fredoka et Baloo 2 y figurent toutes deux, aucune n'est bannie.
    Un <link> Google Fonts casserait le déterminisme (repli système).
    """
    out = []
    for family, fname, wmin, wmax in [
        ("Fredoka", "Fredoka-Variable.woff2", 300, 700),
        ("Baloo 2", "Baloo2-Variable.woff2", 400, 800),
    ]:
        out.append(f"""    @font-face {{
      font-family: "{family}";
      font-weight: {wmin} {wmax};
      font-style: normal;
      font-display: block;
      src: url(data:font/woff2;base64,{b64(FONTS / fname)}) format("woff2");
    }}""")
    return "\n".join(out)


def base_css(logo_uri: str) -> str:
    """CSS partagé : scènes, typographie, tableau de bord, barres, frise, logo."""
    return f"""      :root {{
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
         suivante : GSAP promeut les éléments animés en calques de composition,
         et un calque promu se rasterise au-dessus du fond d'une scène frère
         postérieure — alors même que l'ordre DOM, les styles calculés et
         elementFromPoint disent tous l'inverse. Défaut constaté au contrôle
         visuel sur la variante boulangerie, puis corrigé ici pour les deux. */
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
      .bar-fill {{ display: block; height: 100%; background: var(--bleu-sys); border-radius: 15px; }}

      /* ---------------- séquence 4 : la frise du délai ---------------- */
      .frise {{ width: 1380px; position: relative; height: 4px; background: var(--hair); }}
      .frise-prog {{
        position: absolute; left: 0; top: 0; height: 4px; width: 0;
        background: var(--marine); transform-origin: left center;
      }}
      .frise-cap {{ position: absolute; top: -13px; width: 4px; height: 30px; background: var(--marine); }}
      .frise-label {{
        position: absolute; top: 30px;
        font-family: var(--font-body); font-weight: 600; font-size: 25px; color: var(--muted);
      }}

      .logo {{
        position: absolute; right: 74px; bottom: 62px;
        width: 200px; height: 53px;
        background-image: url({logo_uri});
        background-size: contain; background-repeat: no-repeat; background-position: right bottom;
      }}"""


def board_rows(row_filled: str, rows_empty: list[str]) -> str:
    """Le tableau de bord siège : une seule ligne renseignée, le reste à vide."""
    rows = [
        f'<div class="row row-filled" id="row-ca">'
        f'<span class="row-label">{row_filled}</span>'
        f'<span class="row-value" id="row-ca-val"></span></div>'
    ]
    for i, label in enumerate(rows_empty):
        rows.append(
            f'<div class="row row-empty" id="row-e{i}">'
            f'<span class="row-label">{label}</span>'
            f'<span class="row-dash">&mdash;</span></div>'
        )
    return "\n          ".join(rows)


def bar_rows(labels: list[str], equal: float, i_min: int, i_max: int) -> str:
    out = []
    for i, label in enumerate(labels):
        cls = "bar-fill"
        if i == i_min:
            cls += " is-min"
        elif i == i_max:
            cls += " is-max"
        out.append(
            f'<div class="bar-row" id="barrow-{i}">'
            f'<span class="bar-label">{label}</span>'
            f'<span class="bar-track">'
            f'<span class="{cls}" id="bar-{i}" style="width:{equal}%"></span></span>'
            f"</div>"
        )
    return "\n          ".join(out)


def frise_html() -> str:
    return f"""<div class="frise" id="frise">
            <div class="frise-prog" id="frise-prog"></div>
            <div class="frise-cap" style="left:0;"></div>
            <div class="frise-cap" style="right:0;"></div>
            <div class="frise-label" style="left:0;">{FRISE_LABELS[0]}</div>
            <div class="frise-label" style="right:0;">{FRISE_LABELS[1]}</div>
          </div>"""


def cursor_svg() -> str:
    return f"""<svg class="cursor" id="cursor" viewBox="0 0 24 24" fill="none">
          <path d="M4 2 L4 20 L9 15.5 L12.5 22 L15.5 20.5 L12 14.5 L19 14 Z"
                fill="{MARINE}" stroke="#fff" stroke-width="1.2" stroke-linejoin="round"/>
        </svg>"""


NOTE = """      /* Le premier tween d'une scene demarre a son instant EXACT (voir README). */\n"""


def seq1_js(n_empty: int) -> str:
    """Timeline de la séquence 1 — identique aux deux variantes."""
    rows = "\n      ".join(
        f'tl.from("#row-e{i}", {{ autoAlpha: 0, x: -24, duration: 0.5, '
        f'ease: "power2.out" }}, {S1 + 5.2 + i * 0.55:.2f});'
        for i in range(n_empty)
    )
    return f"""{NOTE}tl.from("#board", {{ autoAlpha: 0, y: 40, duration: 0.9, ease: "power3.out" }}, {S1});
      tl.from("#row-ca", {{ autoAlpha: 0, x: -24, duration: 0.6, ease: "power2.out" }}, {S1 + 1.5});
      tl.from("#row-ca-val", {{ scaleX: 0, duration: 0.8, ease: "expo.out" }}, {S1 + 2.2});
      {rows}
      /* le curseur survole les lignes grises — rien ne s'ouvre */
      tl.set("#cursor", {{ x: 1180, y: 560, autoAlpha: 0 }}, {S1 + 8.6});
      tl.to("#cursor", {{ autoAlpha: 1, duration: 0.3, ease: "sine.out" }}, {S1 + 8.6});
      tl.to("#cursor", {{ x: 700, y: 632, duration: 1.1, ease: "power2.inOut" }}, {S1 + 9.1});
      tl.to("#cursor", {{ y: 706, duration: 0.7, ease: "power2.inOut" }}, {S1 + 10.4});
      tl.to("#cursor", {{ y: 780, duration: 0.7, ease: "power2.inOut" }}, {S1 + 11.3});
      tl.to("#cursor", {{ autoAlpha: 0, duration: 0.4, ease: "sine.in" }}, {S1 + 12.4});
      tl.to("#board", {{ y: -6, duration: 1.6, ease: "sine.inOut", yoyo: true, repeat: 1 }}, {S1 + 4.0});"""


def seq2_js(targets: list[int], i_min: int, i_max: int) -> str:
    """Les douze barres : alignées, puis déformées une par une, puis min/max."""
    bars = "\n      ".join(
        f'tl.to("#bar-{i}", {{ width: "{targets[i]}%", duration: 0.75, '
        f'ease: "power2.inOut" }}, {S2 + 3.4 + i * 0.32:.2f});'
        for i in range(len(targets))
    )
    return f"""{NOTE}tl.from("#s2-kicker", {{ autoAlpha: 0, y: -18, duration: 0.6, ease: "power2.out" }}, {S2});
      tl.from(".bar-row", {{
        autoAlpha: 0, x: -30, duration: 0.5, ease: "power2.out",
        stagger: {{ each: 0.11, from: "start" }}
      }}, {S2 + 0.5});
      {bars}
      /* Le minimum passe en MARINE, pas en accent #007BFF : à l'écran l'accent
         est indiscernable du bleu système #147AFF des onze autres barres — le
         surlignage du meilleur site ne se voyait pas du tout.
         Marine = la référence, orange = l'alerte. */
      tl.to("#bar-{i_min}", {{ backgroundColor: "{MARINE}", duration: 0.5, ease: "power2.out" }}, {S2 + 8.9});
      tl.to("#bar-{i_max}", {{ backgroundColor: "{ORANGE}", duration: 0.5, ease: "power2.out" }}, {S2 + 9.3});
      tl.to("#barrow-{i_min} .bar-label", {{ color: "{MARINE}", duration: 0.5 }}, {S2 + 8.9});
      tl.to("#barrow-{i_max} .bar-label", {{ color: "{MARINE}", duration: 0.5 }}, {S2 + 9.3});
      /* pas d'exit tween : le shader EST la sortie de cette scène */"""


def seq2b_js() -> str:
    """« L'écart » — trois secondes sans voix off, le plan qui doit rester."""
    return f"""{NOTE}tl.from("#s3-kicker", {{ autoAlpha: 0, duration: 0.5, ease: "power2.out" }}, {S3});
      tl.from("#s3-word", {{ autoAlpha: 0, yPercent: 22, duration: 0.8, ease: "power4.out" }}, {S3 + 0.05});
      tl.from("#s3-sub", {{ autoAlpha: 0, y: 22, duration: 0.6, ease: "power2.out" }}, {S3 + 0.9});
      tl.to("#s3-word", {{ y: -7, duration: 1.5, ease: "sine.inOut", yoyo: true, repeat: 1 }}, {S3 + 1.6});"""


def visibility_js() -> str:
    """s1/s4/s5 non-ancres (autoAlpha) ; s2/s3 ancres shader (opacity)."""
    return f"""tl.set("#s1", {{ autoAlpha: 0 }}, {S2});
      tl.set("#s2", {{ opacity: 1 }}, {S2});          /* 1re ancre : à montrer explicitement */
      /* s3 = 2e ancre — HyperShader gère son opacité, ne rien lui écrire ici. */
      tl.set("#s4", {{ autoAlpha: 1 }}, {S4}); tl.set("#s4", {{ autoAlpha: 0 }}, {S5});
      tl.set("#s5", {{ autoAlpha: 1 }}, {S5});"""


def shader_js() -> str:
    return f"""window.HyperShader.init({{
        bgColor: "{CREME}",
        scenes: ["s2", "s3"],
        timeline: tl,
        transitions: [{{ time: {XF_TIME}, shader: "cinematic-zoom", duration: {XF} }}],
      }});"""


def document(title: str, extra_css: str, logo_uri: str,
             scenes_html: str, script_body: str, duree: float = None) -> str:
    """Assemble la composition complète, conforme au contrat d'import.

    `duree` permet à un bloc plus court (le bloc de fin, séquences 7 et 9) de
    réutiliser le même socle que les variantes de 55 s.
    """
    duree = TOTAL if duree is None else duree
    return f"""<!doctype html>
<html lang="fr" style="overflow:hidden; margin:0">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1920, height=1080" />
    <title>{title}</title>
    <script src="{CDN_GSAP}"></script>
    <script src="{CDN_RUNTIME}"></script>
    <script src="{CDN_SHADERS}"></script>
    <style>
{font_faces()}

{base_css(logo_uri)}

{extra_css}
    </style>
  </head>
  <body>
    <div id="main" data-composition-id="main"
         data-width="1920" data-height="1080"
         data-start="0" data-duration="{duree}">
{scenes_html}
    </div>

    <script>
      window.__timelines = window.__timelines || {{}};
      var tl = gsap.timeline({{ paused: true }});

{script_body}

      /* cale la durée de la timeline sur data-duration */
      tl.set("#main", {{}}, {duree});

      window.__timelines["main"] = tl;
    </script>
  </body>
</html>
"""
