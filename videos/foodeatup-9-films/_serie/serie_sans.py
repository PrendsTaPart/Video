#!/usr/bin/env python3
"""Grammaire des neuf films « Une journée SANS FoodEatUp ».

Films miroir des neuf films « avec ». Le raisonnement est dans NOTES §6 : une
journée « avec », seule, donne l'impression que le logiciel réclame quarante-six
gestes par jour. Le miroir montre que ces gestes existent de toute façon —
répartis dans sept outils qui ne se parlent pas, saisis deux fois, souvent
abandonnés.

⚠️ CONTRAINTE JURIDIQUE (NOTES §6.1) — à relire avant de toucher ce fichier.

Aucun concurrent ne doit être identifiable, ni explicitement ni implicitement
(art. L122-1 et L122-2 du Code de la consommation). Il suffit que le
spectateur reconnaisse un acteur pour que le film bascule en publicité
comparative, et le registre ironique ferait alors tomber le dénigrement.

Ce module n'incruste **jamais** de capture d'écran. Toutes les interfaces
« sans » sont des maquettes que nous dessinons ici, en gris `#8A9099`, en
typographie **système**, sans logo, sans nom de produit, sans palette
d'éditeur. Elles doivent évoquer « un logiciel quelconque », jamais un
logiciel précis. Le contournement est aussi la meilleure idée du volet :
**ne pas montrer des marques, montrer le nombre.**

Deux garde-fous restent dus avant diffusion : `no-competitor-check.ts` (liste
de marques à fournir par Michael) et une relecture par un avocat.

Trois pièges, hérités de `serie.py` et toujours actifs ici :

1. GSAP réécrit tout le `transform` dès qu'il anime `scale` ou `x`. Un
   `translate(-50%,-50%)` ou un `skewX` posé en CSS est alors perdu : il doit
   vivre dans le tween.

2. `repeat: -1` déclenche un avertissement de troncature. On calcule un
   nombre fini de répétitions à partir de la durée de la scène.

3. **La fenêtre d'un clip imbriqué se lit en temps ABSOLU**, pas en temps
   local à la scène : `data-duration="D"` sur un clip dont la scène commence
   en `A` donne la fenêtre `[A, D]` et non `[A, A+D]`.

   `serie.py` gère ce piège avec un décalage constant appliqué après coup par
   `ajouter-habillages.py`, ce qui a une fois éteint les cent-deux plans des
   neuf films d'un coup. Ici on ne répète pas cette construction : **le hook
   est une scène comme les autres, déclarée dès le départ**, et `abs_debut`
   est l'instant réel dans le film, hook compris. Aucun script ne décale
   quoi que ce soit après coup, donc rien ne peut se désynchroniser.
"""

import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]

# Palette du registre « sans » (NOTES §6.3). Aucune couleur de la charte
# FoodEatUp n'y figure — elles ne réapparaissent qu'au carton final, et cette
# réapparition est tout l'argument du film.
GRIS = "#8A9099"        # le gris des maquettes d'outils
ANTHRACITE = "#3A3F45"  # le texte
FROID = "#EDEEF0"        # le fond, un blanc sans chaleur
ALERTE = "#D64545"       # les croix, les manques
LIGNE = "#C7CBD1"        # les sept lignes brisées

# Le carton final, seul moment où la charte revient.
MARINE = "#1B2A41"
CREAM = "#FCF9E6"
BLUE = "#007BFF"
ORANGE = "#FFA500"

# Même cadre que la série « avec » : les deux volets se regardent l'un
# l'autre, un cadre différent casserait la comparaison.
FRAME_W, FRAME_H = 1560, 546
FRAME_X = (1920 - FRAME_W) // 2
FRAME_Y = 226

# Typographie système pour tout ce qui est censé appartenir à un outil tiers.
# C'est une exigence juridique, pas un choix graphique : une typographie
# reconnaissable d'éditeur suffirait à identifier un acteur.
SYS = ('ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, '
       'Helvetica, Arial, sans-serif')

