# Les 150 prompts HeyGen — segment avatar (10 s)

Un prompt = un segment D du master (16,0 → 26,0 s). L'avatar est en haut, le logiciel en bas.
**L'avatar parle avec sa voix HeyGen. Aucune voix ElevenLabs sur ce segment.**

---

## 1. Le prompt HeyGen — gabarit unique

Ce bloc est identique sur les 150. Seuls le **script** et le **chapitre Drive** changent. Colle-le tel quel dans HeyGen, en remplaçant les deux crochets.

```
Avatar : [ton avatar 3D FoodEatUp]
Format : 9:16 · 1080×1920 · durée cible 10 s (max 12 s)
Cadrage : plan poitrine, avatar centré dans le tiers supérieur, regard caméra
Fond : uni charte FoodEatUp (ou fond vert si tu veux l'incruster toi-même)
Voix : voix FR de l'avatar, débit posé, ton direct, tutoiement
Musique : AUCUNE (le montage gère l'audio)
Sous-titres HeyGen : DÉSACTIVÉS (burn-in fait au montage)
Gestes : naturels, une seule main, pas de pointage vers le bas du cadre
Script : « [SCRIPT DE L'ÉPISODE] »
```

**Variante LinkedIn (optionnelle)** : même prompt, script doublé (≈ 55 mots, 20 s), fichier `EPxx_long.mp4`.

---

## 2. Règles d'écriture (appliquées aux 150 scripts)

- **25 à 30 mots.** C'est 10 secondes à débit normal. Au-delà, l'avatar accélère et ça s'entend.
- **Une action, un bénéfice, une preuve.** Jamais deux fonctionnalités dans le même segment.
- **Tutoiement, présent de l'indicatif, pas de conditionnel.** « Tu vois », pas « tu pourrais voir ».
- **Première phrase = ce qui est à l'écran.** L'avatar commente le screencast, il ne parle pas dans le vide.
- **Pas de chiffre inventé.** Aucun « +30 % de CA » : on montre le logiciel, on ne promet pas un résultat chiffré.
- **Jamais le mot « solution ».** Il est réservé au hook de fin (« une infinité de solutions »).
- **Pas de CTA.** Le CTA est dans le segment E, en voix ElevenLabs. L'avatar s'arrête sur le bénéfice.

Notation ci-dessous : `EPxx` · **Module › Chapitre Drive** — puis le script entre guillemets.
Un même chapitre peut servir plusieurs épisodes : le screencast est le même, le script change.

---

## 3. Saison 1 — EP01 → EP30

**EP01** · Service › 1 - Commandes multi-canaux
> « Ici, toutes tes commandes arrivent au même endroit : la salle, le téléphone, le site, la livraison. Une seule file, dans l'ordre d'arrivée. Plus personne n'attend parce qu'on a oublié un ticket. »

**EP02** · Service › 3 - Envoi direct cuisine
> « Tu prends la commande à table, elle part en cuisine dans la seconde. Pas de carnet, pas d'aller-retour, pas de ticket perdu entre la salle et le pass. »

**EP03** · StockVision › 1 - Ma carte
> « Chaque plat de ta carte a son coût matière calculé depuis tes ingrédients. Tu vois ta marge réelle, plat par plat, avant même de fixer ton prix. »

**EP04** · Caisse POS › 1 - Configurer sa caisse
> « Ta caisse se configure en quelques minutes : TPE, ticket, moyens de paiement. Elle est reliée à ta carte et à ta cuisine, pas posée à côté. »

**EP05** · Configuration › vue d'ensemble
> « Un seul paramétrage : ta carte, tes zones, tes tables, ta TVA. Tout le reste s'appuie dessus. Tu ne ressaisis jamais deux fois la même information. »

**EP06** · StockVision › 17 - Ajouter et modifier un mouvement
> « Tu envoies un plat, le stock bouge tout seul. Chaque sortie est tracée, avec la quantité et l'heure. Tu sais ce qu'il te reste sans compter les cartons. »

**EP07** · Marketing › 3 - Répondre aux avis
> « Tes avis Google remontent ici. Tu réponds depuis FoodEatUp, l'IA te propose une réponse dans ton ton, tu valides. Le client voit que tu l'as lu. »

