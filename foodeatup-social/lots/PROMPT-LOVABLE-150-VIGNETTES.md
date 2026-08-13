# Prompt Lovable — les 150 vignettes d'épisode

Un seul tour pour toute la série. À coller dans Lovable **avec la photo du chef
en pièce jointe**.

---

## Le message

L'image jointe est la photo officielle du chef FoodEatUp. Elle est aussi ici :
https://raw.githubusercontent.com/PrendsTaPart/Video/claude/foodeatup-video-factory-wtb7gs/foodeatup-social/public/brand/chef-foodeatup.jpg

Le site affiche aujourd'hui **un écran noir** à la place de la vignette sur la
plupart des épisodes : `posterUrl` est vide et le fichier de repli
`/thumbnails/episodes/EPxxx-9x16.jpg` n'existe pas. Génère les **150 vignettes**
listées plus bas, une par épisode, et fais pointer chaque `posterUrl` dessus.

**Les 150, pas seulement les épisodes sortis.** Un épisode non encore tourné a
déjà son gag écrit, son décor de saison et son titre de vignette : il a donc une
image à montrer. Le site marque l'attente autrement — la pastille de statut le
dit déjà, en CSS. Une grille où deux tiers des cases sont noires ne donne envie
de rien.

### Ce que tu changes dans le projet, et rien d'autre

1. Chaque image dans `public/vignettes/EPxxx.jpg`, format 9:16, 1080 × 1920.
2. Le seul champ `posterUrl` des 150 épisodes dans `src/data/series.ts`.

**Ne touche à aucun autre champ de `src/data/series.ts` ni à `src/data/contenu.ts`.**
Ces deux fichiers sont générés par l'usine à vidéos et poussés depuis le dépôt :
`statut`, `videoUrl`, `masterRapidoUrl`, `higgsfield.videoSourceUrl`,
`dureeSecondes` et les publications y sont déjà à jour. Une régénération de ta
part les écraserait, et la prochaine mise à jour de l'usine écraserait la tienne.

### Le chef ne se redessine pas

Même visage, même barbe, même toque blanche, même veste blanche, même tablier au
logo FoodEatUp bleu. C'est **la même personne sur les 150 épisodes** — c'est ce
qui fait une série plutôt qu'une collection d'images. Si une image sort avec un
autre visage, une autre morphologie ou un autre costume, refais-la plutôt que de
l'accepter.

### Trois défauts du premier jet, à ne pas reproduire

1. **Le grisé ne se cuit pas dans le fichier.** Les épisodes non sortis étaient
   désaturés dans le JPEG lui-même : le jour de la publication, la vignette
   restait grise pour toujours. Le grisé est un état d'affichage, le site le pose
   déjà en CSS. Génère **toutes** les images en couleur, sans exception — y
   compris celles des épisodes à venir.

2. **Un seul logo.** Le tablier du chef porte déjà le logo FoodEatUp. N'ajoute
   aucun second badge, ni en bas à droite ni ailleurs, et surtout pas un logo
   redessiné. Deux marques sur la même image, dont une fausse, c'était le défaut
   le plus visible.

3. **Chaque épisode a sa scène.** Les 300 premières images réutilisaient le même
   décor et la même pose ; seul le texte du bandeau changeait. Chaque bloc
   ci-dessous décrit un gag précis. Si deux épisodes sortent avec la même image,
   c'est que le bloc n'a pas été lu.

### Le gabarit, identique sur les 150

> Photo réaliste, cadrage vertical 9:16. Le chef de l'image de référence — MÊME
> visage, même barbe, même toque blanche, même veste de cuisine blanche, même
> tablier blanc au logo FoodEatUp bleu. Ne change ni ses traits ni sa
> morphologie. Son expression : **{EXPRESSION}**. Scène : **{SCÈNE}**. Décor :
> **{DÉCOR}**. Le chef occupe les deux tiers droits du cadre, en plan poitrine ;
> l'élément comique est visible à gauche. Bande crème #FCF9E6 en haut du cadre
> sur un cinquième de la hauteur, portant UNIQUEMENT le texte **« {TEXTE} »** en
> typographie arrondie très grasse, bleu marine #0F1A23, centré. Aucun autre
> texte, aucun logo ajouté, pas de filigrane, pas de bordure décorative.

### Les cinq décors, un par saison

- **SALLE** (saison 1) — une salle de restaurant en plein service, tables
  dressées, clients flous en arrière-plan ; lumière chaude de fin de journée,
  reflets dorés.
- **BUREAU** (saison 2) — un bureau d'arrière-salle, classeurs, tickets de
  caisse, calculatrice, cartons de livraison ; lumière rasante de néon adouci,
  ambiance fin de mois.
- **CUISINE** (saison 3) — une cuisine professionnelle en pleine brigade, inox,
  passe-plat, plannings punaisés au mur ; lumière blanche et nette, vapeur
  légère.
- **DEVANTURE** (saison 4) — la devanture et la terrasse du restaurant, ardoise,
  téléphone à la main, avis clients affichés ; plein jour, lumière franche.
- **AUBE** (saison 5) — le restaurant vide au petit matin, chaises encore sur les
  tables, tablette posée sur le comptoir ; lumière bleutée d'avant-service.

Le décor tient la saison ensemble à l'œil ; le gag change à chaque épisode.

