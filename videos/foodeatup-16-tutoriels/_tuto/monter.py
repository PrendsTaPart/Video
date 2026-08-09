#!/usr/bin/env python3
"""Monte les seize tutoriels : scènes, orchestrateur, bande son.

Il ne décide d'aucune durée. Toutes viennent de `assets/timing.json`, produit
par `vo.py` à partir de segments réellement générés. C'est la règle de la série
et elle a une raison : une borne estimée est fausse d'une demi-seconde sans que
rien ne le signale, et le défaut ne se voit qu'au visionnage complet.

Usage : python3 _tuto/monter.py [sous…]
"""

import json
import pathlib
import sys

ICI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))
from plaques import INTROS, PLAQUES  # noqa: E402
from scripts import TUTORIELS  # noqa: E402
from tuto import NOMS_MODULES, Tuto  # noqa: E402

RACINE = ICI.parent
STUDIO = pathlib.Path(__file__).resolve().parents[3] / "studio-video"
COMPOS = STUDIO / "compositions"
AUDIO = STUDIO / "assets" / "audio"

ORCHESTRATEUR = """<!doctype html>
<html lang="fr">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1920, height=1080" />
    <script src="assets/vendor/gsap.min.js"></script>
    <style>
      * {{ margin:0; padding:0; box-sizing:border-box; }}
      html, body {{ width:1920px; height:1080px; overflow:hidden; background:#EDEEF0; }}
      body {{ font-family:"Inter",sans-serif; }}
      @font-face {{
        font-family:"Fredoka";
        src:url("assets/vendor/fonts/Fredoka-Variable.woff2") format("woff2-variations");
        font-weight:300 700; font-display:block;
      }}
      #root {{ position:relative; width:1920px; height:1080px; overflow:hidden; background:#EDEEF0; }}
      #root > div[data-composition-src] {{ position:absolute; inset:0; }}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="{film}" data-start="0"
         data-width="1920" data-height="1080" data-duration="{total}">
{scenes}

      <!-- Voix off. Le fichier porte déjà ses silences : chaque segment a été
           posé à son instant exact par vo.py, donc la piste commence à 0 et
           rien n'est à recaler ici. -->
      <audio id="el-vo" src="assets/audio/{film}-vo.mp3" data-start="0"
             data-duration="{total}" data-track-index="10" data-volume="1"></audio>
    </div>

    <script>
      window.__timelines = window.__timelines || {{}};
      window.__timelines["{film}"] = gsap.timeline({{ paused: true }});
    </script>
  </body>
</html>
"""

SLOT = """      <div
        id="el-{cid}"
        data-composition-id="{cid}"
        data-composition-src="compositions/{sous}/{cid}.html"
        data-start="{debut:.2f}"
        data-duration="{duree:.2f}"
        data-track-index="1"
        data-width="1920"
        data-height="1080"
      ></div>"""


def phrase_html(texte, accent_mots):
    """Met en gras les mots que la planche veut faire ressortir.

    Un seul groupe par phrase : deux mots accentués dans une même ligne, et
    l'œil ne sait plus lequel est le sujet.
    """
    for mot in accent_mots:
        if mot in texte:
            return texte.replace(mot, f"<b>{mot}</b>", 1)
    return texte


def construire(t):
    sous = t["sous"]
    timing = json.loads((RACINE / sous / "assets" / "timing.json").read_text(encoding="utf-8"))
    total = timing["total"]
    plan = timing["scenes"]
    g = Tuto(module=t["module"], sous=sous)

    ouv_plaque, fin_plaque = PLAQUES.get(sous, (None, None))
    jalons = t["boards"]
    etapes = [s for s in plan if s["genre"].startswith("planche")]
    surtitre = NOMS_MODULES[t["module"]]

    """
    Les bornes écrites dans le HTML sont arrondies au centième, et les durées
    sont **dérivées des débuts arrondis** — jamais arrondies séparément.

    Arrondir les deux indépendamment fait qu'une scène finit un centième après
    le début de la suivante : 18,226 + 4,107 = 22,333, qui s'écrit « 18.23 » et
    « 4.11 », donc une fin à 22,34 pour un voisin qui commence à 22,33. Le lint
    le refuse — « overlapping clips on the same track » — et il a raison : un
    chevauchement d'un centième sur la même piste laisse deux scènes visibles
    en même temps pendant une image.
    """
    debuts = [round(s["debut"], 2) for s in plan] + [round(total, 2)]

    scenes, slots = {}, []
    rang_planche = 0
    for i, s in enumerate(plan):
        cid = f"{sous}-s{i + 1}-{s['genre'].split(':')[0]}"
        debut = debuts[i]
        duree = round(debuts[i + 1] - debuts[i], 2)

        if s["genre"] == "ouverture":
            # L'intro officielle quand elle existe ; le carton fabriqué sinon.
            intro = INTROS.get(sous)
            html = (
                g.intro(cid, debut, duree, intro)
                if intro
                else g.ouverture(cid, debut, duree, t["titre"], t["intention"], ouv_plaque)
            )
        elif s["genre"] == "cloture":
            html = g.cloture(cid, debut, duree, fin_plaque)
        elif s["genre"] == "prompt":
            html = g.prompt(cid, debut, duree, t["prompt"], t["outils"])
        else:
            # Le jalon allumé suit l'étape, mais la frise n'a que quatre cases
            # et certains tutoriels ont cinq phrases : la dernière retombe sur
            # le dernier jalon plutôt que de sortir du tableau.
            actif = min(rang_planche, len(jalons) - 1)
            html = g.planche(
                cid, debut, duree, surtitre,
                rang_planche + 1, len(etapes),
                phrase_html(s["texte"], jalons),
                jalons, actif,
            )
            rang_planche += 1

        scenes[f"{cid}.html"] = html
        slots.append(SLOT.format(cid=cid, sous=sous, debut=debut, duree=duree))

    g.ecrire(scenes)

    COMPOS.mkdir(parents=True, exist_ok=True)
    (COMPOS / f"{sous}.html").write_text(
        ORCHESTRATEUR.format(film=sous, total=f"{total:.2f}", scenes="\n\n".join(slots)),
        encoding="utf-8",
    )

    AUDIO.mkdir(parents=True, exist_ok=True)
    (AUDIO / f"{sous}-vo.mp3").write_bytes((RACINE / sous / "assets" / "vo.mp3").read_bytes())
    return total


def main():
    voulus = sys.argv[1:]
    liste = [t for t in TUTORIELS if not voulus or t["sous"] in voulus]
    total = 0.0
    for t in liste:
        total += construire(t)
        print(f"    → {t['titre']}")
    print(f"\n{len(liste)} tutoriels montés, {total / 60:.1f} min au total.")


if __name__ == "__main__":
    main()
