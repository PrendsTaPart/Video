#!/usr/bin/env python3
"""Grammaire commune des 9 films « Une journée avec FoodEatUp ».

HyperFrames jette le `<head>` des sous-compositions : le bloc de style doit
être répété intégralement dans chacune. Le recopier à la main dans 9 films de
8 scènes, ce sont 72 occasions de laisser diverger la charte. Il vit donc ici,
et chaque film n'écrit que sa table de scènes.

Usage, depuis le dossier d'un film :

    import sys, pathlib
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "_serie"))
    from serie import Serie

    s = Serie(metier=Serie.CUISINE, sous="c2")
    s.ecrire({
        # (identifiant, début dans le film, durée de la scène, …)
        "c2-s1-midi.html": s.carton(
            "c2-s1-midi", "0.00", "7.48", "cloche", "vid-plate-cloche",
            "Midi", "Les premières commandes tombent"),
        "c2-s2-postes.html": s.ecran(
            "c2-s2-postes", "7.48", "12.84", "12:10", "CHAQUE POSTE, SON ÉCRAN",
            "SCENE-2", "vid-scene-2", ["Chaud", "Pass", "Froid"]),
    })

Les HTML produits sont versionnés : HyperFrames les lit, pas ce module. Le
régénérer ne doit jamais être nécessaire pour rendre un film.

Trois pièges sont inscrits ici, chacun payé une fois :

1. GSAP réécrit *tout* le `transform` dès qu'il anime `scale` ou `x`. Rien
   qui doive survivre à un tween ne peut vivre en CSS — ni le centrage du
   cadre (posé en absolu), ni l'inclinaison du balayage (portée par le tween).
2. `repeat: -1` déclenche un avertissement de troncature. Les boucles de fond
   ont donc un compte fini, calculé sur la durée de la scène.
3. **Un clip imbriqué déclare sa durée en temps ABSOLU du film, pas en temps
   local de sa scène.** Mesuré au centième sur quatre rendus : un clip de
   `data-duration = D`, posé dans une scène qui commence à `A`, s'éteint à
   l'instant `D` **du film**. La fenêtre se comporte comme `[A, D]` au lieu
   de `[A, A + D]`. Quand `D <= A` elle est vide, et le clip reste alors
   visible tout du long — ce qui masque le défaut partout sauf sur les
   scènes qui commencent tôt, les seules où `D > A`.

   D'où `abs_debut` : chaque scène reçoit son instant de début dans le film
   et déclare `data-duration = abs_debut + duree`. Le fichier, lui, n'a
   besoin de couvrir que la durée de la scène — le contenu est bien
   échantillonné en temps local, seule la fenêtre est absolue.
"""

import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]

# Charte du site Academy (src/styles.css), convertie depuis oklch.
# Voir NOTES.md §5 bis.1 : les films et le site partagent une seule palette.
CREAM = "#FCF9E6"
CREAM_DEEP = "#F5F0D4"
INK = "#0F1A23"
INK_SOFT = "#4C5760"
BLUE = "#007BFF"
ORANGE = "#FFA500"
BORDER = "#E1DDC7"

# Le cadre occupe 1560 px sur 1920 (81 %). Les bobines sont encodées en
# 1560x546, donc aucune mise à l'échelle au rendu.
FRAME_W, FRAME_H = 1560, 546
FRAME_X = (1920 - FRAME_W) // 2
FRAME_Y = 226

_TEMPLATE = """<!doctype html>
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

_BG_HTML = """        <div class="glow glow-a" id="glowA"></div>
        <div class="glow glow-b" id="glowB"></div>
        <div class="glow glow-c" id="glowC"></div>
        <div class="grid" id="grid"></div>
"""

_VEILLE_HTML = """            <div class="veille"></div>
            <div class="veille-scan" id="scan"></div>
