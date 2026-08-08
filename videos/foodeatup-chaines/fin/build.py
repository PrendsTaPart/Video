#!/usr/bin/env python3
"""
Génère index.html — bloc de FIN : séquences 7 et 9 du tronc commun, ~22 s.

Ce bloc est un tronc commun PARTIEL, et c'est délibéré.
Les séquences 5, 6 et 8 montrent une vue consolidée multi-établissements qui
n'existe pas dans le MCP FoodEatUp (voir SOURCES.md) : elles ne sont pas
produites. Les séquences 7 et 9, elles, ne contiennent AUCUN écran produit —
la 7 est un argument de risque de marque, la 9 est une carte d'offre. Elles se
montent donc derrière n'importe laquelle des deux variantes pour lui donner une
fin et un appel à l'action.

Coupes franches, aucun shader : « registre sobre, aucun mouvement de caméra »
pour la séquence 7.

Régénérer :  python3 build.py
"""

import pathlib
import sys

HERE = pathlib.Path(__file__).parent
sys.path.insert(0, str(HERE.parent / "_shared"))

import base as B  # noqa: E402

IMG = HERE / "assets" / "img"
OUT = HERE / "index.html"

F1, DF1 = 0.0, 12.0    # séq 7 — le risque d'enseigne
F2, DF2 = 12.0, 10.0   # séq 9 — l'offre
TOTAL = 22.0

# Douze points sur la carte, en % du cadre de la carte. Positions figées en dur
# (le déterminisme interdit Math.random()). Aucune ville n'est nommée.
POINTS = [(52, 9), (40, 19), (48, 26), (84, 25), (22, 31), (23, 43),
          (65, 42), (68, 56), (28, 63), (43, 77), (69, 80), (83, 76)]
I_ALERTE = 7   # le point qui bascule

# Aucun nom d'enseigne réelle (interdit C0) : un libellé générique fait le point
# aussi bien, et c'est le prospect qui se projette dedans.
ENSEIGNE = "VOTRE ENSEIGNE"

CTA = "Demander le pilote"
CTA_URL = "foodeatup.com"