La mention **SORTI** marque les 51 épisodes déjà montés et publiés. Elle ne change
rien à la fabrication de l'image — elle est là pour que tu commences par ceux-là
si tu dois t'arrêter en route.

---

## Les 150 épisodes

**EP001** · S1 · décor SALLE · texte « COMMANDES MULTI-CANAUX » · SORTI
Expression : faussement dépité, la main sur le front, mais l'œil qui rit.
Scène : le chien qui te regarde. Lui aussi attend ta commande.

**EP002** · S1 · décor SALLE · texte « ENVOI DIRECT CUISINE » · SORTI
Expression : l'air satisfait de celui qui sait que le problème est déjà réglé.
Scène : la chute en skateboard. Ton service du samedi soir.

**EP003** · S1 · décor SALLE · texte « MA CARTE » · SORTI
Expression : l'air de quelqu'un qui a déjà vu ça cent fois, un sourcil levé.
Scène : le plat dans la piscine. Ta marge, en ce moment.

**EP004** · S1 · décor SALLE · texte « CONFIGURER SA CAISSE »
Expression : un sourire en coin, parfaitement serein au milieu du désastre.
Scène : le chat sur la caisse. Ton nouveau responsable de caisse.

**EP005** · S1 · décor SALLE · texte « VUE D'ENSEMBLE » · SORTI
Expression : faussement dépité, la main sur le front, mais l'œil qui rit.
Scène : le serveur qui glisse. Trois logiciels. Deux mains.

**EP006** · S1 · décor SALLE · texte « AJOUTER MODIFIER MOUVEMENT » · SORTI
Expression : l'air satisfait de celui qui sait que le problème est déjà réglé.
Scène : la pizza frisbee. Ta pizza part plus vite que ton stock.

**EP007** · S1 · décor SALLE · texte « RÉPONDRE AUX AVIS » · SORTI
Expression : l'air de quelqu'un qui a déjà vu ça cent fois, un sourcil levé.
Scène : la mamie qui goûte. Le seul avis client qui compte.

**EP008** · S1 · décor SALLE · texte « FACTURATION »
Expression : un sourire en coin, parfaitement serein au milieu du désastre.
Scène : la pile de tickets. Fin de mois. Encore.

**EP009** · S1 · décor SALLE · texte « SUIVRE ÉCARTS CAISSE »
Expression : faussement dépité, la main sur le front, mais l'œil qui rit.
Scène : le pigeon voleur. Il y a toujours quelqu'un qui prend ta marge.

**EP010** · S1 · décor SALLE · texte « LIRE SES PRÉVISIONS » · SORTI
Expression : faussement dépité, la main sur le front, mais l'œil qui rit.
Scène : le flambage raté. Toi, devant ta facture logicielle.

**EP011** · S1 · décor SALLE · texte « CONNECTER SON HUBRISE »
Expression : l'air satisfait de celui qui sait que le problème est déjà réglé.
Scène : le livreur et le dos d'âne. Ta livraison sans intégration.

**EP012** · S1 · décor SALLE · texte « GÉRER KDS DIRECT »
Expression : l'air de quelqu'un qui a déjà vu ça cent fois, un sourcil levé.
Scène : le client qui attend. Temps d'attente : « on regarde ».

**EP013** · S1 · décor SALLE · texte « PARLER À PREDIBOT » · SORTI
Expression : un sourire en coin, parfaitement serein au milieu du désastre.
Scène : l'avalanche de notifications. Dix logiciels. Dix notifications.

**EP014** · S1 · décor SALLE · texte « MOUVEMENTS DE STOCK » · SORTI
Expression : faussement dépité, la main sur le front, mais l'œil qui rit.
Scène : le raton laveur. Ton gaspillage alimentaire.

**EP015** · S1 · décor SALLE · texte « RÉFÉRENTIELS » · SORTI
Expression : l'air satisfait de celui qui sait que le problème est déjà réglé.
Scène : la tour d'assiettes. Ta gestion actuelle.

**EP016** · S1 · décor SALLE · texte « DÉPENSES » · SORTI
Expression : l'air de quelqu'un qui a déjà vu ça cent fois, un sourcil levé.
Scène : le geyser à café. Tes coûts, ce trimestre.

**EP017** · S1 · décor SALLE · texte « CRÉATION D'UN RAPPORT » · SORTI
Expression : un sourire en coin, parfaitement serein au milieu du désastre.
Scène : le ninja de la frite. Personne ne touche à ta dernière frite.

**EP018** · S1 · décor SALLE · texte « SITE » · SORTI
Expression : faussement dépité, la main sur le front, mais l'œil qui rit.
Scène : le serveur baywatch. Le rush de vingt heures.

**EP019** · S1 · décor SALLE · texte « PRÉDICTIONS DES COMMANDES » · SORTI
Expression : l'air satisfait de celui qui sait que le problème est déjà réglé.
Scène : le burger qui rebondit. Ton chiffre d'affaires, sans outil.

**EP020** · S1 · décor SALLE · texte « AJOUTER UNE RÉSERVATION » · SORTI
Expression : l'air satisfait de celui qui sait que le problème est déjà réglé.
Scène : le chien qui a réservé. Lui, il a réservé.

