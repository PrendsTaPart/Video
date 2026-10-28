# Scripts des épisodes 40 à 45 (à valider)

Règles communes : les chiffres d'exemple sont signalés à l'écran, aucun numéro de téléphone n'apparaît à l'écran, chaque vidéo finit par un CTA « Commente MOT », et rien n'est publié sans validation.

## Ép. 40 : « Ton concurrent a déjà Caroline » (thème rue-de-nuit)
Kit Lovable : rue-de-nuit-*, commun-patron-*, commun-caroline-*, commun-horloge-digitale, commun-carte-notification.
- PATRON : « Mon concurrent me pique tous mes clients. »
- CAROLINE (dans la vitrine d'en face) : « Je sais. C'est moi qui l'aide. »
- PATRON : « Tu bosses pour lui ? »
- CAROLINE : « Ses clients appellent à 22 h. Je décroche. »
- PATRON : « Et ses réservations ? »
- CAROLINE : « Je les pose sur son plan de salle. Que des vraies tables libres. »
- PATRON : « Et quand c'est complet ? »
- CAROLINE : « Liste d'attente. Et je rappelle pour confirmer. »
- PATRON : « Et moi, je fais comment ? »
- CAROLINE : « Ce soir, je bosse pour toi. Et demain, c'est toi qu'on appelle en premier. »
- CTA : « Commente ÉQUIPE, je te présente toute l'équipe IA de FoodEatUp. »

## Ép. 41 : « Six agents construisent ton extension » (thème theatre-voxel)
Faits vérifiés dans la fiche marketplace braindcode-build v0.1.0 :
- 6 agents ;
- 22 skills ;
- 17 commandes ;
- 8 hooks, dont garde-credits-lovable et anti-secret.

Script :
- « Quelqu'un a monté une équipe de six agents Claude qui construisent ton extension de bout en bout. »
- « Le chef de projet découpe le chantier. Le designer pose la charte et les maquettes Figma. »
- « Le bâtisseur construit l'app dans Lovable, étape par étape, et annonce chaque crédit dépensé. »
- « L'intégrateur branche le MCP côté serveur et vérifie qu'aucun secret ne part au navigateur. »
- « Le testeur casse tout : jeton expiré, outil absent, entrée invalide. Rapport obligatoire. »
- « Et le publicateur ne met rien en ligne sans ton accord. »
- « Vingt-deux skills, dix-sept commandes. Ça s'appelle BraindCode Build. »
- CTA : « Commente BUILD, je t'envoie les deux lignes pour l'installer dans Claude Code. »

## Ép. 42 : « La caisse du mois d'une pizzeria » (thème caisse-pizzeria)
Un compteur « Ta caisse du mois » fond poste par poste, et chaque poste renvoie au module FoodEatUp qui le maîtrise. Les montants restent à valider : aucun chiffre n'est présenté comme réel.
- Accroche : « 20 000 € par mois. Ce qui te reste ? Écris ton chiffre en commentaire. »
- TVA : la comptabilité.
- Ingrédients : les fiches techniques.
- Pertes : le stock et l'HACCP.
- Équipe : le planning.
- Appels ratés : Caroline.
- Clients perdus : la fidélité.
- Conclusion : « Huit boucles, un seul logiciel. »
- CTA : « Commente CAISSE, je t'envoie le diagnostic des 8 boucles. »

## Ép. 43 : « Tu viens de devenir patron d'une agence IA » (thème ville-pixel)
- Plan'It (planit.braindcode.com/mcp) orchestre les serveurs MCP, les routines et les KPI.
- Le plugin BraindCode s'installe dans Claude Code et construit de nouvelles « boutiques ».
- CTA : « Commente AGENCE, je t'envoie le lien. »

## Ép. 44 : « Toi, tu répares. Caroline décroche. » (thème atelier-artisans)
Secteurs proposés : pizzeria (commandes), artisan du bâtiment (urgences, devis), boulangerie (gâteaux d'anniversaire), réparation de matériel (rendez-vous), traiteur (événements).
⚠️ À confirmer : Caroline est-elle proposée hors restauration, et via quel produit ?
- Chute : « Trois clients pendant que j'avais la tête dans la chaudière ?! » / « Toi, tu répares. Moi, je décroche. »
- CTA : « Commente CAROLINE, je t'installe la même. »

## Ép. 45 : « Le symbole € qui fait dépenser » (thème editorial-mentaliste)
Accroche : l'étude de Cornell (2009) sur l'affichage des prix des menus.
Enchaînement sur trois produits :
- la carte digitale ;
- le menu digital ;
- les affiches display de FoodEatUp.

À vérifier avant tournage : que le format d'affichage des prix soit bien réglable dans le logiciel.

CTA : « Commente MENU, je t'envoie le tuto. »

## Ép. 46 : « Lui n'a pas l'IA, l'autre l'a installée » (thème iso-duel-nuit)
Référence : deux cafés en écran partagé, vue isométrique de nuit (guerre des prix).
Écran du haut : resto A, sans IA. Écran du bas : resto B, avec FoodEatUp. Même rue, même soir.
- « Deux restos, même rue, même carte, même prix. »
- 19 h 30, le téléphone sonne chez les deux. Haut : personne ne décroche. Bas : Caroline décroche, table réservée.
- Rush : en haut, une commande est ressaisie à la main et le ticket se perd ; en bas, la commande part directement en cuisine.
- Le steak augmente : en haut, personne ne le voit ; en bas, la fiche technique recalcule la marge.
- Lendemain : en haut, les clients ne reviennent pas ; en bas, une campagne fidélité part toute seule.
- Le prix se copie en une nuit. L'organisation, non.
- CTA : « Commente IA, je te montre ce que j'ai installé chez lui. »

## Ép. 47 : « Ne fais jamais partir ton client de zéro » (thème editorial-mentaliste, réutilisé)
Référence : la série Mentaliste, style éditorial (étude de la carte de lavage).
Étude réelle : Nunes et Drèze, 2006, « effet de progression dotée ». 300 cartes de lavage sont distribuées. La carte A demande 8 tampons. La carte B en demande 10, mais 2 sont déjà offerts. Neuf mois plus tard, 19 % des cartes A sont complétées, contre 34 % des cartes B.
Fonctions FoodEatUp vérifiées dans les tutoriels :
- points par euro, par passage ou hybride ;
- multiplicateurs sur les créneaux creux ;
- catalogue de récompenses (produit, bon €, avantage) ;
- espace client avec le solde de points et une barre de progression vers la prochaine récompense ;
- conseil officiel : une première récompense à très bas coût, par exemple un café à 2 points, pour une victoire rapide.

Script :
- « Une station de lavage a distribué 300 cartes de fidélité. Même offre, deux designs. »
- « Carte A : 8 tampons, puis un lavage gratuit. Carte B : 10 tampons, mais les deux premiers sont déjà remplis. »
- « Neuf mois plus tard : 19 % des cartes A complétées. Carte B : 34 %. Presque le double. »
- « Mais pourquoi ? Les deux demandaient exactement 8 lavages. Mais la carte B ne part pas de zéro. »
- « Plus on se sent proche du but, plus on s'active. Tu ne commences pas une tâche : tu en termines une. »
- « Dans FoodEatUp, c'est exactement ce que tu règles. Ton client voit sa barre de progression vers la prochaine récompense dès sa première commande. »
- « Ta première récompense ne coûte presque rien : un café à 2 points. Victoire rapide, il revient. »
- « Et tes points doublés le mardi midi remplissent tes heures creuses. »
- « Alors ne fais jamais partir ton client de zéro. »
- CTA : « Commente FIDÉLITÉ, je t'envoie le tuto pour configurer ton programme. »

Visuels :
- Kit editorial-mentaliste : fonds papier, noir et rouge, histogramme, point d'interrogation, carte bancaire mascotte, barre de progression, carte de fin.
- Cartes à tampons A et B dessinées en HTML.
- Vrais écrans des tutoriels « Booster la fidélité — le programme » et « Vue publique fidélité — côté client ».
