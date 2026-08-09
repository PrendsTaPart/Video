#!/usr/bin/env python3
"""Prépare les seize vignettes, sous le nom qu'elles porteront en bibliothèque.

Les quinze premières viennent du Drive : ce sont les cartons d'intro officiels
de la série, déjà tournés à la charte (logo, photo, titre orange, appel à
l'action). Les cent cinquante-sept tutoriels en ligne utilisent exactement cet
asset — le même fichier sert d'ouverture au film *et* de vignette sur le site.
Les reprendre, plutôt que d'en fabriquer, c'est ce qui fait que la grille du
catalogue reste une grille et non deux séries côte à côte.

La seizième n'a pas de carton : `retrouver-toutes-mes-commandes` a été réanglée
après le tournage des intros. Sa vignette est **extraite de son propre film**,
sur son plan d'ouverture — donc à la même charte, par construction.

Le nom de sortie suit la règle de la bibliothèque : le `-v1` du film est
*remplacé* par `-thumbnail` (`tuto-<slug>-v1` → `tuto-<slug>-thumbnail`), et non
suffixé. Cent vingt et une des cent vingt-quatre fiches déjà en ligne le font
ainsi.

**Ce que ce script produit n'est pas ce qui part en bibliothèque, sauf pour la
seizième.** RapidoCMS n'accepte pas d'octets, seulement une URL publique : les
quinze cartons y sont donc envoyés depuis leur lien Drive, tels quels. Le
dossier `_vignettes/` sert de copie locale contrôlable — et de seule source
possible pour le tutoriel qui n'a pas de carton.

L'écart entre les deux est d'un pixel (1281×721 côté Drive, 1280×720 ici) et ne
se voit pas dans une tuile de catalogue. Le noter reste utile : c'est la raison
pour laquelle une comparaison d'empreintes entre `_vignettes/` et ce que sert la
bibliothèque échouerait sur quinze fichiers sur seize, sans que rien ne soit
cassé.

Usage : python3 _tuto/vignettes.py
"""

import pathlib
import subprocess
import sys

ICI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))
from scripts import TUTORIELS  # noqa: E402

RACINE = ICI.parent
INTROS = RACINE / "_intros"
SORTIE = RACINE / "_vignettes"

# La seconde où prélever l'image du film qui n'a pas de carton Drive. Deux
# secondes : le carton d'ouverture est installé, son animation d'entrée est
# terminée. À zéro, on capturerait la première image d'un fondu.
SECONDE = 2.0

# Le format des vignettes déjà en bibliothèque, relevé sur l'une d'elles
# (`foodeatup-tva-tuto-thumbnail` : 1280×720, 118 ko, encodée par ffmpeg).
# Ce n'est pas le format du film : une vignette de catalogue s'affiche dans une
# tuile, et la servir en 1920×1080 ferait payer trois fois le poids nécessaire
# à chaque visiteur qui ouvre la grille — pour cent quatre-vingt-huit tuiles.
LARGEUR, HAUTEUR = 1280, 720
QUALITE = "3"  # échelle ffmpeg 2–31 ; 3 tient les ~120 ko des vignettes en ligne


def encoder(entree: list[str], cible: pathlib.Path) -> None:
    subprocess.run(
        [
            "ffmpeg", "-y", "-loglevel", "error",
            *entree,
            "-frames:v", "1",
            "-vf", f"scale={LARGEUR}:{HAUTEUR}:flags=lanczos",
            "-q:v", QUALITE,
            str(cible),
        ],
        check=True,
    )


def depuis_intro(source: pathlib.Path, cible: pathlib.Path) -> None:
    encoder(["-i", str(source)], cible)


def depuis_film(film: pathlib.Path, cible: pathlib.Path) -> None:
    encoder(["-ss", str(SECONDE), "-i", str(film)], cible)


def main() -> int:
    SORTIE.mkdir(exist_ok=True)
    manquants = []

    for t in TUTORIELS:
        sous = t["sous"]
        cible = SORTIE / f"tuto-{t['slug']}-thumbnail.jpg"
        intro = INTROS / f"{sous}.jpg"
        film = RACINE / sous / "out" / f"{sous}.mp4"

        if intro.exists():
            depuis_intro(intro, cible)
            origine = "carton Drive"
        elif film.exists():
            depuis_film(film, cible)
            origine = f"film, à {SECONDE:g} s"
        else:
            manquants.append(sous)
            print(f"  ✗ {sous} : ni carton Drive ni film rendu")
            continue

        taille = cible.stat().st_size / 1024
        print(f"  ✓ {sous}  {cible.name}  ({origine}, {taille:.0f} ko)")

    print(f"\n{len(TUTORIELS) - len(manquants)}/{len(TUTORIELS)} vignettes dans {SORTIE}")
    if manquants:
        print(f"manquantes : {', '.join(manquants)} — relancer après leur rendu")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
