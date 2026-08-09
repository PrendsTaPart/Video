#!/usr/bin/env python3
"""Contenu des neuf films « sans » : texte dit, maquettes, compteurs.

Un seul fichier plutôt que neuf, parce que les neuf films partagent la même
armature — NOTES §6.3 impose le refrain, le plan des sept onglets et le carton
final dans **tous**. Répartir ça sur neuf scripts, ce serait neuf occasions de
laisser tomber l'un des trois sans s'en apercevoir. Ici, l'armature est dans le
générateur et ne peut pas manquer ; ce fichier ne porte que ce qui change.

⚠️ Aucun nom de marque ne doit entrer ici — ni dans les libellés d'outils, ni
dans les onglets, ni dans le texte dit (NOTES §6.1). Les libellés désignent une
**fonction** (« Tableur de stock »), jamais un produit, et jamais une catégorie
assez étroite pour ne désigner qu'un seul acteur du marché.

⚠️ Tout chiffre est une **fourchette** (NOTES §6.2). Une publicité comparative
doit être vérifiable ; une valeur unique est attaquable, une fourchette sourcée
ne l'est pas. Référence retenue : 5 à 8 abonnements, 350 à 900 €/mois.

Cette fourchette est désormais sourcée, et elle est conservatrice : calculée
sur les 47 éditeurs du comparateur du site vitrine, tarifs publics relevés en
juillet 2026, un empilement de cinq abonnements au prix médian de sa catégorie
revient à 363 € (les cinq catégories les moins chères) ou 918 € (les cinq les
plus chères). Huit abonnements coûteraient 711 à 1 211 €. Le détail du calcul
est dans RELECTURE-JURIDIQUE-SANS.md, réserve 3. À revérifier si la diffusion
dépasse douze mois.

Chaque film porte huit segments de voix, un par scène de corps. L'armature
complète, générée par `build-sans.py`, fait dix scènes :

    hook · carton · outils · REFRAIN · outils · TAB-CHAOS · compteur ·
    carton · punchline

Le refrain tombe en quatrième position, soit près de 20 % de la durée — la
place fixée au §6.3.
"""

# Le refrain, mot pour mot dans les neuf films. C'est une reprise, pas une
# variation : il ne porte que s'il revient identique.
REFRAIN = "Je paie entre cinq et huit abonnements.<br />Mon équipe en utilise deux."
REFRAIN_APPUI = "Et aucun ne parle aux autres."
REFRAIN_VO = ("Je paie entre cinq et huit abonnements. Mon équipe en utilise deux. "
              "Et aucun ne parle aux autres.")

# Les sept onglets du plan obligatoire, déclinés par métier. Sept, toujours :
# c'est le nombre qui fait l'argument, pas les intitulés.
ONGLETS = {
    "cuisine": ["Stock", "Réception", "Températures", "Fournisseurs",
                "Fiches", "Commandes", "Compta"],
    "salle": ["Réservations", "Caisse", "Plan de salle", "Avis",
              "Cartes cadeaux", "Planning", "Compta"],
    "direction": ["Planning", "Stocks", "Caisse", "Avis",
                  "Campagnes", "Paie", "Compta"],
}

# Photo de fond du carton « ce que la journée a coûté ». Quatre images du
# registre « sans » déjà présentes dans la bibliothèque Higgsfield, jamais
# montées jusqu'ici.
#
# `sept-onglets` a été essayée puis écartée. En plan large, c'est un petit
# écran clair dans une pièce noire : sous le voile du compteur elle devient
# une bouillie grise. Resserrée dans l'écran, elle donne un cadre presque vide
# et rend les libellés d'onglets plus lisibles qu'avant — deux problèmes pour
# une seule image, dont un juridique. Les trois films de direction prennent
# donc le comptoir de fin de service : de l'argent compté à la main sur un
# comptoir, c'est exactement ce que le carton énonce. L'idée des sept onglets
# reste portée par le plan animé `sans-onglets`, en ouverture de D1′ et D3′.
PHOTOS_COMPTEUR = {
    "c1s-cuisine-avant-sans":     "cahier-spirale",
    "c2s-cuisine-pendant-sans":   "ticket-au-sol",
    "c3s-cuisine-apres-sans":     "cahier-spirale",
    "s1s-salle-avant-sans":       "tablettes-depareillees",
    "s2s-salle-pendant-sans":     "tablettes-depareillees",
    "s3s-salle-apres-sans":       "comptoir-fin-service",
    "d1s-direction-avant-sans":   "comptoir-fin-service",
    "d2s-direction-pendant-sans": "comptoir-fin-service",
    "d3s-direction-apres-sans":   "comptoir-fin-service",
}

