# -*- coding: utf-8 -*-
"""« UpEatFood » — la série 4, écrite comme un film.

Trente-cinq plans de dix secondes qui, mis bout à bout, font une publicité de
trois cent cinquante secondes. La forme est empruntée à *Snatch* : quatre
histoires qu'on suit séparément, quatre personnages qui ne se connaissent pas,
et un dernier acte où ils se retrouvent tous au même endroit, le même soir.

Les quatre histoires sont les quatre côtés d'un restaurant :

    en cuisine     le chef            ce qu'il perd : le temps, la marge
    en salle       le serveur         ce qu'il perd : les noms, le calme
    au bureau      le patron          ce qu'il perd : ses nuits, la vue
    à la maison    le client          ce qu'il perd : sa soirée, son envie

Le même acteur les joue tous les quatre — Michael Kebail, le chef de la photo
de référence, en veste, en tablier long, en chemise, en manteau. Le film ne le dit
jamais : il se voit au cinquième épisode, et c'est ce qui donne envie de
revenir.

Chaque saison suit le même mouvement en six temps — trois avant FoodEatUp, la
bascule, deux après. La cinquième saison est le vendredi soir où les quatre
histoires se croisent, en onze plans.

    saison 1  En cuisine        6
    saison 2  En salle          6
    saison 3  Au bureau         6
    saison 4  À la maison       6
    saison 5  Vendredi, 20 h 15 11
                                --
                                35   ×  10 s  =  350 s

Le fil conducteur est une voix off unique, celle d'un conteur qui connaît déjà
la fin. Elle ouvre chaque plan et fait la couture d'un épisode à l'autre :
c'est elle qui autorise à publier les trente-cinq séparément sans que le film
se démonte.
"""

# ── Les quatre histoires ─────────────────────────────────────────────────────
# lieu, rôle joué par le chef, tenue, décor de base, ce que le personnage perd
HISTOIRES = [
    dict(
        slug="en-cuisine", saison=1, titre="En cuisine", numero_depart=501,
        role="Le chef", module="KDS",
        tenue="veste blanche de cuisine et tablier FoodEatUp, manches retroussées",
        decor="une cuisine professionnelle en inox, le pass au premier plan",
        perd="le temps, et la marge avec",
        pitch="Il ouvre à sept heures et ferme à minuit. Entre les deux, il ne "
              "sait pas ce que son plat lui coûte.",
    ),
    dict(
        slug="en-salle", saison=2, titre="En salle", numero_depart=507,
        role="Le serveur", module="Réservation",
        tenue="chemise blanche, tablier long noir, stylo à l'oreille",
        decor="une salle de restaurant dressée, le comptoir d'accueil au premier plan",
        perd="les noms, les notes, et le calme",
        pitch="Six tables, quatre canaux, une seule mémoire : la sienne. Et elle "
              "rentre chez elle à minuit.",
    ),
    dict(
        slug="au-bureau", saison=3, titre="Au bureau", numero_depart=513,
        role="Le patron", module="Comptabilité",
        tenue="chemise ouverte, manches remontées, lunettes remontées sur le front",
        decor="un petit bureau à l'étage du restaurant, classeurs et tickets de caisse",
        perd="ses nuits, et la vue d'ensemble",
        pitch="Il découvre le 15 du mois suivant si le mois d'avant était bon. "
              "C'est un peu tard pour changer quoi que ce soit.",
    ),
    dict(
        slug="a-la-maison", saison=4, titre="À la maison", numero_depart=519,
        role="Le client", module="Le client",
        tenue="manteau et écharpe, téléphone à la main",
        decor="un appartement le soir, puis le trottoir devant le restaurant",
        perd="sa soirée, et l'envie de revenir",
        pitch="Il ne verra jamais le logiciel. Il verra très bien ce que le "
              "logiciel a oublié de faire.",
    ),
]

# ── Le mouvement en six temps, identique pour les quatre histoires ───────────
TEMPS = [
    ("Il était une fois", "Avant FoodEatUp"),
    ("Ce qui coince", "Avant FoodEatUp"),
    ("Le soir où ça casse", "Avant FoodEatUp"),
    ("La bascule", "La bascule"),
    ("Le même geste, autrement", "Avec FoodEatUp"),
    ("Ce qui a changé", "Avec FoodEatUp"),
]

