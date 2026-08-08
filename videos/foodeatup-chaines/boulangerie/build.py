#!/usr/bin/env python3
"""
Génère index.html — vidéo « Chaînes », variante BOULANGERIE, séquences 1 à 4.

KPI : le taux d'invendus par magasin.
Le socle commun (charte, scènes, tableau de bord, barres, frise) vit dans
../_shared/base.py — ici, uniquement ce qui est propre à la boulangerie.

Régénérer :  python3 build.py
"""

import pathlib
import sys

HERE = pathlib.Path(__file__).parent
sys.path.insert(0, str(HERE.parent / "_shared"))

import base as B  # noqa: E402

IMG = HERE / "assets" / "img"
OUT = HERE / "index.html"

# ------------------------------------------------- données séquence 2 (barres)
# Longueurs RELATIVES, sans axe ni pourcentage affiché : SOURCES.md ne contient
# aucun chiffre [SOURCÉ], donc l'écart est MONTRÉ, jamais quantifié.
# Suite figée en dur — le déterminisme du rendu interdit Math.random().
BAR_LABELS = [f"Magasin {i:02d}" for i in range(1, 13)]
BAR_EQUAL = 55.0
BAR_TARGET = [38, 46, 41, 63, 44, 52, 79, 47, 43, 58, 49, 45]
I_MIN = BAR_TARGET.index(min(BAR_TARGET))   # Magasin 01
I_MAX = BAR_TARGET.index(max(BAR_TARGET))   # Magasin 07

# Lignes du tableau de bord siège — séquence 1 (boulangerie).
ROW_FILLED = "CA consolidé"
ROWS_EMPTY = [
    "Invendus par magasin",
    "Coût matière par magasin",
    "Écart production / vente",
    "Marge par référence",
    "Taux de rupture avant 11 h",
]

N_FOURNEES = 5