**EP08** · Comptabilité › facturation
> « Chaque commande génère sa facture. Tu retrouves le facturé, l'encaissé et les impayés dans le même écran. La fin de mois devient une lecture, pas une reconstitution. »

**EP09** · Caisse POS › 7 - Suivre les écarts de caisse
> « À chaque clôture, l'écart entre le théorique et le compté s'affiche. Tu vois quel service dérape et de combien. Ce qui se mesure s'arrête. »

**EP10** · PrediBot › 1 - Lire ses prévisions
> « Un écran, le matin : ton chiffre d'affaires prévu, ta fréquentation, tes points de tension. C'est ton point du jour, sans ouvrir dix onglets. »

**EP11** · HubRise & Livraisons › 1 - Connecter son HubRise
> « Tu connectes HubRise une fois. Tes plateformes de livraison envoient leurs commandes directement dans FoodEatUp. Plus de tablette à surveiller dans un coin. »

**EP12** · KDS › 3 - Gérer le KDS en direct
> « Le KDS affiche chaque plat, son poste et son temps d'attente. Le client ne regarde plus la cuisine : il regarde son plat arriver. »

**EP13** · PrediBot › 3 - Parler à PrediBot
> « Tu poses ta question en français : combien j'ai fait hier, qu'est-ce qui manque demain. PrediBot lit tes vraies données et te répond. Une seule interface, pas dix. »

**EP14** · StockVision › 16 - Mouvements de stock
> « Chaque entrée, chaque sortie, chaque perte est enregistrée. Tu vois ce qui part sans être vendu. Le gaspillage devient une ligne, donc un problème réglable. »

**EP15** · Configuration › référentiels
> « Tes catégories, ta TVA, tes zones, tes équipements : tout est posé une fois, proprement. Quand une pièce bouge, le reste ne s'écroule pas. »

**EP16** · Comptabilité › dépenses
> « Tu enregistres tes achats fournisseurs avec le détail des lignes. Tes dépenses du mois s'additionnent toutes seules, en face de ton chiffre d'affaires. »

**EP17** · StockVision › 19 - Création d'un rapport
> « Tu génères ton rapport par module en un clic : ventes, stock, production. L'historique est gardé. Tu compares ce mois-ci avec le mois dernier, pas avec ton souvenir. »

**EP18** · Service › 2 - Site, vocal et QR code
> « Pendant le rush, tes clients commandent seuls : par QR à table, par le site, par l'agent vocal. Ton équipe sert, elle ne court plus. »

**EP19** · StockVision › 3 - Prédictions des commandes
> « FoodEatUp regarde tes ventes passées et te dit quoi produire demain. Ton chiffre d'affaires ne dépend plus de ton intuition du lundi matin. »

**EP20** · Réservation › 2 - Ajouter une réservation
> « Tu ajoutes une réservation en dix secondes, la table libre est proposée automatiquement. Et tes clients peuvent le faire eux-mêmes, depuis ton site. »

**EP21** · KDS › 1 - Créer tes postes KDS
> « Tu crées tes postes : chaud, froid, dessert. Chaque plat part au bon écran. Plus d'imprimante à secouer au milieu du service. »

**EP22** · PrediBot › 2 - Marketplace de prompts
> « Tout est déjà là : caisse, stock, planning, marketing, HACCP. Un seul abonnement, une seule base de données. Tes outils arrêtent de s'ignorer. »

**EP23** · Marketing › 24 - Calendrier IA avec Iris
> « Iris regarde ton exploitation et te propose quoi publier, et pourquoi. Tu valides ou tu refuses. L'automatisation te sert, elle ne t'échappe pas. »

**EP24** · Mon Site › 5 - Créer un site par IA
> « Ton site de commande est créé par l'IA depuis ta carte. Tes clients commandent en direct, chez toi. Zéro commission sur ces commandes-là. »

**EP25** · Marketing › 6 - Campagne 100 % IA
> « Tu ne lances plus une promo au hasard. FoodEatUp te propose la campagne depuis tes vraies données clients : qui cibler, avec quelle offre, quel jour. »

**EP26** · StockVision › 5 - Envoyer sa liste de courses au fournisseur
> « Ta liste de courses se construit depuis ta production prévue. Tu l'envoies au fournisseur depuis l'écran. Le week-end se prépare le mercredi. »

