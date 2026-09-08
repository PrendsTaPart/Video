"""Écrit CATALOGUE.md : chaque vidéo produite, son thème, sa durée, son fichier
et son adresse dans la bibliothèque RapidoCMS.

    python3 scripts/catalogue.py > CATALOGUE.md
"""
import re
import sys
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))

from build import duration                      # noqa: E402
from serie30 import CLIPS, SERIE                 # noqa: E402
from serie50_data import LIGNES as L50           # noqa: E402
from serie60_data import LIGNES as L60           # noqa: E402

S3 = "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/"
OUT = ROOT / "out"

FILMS = [
    ("foodeatup-clip", "Une journée. Une app.", "Le clip"),
    ("foodeatup-presentation", "Le même restaurant, avant et après", "La présentation"),
    ("foodeatup-commercial", "Le contrôleur", "Le film commercial"),
    ("foodeatup-demo", "Un tour du restaurant", "La démonstration"),
    ("foodeatup-avant-apres", "Le même restaurant, deux fois", "Avant / après"),
    ("foodeatup-teaser", "Bande-annonce", "La bande-annonce"),
]
SHORTS = [
    ("foodeatup-short-haccp", "Le contrôle", "HACCP"),
    ("foodeatup-short-stock", "L'inventaire", "Stock"),
    ("foodeatup-short-equipe", "Le planning", "Équipe"),
    ("foodeatup-short-compta", "L'addition", "Caisse et compta"),
    ("foodeatup-short-reservations", "La double réservation", "Réservations"),
    ("foodeatup-short-avis", "L'avis du soir", "Avis client"),
]


def duree(nom):
    f = OUT / f"{nom}.mp4"
    if not f.exists():
        return "—"
    d = duration(f)
    return f"{int(d // 60)} min {int(d % 60):02d} s" if d >= 60 else f"{d:.0f} s"


def lien(titre_biblio):
    return S3 + urllib.parse.quote(f"FoodEatUp - {titre_biblio} (9x16).mp4")


def table(titre, lignes):
    print(f"\n## {titre}\n")
    print("| Vidéo | Sujet | Durée | Fichier | Bibliothèque |")
    print("|---|---|---|---|---|")
    for nom, titre_v, sujet in lignes:
        etat = "livrée" if (OUT / f"{nom}.mp4").exists() else "en attente"
        url = lien(titre_v) if etat == "livrée" else ""
        cell = f"[voir]({url})" if url else "—"
        print(f"| {titre_v} | {sujet} | {duree(nom)} | `{nom}.mp4` | {cell} |")


print("# Catalogue des vidéos FoodEatUp\n")
print("Toutes les vidéos sont montées à partir de la seule bibliothèque Higgsfield.")
print("Chacune existe en 9:16 (`.mp4`) et en 16:9 (`-16x9.mp4`). Le lien de la")
print("colonne « Bibliothèque » pointe la version verticale déposée dans RapidoCMS.\n")

table("Films", FILMS)
table("Shorts thématiques", SHORTS)
table("Série « 30 problèmes, 30 solutions »",
      [(f"foodeatup-s{n}-{v[1]}", v[2], v[1].replace("-", " ")) for n, v in SERIE.items()])
table("Clips musicaux",
      [(f"foodeatup-clip-{k}", f"{t} ({sous})", "clip musical sans voix")
       for k, (t, sous, _m, _p) in CLIPS.items()])
table("Seconde vague",
      [(f"foodeatup-{c.lower()}-{nom}", titre, nom.replace("-", " "))
       for c, nom, titre, _p, _l in L50])
table("Troisième vague",
      [(f"foodeatup-{c.lower()}-{nom}", titre, nom.replace("-", " "))
       for c, nom, titre, _p, _l in L60])

livrees = len(list(OUT.glob("foodeatup-*.mp4"))) - len(list(OUT.glob("*-16x9.mp4")))
print(f"\n**{livrees} vidéos livrées** à ce jour, chacune en deux formats.\n")
