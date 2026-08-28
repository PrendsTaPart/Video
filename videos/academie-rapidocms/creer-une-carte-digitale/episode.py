#!/usr/bin/env python3
"""Tutoriel 16 — La page Carte digitale : quota, liste et formulaire d'ajout.

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
    prompt="Crée-moi une carte digitale « Accueil boutique » pour mon "
           "commercial, et ajoute-lui le lien de mon site.",
    outil="add_digital_card",
    resultat=[
        "société  : 321 — KEBAIL-ALI",
        "carte    : « Accueil boutique » — créée",
        "quota    : 1 carte sur 10 autorisées",
        "liste    : 1 entrée, l'anneau n'est plus tout vert",
        "",
        "→ add_card_page_link y accroche le site et les réseaux.",
    ],
    cible=RACINE / "composition" / "carte-version-minute.png",
)

EPISODE = Episode(
    slug="creer-une-carte-digitale",
    numero=16,
    titre="La page Carte digitale : quota, liste et formulaire d'ajout",
    titre_court="La page Carte digitale",
    module="Éditeur",
    promesse="À la fin de cette vidéo, vous lisez votre quota de cartes "
             "digitales, vous comprenez l'anneau des statistiques, et vous "
             "savez ce que le formulaire d'ajout attend de vous.",
    source=RACINE.parent / "_sources" / "cartedigital_CMS.mp4",
    suivant="",
    voix_fin="Retenez ceci : dix cartes, une liste, un formulaire. Vous avez "
             "fait le tour du module Éditeur — la suite de l'Académie "
             "RapidoCMS vous attend.",
    vignette_a=33.0,
    pose_vignette="presente-paume",
    mot_cle="digitale",
    racine=RACINE,
    plans=[
        Plan("N1", 24.0, 27.0,
             "Une carte de visite qui ne s'imprime pas, qui se partage en une "
             "seconde et se corrige à tout moment : la carte digitale.",
             chapitre="La page Carte digitale", pose="decouverte", zoom=True),
        Plan("N2", 24.5, 27.5,
             "Menu de gauche, section Éditeur : l'entrée « Carte digitale » "
             "ouvre la page qui recense toutes vos cartes."),
        Plan("N3", 25.0, 28.0,
             "En haut, la section « Statistiques ». À gauche, votre quota : "
             "sur ce compte, dix cartes digitales autorisées, pas une de plus.",
             chapitre="Vos statistiques", pose="pointe-gauche", zoom=True),
        Plan("N4", 24.0, 27.0,
             "Au centre, un anneau partage les cartes créées et les cartes "
             "restantes. Ici il est entièrement vert : aucune carte n'existe "
             "encore.", zoom=True),
        Plan("N5", 24.5, 27.5,
             "Plus bas, la « Liste des cartes ». Vide pour l'instant, elle "
             "affichera chaque carte enregistrée dès que vous en créerez une.",
             chapitre="La liste des cartes", pose="dossier"),
        Plan("N6", 28.0, 31.5,
             "En haut à droite, un seul bouton d'action : « Créer une carte ». "
             "Il passe en bleu plein au survol.",
             chapitre="Créer une carte", pose="pointe-droite", zoom=True),
        Plan("N7", 29.0, 32.0,
             "Le champ « Chercher », à gauche, ne servira que le jour où cette "
             "liste comptera plusieurs cartes.", zoom=True),
        Plan("N8", 32.0, 35.5,
             "La fenêtre « Ajouter une carte » s'ouvre. Six champs : le nom de "
             "la carte, puis le nom et le prénom du propriétaire.",
             chapitre="Le formulaire", pose="checklist", zoom=True),
        Plan("N9", 33.0, 36.0,
             "Ensuite l'adresse e-mail, le numéro de téléphone, et une zone "
             "libre pour les informations supplémentaires que vous voulez "
             "inclure.", zoom=True),
        Plan("N10", 45.0, 48.5,
             "À l'écran, le formulaire reste vide : la démonstration ne "
             "remplit rien. Chez vous, c'est à ce moment que vous saisissez "
             "vos données.", zoom=True),
        Plan("N11", 46.5, 50.0,
             "Le bouton bleu « Ajouter », en bas, enregistre la carte. Elle "
             "rejoint alors la liste, et l'anneau des statistiques change de "
             "couleur.", zoom=True),
        Plan("N12", 0.0, 0.0,
             "Six champs à taper et une fenêtre à ouvrir : c'est exactement le "
             "genre de chose qu'une seule phrase remplace.",
             chapitre="La Version Minute", pose="laptop", image=CARTE),
        Plan("N13", 0.0, 0.0,
             "Dans Claude, l'outil add digital card du MCP RapidoCMS crée la "
             "carte, et add card page link y accroche vos liens.", image=CARTE),
        Plan("N14", 28.0, 31.5,
             "L'astuce : nommez vos cartes par usage, « Accueil », « Salon », "
             "« Terrain », plutôt que par personne. Avec dix cartes au "
             "maximum, vous saurez laquelle rééditer.",
             chapitre="L'astuce", pose="victoire", zoom=True),
    ],
)


if __name__ == "__main__":
    cli(EPISODE)