**EP27** · Caisse POS › 6 - Clôturer sa caisse, le Z
> « Ton Z de caisse en un bouton : le compté, le théorique, l'écart, les moyens de paiement. Tu sais où tu en es tous les lundis matin. »

**EP28** · HubRise › 4 - Centraliser les commandes
> « Uber Eats, Deliveroo, ton site, le comptoir : tout tombe dans la même file. Un vendredi soir, tu regardes un écran, pas quatre. »

**EP29** · PrediBot › 1 - Lire ses prévisions
> « Le brief du jour te dit ce qui compte avant que ça te tombe dessus : les réservations, les productions, les alertes. Tu diriges au lieu de courir. »

**EP30** · Configuration › Academy
> « Le nouveau se forme tout seul : chaque module a ses vidéos, dans l'ordre. Tu ne réexpliques plus la caisse à chaque embauche. »

---

## 4. Saison 2 — EP31 → EP48

**EP31** · HACCP › étiquettes DLC
> « Tu crées ton étiquette DLC en trois secondes, avec le produit, la date et l'agent. Plus personne n'ouvre un bac en se demandant ce que c'est. »

**EP32** · StockVision › 1 - Ma carte, fiche recette
> « Ta recette est enregistrée : ingrédients, quantités, étapes. Le plat sort pareil que ce soit toi ou ton commis. Et son coût est calculé. »

**EP33** · StockVision › 16 - Mouvements de stock
> « Ce qui n'est pas suivi disparaît. Ici chaque produit a son niveau, son seuil et son historique. Tu vois le trou avant le service, pas après. »

**EP34** · Configuration › process
> « Tes procédures sont dans l'outil, pas dans ta tête. Le service ne dépend plus de qui est là ce soir. »

**EP35** · PrediBot › 1 - Lire ses prévisions
> « Prévisions de fréquentation, météo, événements du quartier : PrediBot te dit à quoi ressemble ton service avant qu'il commence. »

**EP36** · PrediBot › 2 - Un seul abonnement
> « Additionne tes abonnements actuels. Ici, la caisse, le stock, le planning, la compta et le marketing sont dans le même outil, sur la même base. »

**EP37** · Équipe & Planning › créer un shift
> « Tu construis le planning de la semaine par glisser-déposer, avec le coût qui s'affiche en direct. Tes équipes savent, et toi aussi. »

**EP38** · StockVision › 4 - Ma liste de courses
> « Ta commande fournisseur se construit depuis tes stocks bas et ta production prévue. Tu ne commandes plus à l'instinct dans les rayons. »

**EP39** · Réservation › 3 - Gérer et no-shows
> « L'imprévu, tu ne l'évites pas. Mais tu vois en direct l'état de ta salle, tes retards et tes annulations, et tu réattribues en un geste. »

**EP40** · StockVision › 17 - Ajouter un mouvement
> « Tu comptes une fois, l'outil compte ensuite. Chaque sortie d'ingrédient est déduite de ton stock, plat par plat. »

**EP41** · StockVision › 15 - Sortie des ingrédients de la production
> « La production sort exactement les quantités prévues de ton stock. Ce qui tombe au sol, tu le vois dans l'écart. Et ce qui se voit se corrige. »

**EP42** · Marketing › 21 - MCP RapidoCMS et Iris
> « Tu n'as pas à tout faire seul. Iris prépare tes contenus, PrediBot surveille tes chiffres, tu gardes la validation. »

**EP43** · Caisse POS › 4 - Remises et avoirs
> « Chaque remise et chaque avoir est tracé, avec qui l'a fait et pourquoi. Les petits gestes ne mangent plus ta marge en silence. »

**EP44** · Réservation › 5 - Commander par QR code
> « Le client scanne, commande, la cuisine reçoit. Ton serveur passe son temps en salle, pas à recopier des lignes sur un carnet. »

**EP45** · StockVision › 18 - Statistiques par module
> « Ton restaurant arrête d'être une boîte noire : ventes, marges, fréquentation, stock, module par module, sur la période que tu choisis. »

**EP46** · StockVision › 20 - Agent IA et suggestions
> « L'IA remonte ce que tu n'as pas le temps de voir : un coût qui monte, un plat qui décroche, un stock qui dort. Le petit détail devient visible. »

