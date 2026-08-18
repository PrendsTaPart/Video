#!/usr/bin/env python3
"""Installe les prises ElevenLabs de « Une journée » et monte dans la foulée.

    python3 scripts/poser-voix-journee.py ~/Téléchargements/*.mp3
    python3 scripts/poser-voix-journee.py --dossier ~/Téléchargements

Pourquoi ce script
------------------
Les six prises sont générées sur ElevenLabs (flow `bIjvieqb4btsukNPIf1z`) mais
aucun outil exposé ici ne permet de les télécharger : `creative_get_flow_run_status`
est absent, et la bibliothèque d'assets ne reçoit jamais les générations — quatre
sondages différents le confirment (par `node_id`, par `generation_id`, par
modalité `audio`, par recherche sur le texte). Elles se récupèrent donc à la
main, une par lien.

Ce script fait le reste : il les range sous les noms que `build-journee.py`
attend, et lance le montage des épisodes dont le plan est là.

L'ordre
-------
Les six fichiers sont attendus dans l'ordre du tableau de la conversation, qui
est aussi l'ordre de génération sur le flow — de haut en bas de la page :

    1  chef-de-cuisine-accroche     « Il ouvre, il produit, il ferme… »
    2  chef-de-cuisine-tension      « Il est le seul à voir la marge… »
    3  second-accroche              « Il tient la mise en place… »
    4  second-tension               « Il répare ce que personne n'a vu venir… »
    5  chef-de-partie-accroche      « Un poste, une carte, et la quantité juste… »
    6  chef-de-partie-tension       « Il est le premier à savoir… »

Avec `--dossier`, les fichiers sont pris par date de modification croissante :
si tu les télécharges dans l'ordre de la page, ça tombe juste. Le script affiche
la correspondance et la durée de chaque prise AVANT d'écrire — une accroche fait
cinq à six secondes, une tension trois à quatre. Si les durées ne suivent pas ce
motif, l'ordre est faux et rien n'est perdu : relance avec les chemins dans le
bon ordre.
"""
import argparse
import pathlib
import shutil
import subprocess
import sys

R = pathlib.Path(__file__).resolve().parent.parent
VOIX = R / "assets" / "vo" / "journee"

NOMS = [
    ("chef-de-cuisine-accroche", "Il ouvre, il produit, il ferme…"),
    ("chef-de-cuisine-tension",  "Il est le seul à voir la marge…"),
    ("second-accroche",          "Il tient la mise en place…"),
    ("second-tension",           "Il répare ce que personne n'a vu venir…"),
    ("chef-de-partie-accroche",  "Un poste, une carte, et la quantité juste…"),
    ("chef-de-partie-tension",   "Il est le premier à savoir…"),
]

# Les huit épisodes dont le plan Higgsfield est déjà dans `dist/hooks/`.
MONTABLES = ["EP301", "EP302", "EP303", "EP304",
             "EP306", "EP307", "EP308", "EP309"]


def duree(f):
    try:
        return float(subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "default=nw=1:nk=1", str(f)],
            capture_output=True, text=True, check=True).stdout.strip())
    except Exception:
        return 0.0


def main(argv):
    p = argparse.ArgumentParser()
    p.add_argument("fichiers", nargs="*", type=pathlib.Path)
    p.add_argument("--dossier", type=pathlib.Path)
    p.add_argument("--monter", action="store_true",
                   help="enchaîner le montage des huit épisodes")
    a = p.parse_args(argv)

    src = list(a.fichiers)
    if a.dossier:
        src = sorted(a.dossier.glob("*.mp3"), key=lambda f: f.stat().st_mtime)
    if len(src) != len(NOMS):
        raise SystemExit(f"attendu {len(NOMS)} fichiers, reçu {len(src)}")

    VOIX.mkdir(parents=True, exist_ok=True)
    print(f"{'fichier source':<34} {'durée':>6}  →  destination")
    for f, (nom, texte) in zip(src, NOMS):
        d = duree(f)
        dest = VOIX / f"{nom}.mp3"
        shutil.copy2(f, dest)
        print(f"{f.name[:33]:<34} {d:5.2f}s  →  {dest.name}")
        print(f"{'':34}          « {texte} »")

    if not a.monter:
        print("\nPrises en place. Pour monter :")
        print("  python3 scripts/build-journee.py EP301 EP302 …")
        return 0

    print()
    for ep in MONTABLES:
        if not (R / "dist" / "hooks" / f"{ep}.mp4").exists():
            print(f"  {ep} : pas de plan — sauté")
            continue
        subprocess.run([sys.executable, str(R / "scripts" / "build-journee.py"),
                        ep], check=False)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