_TEMPLATE = """<!doctype html>
<html>
  <head><meta charset="UTF-8" /></head>
  <body>
    <template>
      <style>{style}
      </style>

      <div id="root" data-composition-id="{cid}" data-width="1920" data-height="1080" data-duration="{dur}">
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


def _repeat(cycle, dur):
    """Répétitions couvrant tout juste la scène (cf. piège 2)."""
    return max(0, math.ceil(float(dur) / cycle))


# Les sept lignes brisées : le motif de fond du volet, en remplacement de la
# trame de points de la série « avec ». Elles ne se touchent jamais — c'est
# littéralement le propos, sept outils qui ne se parlent pas.
_FOND_HTML = "".join(
    f'        <div class="ligne l{i}"></div>\n' for i in range(7)
) + '        <div class="voile"></div>\n'

# Lignes de remplissage de la page du plan « sept onglets ». Elles n'écrivent
# rien : ce sont des barres grises, la moindre chaîne de caractères ici
# risquerait d'évoquer une interface réelle (NOTES §6.1).
_remplissage = "".join(
    f'            <div class="fausse-ligne"'
    f' style="left:{x}px; top:{y}px; width:{w}px;"></div>\n'
    for x, y, w in [(96, 268, 420), (96, 300, 300), (96, 332, 380),
                    (96, 364, 240), (1120, 268, 380), (1120, 300, 260),
                    (1120, 332, 340), (1120, 364, 200),
                    (620, 268, 180), (620, 300, 180), (620, 332, 180)]
)


class SerieSans:
    """Un film « sans ». Une instance par film."""

    CUISINE = "cuisine"
    SALLE = "salle"
    DIRECTION = "direction"

    LIEUX = {CUISINE: "en cuisine", SALLE: "en salle", DIRECTION: "au bureau"}
    PHASES = {"avant": "avant le service",
              "pendant": "pendant le service",
              "apres": "après le service"}

    def __init__(self, metier, sous):
        self.metier = metier
        self.sous = sous  # "c1s", "c2s", … : sous-dossier des médias et HTML
        self.out = ROOT / "studio-video" / "compositions" / sous

    # ── style ────────────────────────────────────────────────────────────
    @property
    def style(self):
        # Les sept lignes sont posées à des hauteurs et des longueurs
        # irrégulières : alignées, elles se liraient comme une grille, donc
        # comme un ordre. Le désordre est le sujet.
        lignes = "".join(
            f"        .l{i} {{ top:{y}px; left:{x}px; width:{w}px; }}\n"
            for i, (y, x, w) in enumerate([
                (118, -60, 520), (246, 640, 380), (372, 120, 300),
                (498, 980, 640), (624, 40, 460), (802, 700, 520),
                (946, 220, 340),
            ])
        )
        return f"""
        @font-face {{
          font-family: "Fredoka";
          src: url("assets/vendor/fonts/Fredoka-Variable.woff2") format("woff2-variations");
          font-weight: 300 700; font-display: block;
        }}
        #root {{ position:absolute; inset:0; background:{FROID}; overflow:hidden;
                 font-family:"Fredoka",sans-serif; }}

        /* Sept lignes grises brisées, qui ne se touchent jamais. Elles
           dérivent lentement et à des vitesses différentes : deux lignes qui
           avanceraient ensemble suggéreraient une coordination. */
        .ligne {{ position:absolute; height:3px; background:{LIGNE}; opacity:.9; }}
{lignes}
        /* Voile froid : casse le blanc pur, qui à l'écran vire au bleu. */
        .voile {{ position:absolute; inset:0;
                  background:linear-gradient(160deg, rgba(58,63,69,.05), rgba(58,63,69,0) 55%); }}

        .clock {{ position:absolute; top:44px; left:64px; font-family:"Fredoka",sans-serif;
                  font-weight:700; font-size:46px; color:{ANTHRACITE}; opacity:0; letter-spacing:.02em; }}
        .eyebrow {{ position:absolute; top:52px; left:340px; right:340px; text-align:center;
                    font-family:"Fredoka",sans-serif; font-weight:600; font-size:40px;
                    color:{GRIS}; opacity:0; }}

        /* --- Maquettes d'outils --------------------------------------------
           Tout ce qui suit est dessiné par nous. Aucune capture, aucun logo,
           aucune palette d'éditeur : typographie système, gris, angles droits.
           Voir la contrainte juridique en tête de module. */
        .board {{ position:absolute; left:{FRAME_X}px; top:{FRAME_Y}px;
                  width:{FRAME_W}px; height:{FRAME_H}px; opacity:0; }}

        .outil {{ position:absolute; top:0; background:#FFFFFF;
                  border:2px solid #D4D8DD; border-radius:8px; overflow:hidden;
                  box-shadow:0 12px 30px rgba(58,63,69,.10); opacity:0; }}
        .outil .barre {{ height:44px; background:{GRIS};
                         display:flex; align-items:center; padding:0 16px; gap:8px; }}
        .outil .pastille {{ width:11px; height:11px; border-radius:50%;
                            background:rgba(255,255,255,.55); }}
        .outil .nom {{ font-family:{SYS}; font-size:20px; font-weight:600;
                       color:#FFFFFF; margin-left:10px; letter-spacing:.01em; }}
        .outil .corps {{ padding:18px 16px; }}
        .outil .rang {{ height:12px; background:#E3E6EA; border-radius:2px; margin-bottom:12px; }}
        .outil .rang.court {{ width:58%; }}
        .outil .rang.moyen {{ width:78%; }}

        /* La croix rouge remplace la coche orange de la série « avec ». */
        .croix {{ position:absolute; font-family:"Fredoka",sans-serif; font-weight:700;
                  font-size:52px; color:{ALERTE}; opacity:0; }}

        .manques {{ position:absolute; left:0; right:0; top:{FRAME_Y + FRAME_H + 58}px;
                    display:flex; justify-content:center; align-items:center; gap:26px; }}
        .manque {{ display:flex; align-items:center; gap:12px; background:#FFFFFF;
                   border:2px solid {ALERTE}; color:{ANTHRACITE};
                   font-family:"Fredoka",sans-serif; font-weight:700; font-size:30px;
                   padding:13px 27px; border-radius:999px; opacity:0; white-space:nowrap; }}
        .manque span {{ color:{ALERTE}; font-size:34px; line-height:1; }}

        /* --- Le plan obligatoire : sept onglets, un chiffre recopié -------- */
        .tabs {{ position:absolute; left:0; right:0; top:0; height:56px;
                 display:flex; align-items:flex-end; padding-left:14px; gap:4px;
                 background:#DDE1E6; }}
        .tab {{ height:42px; width:200px; background:#C9CED4; border-radius:8px 8px 0 0;
                display:flex; align-items:center; justify-content:center;
                font-family:{SYS}; font-size:17px; color:#5D646C; }}
        .tab.actif {{ background:#FFFFFF; color:{ANTHRACITE}; height:48px; }}
        .page {{ position:absolute; left:0; right:0; top:56px; bottom:0; background:#FFFFFF; }}
        .champ {{ position:absolute; width:300px; height:64px; border:2px solid #C9CED4;
                  border-radius:4px; background:#FFFFFF;
                  font-family:{SYS}; font-size:34px; color:{ANTHRACITE};
                  display:flex; align-items:center; justify-content:center; }}
        .champ.vide {{ color:#B7BCC2; }}
        .champ-lib {{ position:absolute; font-family:{SYS}; font-size:22px;
                      color:#7A8189; }}
        /* Matière de la page. Sans elle le plan avait un ventre blanc de
           400 px, et la règle de la série veut qu'aucun plan ne finisse sur
           du vide (NOTES §5 bis). */
        .fausse-ligne {{ position:absolute; height:11px; background:#E9ECEF;
                         border-radius:2px; }}
        /* Curseur dessiné en SVG et non en bordures CSS : le triangle obtenu
           par bordures mesurait vingt pixels et se lisait comme une tache sur
           le chiffre qu'il désigne. */
        .curseur {{ position:absolute; width:42px; height:46px;
                    filter:drop-shadow(0 3px 5px rgba(0,0,0,.32)); }}
        .porte {{ position:absolute; font-family:{SYS}; font-size:30px; font-weight:700;
                  color:{ANTHRACITE}; background:#FFF6C2; border:2px solid #E4D68A;
                  border-radius:4px; padding:6px 14px; opacity:0; white-space:nowrap; }}

        /* --- Cartons, refrain, compteur ------------------------------------ */
        .amb {{ position:absolute; inset:0; width:100%; height:100%; object-fit:cover; opacity:0; }}
        .assombri {{ position:absolute; inset:0; background:rgba(27,32,37,.34); opacity:0; }}
        .title {{ position:absolute; left:0; right:0; bottom:132px; text-align:center;
                  font-family:"Fredoka",sans-serif; font-weight:700; font-size:76px; color:#F4F5F7;
                  text-shadow:0 6px 30px rgba(20,24,28,.75); opacity:0; }}
        .sub {{ position:absolute; left:0; right:0; bottom:74px; text-align:center;
                font-family:"Fredoka",sans-serif; font-weight:600; font-size:34px; color:#DCDEE2;
                text-shadow:0 2px 16px rgba(20,24,28,.8); opacity:0; }}

        .refrain {{ position:absolute; left:150px; right:150px; top:380px; text-align:center;
                    font-family:"Fredoka",sans-serif; font-weight:700; font-size:78px;
                    color:{ANTHRACITE}; opacity:0; line-height:1.22; }}
        .refrain-b {{ position:absolute; left:150px; right:150px; top:640px; text-align:center;
                      font-family:"Fredoka",sans-serif; font-weight:600; font-size:46px;
                      color:{GRIS}; opacity:0; }}

        .compteur {{ position:absolute; left:0; right:0; top:400px;
                     display:flex; justify-content:center; gap:40px; }}
        .compteur .bloc {{ width:400px; text-align:center; background:#FFFFFF;
                           border:2px solid #D4D8DD; border-radius:12px; padding:30px 0 34px;
                           opacity:0; }}
        /* `nowrap` n'est pas cosmétique : « 350 à 900 € » cassait en deux
           lignes et le libellé passait sous le bloc. La taille est réduite en
           Python selon la longueur de la valeur, pas ici. */
        .compteur .val {{ font-family:"Fredoka",sans-serif; font-weight:700; font-size:78px;
                          color:{ALERTE}; white-space:nowrap; line-height:1.05; }}
        .compteur .lib {{ font-family:"Fredoka",sans-serif; font-weight:600; font-size:30px;
                          color:{GRIS}; margin-top:8px; }}

        /* --- Hook d'ouverture ---------------------------------------------- */
        .hk-sur {{ position:absolute; left:0; right:0; top:296px; text-align:center;
                   font-family:"Fredoka",sans-serif; font-weight:600; font-size:48px;
                   color:{GRIS}; opacity:0; letter-spacing:.04em; }}
        .hk-titre {{ position:absolute; left:0; right:0; top:376px; text-align:center;
                     font-family:"Fredoka",sans-serif; font-weight:700; font-size:112px;
                     color:{ANTHRACITE}; opacity:0; }}
        .hk-titre em {{ font-style:normal; color:{ALERTE}; }}
        .hk-phase {{ position:absolute; left:0; right:0; top:552px; text-align:center;
                     font-family:"Fredoka",sans-serif; font-weight:600; font-size:52px;
                     color:{ANTHRACITE}; opacity:0; }}
        .hk-lieu {{ position:absolute; left:0; right:0; top:632px; text-align:center;
                    font-family:"Fredoka",sans-serif; font-weight:600; font-size:40px;
                    color:{GRIS}; opacity:0; }}
        .hk-barre {{ position:absolute; left:50%; margin-left:-90px; top:724px;
                     width:180px; height:6px; border-radius:3px; background:{ALERTE};
                     transform-origin:center; transform:scaleX(0); }}

        /* --- Punchline : la charte revient ---------------------------------
           Seul plan du film qui porte les couleurs FoodEatUp. La bascule est
           l'argument : elle doit être franche, pas fondue. */
        .pl-fond {{ position:absolute; inset:0; background:{MARINE}; opacity:0; }}
        .pl-lueur-a {{ position:absolute; left:-320px; top:-380px; width:1400px; height:800px;
                       border-radius:50%; filter:blur(10px); opacity:0;
                       background:radial-gradient(closest-side, rgba(0,123,255,.30), rgba(0,123,255,0) 70%); }}
        .pl-lueur-b {{ position:absolute; right:-380px; bottom:-420px; width:1300px; height:820px;
                       border-radius:50%; filter:blur(10px); opacity:0;
                       background:radial-gradient(closest-side, rgba(255,165,0,.26), rgba(255,165,0,0) 70%); }}
        .pl-photo {{ position:absolute; right:30px; bottom:0; height:880px; opacity:0; }}
        .pl-logo {{ position:absolute; left:140px; top:236px; width:620px; opacity:0; }}
        .pl-une {{ position:absolute; left:140px; top:432px; width:1020px;
                   font-family:"Fredoka",sans-serif; font-weight:700; font-size:62px;
                   color:{CREAM}; opacity:0; line-height:1.2; }}
        .pl-deux {{ position:absolute; left:140px; top:596px; width:980px;
                    font-family:"Fredoka",sans-serif; font-weight:600; font-size:38px;
                    color:#D9DEE6; opacity:0; line-height:1.36; }}
        .pl-barre {{ position:absolute; left:140px; top:744px; width:180px; height:6px;
                     border-radius:3px; background:{ORANGE};
                     transform-origin:left center; transform:scaleX(0); }}
"""

    # ── fond ─────────────────────────────────────────────────────────────
    def _fond_js(self, dur):
        """Les sept lignes dérivent, chacune à sa vitesse.

        Les mouvements sont dans la timeline et non en `@keyframes` CSS :
        HyperFrames se déplace image par image dans le temps, et seule une
        timeline reste déterministe sous ce traitement.
        """
        vitesses = [17, 13, 21, 11, 19, 15, 23]
        js = "\n        // Sept lignes qui dérivent séparément — rien n'est synchronisé.\n"
        for i, v in enumerate(vitesses):
            sens = 1 if i % 2 == 0 else -1
            js += (f'        tl.to(".l{i}", {{ x:{sens * 46}, duration:{v},'
                   f' ease:"sine.inOut", yoyo:true, repeat:{_repeat(v, dur)} }}, 0);\n')
        return js

    def _clip(self, abs_debut, dur):
        """Durée déclarée d'un clip imbriqué — lue en temps absolu (piège 3)."""
        return f"{float(abs_debut) + float(dur):.2f}"

    def _entete(self, clock, eyebrow):
        return (f'        <div class="clock" id="clock">{clock}</div>\n'
                f'        <div class="eyebrow" id="eyebrow">{eyebrow}</div>\n')

    @staticmethod
    def _entete_js():
        return ('        tl.fromTo("#clock", { opacity:0, y:-12 }, { opacity:1, y:0, duration:.4, ease:"power2.out" }, .05);\n'
                '        tl.fromTo("#eyebrow", { opacity:0, y:-12 }, { opacity:.95, y:0, duration:.4, ease:"power2.out" }, .12);\n')

    def _manques_js(self, manques):
        js = ""
        for i in range(len(manques)):
            js += (f'        tl.fromTo("#mq{i}", {{ opacity:0, scale:.85, y:14 }},'
                   f' {{ opacity:1, scale:1, y:0, duration:.26, ease:"back.out(2)" }},'
                   f' {1.8 + i * .30:.2f});\n')
        return js

    def _manques_html(self, manques):
        return ('        <div class="manques">\n'
                + "".join(f'          <div class="manque" id="mq{i}"><span>✕</span>{t}</div>\n'
                          for i, t in enumerate(manques))
                + "        </div>\n")

    # ── scènes ───────────────────────────────────────────────────────────
    def hook(self, cid, abs_debut, dur, phase):
        """Ouverture demandée par Michael : « Une journée sans FoodEatUp ».

        Pas de logo en couleur ici. Le film raconte l'absence du produit ;
        ouvrir sur sa marque en pleine charte désamorcerait le carton final,
        où le retour de la charte est l'argument. Le mot est écrit, et « sans »
        porte seul la couleur d'alerte.
        """
        body = (
            _FOND_HTML
            + '        <div class="hk-sur" id="hkSur">UNE JOURNÉE</div>\n'
            + '        <div class="hk-titre" id="hkTitre"><em>sans</em> FoodEatUp</div>\n'
            + f'        <div class="hk-phase" id="hkPhase">{self.PHASES[phase]}</div>\n'
            + f'        <div class="hk-lieu" id="hkLieu">{self.LIEUX[self.metier]}</div>\n'
            + '        <div class="hk-barre" id="hkBarre"></div>\n'
        )
        js = (
            self._fond_js(dur)
            + '        tl.fromTo("#hkSur", { opacity:0, y:16 }, { opacity:1, y:0, duration:.4, ease:"power2.out" }, .2);\n'
            + '        tl.fromTo("#hkTitre", { opacity:0, y:26 }, { opacity:1, y:0, duration:.5, ease:"power2.out" }, .5);\n'
            + '        tl.fromTo("#hkPhase", { opacity:0, y:16 }, { opacity:1, y:0, duration:.4, ease:"power2.out" }, 1.05);\n'
            + '        tl.fromTo("#hkLieu", { opacity:0 }, { opacity:1, duration:.35 }, 1.35);\n'
            + '        tl.fromTo("#hkBarre", { scaleX:0 }, { scaleX:1, duration:.4, ease:"power2.out" }, 1.55);\n'
        )
        return _TEMPLATE.format(style=self.style, cid=cid, dur=dur, body=body, js=js)

    def carton(self, cid, abs_debut, dur, plate, vid_id, title, sub,
               title_at=".9", sub_at="1.5"):
        """Plan tourné plein cadre, titre, sous-titre.

        Les plans sont déjà étalonnés au registre « sans » par
        `plans-sans.sh` : désaturés, refroidis, contraste écrasé. On ajoute
        seulement un voile sombre, qui tient le texte lisible sur des images
        volontairement plates.
        """
        body = (
            _FOND_HTML
            + f'        <video class="amb clip" id="{vid_id}" src="assets/plates/{self.sous}/{plate}.mp4"'
            f' muted playsinline data-start="0" data-duration="{self._clip(abs_debut, dur)}"'
            ' data-track-index="2"></video>\n'
            + '        <div class="assombri" id="voile"></div>\n'
            + f'        <div class="title" id="title">{title}</div>\n'
            + f'        <div class="sub" id="sub">{sub}</div>\n'
        )
        # Le zoom ne démarre qu'après l'entrée : deux tweens portant `scale`
        # en même temps, le second gagne et l'apparition est perdue.
        js = (
            self._fond_js(dur)
            + f'        tl.fromTo("#{vid_id}", {{ opacity:0, scale:1.06 }}, {{ opacity:1, scale:1, duration:1.1, ease:"power2.out" }}, 0);\n'
            + f'        tl.to("#{vid_id}", {{ scale:1.04, duration:{max(0.5, float(dur) - 1.1):.2f}, ease:"none" }}, 1.1);\n'
            + '        tl.fromTo("#voile", { opacity:0 }, { opacity:1, duration:.8 }, .3);\n'
            + f'        tl.fromTo("#title", {{ opacity:0, y:24 }}, {{ opacity:1, y:0, duration:.6, ease:"power2.out" }}, {title_at});\n'
            + f'        tl.fromTo("#sub", {{ opacity:0, y:14 }}, {{ opacity:.94, y:0, duration:.5, ease:"power2.out" }}, {sub_at});\n'
        )
        return _TEMPLATE.format(style=self.style, cid=cid, dur=dur, body=body, js=js)

    def outils(self, cid, abs_debut, dur, clock, eyebrow, outils, manques):
        """N maquettes d'outils côte à côte, qui ne se touchent jamais.

        `outils` est une liste de libellés **génériques** : « Tableur »,
        « Cahier de cuisine », « Boîte mail ». Jamais un nom de produit, jamais
        une catégorie assez étroite pour désigner un acteur unique. Chaque
        fenêtre apparaît seule, puis une croix rouge s'inscrit entre deux
        d'entre elles : ce qui manque n'est pas l'outil, c'est le lien.
        """
        n = len(outils)
        larg = (FRAME_W - (n - 1) * 34) // n
        cadres = ""
        for i, nom in enumerate(outils):
            x = i * (larg + 34)
            cadres += (
                f'          <div class="outil" id="ou{i}"'
                f' style="left:{x}px; width:{larg}px; height:{FRAME_H}px;">\n'
                '            <div class="barre"><div class="pastille"></div>'
                '<div class="pastille"></div>'
                f'<div class="nom">{nom}</div></div>\n'
                '            <div class="corps">\n'
                '              <div class="rang"></div>\n'
                '              <div class="rang moyen"></div>\n'
                '              <div class="rang court"></div>\n'
                '              <div class="rang moyen"></div>\n'
                '              <div class="rang court"></div>\n'
                '            </div>\n'
                '          </div>\n'
            )
        # Une croix dans chaque intervalle : la jonction qui n'existe pas.
        for i in range(n - 1):
            cx = i * (larg + 34) + larg + 1
            cadres += (f'          <div class="croix" id="cx{i}"'
                       f' style="left:{cx}px; top:{FRAME_H // 2 - 34}px;">✕</div>\n')

        body = (
            _FOND_HTML
            + self._entete(clock, eyebrow)
            + f'        <div class="board" id="board">\n{cadres}        </div>\n'
            + self._manques_html(manques)
        )
        js = (
            self._fond_js(dur)
            + self._entete_js()
            + '        tl.fromTo("#board", { opacity:0, y:18 }, { opacity:1, y:0, duration:.35, ease:"power2.out" }, .3);\n'
        )
        for i in range(n):
            js += (f'        tl.fromTo("#ou{i}", {{ opacity:0, y:22 }},'
                   f' {{ opacity:1, y:0, duration:.32, ease:"power2.out" }}, {0.55 + i * .22:.2f});\n')
        for i in range(n - 1):
            js += (f'        tl.fromTo("#cx{i}", {{ opacity:0, scale:.5 }},'
                   f' {{ opacity:1, scale:1, duration:.24, ease:"back.out(2.4)" }},'
                   f' {0.55 + n * .22 + i * .26:.2f});\n')
        js += self._manques_js(manques)
        return _TEMPLATE.format(style=self.style, cid=cid, dur=dur, body=body, js=js)

    def tab_chaos(self, cid, abs_debut, dur, clock, eyebrow, onglets, chiffre,
                  manques, allers=3):
        """Le plan obligatoire des neuf films (NOTES §6.3).

        Un écran, sept onglets, et le curseur qui recopie un chiffre à la main
        d'un onglet à l'autre. 1,2 s par aller-retour, trois minimum. Le
        chiffre est le même à chaque fois : c'est la ressaisie qui est le
        sujet, pas la donnée.

        Les onglets portent des libellés génériques. Aucun n'est reconnaissable
        (§6.1) — et c'est le nombre, pas les noms, qui fait l'argument.
        """
        tabs = "".join(
            f'            <div class="tab{" actif" if i == 0 else ""}" id="tb{i}">{t}</div>\n'
            for i, t in enumerate(onglets)
        )
        body = (
            _FOND_HTML
            + self._entete(clock, eyebrow)
            + '        <div class="board" id="board">\n'
            + f'          <div class="tabs">\n{tabs}          </div>\n'
            + '          <div class="page">\n'
            + '            <div class="champ-lib" style="left:98px; top:104px;">Chiffre de la veille</div>\n'
            + f'            <div class="champ" style="left:96px; top:140px;">{chiffre}</div>\n'
            + '            <div class="champ-lib" style="left:1122px; top:104px;">À reporter</div>\n'
            + '            <div class="champ vide" id="cible" style="left:1120px; top:140px;">—</div>\n'
            + _remplissage
            # Position explicite : sans `left`/`top`, l'élément se posait au
            # flux et le tween `x` le déplaçait depuis un point indéterminé.
            + f'            <div class="porte" id="porte" style="left:150px; top:212px;">{chiffre}</div>\n'
            # Le curseur pointe sous et à droite du champ : posé dessus, il
            # masquait le premier chiffre — c'est-à-dire précisément ce que le
            # plan doit faire lire.
            + '            <div class="curseur" id="cur" style="left:330px; top:186px;">\n'
            + '              <svg viewBox="0 0 24 26" width="42" height="46">\n'
            + f'                <path d="M2 1 L2 22 L7.5 16.5 L11 25 L15 23 L11.5 15 L19 15 Z"'
            f' fill="{ANTHRACITE}" stroke="#FFFFFF" stroke-width="1.4" stroke-linejoin="round" />\n'
            + '              </svg>\n'
            + '            </div>\n'
            + '          </div>\n'
            + '        </div>\n'
            + self._manques_html(manques)
        )
        js = (
            self._fond_js(dur)
            + self._entete_js()
            + '        tl.fromTo("#board", { opacity:0, y:18 }, { opacity:1, y:0, duration:.35, ease:"power2.out" }, .3);\n'
        )
        # Un aller-retour : le curseur prend le chiffre à gauche, le porte à
        # droite, le dépose. 1,2 s, comme au §6.3.
        t = 0.9
        for k in range(allers):
            onglet = (k * 2 + 1) % len(onglets)
            js += (
                f'        // Aller-retour {k + 1} : on recopie {chiffre} à la main.\n'
                f'        tl.to("#cur", {{ x:0, y:0, duration:.20, ease:"power2.inOut" }}, {t:.2f});\n'
                f'        tl.fromTo("#porte", {{ opacity:0, x:0, y:0 }},'
                f' {{ opacity:1, x:0, y:0, duration:.14 }}, {t + 0.20:.2f});\n'
                f'        tl.to("#cur", {{ x:940, duration:.44, ease:"power1.inOut" }}, {t + 0.34:.2f});\n'
                f'        tl.to("#porte", {{ x:940, duration:.44, ease:"power1.inOut" }}, {t + 0.34:.2f});\n'
                f'        tl.to("#porte", {{ opacity:0, duration:.12 }}, {t + 0.78:.2f});\n'
                f'        tl.to("#cur", {{ x:0, duration:.30, ease:"power1.inOut" }}, {t + 0.90:.2f});\n'
                # L'onglet actif change à chaque tour : sept fenêtres pour un
                # seul chiffre, c'est le plan tout entier.
                f'        tl.to("#tb{onglet}", {{ backgroundColor:"#FFFFFF", color:"{ANTHRACITE}", duration:.12 }}, {t + 0.34:.2f});\n'
                f'        tl.to("#tb{onglet}", {{ backgroundColor:"#C9CED4", color:"#5D646C", duration:.12 }}, {t + 1.06:.2f});\n'
            )
            t += 1.2
        # Le champ d'arrivée ne se remplit qu'au **dernier** aller-retour. S'il
        # se remplissait au premier, les tours suivants n'auraient plus d'objet
        # à l'écran, et le plan dirait « j'ai recopié » au lieu de « je recopie
        # encore ».
        fin = 0.9 + (allers - 1) * 1.2 + 0.78
        js += (f'        tl.to("#cible", {{ color:"{ANTHRACITE}", duration:.1 }}, {fin:.2f});\n'
               f'        tl.to("#cible", {{ innerText:"{chiffre}", duration:.1 }}, {fin:.2f});\n')
        js += self._manques_js(manques)
        return _TEMPLATE.format(style=self.style, cid=cid, dur=dur, body=body, js=js)

    def refrain(self, cid, abs_debut, dur, phrase, appui):
        """Le refrain, à 20 % de la durée, dans les neuf films.

        Une seule phrase, tenue plein cadre. C'est le seul moment où le film
        s'arrête de raconter une journée pour énoncer son argument, et il ne
        supporte donc aucun décor.
        """
        body = (
            _FOND_HTML
            + f'        <div class="refrain" id="refrain">{phrase}</div>\n'
            + f'        <div class="refrain-b" id="appui">{appui}</div>\n'
        )
        js = (
            self._fond_js(dur)
            + '        tl.fromTo("#refrain", { opacity:0, y:22 }, { opacity:1, y:0, duration:.55, ease:"power2.out" }, .25);\n'
            + '        tl.fromTo("#appui", { opacity:0, y:14 }, { opacity:1, y:0, duration:.45, ease:"power2.out" }, 1.05);\n'
        )
        return _TEMPLATE.format(style=self.style, cid=cid, dur=dur, body=body, js=js)

    def compteur(self, cid, abs_debut, dur, clock, eyebrow, blocs):
        """Le compteur du volet : ce que la journée a coûté.

        `blocs` est une liste de couples (valeur, libellé). Les valeurs sont
        **toujours des fourchettes** (NOTES §6.2) : un chiffre unique est
        attaquable, une fourchette sourcée ne l'est pas.
        """
        # La valeur ne doit jamais revenir à la ligne : le bloc fait 400 px, et
        # une fourchette comme « 1 h 45 à 2 h 30 » n'y tient pas à 78 px. On
        # réduit d'après la longueur plutôt que de raccourcir le texte — c'est
        # la fourchette qui rend le chiffre défendable (NOTES §6.2).
        taille = max((len(v) for v, _ in blocs), default=0)
        px = 78 if taille <= 6 else 62 if taille <= 10 else 46
        cases = "".join(
            f'          <div class="bloc" id="bl{i}">'
            f'<div class="val" style="font-size:{px}px">{v}</div>'
            f'<div class="lib">{lib}</div></div>\n'
            for i, (v, lib) in enumerate(blocs)
        )
        body = (
            _FOND_HTML
            + self._entete(clock, eyebrow)
            + f'        <div class="compteur">\n{cases}        </div>\n'
        )
        js = self._fond_js(dur) + self._entete_js()
        for i in range(len(blocs)):
            js += (f'        tl.fromTo("#bl{i}", {{ opacity:0, y:26 }},'
                   f' {{ opacity:1, y:0, duration:.4, ease:"back.out(1.4)" }}, {0.5 + i * .35:.2f});\n')
        return _TEMPLATE.format(style=self.style, cid=cid, dur=dur, body=body, js=js)

    def punchline(self, cid, abs_debut, dur):
        """Carton final, identique sur les neuf films.

        Seul plan du volet où la charte réapparaît : fond marine, lueurs bleue
        et orange, logo, et la signature de la marque. La bascule est franche
        — c'est elle l'argument, et un fondu long la rendrait décorative.
        Michael ferme le plan, comme sur les neuf films « avec ».
        """
        body = (
            _FOND_HTML
            + '        <div class="pl-fond" id="plFond"></div>\n'
            + '        <div class="pl-lueur-a" id="plA"></div>\n'
            + '        <div class="pl-lueur-b" id="plB"></div>\n'
            + '        <img class="pl-photo" id="plPhoto" src="assets/brand/serie/michael-chef-cadre.jpg" alt="" />\n'
            + '        <img class="pl-logo" id="plLogo" src="assets/brand/serie/logo-mascot.png" alt="" />\n'
            + '        <div class="pl-une" id="plUne">Avec FoodEatUp,<br />une seule application.</div>\n'
            + '        <div class="pl-deux" id="plDeux">La solution qui s&rsquo;occupe de votre établissement'
              '<br />avant, pendant et après votre service.</div>\n'
            + '        <div class="pl-barre" id="plBarre"></div>\n'
        )
        js = (
            self._fond_js(dur)
            # 180 ms : assez pour ne pas clignoter, trop court pour être un fondu.
            + '        tl.fromTo("#plFond", { opacity:0 }, { opacity:1, duration:.18, ease:"power1.in" }, .1);\n'
            + '        tl.fromTo("#plA", { opacity:0 }, { opacity:1, duration:.6 }, .28);\n'
            + '        tl.fromTo("#plB", { opacity:0 }, { opacity:1, duration:.6 }, .36);\n'
            + '        tl.fromTo("#plPhoto", { opacity:0, x:60 }, { opacity:1, x:0, duration:.7, ease:"power2.out" }, .3);\n'
            + '        tl.fromTo("#plLogo", { opacity:0, y:18 }, { opacity:1, y:0, duration:.45, ease:"power2.out" }, .55);\n'
            + '        tl.fromTo("#plUne", { opacity:0, y:18 }, { opacity:1, y:0, duration:.5, ease:"power2.out" }, .95);\n'
            # Les 800 ms du §6.3 : la deuxième phrase ne doit jamais arriver
            # avec la première, c'est le temps de respiration qui la porte.
            + '        tl.fromTo("#plDeux", { opacity:0, y:14 }, { opacity:1, y:0, duration:.5, ease:"power2.out" }, 1.75);\n'
            + '        tl.fromTo("#plBarre", { scaleX:0 }, { scaleX:1, duration:.45, ease:"power2.out" }, 2.30);\n'
        )
        return _TEMPLATE.format(style=self.style, cid=cid, dur=dur, body=body, js=js)

    # ── écriture ─────────────────────────────────────────────────────────
    def ecrire(self, scenes):
        self.out.mkdir(parents=True, exist_ok=True)
        for name, html in scenes.items():
            (self.out / name).write_text(html, encoding="utf-8")
            print("écrit", f"{self.sous}/{name}")