**EP47** · HACCP › contrôle à réception
> « À la livraison, tu contrôles la température, tu prends la photo, c'est tracé. Sept heures du matin, et ta conformité est déjà faite. »

**EP48** · Configuration › paramétrage initial
> « Tu poses ta base une fois : établissement, TVA, zones, équipements. Tout le reste de FoodEatUp s'appuie dessus sans que tu y reviennes. »

---

## 5. Saison 3 — EP49 → EP90 · pool de 42 scripts

Je n'ai pas les titres des EP49 → EP90. Ces 42 scripts couvrent les chapitres pas encore exploités par les autres saisons. **Assigne-les par module** : quand tu m'enverras les titres, je fige le mapping définitif.

### HACCP (14 scripts — module `10rqzHFjXbjkGi73uJyjt3XQM92eaIMK_`)

**S3-01** Relevé de température : « Tu relèves tes frigos depuis ton téléphone. La mesure est datée, signée, archivée. Un contrôle, et tu sors trois mois d'historique en un clic. »
**S3-02** Équipements : « Chaque frigo, chaque chambre froide est déclaré avec ses seuils. Hors zone, tu es alerté. Tu sauves la marchandise avant de la jeter. »
**S3-03** Étiquettes DLC : « Étiquette produite, date de fabrication, DLC calculée. Ton bac étiqueté n'est plus un pari. »
**S3-04** Traçabilité : « Chaque lot reçu est rattaché à ce que tu produis. En cas de rappel, tu remontes la chaîne en quelques secondes. »
**S3-05** Réception fournisseur : « Contrôle à réception : température, aspect, quantité, non-conformités. Tout part dans le dossier HACCP tout seul. »
**S3-06** Plan de nettoyage : « Tes zones et tes postes de nettoyage sont listés. Qui a fait quoi, quand, c'est enregistré. Le plan de nettoyage vit vraiment. »
**S3-07** Checklists hygiène : « Tu crées ta checklist une fois, l'équipe la valide chaque jour. Ce qui est coché est daté et signé. »
**S3-08** Historique : « Tes relevés, tes réceptions et tes validations sont conservés. Le jour du contrôle, tu ne cherches rien. »
**S3-09** Alertes : « Une température hors seuil déclenche une alerte immédiate. Tu réagis pendant le service, pas le lendemain. »
**S3-10** Rôles : « Chaque agent signe ses propres relevés. La responsabilité est claire, sans paperasse supplémentaire. »
**S3-11** Non-conformité : « Tu déclares une non-conformité, tu notes l'action corrective. C'est exactement ce qu'on te demandera de prouver. »
**S3-12** Congélation : « Tu enregistres une mise en congélation avec sa date et sa quantité. Plus de sac sans nom au fond du bac. »
**S3-13** Rapport HACCP : « Tu édites ton dossier de conformité sur la période de ton choix, prêt à présenter. »
**S3-14** Routine du jour : « La conformité devient une routine de deux minutes par service, au lieu d'un dimanche de rattrapage. »

### Équipe & Planning (10 scripts — module `1wboT7bVjEwxbhpU9Xgz8sRjjqn9XEd7X`)

**S3-15** Créer un employé : « Tu crées ta fiche employé avec son rôle et ses horaires. Elle alimente le planning, les pointages et la paie. »
**S3-16** Planning semaine : « Le planning se construit en glisser-déposer, avec le coût de la semaine qui s'affiche pendant que tu poses les shifts. »
**S3-17** Pointages : « Les heures réelles sont pointées. Tu compares le prévu et le réalisé, sans discussion de fin de mois. »
**S3-18** Congés : « Une demande de congé arrive, tu valides ou tu refuses depuis l'écran. Le planning se met à jour tout seul. »
**S3-19** Contrats : « Contrats et documents employés sont rangés au même endroit, avec leurs échéances. »
**S3-20** Coût du travail : « Ton coût de personnel s'affiche en face de ton chiffre d'affaires prévu. Tu ajustes avant, pas après. »
**S3-21** Recrutement : « Tu publies ton offre, tu suis les candidatures par statut, tu décides. Le recrutement arrête de traîner sur ton téléphone. »
**S3-22** Onboarding : « Le nouveau arrive avec son accès, son planning et ses vidéos de formation. Jour un, il est utile. »
**S3-23** Multi-postes : « Tu affectes tes équipes par poste et par zone. Chacun sait où il est attendu ce soir. »
**S3-24** Absences : « Une absence, et tu vois immédiatement quel service est découvert. Tu remplaces avant l'ouverture. »