**EP021** · S1 · décor SALLE · texte « CRÉER TES POSTES » · SORTI
Expression : l'air de quelqu'un qui a déjà vu ça cent fois, un sourcil levé.
Scène : chef contre imprimante. Le vrai ennemi du service.

**EP022** · S1 · décor SALLE · texte « MARKETPLACE DE PROMPTS » · SORTI
Expression : un sourire en coin, parfaitement serein au milieu du désastre.
Scène : la facture qui fait pleurer. Mille euros par mois.

**EP023** · S1 · décor SALLE · texte « CALENDRIER IA AVEC » · SORTI
Expression : faussement dépité, la main sur le front, mais l'œil qui rit.
Scène : l'aspirateur robot. Ton automatisation actuelle.

**EP024** · S1 · décor SALLE · texte « CRÉER SITE PAR » · SORTI
Expression : l'air satisfait de celui qui sait que le problème est déjà réglé.
Scène : la mouette braqueuse. Encore une commission en moins.

**EP025** · S1 · décor SALLE · texte « CAMPAGNE 100 % » · SORTI
Expression : l'air de quelqu'un qui a déjà vu ça cent fois, un sourcil levé.
Scène : le mixeur sans couvercle. Quand tu lances une promo sans données.

**EP026** · S1 · décor SALLE · texte « ENVOYER LISTE COURSES » · SORTI
Expression : un sourire en coin, parfaitement serein au milieu du désastre.
Scène : le ballon qui explose. Ton stock avant le week-end.

**EP027** · S1 · décor SALLE · texte « CLÔTURER SA CAISSE »
Expression : faussement dépité, la main sur le front, mais l'œil qui rit.
Scène : le chat et le verre. Ta trésorerie, chaque lundi.

**EP028** · S1 · décor SALLE · texte « CENTRALISER LES COMMANDES »
Expression : l'air satisfait de celui qui sait que le problème est déjà réglé.
Scène : le tapis à sushis fou. Tes commandes en ligne, un vendredi.

**EP029** · S1 · décor SALLE · texte « LIRE SES PRÉVISIONS » · SORTI
Expression : l'air de quelqu'un qui a déjà vu ça cent fois, un sourcil levé.
Scène : les douze assiettes. Toi, gérant, en 2026.

**EP030** · S1 · décor SALLE · texte « ACADEMY » · SORTI
Expression : l'air de quelqu'un qui a déjà vu ça cent fois, un sourcil levé.
Scène : le pingouin en cuisine. Le nouveau, jour 1.

**EP031** · S2 · décor BUREAU · texte « ÉTIQUETTES DLC » · SORTI
Expression : un sourire en coin, parfaitement serein au milieu du désastre.
Scène : l'avalanche de tupperware. C'est quoi, ça ?

**EP032** · S2 · décor BUREAU · texte « MA CARTE » · SORTI
Expression : faussement dépité, la main sur le front, mais l'œil qui rit.
Scène : la sauce trop forte. Ta recette « au feeling ».

**EP033** · S2 · décor BUREAU · texte « MOUVEMENTS DE STOCK » · SORTI
Expression : l'air satisfait de celui qui sait que le problème est déjà réglé.
Scène : le rôti disparu. Tu as tout préparé. Presque.

**EP034** · S2 · décor BUREAU · texte « PROCESS » · SORTI
Expression : l'air de quelqu'un qui a déjà vu ça cent fois, un sourcil levé.
Scène : le bouchon rebelle. Chaque service, une improvisation.

**EP035** · S2 · décor BUREAU · texte « LIRE SES PRÉVISIONS » · SORTI
Expression : un sourire en coin, parfaitement serein au milieu du désastre.
Scène : le parasol fugitif. Ta terrasse, un jour de vent.

**EP036** · S2 · décor BUREAU · texte « UN SEUL ABONNEMENT » · SORTI
Expression : faussement dépité, la main sur le front, mais l'œil qui rit.
Scène : l'addition. Toi, devant tes abonnements.

**EP037** · S2 · décor BUREAU · texte « CRÉER UN SHIFT » · SORTI
Expression : l'air satisfait de celui qui sait que le problème est déjà réglé.
Scène : le dormeur debout. Fermeture. Troisième soir d'affilée.

**EP038** · S2 · décor BUREAU · texte « MA LISTE COURSES » · SORTI
Expression : l'air de quelqu'un qui a déjà vu ça cent fois, un sourcil levé.
Scène : le chariot fou. Le réappro du lundi.

**EP039** · S2 · décor BUREAU · texte « GÉRER ET NO-SHOWS » · SORTI
Expression : un sourire en coin, parfaitement serein au milieu du désastre.
Scène : le ballon dans la soupe. L'imprévu du service.

**EP040** · S2 · décor BUREAU · texte « AJOUTER UN MOUVEMENT » · SORTI
Expression : un sourire en coin, parfaitement serein au milieu du désastre.
Scène : la chèvre au potager. Ton stock de basilic.

**EP041** · S2 · décor BUREAU · texte « SORTIE INGRÉDIENTS PRODUCTION » · SORTI
Expression : faussement dépité, la main sur le front, mais l'œil qui rit.
Scène : le poulet fugueur. Ton contrôle des portions.

**EP042** · S2 · décor BUREAU · texte « MCP RAPIDOCMS IRIS » · SORTI
Expression : l'air satisfait de celui qui sait que le problème est déjà réglé.
Scène : la nappe et le vent. Tout faire seul.

