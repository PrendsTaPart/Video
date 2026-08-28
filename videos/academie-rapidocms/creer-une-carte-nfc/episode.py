#!/usr/bin/env python3
"""Tutoriel 15 — Choisir un modèle de carte NFC dans la galerie de l'Éditeur.

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
    prompt="Liste-moi les modèles de carte NFC de RapidoCMS, et applique celui "
           "d'Instagram au format carte.",
    outil="list_card_templates",
    resultat=[
        "société  : 321 — KEBAIL-ALI",
        "formats  : Support NFC · Carte NFC",
        "réseaux  : Instagram · Facebook · FoodEatUp",
        "prix     : Gratuit — auteur Deker",
        "",
        "→ assign_card_template ouvre « Carte NFC Instagram » dans l'éditeur.",
    ],
    cible=RACINE / "composition" / "carte-version-minute.png",
)

EPISODE = Episode(
    slug="creer-une-carte-nfc",
    numero=15,
    titre="Choisir un modèle de carte NFC dans la galerie de l'Éditeur",
    titre_court="Modèles de carte NFC",
    module="Éditeur",
    promesse="À la fin de cette vidéo, vous triez la galerie de cartes NFC, "
             "vous distinguez les deux formats, et vous ouvrez le modèle de "
             "votre réseau dans l'éditeur.",
    source=RACINE.parent / "_sources" / "TEMPLATE_DE_CARTE_NFC.mp4",
    suivant="Créer une carte digitale",
    voix_fin="Retenez ceci : le modèle fait le visuel, pas la puce. Dans la "
             "prochaine vidéo, on crée une carte digitale.",
    vignette_a=52.0,
    pose_vignette="telephone",
    mot_cle="NFC",
    racine=RACINE,
    plans=[
        Plan("N1", 0.0, 4.0,
             "Un client vous suit sur Instagram d'un simple geste, sans taper "
             "votre nom. Ça commence par un visuel de carte NFC, déjà dessiné.",
             chapitre="La galerie NFC", pose="decouverte", zoom=True),
        Plan("N2", 0.5, 4.0,
             "Menu de gauche, section Éditeur, « Templates ». La galerie "
             "affiche « Proposition de thème de Cartes NFC pour vous »."),
        Plan("N3", 4.0, 8.0,
             "Le bouton « Filtre : Tout » ouvre un panneau de tri : par date "
             "croissante ou décroissante, de A à Z, de Z à A, puis "
             "« Appliquer ».",
             chapitre="Trier la galerie", pose="reflexion", zoom=True),
        Plan("N4", 4.5, 8.0,
             "Ici, ce tri est ouvert puis refermé sans être appliqué : la "
             "grille reste exactement dans son ordre d'origine.", zoom=True),
        Plan("N5", 24.0, 28.0,
             "Six modèles, deux formats : les « Support NFC », en grand, et "
             "les « Carte NFC », au format poche. Instagram, Facebook, "
             "FoodEatUp.",
             chapitre="Le catalogue par usage", pose="presente-paume"),
        Plan("N6", 40.0, 44.0,
             "Sous la vignette « Carte NFC Instagram », le bouton « Choisir ce "
             "modèle » devient bleu plein dès que vous le survolez.", zoom=True),
        Plan("N7", 48.0, 52.0,
             "La fenêtre « Acheter un template » affiche le badge vert "
             "« Gratuit », le nom du modèle, sa description et ses mots-clés "
             "sous « Tag ».",
             chapitre="La fiche du modèle", pose="pointe-droite", zoom=True),
        Plan("N8", 48.5, 52.0,
             "En bas à droite, « Utiliser ce template » ouvre le modèle dans "
             "l'éditeur de personnalisation.", zoom=True),
        Plan("N9", 52.0, 56.0,
             "Le voilà : dégradé rose, logo Instagram, pictogramme NFC, le "
             "titre « Suivez-nous », l'identifiant du compte, et le grand QR "
             "code.",
             chapitre="Personnaliser la carte", pose="laptop"),
        Plan("N10", 56.0, 60.0,
             "Cliquez sur le logo : cadre bleu, étiquette « Image ». Texte, "
             "image ou conteneur, chaque élément se sélectionne de la même "
             "façon.", zoom=True),
        Plan("N11", 64.0, 68.0,
             "À droite, la bibliothèque de blocs : QR code, Cartes, et les "
             "blocs de base — citation, section de texte, texte, image.",
             zoom=True),
        Plan("N12", 52.5, 56.0,
             "À cet écran, vous dessinez le visuel. Le lien du QR code et "
             "l'encodage de la puce NFC, eux, se règlent ailleurs, plus tard."),
        Plan("N13", 0.0, 0.0,
             "Et si vous n'aviez pas à parcourir la galerie pour savoir quel "
             "modèle NFC existe déjà ?",
             chapitre="La Version Minute", pose="laptop", image=CARTE),
        Plan("N14", 0.0, 0.0,
             "Dans Claude, l'outil list card templates du MCP RapidoCMS vous "
             "les liste, et assign card template applique celui que vous "
             "voulez.", image=CARTE),
        Plan("N15", 24.0, 28.0,
             "L'astuce : choisissez le format avant le réseau. Un « Support "
             "NFC » se pose sur un comptoir, une « Carte NFC » se glisse dans "
             "une poche.",
             chapitre="L'astuce", pose="victoire", zoom=True),
    ],
)


if __name__ == "__main__":
    cli(EPISODE)