### Configuration (8 scripts — module `19xTrrkXtWO3yfJqtC3SIlDgpBjSEc4N9`)

**S3-25** Établissement : « Tu paramètres ton établissement une fois : horaires, coordonnées, TVA. Tout FoodEatUp s'appuie dessus. »
**S3-26** Catégories : « Tes catégories de produits, d'ingrédients et de recettes structurent tout le reste. Cinq minutes qui t'en font gagner cent. »
**S3-27** TVA : « Tes taux de TVA sont posés une fois, appliqués partout : caisse, factures, comptabilité. »
**S3-28** Zones et tables : « Tu dessines ta salle : zones, tables, capacités. Ton plan de salle devient vivant pendant le service. »
**S3-29** Équipements : « Tu déclares tes équipements et leurs seuils. Ils remontent ensuite dans ton suivi HACCP. »
**S3-30** Utilisateurs : « Chaque membre de l'équipe a son accès et ses droits. Tout le monde ne voit pas la compta. »
**S3-31** Import de carte : « Tu importes ta carte entière en un appel : catégories, sous-catégories, plats, prix. »
**S3-32** Abonnement : « Tu vois ton plan, tes options actives et ce que tu consommes. Aucune ligne surprise en fin de mois. »

### Comptabilité (6 scripts — module `1KlXihMLILGDrlxDuO2d3VCe1ic-kCAw_`)

**S3-33** Factures : « Chaque commande produit sa facture, numérotée et conforme. Tu ne la ressaisis nulle part. »
**S3-34** Devis : « Un devis pour un groupe se crée en deux minutes et se transforme en commande quand il est accepté. »
**S3-35** Impayés : « Tu vois ce qui est facturé, encaissé, et ce qui traîne. Les relances arrêtent d'être un jeu de mémoire. »
**S3-36** Dépenses : « Tu photographies la facture fournisseur, elle rentre dans tes dépenses avec ses lignes et son montant. »
**S3-37** Synthèse : « Chiffre d'affaires, dépenses, impayés, marge : la synthèse du mois tient sur un écran. »
**S3-38** Export comptable : « Tu envoies à ton comptable un export propre. Le dimanche soir redevient un dimanche soir. »

### Mon Site (4 scripts — module `1ykcHl2BaY22WlCsBA3DuwXaEMvQZUtMF`)

**S3-39** Éditeur : « Tu actives l'éditeur, tu choisis ton template, ton site est en ligne le jour même, aux couleurs de ta maison. »
**S3-40** Pages : « Tu ajoutes tes pages : carte, avis, allergènes, recrutement. Elles se publient quand tu le décides. »
**S3-41** Domaine : « Tu branches ton nom de domaine. Tes clients arrivent chez toi, pas sur une plateforme. »
**S3-42** Leads du site : « Chaque demande de privatisation ou de contact devient un lead dans ton fichier client. »

---

## 6. Saison 4 — EP91 → EP120

**EP91** · Réservation › 2 - Ajouter une réservation
> « L'anniversaire est noté à la réservation, avec le nombre de couverts et la demande spéciale. La cuisine et la salle le savent avant que le client arrive. »

**EP92** · Réservation › 3 - Gérer et no-shows
> « Quatre-vingts personnes d'un coup, ça se voit venir. Tu ouvres ou tu fermes tes créneaux en direct, et la liste d'attente prend le relais. »

**EP93** · StockVision › 3 - Prédictions des commandes
> « FoodEatUp prévoit tes ventes de poisson à partir de ton historique. Tu commandes la bonne quantité le mardi, pas la canne à pêche le samedi. »

**EP94** · HubRise › 4 - Centraliser les commandes
> « Peu importe qui livre. Tes commandes arrivent dans la même file, avec la bonne adresse et le bon statut, jusqu'à la remise au client. »

**EP95** · KDS › 3 - Gérer le KDS en direct
> « Sur le KDS, chaque plat a son chrono. Tu vois ce qui traîne au moment où ça traîne, et tu relances le bon poste. »