**EP043** · S2 · décor BUREAU · texte « REMISES ET AVOIRS »
Expression : l'air de quelqu'un qui a déjà vu ça cent fois, un sourcil levé.
Scène : l'écureuil et le croissant. Petit vol. Tous les jours.

**EP044** · S2 · décor BUREAU · texte « COMMANDER PAR QR » · SORTI
Expression : un sourire en coin, parfaitement serein au milieu du désastre.
Scène : les six stylos. Prendre la commande en 2026.

**EP045** · S2 · décor BUREAU · texte « STATISTIQUES PAR MODULE » · SORTI
Expression : faussement dépité, la main sur le front, mais l'œil qui rit.
Scène : la chambre froide. Personne ne sait où tu es.

**EP046** · S2 · décor BUREAU · texte « AGENT IA SUGGESTIONS »
Expression : l'air satisfait de celui qui sait que le problème est déjà réglé.
Scène : le sel. Un détail. Un service perdu.

**EP047** · S2 · décor BUREAU · texte « CONTRÔLE À RÉCEPTION »
Expression : l'air de quelqu'un qui a déjà vu ça cent fois, un sourcil levé.
Scène : le camion dans la ruelle. La livraison de 7 h.

**EP048** · S2 · décor BUREAU · texte « PARAMÉTRAGE INITIAL »
Expression : un sourire en coin, parfaitement serein au milieu du désastre.
Scène : la pyramide de sucre. Ce que tu construis chaque jour.

**EP049** · S2 · décor BUREAU · texte « RELEVÉ DE TEMPÉRATURE »
Expression : faussement dépité, la main sur le front, mais l'œil qui rit.
Scène : le chien du pass. Il envoie plus vite que ton pass.

**EP050** · S2 · décor BUREAU · texte « ÉQUIPEMENTS »
Expression : faussement dépité, la main sur le front, mais l'œil qui rit.
Scène : la casserole brûlante. Apprendre sur le tas.

**EP051** · S2 · décor BUREAU · texte « ÉTIQUETTES DLC »
Expression : l'air satisfait de celui qui sait que le problème est déjà réglé.
Scène : la mousse. Un mauvais réglage. Une seule fois.

**EP052** · S2 · décor BUREAU · texte « TRAÇABILITÉ »
Expression : l'air de quelqu'un qui a déjà vu ça cent fois, un sourcil levé.
Scène : le tablier coincé. Encore un truc qui te retient.

**EP053** · S2 · décor BUREAU · texte « RÉCEPTION FOURNISSEUR »
Expression : un sourire en coin, parfaitement serein au milieu du désastre.
Scène : la file et la salle vide. Complet dehors. Vide dedans.

**EP054** · S2 · décor BUREAU · texte « PLAN DE NETTOYAGE »
Expression : faussement dépité, la main sur le front, mais l'œil qui rit.
Scène : le pois. Ton prix ne raconte pas ton coût.

**EP055** · S2 · décor BUREAU · texte « CHECKLISTS HYGIÈNE »
Expression : l'air satisfait de celui qui sait que le problème est déjà réglé.
Scène : le ventilateur. Ta compta, au format papier.

**EP056** · S2 · décor BUREAU · texte « HISTORIQUE »
Expression : l'air de quelqu'un qui a déjà vu ça cent fois, un sourcil levé.
Scène : le passager clandestin. Il y a toujours un truc en trop.

**EP057** · S2 · décor BUREAU · texte « ALERTES »
Expression : un sourire en coin, parfaitement serein au milieu du désastre.
Scène : les pièces. La clôture de caisse.

**EP058** · S2 · décor BUREAU · texte « RÔLES »
Expression : faussement dépité, la main sur le front, mais l'œil qui rit.
Scène : les bougies. L'anniversaire de la table 12.

**EP059** · S2 · décor BUREAU · texte « NON-CONFORMITÉ »
Expression : l'air satisfait de celui qui sait que le problème est déjà réglé.
Scène : l'ardoise. Ta com', chaque matin.

**EP060** · S2 · décor BUREAU · texte « CONGÉLATION »
Expression : l'air satisfait de celui qui sait que le problème est déjà réglé.
Scène : le poulpe multitâche. Ce qu'on te demande d'être.

**EP061** · S3 · décor CUISINE · texte « RAPPORT HACCP » · SORTI
Expression : l'air de quelqu'un qui a déjà vu ça cent fois, un sourcil levé.
Scène : le badge introuvable. Ton système de pointage.

**EP062** · S3 · décor CUISINE · texte « ROUTINE DU JOUR » · SORTI
Expression : un sourire en coin, parfaitement serein au milieu du désastre.
Scène : la photo de pointage. Je te jure, j'étais là à 8 h.

**EP063** · S3 · décor CUISINE · texte « CRÉER UN EMPLOYÉ » · SORTI
Expression : faussement dépité, la main sur le front, mais l'œil qui rit.
Scène : le post-it perdu. Ta demande de congé.

**EP064** · S3 · décor CUISINE · texte « PLANNING SEMAINE » · SORTI
Expression : l'air satisfait de celui qui sait que le problème est déjà réglé.
Scène : le planning au marqueur. Le planning de la semaine.