# Les horloges des quatre scènes à en-tête (outils, outils, onglets, compteur).
# Rassemblées ici plutôt que dispersées dans les blocs : c'est côte à côte
# qu'on vérifie qu'une journée avance, et qu'aucun film ne recule.
HORLOGES = {
    "c1s-cuisine-avant-sans":     ["06:00", "07:30", "09:00", "10:30"],
    "c2s-cuisine-pendant-sans":   ["12:10", "12:40", "13:10", "13:45"],
    "c3s-cuisine-apres-sans":     ["15:00", "15:45", "16:30", "17:30"],
    "s1s-salle-avant-sans":       ["09:00", "10:00", "10:45", "11:30"],
    "s2s-salle-pendant-sans":     ["12:30", "13:15", "13:45", "14:30"],
    "s3s-salle-apres-sans":       ["23:00", "23:20", "23:40", "00:05"],
    "d1s-direction-avant-sans":   ["08:00", "08:40", "09:15", "09:45"],
    "d2s-direction-pendant-sans": ["11:15", "12:00", "12:45", "13:30"],
    "d3s-direction-apres-sans":   ["15:00", "15:45", "16:30", "17:30"],
}

# Les deux surtitres des scènes d'outils. Ils nomment le manque, jamais un
# produit : c'est la jonction absente qui est le sujet, pas l'outil.
SURTITRES = {
    "c1s-cuisine-avant-sans":     ["TROIS ENDROITS POUR UN SEUL MATIN",
                                   "AUCUN NE CONNAÎT LE PRIX D'AUJOURD'HUI"],
    "c2s-cuisine-pendant-sans":   ["TROIS CANAUX, TROIS CARNETS",
                                   "PERSONNE NE SAIT OÙ EN EST LE PASSE"],
    "c3s-cuisine-apres-sans":     ["LES RELEVÉS DU SOIR, ÉPARPILLÉS",
                                   "COMMANDER SANS SAVOIR CE QU'IL RESTE"],
    "s1s-salle-avant-sans":       ["UNE RÉSERVATION, TROIS ENDROITS",
                                   "LE PLAN DE SALLE N'EXISTE QUE DANS MA TÊTE"],
    "s2s-salle-pendant-sans":     ["PRENDRE, RETAPER, RECRIER",
                                   "UN PLAT MANQUE, LE SITE NE LE SAIT PAS"],
    "s3s-salle-apres-sans":       ["TROIS PILES POUR UN SEUL TOTAL",
                                   "L'ÉCART QUE PERSONNE N'EXPLIQUERA"],
    "d1s-direction-avant-sans":   ["TROIS OUTILS AVANT HUIT HEURES TRENTE",
                                   "SEPT IDENTIFIANTS, SEPT PRÉLÈVEMENTS"],
    "d2s-direction-pendant-sans": ["CE QUI SE PASSE, JE L'APPRENDRAI PLUS TARD",
                                   "LA CAMPAGNE, JE L'ÉCRIS MOI-MÊME"],
    "d3s-direction-apres-sans":   ["TROIS FOIS LES MÊMES COORDONNÉES",
                                   "DES DONNÉES QUI NE SE RECOUPENT PAS"],
}