"""


def _repeat(cycle, dur):
    """Répétitions couvrant tout juste la scène.

    On évite `repeat: -1` : HyperFrames avertit qu'une boucle infinie est
    tronquée à la fenêtre déclarée. Le comportement obtenu serait le même,
    mais un compte fini rend le rendu explicitement déterministe et garde le
    lint lisible — donc utile quand un vrai problème apparaîtra.
    """
    return max(0, math.ceil(float(dur) / cycle))


class Serie:
    """Un film de la série. Une instance par film."""

    CUISINE = "#059669"
    SALLE = "#F59E0B"
    DIRECTION = "#475569"

    def __init__(self, metier, sous):
        self.metier = metier
        self.sous = sous  # "c1", "c2", … : sous-dossier des médias et des HTML
        self.out = ROOT / "studio-video" / "compositions" / sous

    # ── style ────────────────────────────────────────────────────────────
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

        /* Fond à la charte du site : le crème, plus les deux dégradés du
           hero-glow (bleu en haut à gauche, orange en haut à droite). Ils
           sont animés — un aplat immobile pendant 75 s se lit comme une
           image figée. */
        .glow {{ position:absolute; border-radius:50%; filter:blur(10px); }}
        .glow-a {{ left:-360px; top:-420px; width:1500px; height:820px;
                   background:radial-gradient(closest-side, rgba(0,123,255,.16), rgba(0,123,255,0) 70%); }}
        .glow-b {{ right:-420px; top:-360px; width:1400px; height:760px;
                   background:radial-gradient(closest-side, rgba(255,165,0,.22), rgba(255,165,0,0) 70%); }}
        .glow-c {{ left:34%; bottom:-560px; width:1300px; height:900px;
                   background:radial-gradient(closest-side, {self._metier_rgba(.10)}, {self._metier_rgba(0)} 70%); }}

        /* Trame de points, reprise du motif de conversation du site. Elle
           donne au fond une texture qui bouge sans jamais attirer l'œil. */
        .grid {{ position:absolute; left:-160px; top:-160px; width:2280px; height:1420px;
                 background-image:radial-gradient(circle at 1px 1px, {BORDER} 0 2px, transparent 2px);
                 background-size:48px 48px; opacity:.55; }}

        /* Liseré métier en haut de cadre — signature de la série. */
        .metier {{ position:absolute; top:0; left:0; right:0; height:5px; background:{self.metier}; }}

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


        /* --- Scènes « motion design » -------------------------------------
           Pour les étapes qui n'ont aucun tutoriel filmé. Volontairement
           schématiques : jamais une fausse capture d'écran. La règle du
           projet interdit d'inventer une interface, donc on explique le
           mécanisme au lieu de le mettre en scène. */
        .board {{ position:absolute; left:180px; top:{FRAME_Y}px;
                  width:{FRAME_W}px; height:{FRAME_H}px; opacity:0; }}
        .md-card {{ position:absolute; left:50%; top:96px; width:520px; margin-left:-260px;
                    background:#FFFFFF; border:3px solid {BORDER}; border-radius:20px;
                    padding:26px 30px; box-shadow:0 18px 44px rgba(15,26,35,.12); }}
        .md-card .nom {{ font-family:"Fredoka",sans-serif; font-weight:700; font-size:38px; color:{INK}; }}
        .md-card .prix {{ font-family:"Fredoka",sans-serif; font-weight:600; font-size:30px; color:{INK_SOFT}; margin-top:6px; }}
        .md-barre {{ position:absolute; left:30px; right:30px; top:56px; height:5px;
                     background:#C64B3A; transform-origin:left center; transform:scaleX(0); }}
        .md-canal {{ position:absolute; top:392px; width:400px; text-align:center;
                     background:#FFFFFF; border:3px solid {BORDER}; border-radius:16px;
                     padding:18px 0; font-family:"Fredoka",sans-serif; font-weight:700;
                     font-size:30px; color:{INK}; opacity:0; }}
        .md-canal .etat {{ display:block; font-size:24px; font-weight:600; color:{INK_SOFT}; margin-top:6px; }}
        .md-lien {{ position:absolute; top:250px; height:4px; background:{BORDER};
                    transform-origin:left center; transform:scaleX(0); }}
        .md-tiroir {{ position:absolute; left:50%; margin-left:-330px; top:150px;
                      width:660px; height:230px; border:5px solid {INK}; border-radius:18px;
                      background:#FFFFFF; overflow:hidden; }}
        .md-tiroir-face {{ position:absolute; left:0; right:0; bottom:0; height:96px;
                           background:{CREAM_DEEP}; border-top:5px solid {INK}; }}
        .md-montant {{ position:absolute; left:0; right:0; top:60px; text-align:center;
                       font-family:"Fredoka",sans-serif; font-weight:700; font-size:76px; color:{INK}; }}

        .md-note {{ position:absolute; left:50%; margin-left:-250px; top:40px; width:500px;
                    background:#FFFFFF; border:3px solid {BORDER}; border-radius:18px;
                    padding:22px 26px; box-shadow:0 18px 44px rgba(15,26,35,.12); }}
        .md-note .entete {{ font-family:"Fredoka",sans-serif; font-weight:700; font-size:30px;
                            color:{INK}; border-bottom:2px solid {BORDER}; padding-bottom:12px; }}
        .md-note .ligne {{ display:flex; justify-content:space-between; margin-top:14px;
                           font-family:"Fredoka",sans-serif; font-weight:600; font-size:26px; color:{INK_SOFT}; }}
        .md-note .total {{ display:flex; justify-content:space-between; margin-top:18px;
                           padding-top:14px; border-top:2px solid {BORDER};
                           font-family:"Fredoka",sans-serif; font-weight:700; font-size:34px; color:{INK}; }}
        .md-part {{ position:absolute; top:150px; width:300px; background:#FFFFFF;
                    border:3px solid {BORDER}; border-radius:16px; padding:18px 0; text-align:center;
                    font-family:"Fredoka",sans-serif; font-weight:700; font-size:34px; color:{INK};
                    opacity:0; box-shadow:0 14px 34px rgba(15,26,35,.10); }}
        .md-part span {{ display:block; font-size:22px; font-weight:600; color:{INK_SOFT}; margin-top:4px; }}
        .md-remise {{ position:absolute; left:50%; margin-left:-130px; top:400px; width:260px;
                      background:{ORANGE}; color:{INK}; border-radius:999px; padding:14px 0;
                      text-align:center; font-family:"Fredoka",sans-serif; font-weight:700;
                      font-size:32px; opacity:0; box-shadow:0 10px 26px rgba(255,165,0,.3); }}
        .md-colonne {{ position:absolute; top:70px; width:420px; text-align:center;
                       background:#FFFFFF; border:3px solid {BORDER}; border-radius:18px;
                       padding:26px 0 30px; opacity:0;
                       box-shadow:0 16px 38px rgba(15,26,35,.10); }}
        .md-colonne .lib {{ font-family:"Fredoka",sans-serif; font-weight:600; font-size:28px;
                            color:{INK_SOFT}; }}
        .md-colonne .val {{ font-family:"Fredoka",sans-serif; font-weight:700; font-size:56px;
                            color:{INK}; margin-top:12px; }}
        .md-ecart {{ position:absolute; left:50%; margin-left:-230px; top:376px; width:460px;
                     text-align:center; background:{ORANGE}; color:{INK}; border-radius:999px;
                     padding:18px 0; font-family:"Fredoka",sans-serif; font-weight:700;
                     font-size:40px; opacity:0; box-shadow:0 12px 30px rgba(255,165,0,.3); }}
        .amb {{ position:absolute; inset:0; width:100%; height:100%; object-fit:cover; opacity:0; }}
        .title {{ position:absolute; left:0; right:0; bottom:132px; text-align:center;
                  font-family:"Fredoka",sans-serif; font-weight:700; font-size:76px; color:{CREAM};
                  text-shadow:0 6px 30px rgba(15,26,35,.6); opacity:0; }}
        .sub {{ position:absolute; left:0; right:0; bottom:74px; text-align:center;
                font-family:"Fredoka",sans-serif; font-weight:600; font-size:34px; color:{CREAM};
                text-shadow:0 2px 16px rgba(15,26,35,.65); opacity:0; }}
"""

    def _metier_rgba(self, alpha):
        h = self.metier.lstrip("#")
        r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
        return f"rgba({r},{g},{b},{alpha})"

    # ── animation de fond ────────────────────────────────────────────────
    def _bg_js(self, dur):
        """Les dégradés dérivent et respirent, la trame glisse.

        Ces mouvements sont dans la timeline (et non en @keyframes CSS) pour
        que le rendu reste déterministe image par image quand HyperFrames se
        déplace dans le temps.
        """
        return (
            "\n        // Fond vivant : les dégradés dérivent et respirent, la trame glisse.\n"
            f'        tl.to("#glowA", {{ x:70, y:38, scale:1.10, duration:11, ease:"sine.inOut", yoyo:true, repeat:{_repeat(11, dur)} }}, 0);\n'
            f'        tl.to("#glowB", {{ x:-56, y:44, scale:1.14, duration:9, ease:"sine.inOut", yoyo:true, repeat:{_repeat(9, dur)} }}, 0);\n'
            f'        tl.to("#glowC", {{ x:48, scale:1.08, duration:13, ease:"sine.inOut", yoyo:true, repeat:{_repeat(13, dur)} }}, 0);\n'
            f'        tl.to("#grid", {{ x:-48, y:-48, duration:16, ease:"none", repeat:{_repeat(16, dur)} }}, 0);\n'
        )

    @staticmethod
    def _veille_js(dur):
        return (
            '        tl.fromTo("#scan", { x:0, skewX:-12 },'
            f' {{ x:4300, skewX:-12, duration:3.4, ease:"none", repeat:{_repeat(3.4, dur)} }}, 0);\n'
        )

    # ── scènes ───────────────────────────────────────────────────────────
    def ecran(self, cid, abs_debut, dur, clock, eyebrow, reel, vid_id, checks):
        """Scène « écran » : horloge, surtitre, bobine dans le cadre, coches.

        `abs_debut` est l'instant où la scène commence dans le film. La durée
        déclarée du clip vaut `abs_debut + dur` : la fenêtre de visibilité est
        lue en temps absolu (voir le piège 3 en tête de module).
        """
        chips = "".join(
            f'          <div class="check" id="ck{i}"><span>✓</span>{t}</div>\n'
            for i, t in enumerate(checks)
        )
        body = (
            _BG_HTML
            + f'        <div class="clock" id="clock">{clock}</div>\n'
            + f'        <div class="eyebrow" id="eyebrow">{eyebrow}</div>\n'
            + '        <div class="frame" id="frame">\n'
            + _VEILLE_HTML
            + f'          <video id="{vid_id}" src="assets/screens/{self.sous}/{reel}.mp4"'
            f' muted playsinline class="clip" data-start="0"'
            f' data-duration="{float(abs_debut) + float(dur):.2f}"'
            ' data-track-index="2"></video>\n'
            + "        </div>\n"
            + f'        <div class="checks">\n{chips}        </div>\n'
        )
        js = (
            self._bg_js(dur)
            + self._veille_js(dur)
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
        return _TEMPLATE.format(style=self.style, cid=cid, dur=dur, body=body, js=js)

    def carton(self, cid, abs_debut, dur, plate, vid_id, title, sub,
               amb_opacity=1, title_at=".9", sub_at="1.5"):
        """Scène « carton » : plan tourné plein cadre, titre, sous-titre."""
        body = (
            _BG_HTML
            + f'        <video class="amb clip" id="{vid_id}" src="assets/plates/{self.sous}/{plate}.mp4"'
            f' muted playsinline data-start="0"'
            f' data-duration="{float(abs_debut) + float(dur):.2f}"'
            ' data-track-index="2"></video>\n'
            + f'        <div class="title" id="title">{title}</div>\n'
            + f'        <div class="sub" id="sub">{sub}</div>\n'
        )
        # Le lent zoom avant ne démarre qu'après l'entrée de l'image : les deux
        # tweens porteraient sinon `scale` en même temps, et le second gagnerait.
        js = (
            self._bg_js(dur)
            + f'        tl.fromTo("#{vid_id}", {{ opacity:0, scale:1.06 }}, {{ opacity:{amb_opacity}, scale:1, duration:1.2, ease:"power2.out" }}, 0);\n'
            + f'        tl.to("#{vid_id}", {{ scale:1.045, duration:{max(0.5, float(dur) - 1.2):.2f}, ease:"none" }}, 1.2);\n'
            + f'        tl.fromTo("#title", {{ opacity:0, y:24 }}, {{ opacity:1, y:0, duration:.6, ease:"power2.out" }}, {title_at});\n'
            + f'        tl.fromTo("#sub", {{ opacity:0, y:14 }}, {{ opacity:.92, y:0, duration:.5, ease:"power2.out" }}, {sub_at});\n'
        )
        return _TEMPLATE.format(style=self.style, cid=cid, dur=dur, body=body, js=js)


    # ── scènes « motion design » ─────────────────────────────────────────
    def motion(self, cid, abs_debut, dur, clock, eyebrow, board_html, board_js, checks):
        """Ossature commune aux scènes schématiques.

        Publique : un schéma qui ne sert qu'à un seul film n'a rien à faire
        dans la grammaire commune, il s'écrit dans le build de ce film et
        passe son HTML et son JS ici.

        Même en-tête que les scènes écran — horloge, surtitre, coches — mais
        le cadre tablette est remplacé par un tableau schématique. Aucune
        vidéo, donc aucun `data-duration` absolu à gérer ici.
        """
        chips = "".join(
            f'          <div class="check" id="ck{i}"><span>✓</span>{t}</div>\n'
            for i, t in enumerate(checks)
        )
        body = (
            _BG_HTML
            + f'        <div class="clock" id="clock">{clock}</div>\n'
            + f'        <div class="eyebrow" id="eyebrow">{eyebrow}</div>\n'
            + f'        <div class="board" id="board">\n{board_html}        </div>\n'
            + f'        <div class="checks">\n{chips}        </div>\n'
        )
        js = (
            self._bg_js(dur)
            + '        tl.fromTo("#clock", { opacity:0, y:-12 }, { opacity:1, y:0, duration:.4, ease:"power2.out" }, .05);\n'
            + '        tl.fromTo("#eyebrow", { opacity:0, y:-12 }, { opacity:.9, y:0, duration:.4, ease:"power2.out" }, .12);\n'
            + '        tl.fromTo("#board", { opacity:0, y:18 }, { opacity:1, y:0, duration:.35, ease:"power2.out" }, .3);\n'
            + board_js
        )
        for i in range(len(checks)):
            js += (
                f'        tl.fromTo("#ck{i}", {{ opacity:0, scale:.8, y:14 }},'
                f' {{ opacity:1, scale:1, y:0, duration:.24, ease:"back.out(2)" }}, {1.75 + i * .28:.2f});\n'
            )
        return _TEMPLATE.format(style=self.style, cid=cid, dur=dur, body=body, js=js)

    def motion_retrait_carte(self, cid, abs_debut, dur, clock, eyebrow, plat, prix, canaux):
        """« Je retire un plat : il disparaît de tous les canaux à la fois. »

        Le propos n'est pas l'écran, c'est la simultanéité. Le schéma la
        montre littéralement : un seul geste sur la fiche, et les trois
        canaux basculent ensemble.
        """
        n = len(canaux)
        ecart = 1560 // n
        html = ('          <div class="md-card" id="mdCard">\n'
                f'            <div class="nom">{plat}</div>\n'
                f'            <div class="prix">{prix}</div>\n'
                '            <div class="md-barre" id="mdBarre"></div>\n'
                '          </div>\n')
        for i, c in enumerate(canaux):
            gauche = i * ecart + (ecart - 400) // 2
            centre = gauche + 200
            largeur = abs(centre - 780) or 1
            x = min(centre, 780)
            html += (f'          <div class="md-lien" id="mdLien{i}" style="left:{x}px; width:{largeur}px;"></div>\n'
                     f'          <div class="md-canal" id="mdCanal{i}" style="left:{gauche}px;">{c}'
                     f'<span class="etat" id="mdEtat{i}">disponible</span></div>\n')
        js = ('        tl.fromTo("#mdCard", { opacity:0, scale:.94 }, { opacity:1, scale:1, duration:.3, ease:"back.out(1.5)" }, .45);\n')
        for i in range(n):
            js += (f'        tl.to("#mdLien{i}", {{ scaleX:1, duration:.3, ease:"power2.out" }}, {0.7 + i * .12:.2f});\n'
                   f'        tl.fromTo("#mdCanal{i}", {{ opacity:0, y:14 }}, {{ opacity:1, y:0, duration:.28, ease:"power2.out" }}, {0.85 + i * .12:.2f});\n')
        # Le geste, puis la bascule simultanée : c'est tout le sujet.
        js += '        tl.to("#mdBarre", { scaleX:1, duration:.35, ease:"power2.inOut" }, 2.0);\n'
        js += '        tl.to("#mdCard", { opacity:.4, duration:.4 }, 2.2);\n'
        for i in range(n):
            js += (f'        tl.to("#mdEtat{i}", {{ opacity:0, duration:.15 }}, 2.45);\n'
                   f'        tl.set("#mdEtat{i}", {{ innerText:"retiré", color:"#C64B3A" }}, 2.6);\n'
                   f'        tl.to("#mdEtat{i}", {{ opacity:1, duration:.2 }}, 2.6);\n'
                   f'        tl.to("#mdCanal{i}", {{ borderColor:"#C64B3A", duration:.3 }}, 2.6);\n')
        return self.motion(cid, abs_debut, dur, clock, eyebrow, html, js, ["Un seul geste"] + [f"{c} à jour" for c in canaux[:2]])

    def motion_fond_caisse(self, cid, abs_debut, dur, clock, eyebrow, montant, checks):
        """« J'ouvre mon fond de caisse. » Un tiroir, un montant qui se pose."""
        html = ('          <div class="md-tiroir" id="mdTiroir">\n'
                f'            <div class="md-montant" id="mdMontant">0,00 €</div>\n'
                '            <div class="md-tiroir-face" id="mdFace"></div>\n'
                '          </div>\n')
        js = ('        tl.fromTo("#mdTiroir", { opacity:0, y:20 }, { opacity:1, y:0, duration:.35, ease:"back.out(1.4)" }, .45);\n'
              '        tl.fromTo("#mdFace", { y:0 }, { y:70, duration:.5, ease:"power2.out" }, .9);\n'
              # Le compteur est animé par un objet intermédiaire : GSAP ne sait
              # pas interpoler un texte, seulement un nombre.
              '        const compteur = { v: 0 };\n'
              f'        tl.to(compteur, {{ v:{montant}, duration:1.1, ease:"power2.out",\n'
              '          onUpdate: () => { document.getElementById("mdMontant").textContent =\n'
              '            compteur.v.toFixed(2).replace(".", ",") + " €"; } }, 1.1);\n')
        return self.motion(cid, abs_debut, dur, clock, eyebrow, html, js, checks)


    def motion_note(self, cid, abs_debut, dur, clock, eyebrow, table, lignes, total, parts, remise):
        """« J'encaisse, je sépare, j'applique la remise. » Une seule note.

        Les trois étapes du module Caisse POS sont réunies ici plutôt que
        d'occuper trois scènes de deux secondes : la voix les nomme dans la
        même respiration et c'est le même objet à l'écran.
        """
        html = '          <div class="md-note" id="mdNote">\n'
        html += f'            <div class="entete">{table}</div>\n'
        for i, (lib, px) in enumerate(lignes):
            html += f'            <div class="ligne" id="mdL{i}"><span>{lib}</span><span>{px}</span></div>\n'
        html += f'            <div class="total" id="mdTotal"><span>Total</span><span>{total}</span></div>\n'
        html += "          </div>\n"
        n = len(parts)
        ecart = 1560 // n
        for i, p in enumerate(parts):
            gauche = i * ecart + (ecart - 300) // 2
            html += (f'          <div class="md-part" id="mdPart{i}" style="left:{gauche}px;">{p}'
                     f'<span>part {i + 1}</span></div>\n')
        html += f'          <div class="md-remise" id="mdRemise">{remise}</div>\n'

        js = '        tl.fromTo("#mdNote", { opacity:0, y:16 }, { opacity:1, y:0, duration:.35, ease:"back.out(1.4)" }, .45);\n'
        for i in range(len(lignes)):
            js += f'        tl.fromTo("#mdL{i}", {{ opacity:0, x:-14 }}, {{ opacity:1, x:0, duration:.22 }}, {0.75 + i * .14:.2f});\n'
        js += '        tl.fromTo("#mdTotal", { opacity:0 }, { opacity:1, duration:.3 }, 1.3);\n'
        # La note se sépare : elle recule, les parts descendent d'elle.
        js += '        tl.to("#mdNote", { scale:.72, y:-70, duration:.5, ease:"power2.inOut" }, 3.4);\n'
        for i in range(n):
            js += (f'        tl.fromTo("#mdPart{i}", {{ opacity:0, y:-40, scale:.85 }},'
                   f' {{ opacity:1, y:0, scale:1, duration:.4, ease:"back.out(1.6)" }}, {3.7 + i * .16:.2f});\n')
        # Puis la remise, posée sur l'ensemble.
        js += '        tl.fromTo("#mdRemise", { opacity:0, scale:.7 }, { opacity:1, scale:1, duration:.35, ease:"back.out(2)" }, 5.9);\n'
        js += f'        tl.to("#mdPart{n - 1}", {{ borderColor:"{ORANGE}", duration:.3 }}, 6.1);\n'
        return self.motion(cid, abs_debut, dur, clock, eyebrow, html, js,
                            ["Encaissé", "Séparé", "Remise appliquée"])


    def motion_ecart(self, cid, abs_debut, dur, clock, eyebrow, colonnes, ecart, checks):
        """« Je compte mon tiroir. » Théorique, compté, et l'écart entre les deux.

        Le propos est que l'écart est *écrit*, pas qu'il est nul. Le schéma
        le pose donc en clair, en orange, plutôt que de le cacher.
        """
        n = len(colonnes)
        ecart_px = 1560 // n
        html = ""
        for i, (lib, val) in enumerate(colonnes):
            gauche = i * ecart_px + (ecart_px - 420) // 2
            html += (f'          <div class="md-colonne" id="mdCol{i}" style="left:{gauche}px;">\n'
                     f'            <div class="lib">{lib}</div>\n'
                     f'            <div class="val">{val}</div>\n'
                     '          </div>\n')
        html += f'          <div class="md-ecart" id="mdEcart">{ecart}</div>\n'
        js = ""
        for i in range(n):
            js += (f'        tl.fromTo("#mdCol{i}", {{ opacity:0, y:20 }},'
                   f' {{ opacity:1, y:0, duration:.35, ease:"back.out(1.5)" }}, {0.5 + i * .22:.2f});\n')
        js += ('        tl.fromTo("#mdEcart", { opacity:0, scale:.75 },'
               ' { opacity:1, scale:1, duration:.4, ease:"back.out(2)" }, 2.1);\n')
        return self.motion(cid, abs_debut, dur, clock, eyebrow, html, js, checks)

    # ── écriture ─────────────────────────────────────────────────────────
    def ecrire(self, scenes):
        self.out.mkdir(parents=True, exist_ok=True)
        for name, html in scenes.items():
            (self.out / name).write_text(html, encoding="utf-8")
            print("écrit", f"{self.sous}/{name}")
