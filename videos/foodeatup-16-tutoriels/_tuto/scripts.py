#!/usr/bin/env python3
"""Les seize tutoriels encore en coquille, écrits.

**D'où vient le contenu.** Ces seize fiches n'ont jamais été tournées : leur
`howItWorks` disait « Cette vidéo est en cours de tournage », et leur
`whatItsFor` répétait le titre. Il n'y avait donc rien à adapter — il fallait
écrire le geste lui-même.

La source est le connecteur MCP de FoodEatUp. Chaque outil porte sa description,
ses paramètres et ses contraintes : `record_pos_payment` dit que le titre-restaurant
ne rend jamais la monnaie, `close_pos_session` qu'il exige une confirmation après
avoir résumé le rapport X, `get_hubrise_status` qu'un plat sans `sku_ref` est
bloqué au push. Ce sont des faits du produit, pas des suppositions : c'est ce qui
sépare un tutoriel utile d'une paraphrase de menu.

⚠️ **Ce que ces films ne sont pas.** Les tutoriels de la série sont montés sur
des captures d'écran réelles. Ceux-ci n'en ont pas. Ils sont donc en motion
design assumé — schématiques, jamais mimétiques : aucun plan ne prétend être
une capture du produit. Le jour où Michael fournit les rushes, ces films sont
remplacés, et les scripts restent — c'est le travail long.

**Le doublon écarté.** `retrouver-toutes-mes-commandes` portait le même sujet
que `mes-commandes-tous-canaux` et `retrouver-ses-commandes-multi-canal`, tous
deux déjà en ligne. Une troisième page sur la même intention se serait
cannibalisée avec les deux autres — exactement ce que le travail de
référencement combat. La fiche est donc reprise sous son angle comptable : la
commande vue depuis sa facture.
"""

# Voix off : Adam - Instructor (ElevenLabs), eleven_multilingual_v2, fr.
VOIX = "TGAegA0zNRi8I6nUdq3i"

# La ligne « avec Claude », commune à toute la série : elle est ajoutée par le
# monteur à chaque tutoriel qui porte un prompt. Reprise telle quelle des
# tutoriels déjà publiés — trois formulations pour le même geste, ce serait
# trois façons de l'expliquer, et qui enchaîne deux tutoriels le remarque.
CLAUDE = ("Vous pouvez aussi le faire depuis Claude : copiez ce prompt, "
          "remplacez les crochets, et collez-le dans la conversation.")

# La ligne de clôture, commune à toute la série.
CTA = "Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui !"


def t(slug, module, sous, titre, intention, a_quoi, etapes, astuce, vo, boards,
      outils, prompt=None, titre_fiche=None):
    return {
        "slug": slug, "module": module, "sous": sous, "titre": titre,
        "titre_fiche": titre_fiche or titre, "intention": intention,
        "a_quoi": a_quoi, "etapes": etapes, "astuce": astuce,
        "vo": vo, "boards": boards, "outils": outils, "prompt": prompt,
    }


