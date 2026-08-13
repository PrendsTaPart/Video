# -*- coding: utf-8 -*-
"""Saison 6 — L'orchestration du restaurant.

Renversement de la série : les cinq premières saisons montrent le logiciel,
celle-ci montre le restaurant. Chaque épisode est un contenu qu'un restaurateur
pourrait publier tel quel sur son propre compte — et c'est là tout l'argument :
si la vidéo donne envie de venir manger, c'est que la méthode marche.

FoodEatUp n'est jamais le sujet. Il est ce qui rend le contenu possible : la
fiche recette qui donne les mots exacts, la carte qui fournit la photo, Iris qui
programme, RapidoCMS qui publie, la réservation qui revient.

Le chef joue tous les rôles. C'est un choix de production autant qu'un ressort
comique : un seul acteur, cinq casquettes, la série se tourne en un jour.
"""

EPISODES = [
 # --- Arc 1 · LA CARTE À L'ÉCRAN -----------------------------------------
 dict(n=151, arc="La carte à l'écran", role="Chef", format="Film de plat",
      agent="fraise",
      accroche="Regarde-le une seconde.", punchline="Voilà pourquoi on se lève à six heures.",
      titre="Le plat, filmé comme une pub",
      publie="Dix secondes sur le plat signature : la sauce qui nappe, la vapeur, "
             "la découpe. Aucun texte, aucune promo — juste l'objet du désir.",
      ressort="Un plat bien filmé est la seule publicité qu'un restaurant n'a pas "
              "besoin d'expliquer.",
      logiciel="La photo et le descriptif viennent de la fiche plat ; la vidéo part "
                "sur les cinq réseaux depuis RapidoCMS.",
      cta="Réserver une table"),
 dict(n=152, arc="La carte à l'écran", role="Chef", format="Recette",
      agent="tomate",
      accroche="On ne cache rien.", punchline="Refais-la chez toi. On t'attend quand même.",
      titre="La recette du plat signature",
      publie="Le chef fait le plat en trente secondes, gestes réels, quantités dites "
             "à voix haute. Il ne cache rien.",
      ressort="Donner sa recette ne fait pas perdre un client : ça prouve qu'on sait "
              "la faire mieux que celui qui la refera chez lui.",
      logiciel="La fiche recette donne les quantités exactes et le coût matière — le "
                "chef lit ce qu'il a déjà saisi.",
      cta="Voir la carte"),
 dict(n=153, arc="La carte à l'écran", role="Chef", format="Annonce",
      agent="ail",
      accroche="Cette semaine seulement.", punchline="Après, la saison change d'avis.",
      titre="Le plat de la semaine",
      publie="Le nouveau plat arrive, on dit pourquoi : le produit est là, la saison "
             "y est, il ne restera pas.",
      ressort="La rareté datée fait venir cette semaine, pas « un jour ».",
      logiciel="Le plat est ajouté à la carte, la publication est programmée le lundi "
                "matin par Iris.",
      cta="Commander en ligne"),
 dict(n=154, arc="La carte à l'écran", role="Serveur", format="Film de plat",
      agent="fraise",
      accroche="Midi. Quinze secondes.", punchline="Décide avant d'arriver.",
      titre="Le menu du midi en quinze secondes",
      publie="Entrée, plat, dessert du jour, filmés à la suite au pass, sans coupe. "
             "Le prix à la fin.",
      ressort="Le client de midi décide en marchant : il faut lui donner la carte "
              "avant qu'il ait passé la porte du voisin.",
      logiciel="Le menu du jour sort du logiciel, la publication part à 11 h.",
      cta="Voir le menu du jour"),
 dict(n=155, arc="La carte à l'écran", role="Chef", format="Annonce",
      agent="citron",
      accroche="Vous l'avez réclamé.", punchline="Il est revenu.",
      titre="Le plat qui revient",
      publie="Un ancien plat retiré de la carte revient parce que les clients l'ont "
             "réclamé. On le dit, on remercie.",
      ressort="Rien ne fidélise comme la preuve qu'on écoute.",
      logiciel="Les avis et les demandes remontent au même endroit ; on sait quel "
                "plat manque vraiment.",
      cta="Réserver une table"),
 dict(n=156, arc="La carte à l'écran", role="Chef", format="Coulisse",
      agent="tomate",
      accroche="Ce que tu ne vois jamais.", punchline="Trente secondes avant ton assiette.",
      titre="Le dessert qu'on ne montre jamais",
      publie="Le dessert monté en direct, à la seconde où il quitte le froid. Le "
             "moment que le client ne voit jamais.",
      ressort="Le dessert se vend au regard, pas à la description.",
      logiciel="Le coût matière du dessert est connu : on sait qu'on peut le pousser.",
      cta="Voir la carte"),

 # --- Arc 2 · LES ÉVÉNEMENTS ---------------------------------------------
 dict(n=157, arc="Les événements", role="Directeur", format="Annonce",
      agent="betterave",
      accroche="Vendredi 12, ici.", punchline="Il y a un nombre de places. Pas plus.",
      titre="Un événement au resto",
      publie="Date, heure, ce qu'on y fait, ce qu'on y mange. Filmé dans la salle "
             "préparée pour l'occasion.",
      ressort="Un événement donne une raison de venir un soir précis — le contraire "
              "d'une publicité qui espère.",
      logiciel="L'événement crée son créneau de réservation ; les places restantes "
                "s'affichent en direct.",
      cta="Réserver sa place"),
 dict(n=158, arc="Les événements", role="Serveur", format="Annonce",
      agent="brocoli",
      accroche="On diffuse le match.", punchline="L'écran est grand. La table se réserve.",
      titre="On diffuse le match",
      publie="L'écran, la salle qui se remplit, l'ardoise du menu match. On annonce "
             "l'heure du coup d'envoi et le plat qui va avec.",
      ressort="Le supporter cherche un endroit trois jours avant. Celui qui publie "
              "trois jours avant gagne la table.",
      logiciel="Le créneau du match est ouvert à la réservation, la campagne part "
                "automatiquement l'avant-veille.",
      cta="Réserver pour le match"),
 dict(n=159, arc="Les événements", role="Serveur", format="Offre",
      agent="citron",
      accroche="C'est ton anniversaire.", punchline="On s'occupe du reste.",
      titre="Fêtez votre anniversaire ici",
      publie="Le dessert avec la bougie, la table décorée, la petite mise en scène "
             "qu'on fait pour chaque anniversaire.",
      ressort="Un anniversaire, c'est huit couverts, pas un. C'est la table la plus "
              "rentable de la semaine.",
      logiciel="La date de naissance est dans la fiche client : la relance part "
                "quinze jours avant, toute seule.",
      cta="Réserver un anniversaire"),
 dict(n=160, arc="Les événements", role="Chef", format="Annonce",
      agent="betterave",
      accroche="Un soir, une cuisine.", punchline="Demain, ce plat n'existe plus.",
      titre="La soirée à thème",
      publie="Un soir, une cuisine, un décor. On montre le plat qui ne sera à la "
             "carte que ce soir-là.",
      ressort="Le thème crée l'envie de raconter — donc le partage.",
      logiciel="Le menu spécial est monté à part, sans toucher à la carte, et "
                "retiré tout seul le lendemain.",
      cta="Réserver sa place"),
 dict(n=161, arc="Les événements", role="Chef", format="Annonce",
      agent="pomme-de-terre",
      accroche="Dimanche, on ouvre à dix heures.", punchline="Prends ton temps.",
      titre="Le brunch du dimanche",
      publie="Le buffet dressé au petit matin, la lumière du dimanche, les gens qui "
             "arrivent en famille.",
      ressort="Le dimanche midi est le service le plus dur à remplir et le plus "
              "facile à vendre en image.",
      logiciel="Le brunch a son propre créneau et sa jauge : on ne survend pas.",
      cta="Réserver le brunch"),
 dict(n=162, arc="Les événements", role="Directeur", format="Offre",
      agent="brocoli",
      accroche="Toute la salle, rien que vous.", punchline="Ça se demande, et c'est possible.",
      titre="Privatiser la salle",
      publie="La salle vide, montée pour un groupe. Ce qu'on peut y faire, pour "
             "combien de personnes.",
      ressort="La privatisation se vend à des gens qui ne savent pas qu'elle existe.",
      logiciel="La demande de devis arrive dans le logiciel avec la date et le "
                "nombre de couverts.",
      cta="Demander un devis"),

 # --- Arc 3 · LES COULISSES ----------------------------------------------
 dict(n=163, arc="Les coulisses", role="Chef", format="Coulisse",
      agent="oignon",
      accroche="Six heures du matin.", punchline="Ton dîner a commencé il y a quatorze heures.",
      titre="Six heures du matin",
      publie="Le restaurant avant tout le monde : les chaises sur les tables, le "
             "premier café, la première livraison.",
      ressort="Le client ne voit jamais l'heure à laquelle commence son dîner.",
      logiciel="Le brief du jour est déjà affiché : couverts prévus, productions à "
                "lancer, alertes de stock.",
      cta="Découvrir la maison"),
 dict(n=164, arc="Les coulisses", role="Chef", format="Portrait",
      agent="oignon",
      accroche="À cinquante kilomètres d'ici.", punchline="C'est lui qui fait la moitié du travail.",
      titre="Le producteur",
      publie="Chez le maraîcher ou l'éleveur, à cinquante kilomètres. On montre la "
             "personne, pas le logo.",
      ressort="Le sourcing raconté par le producteur vaut dix mentions « produits "
              "frais » sur une ardoise.",
      logiciel="Le fournisseur est dans la base : les commandes et les prix passent "
                "par là toute l'année.",
      cta="Voir la carte"),
 dict(n=165, arc="Les coulisses", role="Serveur", format="Portrait",
      agent="navet",
      accroche="Elle t'accueille depuis quatre ans.", punchline="Tu reviens pour elle, pas pour la déco.",
      titre="Portrait d'un serveur",
      publie="Une minute avec la personne qui accueille : depuis quand, ce qu'elle "
             "préfère servir, sa table préférée.",
      ressort="Les clients reviennent pour des gens, pas pour un lieu.",
      logiciel="Son planning et ses heures sont posés ; elle sait sa semaine à "
                "l'avance, ça se voit à l'écran.",
      cta="Réserver une table"),
 dict(n=166, arc="Les coulisses", role="Chef", format="Coulisse",
      agent="tomate",
      accroche="Vingt heures quinze.", punchline="Aucune musique. C'est le vrai son.",
      titre="Le coup de feu, vu de la cuisine",
      publie="Vingt heures quinze. Les tickets, les voix, les assiettes qui partent. "
             "Aucune musique, le son réel.",
      ressort="L'intensité de la cuisine est un spectacle — à condition qu'elle soit "
              "maîtrisée, pas subie.",
      logiciel="Les commandes arrivent à l'écran de cuisine dans l'ordre, par poste. "
                "C'est ce qui rend la scène regardable.",
      cta="Réserver une table"),
 dict(n=167, arc="Les coulisses", role="Plongeur", format="Portrait",
      agent="navet",
      accroche="Le poste qu'on ne montre jamais.", punchline="Sans lui, rien ne sort.",
      titre="Le poste qu'on ne montre jamais",
      publie="La plonge, à fond, sans filtre. Puis la cuisine impeccable à minuit.",
      ressort="Montrer le poste le plus ingrat, c'est le respecter — et ça se "
              "remarque, y compris par ceux qui cherchent un travail.",
      logiciel="Le plan de nettoyage est coché poste par poste ; la conformité "
                "n'est pas une promesse.",
      cta="Rejoindre l'équipe"),
 dict(n=168, arc="Les coulisses", role="Chef", format="Coulisse",
      agent="oignon",
      accroche="Six heures, au marché.", punchline="Ce qu'on refuse compte autant.",
      titre="Les courses du chef",
      publie="Le marché à six heures, ce qu'on prend, ce qu'on refuse et pourquoi.",
      ressort="Le refus d'un produit dit plus sur une maison que dix plats réussis.",
      logiciel="La liste de courses vient de la production prévue — on n'achète pas "
                "au hasard.",
      cta="Voir la carte"),

 # --- Arc 4 · LE CLIENT ---------------------------------------------------
 dict(n=169, arc="Le client", role="Directeur", format="Avis",
      agent="fraise",
      accroche="On lit tout. Même celui-là.", punchline="Et voilà ce qu'on a changé.",
      titre="L'avis qu'on affiche",
      publie="Un vrai avis client lu à voix haute, y compris le reproche. Et ce "
             "qu'on a changé depuis.",
      ressort="Répondre publiquement à une critique convainc plus que cent cinq "
              "étoiles.",
      logiciel="Les avis remontent au même endroit ; la réponse part de là, dans "
                "le ton de la maison.",
      cta="Laisser un avis"),
 dict(n=170, arc="Le client", role="Serveur", format="Portrait",
      agent="citron",
      accroche="Même table depuis six ans.", punchline="On sait déjà ce qu'il va prendre.",
      titre="Le client du mardi",
      publie="Celui qui vient depuis six ans, toujours la même table. On lui donne "
             "la parole.",
      ressort="Un habitué qui parle vaut mieux qu'un influenceur qui passe.",
      logiciel="Sa fiche client garde ses habitudes : la table, le plat, l'allergie.",
      cta="Réserver une table"),
 dict(n=171, arc="Le client", role="Serveur", format="Coulisse",
      agent="pomme-de-terre",
      accroche="Douze personnes, une addition.", punchline="Ça peut très bien se passer.",
      titre="La table de douze",
      publie="Une grande tablée servie sans accroc : la mise en place, le service "
             "synchronisé, l'addition partagée en douze sans drame.",
      ressort="Le groupe est la peur de tout restaurateur — et la démonstration la "
              "plus impressionnante quand ça roule.",
      logiciel="Le plan de salle, les postes et le partage d'addition sont prévus "
                "avant que le groupe s'assoie.",
      cta="Réserver pour un groupe"),
 dict(n=172, arc="Le client", role="Client", format="Démonstration",
      agent="brocoli",
      accroche="Je commande depuis mon canapé.", punchline="Et je la regarde arriver en cuisine.",
      titre="Je commande depuis mon canapé",
      publie="Le chef passe client : il commande sur le site du restaurant, suit sa "
             "commande, et on la voit arriver en cuisine.",
      ressort="Montrer le parcours du client lève le doute de celui qui n'a jamais "
              "commandé chez vous.",
      logiciel="La commande du site tombe dans la même file que la salle. Zéro "
                "commission, zéro ressaisie.",
      cta="Commander en ligne"),
 dict(n=173, arc="Le client", role="Chef", format="Démonstration",
      agent="carotte",
      accroche="Sans gluten. Vraiment.", punchline="On vérifie, on ne suppose pas.",
      titre="Sans gluten, sans stress",
      publie="Une demande particulière prise au sérieux : ce qu'on change, ce qu'on "
             "vérifie, ce qu'on garantit.",
      ressort="La personne qui a une contrainte alimentaire choisit le restaurant "
              "pour toute sa table.",
      logiciel="Les allergènes sont sur la fiche plat, la contrainte est notée sur "
                "la réservation.",
      cta="Réserver une table"),
 dict(n=174, arc="Le client", role="Serveur", format="Coulisse",
      agent="pomme-de-terre",
      accroche="Premier rendez-vous.", punchline="On ne vous dérangera pas.",
      titre="Le premier rendez-vous",
      publie="La table près de la fenêtre, la lumière baissée, le service discret. "
             "Ce qu'on fait sans qu'on nous le demande.",
      ressort="Les gens ne réservent pas un repas, ils réservent une soirée qui doit "
              "bien se passer.",
      logiciel="La note « table calme » est sur la réservation ; le placement se "
                "fait avant l'arrivée.",
      cta="Réserver une table"),

 # --- Arc 5 · LA MAISON ---------------------------------------------------
 dict(n=175, arc="La maison", role="Serveur", format="Démonstration",
      agent="ail",
      accroche="Scanne, commande, c'est tout.", punchline="Trente secondes, filmé en vrai.",
      titre="Le QR code à table",
      publie="Le client scanne, lit la carte, commande. Trente secondes, filmé en "
             "vrai, sans montage.",
      ressort="Ce qui paraît gadget devient évident quand on le voit fonctionner "
              "une fois.",
      logiciel="La carte du QR code est celle du logiciel : un prix changé le matin "
                "est à jour à midi.",
      cta="Voir la carte"),
 dict(n=176, arc="La maison", role="Chef", format="Annonce",
      agent="ail",
      accroche="La carte change lundi.", punchline="Oui, on retire un plat que vous aimiez.",
      titre="La carte change de saison",
      publie="Les plats qui sortent, ceux qui entrent. On assume de retirer un plat "
             "que des gens aimaient.",
      ressort="Le changement de carte est un rendez-vous — à condition de l'annoncer "
              "au lieu de le subir.",
      logiciel="La nouvelle carte part d'un coup sur le site, le QR code et les "
                "réseaux.",
      cta="Découvrir la nouvelle carte"),
 dict(n=177, arc="La maison", role="Directeur", format="Annonce",
      agent="navet",
      accroche="On recrute. Voilà la vérité.", punchline="Les horaires, on les dit.",
      titre="On recrute",
      publie="Le poste, l'équipe, les horaires réels. On dit ce que c'est, pas ce "
             "qu'on voudrait que ce soit.",
      ressort="Une annonce honnête attire moins de candidats et beaucoup moins de "
              "démissions.",
      logiciel="Les candidatures arrivent au même endroit, avec leur statut ; on ne "
                "perd plus personne dans une boîte mail.",
      cta="Postuler"),
 dict(n=178, arc="La maison", role="Chef", format="Démonstration",
      agent="betterave",
      accroche="Chaud à l'arrivée.", punchline="Jamais préparé trop tôt.",
      titre="À emporter, sans que ça refroidisse",
      publie="La commande à emporter préparée au bon moment, pas trop tôt. Le client "
             "arrive, c'est prêt et c'est chaud.",
      ressort="La vente à emporter se gagne ou se perd sur les cinq dernières "
              "minutes.",
      logiciel="L'heure de retrait pilote le lancement en cuisine.",
      cta="Commander à emporter"),
 dict(n=179, arc="La maison", role="Directeur", format="Coulisse",
      agent="carotte",
      accroche="Fermé le lundi.", punchline="Ce n'est pas un jour de repos.",
      titre="Le jour de fermeture",
      publie="Ce qu'on fait le lundi : les commandes, les plannings, la compta, la "
             "carte de la semaine. Le travail invisible.",
      ressort="Le client croit qu'un restaurant ferme pour se reposer. Lui montrer "
              "l'inverse crée du respect.",
      logiciel="Une matinée suffit parce que tout est au même endroit — c'est le "
                "seul moment où le logiciel se voit vraiment.",
      cta="Découvrir la maison"),
 dict(n=180, arc="La maison", role="Directeur", format="Bilan",
      agent="carotte",
      accroche="Un an. Les vrais chiffres.", punchline="Merci.",
      titre="Un an de restaurant",
      publie="Les chiffres de l'année, dits sans fard : couverts, plat le plus "
             "vendu, avis reçus, gens embauchés. Et merci.",
      ressort="La transparence de fin d'année est le contenu le plus partagé d'un "
              "commerce de quartier.",
      logiciel="Tous ces chiffres sortent des rapports — aucun n'est estimé.",
      cta="Réserver une table"),
]
