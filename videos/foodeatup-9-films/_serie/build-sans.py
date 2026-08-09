#!/usr/bin/env python3
"""Monte les neuf films « sans » : scènes, orchestrateurs, audio.

Un seul générateur pour les neuf, parce que les neuf partagent la même
armature. NOTES §6.3 impose le refrain, le plan des sept onglets et le carton
final **dans tous les films** ; écrire neuf montages séparés, ce serait neuf
occasions d'en oublier un. Ici l'armature est ci-dessous, en dur, et ne peut
pas manquer :

    hook · carton · outils · REFRAIN · outils · TAB-CHAOS · compteur ·
    carton · punchline

Les bornes ne sont pas écrites ici : elles viennent de `timing.json`, produit
par `vo-sans.py` à partir de la durée **mesurée** de chaque segment de voix.
Une scène ne peut donc pas se refermer avant sa phrase — c'est vrai par
construction, pas par relecture.

Aucun décalage n'est appliqué après coup. Le hook est la scène 1, déclarée à
0,00 s comme les autres ; c'est ce qui distingue ce montage de celui des films
« avec », où l'habillage posé après coup avait éteint les cent-deux plans de la
série d'un seul geste.

Usage : python3 _serie/build-sans.py [film…]
"""

import json
import pathlib
import shutil
import sys

ICI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))
from films_sans import (FILMS, HORLOGES, ONGLETS,  # noqa: E402
                        PHOTOS_COMPTEUR, REFRAIN, REFRAIN_APPUI, SURTITRES)
from serie_sans import SerieSans  # noqa: E402

RACINE = ICI.parent
STUDIO = ICI.parents[2] / "studio-video"
COMPO = STUDIO / "compositions"
AUDIO = STUDIO / "assets" / "audio"

# Ambiance et voix.
#
# Michael a trouvé musique et bruitages trop présents. Un facteur unique plutôt
# que huit réglages retouchés un par un : la balance entre les bruitages avait
# été travaillée, il n'y avait pas lieu de la défaire, seulement de passer
# l'ensemble sous la voix. 0,25 vaut −12 dB.
#
# ⚠️ Ce facteur doit rester identique à celui de `adoucir-ambiance.py`, qui a
# servi à corriger les neuf films déjà rendus sans les re-rendre. S'ils
# divergent, un nouveau rendu réintroduira les anciens niveaux sans que
# personne le remarque.
AMBIANCE = 0.25

# La voix ne bouge pas. C'est justement pour mieux l'entendre qu'on baisse le
# reste : y toucher défairait le gain obtenu.
#
# Ne pas y reporter le `GAIN_VOIX = 1.26` de `adoucir-ambiance.py`. Ce 1,26
# compense une perte propre à la reconstruction du mixage par ffmpeg — le
# moteur de rendu, lui, applique déjà ce gain. Le déclarer ici l'appliquerait
# deux fois et sortirait un rendu 2 dB au-dessus des neuf films existants.
VOIX = 1

HOOK = 4.20

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
{audio}
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


