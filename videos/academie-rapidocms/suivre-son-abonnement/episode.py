#!/usr/bin/env python3
"""Tutoriel 06 — Suivre son abonnement : lire l'historique et repérer l'échéance.

Le script validé est dans `SCRIPT.md` : ce fichier ne fait que le mettre en
données. La voix off n'est pas réécrite ici.

    python3 episode.py
"""

import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent
sys.path.insert(0, str(RACINE.parent))

from studio import Episode, Plan                              # noqa: E402
from studio.habillage import carte_version_minute             # noqa: E402
from studio.voix_eleven import cli                            # noqa: E402

CARTE = carte_version_minute(
    prompt="Rappelle-moi quelle société pilote mon espace RapidoCMS, "
           "avant que je vérifie mon abonnement.",
    outil="get_company",
    resultat=[
        "société : 321 — KEBAIL-ALI",
        "espace  : RapidoCMS",
        "comptes : Facebook, LinkedIn, Instagram connectés",
        "",
        "→ nom, type, prix et dates d'expiration se lisent",
        "  sur la page « Abonnement ».",
    ],
    cible=RACINE / "composition" / "carte-version-minute.png",
)
CARTE_DEMANDE = CARTE.with_name(CARTE.stem + "-demande.png")

EPISODE = Episode(
    slug="suivre-son-abonnement",
    numero=6,
    titre="Suivre son abonnement : lire l'historique et repérer l'échéance",
    titre_court="Suivre son abonnement",
    module="Abonnement & crédits",
    promesse="À la fin de cette vidéo, vous savez lire le tableau de vos "
             "abonnements et dire jusqu'à quand votre plan court.",
    source=RACINE.parent / "_sources" / "Historique_des_abonnements.mp4",
    suivant="Acheter crédits et stockage",
    voix_fin="Retenez ceci : c'est la date d'expiration qui fait foi. Dans la "
             "prochaine vidéo, on achète des crédits et du stockage.",
    vignette_a=2.0,
    pose_vignette="dossier",
    mot_cle="abonnement",
    racine=RACINE,
    plans=[
        Plan("N1", 0.0, 4.0,
             "Votre plan RapidoCMS se termine un jour, et personne ne vous "
             "prévient. Cette page vous donne la date exacte, en une ligne.",
             chapitre="L'échéance qu'on ne voit pas venir", pose="reflexion",
             zoom=True),
        Plan("N2", 0.0, 4.0,
             "On est sur la page « Abonnement », affichée en pleine largeur. "
             "En haut à droite, votre solde, « 605.00€ », et un bouton bleu "
             "« Acheter un abonnement »."),
        Plan("N3", 12.0, 16.0,
             "Trois onglets se partagent la page : « Historique d'abonnement », "
             "« Packs », et « Dépenses crédit ». On reste sur le premier.",
             chapitre="Les trois onglets", pose="pointe-droite", zoom=True),
        Plan("N4", 20.0, 24.0,
             "Les deux autres servent à acheter des ressources et à suivre ce "
             "que vos actions consomment. C'est le sujet de la vidéo suivante.",
             zoom=True),
        Plan("N5", 28.0, 32.0,
             "Le tableau a cinq colonnes : le nom, le type, le prix, la date "
             "d'achat et la date d'expiration. Une ligne par abonnement "
             "souscrit.",
             chapitre="Lire le tableau", pose="laptop"),
        Plan("N6", 32.0, 36.0,
             "Première ligne : « Premium », de type « annuel », au prix de neuf "
             "cent quatre-vingt-dix-neuf, acheté le 23 août 2025 et valable "
             "jusqu'au 23 août 2026.", zoom=True),
        Plan("N7", 36.0, 40.0,
             "Deuxième ligne : « Essai », mensuel, à zéro, du 23 août au "
             "23 septembre 2025. Les deux dates encadrent la période couverte.",
             zoom=True),
        Plan("N8", 32.0, 36.0,
             "Il n'y a pas de colonne de statut : c'est la date d'expiration, "
             "et elle seule, qui vous dit si le plan court encore.", zoom=True),
        Plan("N9", 8.0, 12.0,
             "Au-dessus, deux champs de date au format jour, mois, année, et "
             "une recherche par nom : de quoi retrouver une ligne quand la "
             "liste s'allonge.",
             chapitre="Filtrer la liste", pose="pointe-gauche", zoom=True),
        Plan("N10", 28.0, 32.0,
             "Pour renouveler ou passer à une formule supérieure, tout part du "
             "bouton bleu « Acheter un abonnement », en haut à droite.",
             chapitre="Renouveler ou changer d'offre", pose="presente-paume",
             zoom=True),
        Plan("N11", 8.0, 12.0,
             "Vous y comparerez ensuite les formules disponibles avant de "
             "valider. Cet écran vient après le clic : il n'est pas dans cette "
             "vidéo."),
        Plan("N12", 0.0, 0.0,
             "Vous n'avez pas toujours envie d'ouvrir la page pour savoir sur "
             "quelle société tourne votre espace.",
             chapitre="La Version Minute", pose="laptop", image=CARTE_DEMANDE),
        Plan("N13", 0.0, 0.0,
             "Dans Claude, l'outil get company du MCP RapidoCMS vous renvoie la "
             "fiche de votre entreprise. Une phrase, une réponse.", image=CARTE),
        Plan("N14", 36.0, 40.0,
             "L'astuce : reportez la date d'expiration la plus proche dans "
             "votre agenda, avec un rappel quinze jours avant. Le tableau, lui, "
             "ne vous préviendra pas.",
             chapitre="L'astuce", pose="victoire", zoom=True),
    ],
)


if __name__ == "__main__":
    cli(EPISODE)
