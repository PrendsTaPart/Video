#!/usr/bin/env python3
"""Tutoriel 41 — Gérer son abonnement et ses factures.

Fiche MCP `tutoriel_spec(numero: 41)`, slug `gerer-son-abonnement`.
Capture source : « Vidéo 41 — Factures et reçus de paiement » — 25,85 s, 392 × 852.

`assets/screencast.mp4` n'est PAS la capture brute : les blocs d'identité de la
facture PDF (vendeur et « Facturer à » — nom, adresse, téléphone, e-mail) y sont
pixellisés à partir de t = 23,5 s. Voir SCRIPT.md, section « Données
personnelles ». Ne jamais remplacer ce fichier par la capture d'origine.

    python3 episode.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "planit-academy"))

from academie import Episode, Segment, build_episode  # noqa: E402

# Capture propre : ni bande noire, ni filigrane.
CROP = "crop=392:852:0:0"

EPISODE = Episode(
    numero=41,
    slug="gerer-son-abonnement",
    titre="Gérer son abonnement et ses factures",
    titre_court="Gérer l'abonnement",
    promesse="Vous changez de formule et récupérez vos factures sans écrire à personne.",
    presentation=(
        "Bienvenue dans l'Académie Plan'It. Aujourd'hui : votre abonnement et vos "
        "factures. Vous changez de formule et vous récupérez vos justificatifs sans "
        "écrire à personne."
    ),
    module_nom="Crédits & Facturation",
    module_couleur="#F45FC4",
    variante="B",
    suivant="Gérer ses appareils connectés",
    crop=CROP,
    ecran_vignette=9.0,        # « Mes factures », la ligne de facture
    racine=Path(__file__).resolve().parent,
    segments=[
        # Coupes volontaires : 11,7 → 14,3 (page Stripe noire, sans contenu) et
        # 16,2 → 24,2 (retour sur un login CRM, puis le panneau Téléchargements
        # d'Android, qui liste des fichiers personnels sans rapport, puis les
        # recadrages du PDF avant qu'il ne se stabilise).
        Segment("N1",  0.0,  2.3, "1 · Le solde de crédits"),
        Segment("N2",  2.3,  4.0, "2 · Les crédits reçus"),
        Segment("N3",  4.0,  5.6, "3 · Formules et factures"),
        Segment("N4",  5.6,  8.2, "4 · Mes factures"),
        Segment("N5",  8.2, 11.7, "5 · Recherche et filtres"),
        Segment("N6", 14.3, 16.2, "6 · Télécharger le PDF"),
        Segment("N7", 24.2, 25.6, "7 · La facture"),
        # L'astuce se repose sur la facture : la capture n'a pas de plan libre.
        Segment("N8", 24.2, 25.6, "8 · Choisir sa formule"),
    ],
)

if __name__ == "__main__":
    build_episode(EPISODE)