def build() -> str:
    carnet_uri = B.data_uri(IMG / "carnet.png")
    fournee_uri = B.data_uri(IMG / "fournee.png")
    logo_uri = B.data_uri(IMG / "logo-horizontal.png")

    carnets = "\n            ".join(
        f'<div class="carnet" id="carnet-{i}"></div>' for i in range(12)
    )
    # Chaque fournée se pose PLUS HAUT que la précédente et légèrement décalée :
    # sans ces offsets les 5 plateaux se superposent au pixel près et
    # l'empilement ne se voit pas du tout (constaté au contrôle visuel).
    stacks = "\n            ".join(
        f'<div class="fournee" id="fournee-{i}" '
        f'style="bottom:{i * 38}px; margin-left:{-130 + (10 if i % 2 else -10)}px;"></div>'
        for i in range(N_FOURNEES)
    )

    js_carnets = "\n      ".join(
        f'tl.from("#carnet-{i}", {{ autoAlpha: 0, y: 34, scale: 0.86, duration: 0.55, '
        f'ease: "back.out(1.4)" }}, {B.S4 + i * 0.16:.2f});'
        for i in range(12)
    )
    js_stack = "\n      ".join(
        f'tl.from("#fournee-{i}", {{ autoAlpha: 0, y: -30, duration: 0.45, '
        f'ease: "power2.out" }}, {B.S5 + 2.2 + i * 0.42:.2f});'
        for i in range(N_FOURNEES)
    )

    extra_css = f"""      /* ---------------- séquence 3 : les douze carnets ---------------- */
      .carnets {{
        display: grid; grid-template-columns: repeat(6, 250px);
        gap: 34px 30px; justify-content: center;
      }}
      .carnet {{
        width: 250px; height: 220px;
        background-image: url({carnet_uri});
        background-size: contain; background-repeat: no-repeat; background-position: center;
      }}

      /* ---------------- séquence 4 : l'empilement des fournées ---------------- */
      .stack {{ position: relative; width: 560px; height: 390px; margin-bottom: 78px; }}
      .fournee {{
        position: absolute; left: 50%; width: 260px; height: 206px;
        background-image: url({fournee_uri});
        background-size: contain; background-repeat: no-repeat; background-position: bottom center;
      }}"""

    scenes = f"""      <!-- ============ SÉQUENCE 1 — le chiffre qui manque ============ -->
      <div class="scene clip" id="s1" data-start="{B.S1}" data-duration="{B.D1}" data-track-index="0">
        <div class="scene-content">
          <div class="board" id="board">
            <div class="board-head">
              <span class="board-title">Tableau de bord</span>
              <span class="board-scope">Si&egrave;ge &middot; 12 magasins</span>
            </div>
          {B.board_rows(ROW_FILLED, ROWS_EMPTY)}
          </div>
        </div>
        {B.cursor_svg()}
      </div>

      <!-- ============ SÉQUENCE 2a — l'écart révélé [ANCRE 1] ============ -->
      <div class="scene clip" id="s2" data-start="{B.S2}" data-duration="{B.D2}" data-track-index="0"
           style="opacity:0;">
        <div class="scene-content">
          <div class="kicker" id="s2-kicker" style="margin-bottom:38px;">
            Taux d'invendus &middot; m&ecirc;me production, m&ecirc;mes horaires
          </div>
          <div class="bars">
          {B.bar_rows(BAR_LABELS, BAR_EQUAL, I_MIN, I_MAX)}
          </div>
        </div>
      </div>

      <!-- ============ SÉQUENCE 2b — « L'écart » [ANCRE 2] ============ -->
      <div class="scene clip" id="s3" data-start="{B.S3}" data-duration="{B.D3}" data-track-index="0"
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

      <!-- ============ SÉQUENCE 3 — pourquoi personne ne le voit ============ -->
      <div class="scene clip" id="s4" data-start="{B.S4}" data-duration="{B.D4}" data-track-index="0"
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

      <!-- ============ SÉQUENCE 4 — le coût du délai ============ -->
      <div class="scene clip" id="s5" data-start="{B.S5}" data-duration="{B.D5}" data-track-index="0"
           style="visibility:hidden;">
        <div class="scene-content">
          <div class="stack" id="stack">
            {stacks}
          </div>
          {B.frise_html()}
          <div class="display" id="s5-line"
               style="font-size:60px; margin-top:96px; text-align:center; line-height:1.22;">
            Vous l'apprenez maintenant.<br />
            <span style="color:rgba(15,26,35,0.55);">
              &Ccedil;a a commenc&eacute; il y a plusieurs semaines.
            </span>
          </div>
        </div>
        <div class="logo" id="s5-logo"></div>
      </div>"""

    script = f"""      /* --- visibilité des scènes --- */
      {B.visibility_js()}

      /* ================= SÉQUENCE 1 — le tableau de bord siège ================= */
      {B.seq1_js(len(ROWS_EMPTY))}

      /* ================= SÉQUENCE 2a — les douze barres ================= */
      {B.seq2_js(BAR_TARGET, I_MIN, I_MAX)}

      /* ================= SÉQUENCE 2b — « L'écart » ================= */
      {B.seq2b_js()}

      /* ================= SÉQUENCE 3 — les douze carnets ================= */
      {js_carnets}
      /* ils se referment */
      tl.to(".carnet", {{
        scaleX: 0.46, opacity: 0.5, duration: 0.7, ease: "power2.inOut",
        stagger: {{ each: 0.07, from: "start" }}
      }}, {B.S4 + 5.4});
      tl.from("#s4-line", {{ autoAlpha: 0, y: 26, duration: 0.7, ease: "power3.out" }}, {B.S4 + 7.4});
      tl.to("#s4-line", {{ y: -5, duration: 1.4, ease: "sine.inOut", yoyo: true, repeat: 1 }}, {B.S4 + 8.6});

      /* ================= SÉQUENCE 4 — la frise du délai ================= */
      tl.to("#frise-prog", {{ width: "100%", duration: 3.4, ease: "none" }}, {B.S5 + 1.0});
      /* au jour 1, une fournée de trop, discrète — puis l'empilement grandit */
      {js_stack}
      tl.from("#s5-line", {{ autoAlpha: 0, y: 26, duration: 0.7, ease: "power3.out" }}, {B.S5 + 5.4});
      tl.from("#s5-logo", {{ autoAlpha: 0, duration: 0.6, ease: "sine.out" }}, {B.S5 + 6.4});
      tl.to("#s5-line", {{ y: -5, duration: 1.4, ease: "sine.inOut", yoyo: true, repeat: 1 }}, {B.S5 + 6.8});

      /* --- une seule chaîne shader contiguë : s2 -> s3 --- */
      {B.shader_js()}"""

    return B.document(
        "FoodEatUp — Chaînes — Boulangerie — séquences 1 à 4",
        extra_css, logo_uri, scenes, script)


if __name__ == "__main__":
    html = build()
    OUT.write_text(html, encoding="utf-8")
    print(f"écrit {OUT}  —  {len(html.encode()) / 1024:.0f} Ko")
    print(f"durée totale {B.TOTAL}s · 5 scènes · shader s2→s3 à {B.XF_TIME}s")