**EP96** · HACCP › relevé de température
> « Trente-neuf degrés en cuisine, ton frigo souffre. Le relevé hors seuil te prévient tout de suite. Tu sauves la marchandise. »

**EP97** · HubRise › 2 - Relier Uber Eats et Deliveroo
> « Tes plateformes envoient tout dans FoodEatUp. Six alertes deviennent une file de commandes. La tablette murale, tu peux la ranger. »

**EP98** · Service › 1 - Commandes multi-canaux
> « L'intelligence utile, c'est celle qui range tes commandes, pas celle qui danse. Ici, chaque canal alimente le même service. »

**EP99** · Caroline › 1 - Configurer voix et prompts
> « Caroline répond au téléphone pendant ton rush. Elle prend la réservation, la note, et te la remonte. Aucun appel ne tombe dans le vide. »

**EP100** · Marketing › 1 - Débloquer les avis
> « Tes avis remontent au même endroit, site et Google. Tu réponds à celui qui t'a mis deux étoiles avant qu'il devienne ta vitrine. »

**EP101** · Caisse POS › 6 - Clôturer sa caisse
> « La clôture, c'est un bouton. Le détail par moyen de paiement, la TVA, l'écart : tout est là, sans calculatrice ni suspense. »

**EP102** · HACCP › checklists hygiène
> « Ta checklist est validée chaque jour par ton équipe. Le jour du vrai contrôle, tu ouvres l'historique et tu ne bouges pas. »

**EP103** · Réservation › 1 - Réservations du jour
> « Un groupe qui arrive, tu vérifies la disponibilité réelle en trois secondes : tables libres, horaires, capacité. Tu dis oui en connaissance de cause. »

**EP104** · Réservation › 3 - Gérer et no-shows
> « Tu marques le no-show, la table se libère immédiatement et repart à la vente. Le client, lui, garde son historique. »

**EP105** · Mon Site › 6 - Réservations et horaires
> « Tes créneaux sont réservables en ligne, en direct, avec tes vraies disponibilités. Le premier qui réserve a la table. »

**EP106** · Caisse POS › 5 - Séparer une addition
> « Quatorze parts, quatorze cartes : tu découpes l'addition depuis l'écran, chacun paie ce qu'il doit, le reste dû s'affiche en direct. »

**EP107** · Caisse POS › 3 - Encaisser une commande
> « L'addition est rattachée à la table dès la commande. Elle ne se perd pas, elle ne s'oublie pas, elle ne disparaît pas. »

**EP108** · KDS › 2 - Vue KDS par poste
> « Chaque poste voit ce qui le concerne, et seulement ça. Tu n'as pas besoin de six bras, tu as besoin de six écrans qui parlent entre eux. »

**EP109** · HACCP › traçabilité
> « Chaque production est datée, tracée, rattachée à son lot. Ce qui fermente en cave n'est plus une surprise. »

**EP110** · StockVision › 18 - Statistiques par module
> « La tendance, tu la testes. Tu regardes ce que ce plat rapporte vraiment, et tu décides de le garder ou pas sur des chiffres. »

**EP111** · StockVision › 12 - Valider une production
> « La production planifiée sort ses ingrédients du stock, sa quantité est validée, sa traçabilité écrite. Le gain de temps est là, pas dans le gadget. »

**EP112** · Mon Site › 2 - Choisir ton template
> « Ta carte en ligne, propre, à jour, consultable par QR à table. Pas de casque, pas d'appli à installer. »

**EP113** · HubRise › 4 - Centraliser les commandes
> « Le suivi de commande affiche l'état en direct, de la prise à la remise. Tu sais toujours où est la commande et chez qui. »

**EP114** · Marketing › 5 - Lancer une campagne
> « Ce que ton équipe filme, tu peux l'exploiter : campagne, segment, envoi, résultats. Publier, oui — mesurer, encore mieux. »

**EP115** · StockVision › 16 - Mouvements de stock
> « Ce qui rentre, ce qui sort, ce qui se perd. Circuit court ou pas, la quantité doit être comptée. »

**EP116** · KDS › 1 - Créer tes postes KDS
> « Tes commandes tiennent sur un écran, pas sur un mur. Chaque poste voit les siennes, dans l'ordre, avec son temps. »

