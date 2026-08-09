#!/usr/bin/env python3
"""Le plan réel qui ouvre et referme chaque tutoriel.

**Aucune génération.** Ces plans sont déjà tournés, déjà payés, déjà
ré-encodés au standard de la série (1920×1080, 30 i/s, GOP court) et déjà
présents dans `studio-video/assets/plates/`. Les réutiliser ne coûte rien et
donne aux seize films la même image que les dix-huit déjà en ligne — c'est la
même série, il faut que ça se voie.

**Ce qu'un plan fait ici, et ce qu'il ne fait pas.** Il ouvre le film sur un
lieu réel, sous un voile crème, le temps du titre. Il ne montre jamais le
geste enseigné : ce serait promettre une capture d'écran qu'on n'a pas. Le
geste est expliqué par les planches schématiques qui suivent.

**Les cinq trous, et pourquoi ils sont des trous.** La bibliothèque a été
tournée pour une journée de restaurant : cuisine, salle, bureau. Elle ne
contient ni livreur, ni roue cadeaux, ni écran de connecteur — ce sont des
sujets qu'aucun des dix-huit films n'avait à montrer. Ces cinq-là reçoivent
une image fabriquée sur RapidoCMS (`images.py`), animée en lent zoom : une
image fixe qui bouge lentement se tient aussi bien qu'un plan, à condition de
l'assumer comme une image.
"""

# tutoriel → (plan d'ouverture, plan de clôture)
#
# Le plan de clôture est toujours un plan de fin de journée ou de lieu qui se
# vide : la dernière image d'un tutoriel n'a pas à relancer, elle referme.
PLAQUES = {
    # ── Caisse ────────────────────────────────────────────────────────────
    # Salle prête, avant l'ouverture : c'est le moment où l'on règle la caisse.
    "t01": ("s1/salle-prete.mp4", "s3/salle-apres-midi.mp4"),
    "t02": ("s1/salle-vide.mp4", "s3/salle-apres-midi.mp4"),
    # Le serveur qui accueille : l'encaissement au comptoir et à la table.
    "t03": ("s2/serveur-accueil.mp4", "s3/serveur-fermeture.mp4"),
    "t04": ("s2/salle-service.mp4", "s3/salle-apres-midi.mp4"),
    "t05": ("s2/salle-service.mp4", "s3/serveur-fermeture.mp4"),
    # L'imprimante qui déroule un ticket Z : le sujet exact de la clôture.
    "t06": ("s3/ticket-z.mp4", "s3/serveur-fermeture.mp4"),
    "t07": ("d2/tableau-de-bord.mp4", "d3/devanture-nuit.mp4"),

    # ── HubRise & livraisons ──────────────────────────────────────────────
    # Aucun plan de livraison dans la bibliothèque : images RapidoCMS.
    "t08": ("tuto/connecteur-hubrise-16x9.jpg", "d3/devanture-nuit.mp4"),
    "t09": ("tuto/livreur-scooter-16x9.jpg", "d3/devanture-nuit.mp4"),
    "t10": ("tuto/reference-plat-16x9.jpg", "c3/cuisine-nuit.mp4"),
    "t11": ("c2/deux-chefs.mp4", "c3/cuisine-nuit.mp4"),

    # ── KDS ───────────────────────────────────────────────────────────────
    # Le chef qui valide un ticket sur l'écran de cuisine : le sujet même.
    "t12": ("c2/chef-kds.mp4", "c3/chef-nettoie.mp4"),

    # ── Site & réservations ───────────────────────────────────────────────
    "t13": ("s1/salle-vide.mp4", "d3/devanture-nuit.mp4"),

    # ── Marketing & Iris ──────────────────────────────────────────────────
    "t14": ("tuto/roue-cadeaux-16x9.jpg", "s3/salle-apres-midi.mp4"),
    "t15": ("tuto/connecteur-contenu-16x9.jpg", "d3/devanture-nuit.mp4"),

    # ── Comptabilité ──────────────────────────────────────────────────────
    "t16": ("d1/directeur-bureau.mp4", "d3/devanture-nuit.mp4"),
}

# Les cinq images à fabriquer, avec ce qu'elles doivent montrer.
#
# ⚠️ Aucune marque tierce visible. « Uber Eats » et « Deliveroo » sont nommés
# dans le titre du tutoriel — c'est un fait, et le dire est légitime. Montrer
# leurs logos demanderait leur autorisation. Les images restent donc
# génériques : un sac isotherme sans marque, un scooter sans livrée.
IMAGES = {
    "t08": (
        "connecteur-hubrise",
        "Illustration éditoriale à plat, palette crème #FCF9E6 et bleu #007BFF, encre "
        "#0F1A23. Trois cartes reliées par des traits fins : à gauche une carte « plateformes », "
        "au centre une carte « connecteur », à droite une carte « restaurant ». Style vectoriel "
        "épuré, ombres douces, aucune marque, aucun logo, aucun texte lisible.",
    ),
    "t09": (
        "livreur-scooter",
        "Illustration éditoriale, palette crème #FCF9E6 et violet #7C3AED. Un livreur à "
        "scooter vu de trois quarts arrière, grand sac isotherme carré sur le dos, rue "
        "résidentielle en fin de journée. Style vectoriel épuré, aplats, ombres douces. "
        "Sac et scooter entièrement neutres : aucune marque, aucun logo, aucune livrée "
        "colorée reconnaissable, aucun texte.",
    ),
    "t10": (
        "reference-plat",
        "Illustration éditoriale à plat, palette crème #FCF9E6 et violet #7C3AED. Deux "
        "fiches de plat côte à côte reliées par un trait, chacune portant une étiquette "
        "de référence figurée par des tirets, l'une avec une coche, l'autre avec une "
        "croix. Style vectoriel épuré, aucune marque, aucun texte lisible.",
    ),
    "t14": (
        "roue-cadeaux",
        "Illustration éditoriale, palette crème #FCF9E6 et rose #D6336C. Une roue de la "
        "fortune à huit secteurs vue de face, un repère en haut, quelques cartes de bons "
        "posées à côté. Style vectoriel épuré, aplats, ombres douces, aucune marque, "
        "aucun texte lisible.",
    ),
    "t15": (
        "connecteur-contenu",
        "Illustration éditoriale à plat, palette crème #FCF9E6 et rose #D6336C. Deux prises "
        "qui se rejoignent au centre, entourées d'icônes simples de contenu — image, "
        "calendrier, bulle de message. Style vectoriel épuré, ombres douces, aucune marque, "
        "aucun logo, aucun texte lisible.",
    ),
}
