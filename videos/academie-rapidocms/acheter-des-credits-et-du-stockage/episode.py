#!/usr/bin/env python3
"""Tutoriel 07 — Suivre ses dépenses de crédits et ouvrir la page des packs.

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
    prompt="Liste les fichiers stockés sur mon espace RapidoCMS, "
           "du plus lourd au plus léger.",
    outil="list_all_files",
    resultat=[
        "société  : 321 — KEBAIL-ALI",
        "fichiers : 0 — la bibliothèque est vide",
        "",
        "→ rien à supprimer : le stockage acheté servira",
        "  aux visuels que vous ajouterez ensuite.",
    ],
    cible=RACINE / "composition" / "carte-version-minute.png",
)
CARTE_DEMANDE = CARTE.with_name(CARTE.stem + "-demande.png")

EPISODE = Episode(
    slug="acheter-des-credits-et-du-stockage",
    numero=7,
    titre="Suivre ses dépenses de crédits et ouvrir la page des packs",
    titre_court="Acheter crédits et stockage",
    module="Abonnement & crédits",
    promesse="À la fin de cette vidéo, vous savez ce que chaque action vous "
             "coûte, et où choisir un pack de stockage ou de crédits.",
    source=RACINE.parent / "_sources" / "Historique_des_achat_cr_dits.mp4",
    suivant="Créer un post",
    voix_fin="Retenez ceci : on regarde ses dépenses avant de recharger. Dans "
             "la prochaine vidéo, on crée un post.",
    vignette_a=29.0,
    pose_vignette="presente-paume",
    mot_cle="crédits",
    racine=RACINE,
    plans=[
        Plan("N1", 0.0, 4.0,
             "Vous générez des textes, des images, vous stockez des fichiers — "
             "et vous ne savez pas ce que ça coûte. Cet écran répond.",
             chapitre="Le compteur qui descend", pose="reflexion", zoom=True),
        Plan("N2", 0.0, 4.0,
             "Page « Abonnement », troisième onglet : « Dépenses crédit ». En "
             "haut à droite, votre solde affiche « 605.00€ »."),
        Plan("N3", 8.0, 12.0,
             "Au-dessus du tableau, une liste « Type », réglée sur « Tout », et "
             "deux champs de date pour ne garder qu'une période.",
             chapitre="L'onglet Dépenses crédit", pose="pointe-gauche",
             zoom=True),
        Plan("N4", 8.0, 12.0,
             "Le tableau a quatre colonnes : le type d'usage, la taille "
             "consommée, le prix, et la date de dépense.", zoom=True),
        Plan("N5", 20.0, 24.0,
             "Ici, une seule ligne : un usage de type texte, six cent trente-"
             "deux jetons, facturés bien moins d'un centime, le 1er septembre "
             "2025.",
             chapitre="Lire une ligne de dépense", pose="laptop", zoom=True),
        Plan("N6", 20.0, 24.0,
             "C'est le niveau de détail : chaque génération laisse sa trace, "
             "avec son prix exact, jusqu'au dix-millième d'euro.", zoom=True),
        Plan("N7", 24.0, 28.0,
             "Quand le solde baisse, le bouton bleu « Acheter un pack », en "
             "haut à droite, ouvre la page « Ajouter un pack ».",
             chapitre="Ouvrir les packs", pose="pointe-droite"),
        Plan("N8", 28.0, 32.0,
             "Deux cartes côte à côte. À gauche, « Pack stockage » : un giga "
             "pour cinq euros, cinq gigas pour quinze, dix gigas pour vingt.",
             zoom=True),
        Plan("N9", 28.0, 32.0,
             "À droite, « Pack crédit » : un, cinq ou dix euros, rechargés tels "
             "quels. Chaque carte a son bouton « Payer ».", zoom=True),
        Plan("N10", 28.0, 32.0,
             "Vous cochez ensuite un montant, puis « Payer », et le paiement se "
             "fait à l'étape suivante. Cette capture s'arrête juste avant."),
        Plan("N11", 0.0, 0.0,
             "Avant d'acheter du stockage, la vraie question est : qu'est-ce "
             "qui occupe déjà votre espace ?",
             chapitre="La Version Minute", pose="laptop", image=CARTE_DEMANDE),
        Plan("N12", 0.0, 0.0,
             "Dans Claude, l'outil list all files du MCP RapidoCMS liste vos "
             "fichiers. Vous saurez quoi supprimer avant de payer.",
             image=CARTE),
        Plan("N13", 20.0, 24.0,
             "L'astuce : filtrez « Dépenses crédit » sur le mois écoulé avant "
             "chaque achat. Vous verrez votre rythme réel, et vous prendrez la "
             "bonne taille de pack.",
             chapitre="L'astuce", pose="victoire", zoom=True),
    ],
)


if __name__ == "__main__":
    cli(EPISODE)