**EP117** · StockVision › 1 - Ma carte, fiche recette
> « La fiche technique fixe les quantités, les étapes et le coût. Le plat sort en dix minutes, tous les jours, par n'importe qui de ta brigade. »

**EP118** · Mon Site › 5 - Créer un site par IA
> « Ton site de réservation et de commande est prêt en un clic, depuis ta carte. La file d'attente devient un carnet plein. »

**EP119** · Marketing › 9 - Ciblage et consentement
> « Cinq cents tracts, zéro donnée. Ici, chaque client capté entre dans ton fichier, avec son consentement, et devient une campagne. »

**EP120** · PrediBot › 1 - Lire ses prévisions
> « Une base, un écran, une équipe. Ta caisse, ta cuisine, ton stock et ton marketing lisent les mêmes données. Ils finissent enfin par se parler. »

---

## 7. Saison 5 — EP121 → EP150

**EP121** · Service › 3 - Envoi direct cuisine
> « Les modifications se saisissent sur la commande : sans oignon, cuisson, allergie. Elles partent en cuisine avec le plat, écrites noir sur blanc. »

**EP122** · Marketing › 20 - Vue client fidélité
> « La fiche client te dit qui il est, ce qu'il commande et quand il est venu la dernière fois. « Comme d'habitude » devient une information, pas un bluff. »

**EP123** · StockVision › 1 - Ma carte, allergènes
> « Les allergènes et les régimes sont portés par ta carte et par la réservation. L'info arrive en cuisine avant l'entrée, pas au dessert. »

**EP124** · Caisse POS › 6 - Clôturer sa caisse
> « Le service a une fin : tu clôtures, tu comptes, tu archives. L'écran te dit quand la journée est vraiment finie. »

**EP125** · Caroline › 3 - Dessiner son plan de salle
> « Ton plan de salle est le tien : zones, tables, capacités, blocages. Tu places, tu bloques, tu libères en un geste. »

**EP126** · Caisse POS › 5 - Séparer une addition
> « Tu partages l'addition par article ou par personne. Ce qui reste dû s'affiche en direct. Personne ne recompte à la main. »

**EP127** · Réservation › 1 - Réservations du jour
> « Deux cents couverts un 31 décembre, ça se pilote : arrivées échelonnées, tables assignées, cuisine prévenue. La soirée reste une fête. »

**EP128** · Réservation › 4 - Placer un client à table
> « Tu places tes clients selon la vraie capacité de ta salle. Serrer, ça se décide — ça ne se subit pas un soir de Saint-Valentin. »

**EP129** · Caroline › 4 - Gérer ses tables
> « Tu ouvres ta terrasse dans le logiciel : tables ajoutées, capacité mise à jour, réservations ouvertes dessus. Le premier rayon de soleil est rentable. »

**EP130** · Marketing › 7 - Ton agenda marketing
> « Ton agenda marketing connaît les temps forts de ton quartier. Tu prépares l'événement avant qu'il soit devant ta porte. »

**EP131** · Équipe & Planning › planning de la semaine
> « Tu construis la semaine de rentrée en amont : shifts posés, congés validés, coût affiché. Le premier septembre, tu n'es pas seul en cuisine. »

**EP132** · Mon Site › 6 - Réservations et horaires
> « Tes horaires d'ouverture sont à jour partout : site, réservation, Google. Quand tout le quartier ferme, on te trouve. »

**EP133** · Caisse POS › 3 - Encaisser une commande
> « Trois tournées en une minute : tu encaisses au comptoir ou à table, TPE relié, ticket envoyé. Ta caisse tient le rythme du match. »

**EP134** · HACCP › relevé de température
> « L'huile et les frigos ont leurs seuils. Le relevé se fait en dix secondes, il est daté et gardé. Ta friteuse aussi a une conformité. »

**EP135** · Réservation › 1 - Réservations du jour
> « Tes réservations du soir sont ici, pas sur un carnet taché de café : contact, couverts, table, historique. Rien ne s'efface. »

**EP136** · Service › 1 - Commandes multi-canaux
> « Le service, c'est cent gestes invisibles. FoodEatUp en enregistre la trace pour que tu saches où part vraiment ton temps. »

**EP137** · Caisse POS › 3 - Encaisser une commande
> « Deux cent quarante cafés, deux cent quarante lignes encaissées. Tu compares le vendu et l'encaissé, à l'unité près. »

