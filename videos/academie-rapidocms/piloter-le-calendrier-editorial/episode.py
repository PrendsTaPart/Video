#!/usr/bin/env python3
"""Tutoriel 09 — Lire et filtrer le calendrier éditorial.

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
    prompt="Qu'est-ce qui est programmé sur mes réseaux dans les sept "
           "prochains jours ?",
    outil="list_scheduled_posts",
    resultat=[
        "société    : 321 — KEBAIL-ALI",
        "comptes    : Facebook, LinkedIn, Instagram",
        "programmés : 0 sur la période",
        "",
        "→ le calendrier d'octobre est vide : rien ne part cette semaine.",
    ],
    cible=RACINE / "composition" / "carte-version-minute.png",
)
CARTE_DEMANDE = CARTE.with_name(CARTE.stem + "-demande.png")

EPISODE = Episode(
    slug="piloter-le-calendrier-editorial",
    numero=9,
    titre="Lire et filtrer le calendrier éditorial",
    titre_court="Piloter le calendrier éditorial",
    module="Communication",
    promesse="À la fin de cette vidéo, vous savez ouvrir votre calendrier, le "
             "filtrer par réseau et par compte, et changer d'échelle de "
             "lecture.",
    source=RACINE.parent / "_sources"
    / "Publication_des_postes_ou_brouillon_sur_le_calendrier__ditorial.mp4",
    suivant="Consulter l'historique des publications",
    voix_fin="Retenez ceci : on filtre d'abord, on planifie ensuite. Dans la "
             "prochaine vidéo, on consulte l'historique des publications.",
    vignette_a=25.0,
    pose_vignette="pointe-droite",
    mot_cle="calendrier",
    racine=RACINE,
    plans=[
        Plan("N1", 0.0, 4.0,
             "Vos publications sont éparpillées entre un tableur, un carnet et "
             "votre mémoire. RapidoCMS les rassemble sur une seule grille.",
             chapitre="Le calendrier, pas le tableur", pose="decouverte",
             zoom=True),
        Plan("N2", 0.0, 4.0,
             "Menu latéral, rubrique CMS, entrée « Calendrier ». La grille du "
             "mois s'ouvre — ici sur un compte de démonstration encore vide."),
        Plan("N3", 12.0, 16.0,
             "En haut, deux chevrons encadrent le nom du mois, « Octobre ». Au "
             "centre, « Aujourd'hui », et la date du jour, « 16 Oct. ».",
             chapitre="Se repérer dans le mois", pose="pointe-gauche",
             zoom=True),
        Plan("N4", 12.0, 16.0,
             "À droite, un champ de recherche, et le sélecteur de vue : "
             "« Jour », « Semaine », « Mois ». « Mois » est actif par défaut.",
             zoom=True),
        Plan("N5", 20.0, 24.0,
             "Trois filtres sous la barre. Le premier, « Réseaux sociaux », "
             "s'ouvre sur quatre choix : Facebook, LinkedIn, Instagram, ou "
             "tout.",
             chapitre="Filtrer par réseau", pose="pointe-droite", zoom=True),
        Plan("N6", 20.0, 24.0,
             "Vous cochez un réseau, puis « Appliquer », en bas du menu. La "
             "grille ne garde alors que les publications de ce réseau.",
             zoom=True),
        Plan("N7", 24.0, 28.0,
             "Le filtre « Compte » liste vos pages connectées, chacune avec son "
             "icône : « Cocuisinage By Foodeatup », « Avatalk » et « Plan'It » "
             "sur Facebook.",
             chapitre="Filtrer par compte", pose="dossier", zoom=True),
        Plan("N8", 24.0, 28.0,
             "« BraindCode » et « Cocuisinage » sur Instagram ; "
             "« RapidoSoftware », « BraindCode » et « FoodEatUp » sur LinkedIn. "
             "Huit pages, une seule grille.", zoom=True),
        Plan("N9", 24.0, 28.0,
             "Le troisième filtre, « Statut », n'est pas ouvert ici : il "
             "servira à ne garder que les publications d'un même état."),
        Plan("N10", 32.0, 36.0,
             "Un clic sur « Jour », et la grille devient une colonne d'heures, "
             "à partir de minuit. C'est la vue des journées chargées.",
             chapitre="Changer de vue", pose="laptop", zoom=True),
        Plan("N11", 40.0, 44.0,
             "Un clic sur « Mois », et vous revenez à la vue d'ensemble. "
             "« Semaine » se place entre les deux : cette capture ne l'ouvre "
             "pas."),
        Plan("N12", 0.0, 0.0,
             "Ouvrir le calendrier juste pour vérifier ce qui part cette "
             "semaine, c'est trois clics de trop.",
             chapitre="La Version Minute", pose="laptop", image=CARTE_DEMANDE),
        Plan("N13", 0.0, 0.0,
             "Dans Claude, l'outil list scheduled posts du MCP RapidoCMS vous "
             "renvoie tout ce qui est programmé. Une phrase, une réponse.",
             image=CARTE),
        Plan("N14", 32.0, 36.0,
             "L'astuce : arbitrez votre rythme en vue « Mois », puis repassez "
             "en vue « Jour » la veille, pour vérifier les heures d'envoi.",
             chapitre="L'astuce", pose="victoire", zoom=True),
    ],
)


if __name__ == "__main__":
    cli(EPISODE)
