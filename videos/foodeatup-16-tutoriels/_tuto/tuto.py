#!/usr/bin/env python3
"""Grammaire de motion design des seize tutoriels sans rush.

**Pourquoi une grammaire séparée de celle des neuf films.** `_serie/serie.py`
raconte une journée : horloge, surtitre de moment, liseré métier, cadre tablette
qui joue un rush. Un tutoriel ne raconte pas un moment, il enseigne un geste, et
il n'a pas de rush. Les deux partagent la charte du site — c'est tout ce qu'ils
ont à partager, et le reste diverge assez pour qu'un module commun devienne un
sac de conditions.

**Ce que ces films assument.** Aucun plan ne prétend être une capture d'écran.
Une planche schématique dit « voici l'étape, voici ce qui compte » ; une fausse
interface dirait « voici le produit », ce qui serait faux tant que le rush
n'existe pas. Le jour où Michael filme, ces films sont remplacés — les scripts,
eux, restent.

Trois pièges de HyperFrames, repris de la grammaire des films et payés une fois
chacun :

1. **HyperFrames jette le `<head>` des sous-compositions.** Le bloc de style est
   donc répété intégralement dans chaque scène. Le recopier à la main sur seize
   films de sept scènes, ce sont cent douze occasions de laisser diverger la
   charte : il vit ici.
2. **GSAP réécrit tout le `transform`** dès qu'il anime `scale` ou `x`. Rien qui
   doive survivre à un tween ne peut vivre en CSS — les centrages sont posés en
   absolu, jamais en `translate`.
3. **Un clip imbriqué déclare sa durée en temps ABSOLU du film.** Une scène qui
   commence à `A` et dure `D` déclare `data-duration = A + D`, sinon sa fenêtre
   se comporte comme `[A, D]` et le clip reste visible tout du long. D'où
   `abs_debut` sur chaque scène.
"""

import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]

# Charte du site (src/styles.css), convertie depuis oklch. Films et site
# partagent une seule palette — voir NOTES.md §5 bis.1.
CREAM = "#FCF9E6"
CREAM_DEEP = "#F5F0D4"
INK = "#0F1A23"
INK_SOFT = "#4C5760"
BORDER = "#E3DDC0"
BLEU = "#007BFF"
ORANGE = "#FFA500"
BLANC = "#FFFFFF"

# Accent par module : le même code couleur que les catégories du site, pour
# qu'un tutoriel se rattache visuellement à son module sans le nommer.
ACCENTS = {
    "caisse-pos": "#0D6EFD",
    "hubrise-livraisons": "#7C3AED",
    "kds-cuisine": "#E8590C",
    "site-web-vitrine": "#0CA678",
    "marketing-fidelite": "#D6336C",
    "comptabilite": "#1C7ED6",
}

NOMS_MODULES = {
    "caisse-pos": "Caisse POS & Matériel",
    "hubrise-livraisons": "HubRise & Livraisons",
    "kds-cuisine": "Écran Cuisine (KDS)",
    "site-web-vitrine": "Site Web & Vitrine",
    "marketing-fidelite": "Marketing, Fidélité & Iris",
    "comptabilite": "Comptabilité & Achats",
}

_TEMPLATE = """<!doctype html>
<html>
  <head><meta charset="UTF-8" /></head>
  <body>
    <template>
      <style>{style}
      </style>

      <div id="root" data-composition-id="{cid}" data-width="1920" data-height="1080" data-duration="{dur}">
        <div class="accent"></div>
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

_BG_HTML = """        <div class="glow glow-a" id="glowA"></div>
        <div class="glow glow-b" id="glowB"></div>
        <div class="grid" id="grid"></div>