TUTORIELS = [

    # ── Caisse POS & Matériel ───────────────────────────────────────────────
    t(
        "configurer-sa-caisse-pos", "caisse-pos", "t01",
        "Configurer sa caisse POS — TPE & ticket",
        "Préparer la caisse avant le premier encaissement.",
        "Une caisse mal déclarée se voit au premier service : le TPE ne répond pas, "
        "le ticket sort sans mentions légales, et personne ne sait quel terminal a "
        "encaissé quoi. Ce réglage se fait une fois, et il porte tout le reste.",
        [
            "Déclarez vos îlots d'encaissement : un comptoir, une terrasse, un bar sont trois points de vente distincts.",
            "Appairez chaque terminal Smile&Pay à son îlot, et désignez celui qui sert par défaut.",
            "Renseignez l'en-tête du ticket : raison sociale, adresse, numéro de TVA. Ce sont les mentions obligatoires.",
            "Testez un encaissement à un euro, puis annulez-le : c'est le seul moyen de vérifier la chaîne complète avant le service.",
        ],
        "Nommez vos terminaux par leur place réelle — « Comptoir », « Terrasse » — jamais par leur numéro de série. "
        "Le jour où un écart apparaît, vous cherchez un endroit, pas un numéro.",
        [
            ("N0", "Avant le premier encaissement, la caisse se déclare une fois. Ce réglage porte tout le reste."),
            ("N1", "Commencez par vos îlots : un comptoir, une terrasse, un bar sont trois points de vente distincts."),
            ("N2", "Appairez chaque terminal Smile&Pay à son îlot, et désignez celui qui sert par défaut."),
            ("N3", "Renseignez l'en-tête du ticket : raison sociale, adresse, numéro de TVA. Ce sont les mentions obligatoires."),
            ("N4", "Puis testez un encaissement à un euro, et annulez-le. C'est le seul moyen de vérifier la chaîne complète avant le service."),
            ("CTA", CTA),
        ],
        ["îlots", "terminaux", "ticket", "test à 1 €"],
        ["list_payment_terminals"],
        "Liste mes terminaux de paiement pour l'établissement [ID] : "
        "libellé, îlot, lequel est actif par défaut, et la date de dernière utilisation.",
    ),

    t(
        "ouvrir-son-fond-de-caisse", "caisse-pos", "t02",
        "Ouvrir son fond de caisse en début de service",
        "Ouvrir la session avant le premier client.",
        "Tant que la session n'est pas ouverte, aucun encaissement ne se rattache à "
        "personne ni à un fond de départ. L'écart de fin de service devient alors "
        "inexplicable — non pas grand, mais impossible à attribuer.",
        [
            "Choisissez l'opérateur : seul un employé disposant de la permission caisse peut ouvrir une session.",
            "Comptez le fond de caisse réel et saisissez-le, au centime. C'est la référence de tout l'écart de ce soir.",
            "Validez : la session s'ouvre, et chaque encaissement s'y rattache automatiquement.",
            "Une seule session à la fois par établissement : si elle est déjà ouverte, c'est la précédente qu'il faut clôturer.",
        ],
        "Saisissez le fond compté, pas le fond théorique. Reporter le montant d'hier parce que « ça n'a pas bougé » "
        "revient à effacer l'écart d'hier dans celui d'aujourd'hui.",
        [
            ("N0", "Le fond de caisse s'ouvre avant le premier client. Sans session ouverte, aucun encaissement ne se rattache à personne."),
            ("N1", "Choisissez l'opérateur : seul un employé avec la permission caisse peut ouvrir une session."),
            ("N2", "Comptez le fond réel, et saisissez-le au centime. C'est la référence de tout l'écart de ce soir."),
            ("N3", "Validez : la session s'ouvre, et chaque encaissement s'y rattache tout seul."),
            ("N4", "Une seule session à la fois. Si elle est déjà ouverte, c'est la précédente qu'il faut clôturer."),
            ("CTA", CTA),
        ],
        ["opérateur", "comptage", "ouverture", "une seule"],
        ["open_pos_session", "get_pos_session"],
        "Ouvre la caisse de l'établissement [ID] avec un fond de [MONTANT] euros, "
        "opérateur [ID EMPLOYÉ].",
    ),

    t(
        "encaisser-une-commande", "caisse-pos", "t03",
        "Encaisser une commande — comptoir & table",
        "Solder une note, quel que soit le moyen de paiement.",
        "Encaisser, ce n'est pas enregistrer un total : c'est faire tomber le reste "
        "dû à zéro. Tant qu'il ne l'est pas, la note reste ouverte — et c'est cette "
        "règle qui rend possibles les paiements partagés et les acomptes.",
        [
            "Ouvrez la note, au comptoir ou à la table : le reste dû s'affiche.",
            "Choisissez le moyen : espèces, carte, titre-restaurant ou chèque.",
            "En espèces, saisissez le montant remis — le rendu se calcule tout seul.",
            "Le titre-restaurant ne rend jamais la monnaie : le surplus est perdu pour le client, jamais rendu en pièces.",
            "La note se solde d'elle-même quand le reste dû atteint zéro.",
        ],
        "Saisissez toujours le montant réellement remis, même quand il est rond. C'est ce chiffre qui alimente "
        "le rendu, et c'est lui qu'on relit quand un écart apparaît le soir.",
        [
            ("N0", "Encaisser, ce n'est pas enregistrer un total. C'est faire tomber le reste dû à zéro."),
            ("N1", "Ouvrez la note, au comptoir ou à la table : le reste dû s'affiche."),
            ("N2", "Choisissez le moyen : espèces, carte, titre-restaurant ou chèque."),
            ("N3", "En espèces, saisissez le montant remis. Le rendu se calcule tout seul."),
            ("N4", "Attention au titre-restaurant : il ne rend jamais la monnaie. Le surplus est perdu, jamais rendu en pièces."),
            ("N5", "Et la note se solde d'elle-même dès que le reste dû atteint zéro."),
            ("CTA", CTA),
        ],
        ["la note", "le mode", "le rendu", "soldée"],
        ["record_pos_payment", "list_pos_payments"],
        "Encaisse la commande [ID] de l'établissement [ID] : [MONTANT] euros en "
        "[especes / carte / titre_restaurant / cheque], opérateur [ID EMPLOYÉ]. "
        "Pour des espèces, indique aussi le montant remis par le client.",
    ),

    t(
        "appliquer-une-remise", "caisse-pos", "t04",
        "Appliquer une remise et des avoirs",
        "Accorder un geste commercial sans perdre la trace.",
        "Une remise accordée de tête et non saisie disparaît deux fois : du ticket "
        "du client, et du rapport de caisse. À la fin du mois, le chiffre manque et "
        "personne ne sait pourquoi.",
        [
            "Appliquez la remise sur la note avant l'encaissement, jamais après : une note soldée ne se remise plus.",
            "Choisissez le motif — geste commercial, plat non conforme, avoir. C'est lui qu'on relit dans le rapport.",
            "Un avoir se pose sur la note suivante du même client : c'est une créance, pas une ristourne.",
            "Le rapport de caisse totalise les remises à part du chiffre d'affaires : la marge reste lisible.",
        ],
        "Une remise sans motif est une remise perdue. Le montant, on le retrouve ; la raison, jamais — "
        "et c'est la raison qui dit s'il faut changer le plat ou changer le fournisseur.",
        [
            ("N0", "Une remise accordée de tête et non saisie disparaît deux fois : du ticket, et du rapport."),
            ("N1", "Appliquez-la sur la note avant l'encaissement. Une note soldée ne se remise plus."),
            ("N2", "Choisissez le motif : geste commercial, plat non conforme, avoir. C'est lui qu'on relit ensuite."),
            ("N3", "Un avoir, lui, se pose sur la note suivante du même client. C'est une créance, pas une ristourne."),
            ("N4", "Le rapport totalise les remises à part du chiffre d'affaires : la marge reste lisible."),
            ("CTA", CTA),
        ],
        ["avant paiement", "le motif", "l'avoir", "le rapport"],
        ["get_pos_report"],
        None,  # aucun outil MCP ne pose une remise : ne pas en inventer un.
    ),

    t(
        "separer-une-addition", "caisse-pos", "t05",
        "Séparer une addition — multi-paiement",
        "Faire payer une même note à plusieurs, sans recompter.",
        "Une table de six qui paie en trois fois, c'est trois paiements sur une seule "
        "note — pas trois notes. La différence compte : une seule commande part en "
        "cuisine, une seule facture sort, et le reste dû se recalcule tout seul.",
        [
            "Gardez une seule note : c'est elle qui porte les plats et le total.",
            "Encaissez un premier paiement partiel — le reste dû se recalcule immédiatement.",
            "Changez de moyen entre deux paiements : carte pour l'un, espèces pour l'autre, titre-restaurant pour un troisième.",
            "Répétez jusqu'à zéro : la note se solde à l'instant où le reste dû est couvert.",
            "Relisez la liste des paiements : chaque part, son moyen, son rendu.",
        ],
        "Ne créez jamais plusieurs notes pour partager une addition. Vous doubleriez la commande en cuisine "
        "et vous perdriez le total réel de la table.",
        [
            ("N0", "Une table de six qui paie en trois fois, c'est trois paiements sur une seule note — pas trois notes."),
            ("N1", "Gardez une seule note : c'est elle qui porte les plats et le total."),
            ("N2", "Encaissez un premier paiement partiel. Le reste dû se recalcule immédiatement."),
            ("N3", "Changez de moyen entre deux paiements : carte pour l'un, espèces pour l'autre."),
            ("N4", "Répétez jusqu'à zéro. La note se solde à l'instant où le reste dû est couvert."),
            ("N5", "Et relisez la liste des paiements : chaque part, son moyen, son rendu."),
            ("CTA", CTA),
        ],
        ["une note", "paiement partiel", "modes", "soldée"],
        ["record_pos_payment", "list_pos_payments"],
        "Montre-moi les paiements de la commande [ID] pour l'établissement [ID] : "
        "les modes, les montants, le rendu et le reste dû.",
    ),

    t(
        "cloturer-sa-caisse", "caisse-pos", "t06",
        "Clôturer sa caisse — le Z de caisse",
        "Fermer la journée et figer les chiffres.",
        "La clôture n'est pas une formalité de fin de service : c'est elle qui fige "
        "le chiffre d'affaires du jour, sa ventilation de TVA et son écart. Une "
        "session qu'on oublie de fermer emporte le service du lendemain avec elle.",
        [
            "Lisez le rapport X avant de compter : c'est l'état de la session en cours, chiffre d'affaires, modes de paiement, TVA, remises.",
            "Comptez les espèces en caisse et saisissez le montant compté.",
            "Confirmez : l'écart se calcule entre le théorique et le compté.",
            "Le rapport Z est alors figé. Il ne se recalcule plus, même si une correction arrive après.",
        ],
        "Lisez toujours le X avant de compter, jamais après. Connaître le montant théorique avant de compter, "
        "c'est se donner une chance de compter deux fois quand ça ne tombe pas juste.",
        [
            ("N0", "La clôture fige le chiffre du jour, sa TVA et son écart. Une session oubliée emporte le service du lendemain."),
            ("N1", "Lisez le rapport X avant de compter : la session en cours, son chiffre, ses modes de paiement, sa TVA, ses remises."),
            ("N2", "Comptez les espèces, et saisissez le montant compté."),
            ("N3", "Confirmez : l'écart se calcule entre le théorique et le compté."),
            ("N4", "Le rapport Z est figé. Il ne se recalcule plus, même si une correction arrive après."),
            ("CTA", CTA),
        ],
        ["rapport X", "comptage", "écart", "Z figé"],
        ["get_pos_report", "close_pos_session"],
        "Résume-moi le rapport X de la caisse de l'établissement [ID], puis clôture "
        "la session avec un comptage espèces de [MONTANT] euros, opérateur [ID EMPLOYÉ].",
    ),

    t(
        "suivre-les-ecarts-de-caisse", "caisse-pos", "t07",
        "Suivre les écarts de caisse — historique",
        "Lire les écarts sur la durée plutôt qu'au jour le jour.",
        "Un écart isolé ne dit rien : on rend mal la monnaie, ça arrive. C'est la "
        "répétition qui parle — toujours le même opérateur, toujours le même "
        "service, toujours le même sens.",
        [
            "Ouvrez l'historique des sessions clôturées : chacune porte son rapport Z.",
            "Comparez l'écart par session, pas seulement son montant : son signe compte autant.",
            "Ventilez par opérateur : un écart qui suit une personne n'a pas la même cause qu'un écart qui suit un service.",
            "Ventilez par moyen de paiement : un écart qui ne touche que les espèces désigne le rendu de monnaie.",
        ],
        "Un écart toujours négatif du même montant n'est presque jamais un vol : c'est un fond de caisse "
        "mal saisi à l'ouverture, qui se reproduit chaque jour.",
        [
            ("N0", "Un écart isolé ne dit rien. C'est la répétition qui parle."),
            ("N1", "Ouvrez l'historique des sessions clôturées : chacune porte son rapport Z."),
            ("N2", "Comparez les écarts, et regardez leur signe autant que leur montant."),
            ("N3", "Ventilez par opérateur : un écart qui suit une personne n'a pas la même cause qu'un écart qui suit un service."),
            ("N4", "Puis par moyen de paiement : un écart qui ne touche que les espèces désigne le rendu de monnaie."),
            ("CTA", CTA),
        ],
        ["historique", "signe", "opérateur", "moyen"],
        ["get_pos_report"],
        "Donne-moi le rapport Z de la session [ID SESSION] de l'établissement [ID] : "
        "chiffre d'affaires, ticket moyen, ventilation par mode et par opérateur, TVA, remises.",
    ),

    # ── HubRise & Livraisons ────────────────────────────────────────────────
    t(
        "connecter-son-hubrise", "hubrise-livraisons", "t08",
        "Connecter son HubRise à FoodEatUp",
        "Brancher le connecteur qui relie les plateformes à la carte.",
        "HubRise est le point de passage : c'est lui qui parle aux plateformes de "
        "livraison, et FoodEatUp qui parle à HubRise. Une seule connexion à tenir, "
        "au lieu d'une par plateforme.",
        [
            "Créez ou reliez votre compte HubRise depuis FoodEatUp.",
            "Choisissez la location : c'est le point de vente précis, pas l'enseigne. Une erreur ici envoie les commandes au mauvais établissement.",
            "Autorisez le connecteur, puis vérifiez son état : connecté, location reconnue.",
            "Contrôlez enfin les commandes du jour restées en attente côté plateformes — elles disent si le flux passe vraiment.",
        ],
        "Vérifiez la location avant tout le reste. Une enseigne à deux adresses a deux locations, "
        "et rien dans l'interface ne vous dira que vous avez choisi la mauvaise.",
        [
            ("N0", "HubRise est le point de passage : il parle aux plateformes, et FoodEatUp lui parle. Une seule connexion à tenir."),
            ("N1", "Créez ou reliez votre compte HubRise depuis FoodEatUp."),
            ("N2", "Choisissez la location : le point de vente précis, pas l'enseigne. Une erreur ici envoie les commandes au mauvais établissement."),
            ("N3", "Autorisez le connecteur, puis vérifiez son état : connecté, location reconnue."),
            ("N4", "Et contrôlez les commandes du jour restées en attente côté plateformes. C'est elles qui disent si le flux passe."),
            ("CTA", CTA),
        ],
        ["compte", "location", "autorisation", "contrôle"],
        ["get_hubrise_status"],
        "Donne-moi l'état du connecteur HubRise de l'établissement [ID] : connexion, "
        "location, plats bloqués au push, commandes du jour en attente côté plateformes.",
    ),

    t(
        "relier-uber-eats-et-deliveroo", "hubrise-livraisons", "t09",
        "Relier Uber Eats & Deliveroo via HubRise",
        "Faire arriver les commandes des plateformes dans la même liste.",
        "Chaque plateforme se relie une fois, à HubRise, pas à FoodEatUp. Les "
        "commandes descendent ensuite dans la liste unique — mêmes statuts, même "
        "cuisine, même comptabilité que les commandes sur place.",
        [
            "Reliez chaque plateforme depuis votre compte HubRise, l'une après l'autre.",
            "Rattachez-les à la même location que celle choisie pour FoodEatUp.",
            "Attendez une première commande réelle : c'est le seul test qui vaille.",
            "Vérifiez qu'elle apparaît bien dans vos commandes, avec son canal d'origine.",
        ],
        "Ne testez pas avec une commande fictive passée depuis votre propre téléphone hors zone de livraison : "
        "elle est refusée par la plateforme avant d'atteindre HubRise, et vous conclurez à tort que le lien ne marche pas.",
        [
            ("N0", "Chaque plateforme se relie une fois, à HubRise, pas à FoodEatUp."),
            ("N1", "Reliez-les l'une après l'autre depuis votre compte HubRise."),
            ("N2", "Rattachez-les à la même location que celle choisie pour FoodEatUp."),
            ("N3", "Puis attendez une première commande réelle. C'est le seul test qui vaille."),
            ("N4", "Vérifiez qu'elle apparaît dans vos commandes, avec son canal d'origine."),
            ("CTA", CTA),
        ],
        ["par plateforme", "même location", "commande réelle", "canal"],
        ["get_hubrise_status", "list_orders"],
        "Vérifie l'état HubRise de l'établissement [ID], puis liste les commandes "
        "du jour pour voir celles qui viennent des plateformes.",
    ),

    t(
        "synchroniser-sa-caisse-tierce", "hubrise-livraisons", "t10",
        "Synchroniser sa caisse tierce via HubRise",
        "Faire correspondre les plats de part et d'autre.",
        "La synchronisation ne tient qu'à une chose : la référence de chaque plat. "
        "Sans elle, le plat existe des deux côtés sans que rien ne les relie, et il "
        "est purement et simplement bloqué au push.",
        [
            "Renseignez la référence — le sku_ref — de chaque plat de votre carte.",
            "Reprenez exactement la référence de la caisse tierce : une majuscule d'écart suffit à casser le lien.",
            "Relancez la synchronisation.",
            "Relisez l'état du connecteur : il liste nommément les plats sans référence, donc bloqués.",
        ],
        "Traitez la liste des plats sans référence comme une liste de courses : tant qu'elle n'est pas vide, "
        "la carte est incomplète chez le client, et personne ne vous le signalera.",
        [
            ("N0", "La synchronisation ne tient qu'à une chose : la référence de chaque plat."),
            ("N1", "Renseignez le sku_ref de chaque plat de votre carte."),
            ("N2", "Reprenez exactement la référence de la caisse tierce. Une majuscule d'écart suffit à casser le lien."),
            ("N3", "Relancez la synchronisation."),
            ("N4", "Et relisez l'état du connecteur : il liste nommément les plats sans référence, donc bloqués au push."),
            ("CTA", CTA),
        ],
        ["sku_ref", "à la lettre", "synchro", "plats bloqués"],
        ["get_hubrise_status", "list_dishes"],
        "Liste les plats de l'établissement [ID] qui n'ont pas de sku_ref et sont "
        "donc bloqués au push HubRise.",
    ),

    t(
        "centraliser-les-commandes-livraison", "hubrise-livraisons", "t11",
        "Centraliser les commandes — flux livraison",
        "Tenir un seul flux, quelle que soit la provenance.",
        "Une commande de plateforme n'est pas une commande à part : elle entre dans "
        "la même liste, avec les mêmes statuts, et part en cuisine par le même "
        "chemin. Ce qui change, c'est son canal — et c'est la seule chose à savoir.",
        [
            "Ouvrez vos commandes : toutes y sont, tous canaux confondus.",
            "Filtrez par canal pour isoler la livraison — sur place, vitrine, téléphone, agent vocal, plateformes.",
            "Suivez le statut comme pour n'importe quelle commande : en attente, confirmée, en préparation, prête, livrée.",
            "Surveillez les commandes du jour restées en attente côté plateformes : ce sont celles qui n'ont pas franchi le connecteur.",
        ],
        "Ne traitez pas les commandes de livraison sur un écran séparé. Un service qui regarde deux listes "
        "en oublie une, toujours la même, toujours au coup de feu.",
        [
            ("N0", "Une commande de plateforme n'est pas une commande à part. Même liste, mêmes statuts, même cuisine."),
            ("N1", "Ouvrez vos commandes : toutes y sont, tous canaux confondus."),
            ("N2", "Filtrez par canal pour isoler la livraison."),
            ("N3", "Suivez le statut comme pour n'importe quelle commande : en attente, confirmée, en préparation, prête, livrée."),
            ("N4", "Et surveillez celles restées en attente côté plateformes : ce sont celles qui n'ont pas franchi le connecteur."),
            ("CTA", CTA),
        ],
        ["une liste", "filtre canal", "les statuts", "en attente"],
        ["list_orders", "get_hubrise_status", "update_order_status"],
        "Liste les commandes du jour de l'établissement [ID], canal par canal, "
        "et signale celles encore en attente côté plateformes.",
    ),

    # ── Écran Cuisine (KDS) ─────────────────────────────────────────────────
    t(
        "gerer-une-commande-en-direct-kds", "kds-cuisine", "t12",
        "Gérer une commande en direct sur le KDS",
        "Faire avancer un ticket plat par plat, pendant le service.",
        "Le KDS ne suit pas des commandes, il suit des plats. C'est ce qui permet à "
        "une entrée de partir pendant qu'un plat chaud cuit encore, sans que le "
        "ticket entier attende le plus lent.",
        [
            "Le ticket arrive au poste concerné dès que la commande est confirmée.",
            "Faites avancer chaque plat séparément : à faire, en cours, prêt, servi.",
            "Passez un plat en « en cours » quand vous le commencez, pas quand vous le voyez : c'est ce qui rend le compteur d'attente juste.",
            "« Prêt » l'envoie au pass. Le ticket ne disparaît qu'une fois tous ses plats servis.",
            "La charge des postes se met à jour à chaque changement : elle dit où ça bloque, en direct.",
        ],
        "Le passage en « en cours » est le seul geste que personne ne fait spontanément — et c'est le seul "
        "qui rende le temps d'attente crédible. Sans lui, tout paraît prêt d'un coup.",
        [
            ("N0", "Le KDS ne suit pas des commandes, il suit des plats. L'entrée part pendant que le chaud cuit."),
            ("N1", "Le ticket arrive au poste dès que la commande est confirmée."),
            ("N2", "Faites avancer chaque plat séparément : à faire, en cours, prêt, servi."),
            ("N3", "Passez un plat en « en cours » quand vous le commencez, pas quand vous le voyez. C'est ce qui rend le compteur d'attente juste."),
            ("N4", "« Prêt » l'envoie au pass. Le ticket ne disparaît qu'une fois tous ses plats servis."),
            ("N5", "Et la charge des postes se met à jour à chaque changement : elle dit où ça bloque, en direct."),
            ("CTA", CTA),
        ],
        ["par plat", "quatre statuts", "en cours", "charge des postes"],
        ["update_kds_item_status", "get_station_load"],
        "Passe le plat [ID ITEM] de l'établissement [ID] en statut "
        "[pending / in_progress / ready / served], puis donne-moi la charge des postes.",
    ),

    # ── Site Web & Vitrine ──────────────────────────────────────────────────
    t(
        "configurer-horaires-et-reservations-site", "site-web-vitrine", "t13",
        "Configurer ses horaires et réservations",
        "Ouvrir la réservation en ligne sans se retrouver complet à tort.",
        "Les horaires du site ne sont pas un affichage : ce sont eux qui ouvrent et "
        "ferment les créneaux de réservation. Une coupure oubliée l'après-midi, et "
        "le site accepte des tables à quinze heures.",
        [
            "Saisissez vos horaires jour par jour, coupures comprises.",
            "Activez la page réservations, puis publiez-la : tant qu'elle est en brouillon, elle n'existe pas pour le client.",
            "Réglez la durée d'un couvert et la capacité : c'est ce qui détermine combien de tables un créneau accepte.",
            "Vérifiez les disponibilités réelles sur une date donnée avant d'annoncer l'ouverture.",
            "Contrôlez enfin le domaine : une page publiée sur un domaine non validé reste invisible.",
        ],
        "Publiez la page réservations un jour de fermeture. Vous verrez les créneaux se fermer d'eux-mêmes — "
        "c'est la meilleure preuve que les horaires sont bien pris en compte.",
        [
            ("N0", "Les horaires du site ne sont pas un affichage : ce sont eux qui ouvrent et ferment les créneaux."),
            ("N1", "Saisissez-les jour par jour, coupures comprises."),
            ("N2", "Activez la page réservations, puis publiez-la. En brouillon, elle n'existe pas pour le client."),
            ("N3", "Réglez la durée d'un couvert et la capacité : c'est ce qui détermine combien de tables un créneau accepte."),
            ("N4", "Vérifiez les disponibilités réelles sur une date avant d'annoncer l'ouverture."),
            ("N5", "Et contrôlez le domaine : une page publiée sur un domaine non validé reste invisible."),
            ("CTA", CTA),
        ],
        ["horaires", "publier", "capacité", "domaine"],
        ["get_site_status", "toggle_site_page", "reservation_availability", "get_domain_status"],
        "Donne-moi l'état du site de l'établissement [ID] — pages publiées, URL, "
        "domaine — puis les disponibilités de réservation pour le [DATE].",
    ),

    # ── Marketing, Fidélité & Iris ──────────────────────────────────────────
    t(
        "voir-les-gagnants-historique", "marketing-fidelite", "t14",
        "Voir les gagnants — historique",
        "Savoir ce que la roue a réellement rapporté.",
        "Une roue cadeaux se juge sur deux chiffres, et ce ne sont pas les lancers : "
        "les contacts captés, et les lots effectivement retirés. Un lot gagné qui "
        "n'est jamais venu au restaurant n'a rien rapporté.",
        [
            "Ouvrez la roue : son statut, ses lancers, ses contacts captés.",
            "Lisez les statistiques : lancers, lots gagnés, leads. Le rapport entre les deux premiers dit si la roue est trop généreuse.",
            "Passez aux bons émis : actifs, utilisés, expirés.",
            "Ce sont les bons utilisés qui mesurent le retour — pas les lots gagnés.",
            "Un taux d'expiration élevé signale un lot peu désirable, ou une durée de validité trop courte.",
        ],
        "Comparez toujours les bons utilisés aux contacts captés, jamais aux lancers. Le lancer est gratuit "
        "pour le client ; c'est le déplacement qui coûte, et c'est lui qu'on mesure.",
        [
            ("N0", "Une roue cadeaux se juge sur deux chiffres, et ce ne sont pas les lancers."),
            ("N1", "Ouvrez la roue : son statut, ses lancers, ses contacts captés."),
            ("N2", "Lisez les statistiques. Le rapport entre lancers et lots gagnés dit si la roue est trop généreuse."),
            ("N3", "Puis passez aux bons émis : actifs, utilisés, expirés."),
            ("N4", "Ce sont les bons utilisés qui mesurent le retour — pas les lots gagnés."),
            ("N5", "Et un taux d'expiration élevé signale un lot peu désirable, ou une validité trop courte."),
            ("CTA", CTA),
        ],
        ["la roue", "les stats", "bons émis", "bons utilisés"],
        ["list_wheel_games", "get_wheel_stats", "list_redemptions"],
        "Donne-moi les statistiques de la roue [ID] de l'établissement [ID] — "
        "lancers, lots gagnés, leads — puis les bons fidélité émis par statut.",
    ),

    t(
        "integrer-le-mcp-rapidocms-iris", "marketing-fidelite", "t15",
        "Intégrer le MCP RapidoCMS & Iris",
        "Brancher son assistant sur le contenu et la vitrine.",
        "Le connecteur RapidoCMS donne à un assistant IA la main sur le contenu : "
        "visuels, publications, pages de la vitrine. Il vient en plus du connecteur "
        "FoodEatUp, qui lui tient le restaurant — deux connecteurs, deux périmètres.",
        [
            "Récupérez votre clé d'accès RapidoCMS depuis votre espace.",
            "Ajoutez le connecteur dans votre assistant : l'adresse est cms.rapidosoftware.com/mcp.",
            "Autorisez-le, puis vérifiez que votre marque et vos comptes connectés remontent.",
            "Gardez les deux connecteurs séparés : FoodEatUp pour le restaurant, RapidoCMS pour le contenu.",
            "Testez sur une demande sans effet — lister vos campagnes — avant toute publication.",
        ],
        "Testez toujours par une lecture avant une écriture. Un connecteur mal autorisé publie sur le mauvais "
        "compte, et une publication ne se rattrape pas.",
        [
            ("N0", "Le connecteur RapidoCMS donne à votre assistant la main sur le contenu : visuels, publications, vitrine."),
            ("N1", "Récupérez votre clé d'accès depuis votre espace RapidoCMS."),
            ("N2", "Ajoutez le connecteur dans votre assistant : cms point rapidosoftware point com, barre oblique, m c p."),
            ("N3", "Autorisez-le, puis vérifiez que votre marque et vos comptes connectés remontent."),
            ("N4", "Gardez les deux connecteurs séparés : FoodEatUp tient le restaurant, RapidoCMS tient le contenu."),
            ("N5", "Et testez sur une demande sans effet — lister vos campagnes — avant toute publication."),
            ("CTA", CTA),
        ],
        ["la clé", "le connecteur", "vérifier", "lire avant d'écrire"],
        [],
        "Liste mes campagnes RapidoCMS et les comptes sociaux connectés à ma marque.",
    ),

    # ── Comptabilité & Achats ───────────────────────────────────────────────
    t(
        "retrouver-toutes-mes-commandes", "comptabilite", "t16",
        "Retrouver la commande derrière une facture",
        "Rapprocher une écriture de la commande qui l'a produite.",
        "Chaque commande crée sa facture et son devis. Le rapprochement compte au "
        "moment du contrôle : retrouver, derrière une ligne comptable, ce qui a été "
        "servi, à qui, par quel canal — et vérifier que le statut des deux concorde.",
        [
            "Partez de la facture, et remontez à la commande qui l'a générée.",
            "Filtrez par canal, par statut ou par date pour retrouver une commande dont vous n'avez que l'à-peu-près.",
            "Ouvrez le détail : les articles, le client, le total, et les liens vers la facture et le devis.",
            "Vérifiez la concordance des statuts : changer celui de la commande se répercute sur la facture et le devis.",
            "Une commande annulée dont la facture reste ouverte est l'écart que le contrôle trouvera à votre place.",
        ],
        "Rapprochez au fil de l'eau, pas en fin de mois. Un écart de statut vieux de trois semaines demande "
        "de se souvenir du service — ce que personne ne fait.",
        [
            ("N0", "Chaque commande crée sa facture et son devis. Le rapprochement, lui, compte au moment du contrôle."),
            ("N1", "Partez de la facture, et remontez à la commande qui l'a générée."),
            ("N2", "Filtrez par canal, par statut ou par date quand vous n'avez que l'à-peu-près."),
            ("N3", "Ouvrez le détail : les articles, le client, le total, et les liens vers la facture et le devis."),
            ("N4", "Vérifiez la concordance des statuts : changer celui de la commande se répercute sur les deux."),
            ("N5", "Une commande annulée dont la facture reste ouverte est l'écart que le contrôle trouvera à votre place."),
            ("CTA", CTA),
        ],
        ["depuis la facture", "les filtres", "le détail", "concordance"],
        ["list_orders", "get_order", "get_invoice", "update_order_status"],
        "Retrouve la commande liée à la facture [NUMÉRO] de l'établissement [ID], "
        "et dis-moi si le statut de la commande et celui de la facture concordent.",
        titre_fiche="Retrouver la commande derrière une facture",
    ),
]

assert len(TUTORIELS) == 16, f"{len(TUTORIELS)} tutoriels, 16 attendus"
_slugs = [x["slug"] for x in TUTORIELS]
assert len(set(_slugs)) == 16, "slug en double"