# ── Les vingt-quatre plans des quatre histoires ──────────────────────────────
# titre, accroche (voix off du conteur), punchline (la chute), résumé,
# scene (ce qu'on filme), bascule (à 5 s), fin (les deux dernières secondes),
# dit (la réplique du personnage), story (la punchline FoodEatUp du générique)
PLANS = {
    # ── 1. En cuisine ────────────────────────────────────────────────────────
    "EP501": dict(
        titre="Sept heures, et personne",
        accroche="Il était une fois un restaurant, et un homme qui ouvrait seul.",
        punchline="Personne ne verra jamais ces quatre heures-là.",
        resume="Sept heures du matin. Le chef ouvre, allume, relève les températures, "
               "reçoit la livraison et décide la carte du jour sur ce qui est arrivé. "
               "Quatre heures avant que quiconque pousse la porte.",
        scene="Une cuisine professionnelle éteinte, à l'aube. Une seule veilleuse au-dessus du pass.",
        bascule="la lumière des néons s'allume d'un coup, rangée par rangée, et la cuisine sort du noir",
        fin="Il pose les mains à plat sur le pass, immobile, et regarde la salle vide devant lui.",
        dit="Bon. On y va.",
        story="Sa journée commence quatre heures avant la vôtre.",
    ),
    "EP502": dict(
        titre="Le carnet, le tableau, la tête",
        accroche="Il tenait ses comptes à trois endroits. Aucun ne parlait aux autres.",
        punchline="Trois vérités, et pas une seule bonne.",
        resume="Un carnet pour les livraisons, un tableau blanc pour la production, "
               "et le reste dans la tête. Trois systèmes qui ne se parlent pas : la marge "
               "du plat, personne ne la connaît vraiment.",
        scene="Le chef écrit sur un carnet gras, lève les yeux vers un tableau blanc couvert de chiffres effacés.",
        bascule="il s'arrête au milieu d'un chiffre, revient au carnet, ne retrouve pas la ligne",
        fin="Il pose le crayon et regarde le tableau comme on regarde une langue étrangère.",
        dit="Ça, c'était mardi. Ou jeudi.",
        story="Trois carnets ne font pas une comptabilité.",
    ),
    "EP503": dict(
        titre="Vendredi, le bac vide",
        accroche="Puis vint le vendredi où le bac était vide.",
        punchline="Il l'avait dit le matin. On l'a écouté à vingt heures.",
        resume="Dix-neuf heures quarante, plein service : le bac du plat signature est vide. "
               "Il l'avait annoncé le matin. Personne n'avait de quoi le vérifier.",
        scene="Plein service, vapeur, tickets qui s'accumulent sur la barre du pass.",
        bascule="il soulève le couvercle d'un bac, et le bac est vide jusqu'au fond",
        fin="Il repose le couvercle sans un mot, et regarde les tickets qui continuent de tomber.",
        dit="Va dire à la douze qu'il n'y en a plus.",
        story="Une rupture un vendredi soir coûte plus qu'un mois de logiciel.",
    ),
    "EP504": dict(
        titre="Une phrase, un matin",
        accroche="Un matin, il n'a pas ouvert le carnet.",
        punchline="Il a simplement demandé.",
        resume="Même cuisine, même heure. Il ne cherche plus dans le carnet : il demande "
               "ce qui manque, et la réponse arrive avant qu'il ait fini son café.",
        scene="La même cuisine à l'aube, la même veilleuse, le carnet gras fermé sur le pass.",
        bascule="il pose la main sur le carnet fermé et ne l'ouvre pas",
        fin="Il regarde droit devant lui, et pour la première fois il n'a pas l'air pressé.",
        dit="Qu'est-ce qu'il me manque, aujourd'hui ?",
        story="Demandez le matin. Vous commanderez au lieu de vous excuser.",
    ),
    "EP505": dict(
        titre="Le plat, et ce qu'il coûte",
        accroche="Le même geste, la même sauce. Mais il sait, maintenant.",
        punchline="Le goût n'a pas changé. Le reste, si.",
        resume="La fiche technique dit ce qu'il y a dans le plat, ce qu'il coûte et ce qu'il "
               "rapporte. Le geste est le même qu'avant ; ce qui change, c'est qu'il ne se "
               "demande plus s'il gagne de l'argent dessus.",
        scene="Gros plan sur le dressage du plat signature, lumière rasante, vapeur.",
        bascule="la sauce nappe l'assiette en un seul geste, net, sans reprise",
        fin="Il essuie le bord de l'assiette avec le pouce et la pousse sur le pass.",
        dit="Celui-là, je sais ce qu'il me rapporte.",
        story="Le coût matière à jour, à chaque service.",
    ),
    "EP506": dict(
        titre="Il ferme, et il sait",
        accroche="Il ferme toujours à minuit. Mais il ne se demande plus rien.",
        punchline="La marge du jour l'attendait avant qu'il éteigne.",
        resume="La cuisine est rangée, les pertes saisies, le nettoyage photographié. "
               "La marge du service s'affiche seule. Il ferme en sachant, au lieu de fermer "
               "en espérant.",
        scene="La cuisine nettoyée, inox essuyé, une seule lumière encore allumée au-dessus du pass.",
        bascule="il éteint la dernière rampe de néons et la pièce passe au bleu de la veilleuse",
        fin="Il reste une seconde dans l'embrasure, la main sur l'interrupteur, et sourit à peine.",
        dit="Bonne soirée à tous.",
        story="Fermer en sachant, pas en espérant.",
    ),

    # ── 2. En salle ──────────────────────────────────────────────────────────
    "EP507": dict(
        titre="Six tables, une mémoire",
        accroche="Il était une fois un homme qui tenait une salle entière dans sa tête.",
        punchline="Et sa tête rentrait chez elle à minuit.",
        resume="Le serveur connaît les allergies, les habitudes, le prénom du fils. "
               "Tout est dans sa tête, et rien n'est écrit nulle part.",
        scene="Une salle dressée avant le service, nappes blanches, lumière basse.",
        bascule="il touche successivement quatre tables du bout des doigts, comme on récite",
        fin="Il s'arrête au milieu de la salle et regarde les tables vides, une par une.",
        dit="La six ne mange pas de crustacés.",
        story="Ce qu'il sait ne devrait pas rentrer chez lui le soir.",
    ),
    "EP508": dict(
        titre="Le téléphone qui sonne dans le vide",
        accroche="Quatre canaux, et une seule paire de mains.",
        punchline="Le téléphone, lui, ne prend jamais sa pause.",
        resume="Le téléphone, le site, la plateforme, la porte. Quatre canaux de réservation "
               "qui n'ont aucun moyen de savoir ce que les trois autres ont accepté.",
        scene="Le comptoir d'accueil, un carnet de réservations ouvert, un téléphone qui sonne.",
        bascule="le téléphone sonne pendant qu'il écrit, il suspend le stylo à mi-mot",
        fin="Il repose le combiné, regarde la ligne inachevée sur le carnet et hésite.",
        dit="Attendez… c'était pour quelle heure ?",
        story="Quatre canaux, un seul plan de salle.",
    ),
    "EP509": dict(
        titre="La table de douze qui n'existait pas",
        accroche="Puis vint le soir où deux tables portaient le même numéro.",
        punchline="Douze personnes debout, et une salle complète.",
        resume="Une table de douze acceptée au téléphone trois jours plus tôt, jamais reportée "
               "dans le plan de salle. Elle arrive à vingt heures. La salle est pleine.",
        scene="La salle en plein service, bruyante. Un groupe attend debout près de la porte.",
        bascule="il fait pivoter le carnet vers lui, et la ligne n'y est pas",
        fin="Il lève les yeux vers le groupe qui attend, et ne trouve rien à dire.",
        dit="Je suis vraiment désolé.",
        story="Une réservation qu'on ne voit pas est une réservation qu'on perd.",
    ),
    "EP510": dict(
        titre="Le plan de salle qui se remplit tout seul",
        accroche="Un soir, le carnet est resté fermé.",
        punchline="Les quatre canaux arrivaient au même endroit.",
        resume="Le téléphone, le site, la plateforme et la porte tombent dans le même plan "
               "de salle. La contrainte alimentaire arrive écrite sur la réservation.",
        scene="Le comptoir d'accueil, le carnet de réservations fermé, posé de côté.",
        bascule="il tourne le carnet face contre bois et le pousse au bout du comptoir",
        fin="Il se redresse, regarde la salle, et croise les mains derrière le dos.",
        dit="On est complets. Et je le sais depuis mardi.",
        story="Quatre canaux, une seule file, dans l'ordre d'arrivée.",
    ),
    "EP511": dict(
        titre="Le prénom du fils",
        accroche="Ce qu'il savait par cœur, quelqu'un d'autre le sait aussi maintenant.",
        punchline="Ce n'est plus sa mémoire. C'est celle de la maison.",
        resume="Les allergies, les habitudes, la dernière visite : la fiche client les porte. "
               "Le service ne dépend plus de qui travaille ce soir-là.",
        scene="Une table de deux, à hauteur d'assiette. Le serveur s'approche.",
        bascule="il pose l'assiette et dit un prénom qu'il n'a pas eu à demander",
        fin="Les clients se regardent, surpris ; lui repart déjà vers la table suivante.",
        dit="Sans crustacés, comme la dernière fois.",
        story="La mémoire de la maison, pas celle du serveur.",
    ),
    "EP512": dict(
        titre="Minuit, et rien à retenir",
        accroche="Il rentre chez lui les mains vides. C'est nouveau.",
        punchline="Ce qu'il sait est resté au restaurant.",
        resume="Fin de service. Ce qui s'est passé ce soir est écrit là où le prochain "
               "service le lira. Il n'emporte plus rien.",
        scene="La salle vide après le service, chaises retournées sur les tables.",
        bascule="il éteint la rangée de lumières du fond et la salle se réduit à un couloir",
        fin="Il enfile sa veste sans se retourner et pousse la porte.",
        dit="À demain.",
        story="Rentrez chez vous sans le restaurant dans la tête.",
    ),

    # ── 3. Au bureau ─────────────────────────────────────────────────────────
    "EP513": dict(
        titre="Le bureau au-dessus de la salle",
        accroche="Il était une fois un homme qui comptait au-dessus du bruit.",
        punchline="Sous le plancher, le service. Au-dessus, les chiffres.",
        resume="Un bureau minuscule au premier étage. Sous le plancher, cent couverts. "
               "Au-dessus, un homme qui essaie de savoir si la soirée est rentable.",
        scene="Un bureau étroit à l'étage, une lampe, des classeurs, le bruit du service en dessous.",
        bascule="le bruit d'un plateau qui tombe monte du plancher, il lève les yeux au plafond",
        fin="Il baisse les yeux vers la pile de tickets et n'en prend aucun.",
        dit="Cent quatre couverts. Et alors ?",
        story="Compter après coup, c'est constater.",
    ),
    "EP514": dict(
        titre="La pile qui grandit toute seule",
        accroche="Les factures arrivaient plus vite qu'il ne les ouvrait.",
        punchline="C'est bien la seule chose ici qui pousse sans qu'on l'arrose.",
        resume="Bons de livraison, factures fournisseurs, tickets de caisse. Tout arrive en "
               "papier, tout se ressaisit à la main, et rien ne se recoupe.",
        scene="Le bureau de nuit, une pile de papiers plus haute que la lampe.",
        bascule="il pose une facture de plus au sommet et la pile penche sans tomber",
        fin="Il retire ses lunettes et se frotte les yeux, la pile toujours là.",
        dit="Je fais ça dimanche.",
        story="Ce qui se ressaisit à la main se paie deux fois.",
    ),
    "EP515": dict(
        titre="Le quinze du mois suivant",
        accroche="Puis vint le jour où il apprit que le mois d'avant avait été mauvais.",
        punchline="Un mois trop tard pour y changer quoi que ce soit.",
        resume="Le bilan du mois arrive le 15 du mois suivant. Quand il découvre le problème, "
               "il a déjà quinze jours du mois d'après derrière lui.",
        scene="Le bureau en plein jour, un tableau imprimé posé au milieu, seul.",
        bascule="il fait glisser le tableau vers lui et s'arrête sur une ligne",
        fin="Il repousse la feuille de deux centimètres et regarde par la fenêtre.",
        dit="Février. On est le quinze mars.",
        story="Savoir en mars ce qui s'est joué en février, c'est ne pas savoir.",
    ),
    "EP516": dict(
        titre="La question posée à voix haute",
        accroche="Un soir, il n'a pas ouvert le classeur.",
        punchline="Il a posé la question, et la réponse était déjà là.",
        resume="Le coût matière à jour, la marge en euros, la comparaison avec le mois dernier. "
               "Il ne cherche plus l'information : il la demande.",
        scene="Le bureau le soir, le classeur fermé, la lampe allumée, la pile absente.",
        bascule="il pousse le classeur fermé hors du cercle de lumière de la lampe",
        fin="Il s'adosse à son fauteuil, les mains derrière la tête, et écoute le service.",
        dit="Combien me coûte le plat du jour, là, maintenant ?",
        story="La marge en euros, pas dans trois semaines.",
    ),
    "EP517": dict(
        titre="Le planning avant le samedi",
        accroche="Il a arrêté d'être trop nombreux le mardi.",
        punchline="Et de manquer de bras le samedi.",
        resume="La prévision de couverts croise le planning : on n'est plus sur-effectif le "
               "mardi ni sous-effectif le samedi. Le premier poste maîtrisable d'un restaurant "
               "cesse de se décider au feeling.",
        scene="Le bureau en fin de matinée, lumière de fenêtre, un planning affiché au mur.",
        bascule="il décroche une étiquette du planning et la repose deux cases plus loin",
        fin="Il recule d'un pas, regarde le mur entier, et hoche la tête une fois.",
        dit="Samedi, on sera quatre. Pas trois.",
        story="Le coût salarial se décide avant le service, pas après.",
    ),
    "EP518": dict(
        titre="Il éteint la lampe à vingt-trois heures",
        accroche="Le bureau ferme maintenant en même temps que la salle.",
        punchline="Les dimanches lui ont été rendus.",
        resume="Le Z, les pertes, le coût du travail du service : trois chiffres disponibles "
               "avant d'éteindre. Il n'y a plus de comptabilité à rattraper le dimanche.",
        scene="Le bureau à vingt-trois heures, rangé, la pile de papiers absente du cadre.",
        bascule="il éteint la lampe de bureau et la pièce ne garde que la lueur de l'escalier",
        fin="Il descend la première marche et laisse la porte ouverte derrière lui.",
        dit="Dimanche, je ne viens pas.",
        story="Rendez-vous vos dimanches.",
    ),

    # ── 4. À la maison ───────────────────────────────────────────────────────
    "EP519": dict(
        titre="Il cherche où aller",
        accroche="Il était une fois quelqu'un qui cherchait simplement où dîner.",
        punchline="Il ne verra jamais votre logiciel. Il verra tout le reste.",
        resume="Vingt heures, chez lui. Il cherche, il compare, il hésite entre trois "
               "adresses. Ce qu'il trouve du restaurant décide de sa soirée.",
        scene="Un salon le soir, une seule lampe, un téléphone éclairant un visage.",
        bascule="il fait défiler l'écran d'un pouce et le reflet de l'écran change sur son visage",
        fin="Il repose le téléphone sur ses genoux et regarde dans le vide.",
        dit="Bon. On tente celui-là.",
        story="Il décide chez lui, trois jours avant d'entrer.",
    ),
    "EP520": dict(
        titre="La carte date de mardi",
        accroche="La carte qu'il a lue n'était plus la bonne.",
        punchline="On est vendredi.",
        resume="La carte en ligne n'a pas bougé depuis mardi. Le plat qui l'a décidé n'existe "
               "plus. Il l'apprendra à table, devant quelqu'un qui s'excuse.",
        scene="Le trottoir devant un restaurant, la nuit, une ardoise sous la pluie fine.",
        bascule="il approche le visage de l'ardoise et l'écriture est délavée jusqu'à l'illisible",
        fin="Il recule d'un pas, regarde la vitrine, et son enthousiasme retombe d'un cran.",
        dit="C'était pas ça, sur le site.",
        story="Une carte qui date de mardi vous coûte le vendredi.",
    ),
    "EP521": dict(
        titre="Personne ne décroche",
        accroche="Puis vint le soir où il a appelé, et où personne n'a répondu.",
        punchline="Il a rappelé le restaurant d'à côté.",
        resume="Vingt heures dix : il appelle pour réserver à six, dont deux personnes qui ne "
               "mangent pas de fruits à coque. Tout le monde est en salle. Le téléphone sonne "
               "dans le vide.",
        scene="Le salon, le téléphone à l'oreille, la sonnerie qu'on entend dans le combiné.",
        bascule="la sonnerie s'arrête net et bascule sur une voix enregistrée",
        fin="Il éloigne le téléphone de son oreille, regarde l'écran, et raccroche.",
        dit="Tant pis.",
        story="Le client qui n'a pas eu de réponse ne rappelle pas.",
    ),
    "EP522": dict(
        titre="Quelqu'un décroche à la première sonnerie",
        accroche="Un soir, quelqu'un a décroché. Au premier coup.",
        punchline="Et on lui a demandé s'il y avait une allergie.",
        resume="L'agent au téléphone prend l'appel en plein service, demande le nombre de "
               "couverts, l'heure et la contrainte alimentaire. La réservation arrive dans le "
               "plan de salle avec la note écrite dessus.",
        scene="Le salon, la même lampe, le téléphone à l'oreille — mais il sourit.",
        bascule="il attrape un stylo par réflexe, puis le repose : il n'a rien à noter",
        fin="Il raccroche et reste une seconde le téléphone à la main, un peu étonné.",
        dit="Six. Et deux sans fruits à coque, oui.",
        story="Décrocher à la première sonnerie, même en plein coup de feu.",
    ),
    "EP523": dict(
        titre="La table était prête à son nom",
        accroche="Il n'a rien eu à expliquer en arrivant.",
        punchline="C'était déjà écrit.",
        resume="La table est prête, l'allergie est notée, personne ne lui redemande rien. "
               "Tout ce que le logiciel a fait, il ne le verra pas — il verra qu'on ne lui a "
               "rien redemandé.",
        scene="L'entrée du restaurant, la nuit, le manteau encore sur les épaules.",
        bascule="on lui prend son manteau et on lui montre une table déjà dressée pour six",
        fin="Il s'assied, regarde la table autour de lui, et desserre son écharpe.",
        dit="Vous aviez noté ?",
        story="Ce qu'il ne remarque pas, c'est exactement ce qui le fait revenir.",
    ),
    "EP524": dict(
        titre="Vingt-trois heures, dans le métro",
        accroche="Ce qu'il écrit le soir vaut le service entier.",
        punchline="Cinq étoiles, et il ne saura jamais pourquoi.",
        resume="Vingt-trois heures, dans le métro, il note le restaurant. Personne en salle ne "
               "saura jamais que ça s'est joué sur une allergie notée trois jours plus tôt.",
        scene="Une rame de métro la nuit, néons, un visage éclairé par un téléphone.",
        bascule="son pouce s'arrête sur la cinquième étoile et appuie",
        fin="Il range le téléphone dans sa poche et regarde la nuit défiler par la vitre.",
        dit="Franchement, c'était très bien.",
        story="Un avis, c'est un service entier qui remonte.",
    ),

    # ── 5. Vendredi, 20 h 15 — les quatre histoires se croisent ──────────────
    "EP525": dict(
        titre="Le même soir, quatre fois",
        accroche="Ce que vous venez de voir se passait le même soir. Vendredi.",
        punchline="Aucun des quatre ne sait que les trois autres existent.",
        resume="Quatre histoires, quatre lieux, un seul vendredi. Le film reprend à dix-huit "
               "heures, et cette fois on les voit tous les quatre en même temps.",
        scene="Écran partagé en quatre : la cuisine, la salle, le bureau, un salon.",
        bascule="les quatre cadrans d'horloge des quatre images marquent la même heure",
        fin="Les quatre images se resserrent d'un cran vers le centre, sans se toucher.",
        dit="Vendredi. Dix-huit heures.",
        story="Quatre métiers, un seul service.",
    ),
    "EP526": dict(
        titre="18 h 40 — il réserve",
        accroche="Tout commence par quelqu'un qui n'est pas encore là.",
        punchline="Six couverts, deux allergies, et le service ne le sait pas encore.",
        resume="Le client réserve depuis son salon. Six couverts, deux personnes qui ne mangent "
               "pas de fruits à coque. C'est le premier domino.",
        scene="Le salon du client, le téléphone à l'oreille, l'horloge du mur à 18 h 40.",
        bascule="il dit une phrase et, hors champ, un écran s'allume brièvement",
        fin="Il raccroche et pose le téléphone à côté de lui, l'air satisfait.",
        dit="Six, à vingt heures et quart.",
        story="Une phrase dite chez soi arrive en cuisine.",
    ),
    "EP527": dict(
        titre="18 h 41 — la salle le voit",
        accroche="Une minute plus tard, à trois kilomètres de là.",
        punchline="La table de six existait avant que personne ne la demande.",
        resume="La réservation arrive dans le plan de salle avec la contrainte écrite dessus. "
               "Le serveur n'a rien noté : il a lu.",
        scene="Le comptoir d'accueil de la salle, avant l'ouverture, tables dressées.",
        bascule="il lève les yeux du comptoir vers une table du fond et la désigne du menton",
        fin="Il déplace une chaise, compte du regard, et hoche la tête.",
        dit="La quatorze. Six. Deux sans fruits à coque.",
        story="La contrainte arrive écrite sur la réservation.",
    ),
    "EP528": dict(
        titre="18 h 42 — la cuisine l'apprend",
        accroche="Une minute encore, et l'information passe la porte battante.",
        punchline="Personne n'a crié le nom d'une allergie à travers la cuisine.",
        resume="La contrainte alimentaire arrive au pass sans que quiconque ait traversé la "
               "cuisine en criant. Le chef adapte deux assiettes sur les six.",
        scene="Le pass de la cuisine avant le service, les bacs pleins, la vapeur qui monte.",
        bascule="il pose deux assiettes à part, à gauche de la rangée, et les marque du doigt",
        fin="Il regarde les six assiettes alignées et recule d'un demi-pas.",
        dit="Deux à part. Compris.",
        story="Une allergie notée vaut mieux qu'une allergie criée.",
    ),
    "EP529": dict(
        titre="18 h 43 — le bureau voit le couvert",
        accroche="Et à l'étage, quelqu'un a vu passer six couverts de plus.",
        punchline="Il connaît la marge de la soirée avant qu'elle ait commencé.",
        resume="Le bureau voit la réservation entrer dans la prévision : les achats du "
               "lendemain, le nombre de bras, la marge attendue. Tout bouge d'un cran.",
        scene="Le bureau à l'étage, la lampe allumée, le bruit de la salle qui monte du plancher.",
        bascule="il lève la tête vers le plancher, comme s'il entendait la table s'ajouter",
        fin="Il repose son stylo à côté du carnet fermé et sourit sans lever les yeux.",
        dit="Cent dix, ce soir.",
        story="Le couvert compte avant d'entrer, pas après.",
    ),
    "EP530": dict(
        titre="20 h 15 — les quatre au même endroit",
        accroche="À vingt heures quinze, les quatre histoires n'en font plus qu'une.",
        punchline="Et c'est le même homme, dans quatre vies.",
        resume="Le client pousse la porte. Le serveur l'accueille. Le chef envoie. "
               "Le patron regarde depuis l'escalier. C'est le point de croisement du film.",
        scene="Le hall du restaurant en plein service, vu depuis la porte d'entrée.",
        bascule="la caméra pivote lentement et cadre les quatre personnages dans le même plan",
        fin="Les quatre sont immobiles, chacun à sa place, et personne ne se regarde.",
        dit="Bonsoir. Vous avez réservé ?",
        story="Quatre postes, une seule saisie.",
    ),
    "EP531": dict(
        titre="20 h 31 — le plat part",
        accroche="Seize minutes plus tard, l'assiette quitte le pass.",
        punchline="Six assiettes, dont deux qui ne ressemblent pas aux autres.",
        resume="Le plat part du pass, traverse la salle, arrive à la table. Deux assiettes sur "
               "six sont différentes, et personne n'a eu à le rappeler.",
        scene="Un plan-séquence qui suit une assiette du pass jusqu'à la table.",
        bascule="l'assiette passe la porte battante et le bruit change d'un coup",
        fin="L'assiette se pose sur la nappe, et la main se retire du cadre.",
        dit="Voilà. Sans fruits à coque.",
        story="Du pass à la table, sans un mot de plus.",
    ),
    "EP532": dict(
        titre="20 h 32 — il ne remarque rien",
        accroche="Il n'a rien remarqué. C'est exactement le but.",
        punchline="Ce qu'on ne remarque pas, c'est ce qui marche.",
        resume="Le client mange. Il ne saura jamais qu'une contrainte est passée par trois "
               "postes en quatre-vingt-dix minutes. Il saura seulement que c'était bien.",
        scene="La table de six vue à hauteur d'assiette, rires, mains, verres.",
        bascule="il lève son verre vers quelqu'un hors champ et le repose sans regarder l'assiette",
        fin="Il reprend une bouchée et continue sa conversation, sans un regard pour la salle.",
        dit="C'est très bon.",
        story="La meilleure technologie est celle qu'on ne voit pas.",
    ),
    "EP533": dict(
        titre="23 h 50 — le Z avant d'éteindre",
        accroche="À minuit moins dix, il n'y avait plus rien à rattraper.",
        punchline="Le dimanche est resté un dimanche.",
        resume="Le Z, les pertes, le coût du travail du service. Trois chiffres avant "
               "d'éteindre. Personne ne reviendra dimanche pour les chercher.",
        scene="Le bureau à l'étage, la salle éteinte en contrebas par la fenêtre intérieure.",
        bascule="il éteint la lampe et la fenêtre intérieure devient la seule source de lumière",
        fin="Il descend l'escalier et la lumière de la cage s'éteint derrière lui.",
        dit="C'était une bonne soirée.",
        story="Trois chiffres avant d'éteindre, pas le 15 du mois suivant.",
    ),
    "EP534": dict(
        titre="7 h 00 — le lendemain",
        accroche="Le lendemain, il a ouvert. Comme tous les jours.",
        punchline="Mais il n'a plus jamais ouvert le carnet.",
        resume="Sept heures du matin, la même cuisine, la même veilleuse. Rien n'a changé du "
               "métier. Tout a changé de ce qu'il faut porter dans sa tête pour l'exercer.",
        scene="La cuisine à l'aube, exactement le cadre du tout premier plan du film.",
        bascule="les néons s'allument rangée par rangée, comme au premier épisode",
        fin="Il pose les mains à plat sur le pass, immobile, et regarde la salle vide.",
        dit="Bon. On y va.",
        story="Le même métier. Sans la charge.",
    ),
    "EP535": dict(
        titre="Il était une fois un restaurant",
        accroche="Il était une fois un restaurant. Il y est toujours.",
        punchline="Quatre métiers, un seul logiciel, et personne n'a rien vu passer.",
        resume="Le dernier plan referme le film : les quatre personnages, le même homme, "
               "réunis une seconde à l'image. C'est le seul moment où le film le dit.",
        scene="La façade du restaurant, la nuit, l'enseigne allumée, la rue déserte.",
        bascule="les quatre silhouettes apparaissent en surimpression dans la vitrine, une par une",
        fin="Les quatre reflets se superposent en un seul, et l'enseigne reste seule allumée.",
        dit="Il était une fois un restaurant.",
        story="FoodEatUp. Le restaurant qui se gère tout seul.",
    ),
}
