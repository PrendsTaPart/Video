#!/usr/bin/env python3
"""Tutoriel 10 — Lire la page Historique, même quand elle est vide.

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
    prompt="Montre-moi mes publications passées sur Facebook, LinkedIn et "
           "Instagram, avec leurs statistiques.",
    outil="post_insights",
    resultat=[
        "société   : 321 — KEBAIL-ALI",
        "Facebook  : 0 publication",
        "LinkedIn  : 1 publication",
        "Instagram : 0 publication",
        "",
        "→ les statistiques arrivent dès la première publication.",
    ],
    cible=RACINE / "composition" / "carte-version-minute.png",
)
CARTE_DEMANDE = CARTE.with_name(CARTE.stem + "-demande.png")

EPISODE = Episode(
    slug="consulter-l-historique-des-publications",
    numero=10,
    titre="Lire la page Historique, même quand elle est vide",
    titre_court="Consulter l'historique des publications",
    module="Communication",
    promesse="À la fin de cette vidéo, vous savez où retrouver vos "
             "publications passées et en attente, et quoi faire quand la page "
             "reste vide.",
    source=RACINE.parent / "_sources"
    / "Historique_des_publications_sur_les_r_seaux_sociaux.mp4",
    suivant="Lancer une campagne",
    voix_fin="Retenez ceci : le compteur des tuiles avant les filtres. Dans la "
             "prochaine vidéo, on lance une campagne.",
    vignette_a=13.0,
    pose_vignette="decouverte",
    mot_cle="historique",
    racine=RACINE,
    plans=[
        Plan("N1", 8.0, 12.0,
             "Est-ce que ce post est parti ? Sur quel réseau, et quand ? La "
             "page « Historique » est faite pour cette question-là.",
             chapitre="Ce qui est déjà parti", pose="reflexion", zoom=True),
        Plan("N2", 8.0, 12.0,
             "Menu latéral, rubrique CMS, entrée « Historique ». Elle "
             "rassemble vos publications passées et celles encore en attente."),
        Plan("N3", 10.0, 14.0,
             "En haut, trois tuiles : Facebook, LinkedIn, Instagram. Chacune "
             "porte un compteur — ici zéro, un, et zéro.",
             chapitre="Choisir le réseau", pose="pointe-droite", zoom=True),
        Plan("N4", 12.0, 16.0,
             "Un clic sur Instagram : la tuile s'encadre de bleu, c'est le "
             "réseau affiché en dessous. Son compteur reste à zéro.", zoom=True),
        Plan("N5", 16.0, 20.0,
             "Retour sur Facebook d'un clic. C'est ce sélecteur qui commande "
             "tout le contenu de la page."),
        Plan("N6", 16.0, 20.0,
             "Sous les tuiles, la ligne de filtres : une liste « Compte » pour "
             "choisir la page ou la marque, deux champs de date, et une "
             "recherche.",
             chapitre="Filtrer la liste", pose="pointe-gauche", zoom=True),
        Plan("N7", 18.0, 22.0,
             "Les deux dates encadrent une période. Elles restent vides ici : "
             "rien n'est filtré, on voit donc tout ce que le réseau contient.",
             zoom=True),
        Plan("N8", 20.0, 24.0,
             "Trois sous-onglets ensuite : toutes les publications, les "
             "publiées, et celles en attente. Le premier est actif.",
             chapitre="Publiées ou en attente", pose="checklist", zoom=True),
        Plan("N9", 20.0, 24.0,
             "C'est là que vous séparez ce qui est déjà parti de ce qui attend "
             "son créneau. Cette capture ne les quitte jamais."),
        Plan("N10", 12.0, 16.0,
             "Au centre, un message : « Il n'y a actuellement aucune donnée à "
             "afficher ». Il ne bouge pas d'un bout à l'autre de la vidéo.",
             chapitre="Quand la page reste vide", pose="stop", zoom=True),
        Plan("N11", 14.0, 18.0,
             "Ce n'est pas une erreur : le réseau sélectionné n'a rien publié. "
             "La seule publication du compte est sur LinkedIn, jamais ouvert "
             "ici.", zoom=True),
        Plan("N12", 0.0, 0.0,
             "Tant que la liste est vide, l'écran ne vous apprend rien. Une "
             "question suffit à faire le tour.",
             chapitre="La Version Minute", pose="laptop", image=CARTE_DEMANDE),
        Plan("N13", 0.0, 0.0,
             "Dans Claude, l'outil post insights du MCP RapidoCMS vous ramène "
             "vos publications et leurs chiffres, réseau par réseau.",
             image=CARTE),
        Plan("N14", 12.0, 16.0,
             "L'astuce : lisez d'abord les compteurs des trois tuiles. S'ils "
             "sont à zéro, inutile de toucher aux filtres : c'est le réseau "
             "qu'il faut changer.",
             chapitre="L'astuce", pose="victoire", zoom=True),
    ],
)


if __name__ == "__main__":
    cli(EPISODE)
