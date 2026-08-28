#!/usr/bin/env python3
"""Tutoriel 04 — Ses réseaux sociaux connectés, et quand les reconnecter.

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
    prompt="Liste les comptes réseaux sociaux reliés à mon espace RapidoCMS, "
           "avec leur date d'expiration.",
    outil="list_connected_accounts",
    resultat=[
        "société   : 321 — KEBAIL-ALI",
        "Facebook  : 3 pages — expire le 05/12",
        "Instagram : 2 comptes — expire le 05/12",
        "LinkedIn  : 3 pages — expire le 15/11",
        "",
        "→ échéance la plus proche : LinkedIn, le 15 novembre.",
    ],
    cible=RACINE / "composition" / "carte-version-minute.png",
)

EPISODE = Episode(
    slug="connecter-ses-reseaux-sociaux",
    numero=4,
    titre="Ses réseaux sociaux connectés, et quand les reconnecter",
    titre_court="Connecter ses réseaux sociaux",
    module="Prise en main",
    promesse="À la fin de cette vidéo, vous savez lire l'écran des comptes "
             "reliés et repérer celui qui va expirer.",
    source=RACINE.parent / "_sources" / "Configuration_et_connexion_social_media.mp4",
    suivant="Lire son tableau de bord",
    voix_fin="Retenez ceci : un compte relié n'est pas relié pour toujours. "
             "Dans la prochaine vidéo, on lit votre tableau de bord.",
    vignette_a=20.0,
    pose_vignette="presente-paume",
    mot_cle="réseaux",
    racine=RACINE,
    plans=[
        Plan("N1", 0.0, 4.0,
             "Vous publiez encore réseau par réseau. Avant de changer ça, "
             "RapidoCMS a besoin de savoir quels comptes vous appartiennent.",
             chapitre="Vos comptes au même endroit", pose="accueil",
             zoom=True),
        Plan("N2", 0.0, 4.0,
             "Page « Profil », onglet « Configuration compte ». La section "
             "« Réseaux sociaux » aligne quatre tuiles : Facebook, LinkedIn, "
             "Instagram, et un plus."),
        Plan("N3", 20.0, 24.0,
             "Sélectionnez une tuile : le panneau de droite se remplit. "
             "Facebook liste trois pages reliées : « Cocuisinage By "
             "Foodeatup », « Avatalk » et « Plan'It ».",
             chapitre="Facebook et LinkedIn", pose="pointe-droite", zoom=True),
        Plan("N4", 20.0, 24.0,
             "Le bouton « Se connecter » lance l'autorisation côté Facebook. "
             "La capture ne l'ouvre pas : elle montre le résultat, une fois "
             "les pages autorisées.", zoom=True),
        Plan("N5", 24.0, 28.0,
             "La tuile LinkedIn suit exactement le même principe, avec trois "
             "organisations : « RapidoSoftware », « BraindCode » et "
             "« FoodEatUp »."),
        Plan("N6", 24.5, 28.0,
             "Son tableau n'a que deux colonnes, le nom et l'expiration : "
             "LinkedIn ne renvoie pas de vignette. Ce n'est pas une erreur.",
             zoom=True),
        Plan("N7", 16.0, 20.0,
             "Instagram pose une condition, rappelée par le bandeau bleu : "
             "votre compte doit d'abord être associé à une page Facebook.",
             chapitre="Le cas Instagram", pose="stop", zoom=True),
        Plan("N8", 16.0, 20.0,
             "Le bouton « associer » prend le relais ensuite. Deux comptes "
             "figurent déjà dans la liste : « BraindCode » et « Cocuisinage ».",
             zoom=True),
        Plan("N9", 20.0, 24.0,
             "La colonne « Expiration » est la plus importante de l'écran. Une "
             "autorisation a une fin de validité, ici le cinq décembre côté "
             "Facebook.",
             chapitre="Les dates d'expiration", pose="reflexion", zoom=True),
        Plan("N10", 24.0, 28.0,
             "Côté LinkedIn, c'est le quinze novembre. Passée la date, la "
             "publication échoue : il faut repasser par « Se connecter » pour "
             "prolonger.", zoom=True),
        Plan("N11", 20.0, 24.0,
             "À droite de chaque ligne, la corbeille rouge retire le compte de "
             "votre espace RapidoCMS. Elle ne touche à rien sur le réseau "
             "lui-même.", zoom=True),
        Plan("N12", 32.0, 36.0,
             "La quatrième tuile sert à ajouter un autre réseau. Dans cette "
             "version, elle n'ouvre rien : elle affiche un panneau encore "
             "vide.",
             chapitre="La tuile plus", pose="decouverte", zoom=True),
        Plan("N13", 0.0, 0.0,
             "Cet inventaire, vous n'avez pas besoin d'ouvrir la page pour "
             "l'obtenir.",
             chapitre="La Version Minute", pose="laptop", image=CARTE),
        Plan("N14", 0.0, 0.0,
             "Dans Claude, l'outil list connected accounts du MCP RapidoCMS "
             "vous rend la liste des comptes reliés et leurs échéances.",
             image=CARTE),
        Plan("N15", 24.0, 28.0,
             "L'astuce : notez la date la plus proche dans votre agenda, moins "
             "une semaine. Une autorisation expirée ne prévient pas, elle fait "
             "juste échouer la publication.",
             chapitre="L'astuce", pose="victoire", zoom=True),
    ],
)


if __name__ == "__main__":
    cli(EPISODE)
