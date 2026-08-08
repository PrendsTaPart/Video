#!/usr/bin/env python3
"""
Génère index.html — vidéo « Chaînes », variante RESTAURATION, séquences 1 à 4.

KPI : le food cost par site, à carte identique.
Le socle commun (charte, scènes, tableau de bord, barres, frise) vit dans
../_shared/base.py — ici, uniquement ce qui est propre à la restauration.

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
BAR_LABELS = [f"Site {i:02d}" for i in range(1, 13)]
BAR_EQUAL = 55.0
BAR_TARGET = [48, 55, 39, 62, 51, 44, 58, 46, 81, 53, 49, 57]
I_MIN = BAR_TARGET.index(min(BAR_TARGET))   # Site 03
I_MAX = BAR_TARGET.index(max(BAR_TARGET))   # Site 09

# Séquence 3 — douze fiches techniques du MÊME plat.
# Trois lignes d'ingrédients par fiche ; le grammage est rendu par une BARRE
# orange de longueur variable, jamais par un nombre : afficher des grammes
# reviendrait à écrire à l'écran des chiffres absents de SOURCES.md.
DISH_NAME = "Burger maison"
GRAMMAGES = [
    [62, 48, 35], [70, 44, 40], [55, 56, 31], [78, 40, 44], [60, 52, 28], [66, 46, 38],
    [52, 60, 33], [74, 42, 47], [58, 50, 30], [68, 54, 36], [64, 45, 42], [56, 58, 34],
]

# Lignes du tableau de bord siège — séquence 1 (restauration).
ROW_FILLED = "CA consolidé"
ROWS_EMPTY = [
    "Food cost par site",
    "Marge par plat",
    "Écart de grammage",
    "Coût du travail rapporté au CA",
    "Ticket moyen par site",
]

# Séquence 4 — deux courbes : le prix fournisseur monte, la marge s'érode.
PRIX_PTS = "0,206 200,201 400,184 600,158 800,132 1000,108 1200,84"
MARGE_PTS = "0,64 200,70 400,88 600,116 800,142 1000,166 1200,192"


def build() -> str:
    plat_uri = B.data_uri(IMG / "plat.png")
    logo_uri = B.data_uri(IMG / "logo-horizontal.png")

    # --- séquence 3 : les douze fiches techniques ---
    fiches = []
    for i, grams in enumerate(GRAMMAGES):
        lignes = "".join(
            f'<span class="fiche-ing"><i class="fiche-dot"></i>'
            f'<i class="fiche-qty" style="width:{g}%"></i></span>'
            for g in grams
        )
        fiches.append(
            f'<div class="fiche" id="fiche-{i}">'
            f'<div class="fiche-img"></div>'
            f'<div class="fiche-name">{DISH_NAME}</div>'
            f'<div class="fiche-lines">{lignes}</div>'
            f"</div>"
        )
    fiches_html = "\n            ".join(fiches)

    js_fiches = "\n      ".join(
        f'tl.from("#fiche-{i}", {{ autoAlpha: 0, y: 34, scale: 0.88, duration: 0.55, '
        f'ease: "back.out(1.4)" }}, {B.S4 + 0.3 + i * 0.16:.2f});'
        for i in range(12)
    )

    extra_css = f"""      /* ---------------- séquence 3 : les douze fiches techniques ---------------- */
      .fiches {{
        display: grid; grid-template-columns: repeat(6, 262px);
        gap: 26px 24px; justify-content: center;
      }}
      .fiche {{
        width: 262px; background: #fff; border-radius: 16px;
        border: 1px solid var(--hair); box-shadow: 0 14px 34px rgba(15, 26, 35, 0.07);
        padding: 16px 18px 18px; display: flex; flex-direction: column; align-items: center;
      }}
      .fiche-img {{
        width: 132px; height: 103px;
        background-image: url({plat_uri});
        background-size: contain; background-repeat: no-repeat; background-position: center;
      }}
      .fiche-name {{
        font-family: var(--font-body); font-weight: 600; font-size: 21px;
        margin: 8px 0 12px; color: var(--marine);
      }}
      .fiche-lines {{ width: 100%; display: flex; flex-direction: column; gap: 9px; }}
      .fiche-ing {{ display: flex; align-items: center; gap: 9px; }}
      .fiche-dot {{
        width: 8px; height: 8px; flex: none; border-radius: 50%;
        background: rgba(15, 26, 35, 0.22);
      }}
      /* le grammage : une barre, jamais un nombre */
      .fiche-qty {{ height: 9px; border-radius: 5px; background: var(--orange); }}

      /* ---------------- séquence 4 : prix fournisseur vs marge ---------------- */
      .courbes {{ position: relative; width: 1200px; height: 260px; margin-bottom: 92px; }}
      .courbe-legende {{
        position: absolute; font-family: var(--font-body); font-weight: 600; font-size: 24px;
      }}"""

    scenes = f"""      <!-- ============ SÉQUENCE 1 — le chiffre qui manque ============ -->
      <div class="scene clip" id="s1" data-start="{B.S1}" data-duration="{B.D1}" data-track-index="0">
        <div class="scene-content">
          <div class="board" id="board">
            <div class="board-head">
              <span class="board-title">Tableau de bord</span>
              <span class="board-scope">Si&egrave;ge &middot; 12 restaurants</span>
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
            Food cost par site &middot; m&ecirc;me plat, m&ecirc;me prix de vente
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
          <div class="kicker" id="s3-kicker">Site 03 &nbsp;&mdash;&nbsp; Site 09</div>
          <div class="display" id="s3-word" style="font-size:250px; margin:12px 0 22px;">
            L'&eacute;cart
          </div>
          <div class="body" id="s3-sub" style="font-size:44px; color:rgba(15,26,35,0.62);">
            Personne dans l'entreprise ne saurait le dire site par site.
          </div>
        </div>
      </div>

      <!-- ============ SÉQUENCE 3 — douze fiches du même plat ============ -->
      <div class="scene clip" id="s4" data-start="{B.S4}" data-duration="{B.D4}" data-track-index="0"
           style="visibility:hidden;">
        <div class="scene-content">
          <div class="fiches" id="fiches">
            {fiches_html}
          </div>
          <div class="display" id="s4-line" style="font-size:76px; margin-top:48px;">
            Le m&ecirc;me plat. Douze recettes.
          </div>
        </div>
      </div>

      <!-- ============ SÉQUENCE 4 — le coût du délai ============ -->
      <div class="scene clip" id="s5" data-start="{B.S5}" data-duration="{B.D5}" data-track-index="0"
           style="visibility:hidden;">
        <div class="scene-content">
          <div class="courbes" id="courbes">
            <svg viewBox="0 0 1200 260" width="1200" height="260" fill="none">
              <polyline id="c-prix" points="{PRIX_PTS}" stroke="{B.ORANGE}" stroke-width="7"
                        stroke-linecap="round" stroke-linejoin="round"
                        stroke-dasharray="1300" stroke-dashoffset="1300"/>
              <polyline id="c-marge" points="{MARGE_PTS}" stroke="{B.MARINE}" stroke-width="7"
                        stroke-linecap="round" stroke-linejoin="round"
                        stroke-dasharray="1300" stroke-dashoffset="1300"/>
            </svg>
            <!-- légendes dégagées verticalement : la courbe prix finit à y=84 et
                 la courbe marge à y=192 — posées à ces hauteurs, les libellés
                 chevauchaient le trait. -->
            <span class="courbe-legende" id="lg-prix"
                  style="right:0; top:34px; color:{B.ORANGE};">Prix fournisseur</span>
            <span class="courbe-legende" id="lg-marge"
                  style="right:0; top:202px; color:{B.MARINE};">Marge</span>
          </div>
          {B.frise_html()}
          <div class="display" id="s5-line"
               style="font-size:60px; margin-top:96px; text-align:center; line-height:1.22;">
            Le chiffre d'affaires n'a rien dit.<br />
            <span style="color:rgba(15,26,35,0.55);">La marge, si.</span>
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

      /* ================= SÉQUENCE 3 — les douze fiches ================= */
      {js_fiches}
      /* les grammages se révèlent : même plat, douze recettes */
      tl.from(".fiche-qty", {{
        scaleX: 0, transformOrigin: "left center", duration: 0.5, ease: "power2.out",
        stagger: {{ each: 0.035, from: "start" }}
      }}, {B.S4 + 2.6});
      tl.from("#s4-line", {{ autoAlpha: 0, y: 26, duration: 0.7, ease: "power3.out" }}, {B.S4 + 7.4});
      tl.to("#s4-line", {{ y: -5, duration: 1.4, ease: "sine.inOut", yoyo: true, repeat: 1 }}, {B.S4 + 8.6});

      /* ================= SÉQUENCE 4 — prix fournisseur vs marge ================= */
      tl.to("#c-prix", {{ strokeDashoffset: 0, duration: 2.6, ease: "none" }}, {B.S5 + 0.4});
      tl.to("#c-marge", {{ strokeDashoffset: 0, duration: 2.6, ease: "none" }}, {B.S5 + 0.4});
      tl.from("#lg-prix", {{ autoAlpha: 0, x: 24, duration: 0.5, ease: "power2.out" }}, {B.S5 + 2.4});
      tl.from("#lg-marge", {{ autoAlpha: 0, x: 24, duration: 0.5, ease: "power2.out" }}, {B.S5 + 2.7});
      tl.from("#frise", {{ scaleX: 0, transformOrigin: "left center", duration: 0.8, ease: "power2.out" }}, {B.S5 + 0.2});
      tl.to("#frise-prog", {{ width: "100%", duration: 3.0, ease: "none" }}, {B.S5 + 0.9});
      tl.from("#s5-line", {{ autoAlpha: 0, y: 26, duration: 0.7, ease: "power3.out" }}, {B.S5 + 5.4});
      tl.from("#s5-logo", {{ autoAlpha: 0, duration: 0.6, ease: "sine.out" }}, {B.S5 + 6.4});
      tl.to("#s5-line", {{ y: -5, duration: 1.4, ease: "sine.inOut", yoyo: true, repeat: 1 }}, {B.S5 + 6.8});

      /* --- une seule chaîne shader contiguë : s2 -> s3 --- */
      {B.shader_js()}"""

    return B.document(
        "FoodEatUp — Chaînes — Restauration — séquences 1 à 4",
        extra_css, logo_uri, scenes, script)


if __name__ == "__main__":
    html = build()
    OUT.write_text(html, encoding="utf-8")
    print(f"écrit {OUT}  —  {len(html.encode()) / 1024:.0f} Ko")
    print(f"durée totale {B.TOTAL}s · 5 scènes · shader s2→s3 à {B.XF_TIME}s")
