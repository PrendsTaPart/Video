#!/usr/bin/env python3
"""Tutoriel 12 — Découvrir l'éditeur : trois formats et des modèles prêts à l'emploi.

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
    prompt="Génère un visuel carré pour un post Instagram : fond sombre, "
           "un casque audio, et l'accroche 50 % de remise.",
    outil="generate_image",
    resultat=[
        "visuel généré : 1080 × 1080",
        "style   : fond sombre, produit centré",
        "rangé dans la bibliothèque de la société 321",
        "crédits restants : 605,00 €",
        "",
        "→ list_all_files le retrouve, l'éditeur l'ajuste.",
    ],
    cible=RACINE / "composition" / "carte-version-minute.png",
)

EPISODE = Episode(
    slug="decouvrir-l-editeur",
    numero=12,
    titre="Découvrir l'éditeur : trois formats et des modèles prêts à l'emploi",
    titre_court="Découvrir l'éditeur",
    module="Éditeur",
    promesse="À la fin de cette vidéo, vous savez ce que propose l'éditeur de "
             "RapidoCMS, et par quel point d'entrée commencer selon ce que "
             "vous voulez créer.",
    source=RACINE.parent / "_sources" / "EDITEUR_CMS.mp4",
    suivant="Choisir un template de post",
    voix_fin="Retenez ceci : trois formats, des modèles prêts à l'emploi, et "
             "un historique qui se remplira. Dans la prochaine vidéo, on "
             "choisit un template de post.",
    vignette_a=13.0,
    pose_vignette="decouverte",
    mot_cle="éditeur",
    racine=RACINE,
    plans=[
        Plan("N1", 12.0, 16.0,
             "Créer un visuel propre sans logiciel de design ni allers-retours "
             "par mail : RapidoCMS a son éditeur intégré, et il commence ici.",
             chapitre="La page Éditeur", pose="decouverte"),
        Plan("N2", 12.0, 16.0,
             "Nous sommes dans RapidoCMS, rubrique Éditeur, page Templates. "
             "Trois blocs se succèdent, du plus général au plus personnel."),
        Plan("N3", 24.0, 28.0,
             "Le menu de gauche regroupe quatre entrées sous Éditeur : les "
             "templates, la carte digitale, la bibliothèque et les prompts. "
             "Nous restons sur la première."),
        Plan("N4", 16.0, 20.0,
             "Le premier bloc s'appelle « Designer dans l'éditeur ». Trois "
             "points d'entrée : « Carte de visite », « Cartes NFC », et "
             "« Poste ».",
             chapitre="Designer dans l'éditeur", pose="presente-paume",
             zoom=True),
        Plan("N5", 16.0, 20.0,
             "« Carte de visite » est le point d'entrée des cartes "
             "professionnelles : votre nom, votre logo, vos coordonnées, au "
             "format d'une carte.", zoom=True),
        Plan("N6", 24.0, 28.0,
             "« Cartes NFC » vise la carte qu'on approche d'un téléphone. Même "
             "logique de mise en page, mais destinée à être partagée sans "
             "papier.", zoom=True),
        Plan("N7", 28.0, 32.0,
             "« Poste » est le troisième point d'entrée : les visuels destinés "
             "à vos publications, aux dimensions des réseaux sociaux.",
             zoom=True),
        Plan("N8", 32.0, 36.0,
             "En dessous, « Proposition pour vous » aligne trois vignettes, "
             "une par format : une carte de visite, une carte NFC, un visuel "
             "de post.",
             chapitre="Les modèles proposés", pose="dossier"),
        Plan("N9", 36.0, 40.0,
             "Ce sont des modèles prêts à l'emploi. Vous partirez de l'un "
             "d'eux et remplacerez textes, images et couleurs, plutôt que "
             "d'ouvrir une page blanche.", zoom=True),
        Plan("N10", 48.0, 52.0,
             "Tout en bas, la section de vos derniers designs. Sur ce compte "
             "de démonstration, elle est vide : aucune donnée à afficher.",
             chapitre="Vos derniers designs", pose="reflexion"),
        Plan("N11", 50.0, 53.0,
             "Dès votre première création enregistrée, elle listera vos "
             "visuels récents, et vous les rouvrirez d'un clic pour les "
             "modifier."),
        Plan("N12", 0.0, 0.0,
             "L'éditeur reste utile pour ajuster une mise en page. Mais pour "
             "obtenir un visuel de départ, une phrase suffit.",
             chapitre="La Version Minute", pose="laptop", image=CARTE),
        Plan("N13", 0.0, 0.0,
             "L'outil generate image du MCP RapidoCMS produit l'image et la "
             "range dans votre bibliothèque. Vous l'ouvrez ensuite dans "
             "l'éditeur pour l'ajuster.", image=CARTE),
        Plan("N14", 32.0, 36.0,
             "L'astuce : choisissez le format avant le design. Un visuel pensé "
             "pour une carte NFC ne se recadre pas proprement en post carré.",
             chapitre="L'astuce", pose="victoire", zoom=True),
    ],
)


if __name__ == "__main__":
    cli(EPISODE)
