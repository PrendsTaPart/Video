#!/usr/bin/env python3
"""Tutoriel 08 — Créer un post : la page Réseaux sociaux et son formulaire.

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
    prompt="Prépare un brouillon de post Facebook pour le compte "
           "Cocuisinage By Foodeatup, sur le thème de la rentrée.",
    outil="create_draft_tool",
    resultat=[
        "brouillon : « Rentrée — Cocuisinage »",
        "réseau    : Facebook",
        "compte    : Cocuisinage By Foodeatup",
        "type      : texte · statut : brouillon",
        "",
        "→ list_drafts_tool le retrouve dans la liste.",
    ],
    cible=RACINE / "composition" / "carte-version-minute.png",
)

EPISODE = Episode(
    slug="creer-un-post-reseaux-sociaux",
    numero=8,
    titre="Créer un post : la page Réseaux sociaux et son formulaire",
    titre_court="Créer un post",
    module="Communication",
    promesse="À la fin de cette vidéo, vous savez où se crée un post dans "
             "RapidoCMS et ce que demande le formulaire, champ par champ.",
    source=RACINE.parent / "_sources" / "comunication_resaux_socieaux.mp4",
    suivant="Piloter le calendrier éditorial",
    voix_fin="Retenez ceci : un nom, un réseau, un compte, un type — et le "
             "post est prêt à écrire. Dans la prochaine vidéo, on pilote le "
             "calendrier éditorial.",
    vignette_a=40.0,
    pose_vignette="presente-paume",
    mot_cle="post",
    racine=RACINE,
    plans=[
        Plan("N1", 8.0, 12.0,
             "Publier sur Facebook, LinkedIn et Instagram sans jongler entre "
             "trois applications : tout part d'une seule page, et d'un seul "
             "bouton.",
             chapitre="La page Réseaux sociaux", pose="decouverte"),
        Plan("N2", 8.0, 12.0,
             "Nous sommes dans RapidoCMS, rubrique Communication, page Réseaux "
             "sociaux. Trois onglets séparent vos publications par réseau : "
             "Facebook, LinkedIn, Instagram."),
        Plan("N3", 12.0, 16.0,
             "Sur ce compte de démonstration, chaque onglet est vide : « Il "
             "n'y a actuellement aucune donnée à afficher ». Vos posts "
             "viendront s'y ranger, réseau par réseau.", zoom=True),
        Plan("N4", 16.0, 20.0,
             "L'onglet actif est souligné en bleu. Vous changez d'onglet pour "
             "vérifier ce qui est prévu sur un réseau précis, sans quitter la "
             "page."),
        Plan("N5", 20.0, 24.0,
             "Le bouton « Créer un poste » est en haut à droite. C'est le seul "
             "point d'entrée : il ouvre le formulaire à la place de la liste.",
             chapitre="Créer un poste", pose="pointe-droite", zoom=True),
        Plan("N6", 24.0, 28.0,
             "Deux colonnes. À gauche le paramétrage, à droite l'aperçu : une "
             "maquette de post avec « J'aime », « Commenter » et « Partager »."),
        Plan("N7", 30.0, 34.0,
             "Premier champ, le nom du poste. Ici, « Test ». Ce nom est "
             "interne : il sert à retrouver le post dans la liste, il n'est "
             "jamais publié.",
             chapitre="Nommer et choisir le réseau", pose="checklist",
             zoom=True),
        Plan("N8", 34.0, 38.0,
             "Deuxième champ, « Choisir un réseau social ». La liste propose "
             "vos réseaux connectés ; on retient Facebook.", zoom=True),
        Plan("N9", 38.0, 42.0,
             "Troisième champ, « Choisir un compte » : ici « Cocuisinage By "
             "Foodeatup ». L'aperçu se met à jour en direct, avec le nom de la "
             "page et la mention « Maintenant ».",
             chapitre="Le compte et le type", pose="pointe-gauche", zoom=True),
        Plan("N10", 42.0, 46.0,
             "Quatrième champ, « Type de poste » : « Texte ». Le cadre image "
             "disparaît de l'aperçu, et un champ de rédaction s'ouvre plus "
             "bas.", zoom=True),
        Plan("N11", 44.0, 48.0,
             "Ce champ accueille votre message. À côté apparaît « Aide du "
             "bot », que cette démonstration n'ouvre pas. Le bouton « Créer » "
             "attend sous le champ.", zoom=True),
        Plan("N12", 44.0, 48.0,
             "Dans la capture, le texte reste vide et le post n'est pas créé. "
             "Chez vous : rédigez, cliquez sur « Créer », et le post rejoindra "
             "la liste de l'onglet."),
        Plan("N13", 0.0, 0.0,
             "Ce formulaire, vous pouvez aussi ne jamais l'ouvrir : la même "
             "chose se demande en une phrase, depuis Claude.",
             chapitre="La Version Minute", pose="laptop", image=CARTE),
        Plan("N14", 0.0, 0.0,
             "L'outil create draft tool du MCP RapidoCMS crée le brouillon "
             "avec son réseau, son compte et son texte. Vous le retrouvez "
             "ensuite dans la liste.", image=CARTE),
        Plan("N15", 38.0, 42.0,
             "L'astuce : donnez au poste un nom qui commence par la date et le "
             "réseau. Quand la liste se remplit, vous retrouvez n'importe quel "
             "post en un coup d'œil.",
             chapitre="L'astuce", pose="victoire", zoom=True),
    ],
)


if __name__ == "__main__":
    cli(EPISODE)
