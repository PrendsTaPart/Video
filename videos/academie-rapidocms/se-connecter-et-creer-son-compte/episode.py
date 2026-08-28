#!/usr/bin/env python3
"""Tutoriel 01 — Se connecter, récupérer son mot de passe, créer son compte.

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
    prompt="Rappelle-moi qui est connecté sur mon espace RapidoCMS, "
           "et quelle entreprise il pilote.",
    outil="get_profile",
    resultat=[
        "profil   : Michael KEBAIL-ALI",
        "rôle     : admin",
        "société  : 321 — KEBAIL-ALI",
        "",
        "→ get_company complète la fiche : SIRET, banque, coordonnées.",
    ],
    cible=RACINE / "composition" / "carte-version-minute.png",
)

EPISODE = Episode(
    slug="se-connecter-et-creer-son-compte",
    numero=1,
    titre="Se connecter, récupérer son mot de passe, créer son compte",
    titre_court="Entrer dans RapidoCMS",
    module="Prise en main",
    promesse="À la fin de cette vidéo, vous entrez dans RapidoCMS, quel que "
             "soit votre point de départ.",
    source=RACINE.parent / "_sources" / "Connexions_Inscription_oublie_de_mot_de_passe.mp4",
    suivant="Configurer son profil",
    voix_fin="Retenez ceci : trois cartes, une seule porte. Dans la prochaine "
             "vidéo, on configure votre profil et votre fiche entreprise.",
    vignette_a=17.0,
    pose_vignette="decouverte",
    mot_cle="connecter",
    racine=RACINE,
    plans=[
        Plan("N1", 0.0, 4.0,
             "Vous avez vos accès RapidoCMS, vous ouvrez la page, et vous ne "
             "savez pas trop où cliquer. En deux minutes, c'est réglé.",
             chapitre="La porte d'entrée", pose="decouverte", zoom=True),
        Plan("N2", 2.0, 6.0,
             "Tout se joue sur trois cartes, avant même d'entrer dans "
             "l'application : se connecter, récupérer un mot de passe, créer "
             "un compte."),
        Plan("N3", 8.0, 12.0,
             "La première s'appelle « Accéder à mon compte ». Deux champs, pas "
             "un de plus : votre adresse e-mail, et votre mot de passe.",
             zoom=True),
        Plan("N4", 12.0, 16.5,
             "Vous saisissez l'adresse avec laquelle votre espace a été créé, "
             "puis le mot de passe. L'œil au bout du champ vous laisse le "
             "relire avant de valider.",
             chapitre="Se connecter", pose="pointe-gauche", zoom=True),
        Plan("N5", 16.0, 20.0,
             "Le bouton bleu « Se connecter » vous ouvre le tableau de bord, "
             "sur vos statistiques et votre calendrier.", zoom=True),
        Plan("N6", 20.0, 24.0,
             "Sous le séparateur « OU », le bouton Google fait la même chose "
             "sans mot de passe à retenir. Vous choisissez votre compte, et "
             "vous êtes dedans.",
             chapitre="L'entrée par Google", pose="pointe-droite"),
        Plan("N7", 24.0, 28.0,
             "Mot de passe perdu ? Le lien « Mot de passe oublié ? » est juste "
             "au-dessus du bouton bleu, à droite.",
             chapitre="Mot de passe oublié", pose="reflexion", zoom=True),
        Plan("N8", 28.0, 33.0,
             "La carte qui s'ouvre ne demande qu'une chose : l'adresse e-mail "
             "de votre compte.", zoom=True),
        Plan("N9", 34.0, 39.0,
             "« Envoyer le lien de réinitialisation », et vous recevez dans "
             "votre boîte le lien qui vous laissera choisir un nouveau mot de "
             "passe. Le lien expire : ouvrez-le tout de suite.", zoom=True),
        Plan("N10", 40.0, 44.0,
             "Pas encore de compte ? « Créer un compte » est en bas de chaque "
             "carte, et vous y ramène toujours.",
             chapitre="Créer un compte", pose="checklist"),
        Plan("N11", 44.0, 48.0,
             "Cinq champs : le nom du gérant, son prénom, l'adresse e-mail, le "
             "mot de passe, et sa confirmation.", zoom=True),
        Plan("N12", 47.0, 51.5,
             "« Suivant » crée l'espace. Vous enchaînez alors sur votre profil "
             "et sur la fiche de votre entreprise — c'est le tutoriel suivant.",
             zoom=True),
        Plan("N13", 0.0, 0.0,
             "Une fois dedans, vous n'avez plus besoin d'ouvrir l'interface "
             "pour vérifier qui vous êtes.",
             chapitre="La Version Minute", pose="laptop", image=CARTE),
        Plan("N14", 0.0, 0.0,
             "Dans Claude, l'outil get profile du MCP RapidoCMS vous renvoie "
             "votre profil, et get company votre fiche entreprise. Une phrase, "
             "une réponse.", image=CARTE),
        Plan("N15", 8.0, 12.0,
             "L'astuce : connectez-vous une fois avec Google, et vous n'aurez "
             "plus jamais à gérer ce mot de passe-là. C'est aussi ce qui vous "
             "évite d'être bloqué le jour où vous changez d'ordinateur.",
             chapitre="L'astuce", pose="victoire", zoom=True),
    ],
)


if __name__ == "__main__":
    cli(EPISODE)
