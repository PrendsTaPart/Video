#!/usr/bin/env python3
"""Tutoriel 03 — Remplir sa fiche entreprise et sa charte de marque.

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
    prompt="Crée la marque de mon entreprise dans RapidoCMS : nom, slogan, "
           "langue officielle et site web.",
    outil="create_brand",
    resultat=[
        "société  : 321 — KEBAIL-ALI",
        "marque   : créée",
        "langue   : français",
        "slogan   : à compléter",
        "",
        "→ get_company relit la fiche : SIRET, banque, coordonnées.",
    ],
    cible=RACINE / "composition" / "carte-version-minute.png",
)

EPISODE = Episode(
    slug="remplir-sa-fiche-entreprise",
    numero=3,
    titre="Remplir sa fiche entreprise et sa charte de marque",
    titre_court="Remplir sa fiche entreprise",
    module="Prise en main",
    promesse="À la fin de cette vidéo, vous savez où vivent les informations "
             "légales, bancaires et graphiques de votre entreprise.",
    source=RACINE.parent / "_sources" / "Configuration_du_fiche_entreprise.mp4",
    suivant="Connecter ses réseaux sociaux",
    voix_fin="Retenez ceci : deux cartes, deux enregistrements. Dans la "
             "prochaine vidéo, on connecte vos réseaux sociaux.",
    vignette_a=44.0,
    pose_vignette="dossier",
    mot_cle="entreprise",
    racine=RACINE,
    plans=[
        Plan("N1", 0.0, 4.0,
             "Un devis sans SIRET, une facture sans IBAN, un logo qui change à "
             "chaque support. Tout ça part d'une seule fiche, et elle se "
             "remplit une fois.",
             chapitre="La fiche de votre entreprise", pose="dossier",
             zoom=True),
        Plan("N2", 0.0, 4.0,
             "Page « Profil », onglet « Entreprise ». Deux sous-onglets : "
             "« Entreprise » pour l'administratif, « Ma marque » pour "
             "l'identité visuelle."),
        Plan("N3", 0.0, 4.0,
             "La section « Information sur l'entreprise » affiche ici le nom "
             "« Braindcode » et le SIRET « 12345678912345 ».",
             chapitre="Les informations légales", pose="pointe-droite",
             zoom=True),
        Plan("N4", 0.5, 4.5,
             "En dessous, l'e-mail professionnel, puis « Numéro », « Adresse » "
             "et « Code postal » — vides dans cette démonstration.", zoom=True),
        Plan("N5", 12.0, 16.0,
             "La section « Information bancaire » attend trois valeurs : votre "
             "banque, votre code SWIFT et votre IBAN.",
             chapitre="Les coordonnées bancaires", pose="reflexion", zoom=True),
        Plan("N6", 12.5, 16.5,
             "Les trois champs affichent le même texte indicatif : ne vous y "
             "fiez pas, fiez-vous au libellé écrit au-dessus de chacun.",
             zoom=True),
        Plan("N7", 36.0, 40.0,
             "Le bouton bleu « Modifier », en bas de la carte, enregistre "
             "cette fiche. Ici il est seulement survolé : aucune confirmation "
             "n'apparaît.", zoom=True),
        Plan("N8", 44.0, 48.0,
             "« Ma marque » ouvre une seconde carte : « Nom de la marque », "
             "« Langue officielle », « Site web » et « Slogan ».",
             chapitre="Le sous-onglet Ma marque", pose="decouverte"),
        Plan("N9", 44.5, 48.0,
             "Ces champs sont vides du début à la fin de la capture. Une fois "
             "remplis, ils décrivent la marque que la plateforme reprendra "
             "dans vos contenus.", zoom=True),
        Plan("N10", 56.0, 60.0,
             "En bas, la « Charte graphique » : le logo via « Parcourir », la "
             "police du texte, et les couleurs de marque derrière le bouton "
             "plus.",
             chapitre="La charte graphique", pose="presente-paume", zoom=True),
        Plan("N11", 56.5, 60.0,
             "Dans cette capture, aucun logo n'est importé, la liste des "
             "polices n'est jamais déroulée et le sélecteur de couleurs n'est "
             "pas ouvert.", zoom=True),
        Plan("N12", 72.0, 76.0,
             "Un second bouton « Modifier » valide la charte. Chaque "
             "sous-onglet s'enregistre séparément : c'est le piège de cette "
             "page.", zoom=True),
        Plan("N13", 0.0, 0.0,
             "Cette carte de marque, vous pouvez aussi la créer sans ouvrir un "
             "seul champ.",
             chapitre="La Version Minute", pose="laptop", image=CARTE),
        Plan("N14", 0.0, 0.0,
             "Dans Claude, l'outil create brand du MCP RapidoCMS crée la "
             "marque, et get company relit la fiche administrative.",
             image=CARTE),
        Plan("N15", 44.0, 48.0,
             "L'astuce : enregistrez avant de changer de sous-onglet. Un clic "
             "sur « Modifier » ne vaut que pour la carte affichée à l'écran.",
             chapitre="L'astuce", pose="victoire", zoom=True),
    ],
)


if __name__ == "__main__":
    cli(EPISODE)