def build() -> str:
    carte_uri = B.data_uri(IMG / "carte-france.png")
    logo_uri = B.data_uri(IMG / "logo-horizontal.png")

    pts = "\n            ".join(
        f'<span class="pt{" is-alerte" if i == I_ALERTE else ""}" id="pt-{i}" '
        f'style="left:{x}%; top:{y}%;"></span>'
        for i, (x, y) in enumerate(POINTS)
    )
    js_pts = "\n      ".join(
        f'tl.from("#pt-{i}", {{ autoAlpha: 0, scale: 0, duration: 0.4, '
        f'ease: "back.out(2)" }}, {F1 + 1.0 + i * 0.09:.2f});'
        for i in range(len(POINTS))
    )

    extra_css = f"""      /* ---------------- séquence 7 : le risque d'enseigne ---------------- */
      .carte-wrap {{ position: relative; width: 520px; height: 529px; }}
      .carte {{
        position: absolute; inset: 0;
        background-image: url({carte_uri});
        background-size: contain; background-repeat: no-repeat; background-position: center;
      }}
      .pt {{
        position: absolute; width: 20px; height: 20px; margin: -10px 0 0 -10px;
        border-radius: 50%; background: var(--creme);
        box-shadow: 0 0 0 3px rgba(252, 249, 230, 0.55);
      }}
      .pt.is-alerte {{ background: var(--creme); }}
      .halo {{
        position: absolute; width: 20px; height: 20px; margin: -10px 0 0 -10px;
        border-radius: 50%; border: 3px solid var(--orange); opacity: 0;
      }}
      .enseigne {{
        font-family: var(--font-body); font-weight: 800; font-size: 34px;
        letter-spacing: 0.3em; color: var(--marine); margin-bottom: 26px;
      }}

      /* ---------------- séquence 9 : l'offre ---------------- */
      .offre {{
        font-family: var(--font-display); font-weight: 600; font-size: 108px;
        line-height: 1.12; text-align: center;
      }}
      .cta {{
        display: inline-flex; align-items: center; gap: 18px;
        background: var(--orange); color: var(--marine);
        font-family: var(--font-body); font-weight: 800; font-size: 40px;
        padding: 26px 54px; border-radius: 999px; margin-top: 58px;
      }}
      .cta-url {{
        font-family: var(--font-body); font-weight: 600; font-size: 30px;
        color: var(--muted); margin-top: 26px; letter-spacing: 0.08em;
      }}"""

    scenes = f"""      <!-- ============ SÉQUENCE 7 — le risque d'enseigne ============ -->
      <div class="scene clip" id="s1" data-start="{F1}" data-duration="{DF1}" data-track-index="0">
        <div class="scene-content">
          <div class="enseigne" id="enseigne">{ENSEIGNE}</div>
          <div class="carte-wrap" id="carte-wrap">
            <div class="carte"></div>
            {pts}
            <span class="halo" id="halo"
                  style="left:{POINTS[I_ALERTE][0]}%; top:{POINTS[I_ALERTE][1]}%;"></span>
          </div>
          <div class="body" id="s1-line"
               style="font-size:46px; margin-top:44px; text-align:center; line-height:1.3;">
            Le contr&ocirc;le porte sur un site.<br />
            <span style="font-weight:600;">La r&eacute;putation porte sur la marque.</span>
          </div>
        </div>
      </div>

      <!-- ============ SÉQUENCE 9 — l'offre ============ -->
      <div class="scene clip" id="s2" data-start="{F2}" data-duration="{DF2}" data-track-index="0"
           style="visibility:hidden;">
        <div class="scene-content">
          <div class="offre" id="offre">
            Trois sites. Soixante jours.<br /><span id="offre-2">Vos chiffres.</span>
          </div>
          <div class="cta" id="cta">{CTA}</div>
          <div class="cta-url" id="cta-url">{CTA_URL}</div>
        </div>
        <div class="logo" id="logo"></div>
      </div>"""

    script = f"""      /* --- visibilité : deux scènes non-ancres, coupes franches --- */
      tl.set("#s1", {{ autoAlpha: 0 }}, {F2});
      tl.set("#s2", {{ autoAlpha: 1 }}, {F2});

      /* ================= SÉQUENCE 7 — le risque d'enseigne ================= */
      /* Registre sobre : la carte ne bouge pas, seuls les points apparaissent. */
      tl.from("#carte-wrap", {{ autoAlpha: 0, duration: 1.0, ease: "power2.out" }}, {F1 + 0.2});
      tl.from("#enseigne", {{ autoAlpha: 0, y: -16, duration: 0.7, ease: "power2.out" }}, {F1 + 0.4});
      {js_pts}
      /* un seul point bascule — l'orange est réservé aux alertes */
      tl.to("#pt-{I_ALERTE}", {{ backgroundColor: "{B.ORANGE}", scale: 1.35,
        duration: 0.5, ease: "power2.out" }}, {F1 + 4.2});
      tl.fromTo("#halo", {{ scale: 1, opacity: 0.9 }},
        {{ scale: 3.4, opacity: 0, duration: 1.8, ease: "power2.out" }}, {F1 + 4.3});
      tl.fromTo("#halo", {{ scale: 1, opacity: 0.7 }},
        {{ scale: 3.4, opacity: 0, duration: 1.8, ease: "power2.out" }}, {F1 + 6.1});
      tl.to("#enseigne", {{ color: "{B.ORANGE}", duration: 0.6, ease: "power2.out" }}, {F1 + 4.6});
      tl.from("#s1-line", {{ autoAlpha: 0, y: 22, duration: 0.7, ease: "power3.out" }}, {F1 + 6.6});
      tl.to("#s1-line", {{ y: -4, duration: 1.5, ease: "sine.inOut", yoyo: true, repeat: 1 }}, {F1 + 8.0});

      /* ================= SÉQUENCE 9 — l'offre ================= */
      /* Entrée calée sur le DÉBUT EXACT de la scène, sans les 0,2 s d'usage :
         tous les éléments de ce plan sont animés en `tl.from()`, et GSAP applique
         leur état de départ dès la construction (immediateRender). Avec un retard,
         la scène était visible mais tout son contenu encore invisible — une image
         entièrement vide à la coupe, mesurée sur le MP4. */
      tl.from("#offre", {{ autoAlpha: 0, y: 30, duration: 0.8, ease: "power3.out" }}, {F2});
      tl.from("#offre-2", {{ autoAlpha: 0, duration: 0.6, ease: "power2.out" }}, {F2 + 0.9});
      tl.from("#cta", {{ autoAlpha: 0, scale: 0.86, duration: 0.6, ease: "back.out(1.6)" }}, {F2 + 1.6});
      tl.from("#cta-url", {{ autoAlpha: 0, duration: 0.5, ease: "power2.out" }}, {F2 + 2.2});
      tl.from("#logo", {{ autoAlpha: 0, duration: 0.6, ease: "sine.out" }}, {F2 + 2.6});
      /* respiration du bouton : un seul point de sortie, on le tient à l'écran */
      tl.to("#cta", {{ scale: 1.035, duration: 1.6, ease: "sine.inOut", yoyo: true, repeat: 1 }}, {F2 + 3.2});
      tl.to("#offre", {{ y: -5, duration: 1.6, ease: "sine.inOut", yoyo: true, repeat: 1 }}, {F2 + 3.4});"""

    return B.document("FoodEatUp — Chaînes — Fin (séquences 7 et 9)",
                      extra_css, logo_uri, scenes, script, duree=TOTAL)


if __name__ == "__main__":
    html = build()
    OUT.write_text(html, encoding="utf-8")
    print(f"écrit {OUT}  —  {len(html.encode()) / 1024:.0f} Ko")
    print(f"durée totale {TOTAL}s · 2 scènes · coupes franches")