"""


def _repeat(cycle, dur):
    """Répétitions couvrant tout juste la scène.

    `repeat: -1` déclenche un avertissement de troncature au lint. Un compte
    fini donne le même rendu et le rend explicitement déterministe — donc le
    lint reste lisible, et utile le jour où un vrai problème apparaît.
    """
    return max(1, math.ceil(float(dur) / cycle))


def _echapper(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


class Tuto:
    def __init__(self, module, sous):
        self.module = module
        self.accent = ACCENTS[module]
        self.sous = sous
        self.out = ROOT / "studio-video" / "compositions" / sous

    # ── style, répété dans chaque scène ────────────────────────────────────
    @property
    def style(self):
        return f"""
        @font-face {{
          font-family: "Fredoka";
          src: url("assets/vendor/fonts/Fredoka-Variable.woff2") format("woff2-variations");
          font-weight: 300 700; font-display: block;
        }}
        #root {{ position:absolute; inset:0; background:{CREAM}; overflow:hidden;
                 font-family:"Inter",sans-serif; }}

        /* Fond à la charte : le crème du site, plus les deux halos du hero.
           Ils respirent lentement — un aplat immobile pendant cinquante
           secondes se lit comme une image figée, et on croit la vidéo bloquée. */
        .glow {{ position:absolute; border-radius:50%; filter:blur(10px); }}
        .glow-a {{ left:-360px; top:-420px; width:1500px; height:820px;
                   background:radial-gradient(closest-side, rgba(0,123,255,.16), rgba(0,123,255,0) 70%); }}
        .glow-b {{ right:-420px; top:-360px; width:1400px; height:760px;
                   background:radial-gradient(closest-side, rgba(255,165,0,.22), rgba(255,165,0,0) 70%); }}
        .grid {{ position:absolute; left:-160px; top:-160px; width:2280px; height:1420px;
                 background-image:radial-gradient(circle at 1px 1px, {BORDER} 0 2px, transparent 2px);
                 background-size:48px 48px; opacity:.55; }}

        /* Liseré d'accent : signature du module, en haut de cadre. */
        .accent {{ position:absolute; top:0; left:0; right:0; height:6px; background:{self.accent}; }}

        .eyebrow {{ position:absolute; top:58px; left:120px; right:120px;
                    font-family:"Fredoka",sans-serif; font-weight:600; font-size:38px;
                    letter-spacing:.06em; text-transform:uppercase;
                    color:{self.accent}; opacity:0; }}

        .etape {{ position:absolute; top:58px; right:120px; font-family:"Fredoka",sans-serif;
                  font-weight:700; font-size:38px; color:{INK_SOFT}; opacity:0; }}

        /* La planche : le bloc de contenu d'une scène. Posée en absolu et
           centrée par `left/right`, jamais par `translate` — GSAP réécrit le
           transform entier dès qu'il touche à `scale`. */
        /* La carte occupe toute la bande centrale et centre son texte, plutôt
           que de coller en haut et de laisser trois cents pixels de vide
           au-dessus de la frise. Le centrage est fait par `align-items`, jamais
           par `translate` : GSAP anime `y` sur cette carte, et un tween qui
           touche au transform effacerait un `translateY(-50%)` posé en CSS. */
        .board {{ position:absolute; left:150px; right:150px; top:190px; bottom:250px;
                  display:flex; align-items:center;
                  background:{BLANC}; border:2px solid {BORDER}; border-radius:38px;
                  padding:56px 72px; opacity:0;
                  box-shadow:0 26px 60px rgba(15,26,35,.10); }}

        .phrase {{ font-family:"Fredoka",sans-serif; font-weight:600; font-size:60px;
                   line-height:1.24; color:{INK}; }}
        .phrase b {{ color:{self.accent}; font-weight:700; }}

        .jalons {{ position:absolute; left:150px; right:150px; bottom:110px;
                   display:flex; gap:22px; }}
        .jalon {{ flex:1; border:2px solid {BORDER}; border-radius:22px; background:{CREAM_DEEP};
                  padding:22px 26px; font-family:"Fredoka",sans-serif; font-weight:600;
                  font-size:32px; color:{INK_SOFT}; text-align:center; opacity:.45; }}
        .jalon.on {{ background:{self.accent}; border-color:{self.accent}; color:{BLANC}; opacity:1; }}

        /* La plaque : un plan réel de la bibliothèque, plein cadre, derrière le
           carton. Le voile qui la couvre n'est pas décoratif — sans lui, un
           titre blanc posé sur une image contrastée devient illisible dès que
           l'image bouge, et elle bouge tout le temps. */
        .plaque {{ position:absolute; inset:0; width:1920px; height:1080px;
                   object-fit:cover; opacity:0; }}
        .voile {{ position:absolute; inset:0; opacity:0;
                  background:linear-gradient(180deg,
                    rgba(252,249,230,.86) 0%, rgba(252,249,230,.80) 45%,
                    rgba(252,249,230,.92) 100%); }}

        /* Carton d'ouverture et de fin. */
        .carton {{ position:absolute; inset:0; display:flex; flex-direction:column;
                   align-items:center; justify-content:center; padding:0 200px; text-align:center; }}
        .cart-module {{ font-family:"Fredoka",sans-serif; font-weight:600; font-size:40px;
                        letter-spacing:.08em; text-transform:uppercase; color:{self.accent}; opacity:0; }}
        .cart-titre {{ font-family:"Fredoka",sans-serif; font-weight:700; font-size:104px;
                       line-height:1.1; color:{INK}; margin-top:34px; opacity:0; }}
        .cart-sous {{ font-family:"Inter",sans-serif; font-weight:500; font-size:44px;
                      color:{INK_SOFT}; margin-top:34px; opacity:0; }}
        .trait {{ width:200px; height:8px; border-radius:4px; background:{self.accent};
                  margin-top:52px; opacity:0; transform-origin:center; }}

        /* Le bloc de prompt : cadre sombre, texte clair — la seule surface
           foncée de la série, pour qu'on la reconnaisse d'un coup d'œil. */
        .prompt {{ position:absolute; left:180px; right:180px; top:220px; bottom:220px;
                   display:flex; flex-direction:column; justify-content:center;
                   background:{INK}; border-radius:34px; padding:56px 64px; opacity:0; }}
        .prompt-titre {{ font-family:"Fredoka",sans-serif; font-weight:600; font-size:34px;
                         letter-spacing:.06em; text-transform:uppercase; color:{ORANGE}; }}
        .prompt-texte {{ font-family:"Inter",sans-serif; font-weight:500; font-size:44px;
                         line-height:1.42; color:#F4F6F8; margin-top:30px; }}
        .prompt-outils {{ margin-top:40px; display:flex; flex-wrap:wrap; gap:16px; }}
        .outil {{ font-family:"Inter",sans-serif; font-weight:600; font-size:28px;
                  color:{CREAM}; background:rgba(255,255,255,.10); border-radius:999px;
                  padding:12px 24px; opacity:0; }}
        """

    # ── fond commun ────────────────────────────────────────────────────────
    def _bg_js(self, dur):
        """Halos qui respirent et trame qui dérive, sur toute la scène."""
        r = _repeat(9.0, dur)
        return (
            f'        tl.to("#glowA", {{ scale:1.06, duration:4.5, ease:"sine.inOut",'
            f' yoyo:true, repeat:{r} }}, 0);\n'
            f'        tl.to("#glowB", {{ scale:1.05, duration:5.2, ease:"sine.inOut",'
            f' yoyo:true, repeat:{_repeat(10.4, dur)} }}, 0);\n'
            f'        tl.to("#grid", {{ x:-48, y:-48, duration:6.0, ease:"none",'
            f' repeat:{_repeat(6.0, dur)} }}, 0);\n'
        )

    def _plaque(self, abs_debut, dur, plaque, vid_id):
        """Le plan réel derrière un carton, avec son voile.

        ⚠️ `data-duration` est en temps **absolu du film** — même piège que les
        scènes : une plaque déclarée sur sa seule durée locale s'éteindrait à
        l'instant `dur` du film, donc bien avant sa scène pour toute scène qui
        commence après. D'où `abs_debut + dur`.

        Le plan n'est pas coupé au montage : il est plus long que la scène,
        c'est la marge. Ce qu'on voit est son début, jamais sa fin — un plan
        généré finit souvent par une dérive de cadre qu'on ne veut pas montrer.
        """
        if not plaque:
            return "", ""
        # Une image fixe et un plan se déclarent pareil et s'animent pareil : le
        # lent zoom suffit à faire vivre une image, à condition qu'elle soit
        # assumée comme une image. Cinq sujets n'existent pas dans la
        # bibliothèque tournée — livreur, roue, connecteurs — et ce sont eux.
        balise = "img" if plaque.endswith((".jpg", ".png", ".webp")) else "video"
        attrs = "" if balise == "img" else " muted playsinline"
        html = (
            f'        <{balise} class="plaque clip" id="{vid_id}"'
            f' src="assets/plates/{plaque}"{attrs} data-start="0"'
            f' data-duration="{float(abs_debut) + float(dur):.2f}"'
            f' data-track-index="2"></{balise}>\n'
            '        <div class="voile" id="voile"></div>\n'
        )
        js = (
            f'        tl.fromTo("#{vid_id}", {{ opacity:0, scale:1.06 }},'
            f' {{ opacity:1, scale:1, duration:1.1, ease:"power2.out" }}, 0);\n'
            # Le lent zoom ne démarre qu'après l'entrée : deux tweens qui
            # portent `scale` en même temps, et le second gagne sans prévenir.
            f'        tl.to("#{vid_id}", {{ scale:1.04, duration:{max(0.5, float(dur) - 1.1):.2f},'
            f' ease:"none" }}, 1.1);\n'
            '        tl.fromTo("#voile", { opacity:0 }, { opacity:1, duration:.8, ease:"power2.out" }, .15);\n'
        )
        return html, js

    def intro(self, cid, abs_debut, dur, image):
        """Le carton d'intro officiel de la série, plein cadre.

        **Il remplace le carton fabriqué, il ne s'y ajoute pas.** Ces images
        viennent du Drive : logo, photo du fondateur, titre du tutoriel, appel
        à l'action. C'est ce qu'ouvrent les cent cinquante-sept tutoriels déjà
        publiés, et c'est aussi leur vignette sur le site. Poser mon carton
        derrière ou devant ferait deux titres d'affilée.

        Pas de voile ici, contrairement aux plaques : l'image est composée pour
        être lue telle quelle, et rien n'est écrit par-dessus. Le lent zoom est
        la seule liberté prise — une image parfaitement immobile pendant sept
        secondes se lit comme une vidéo bloquée.
        """
        body = (
            f'        <img class="plaque clip" id="vid-intro" src="assets/plates/{image}"'
            f' data-start="0" data-duration="{float(abs_debut) + float(dur):.2f}"'
            ' data-track-index="2"></img>\n'
        )
        js = (
            '        tl.fromTo("#vid-intro", { opacity:0 }, { opacity:1, duration:.5, ease:"power2.out" }, 0);\n'
            f'        tl.to("#vid-intro", {{ scale:1.035, duration:{max(0.5, float(dur) - 0.5):.2f},'
            ' ease:"none" }, .5);\n'
        )
        return _TEMPLATE.format(style=self.style, cid=cid, dur=f"{abs_debut + dur:.2f}", body=body, js=js)

    # ── carton d'ouverture ─────────────────────────────────────────────────
    def ouverture(self, cid, abs_debut, dur, titre, intention, plaque=None):
        p_html, p_js = self._plaque(abs_debut, dur, plaque, "vid-ouv")
        body = (
            _BG_HTML
            + p_html
            + '        <div class="carton">\n'
            + f'          <div class="cart-module" id="mod">{_echapper(NOMS_MODULES[self.module])}</div>\n'
            + f'          <div class="cart-titre" id="ti">{_echapper(titre)}</div>\n'
            + '          <div class="trait" id="tr"></div>\n'
            + f'          <div class="cart-sous" id="su">{_echapper(intention)}</div>\n'
            + '        </div>\n'
        )
        js = (
            self._bg_js(dur)
            + p_js
            + '        tl.fromTo("#mod", { opacity:0, y:-16 }, { opacity:1, y:0, duration:.5, ease:"power2.out" }, .15);\n'
            + '        tl.fromTo("#ti", { opacity:0, y:26 }, { opacity:1, y:0, duration:.6, ease:"power3.out" }, .45);\n'
            + '        tl.fromTo("#tr", { opacity:0, scaleX:0 }, { opacity:1, scaleX:1, duration:.5, ease:"power2.out" }, .95);\n'
            + '        tl.fromTo("#su", { opacity:0, y:18 }, { opacity:1, y:0, duration:.5, ease:"power2.out" }, 1.2);\n'
        )
        return _TEMPLATE.format(style=self.style, cid=cid, dur=f"{abs_debut + dur:.2f}", body=body, js=js)

    # ── planche d'étape ────────────────────────────────────────────────────
    def planche(self, cid, abs_debut, dur, surtitre, rang, total, phrase, jalons, actif):
        """Une étape : sa phrase, et la frise des jalons dont un seul est allumé.

        La frise est le seul repère de progression du film. Sans elle, sept
        planches successives se ressemblent et on perd le compte — on ne sait
        plus si le geste montré est le deuxième ou l'avant-dernier.
        """
        chips = "".join(
            f'          <div class="jalon{" on" if i == actif else ""}" id="jl{i}">{_echapper(j)}</div>\n'
            for i, j in enumerate(jalons)
        )
        body = (
            _BG_HTML
            + f'        <div class="eyebrow" id="eb">{_echapper(surtitre)}</div>\n'
            + f'        <div class="etape" id="et">{rang} / {total}</div>\n'
            + f'        <div class="board" id="bd"><div class="phrase">{phrase}</div></div>\n'
            + f'        <div class="jalons">\n{chips}        </div>\n'
        )
        js = (
            self._bg_js(dur)
            + '        tl.fromTo("#eb", { opacity:0, y:-12 }, { opacity:1, y:0, duration:.4, ease:"power2.out" }, .05);\n'
            + '        tl.fromTo("#et", { opacity:0 }, { opacity:.9, duration:.4 }, .12);\n'
            + '        tl.fromTo("#bd", { opacity:0, y:22 }, { opacity:1, y:0, duration:.45, ease:"power3.out" }, .22);\n'
        )
        for i in range(len(jalons)):
            js += (
                f'        tl.fromTo("#jl{i}", {{ opacity:0, y:16 }},'
                f' {{ opacity:{"1" if i == actif else ".45"}, y:0, duration:.3,'
                f' ease:"back.out(1.7)" }}, {0.55 + i * 0.12:.2f});\n'
            )
        # Le jalon actif respire : c'est ce qui distingue la frise d'une image.
        js += (
            f'        tl.to("#jl{actif}", {{ scale:1.04, duration:1.6, ease:"sine.inOut",'
            f' yoyo:true, repeat:{_repeat(3.2, dur)} }}, 1.1);\n'
        )
        return _TEMPLATE.format(style=self.style, cid=cid, dur=f"{abs_debut + dur:.2f}", body=body, js=js)

    # ── planche « avec Claude » ────────────────────────────────────────────
    def prompt(self, cid, abs_debut, dur, texte, outils):
        chips = "".join(
            f'          <div class="outil" id="ou{i}">{_echapper(o)}</div>\n'
            for i, o in enumerate(outils)
        )
        body = (
            _BG_HTML
            + '        <div class="eyebrow" id="eb">Avec Claude</div>\n'
            + '        <div class="prompt" id="pr">\n'
            + '          <div class="prompt-titre">Copiez ce prompt</div>\n'
            + f'          <div class="prompt-texte">{_echapper(texte)}</div>\n'
            + f'          <div class="prompt-outils">\n{chips}          </div>\n'
            + '        </div>\n'
        )
        js = (
            self._bg_js(dur)
            + '        tl.fromTo("#eb", { opacity:0, y:-12 }, { opacity:1, y:0, duration:.4, ease:"power2.out" }, .05);\n'
            + '        tl.fromTo("#pr", { opacity:0, y:26 }, { opacity:1, y:0, duration:.5, ease:"power3.out" }, .2);\n'
        )
        for i in range(len(outils)):
            js += (
                f'        tl.fromTo("#ou{i}", {{ opacity:0, scale:.85 }},'
                f' {{ opacity:1, scale:1, duration:.28, ease:"back.out(2)" }}, {0.9 + i * 0.22:.2f});\n'
            )
        return _TEMPLATE.format(style=self.style, cid=cid, dur=f"{abs_debut + dur:.2f}", body=body, js=js)

    # ── carton de fin ──────────────────────────────────────────────────────
    def cloture(self, cid, abs_debut, dur, plaque=None):
        p_html, p_js = self._plaque(abs_debut, dur, plaque, "vid-fin")
        body = (
            _BG_HTML
            + p_html
            + '        <div class="carton">\n'
            + '          <div class="cart-module" id="mod">Académie FoodEatUp</div>\n'
            + '          <div class="cart-titre" id="ti">Passez à la restauration intelligente</div>\n'
            + '          <div class="trait" id="tr"></div>\n'
            + '          <div class="cart-sous" id="su">Essayez gratuitement dès aujourd\'hui</div>\n'
            + '        </div>\n'
        )
        js = (
            self._bg_js(dur)
            + p_js
            + '        tl.fromTo("#mod", { opacity:0, y:-16 }, { opacity:1, y:0, duration:.45, ease:"power2.out" }, .1);\n'
            + '        tl.fromTo("#ti", { opacity:0, y:24 }, { opacity:1, y:0, duration:.55, ease:"power3.out" }, .35);\n'
            + '        tl.fromTo("#tr", { opacity:0, scaleX:0 }, { opacity:1, scaleX:1, duration:.45, ease:"power2.out" }, .8);\n'
            + '        tl.fromTo("#su", { opacity:0, y:16 }, { opacity:1, y:0, duration:.45, ease:"power2.out" }, 1.0);\n'
        )
        return _TEMPLATE.format(style=self.style, cid=cid, dur=f"{abs_debut + dur:.2f}", body=body, js=js)

    def ecrire(self, scenes):
        self.out.mkdir(parents=True, exist_ok=True)
        for nom, html in scenes.items():
            (self.out / nom).write_text(html, encoding="utf-8")
        print(f"  {self.sous} : {len(scenes)} scènes")
