#!/usr/bin/env python3
"""Tutoriel 14 — Choisir un modèle de carte de visite et l'ouvrir dans l'éditeur.

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
    prompt="Montre-moi les modèles de carte de visite disponibles dans "
           "RapidoCMS, et applique-moi celui du photographe.",
    outil="list_card_templates",
    resultat=[
        "société  : 321 — KEBAIL-ALI",
        "modèles  : Ressources humaines · Photographer · Immobilier",
        "           Webmaster · Graphiste · Graphiste version 2",
        "prix     : Gratuit — auteur Deker",
        "",
        "→ assign_card_template ouvre « Photographer » dans l'éditeur.",
    ],
    cible=RACINE / "composition" / "carte-version-minute.png",
)
CARTE_DEMANDE = CARTE.with_name(CARTE.stem + "-demande.png")

EPISODE = Episode(
    slug="creer-une-carte-de-visite",
    numero=14,
    titre="Choisir un modèle de carte de visite et l'ouvrir dans l'éditeur",
    titre_court="Modèles de carte de visite",
    module="Éditeur",
    promesse="À la fin de cette vidéo, vous repérez le bon modèle de carte de "
             "visite, vous lisez sa fiche, et vous savez où le personnaliser.",
    source=RACINE.parent / "_sources" / "Templates_de_cartes_de_visite.mp4",
    suivant="Créer une carte NFC",
    voix_fin="Retenez ceci : un bon modèle vous fait gagner une journée de "
             "design. Dans la prochaine vidéo, on passe aux cartes NFC.",
    vignette_a=32.0,
    pose_vignette="decouverte",
    mot_cle="modèle",
    racine=RACINE,
    plans=[
        Plan("N1", 28.0, 31.5,
             "Une carte de visite à faire, aucun logiciel de design, pas le "
             "temps. Dans RapidoCMS, vous partez d'un modèle déjà dessiné.",
             chapitre="La galerie de modèles", pose="decouverte", zoom=True),
        Plan("N2", 29.0, 32.0,
             "Menu de gauche, section Éditeur, entrée « Templates ». La "
             "galerie s'ouvre sur « Proposition de thème de Carte de visite "
             "pour vous »."),
        Plan("N3", 28.0, 31.5,
             "Six modèles y sont proposés, tous signés « Deker » : Ressources "
             "humaines, Photographer, Immobilier, Webmaster, Graphiste, et "
             "Graphiste version deux.", zoom=True),
        Plan("N4", 29.0, 32.0,
             "Prenez celui qui parle de votre métier. Sous chaque vignette, un "
             "seul bouton, et il devient bleu au survol : « Choisir ce "
             "modèle ».",
             chapitre="Choisir son modèle", pose="pointe-droite", zoom=True),
        Plan("N5", 40.0, 43.5,
             "La fenêtre qui s'ouvre présente le modèle : un badge vert "
             "« Gratuit », son nom, sa description complète, et ses mots-clés "
             "regroupés sous « Tag ».",
             chapitre="La fiche du modèle", pose="reflexion", zoom=True),
        Plan("N6", 41.0, 44.0,
             "La description dit à quel usage le modèle est pensé. Si elle "
             "vous convient, le bouton « Utiliser ce template » l'ouvre dans "
             "l'éditeur.", zoom=True),
        Plan("N7", 44.0, 48.0,
             "Le voilà ouvert dans l'éditeur de personnalisation, recto "
             "d'abord : le nom, le métier, le téléphone, l'e-mail, la ville et "
             "le site web.",
             chapitre="L'éditeur", pose="laptop"),
        Plan("N8", 48.0, 52.0,
             "Un clic sur un texte le sélectionne : cadre bleu, étiquette "
             "« Texte ». Vous remplacez alors le contenu du modèle par le "
             "vôtre.", zoom=True),
        Plan("N9", 52.0, 56.0,
             "Faites défiler le canevas pour atteindre le verso. L'image et le "
             "QR code s'y sélectionnent de la même façon, d'un simple clic.",
             zoom=True),
        Plan("N10", 56.0, 60.0,
             "À droite, dès qu'un élément est sélectionné, le panneau bascule "
             "en propriétés : Général, Dimension, Typographie, Décorations. "
             "Tout se règle là.",
             chapitre="Le panneau de droite", pose="pointe-droite", zoom=True),
        Plan("N11", 60.0, 62.5,
             "Sans sélection, ce même panneau redevient une bibliothèque de "
             "blocs : QR code, Cartes, et les blocs de base — citation, texte, "
             "image.", zoom=True),
        Plan("N12", 0.0, 0.0,
             "Avant même d'ouvrir la galerie, vous pouvez savoir quels modèles "
             "existent, sans faire défiler une seule vignette.",
             chapitre="La Version Minute", pose="laptop", image=CARTE_DEMANDE),
        Plan("N13", 0.0, 0.0,
             "Dans Claude, l'outil list card templates du MCP RapidoCMS vous "
             "les liste, et assign card template applique celui que vous avez "
             "choisi.", image=CARTE),
        Plan("N14", 40.0, 43.5,
             "L'astuce : relevez les mots-clés du bloc « Tag » d'un modèle qui "
             "vous plaît, puis tapez-les dans « Chercher une page ». Vous "
             "retrouvez ses voisins en une recherche.",
             chapitre="L'astuce", pose="victoire", zoom=True),
    ],
)


if __name__ == "__main__":
    cli(EPISODE)
