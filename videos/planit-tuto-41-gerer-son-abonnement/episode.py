#!/usr/bin/env python3
"""Tutoriel 41 — Gérer son abonnement et ses factures.

Fiche MCP `tutoriel_spec(numero: 41)`, slug `gerer-son-abonnement`.
Capture source : « Vidéo 41 — Factures et reçus de paiement » — 25,85 s, 392 × 852.

`assets/screencast.mp4` n'est PAS la capture brute : les blocs d'identité de la
facture PDF (vendeur et « Facturer à » — nom, adresse, téléphone, e-mail) y sont
pixellisés à partir de t = 23,5 s, et quatre secondes de gel sont ajoutées à la
fin pour tenir la conclusion sur la facture. Voir SCRIPT.md, section « Données
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
        # Le dernier plan déborde sur les quatre secondes de gel ajoutées en fin
        # de source : la facture reste à l'écran le temps de la conclusion.
        Segment("N1",  0.0,  3.6, "1 · Le solde de crédits"),
        Segment("N2",  3.6,  5.6, "2 · Crédits, formules, factures"),
        Segment("N3",  5.6,  8.2, "3 · Mes factures"),
        Segment("N4",  8.2, 11.7, "4 · Recherche et filtres"),
        Segment("N5", 14.3, 16.2, "5 · Télécharger le PDF"),
        Segment("N6", 24.2, 27.6, "6 · La facture"),
    ],
)

if __name__ == "__main__":
    build_episode(EPISODE)