**EP065** · S3 · décor CUISINE · texte « POINTAGES » · SORTI
Expression : l'air de quelqu'un qui a déjà vu ça cent fois, un sourcil levé.
Scène : le stagiaire au bureau. Qui a accès à quoi ?

**EP066** · S3 · décor CUISINE · texte « CONGÉS » · SORTI
Expression : un sourire en coin, parfaitement serein au milieu du désastre.
Scène : le grille-pain qui ne répond pas. Ta cuisine n'a personne à qui parler.

**EP067** · S3 · décor CUISINE · texte « CONTRATS » · SORTI
Expression : faussement dépité, la main sur le front, mais l'œil qui rit.
Scène : le thermomètre humain. Ton relevé de température.

**EP068** · S3 · décor CUISINE · texte « COÛT DU TRAVAIL »
Expression : l'air satisfait de celui qui sait que le problème est déjà réglé.
Scène : le second avis. Le test scientifique du nez.

**EP069** · S3 · décor CUISINE · texte « RECRUTEMENT » · SORTI
Expression : l'air de quelqu'un qui a déjà vu ça cent fois, un sourcil levé.
Scène : le livreur fantôme. Tu as vérifié la livraison ?

**EP070** · S3 · décor CUISINE · texte « ONBOARDING » · SORTI
Expression : l'air de quelqu'un qui a déjà vu ça cent fois, un sourcil levé.
Scène : la dalle propre. C'est fait.

**EP071** · S3 · décor CUISINE · texte « MULTI-POSTES » · SORTI
Expression : un sourire en coin, parfaitement serein au milieu du désastre.
Scène : la liste à l'envers. La check-list du soir.

**EP072** · S3 · décor CUISINE · texte « ABSENCES » · SORTI
Expression : faussement dépité, la main sur le front, mais l'œil qui rit.
Scène : le classeur. Contrôle sanitaire. Ce matin.

**EP073** · S3 · décor CUISINE · texte « ÉTABLISSEMENT » · SORTI
Expression : l'air satisfait de celui qui sait que le problème est déjà réglé.
Scène : pile ou face. Combien tu commandes pour samedi ?

**EP074** · S3 · décor CUISINE · texte « CATÉGORIES » · SORTI
Expression : l'air de quelqu'un qui a déjà vu ça cent fois, un sourcil levé.
Scène : la liste oubliée. Tu as oublié la liste.

**EP075** · S3 · décor CUISINE · texte « TVA » · SORTI
Expression : un sourire en coin, parfaitement serein au milieu du désastre.
Scène : la facture dans la poche. Ta facture fournisseur.

**EP076** · S3 · décor CUISINE · texte « ZONES ET TABLES »
Expression : faussement dépité, la main sur le front, mais l'œil qui rit.
Scène : le recomptage. Ton inventaire du mardi.

**EP077** · S3 · décor CUISINE · texte « ÉQUIPEMENTS »
Expression : l'air satisfait de celui qui sait que le problème est déjà réglé.
Scène : le devis sur le set de table. Ton devis pour le mariage de samedi.

**EP078** · S3 · décor CUISINE · texte « UTILISATEURS »
Expression : l'air de quelqu'un qui a déjà vu ça cent fois, un sourcil levé.
Scène : la boîte à chaussures. Ta comptabilité annuelle.

**EP079** · S3 · décor CUISINE · texte « IMPORT DE CARTE »
Expression : un sourire en coin, parfaitement serein au milieu du désastre.
Scène : les quatorze cartes. Ton programme de fidélité.

**EP080** · S3 · décor CUISINE · texte « ABONNEMENT »
Expression : un sourire en coin, parfaitement serein au milieu du désastre.
Scène : le tiroir vide. Ouverture. Fond de caisse : ?

**EP081** · S3 · décor CUISINE · texte « FACTURES »
Expression : faussement dépité, la main sur le front, mais l'œil qui rit.
Scène : huit calculatrices. On peut séparer ?

**EP082** · S3 · décor CUISINE · texte « DEVIS »
Expression : l'air satisfait de celui qui sait que le problème est déjà réglé.
Scène : le centime. Il manque un centime.

**EP083** · S3 · décor CUISINE · texte « IMPAYÉS »
Expression : l'air de quelqu'un qui a déjà vu ça cent fois, un sourcil levé.
Scène : le cri dans le vide. J'AI DIT DEUX BURGERS !

**EP084** · S3 · décor CUISINE · texte « DÉPENSES »
Expression : un sourire en coin, parfaitement serein au milieu du désastre.
Scène : le qr code scotché. Commander à table.

**EP085** · S3 · décor CUISINE · texte « SYNTHÈSE »
Expression : faussement dépité, la main sur le front, mais l'œil qui rit.
Scène : le ballon qui se dégonfle. Table de 8. 20 h 30. Personne.

**EP086** · S3 · décor CUISINE · texte « EXPORT COMPTABLE »
Expression : l'air satisfait de celui qui sait que le problème est déjà réglé.
Scène : le téléphone que personne ne prend. Trois appels manqués pendant le coup de feu.

**EP087** · S3 · décor CUISINE · texte « ÉDITEUR »
Expression : l'air de quelqu'un qui a déjà vu ça cent fois, un sourcil levé.
Scène : les trois tablettes. Trois plateformes. Trois écrans.

