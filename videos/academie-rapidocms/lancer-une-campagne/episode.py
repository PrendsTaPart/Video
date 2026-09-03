#!/usr/bin/env python3
"""Tutoriel 11 — Lancer une campagne : la page Campagne et sa fenêtre de création.

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
    prompt="Crée une campagne « Rentrée » sur Facebook pour ma société, "
           "et dis-moi combien j'en ai.",
    outil="create_campagne",
    resultat=[
        "campagne : « Rentrée »",
        "réseau   : Facebook · société 321 — KEBAIL-ALI",
        "posts rattachés : 0",
        "total des campagnes : 1",
        "",
        "→ add_post_campagne y rattache chaque post.",
    ],
    cible=RACINE / "composition" / "carte-version-minute.png",
)
CARTE_DEMANDE = CARTE.with_name(CARTE.stem + "-demande.png")

EPISODE = Episode(
    slug="lancer-une-campagne",
    numero=11,
    titre="Lancer une campagne : la page Campagne et sa fenêtre de création",
    titre_court="Lancer une campagne",
    module="Communication",
    promesse="À la fin de cette vidéo, vous savez à quoi sert la page "
             "Campagne, ce que comptent ses statistiques, et ce que demande "
             "la fenêtre de création.",
    source=RACINE.parent / "_sources"
    / "Affiliation_des_postes_a_une_campagne_marketing.mp4",
    suivant="Découvrir l'éditeur",
    voix_fin="Retenez ceci : la campagne est le dossier qui regroupe vos posts "
             "et leurs résultats. Dans la prochaine vidéo, on découvre "
             "l'éditeur.",
    vignette_a=32.0,
    pose_vignette="dossier",
    mot_cle="campagne",
    racine=RACINE,
    plans=[
        Plan("N1", 0.0, 4.0,
             "Vos posts partent dans tous les sens et vous ne savez plus "
             "lesquels servent le même objectif. Une campagne les regroupe.",
             chapitre="Où vivent les campagnes", pose="decouverte"),
        Plan("N2", 24.0, 28.0,
             "Nous sommes dans RapidoCMS, rubrique Communication, page "
             "Campagne. Une recherche en haut, des statistiques au milieu, la "
             "liste de vos campagnes en dessous."),
        Plan("N3", 14.0, 18.0,
             "La première section compte deux choses : le nombre de campagnes "
             "créées, et le nombre de posts qui leur sont rattachés.",
             chapitre="Les statistiques", pose="reflexion", zoom=True),
        Plan("N4", 14.0, 18.0,
             "Ici tout est à zéro, et les deux encarts de droite annoncent "
             "qu'aucune donnée n'est disponible. Ils se rempliront dès votre "
             "première campagne.", zoom=True),
        Plan("N5", 20.0, 24.0,
             "Plus bas, « Liste des campagnes » : vide elle aussi. C'est là "
             "qu'apparaîtront vos campagnes, chacune avec ses statistiques.",
             chapitre="La liste des campagnes", pose="pointe-gauche"),
        Plan("N6", 24.0, 28.0,
             "Le champ « Chercher », en haut, servira quand la liste "
             "s'allongera : vous tapez le nom d'une campagne pour la retrouver "
             "sans faire défiler."),
        Plan("N7", 28.0, 32.0,
             "Le bouton « Créer une campagne » est en haut à droite. Il "
             "devient bleu au survol, et ouvre une fenêtre par-dessus la page.",
             chapitre="Créer une campagne", pose="pointe-droite", zoom=True),
        Plan("N8", 32.0, 36.0,
             "Trois informations sont demandées : le nom de la campagne, une "
             "description qui précise l'objectif ou le public visé, et le "
             "réseau principal.", zoom=True),
        Plan("N9", 32.0, 36.0,
             "Les réseaux proposés sont Facebook, Instagram et LinkedIn, à "
             "cocher. Le bouton « Ajouter », en bas, valide la création.",
             zoom=True),
        Plan("N10", 52.0, 56.0,
             "Dans cette démonstration, les champs restent vides et rien n'est "
             "coché : la campagne n'est donc jamais créée, et la liste reste "
             "vide.",
             chapitre="Ce que la capture ne montre pas", pose="stop"),
        Plan("N11", 55.0, 58.0,
             "Chez vous, remplissez le nom, la description, cochez un réseau, "
             "puis « Ajouter » : la campagne rejoindra la liste, et ses "
             "compteurs démarreront.", zoom=True),
        Plan("N12", 0.0, 0.0,
             "Et si vous n'aviez pas à ouvrir cette page du tout ? Une "
             "campagne se crée en une phrase, depuis Claude.",
             chapitre="La Version Minute", pose="laptop", image=CARTE_DEMANDE),
        Plan("N13", 0.0, 0.0,
             "L'outil create campagne du MCP RapidoCMS la crée avec son nom, "
             "sa description et son réseau. Ensuite, add post campagne y "
             "rattache vos posts.", image=CARTE),
        Plan("N14", 20.0, 24.0,
             "L'astuce : créez la campagne avant les posts. Chaque post "
             "rattaché alimente les compteurs, et vous mesurez un ensemble au "
             "lieu de publications isolées.",
             chapitre="L'astuce", pose="victoire", zoom=True),
    ],
)


if __name__ == "__main__":
    cli(EPISODE)