**EP138** · KDS › 3 - Gérer le KDS en direct
> « De l'envoi au pass, chaque plat a son statut et son chrono. Tu comptes tes assiettes, tu ne les devines pas. »

**EP139** · KDS › 2 - Vue KDS par poste
> « Pendant le coup de feu, tu vois la charge de chaque poste. Tu envoies où il y a de la place. Être équipé, c'est ça. »

**EP140** · StockVision › 16 - Mouvements de stock
> « L'inventaire est daté, signé, comparé au théorique. Ce qui disparaît la nuit finit toujours par apparaître dans l'écart. »

**EP141** · PrediBot › 3 - Parler à PrediBot
> « Tu demandes, PrediBot répond avec tes vraies données : la table en attente, la production à lancer, l'alerte à traiter. Le pilote automatique existe. »

**EP142** · Équipe & Planning › affectation des postes
> « Les postes sont répartis avant le service, pas pendant. Chacun sait ce qu'il envoie, personne ne dégaine sa spatule pour le savoir. »

**EP143** · Comptabilité › devis
> « Deux cents parts, ça commence par un devis : quantités, prix, marge. Il se transforme en commande, puis en facture, sans ressaisie. »

**EP144** · Marketing › 3 - Répondre aux avis
> « Un avis une étoile, tu le vois tout de suite et tu réponds depuis l'outil. Une réponse rapide vaut mieux qu'un long procès. »

**EP145** · PrediBot › 1 - Lire ses prévisions
> « Ton point du jour en un écran : ce qui arrive, ce qui manque, ce qui coince. L'espèce « gérant épuisé » n'est pas obligée de survivre comme ça. »

**EP146** · Comptabilité › événements privés
> « Un événement, c'est une demande, un devis, une réservation et une facture. Enchaînés. Rien ne se prépare la veille au soir. »

**EP147** · Comptabilité › facture et devis
> « Douze mille euros de prestation ne tiennent pas sur un post-it. Devis signé, acompte suivi, facture éditée : tout est dans le dossier. »

**EP148** · HubRise › 3 - Synchro caisse tierce
> « Trois plateformes, une seule file. Les commandes arrivent centralisées, avec leur horaire de retrait. Tes livreurs ne se croisent plus au même moment. »

**EP149** · Marketing › 5 - Lancer une campagne
> « Ta salle a quelque chose d'unique : fais-le savoir. Campagne créée, segment choisi, résultats mesurés, CA attribué. »

**EP150** · PrediBot › 1 - Lire ses prévisions
> « Cent cinquante épisodes pour dire une chose : ton restaurant tient dans un seul outil, avant, pendant et après ton service. Le reste, c'est du bruit. »

---

## 8. `content/heygen-scripts.json` — format attendu

```json
{
  "id": "HG007",
  "episode": "EP007",
  "module": "marketing",
  "chapitre": "3 - RÉPONDRE AUX AVIS",
  "drive_folder_id": "1ZXZeT7GyPTkQT95XNGu8svx6OI1aUgNA",
  "script": "Tes avis Google remontent ici. Tu réponds depuis FoodEatUp, l'IA te propose une réponse dans ton ton, tu valides. Le client voit que tu l'as lu.",
  "mots": 28,
  "duree_cible_s": 10,
  "variante_longue": null,
  "fichier_attendu": "assets/avatar/EP007.mp4"
}
```

Claude Code lit ce fichier pour vérifier que chaque `fichier_attendu` existe avant de lancer un build, et pour rapprocher le screencast du bon chapitre Drive.

---

## 9. Ordre de production conseillé pour les 150 rendus HeyGen

Tu vas rendre 150 segments. Regroupe-les **par chapitre Drive**, pas par numéro d'épisode : tu enchaînes les scripts qui parlent du même écran, tu gardes le même réglage, et tu vas trois fois plus vite.

1. Les 12 chapitres les plus utilisés (Réservation, Caisse, KDS, Service, StockVision, PrediBot) — ils couvrent environ 90 épisodes.
2. Puis Marketing, Mon Site, HubRise, Caroline.
3. Puis HACCP, Équipe, Configuration, Comptabilité — c'est là que tombera l'essentiel de la saison 3 une fois le mapping figé.
4. EP150 en dernier.