**EP088** · S3 · décor CUISINE · texte « PAGES »
Expression : un sourire en coin, parfaitement serein au milieu du désastre.
Scène : une étoile. Un avis. Publié il y a six jours.

**EP089** · S3 · décor CUISINE · texte « DOMAINE »
Expression : faussement dépité, la main sur le front, mais l'œil qui rit.
Scène : le bocal presque vide. Ton jeu concours.

**EP090** · S3 · décor CUISINE · texte « LEADS DU SITE »
Expression : faussement dépité, la main sur le front, mais l'œil qui rit.
Scène : le marc de café. Ta prévision pour samedi.

**EP091** · S4 · décor DEVANTURE · texte « AJOUTER UNE RÉSERVATION »
Expression : l'air satisfait de celui qui sait que le problème est déjà réglé.
Scène : le pétard dans le tiramisu. Anniversaire de table 12.

**EP092** · S4 · décor DEVANTURE · texte « GÉRER ET NO-SHOWS »
Expression : l'air de quelqu'un qui a déjà vu ça cent fois, un sourcil levé.
Scène : le super-héros qui a réservé. Lui, il avait réservé.

**EP093** · S4 · décor DEVANTURE · texte « PRÉDICTIONS DES COMMANDES »
Expression : un sourire en coin, parfaitement serein au milieu du désastre.
Scène : le chef part à la pêche. Rupture de stock, 20 h 15.

**EP094** · S4 · décor DEVANTURE · texte « CENTRALISER LES COMMANDES »
Expression : faussement dépité, la main sur le front, mais l'œil qui rit.
Scène : le robot livreur qui double le scooter. 2026, la livraison change de main.

**EP095** · S4 · décor DEVANTURE · texte « GÉRER KDS DIRECT »
Expression : l'air satisfait de celui qui sait que le problème est déjà réglé.
Scène : l'éclipse de 13 h 12. Le service s'est arrêté deux minutes.

**EP096** · S4 · décor DEVANTURE · texte « RELEVÉ DE TEMPÉRATURE »
Expression : l'air de quelqu'un qui a déjà vu ça cent fois, un sourcil levé.
Scène : canicule : le beurre fugueur. 39° en cuisine.

**EP097** · S4 · décor DEVANTURE · texte « RELIER UBER EATS »
Expression : un sourire en coin, parfaitement serein au milieu du désastre.
Scène : le mur de tablettes. Six plateformes. Six alertes.

**EP098** · S4 · décor DEVANTURE · texte « COMMANDES MULTI-CANAUX »
Expression : faussement dépité, la main sur le front, mais l'œil qui rit.
Scène : le robot serveur qui bugge et danse. Ton nouveau serveur, en période d'essai.

**EP099** · S4 · décor DEVANTURE · texte « CONFIGURER VOIX PROMPTS »
Expression : l'air satisfait de celui qui sait que le problème est déjà réglé.
Scène : le répondeur préhistorique. Quarante appels pendant le rush.

**EP100** · S4 · décor DEVANTURE · texte « DÉBLOQUER LES AVIS »
Expression : faussement dépité, la main sur le front, mais l'œil qui rit.
Scène : l'influenceur au ring light. Il a mis vingt minutes à filmer.

**EP101** · S4 · décor DEVANTURE · texte « CLÔTURER SA CAISSE »
Expression : l'air satisfait de celui qui sait que le problème est déjà réglé.
Scène : pov : thriller comptable. Rapprochement des caisses. Vendredi soir.

**EP102** · S4 · décor DEVANTURE · texte « CHECKLISTS HYGIÈNE »
Expression : l'air de quelqu'un qui a déjà vu ça cent fois, un sourcil levé.
Scène : l'inspecteur surprise. Contrôle surprise. Ou pas.

**EP103** · S4 · décor DEVANTURE · texte « RÉSERVATIONS DU JOUR »
Expression : un sourire en coin, parfaitement serein au milieu du désastre.
Scène : le car de 40 sans réservation. Quarante couverts. Sans prévenir.

**EP104** · S4 · décor DEVANTURE · texte « GÉRER ET NO-SHOWS »
Expression : faussement dépité, la main sur le front, mais l'œil qui rit.
Scène : le no-show western. Table de huit. 20 h 30.

**EP105** · S4 · décor DEVANTURE · texte « RÉSERVATIONS ET HORAIRES »
Expression : l'air satisfait de celui qui sait que le problème est déjà réglé.
Scène : le duel de la dernière table. Dernière table du samedi.

**EP106** · S4 · décor DEVANTURE · texte « SÉPARER UNE ADDITION »
Expression : l'air de quelqu'un qui a déjà vu ça cent fois, un sourcil levé.
Scène : l'addition en quatorze parts. On peut payer chacun ?

**EP107** · S4 · décor DEVANTURE · texte « ENCAISSER UNE COMMANDE »
Expression : un sourire en coin, parfaitement serein au milieu du désastre.
Scène : le magicien de l'addition. Tout le monde a un tour.

**EP108** · S4 · décor DEVANTURE · texte « VUE KDS PAR »
Expression : faussement dépité, la main sur le front, mais l'œil qui rit.
Scène : le poulpe du pass. Il te faudrait six bras.

**EP109** · S4 · décor DEVANTURE · texte « TRAÇABILITÉ »
Expression : l'air satisfait de celui qui sait que le problème est déjà réglé.
Scène : le kombucha qui explose. Ta cave à ferments.

