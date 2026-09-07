# Bibliothèque Higgsfield — 150 plans analysés (relevé du 2026-09-07)

Source : historique de générations Higgsfield du compte (Seedance 2.5, 10 s chacun, 720×1280). Aucun plan n'a été régénéré : tout est réutilisé tel quel (règle du dépôt). Fichiers locaux : `assets/higgsfield/vNNN.mp4` (téléchargés depuis les `rawUrl`, non versionnés) ; catalogue complet avec prompts : `assets/higgsfield-catalogue.json`.

## Répartition par série

- **70** · Michael fait son cinéma — saison restaurant (comédie, veste FoodEatUp)
- **51** · Plan'It corporate (bureau, documentaire) — hors sujet FoodEatUp
- **19** · Michael remonte le temps (RapidoCMS, époques) — hors sujet FoodEatUp
- **10** · Cuisine Seedance sans texte (objet net / chef flou, lèvres mimées)

## Ce que disent les prompts

- Structure récurrente de la saison restaurant : `REF: Michael = image_1 + tenue de saison, Location = @Image 3/4, FORMAT: 9:16, 10 s, 4 shots, realistic comedy` puis un gag en quatre plans de 2-3 s ; les répliques sont écrites (lip-sync), les shots 2 et 3 (2-8 s) portent le gag visuel.
- 39 générations sont des `video_extension` (prolongement d'un plan précédent), les autres des générations image→vidéo avec référence personnage.
- Les 10 plans « cuisine sans texte » (25, 141-149) sont pensés pour recevoir une voix off : objet net qui change d'état à 5 s, chef flou derrière. Ne pas poser un autre texte sur les lèvres qui bougent.
- Les séries Plan'It (51 plans) et « remonte le temps » (19) ne concernent pas FoodEatUp et ne sont pas utilisées ici.

## Index par problème de restaurant (saison restaurant)

- HACCP températures : 84, 85, 143
- allergènes : 74, 75, 76
- avis client : 86, 87
- avis client / influenceur : 72, 73
- caisse/compta : 27, 30, 46, 47, 58, 59, 78, 80
- campagne marketing : 62, 63
- commande fournisseur : 77, 79
- commandes en cuisine (KDS) : 23, 70, 71
- devis groupe : 148
- dépendance plateformes : 141
- facture : 56, 57
- fichier client : 41, 42, 43
- file d'attente : 81, 82, 83
- food cost / fiche technique : 44, 45, 145
- happy hour / marketing : 48, 49
- inventaire stock : 68, 69
- livraison : 50, 51
- nettoyage : 35, 36
- pilotage global (agents IA) : 25
- planning production : 54, 55
- planning équipe : 33, 34, 66, 67, 144
- prise de commande : 39, 40, 146, 147
- prise de commande papier : 24
- recrutement : 26, 64, 65
- rupture de stock : 31, 32, 142
- réservations : 37, 38, 52, 53, 88, 89
- terrasse météo / placement : 60, 61

## Plans utilisés dans les 4 films

| Film | Plans Higgsfield |
|---|---|
| Clip | 149, 23, 24, 71, 38, 37, 69, 79, 84, 85, 33, 34, 47, 78, 86, 77, 143, 144, 145, 22, 20, 28, 66, 19, 21 |
| Présentation | 23, 69, 84, 38, 141, 142, 25, 53, 63, 85, 143, 29, 28, 19 (+ hero-video, screencasts) |
| Commercial | 85, 84, 143, 142, 144, 25, 28, 19 (+ screencast export HACCP) |
| Démo | aucun (screencasts réels + avatar HeyGen existant) |

## Catalogue

| # | date | série | lieu | problème | gag | note montage |
|---|---|---|---|---|---|---|
| 0 | 2026-09-06 | michael-remonte-le-temps | entrée de grotte, aube d'hiver |  | conteur solennel, « il était une fois » | Garder le début (0-5 s) : flamme dans le vent et regard sur la vallée, beau plan d'ambiance sans parole ; version 9:16. |
| 1 | 2026-09-06 | michael-remonte-le-temps | entrée de grotte, aube d'hiver |  | conteur solennel, « il était une fois » | Doublon 16:9 de l'index 0 ; garder la descente de perche jusqu'au visage (3-6 s) si besoin d'un plan horizontal. |
| 2 | 2026-09-06 | michael-remonte-le-temps | palissade d'oppidum gaulois, nuit |  | chute historique, gravité puis demi-sourire | Fin (4-10 s) : plan poitrine avec le jambon net au premier plan et la lueur orange, le plus fort visuellement. |
| 3 | 2026-09-06 | michael-remonte-le-temps | halle gauloise, foyer central, soir |  | partage du même feu, même table | Milieu (5-9 s) : les trois coups de couteau et les mains qui prennent les tranches, très rythmique et sans dialogue. |
| 4 | 2026-09-06 | michael-remonte-le-temps | promontoire boisé, vallée de feux, aube |  | tribus ennemies, conteur grave | Début (0-6 s) : regard sur la vallée brumeuse et la buée, plan d'ambiance utilisable sans son. |
| 5 | 2026-09-05 | michael-remonte-le-temps | entrée de grotte, aube d'hiver |  | conteur solennel préhistorique | Comparer avec l'index 0 et ne garder qu'une des deux prises ; préférer celle où la flamme reste seule source de lumière. |
| 6 | 2026-09-05 | michael-remonte-le-temps | promontoire boisé, vallée de feux, aube |  | tribus ennemies, conteur grave | Doublon de l'index 4 ; garder la version où le torque et la cape sont les plus lisibles. |
| 7 | 2026-09-05 | michael-remonte-le-temps | atelier romain de peintre d'écriteaux |  | une guerre résumée en trois mots | Le clip 2 (trois coups de pinceau espacés) est le plan clé pour un lettrage suivi ; vérifier lequel des trois clips cette extension contient. |
| 8 | 2026-09-05 | michael-remonte-le-temps | atelier romain, tréteaux, amphores |  | trois mots contre des pages entières | Milieu (3-6 s) : les trois coups de pinceau avec temps d'arrêt, idéal pour poser des mots en suivi de mouvement. |
| 9 | 2026-09-05 | michael-remonte-le-temps | atelier romain ouvert sur cour ensoleillée |  | le général qui écrivait trop | Début (0-4 s) : pinceau qui trace, peinture rouge qui coule, bon insert de texture ; fin parlée peu réutilisable hors épisode. |
| 10 | 2026-09-05 | michael-remonte-le-temps | atelier monétaire d'Alexandrie, nuit |  | il ne reste que l'image choisie | Fin (4-10 s) : plan poitrine avec le pot en albâtre net et la braise, chute posée ; début utile en insert produit. |
| 11 | 2026-09-05 | michael-remonte-le-temps | atelier monétaire, billot et établi |  | une matrice, mille pièces, même sceau | Début (0-5 s) : les deux coups de marteau et la pièce qui brille, geste percussif parfait pour un cut musical. |
| 12 | 2026-09-05 | michael-remonte-le-temps | atelier monétaire, fin de journée |  | la reine qui choisit son visage | Début (0-6 s) : burin, limaille, matrice levée à l'œil, gros travail de main sans parole. |
| 13 | 2026-09-05 | michael-remonte-le-temps | atelier d'imprimerie XVe, établi |  | 180 livres contre un seul copié | Milieu (2-4 s) : comparaison manuscrit / pile de livres, image de contraste forte ; fin parlée. |
| 14 | 2026-09-04 | michael-remonte-le-temps | atelier d'imprimerie XVe, presse à vis |  | l'effort de la première page imprimée | Milieu (5-8 s) : le coup de presse et la feuille décollée, geste physique et sonore idéal en clip. |
| 15 | 2026-09-04 | michael-remonte-le-temps | scriptorium de pierre, nuit, bougie |  | deux ans pour copier un livre | Début (0-6 s) : plume qui gratte et main qui tremble à la bougie, clair-obscur cinématographique. |
| 16 | 2026-09-04 | michael-remonte-le-temps | plage sous une voile, caisses de bois |  | le piment nommé poivre a changé le goût du monde | Fin (4-10 s) : bouteille nette au premier plan sous le visage, plan produit prêt pour un logo en suivi. |
| 17 | 2026-09-04 | michael-remonte-le-temps | plage des Caraïbes, chaloupe échouée |  | il cherchait le poivre, il a trouvé le feu | Milieu (3-7 s) : la morsure du piment et la réaction, moment comique physique universel. |
| 18 | 2026-09-04 | michael-remonte-le-temps | quai de port espagnol, aube |  | le poivre plus cher que l'or | Début (0-4 s) : grains de poivre dans la paume et descente de perche jusqu'au visage, belle ouverture. |
| 19 | 2026-08-31 | michael-fait-son-cinema-restaurant | scène de concours culinaire, confettis |  | victoire du jury, « juste les bons outils » | Début (0-2 s) explosion de confettis et fin (8-10 s) clin d'œil et salut : deux plans de conclusion pour un clip ou une pub. |
| 20 | 2026-08-31 | michael-fait-son-cinema-restaurant | passe entre cuisine et salle |  | brigade au pas militaire, fierté paternelle | Shot 2 (2-5 s) : le départ synchronisé des serveurs, très rythmique, parfait sur un temps fort musical. |
| 21 | 2026-08-31 | michael-fait-son-cinema-restaurant | table éclairée, salle sombre, juge |  | suspense du verdict, « techniquement irréprochable » | Shot 3 (5-8 s) : Michael qui avale sa salive, réaction réutilisable pour tout moment de tension. |
| 22 | 2026-08-31 | michael-fait-son-cinema-restaurant | poste de dressage sous lampes chauffantes |  | perfection au millimètre | Shot 1 (0-2 s) macro pince et micro-pousse : insert cuisine premium utilisable partout. |
| 23 | 2026-08-31 | michael-fait-son-cinema-restaurant | cuisine en plein rush, minuteur rouge | commandes en cuisine (KDS) | le calme du chef quand tout brûle | Shot 2 (2-5 s) : travelling rapide sur la cuisine en rush avec Michael immobile au centre, plan phare pour un clip et une démo KDS. |
| 24 | 2026-08-31 | michael-fait-son-cinema-restaurant | cuisine plateau TV, cloche d'argent | prise de commande papier | la boîte mystère pleine de tickets | Shot 2 (2-5 s) : le tas de tickets qui se déverse sous la cloche, image parfaite du problème « papier » avant la solution. |
| 25 | 2026-08-30 | cuisine-seedance-sans-texte | restaurant, objet net, chef flou | pilotage global (agents IA) |  | Milieu (5-8 s) : le changement d'état de l'objet, prévu pour une voix off posée au montage ; pas de son utilisable. |
| 26 | 2026-08-30 | michael-fait-son-cinema-restaurant | rue devant le restaurant, pile de CV | recrutement | personne ou trop de monde | Shot 3 (5-8 s) : la tempête de CV au ralenti, image forte du recrutement à l'ancienne ; doublon de l'index 64. |
| 27 | 2026-08-30 | michael-fait-son-cinema-restaurant | comptoir puis rue, crépuscule | caisse/compta | l'ardoise longue comme la rue | Shot 2 (2-5 s) : le rouleau qui se déroule jusque dans la rue, gag visuel lisible sans dialogue. |
| 28 | 2026-08-30 | michael-fait-son-cinema-restaurant | salle du restaurant, fin d'après-midi |  | générique de fin, tout roule | Début (0-5 s) : le recul continu avec les saluts de l'équipe, plan de conclusion idéal pour un « après » de pub. |
| 29 | 2026-08-30 | michael-fait-son-cinema-restaurant | salle avec tapis rouge, podium |  | le gagnant c'est le téléphone | Shot 3 (5-8 s) : le téléphone levé en trophée (écran flou), à réutiliser pour incruster l'application. |
| 30 | 2026-08-30 | michael-fait-son-cinema-restaurant | comptoir, arrière du bar, mur de tickets | caisse/compta | l'ardoise qui ne se paie jamais | Shot 3 (5-8 s) : le montage jour après jour du mur qui déborde, très efficace en accéléré. |
| 31 | 2026-08-30 | michael-fait-son-cinema-restaurant | bar puis cuisine, trente coupes | rupture de stock | le jeu qui vide le stock | Shot 3 (5-8 s) : chantilly et cerise au ralenti, moment comique et gourmand ; punchline « le stock aussi, il joue » en fin. |
| 32 | 2026-08-30 | michael-fait-son-cinema-restaurant | bar en mode jeu télé, roue de la fortune | rupture de stock | la roue qui s'emballe | Shot 4 (8-10 s) : la roue qui traverse la salle au ralenti ; shot 1 utile pour illustrer la roue de la fortune FoodEatUp. |
| 33 | 2026-08-30 | michael-fait-son-cinema-restaurant | salle pleine du samedi midi | planning équipe | « je gère » puis « j'ai validé quoi ? » | Shot 2 (2-5 s) : orbite accélérée de Michael qui fait tout seul, plan d'énergie pur pour un clip. |
| 34 | 2026-08-30 | michael-fait-son-cinema-restaurant | back-office sombre, fauteuil pivotant | planning équipe | trois samedis, rire qui se brise | Shot 2 (2-5 s) : les trois rires qui se fissurent, gag de montage en trois temps. |
| 35 | 2026-08-30 | michael-fait-son-cinema-restaurant | cuisine sous la vapeur, noir et blanc | nettoyage | le coupable, c'était moi | Shot 3 (5-8 s) : zoom sur la case du planning avec sa photo, chute visuelle ; le noir et blanc peut détonner dans un clip couleur. |
| 36 | 2026-08-30 | michael-fait-son-cinema-restaurant | cuisine la nuit, noir et blanc | nettoyage | qui a nettoyé la hotte ? moi ? | Shot 3 (5-8 s) : les trois qui se désignent en même temps, gag choral lisible sans son. |
| 37 | 2026-08-30 | michael-fait-son-cinema-restaurant | comptoir, téléphones qui sonnent | réservations | répondre à une spatule | Shot 3 (5-8 s) : montage des objets décrochés, absurde et rapide, parfait pour un enchaînement musical. |
| 38 | 2026-08-30 | michael-fait-son-cinema-restaurant | comptoir en heure de pointe, trois téléphones | réservations | « je vends quoi, là ? » | Shot 3 (5-8 s) : les trois téléphones qui sonnent ensemble, client et chef en fond, image de la surcharge téléphonique avant la réservation en ligne. |
| 39 | 2026-08-30 | michael-fait-son-cinema-restaurant | place du village puis salle | prise de commande | la commande mangée par le chien | Shot 2 (2-5 s) : l'échange pain contre serviette au ralenti avec le chien, très partageable. |
| 40 | 2026-08-30 | michael-fait-son-cinema-restaurant | terrasse venteuse puis rue et fontaine | prise de commande | la serviette de commande envolée | Shot 2 (2-5 s) : la poursuite de la serviette entre passants, voiture et vélo, action rythmée sans dialogue. |
| 41 | 2026-08-30 | michael-fait-son-cinema-restaurant | comptoir, habitué et assiettes | fichier client | le « comme d'habitude » deviné à l'aveugle | Shot 2 (2-5 s) : le comptoir qui déborde vu du dessus, gag d'accumulation ; la paume montrée en fin appelle une fiche client. |
| 42 | 2026-08-30 | michael-fait-son-cinema-restaurant | comptoir, mur de post-it à visages | fichier client | je ne sais pas c'est quoi, d'habitude | Shot 2 (2-5 s) : le mur de post-it avec rack focus, image parfaite de la mémoire client papier. |
| 43 | 2026-08-30 | michael-fait-son-cinema-restaurant | comptoir, mur de post-it à visages | fichier client | je ne sais pas c'est quoi, d'habitude | Doublon horizontal de l'index 42 ; préférer la version dont le mur de post-it est le plus net. |
| 44 | 2026-08-30 | michael-fait-son-cinema-restaurant | arrière-salle, lampe verte de casino | food cost / fiche technique | on perd deux euros par assiette | Shot 2-3 (2-8 s) : le crayon qui s'arrête et « quatorze de vente, seize de coût », dialogue clé pour une pub food cost. |
| 45 | 2026-08-30 | michael-fait-son-cinema-restaurant | arrière-salle, table de poker | food cost / fiche technique | le coût matière : « un peu » | Shot 3 (5-8 s) : les tickets retournés un à un avec « truffe ? un peu », ping-pong comique sur le coût matière. |
| 46 | 2026-08-30 | michael-fait-son-cinema-restaurant | vitrine couverte de calculs, crépuscule | caisse/compta | le dernier paie pour tout le monde | Shot 4 (8-10 s) : l'effondrement face contre table et le marqueur qui roule, chute silencieuse efficace. |
| 47 | 2026-08-30 | michael-fait-son-cinema-restaurant | salle, table de douze, vitrine | caisse/compta | l'addition séparée en équations | Shot 2 (2-5 s) : recul sur la vitrine entièrement couverte de calculs, image du partage d'addition impossible. |
| 48 | 2026-08-30 | michael-fait-son-cinema-restaurant | bar, brume, néons bleus | happy hour / marketing | les vampires du happy hour | Shot 2 (2-5 s) : mousse qui déborde, citrons volants, shaker au ralenti, montage bar très clip. |
| 49 | 2026-08-30 | michael-fait-son-cinema-restaurant | bar vide, cinq heures, lumière dorée | happy hour / marketing | ils sortent la nuit, l'ail ne marche pas | Shot 3 (5-8 s) : les cadres au ralenti qui convergent vers le bar, image de l'affluence déclenchée ; l'ail en fin est le gag. |
| 50 | 2026-08-30 | michael-fait-son-cinema-restaurant | rue de banlieue sous la pluie, scooter | livraison | la pizza livrée au mauvais foyer | Shot 2 (2-5 s) : le même rond-point trois fois et la boîte détrempée, montage rapide idéal. |
| 51 | 2026-08-30 | michael-fait-son-cinema-restaurant | rues puis chemin de campagne, scooter | livraison | le GPS mène à la vache | Shot 3 (5-8 s) : freinage devant le champ et la vache, gag visuel immédiat. |
| 52 | 2026-08-30 | michael-fait-son-cinema-restaurant | salle décorée, ballons, gâteau | réservations | souffler les bougies des autres | Shot 2 (2-5 s) : tables poussées deux, trois, huit jusqu'au trottoir en time-lapse ; fin « pardon » très drôle. |
| 53 | 2026-08-30 | michael-fait-son-cinema-restaurant | entrée du restaurant, samedi | réservations | douze… familles | Shot 2 (2-5 s) : le travelling latéral sans fin sur la foule qui entre, image de la réservation mal prise. |
| 54 | 2026-08-30 | michael-fait-son-cinema-restaurant | cuisine à l'aube, tour de crêpes | planning production | la 300e crêpe sur la tête | Shot 2 (2-5 s) : la crêpe qui monte à contre-jour et atterrit sur sa tête, gag physique pur. |
| 55 | 2026-08-29 | michael-fait-son-cinema-restaurant | cuisine à l'aube, entraînement de boxe | planning production | le training montage des crêpes | Shot 2 (2-5 s) : le montage d'entraînement à rampes de vitesse, énergie de clip ; crêpe au plafond en shot 3. |
| 56 | 2026-08-29 | michael-fait-son-cinema-restaurant | cave du restaurant, vision nocturne | facture | la facture retrouvée… impayée | Shot 3 (5-8 s) : la facture brandie triomphalement puis le visage qui tombe ; le look vision nocturne est marqué. |
| 57 | 2026-08-29 | michael-fait-son-cinema-restaurant | escalier et cave, boîtes de tickets | facture | chercher une facture à 3 h du matin | Shot 3 (5-8 s) : la boîte à chaussures qui libère des centaines de tickets, image du classement papier. |
| 58 | 2026-08-29 | michael-fait-son-cinema-restaurant | salle en tribunal, table du client | caisse/compta | le procès du tiramisu | Shot 3 (5-8 s) : le coup de louche sur la table avec réverbération, ponctuation parfaite au montage. |
| 59 | 2026-08-29 | michael-fait-son-cinema-restaurant | salle éclairée en tribunal | caisse/compta | « c'est… du café » | Shot 3 (5-8 s) : le crash zoom sur la joue tachée de cacao, gag rapide et lisible. |
| 60 | 2026-08-29 | michael-fait-son-cinema-restaurant | salle inondée par l'orage, quarante clients | terrasse météo / placement | presque tout le monde est là | Shot 3 (5-8 s) : comptage des têtes au ralenti puis rack focus sur le client dehors, chute visuelle. |
| 61 | 2026-08-29 | michael-fait-son-cinema-restaurant | terrasse ensoleillée puis tempête | terrasse météo / placement | « belle journée » puis déluge | Shot 3 (5-8 s) : chaos de la terrasse sous la pluie, parasols et nappes en vol, très fort en clip. |
| 62 | 2026-08-29 | michael-fait-son-cinema-restaurant | entrée du restaurant, file de centaines | campagne marketing | la promo envoyée à toute la ville | Shot 1 (0-2 s) : le drone sur la file qui serpente dans le quartier, plan spectaculaire pour illustrer une campagne qui marche trop bien. |
| 63 | 2026-08-29 | michael-fait-son-cinema-restaurant | back-office sombre, bouton rouge | campagne marketing | le bouton « envoyer » nucléaire | Shot 3 (5-8 s) : les cinq cutaways de téléphones qui vibrent, illustre une campagne SMS/WhatsApp en un clin d'œil. |
| 64 | 2026-08-29 | michael-fait-son-cinema-restaurant | rue devant le restaurant, pile de CV | recrutement | personne ou trop de monde | Doublon de l'index 26 ; garder la version où la tempête de CV (5-8 s) est la plus lisible. |
| 65 | 2026-08-29 | michael-fait-son-cinema-restaurant | salle transformée en plateau de casting | recrutement | suivant, suivant, suivant | Shot 3 (5-8 s) : « je travaille pas le week-end » puis le candidat inaudible, enchaînement comique en trois temps. |
| 66 | 2026-08-29 | michael-fait-son-cinema-restaurant | bar, écran de ralenti vidéo | planning équipe | la VAR du retard | Shot 4 (8-10 s) : la glissade sur les genoux du serveur et les bras levés, célébration très clip. |
| 67 | 2026-08-29 | michael-fait-son-cinema-restaurant | entrée du restaurant en ligne d'arrivée | planning équipe | une seconde de retard sifflée | Shot 1-2 (0-5 s) : le sprint au ralenti et le freeze photo-finish, image du pointage à la seconde. |
| 68 | 2026-08-29 | michael-fait-son-cinema-restaurant | réserve, étagère de bouteilles | inventaire stock | la boucle temporelle de l'inventaire | Shot 2 (2-5 s) : le match-cut du mur écrit puis propre, gag de montage propre ; fin résignée avec la bouteille. |
| 69 | 2026-08-29 | michael-fait-son-cinema-restaurant | réserve, réveil sur une caisse | inventaire stock | douze, onze, quinze : encore ? | Shot 3 (5-8 s) : les trois jump-cuts identiques avec un chiffre différent, illustration parfaite de l'inventaire manuel faux. |
| 70 | 2026-08-29 | michael-fait-son-cinema-restaurant | cuisine en alerte rouge puis porte de la salle | commandes en cuisine (KDS) | remonter à la surface de la salle | Shot 3 (5-8 s) : travelling à travers la porte vers le blanc surexposé de la salle, transition cuisine/salle magnifique. |
| 71 | 2026-08-29 | michael-fait-son-cinema-restaurant | cuisine en lumière rouge, imprimante à tickets | commandes en cuisine (KDS) | ça fait beaucoup de ping | Shot 3 (5-8 s) : la rafale de tickets qui sort de l'imprimante et s'enroule au sol, image du rush de commandes. |
| 72 | 2026-08-29 | michael-fait-son-cinema-restaurant | table de fenêtre, plante verte | avis client / influenceur | et le cycle recommence | Shot 2 (2-5 s) : Michael qui émerge de la plante au ralenti avec l'assiette fumante, image absurde et belle. |
| 73 | 2026-08-29 | michael-fait-son-cinema-restaurant | table de fenêtre, ring light, plante verte | avis client / influenceur | le client qui filme, dans son habitat | Shot 2 (2-5 s) : orbite autour de la table et vapeur qui s'évanouit en time-lapse, plan très reconnaissable. |
| 74 | 2026-08-29 | michael-fait-son-cinema-restaurant | salle puis cuisine, deux bols de sauce | allergènes | elle m'a dit quel légume, déjà ? | Shot 3 (5-8 s) : alternance rapide bol rouge / bol vert / yeux, tension idéale avant une solution « allergènes notés ». |
| 75 | 2026-08-29 | michael-fait-son-cinema-restaurant | cuisine puis table de la cliente | allergènes | le plat le plus sûr : pain et eau | Shot 2 (2-5 s) : la fiche recette illisible retournée, argument fiche technique ; shot 4 chute sobre. |
| 76 | 2026-08-29 | michael-fait-son-cinema-restaurant | salle puis cuisine, deux bols de sauce | allergènes | c'est laquelle ? | Shot 1 (0-2 s) : le sourire qui tombe dès qu'il se retourne, réaction réutilisable ; comparer avec l'index 74 pour la meilleure prise. |
| 77 | 2026-08-29 | michael-fait-son-cinema-restaurant | cuisine ensevelie sous les oignons | commande fournisseur | je pleure pas, c'est les oignons | Shot 2 (2-5 s) : l'escalade au ralenti sur la montagne d'oignons, image spectaculaire de la surcommande. |
| 78 | 2026-08-29 | michael-fait-son-cinema-restaurant | bar fermé, lampe frontale, tiroir-caisse | caisse/compta | il manque cinq euros | Shot 1 (0-2 s) : macro sur les tours de pièces balayées par la frontale, insert caisse superbe. |
| 79 | 2026-08-29 | michael-fait-son-cinema-restaurant | bar puis rue, camion de livraison | commande fournisseur | dix palettes au lieu de dix oignons | Shot 2 (2-5 s) : la contre-plongée sur la montagne de palettes qui descend du hayon, plan monstre-movie pour une erreur de commande. |
| 80 | 2026-08-29 | michael-fait-son-cinema-restaurant | bar la nuit, horloge, tiroir-caisse | caisse/compta | le billet oublié dans le tablier | Shot 2 (2-5 s) : le time-lapse de la nuit de recomptage, gag d'accumulation ; chute « ah, c'est moi ». |
| 81 | 2026-08-29 | michael-fait-son-cinema-restaurant | salle prise d'assaut, brunch | file d'attente | ils ont faim, moi aussi | Shot 2 (2-5 s) : montage hyper rapide des assiettes qui traversent la salle, énergie de rush. |
| 82 | 2026-08-29 | michael-fait-son-cinema-restaurant | salle prise d'assaut, brunch | file d'attente | ils ont faim, moi aussi | Doublon de l'index 81 ; ne garder que la meilleure version du shot 1 (porte qui cède, cheveux soufflés). |
| 83 | 2026-08-29 | michael-fait-son-cinema-restaurant | restaurant vide, dimanche matin, vitrine | file d'attente | les zombies du brunch | Shot 3 (5-8 s) : les mains qui se plaquent sur la vitre une à une, image mémorable de l'affluence. |
| 84 | 2026-08-29 | michael-fait-son-cinema-restaurant | cuisine, ampoule nue, boîte de post-it | HACCP températures | je note tout, dans ma tête | Shot 4 (8-10 s) : les post-it qui s'envolent au ralenti pendant que Michael reste immobile, image parfaite du relevé papier perdu. |
| 85 | 2026-08-29 | michael-fait-son-cinema-restaurant | cuisine dans le noir, interrogatoire | HACCP températures | vos températures ? quelque part | Shot 2-3 (2-8 s) : « vos températures ? » et le post-it froissé, dialogue clé pour une pub HACCP. |
| 86 | 2026-08-29 | michael-fait-son-cinema-restaurant | bar en fin de service, chaises sur les tables | avis client | une étoile… le livreur | Shot 2 (2-5 s) : le sourire qui se fige sur la notification floue, à réutiliser pour incruster un avis ; crash zoom final. |
| 87 | 2026-08-28 | michael-fait-son-cinema-restaurant | salle pleine, derrière le bar, passoire | avis client | le critique imaginaire | Shot 1 (0-2 s) : le POV à travers les trous de la passoire, ouverture graphique originale. |
| 88 | 2026-08-28 | michael-fait-son-cinema-restaurant | bistrot à midi, table disputée | réservations | table pour trois | Shot 3 (5-8 s) : la table traînée dans un nuage de poussière puis les deux clients dos à dos, chute visuelle. |
| 89 | 2026-08-28 | michael-fait-son-cinema-restaurant | bistrot à midi, western | réservations | j'ai réservé deux fois | Shot 2 (2-5 s) : les deux clients qui convergent au ralenti vers la même table, image du double booking ; freeze final. |
| 90 | 2026-08-26 | planit-corporate | bureau moderne, tablette sur le bureau |  |  | Tout le plan est une plaque d'incrustation : utiliser 3-9 s pour composer l'écran réel de l'application. |
| 91 | 2026-08-26 | planit-corporate | bureau moderne, carnet violet |  | surprise silencieuse à la lecture | Milieu (4-6 s) : le haussement de sourcils, micro-réaction utile en plan de coupe. |
| 92 | 2026-08-26 | planit-corporate | bureau moderne, porte et bureau |  | le carnet s'est rempli tout seul | Fin (4.6-10 s) : découverte du carnet et téléphone reposé, geste signifiant « plus besoin de l'écran ». |
| 93 | 2026-08-26 | planit-corporate | bureau moderne, carnet violet ouvert |  | le travail se fait sans main | Plan complet utilisable : deux tournes de page à 3 s et 6.5 s, bon plan de respiration ou de transition. |
| 94 | 2026-08-26 | planit-corporate | bureau moderne vide, plan large |  | présence invisible | Plan d'ambiance entier ; le frémissement à 6 s est le seul événement, à garder pour une fin de séquence. |
| 95 | 2026-08-26 | planit-corporate | bureau moderne, porte |  | partir sans son téléphone | Fin (5-10 s) : sortie par la porte et cadre tenu sur le bureau vide, plan de clôture. |
| 96 | 2026-08-26 | planit-corporate | bureau moderne vide, deuxième poste |  |  | Plan complet : variation lumineuse continue, sert de plan de coupe « le temps passe ». |
| 97 | 2026-08-26 | planit-corporate | bureau moderne, surface du bureau |  | le téléphone retourné, geste de lâcher-prise | Début (0-3 s) : le geste de retourner le téléphone, symbole clair ; le reste est du silence utile en pause. |
| 98 | 2026-08-25 | planit-corporate | bureau moderne, gros plan visage |  |  | Milieu (3-5.5 s) : la phrase parlée, seule ligne de l'acte, à garder synchro ; ensuite attente calme. |
| 99 | 2026-08-25 | planit-corporate | bureau moderne, matin ordinaire |  |  | Plan d'exposition entier ; garder le début (0-4 s) pour établir le bureau et le carnet violet. |
| 100 | 2026-08-25 | planit-corporate | home office 2022, bureau de nuit |  | le clavier repoussé, fin de nuit | Milieu (3.6-5 s) : le clavier repoussé, geste de renoncement net. |
| 101 | 2026-08-25 | planit-corporate | home office 2022, gros plan de nuit |  | fatigue devant l'écran | Milieu (4-6 s) : les yeux frottés, micro-geste de fatigue réutilisable. |
| 102 | 2026-08-25 | planit-corporate | home office 2022, pile d'impressions |  | des pages imprimées jamais lues | Début (0-4.6 s) : la feuille posée et les deux tapes, puis immobilité utile comme plan de coupe. |
| 103 | 2026-08-25 | planit-corporate | home office 2022, gros plan face à l'écran |  | juger une réponse de l'IA | Milieu (2.4-7 s) : la lecture et le doute, expression nuancée pour une narration sur la confiance. |
| 104 | 2026-08-25 | planit-corporate | home office 2022, mains sur le clavier |  | écrire, effacer, réécrire | Plan complet en slider ; les effacements à 2.8 s et 6.9 s rythment bien un insert. |
| 105 | 2026-08-25 | planit-corporate | home office 2022, écran sombre |  | attendre que la machine réponde | Milieu (2.6-7 s) : la lueur qui pulse et la lecture, plan d'attente calme. |
| 106 | 2026-08-25 | planit-corporate | petit appartement 2008, lit, nuit |  | l'écran qui meurt | Milieu (2.4-6.6 s) : l'extinction progressive puis le noir, plan de rupture très lisible. |
| 107 | 2026-08-25 | planit-corporate | couloir public la nuit, prise au sol |  | chercher une prise, dépendance au chargeur | Milieu (2.6-6 s) : le câble qui accroche et le branchement raté puis réussi, gestes concrets. |
| 108 | 2026-08-25 | planit-corporate | table en bois, douze écrans en grille |  | douze écrans, tous identiques | Plan complet : l'allumage un à un des douze rectangles, très graphique, tient dix secondes. |
| 109 | 2026-08-25 | planit-corporate | rame de métro la nuit |  | absorbé par l'écran | Fin (5-10 s) : secousse absorbée sans lever les yeux et lumières du tunnel sur le visage. |
| 110 | 2026-08-25 | planit-corporate | fond noir, main et téléphone |  | le scroll infini | Fin (6.5-10 s) : l'hésitation du cinquième swipe et le pouce arrêté, geste symbolique. |
| 111 | 2026-08-25 | planit-corporate | trottoir de nuit, file devant une boutique |  | la file d'attente pour un appareil | Milieu (2-7.4 s) : lean-out, buée et deux pas en avant, plan d'attente qui raconte 2008. |
| 112 | 2026-08-25 | planit-corporate | petit bureau près de la salle des machines, 1989 |  | fermer le tiroir des fiches papier | Fin (7.6-10 s) : le tiroir refermé d'un geste et la main posée dessus, point final d'époque. |
| 113 | 2026-08-25 | planit-corporate | salle des machines 1989, câble vers le mur |  | où va le câble | Milieu (1.6-6 s) : le regard qui remonte le câble jusqu'au conduit, mouvement lent et lisible. |
| 114 | 2026-08-25 | planit-corporate | salle des machines 1989, plancher technique |  | l'effort de brancher | Milieu (3.8-5.2 s) : le câble qui cède sous la paume, puis la dalle remise à 9 s. |
| 115 | 2026-08-24 | planit-corporate | salle des machines 1989, couloir d'armoires |  | attendre que ça marche | Fin (7-10 s) : la micro-réaction aux 7.8 s après quatre secondes de rien, à garder entière. |
| 116 | 2026-08-24 | planit-corporate | panneau d'armoire 1989, voyants |  | le voyant qui finit par s'allumer | Plan complet : clignotements réguliers puis allumage à 7.9 s, insert graphique très propre. |
| 117 | 2026-08-24 | planit-corporate | salle des machines 1989, entrée |  | découvrir la machine | Début (0-4.6 s) : l'entrée en six pas dans le couloir de voyants, plan d'exposition d'époque. |
| 118 | 2026-08-24 | planit-corporate | atelier d'époque, portes doubles |  | fermer l'atelier sur l'invention | Milieu (4.4-7.4 s) : les deux battants qui coupent la lumière puis la barre, obscurcissement motivé très beau. |
| 119 | 2026-08-24 | planit-corporate | atelier d'époque, établi, carnet |  | raturer et recommencer | Milieu (2.4-6.4 s) : la rature et le silence de réflexion, plan d'insert utile pour « itération ». |
| 120 | 2026-08-24 | planit-corporate | rue pavée devant l'atelier |  | la machine bouge pour la première fois | Milieu (1.5-6 s) : la roue qui se libère et la machine qui avance, moment de bascule de l'acte. |
| 121 | 2026-08-24 | planit-corporate | rue pavée, sortie de l'atelier |  | seul dans la rue avec l'invention | Début (0-6 s) : regards à gauche et à droite dans la rue déserte, plan d'attente d'époque. |
| 122 | 2026-08-24 | planit-corporate | atelier d'époque, manivelle |  | forcer jusqu'à ce que ça cède | Milieu (4.4-7.6 s) : la manivelle qui bloque puis cède, geste d'effort très cinématographique. |
| 123 | 2026-08-23 | planit-corporate | bureau partagé, plan large depuis la porte |  | lire, poser, partir | Fin (6-10 s) : sortie et bureau vide avec les bandes de lumière, plan de clôture. |
| 124 | 2026-08-23 | planit-corporate | bureau partagé, tiroir |  | tout ranger dans le tiroir | Milieu (5.4-8.6 s) : les bords tapés puis le tiroir refermé d'un seul mouvement. |
| 125 | 2026-08-23 | planit-corporate | bureau partagé, surface du bureau |  | les mains qui lâchent | Début (0-3.6 s) : les mains qui se retirent ; le reste est une pause silencieuse pour une voix off. |
| 126 | 2026-08-23 | planit-corporate | bureau partagé, gros plan visage |  |  | Milieu (5-7 s) : la ligne parlée, à garder synchro ; premières secondes utiles en réaction muette. |
| 127 | 2026-08-23 | planit-corporate | bureau partagé, pile de devis |  | les devis qui tombent, il laisse faire | Fin (6.2-10 s) : les feuilles qui tombent et l'immobilité résignée, plan de problème. |
| 128 | 2026-08-22 | planit-corporate | bureau partagé, deuxième bureau |  | quelqu'un a travaillé ici | Plan complet en push lent ; le frémissement à 6.8 s est le seul événement, plan de mystère. |
| 129 | 2026-08-22 | planit-corporate | bureau partagé, plan moyen |  | poser le stylo | Milieu (3-6 s) : feuille puis stylo posés, puis retrait des mains, geste de délégation. |
| 130 | 2026-08-22 | planit-corporate | bureau partagé, mains et bac |  | le geste manuel répétitif | Plan complet : quatre cycles avec ralentissement, insert parfait pour « tâche répétitive ». |
| 131 | 2026-08-22 | planit-corporate | bureau partagé, deux bureaux en cadre |  | regarder le bureau vide | Milieu (5.4-7.4 s) : le regard tenu vers le bureau vide, image du collègue absent. |
| 132 | 2026-08-22 | planit-corporate | bureau partagé, post-it vierges |  | lire, poser, partir | Fin (6.4-10 s) : départ avec le carnet sous le bras et bureau vide. |
| 133 | 2026-08-22 | planit-corporate | bureau partagé, plan large caméra à l'épaule |  | ne rien faire pendant que ça travaille | Milieu (2.4-8.6 s) : regard fenêtre, chaise reculée, gorgée ; plan de sérénité pour un « après ». |
| 134 | 2026-08-22 | planit-corporate | bureau partagé, vue du dessus |  | remettre de l'ordre | Début (1.2-6.2 s) : le balayage des post-it vers le centre, geste de tri graphique. |
| 135 | 2026-08-22 | planit-corporate | bureau partagé, gros plan visage |  |  | Milieu (5.2-7 s) : la ligne parlée ; garder les secondes précédentes pour l'expression fatiguée. |
| 136 | 2026-08-22 | planit-corporate | bureau partagé, post-it, téléphone qui vibre |  | interrompu jusqu'à renoncer | Milieu (5-8 s) : la deuxième vibration qui arrête le stylo et les notes qui tombent. |
| 137 | 2026-08-21 | planit-corporate | bureau partagé, post-it, téléphone qui vibre |  | interrompu jusqu'à renoncer | Doublon de l'index 136 ; garder la prise où les deux notes tombent le plus lisiblement à 6.5 s. |
| 138 | 2026-08-21 | planit-corporate | atelier d'époque, machine de fer |  | contempler l'invention finie | Milieu (2.5-8 s) : le pas en arrière et l'essuyage des mains en trois passes, geste d'accomplissement. |
| 139 | 2026-08-21 | planit-corporate | bureau partagé, séquence de cinq plans |  | les devis en retard, puis lâcher prise | Shot 1 (0-10 s) et shot 2 (10-14 s) pour le problème et la phrase ; shot 5 pour la conclusion ; vérifier quelle portion de 10 s a été rendue. |
| 140 | 2026-08-21 | planit-corporate | bureau partagé, séquence de cinq plans |  | les devis en retard, puis lâcher prise | Doublon horizontal de l'index 139 ; garder le shot 2 (phrase) de la version dont le visage est le plus stable. |
| 141 | 2026-08-21 | cuisine-seedance-sans-texte | restaurant, objet net, chef flou | dépendance plateformes | vos clients ou ceux de la plateforme ? | Milieu (5-8 s) : le changement d'état de l'objet, prévu pour une voix off ; les lèvres bougent, ne pas poser un autre texte dessus. |
| 142 | 2026-08-20 | cuisine-seedance-sans-texte | cuisine, frigo, chef flou | rupture de stock | une rupture le samedi, la poubelle le dimanche | Milieu (5-8 s) : l'objet qui change d'état, image de stock réel ; fin figée utilisable pour une incrustation. |
| 143 | 2026-08-19 | cuisine-seedance-sans-texte | cuisine, thermomètre ou registre, chef flou | HACCP températures | l'échec qui coûte la fermeture | Milieu (5-8 s) : changement d'état de l'objet sanitaire, à combiner avec les index 84-85 pour un bloc HACCP. |
| 144 | 2026-08-19 | cuisine-seedance-sans-texte | salle ou planning mural, chef flou | planning équipe | combien de couverts, vraiment | Milieu (5-8 s) : le changement d'état ; fin figée à 8-10 s pour une incrustation de planning. |
| 145 | 2026-08-19 | cuisine-seedance-sans-texte | cuisine, fiche technique, chef flou | food cost / fiche technique | une fiche fausse, tout est faux | Milieu (5-8 s) : changement d'état de l'objet ; à combiner avec les index 44-45 pour le food cost. |
| 146 | 2026-08-19 | cuisine-seedance-sans-texte | table de restaurant, touriste, serveur | prise de commande | ni l'un ni l'autre ne sait ce qui va arriver | Début (0-5 s) : le serveur qui acquiesce stylo en l'air, gag lisible ; entrée du chef à 8 s pour la punchline mimée. |
| 147 | 2026-08-19 | cuisine-seedance-sans-texte | salle puis passe de cuisine, film de fantômes | prise de commande | le supplément fantôme | Début (0-5 s) : l'encre qui disparaît lettre après lettre, effet visuel fort pour une commande perdue. |
| 148 | 2026-08-19 | cuisine-seedance-sans-texte | table, set de table griffonné, poubelle | devis groupe | le devis parti à la poubelle avec le set | Début (0-5 s) : gros plan sur le set de table griffonné et froissé, image du devis manuscrit perdu. |
| 149 | 2026-08-19 | cuisine-seedance-sans-texte | cuisine, flambage de crevettes |  | le flambage qui dérape, sourcils roussis | Début (0-4 s) : la flamme qui explose plein cadre, plan choc ; fin (8-10 s) regard blanc à la caméra pour une chute. |
