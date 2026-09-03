#!/usr/bin/env python3
"""Tutoriel 05 — Lire son tableau de bord : réseaux, abonnement, crédits.

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
    prompt="Donne-moi les performances de mes publications RapidoCMS, "
           "plateforme par plateforme.",
    outil="post_insights",
    resultat=[
        "société    : 321 — KEBAIL-ALI",
        "LinkedIn   : 1 post — 0 j'aime, 0 commentaire",
        "Facebook   : 0 post",
        "Instagram  : 0 post",
        "",
        "→ taux d'engagement : 0 % — trop peu de données.",
    ],
    cible=RACINE / "composition" / "carte-version-minute.png",
)
CARTE_DEMANDE = CARTE.with_name(CARTE.stem + "-demande.png")

EPISODE = Episode(
    slug="lire-son-tableau-de-bord",
    numero=5,
    titre="Lire son tableau de bord : réseaux, abonnement, crédits",
    titre_court="Lire son tableau de bord",
    module="Prise en main",
    promesse="À la fin de cette vidéo, vous savez ce que chacune des trois "
             "sections du tableau de bord vous dit.",
    source=RACINE.parent / "_sources" / "Affichage_des_statistiques_du_dashboard.mp4",
    suivant="Suivre son abonnement",
    voix_fin="Retenez ceci : trois sections, trois questions — ce qui a "
             "marché, ce qui reste, ce qui est consommé. Dans la prochaine "
             "vidéo, on suit votre abonnement.",
    vignette_a=32.0,
    pose_vignette="pointe-droite",
    mot_cle="tableau",
    racine=RACINE,
    plans=[
        Plan("N1", 8.0, 12.0,
             "Vous ouvrez RapidoCMS et vous ne savez pas où regarder. Le "
             "tableau de bord répond à trois questions, dans l'ordre, de haut "
             "en bas.",
             chapitre="Votre page d'accueil", pose="accueil", zoom=True),
        Plan("N2", 8.0, 12.0,
             "C'est la première entrée du menu de gauche, et la page sur "
             "laquelle vous arrivez à chaque connexion."),
        Plan("N3", 10.0, 14.0,
             "En haut, « Statistiques réseaux sociaux » : une carte par "
             "plateforme reliée à votre espace, Facebook, LinkedIn et "
             "Instagram.",
             chapitre="Les statistiques réseaux sociaux", pose="pointe-gauche",
             zoom=True),
        Plan("N4", 12.0, 16.0,
             "Chaque carte donne le nombre d'interactions, les j'aime, les "
             "commentaires, les partages, le taux d'engagement et le nombre de "
             "posts.", zoom=True),
        Plan("N5", 12.0, 16.0,
             "Sur ce compte de démonstration, tout est à zéro sauf un post "
             "côté LinkedIn. C'est un espace neuf, pas une panne.", zoom=True),
        Plan("N6", 10.0, 14.0,
             "À droite du titre, un sélecteur affiche « Tout ». Dans cette "
             "capture, il n'est jamais ouvert : il reste sur sa valeur par "
             "défaut.",
             chapitre="Le filtre Tout", pose="reflexion", zoom=True),
        Plan("N7", 28.0, 32.0,
             "En descendant, la carte d'abonnement, et l'offre en cours à "
             "côté : « Premium ». C'est elle qui fixe vos plafonds.",
             chapitre="Les statistiques d'abonnement", pose="dossier",
             zoom=True),
        Plan("N8", 30.0, 34.0,
             "Deux colonnes seulement : « Utilisé » et « Restant ». Cartes "
             "digitales, zéro sur dix. Comptes réseaux sociaux, huit sur dix.",
             zoom=True),
        Plan("N9", 30.0, 34.0,
             "C'est la ligne à surveiller : quand la barre arrive au bout, il "
             "faut libérer un compte ou passer à l'offre supérieure.",
             zoom=True),
        Plan("N10", 46.0, 50.0,
             "Tout en bas, les statistiques de crédit : un histogramme, un "
             "mois par colonne, une couleur par type de consommation.",
             chapitre="Les crédits", pose="presente-paume", zoom=True),
        Plan("N11", 46.0, 50.0,
             "La légende donne les quatre séries : image, texte, template et "
             "chatbot. Ici, une seule barre violette, en septembre : du texte.",
             zoom=True),
        Plan("N12", 44.0, 48.0,
             "Au fil des semaines, ce graphique vous dira où partent vos "
             "crédits, et lequel de vos usages vous coûte le plus cher.",
             zoom=True),
        Plan("N13", 0.0, 0.0,
             "Ces chiffres, vous pouvez les demander sans ouvrir la page ni "
             "faire défiler quoi que ce soit.",
             chapitre="La Version Minute", pose="laptop", image=CARTE_DEMANDE),
        Plan("N14", 0.0, 0.0,
             "Dans Claude, l'outil post insights du MCP RapidoCMS vous rend "
             "les performances de vos publications, plateforme par plateforme.",
             image=CARTE),
        Plan("N15", 24.0, 28.0,
             "L'astuce : lisez cette page de bas en haut. Les crédits et "
             "l'abonnement disent ce que vous pouvez encore faire ; les cartes "
             "du haut disent ce que ça a donné.",
             chapitre="L'astuce", pose="victoire", zoom=True),
    ],
)


if __name__ == "__main__":
    cli(EPISODE)