**EP110** · S4 · décor DEVANTURE · texte « STATISTIQUES PAR MODULE »
Expression : l'air satisfait de celui qui sait que le problème est déjà réglé.
Scène : le menu 100 % matcha. Tu suis toutes les tendances.

**EP111** · S4 · décor DEVANTURE · texte « VALIDER UNE PRODUCTION »
Expression : l'air de quelqu'un qui a déjà vu ça cent fois, un sourcil levé.
Scène : l'imprimante 3d qui déraille. La cuisine du futur.

**EP112** · S4 · décor DEVANTURE · texte « CHOISIR TON TEMPLATE »
Expression : un sourire en coin, parfaitement serein au milieu du désastre.
Scène : le casque de réalité augmentée. La carte du futur.

**EP113** · S4 · décor DEVANTURE · texte « CENTRALISER LES COMMANDES »
Expression : faussement dépité, la main sur le front, mais l'œil qui rit.
Scène : le drone qui se trompe de balcon. Livraison réussie. Presque.

**EP114** · S4 · décor DEVANTURE · texte « LANCER UNE CAMPAGNE »
Expression : l'air satisfait de celui qui sait que le problème est déjà réglé.
Scène : la choré pendant que ça brûle. Ton community manager, c'est ta brigade.

**EP115** · S4 · décor DEVANTURE · texte « MOUVEMENTS DE STOCK »
Expression : l'air de quelqu'un qui a déjà vu ça cent fois, un sourcil levé.
Scène : les poules du potager du toit. Circuit court, très court.

**EP116** · S4 · décor DEVANTURE · texte « CRÉER TES POSTES »
Expression : un sourire en coin, parfaitement serein au milieu du désastre.
Scène : le stagiaire et le mur de craie. Ton système de commandes.

**EP117** · S4 · décor DEVANTURE · texte « MA CARTE »
Expression : faussement dépité, la main sur le front, mais l'œil qui rit.
Scène : le plat étoilé en dix minutes. Le défi à dix minutes.

**EP118** · S4 · décor DEVANTURE · texte « CRÉER SITE PAR »
Expression : l'air satisfait de celui qui sait que le problème est déjà réglé.
Scène : la file du brunch. Le brunch du dimanche.

**EP119** · S4 · décor DEVANTURE · texte « CIBLAGE ET CONSENTEMENT »
Expression : l'air de quelqu'un qui a déjà vu ça cent fois, un sourcil levé.
Scène : la mascotte poulet et le vent. Ta stratégie d'acquisition.

**EP120** · S4 · décor DEVANTURE · texte « LIRE SES PRÉVISIONS »
Expression : l'air de quelqu'un qui a déjà vu ça cent fois, un sourcil levé.
Scène : la réunion des dix logiciels. Réunion de tes dix logiciels.

**EP121** · S5 · décor AUBE · texte « ENVOI DIRECT CUISINE »
Expression : un sourire en coin, parfaitement serein au milieu du désastre.
Scène : le modificateur infini. Alors, sans oignon, mais…

**EP122** · S5 · décor AUBE · texte « VUE CLIENT FIDÉLITÉ »
Expression : faussement dépité, la main sur le front, mais l'œil qui rit.
Scène : « comme d'habitude ». Il dit « comme d'habitude ».

**EP123** · S5 · décor AUBE · texte « MA CARTE »
Expression : l'air satisfait de celui qui sait que le problème est déjà réglé.
Scène : le végétarien du dessert. Il annonce ça au dessert.

**EP124** · S5 · décor AUBE · texte « CLÔTURER SA CAISSE »
Expression : l'air de quelqu'un qui a déjà vu ça cent fois, un sourcil levé.
Scène : la table qui ne part jamais. Il est minuit dix.

**EP125** · S5 · décor AUBE · texte « DESSINER PLAN SALLE »
Expression : un sourire en coin, parfaitement serein au milieu du désastre.
Scène : le client qui refait le plan de salle. Je serais mieux là, non ?

**EP126** · S5 · décor AUBE · texte « SÉPARER UNE ADDITION »
Expression : faussement dépité, la main sur le front, mais l'œil qui rit.
Scène : six fourchettes, une salade. On partage, c'est plus convivial.

**EP127** · S5 · décor AUBE · texte « RÉSERVATIONS DU JOUR »
Expression : l'air satisfait de celui qui sait que le problème est déjà réglé.
Scène : réveillon, 23 h 58. Bonne année à tout le monde.

**EP128** · S5 · décor AUBE · texte « PLACER CLIENT TABLE »
Expression : l'air de quelqu'un qui a déjà vu ça cent fois, un sourcil levé.
Scène : saint-valentin surbookée. Trente couverts en plus, ça rentre.

**EP129** · S5 · décor AUBE · texte « GÉRER SES TABLES »
Expression : un sourire en coin, parfaitement serein au milieu du désastre.
Scène : premier jour de terrasse, 4 degrés. Premier rayon de soleil de l'année.

**EP130** · S5 · décor AUBE · texte « TON AGENDA MARKETING »
Expression : un sourire en coin, parfaitement serein au milieu du désastre.
Scène : fête de la musique. 21 juin. Devant ta porte.