FILMS = {
    # ── Cuisine ──────────────────────────────────────────────────────────
    "c1s-cuisine-avant-sans": {
        "sous": "c1s", "metier": "cuisine", "phase": "avant",
        "plates": ("sans-cahier", "cuisine-vide-matin"),
        "chiffre": "18,40 €",
        "ouverture": ("Six heures", "La livraison arrive"),
        "cloture": ("Onze heures", "Ma traçabilité du matin n'est toujours pas saisie"),
        "outils1": (["Feuille de relevé", "Cahier de cuisine", "Tableur de stock"],
                    ["Aucun lien", "Aucune alerte"]),
        "outils2": (["Classeur fiches", "Tarifs fournisseurs", "Tableur de stock"],
                    ["Prix jamais à jour", "Marge inconnue"]),
        "compteur": [("5 à 8", "abonnements"),
                     ("1 h 45 à 2 h 30", "de saisie avant le service"),
                     ("3", "fois le même chiffre")],
        "vo": [
            "Six heures. La livraison arrive. Personne pour la contrôler à ma place.",
            "Les températures sur une feuille volante. Les dates limites dans un cahier. "
            "Le stock dans un tableur, sur l'ordinateur du bureau.",
            REFRAIN_VO,
            "Ma fiche technique est dans un classeur. Le prix de mes matières a bougé la "
            "semaine dernière. Ni le classeur ni le tableur ne le savent.",
            "Alors je recopie. Le même chiffre, trois fois, à trois endroits. "
            "Et une fois sur trois, je me trompe.",
            "Deux heures de saisie avant même d'avoir allumé un piano.",
            "Onze heures. Le service commence. Ma traçabilité du matin n'est toujours pas "
            "enregistrée.",
        ],
    },
    "c2s-cuisine-pendant-sans": {
        "sous": "c2s", "metier": "cuisine", "phase": "pendant",
        "plates": ("couloir-cuisine", "tickets-empiles"),
        "chiffre": "24 couverts",
        "ouverture": ("Midi dix", "Trois écrans qui ne disent pas la même chose"),
        "cloture": ("Quatorze heures", "On a servi tout le monde, personne n'a compté"),
        "outils1": (["Carnet de salle", "Bloc téléphone", "Tablette web"],
                    ["Trois entrées", "Aucun total"]),
        "outils2": (["Bon de cuisine", "Écran de passe", "Carnet de salle"],
                    ["Personne ne sait", "On recompte"]),
        "compteur": [("5 à 8", "abonnements"),
                     ("30 à 45 min", "perdues par service"),
                     ("2 à 3", "plats sortis deux fois")],
        "vo": [
            "Midi dix. Trois canaux, trois écrans, trois sonneries qui ne disent pas la "
            "même chose.",
            "Les commandes de la salle arrivent sur un carnet. Celles du téléphone, sur un "
            "bout de papier. Celles du web, sur une tablette posée sur le frigo.",
            REFRAIN_VO,
            "Personne ne sait combien de plateaux sont en cours. Alors on crie. Et on "
            "recompte.",
            "Le nombre de couverts, je le recopie. D'un écran à l'autre, à la main, en "
            "plein coup de feu.",
            "Sur un seul service, ça fait une demi-heure perdue et des plats sortis deux fois.",
            "Quatorze heures. On a servi tout le monde. Personne ne sait combien on a vendu.",
        ],
    },
    "c3s-cuisine-apres-sans": {
        "sous": "c3s", "metier": "cuisine", "phase": "apres",
        "plates": ("cuisine-vide-nuit", "telephone-comptoir"),
        "chiffre": "1 240 €",
        "ouverture": ("Quinze heures", "Le service est fini, ma journée non"),
        "cloture": ("Dix-neuf heures", "Le classeur du mois est toujours à faire"),
        "outils1": (["Carnet de pertes", "Feuille nettoyage", "Relevé du matin"],
                    ["Rien n'est daté", "Rien n'est signé"]),
        "outils2": (["Bon fournisseur", "Tableur de stock", "Boîte mail"],
                    ["Commande de mémoire", "Stock réel inconnu"]),
        "compteur": [("5 à 8", "abonnements"),
                     ("4", "endroits pour un relevé"),
                     ("1 h à 1 h 30", "après la fermeture")],
        "vo": [
            "Quinze heures. Le service est fini. Ma journée, non.",
            "Les pertes sur un carnet. Le nettoyage sur une feuille plastifiée. Les "
            "températures du soir, encore sur la feuille du matin.",
            REFRAIN_VO,
            "Ma commande fournisseur, je la passe de mémoire. Mon stock réel, je ne l'ai "
            "jamais vraiment su.",
            "Le chiffre du midi, je le recopie du carnet vers le tableur, et du tableur vers "
            "le mail du comptable.",
            "Une inspection demanderait ces relevés. Ils sont dans quatre endroits différents.",
            "Dix-neuf heures. Je rentre. Le classeur du mois est toujours à faire.",
        ],
    },
    # ── Salle ────────────────────────────────────────────────────────────
    "s1s-salle-avant-sans": {
        "sous": "s1s", "metier": "salle", "phase": "avant",
        "plates": ("salle-chaises", "salle-prete"),
        "chiffre": "20 h 30",
        "ouverture": ("Neuf heures", "La salle est vide, le téléphone non"),
        "cloture": ("Midi", "Je ne sais pas combien de couverts j'ai ce soir"),
        "outils1": (["Cahier réservations", "Boîte mail", "Bloc téléphone"],
                    ["Trois listes", "Aucune vue d'ensemble"]),
        "outils2": (["Plan de salle papier", "Cahier réservations", "Liste d'attente"],
                    ["Dans ma tête", "Nulle part ailleurs"]),
        "compteur": [("5 à 8", "abonnements"),
                     ("3", "endroits pour une réservation"),
                     ("1 à 2", "tables données deux fois par mois")],
        "vo": [
            "Neuf heures. La salle est vide. Le téléphone, lui, a déjà sonné trois fois.",
            "Les réservations sur un cahier. Celles du web dans une boîte mail. Celles du "
            "téléphone, sur un papier collé à la caisse.",
            REFRAIN_VO,
            "Le plan de salle est dans ma tête. Quand je ne suis pas là, il n'existe plus.",
            "Un client rappelle pour changer d'heure. Je cherche son nom à trois endroits "
            "avant de le trouver.",
            "Une ou deux tables données deux fois par mois. C'est peu. Ça suffit pour perdre "
            "un habitué.",
            "Midi. On ouvre. Je ne sais toujours pas combien de couverts j'ai ce soir.",
        ],
    },
    "s2s-salle-pendant-sans": {
        "sous": "s2s", "metier": "salle", "phase": "pendant",
        "plates": ("sans-tablettes", "telephone-comptoir"),
        "chiffre": "Table 12",
        "ouverture": ("Midi trente", "Trois tablettes, aucune ne parle à l'autre"),
        "cloture": ("Quinze heures", "Tout le monde a mangé, personne n'a compté"),
        "outils1": (["Carnet de commande", "Caisse", "Bon de cuisine"],
                    ["On retape", "On recrie"]),
        "outils2": (["Carte du jour", "Écran de cuisine", "Site de commande"],
                    ["La cuisine sait", "Le site jamais"]),
        "compteur": [("5 à 8", "abonnements"),
                     ("3", "saisies pour un couvert"),
                     ("1", "addition fausse par semaine")],
        "vo": [
            "Midi trente. Trois tablettes derrière le comptoir. Aucune ne parle à l'autre.",
            "La commande se prend sur un carnet, se retape sur la caisse, et se recrie en "
            "cuisine.",
            REFRAIN_VO,
            "Un plat n'est plus disponible. La cuisine le sait. La salle, dans dix minutes. "
            "Le site de commande, jamais.",
            "Le numéro de table, je le retape à chaque étape. Trois fois pour un seul couvert.",
            "Sur un service complet, ça fait des dizaines de ressaisies. Et une addition "
            "fausse par semaine.",
            "Quinze heures. Tout le monde a mangé. Personne n'a compté.",
        ],
    },
    "s3s-salle-apres-sans": {
        "sous": "s3s", "metier": "salle", "phase": "apres",
        "plates": ("imprimante-z", "salle-apres"),
        "chiffre": "2 318 €",
        "ouverture": ("Vingt-trois heures", "La dernière table est partie"),
        "cloture": ("Minuit passé", "Le rapprochement, je le ferai dimanche"),
        "outils1": (["Ticket de caisse", "Titres restaurant", "Enveloppe pourboires"],
                    ["Trois piles", "Un seul total attendu"]),
        "outils2": (["Fond de caisse", "Cahier de soirée", "Tableur du mois"],
                    ["Écart inexpliqué", "Personne ne saura"]),
        "compteur": [("5 à 8", "abonnements"),
                     ("20 à 40 min", "chaque soir"),
                     ("5 à 7", "semaines par an")],
        "vo": [
            "Vingt-trois heures. La dernière table est partie.",
            "La caisse d'un côté. Les titres restaurant de l'autre. Les pourboires dans une "
            "enveloppe.",
            REFRAIN_VO,
            "Mon fond de caisse ne tombe pas juste. Il manque quelques euros. Personne ne "
            "saura jamais d'où ils viennent.",
            "Le total de la soirée, je le recopie du ticket vers un cahier, puis du cahier "
            "vers un tableur.",
            "Une demi-heure par soir. Sur une année, ça fait plus de cinq semaines de travail.",
            "Minuit passé. Je ferme. Le rapprochement, je le ferai dimanche.",
        ],
    },
    # ── Direction ────────────────────────────────────────────────────────
    # D1′ est le film pilote du volet (NOTES §6.5) : sept onglets, sept
    # identifiants, sept prélèvements. Le plus universel, et celui qui décide
    # si la série entière tient.
    "d1s-direction-avant-sans": {
        "sous": "d1s", "metier": "direction", "phase": "avant",
        "plates": ("sans-onglets", "bureau-matin"),
        "chiffre": "3 640 €",
        "ouverture": ("Huit heures", "Sept onglets s'ouvrent avec mon ordinateur"),
        "cloture": ("Dix heures", "Je n'ai rien décidé, j'ai seulement rassemblé"),
        "outils1": (["Planning", "Stocks", "Caisse"],
                    ["Trois connexions", "Aucun recoupement"]),
        "outils2": (["Avis clients", "Comptabilité", "Campagnes"],
                    ["Sept identifiants", "Sept prélèvements"]),
        "compteur": [("5 à 8", "abonnements"),
                     ("350 à 900 €", "par mois"),
                     ("0", "qui parle aux autres")],
        "vo": [
            "Huit heures. J'ouvre mon ordinateur. Sept onglets s'ouvrent avec lui.",
            "Un pour le planning. Un pour les stocks. Un pour la caisse. Un pour les avis. "
            "Un pour la comptabilité. Et deux dont je ne sais plus très bien à quoi ils "
            "servent.",
            REFRAIN_VO,
            "Sept identifiants. Sept mots de passe. Sept prélèvements sur le même compte, à "
            "sept dates différentes.",
            "Et pour savoir ce que j'ai vendu hier, je recopie le même chiffre d'un onglet à "
            "l'autre.",
            "Entre trois cent cinquante et neuf cents euros par mois. Pour des outils qui ne "
            "se parlent pas.",
            "Dix heures. Je n'ai encore rien décidé. J'ai seulement rassemblé.",
        ],
    },
    "d2s-direction-pendant-sans": {
        "sous": "d2s", "metier": "direction", "phase": "pendant",
        "plates": ("bureau-matin", "tickets-empiles"),
        "chiffre": "1 890 €",
        "ouverture": ("Onze heures quinze", "Le service a commencé, je ne le vois pas"),
        "cloture": ("Quatorze heures", "Je découvre ce qui s'est passé"),
        "outils1": (["Écran de cuisine", "Caisse", "Tableur de stock"],
                    ["Ce soir", "Demain", "La semaine prochaine"]),
        "outils2": (["Campagnes", "Fichier clients", "Avis clients"],
                    ["Je l'écris moi-même", "Le soir"]),
        "compteur": [("5 à 8", "abonnements"),
                     ("24 h", "de retard sur mes chiffres"),
                     ("3", "outils pour une campagne")],
        "vo": [
            "Onze heures quinze. Le service a commencé. Je ne le vois pas.",
            "Ce qui tourne en cuisine, je l'apprendrai ce soir. Ce qui coince en salle, "
            "demain. Ce qui manque en stock, la semaine prochaine.",
            REFRAIN_VO,
            "Ma campagne du mois, je l'écris moi-même, le soir, sur un outil que j'ai payé "
            "pour ne pas avoir à le faire.",
            "Mon chiffre de la veille, je vais le chercher. Puis je le retape ailleurs pour "
            "pouvoir le comparer.",
            "Décider avec les chiffres d'hier, c'est décider en retard.",
            "Quatorze heures. Le service est fini. Je découvre seulement ce qui s'y est passé.",
        ],
    },
    "d3s-direction-apres-sans": {
        "sous": "d3s", "metier": "direction", "phase": "apres",
        "plates": ("sans-onglets", "devanture-nuit"),
        "chiffre": "4 275 €",
        "ouverture": ("Quinze heures", "L'heure des choses qu'on repousse"),
        "cloture": ("Dix-neuf heures", "Ma journée est finie, mon classeur non"),
        "outils1": (["Facturier", "Modèle de devis", "Portail déclaratif"],
                    ["Trois fois les mêmes coordonnées"]),
        "outils2": (["Caisse", "Tableur du mois", "Comptabilité"],
                    ["Données éparpillées", "Aucune réponse"]),
        "compteur": [("5 à 8", "abonnements"),
                     ("2 h 14", "tous les soirs"),
                     ("3", "saisies en double")],
        "vo": [
            "Quinze heures. L'heure des choses qu'on repousse toujours.",
            "Une facture à faire. Un devis à envoyer. Une déclaration à déposer. Trois "
            "outils, et trois fois les mêmes coordonnées à retaper.",
            REFRAIN_VO,
            "Je voudrais savoir ce qui marche et ce qu'il faut arrêter. Personne ne peut me "
            "le dire : mes données sont éparpillées.",
            "Le montant du devis, je le reprends du tableur. À la main. Une virgule mal "
            "placée, et c'est ma marge.",
            "Deux heures quatorze, tous les soirs. Trois saisies en double. Sept abonnements.",
            "Dix-neuf heures. Ma journée est finie. Mon classeur du mois, non.",
        ],
    },
}

# La punchline ferme les neuf films, mot pour mot. Elle est dite, pas seulement
# écrite : c'est la demande de Michael, et c'est aussi ce qui fait résoudre la
# phrase musicale sur sa tonique (NOTES §6.3).
PUNCHLINE_VO = ("Avec FoodEatUp, une seule application. La solution qui s'occupe de "
                "votre établissement, avant, pendant et après votre service.")