def construire(film, spec):
    sous = spec["sous"]
    t = json.loads((RACINE / film / "assets" / "timing.json").read_text())
    b = t["scenes"]          # huit bornes, une par scène de corps
    total = t["total"]
    s = SerieSans(metier=spec["metier"], sous=sous)

    o1_noms, o1_manques = spec["outils1"]
    o2_noms, o2_manques = spec["outils2"]
    ouv_t, ouv_s = spec["ouverture"]
    clo_t, clo_s = spec["cloture"]
    onglets = ONGLETS[spec["metier"]]
    horloges, surtitres = HORLOGES[film], SURTITRES[film]

    # Le plan des sept onglets doit tenir au moins trois allers-retours de
    # 1,2 s (§6.3) plus l'entrée du tableau. Si le segment de voix est plus
    # long, on en met un de plus plutôt que de laisser le curseur immobile.
    allers = max(3, int((b[4]["duree"] - 1.4) // 1.2))

    scenes = {
        f"{sous}-s1-hook.html": ("hook", s.hook(
            f"{sous}-s1-hook", 0.00, HOOK, spec["phase"])),
        f"{sous}-s2-ouverture.html": ("carton", s.carton(
            f"{sous}-s2-ouverture", b[0]["debut"], b[0]["duree"],
            spec["plates"][0], f"vid-{sous}-ouv", ouv_t, ouv_s,
            title_at=".7", sub_at="1.4")),
        f"{sous}-s3-outils.html": ("outils", s.outils(
            f"{sous}-s3-outils", b[1]["debut"], b[1]["duree"],
            horloges[0], surtitres[0], o1_noms, o1_manques)),
        f"{sous}-s4-refrain.html": ("refrain", s.refrain(
            f"{sous}-s4-refrain", b[2]["debut"], b[2]["duree"],
            REFRAIN, REFRAIN_APPUI)),
        f"{sous}-s5-outils.html": ("outils", s.outils(
            f"{sous}-s5-outils", b[3]["debut"], b[3]["duree"],
            horloges[1], surtitres[1], o2_noms, o2_manques)),
        f"{sous}-s6-onglets.html": ("tabs", s.tab_chaos(
            f"{sous}-s6-onglets", b[4]["debut"], b[4]["duree"],
            horloges[2], "LE MÊME CHIFFRE, RECOPIÉ À LA MAIN",
            onglets, spec["chiffre"], ["Sept fenêtres", "Un seul chiffre"],
            allers=allers)),
        f"{sous}-s7-compteur.html": ("compteur", s.compteur(
            f"{sous}-s7-compteur", b[5]["debut"], b[5]["duree"],
            horloges[3], "CE QUE LA JOURNÉE A COÛTÉ", spec["compteur"],
            photo=PHOTOS_COMPTEUR[film])),
        f"{sous}-s8-cloture.html": ("carton", s.carton(
            f"{sous}-s8-cloture", b[6]["debut"], b[6]["duree"],
            spec["plates"][1], f"vid-{sous}-clo", clo_t, clo_s,
            title_at=".5", sub_at="1.2")),
        f"{sous}-s9-punchline.html": ("punchline", s.punchline(
            f"{sous}-s9-punchline", b[7]["debut"], b[7]["duree"])),
    }
    s.ecrire({n: html for n, (_, html) in scenes.items()})

    # ── orchestrateur ────────────────────────────────────────────────────
    bornes = [(0.00, HOOK)] + [(x["debut"], x["duree"]) for x in b]
    slots = "\n\n".join(
        SLOT.format(cid=nom[:-5], sous=sous, debut=d, duree=du)
        for nom, (d, du) in zip(scenes, bornes))

    pl_debut, pl_duree = b[7]["debut"], b[7]["duree"]
    lit = {"avant": "lit-avant", "pendant": "lit-pendant",
           "apres": "lit-apres"}[spec["phase"]]

    lignes = [
        # Marqueur lu par `adoucir-ambiance.py`, qui refuse alors de tourner :
        # il multiplie les volumes déclarés par le même facteur, donc l'appliquer
        # sur une composition qui le porte déjà donnerait −24 dB au lieu de −12.
        f'      <!-- ambiance-adoucie={AMBIANCE} -->',
        "      <!-- Voix off. Le fichier porte déjà ses silences : les segments",
        "           ont été posés à leur instant exact par vo-sans.py, donc la",
        "           piste commence à 0 et rien n'est à recaler ici. -->",
        f'      <audio id="el-vo" src="assets/audio/{film}-vo.mp3" data-start="0"'
        f' data-duration="{total:.2f}" data-track-index="10" data-volume="{VOIX}"></audio>',
        "",
        "      <!-- Lit non résolu : il tourne sans jamais retomber sur sa",
        "           fondamentale, et il s'arrête net à l'entrée du carton final. -->",
        f'      <audio id="sfx-lit" src="assets/audio/sans/{lit}.mp3" data-start="0"'
        f' data-duration="{pl_debut:.2f}" data-track-index="11" data-volume="{0.42 * AMBIANCE:.4f}"></audio>',
        "",
        "      <!-- La cadence. Seul accord qui se referme de tout le film, et",
        "           c'est lui l'argument (NOTES §6.3). -->",
        f'      <audio id="sfx-resolution" src="assets/audio/sans/resolution.mp3"'
        f' data-start="{pl_debut:.2f}" data-duration="{pl_duree:.2f}"'
        f' data-track-index="11" data-volume="{0.62 * AMBIANCE:.4f}"></audio>',
        "",
        "      <!-- Une page tournée à chaque fenêtre d'outil qui apparaît. -->",
    ]
    n = 0
    for idx, (noms, _) in ((1, spec["outils1"]), (3, spec["outils2"])):
        for i in range(len(noms)):
            n += 1
            at = b[idx]["debut"] + 0.55 + i * 0.22
            # Une piste par fenêtre, pas deux en alternance : le bruitage dure
            # 0,90 s et les fenêtres s'ouvrent toutes les 0,22 s, donc deux
            # bruitages posés sur la même piste se chevaucheraient.
            lignes.append(
                f'      <audio id="sfx-papier-{n:02d}" src="assets/audio/sans/papier.mp3"'
                f' data-start="{at:.2f}" data-duration="0.90"'
                f' data-track-index="{12 + n}" data-volume="{0.85 * AMBIANCE:.4f}"></audio>')

    lignes += ["",
               "      <!-- Une frappe par aller-retour du curseur : c'est le bruit",
               "           de la ressaisie, et il doit être sec. -->"]
    for k in range(allers):
        at = b[4]["debut"] + 0.9 + k * 1.2 + 0.20
        lignes.append(
            f'      <audio id="sfx-frappe-{k + 1:02d}" src="assets/audio/sans/frappe.mp3"'
            f' data-start="{at:.2f}" data-duration="0.52"'
            f' data-track-index="{20 + k % 2}" data-volume="{0.30 * AMBIANCE:.4f}"></audio>')
        lignes.append(
            f'      <audio id="sfx-clic-{k + 1:02d}" src="assets/audio/sans/clic-mat.mp3"'
            f' data-start="{at + 0.58:.2f}" data-duration="0.52"'
            f' data-track-index="{22 + k % 2}" data-volume="{0.26 * AMBIANCE:.4f}"></audio>')

    lignes += ["",
               "      <!-- Le compteur tombe sur un souffle de machine qui s'arrête. -->",
               f'      <audio id="sfx-soupir" src="assets/audio/sans/soupir-machine.mp3"'
               f' data-start="{b[5]["debut"] + 0.35:.2f}" data-duration="1.65"'
               f' data-track-index="24" data-volume="{0.18 * AMBIANCE:.4f}"></audio>']

    (COMPO / f"{film}.html").write_text(
        ORCHESTRATEUR.format(film=film, total=f"{total:.2f}",
                             scenes=slots, audio="\n".join(lignes)),
        encoding="utf-8")

    AUDIO.mkdir(parents=True, exist_ok=True)
    shutil.copy(RACINE / film / "assets" / "vo.mp3", AUDIO / f"{film}-vo.mp3")
    print(f"  + {film:28} {total:6.2f} s   9 scènes, {allers} allers-retours")
    return total


def main():
    voulus = sys.argv[1:] or list(FILMS)
    for film in voulus:
        construire(film, FILMS[film])


if __name__ == "__main__":
    main()