**EP131** · S5 · décor AUBE · texte « PLANNING SEMAINE »
Expression : faussement dépité, la main sur le front, mais l'œil qui rit.
Scène : rentrée : tout le monde est encore en vacances. 1er septembre. Deux absents.

**EP132** · S5 · décor AUBE · texte « RÉSERVATIONS ET HORAIRES »
Expression : l'air satisfait de celui qui sait que le problème est déjà réglé.
Scène : le 15 août, seul ouvert. Tout le quartier est fermé.

**EP133** · S5 · décor AUBE · texte « ENCAISSER UNE COMMANDE »
Expression : l'air de quelqu'un qui a déjà vu ça cent fois, un sourcil levé.
Scène : le but à la 90e. Une minute pour encaisser trois tournées.

**EP134** · S5 · décor AUBE · texte « RELEVÉ DE TEMPÉRATURE »
Expression : un sourire en coin, parfaitement serein au milieu du désastre.
Scène : pov : la friteuse. Sept heures de service. Vue d'en bas.

**EP135** · S5 · décor AUBE · texte « RÉSERVATIONS DU JOUR »
Expression : faussement dépité, la main sur le front, mais l'œil qui rit.
Scène : pov : le carnet de réservations. Toutes tes réservations du soir.

**EP136** · S5 · décor AUBE · texte « COMMANDES MULTI-CANAUX »
Expression : l'air satisfait de celui qui sait que le problème est déjà réglé.
Scène : pov : le lave-verres. Deux minutes par cycle. Quatre-vingts cycles.

**EP137** · S5 · décor AUBE · texte « ENCAISSER UNE COMMANDE »
Expression : l'air de quelqu'un qui a déjà vu ça cent fois, un sourcil levé.
Scène : pov : la machine à café. Deux cent quarante cafés. Aujourd'hui.

**EP138** · S5 · décor AUBE · texte « GÉRER KDS DIRECT »
Expression : un sourire en coin, parfaitement serein au milieu du désastre.
Scène : pov : l'assiette, du pass à la table. Quarante-cinq secondes de vie.

**EP139** · S5 · décor AUBE · texte « VUE KDS PAR »
Expression : faussement dépité, la main sur le front, mais l'œil qui rit.
Scène : le rush, film de guerre. 20 h 30. Le coup de feu.

**EP140** · S5 · décor AUBE · texte « MOUVEMENTS DE STOCK »
Expression : faussement dépité, la main sur le front, mais l'œil qui rit.
Scène : le braquage du frigo. Ton inventaire, la nuit.

**EP141** · S5 · décor AUBE · texte « PARLER À PREDIBOT »
Expression : l'air satisfait de celui qui sait que le problème est déjà réglé.
Scène : cuisine, cockpit spatial. Table 6 depuis 22 minutes.

**EP142** · S5 · décor AUBE · texte « AFFECTATION DES POSTES »
Expression : l'air de quelqu'un qui a déjà vu ça cent fois, un sourcil levé.
Scène : duel à la spatule. Qui envoie le plat du jour.

**EP143** · S5 · décor AUBE · texte « DEVIS »
Expression : un sourire en coin, parfaitement serein au milieu du désastre.
Scène : la commande de 200 pièces. Une seule commande.

**EP144** · S5 · décor AUBE · texte « RÉPONDRE AUX AVIS »
Expression : faussement dépité, la main sur le front, mais l'œil qui rit.
Scène : le procès du steak trop cuit. Un avis une étoile.

**EP145** · S5 · décor AUBE · texte « LIRE SES PRÉVISIONS »
Expression : l'air satisfait de celui qui sait que le problème est déjà réglé.
Scène : documentaire animalier : le gérant. Le gérant, dans son habitat naturel.

**EP146** · S5 · décor AUBE · texte « ÉVÉNEMENTS PRIVÉS »
Expression : l'air de quelqu'un qui a déjà vu ça cent fois, un sourcil levé.
Scène : quarante bougies et les sprinklers. Quarante bougies. Une seule mauvaise idée.

**EP147** · S5 · décor AUBE · texte « FACTURE ET DEVIS »
Expression : un sourire en coin, parfaitement serein au milieu du désastre.
Scène : le gâteau à cinq étages. Douze mille euros de prestation.

**EP148** · S5 · décor AUBE · texte « SYNCHRO CAISSE TIERCE »
Expression : faussement dépité, la main sur le front, mais l'œil qui rit.
Scène : le sumo de la place de livraison. Trois plateformes. Une place.

**EP149** · S5 · décor AUBE · texte « LANCER UNE CAMPAGNE »
Expression : l'air satisfait de celui qui sait que le problème est déjà réglé.
Scène : le flash mob de la salle. Ta salle a un truc que personne d'autre n'a.

**EP150** · S5 · décor AUBE · texte « LIRE SES PRÉVISIONS »
Expression : l'air satisfait de celui qui sait que le problème est déjà réglé.
Scène : le salut final. Cent cinquante épisodes.

---

## Contrôle avant de rendre la main

- 150 fichiers dans `public/vignettes/`, tous en couleur, aucun manquant ;
- 150 `posterUrl` mis à jour, aucun autre champ touché ;
- aucun second logo sur aucune image ;
- deux images prises au hasard dans la même saison montrent deux scènes
  différentes ;
- le visage du chef est le même sur les 150, et c'est celui de la photo jointe ;
- plus aucun écran noir sur la grille des épisodes.
