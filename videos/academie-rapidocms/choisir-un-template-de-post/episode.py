#!/usr/bin/env python3
"""Tutoriel 13 — Choisir un template de post et l'ouvrir dans l'éditeur.

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
    prompt="Enregistre ce visuel comme template de post réutilisable, "
           "nommé « Promo produit — fond sombre ».",
    outil="create_post_template",
    resultat=[
        "template : « Promo produit — fond sombre »",
        "format   : 1080 × 1080 · statut : gratuit",
        "tags     : promotion, lancement, produit",
        "visible dans Éditeur → Templates",
        "",
        "→ create_draft_tool le reprend pour un post.",
    ],
    cible=RACINE / "composition" / "carte-version-minute.png",
)
CARTE_DEMANDE = CARTE.with_name(CARTE.stem + "-demande.png")

EPISODE = Episode(
    slug="choisir-un-template-de-post",
    numero=13,
    titre="Choisir un template de post et l'ouvrir dans l'éditeur",
    titre_court="Choisir un template de post",
    module="Éditeur",
    promesse="À la fin de cette vidéo, vous savez choisir un modèle de visuel "
             "dans la galerie, lire sa fiche, et reconnaître l'éditeur qui "
             "s'ouvre derrière.",
    source=RACINE.parent / "_sources"
    / "Creation_des_postes_pour_les_r_seaux_sociaux.mp4",
    suivant="Créer une carte de visite",
    voix_fin="Retenez ceci : un modèle bien choisi fait la moitié du travail. "
             "Dans la prochaine vidéo, on crée une carte de visite.",
    vignette_a=28.0,
    pose_vignette="presente-paume",
    mot_cle="template",
    racine=RACINE,
    plans=[
        Plan("N1", 16.0, 20.0,
             "Partir d'une page blanche pour un visuel de post, c'est long. "
             "Partir d'un modèle déjà composé, c'est deux minutes.",
             chapitre="La galerie de modèles", pose="decouverte"),
        Plan("N2", 16.0, 20.0,
             "Nous sommes dans RapidoCMS, Éditeur, page Templates : une grille "
             "de modèles de post, proposés selon vos besoins."),
        Plan("N3", 20.0, 24.0,
             "Chaque carte montre un aperçu, le nom du modèle — « Produit "
             "Casque écouteurs », « Produit Canapé », « Produit Drone » — et "
             "le bouton « Choisir ce modèle ».", zoom=True),
        Plan("N4", 20.0, 24.0,
             "En haut, un filtre et un champ de recherche vous aideront à "
             "cibler quand la galerie s'allongera."),
        Plan("N5", 28.0, 32.0,
             "« Choisir ce modèle » n'applique rien : il ouvre la fiche du "
             "modèle par-dessus la grille, avec son visuel en grand.",
             chapitre="La fiche du modèle", pose="dossier", zoom=True),
        Plan("N6", 32.0, 36.0,
             "On y lit son statut — ici le badge vert « Gratuit » —, sa "
             "description, et ses tags : Instagram, promotion, lancement, "
             "événement.", zoom=True),
        Plan("N7", 32.0, 36.0,
             "Ces tags disent à quoi le modèle est destiné. Lisez-les : ils "
             "vous évitent de charger un visuel calibré pour un tout autre "
             "usage."),
        Plan("N8", 40.0, 44.0,
             "Le bouton « Utiliser ce template » passe en bleu au survol. Il "
             "charge le modèle et bascule sur l'éditeur de personnalisation.",
             chapitre="Ouvrir le modèle", pose="pointe-droite", zoom=True),
        Plan("N9", 44.0, 48.0,
             "Le visuel occupe le centre. En haut à gauche, trois aperçus : "
             "bureau, tablette, mobile. En haut à droite, la barre d'outils : "
             "annuler, rétablir, télécharger, enregistrer.",
             chapitre="L'éditeur de personnalisation", pose="laptop"),
        Plan("N10", 48.0, 52.0,
             "Un clic sur un élément l'entoure d'un cadre bleu : c'est lui que "
             "vous modifiez. Dans la capture, la sélection est montrée, mais "
             "aucun texte n'est réellement changé.", zoom=True),
        Plan("N11", 52.0, 56.0,
             "À droite, la section « Postes » propose trois formats de visuel, "
             "dont un huit cents par six cents : vous choisissez celui du "
             "réseau visé.",
             chapitre="Formats et blocs", pose="checklist", zoom=True),
        Plan("N12", 52.0, 56.0,
             "En dessous, les blocs de base — « Quote », « Text section », "
             "« Text », « Image » — que vous glisserez dans le visuel pour "
             "compléter la mise en page.", zoom=True),
        Plan("N13", 0.0, 0.0,
             "La capture s'arrête là : rien n'est enregistré, rien n'est "
             "publié. Voici comment aller plus vite sur la partie modèle.",
             chapitre="La Version Minute", pose="presente-paume", image=CARTE_DEMANDE),
        Plan("N14", 0.0, 0.0,
             "L'outil create post template du MCP RapidoCMS enregistre votre "
             "visuel comme modèle réutilisable. Vous le rappelez ensuite à "
             "chaque publication.", image=CARTE),
        Plan("N15", 44.0, 48.0,
             "L'astuce : fixez le format avant de retoucher les textes. "
             "Changer de dimensions après coup vous oblige à repositionner "
             "chaque bloc.",
             chapitre="L'astuce", pose="victoire", zoom=True),
    ],
)


if __name__ == "__main__":
    cli(EPISODE)
