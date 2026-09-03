#!/usr/bin/env python3
"""Récapitulatif de la série : durées, poids et fiche MCP de chaque tutoriel.

    python3 recapitulatif.py > RECAPITULATIF.md
"""
import subprocess, sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent
sys.path.insert(0, str(RACINE))
from studio.charte import ffmpeg  # noqa: E402

# Rattachement des vidéos aux fiches déjà prévues au catalogue de l'Académie.
FICHES = {
    "se-connecter-et-creer-son-compte": ("01", "01-creer-un-compte-rapidocms"),
    "configurer-son-profil": ("02", "01-completer-son-profil"),
    "remplir-sa-fiche-entreprise": ("03", "01-renseigner-son-entreprise"),
    "connecter-ses-reseaux-sociaux": ("04", "02-comprendre-l-association-de-comptes"),
    "lire-son-tableau-de-bord": ("05", "03-lire-son-tableau-de-bord"),
    "suivre-son-abonnement": ("06", "15-historique-des-achats"),
    "acheter-des-credits-et-du-stockage": ("07", "15-suivre-sa-consommation"),
    "creer-un-post-reseaux-sociaux": ("08", "05-creer-un-post-le-principe"),
    "piloter-le-calendrier-editorial": ("09", "04-decouvrir-le-calendrier"),
    "consulter-l-historique-des-publications": ("10", "07-decouvrir-l-historique"),
    "lancer-une-campagne": ("11", "08-creer-une-campagne"),
    "decouvrir-l-editeur": ("12", "10-decouvrir-l-editeur"),
    "choisir-un-template-de-post": ("13", "10-utiliser-un-template"),
    "creer-une-carte-de-visite": ("14", "12-choisir-un-template-de-carte"),
    "creer-une-carte-nfc": ("15", "10-choisir-un-modele-de-carte-nfc"),
    "creer-une-carte-digitale": ("16", "12-creer-une-carte-digitale"),
}


def duree(chemin: Path) -> str:
    if not chemin.exists():
        return "—"
    proc = subprocess.run([ffmpeg(), "-hide_banner", "-i", str(chemin)],
                          capture_output=True, text=True)
    for ligne in proc.stderr.splitlines():
        if "Duration:" in ligne:
            h, m, s = ligne.split("Duration:")[1].split(",")[0].strip().split(":")
            total = int(h) * 3600 + int(m) * 60 + float(s)
            return f"{int(total // 60)} min {int(total % 60):02d} s"
    return "?"


print("# Récapitulatif — série RapidoCMS Académie\n")
print("| N° | Tutoriel | Master 16:9 | Short 9:16 | Vignette | Fiche du catalogue |")
print("|---|---|---|---|---|---|")
faits = 0
for slug, (numero, fiche) in sorted(FICHES.items(), key=lambda kv: kv[1][0]):
    exports = RACINE / slug / "exports"
    master = exports / f"{slug}-16x9.mp4"
    short = exports / f"{slug}-9x16.mp4"
    vignette = exports / f"{slug}-vignette.jpg"
    if master.exists():
        faits += 1
    print(f"| {numero} | `{slug}` | {duree(master)} | {duree(short)} | "
          f"{'oui' if vignette.exists() else '—'} | `{fiche}` |")
print(f"\n**{faits} masters sur {len(FICHES)}.**")
