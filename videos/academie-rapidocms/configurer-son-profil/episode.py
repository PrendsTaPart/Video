#!/usr/bin/env python3
"""Tutoriel 02 — Configurer son profil administrateur.

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
    prompt="Vérifie que ma fiche administrateur RapidoCMS est complète, "
           "et dis-moi ce qui manque.",
    outil="get_profile",
    resultat=[
        "profil   : Michael KEBAIL-ALI",
        "société  : 321 — KEBAIL-ALI",
        "e-mail   : renseigné",
        "photo    : aucune",
        "",
        "→ à compléter : numéro, adresse, code postal.",
    ],
    cible=RACINE / "composition" / "carte-version-minute.png",
)

EPISODE = Episode(
    slug="configurer-son-profil",
    numero=2,
    titre="Configurer son profil administrateur",
    titre_court="Configurer son profil",
    module="Prise en main",
    promesse="À la fin de cette vidéo, votre fiche d'administrateur est "
             "complète et vous savez quel bouton l'enregistre.",
    source=RACINE.parent / "_sources" / "Configuration_du_profil_et_de_la_fiche_entreprise.mp4",
    suivant="Remplir sa fiche entreprise",
    voix_fin="Retenez ceci : rien n'est enregistré tant que « Modifier » n'est "
             "pas cliqué. Dans la prochaine vidéo, on remplit la fiche de "
             "votre entreprise.",
    vignette_a=20.0,
    pose_vignette="laptop",
    mot_cle="profil",
    racine=RACINE,
    plans=[
        Plan("N1", 0.0, 4.0,
             "Vos coordonnées sont incomplètes dans RapidoCMS, et ça finit par "
             "se voir partout. Une page suffit à tout remettre d'aplomb.",
             chapitre="Votre carte d'identité RapidoCMS", pose="decouverte",
             zoom=True),
        Plan("N2", 0.0, 4.0,
             "La page « Profil » s'ouvre sur trois onglets : « Profil », "
             "« Entreprise » et « Configuration compte ». On reste sur le "
             "premier."),
        Plan("N3", 8.0, 12.0,
             "La carte « Paramètre du profil » rassemble tout. Ici, le nom "
             "« KEBAIL-ALI » et le prénom « Michael » sont déjà renseignés.",
             chapitre="Les champs d'identité", pose="presente-paume",
             zoom=True),
        Plan("N4", 8.0, 12.0,
             "Juste en dessous, l'adresse e-mail du compte : c'est elle qui "
             "vous sert à vous connecter. Vérifiez-la avant tout le reste.",
             zoom=True),
        Plan("N5", 20.0, 24.0,
             "Trois champs restent vides : « Numéro », « Adresse » et « Code "
             "postal ». La démonstration les laisse tels quels.",
             chapitre="Les coordonnées", pose="pointe-gauche", zoom=True),
        Plan("N6", 21.0, 25.0,
             "Renseignez-les une bonne fois : ce sont les coordonnées qui "
             "suivront votre compte partout dans la plateforme.", zoom=True),
        Plan("N7", 30.0, 34.0,
             "Le bloc « Photo de Profil » attend une image. Le bouton "
             "« Parcourir » ouvre l'explorateur de fichiers de votre "
             "ordinateur.",
             chapitre="La photo de profil", pose="pointe-droite", zoom=True),
        Plan("N8", 31.0, 35.0,
             "Ici, le bouton est seulement survolé : aucune image n'est "
             "choisie, et la vignette d'aperçu reste grise.", zoom=True),
        Plan("N9", 20.0, 24.0,
             "Une fois votre image importée, c'est dans cette vignette qu'elle "
             "s'affichera, juste sous la zone de dépôt en pointillés.",
             zoom=True),
        Plan("N10", 43.0, 47.0,
             "Tout en bas de la carte, le bouton bleu « Modifier » enregistre "
             "la fiche. C'est le seul geste qui valide vos changements.",
             chapitre="Enregistrer", pose="checklist", zoom=True),
        Plan("N11", 43.0, 47.5,
             "Dans cette capture, il est survolé mais rien ne bouge : aucun "
             "message de confirmation n'apparaît. Rechargez la page pour "
             "vérifier.", zoom=True),
        Plan("N12", 0.0, 0.0,
             "Vous pouvez aussi ne jamais ouvrir cette page et demander "
             "directement à Claude ce qui manque.",
             chapitre="La Version Minute", pose="laptop", image=CARTE),
        Plan("N13", 0.0, 0.0,
             "L'outil get profile du MCP RapidoCMS renvoie votre fiche admin "
             "et les champs encore vides. Une phrase, une réponse.",
             image=CARTE),
        Plan("N14", 8.0, 12.0,
             "L'astuce : traitez l'e-mail comme un identifiant, pas comme un "
             "détail. Le changer change votre façon de vous connecter — "
             "prévenez vos collaborateurs avant.",
             chapitre="L'astuce", pose="victoire", zoom=True),
    ],
)


if __name__ == "__main__":
    cli(EPISODE)
