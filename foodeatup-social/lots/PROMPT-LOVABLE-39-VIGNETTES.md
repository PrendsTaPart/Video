# Prompt Lovable — les 39 vignettes des épisodes sortis

Un seul tour pour trente-neuf vignettes. À coller tel quel dans Lovable, **avec
la photo du chef en pièce jointe**.

---

## Le message

L'image jointe est la photo officielle du chef FoodEatUp. Elle est aussi ici :
https://raw.githubusercontent.com/PrendsTaPart/Video/claude/foodeatup-video-factory-wtb7gs/foodeatup-social/public/brand/chef-foodeatup.jpg

Génère les **39 vignettes** listées plus bas — une par épisode sorti — en
utilisant cette photo comme image de référence, puis fais pointer le `posterUrl`
de chaque épisode sur son image.

### Ce que tu changes dans le projet, et rien d'autre

1. Tu enregistres chaque image dans `public/vignettes/EPxxx.jpg`, format 9:16,
   1080 × 1920.
2. Tu mets à jour le seul champ `posterUrl` de ces 39 épisodes dans
   `src/data/series.ts`.

**Ne touche à aucun autre champ de `src/data/series.ts` ni à `src/data/contenu.ts`.**
Ces deux fichiers sont générés par l'usine à vidéos et poussés depuis le dépôt :
`statut`, `videoUrl`, `masterRapidoUrl`, `higgsfield.videoSourceUrl`,
`dureeSecondes` et les publications y sont déjà à jour et corrects. Une
régénération de ta part les écraserait, et la prochaine mise à jour de l'usine
écraserait la tienne. Les liens de la bibliothèque RapidoCMS y sont tous
renseignés : les 39 masters montés et les 63 clips Higgsfield d'origine.

### Le chef ne se redessine pas

Même visage, même barbe, même toque blanche, même veste blanche, même tablier au
logo FoodEatUp bleu. C'est **la même personne sur les 150 épisodes** — c'est ce
qui fait une série plutôt qu'une collection d'images. Si une image sort avec un
autre visage, une autre morphologie ou un autre costume, refais-la plutôt que de
l'accepter.

### Trois défauts du premier jet, à ne pas reproduire

Les 300 vignettes générées jusqu'ici ont trois problèmes. Ils viennent d'une
lecture rapide de la consigne, pas d'une limite de l'outil.

1. **Le grisé ne se cuit pas dans le fichier.** Les épisodes non sortis étaient
   désaturés dans le JPEG lui-même. Le jour où l'épisode sort, sa vignette reste
   grise pour toujours. Le grisé est un état d'affichage, le site le pose déjà en
   CSS. Génère **toutes** les images en couleur, sans exception.

2. **Un seul logo.** Le tablier du chef porte déjà le logo FoodEatUp. N'ajoute
   aucun second badge — ni en bas à droite, ni ailleurs — et surtout pas un logo
   redessiné. Deux marques sur la même image, dont une fausse, c'est le défaut le
   plus visible du premier jet.

3. **Chaque épisode a sa scène.** Les 300 premières images réutilisaient le même
   décor et la même pose ; seul le texte du bandeau changeait. Chaque bloc
   ci-dessous décrit un gag précis. Si deux épisodes sortent avec la même image,
   c'est que le bloc n'a pas été lu.

### Le gabarit, identique sur les 39

> Photo réaliste, cadrage vertical 9:16. Le chef de l'image de référence — MÊME
> visage, même barbe, même toque blanche, même veste de cuisine blanche, même
> tablier blanc au logo FoodEatUp bleu. Ne change ni ses traits ni sa
> morphologie. Son expression : **{EXPRESSION}**. Scène : **{SCÈNE}**. Décor :
> **{DÉCOR}**. Le chef occupe les deux tiers droits du cadre, en plan poitrine ;
> l'élément comique est visible à gauche. Bande crème #FCF9E6 en haut du cadre
> sur un cinquième de la hauteur, portant UNIQUEMENT le texte **« {TEXTE} »** en
> typographie arrondie très grasse, bleu marine #0F1A23, centré. Aucun autre
> texte, aucun logo ajouté, pas de filigrane, pas de bordure décorative.

### Les trois décors

- **SALLE** — une salle de restaurant en plein service, tables dressées, clients
  flous en arrière-plan ; lumière chaude de fin de journée, reflets dorés.
- **BUREAU** — un bureau d'arrière-salle, classeurs, tickets de caisse,
  calculatrice, cartons de livraison ; lumière rasante de néon adouci, ambiance
  fin de mois.
- **CUISINE** — une cuisine professionnelle en pleine brigade, inox, passe-plat,
  plannings punaisés au mur ; lumière blanche et nette de cuisine, vapeur légère.

Le décor dit la saison, pas l'épisode : c'est ce qui fait tenir une saison
ensemble à l'œil. Le gag, lui, change à chaque fois.

---

## Les 39 épisodes

**EP001** · décor SALLE · texte « COMMANDES MULTI-CANAUX »
Expression : faussement dépité, la main sur le front, mais l'œil qui rit.
Scène : le chien qui te regarde. Lui aussi attend ta commande.

**EP002** · décor SALLE · texte « ENVOI DIRECT CUISINE »
Expression : l'air satisfait de celui qui sait que le problème est déjà réglé.
Scène : la chute en skateboard. Ton service du samedi soir.

**EP003** · décor SALLE · texte « MA CARTE »
Expression : l'air de quelqu'un qui a déjà vu ça cent fois, un sourcil levé.
Scène : le plat dans la piscine. Ta marge, en ce moment.

**EP005** · décor SALLE · texte « VUE D'ENSEMBLE »
Expression : faussement dépité, la main sur le front, mais l'œil qui rit.
Scène : le serveur qui glisse. Trois logiciels. Deux mains.

**EP006** · décor SALLE · texte « AJOUTER MODIFIER MOUVEMENT »
Expression : l'air satisfait de celui qui sait que le problème est déjà réglé.
Scène : la pizza frisbee. Ta pizza part plus vite que ton stock.

**EP007** · décor SALLE · texte « RÉPONDRE AUX AVIS »
Expression : l'air de quelqu'un qui a déjà vu ça cent fois, un sourcil levé.
Scène : la mamie qui goûte. Le seul avis client qui compte.

**EP010** · décor SALLE · texte « LIRE SES PRÉVISIONS »
Expression : faussement dépité, la main sur le front, mais l'œil qui rit.
Scène : le flambage raté. Toi, devant ta facture logicielle.

**EP013** · décor SALLE · texte « PARLER À PREDIBOT »
Expression : un sourire en coin, parfaitement serein au milieu du désastre.
Scène : l'avalanche de notifications. Dix logiciels. Dix notifications.

**EP014** · décor SALLE · texte « MOUVEMENTS DE STOCK »
Expression : faussement dépité, la main sur le front, mais l'œil qui rit.
Scène : le raton laveur. Ton gaspillage alimentaire.

**EP015** · décor SALLE · texte « RÉFÉRENTIELS »
Expression : l'air satisfait de celui qui sait que le problème est déjà réglé.
Scène : la tour d'assiettes. Ta gestion actuelle.

**EP016** · décor SALLE · texte « DÉPENSES »
Expression : l'air de quelqu'un qui a déjà vu ça cent fois, un sourcil levé.
Scène : le geyser à café. Tes coûts, ce trimestre.

**EP017** · décor SALLE · texte « CRÉATION D'UN RAPPORT »
Expression : un sourire en coin, parfaitement serein au milieu du désastre.
Scène : le ninja de la frite. Personne ne touche à ta dernière frite.

**EP018** · décor SALLE · texte « SITE »
Expression : faussement dépité, la main sur le front, mais l'œil qui rit.
Scène : le serveur baywatch. Le rush de vingt heures.

**EP019** · décor SALLE · texte « PRÉDICTIONS DES COMMANDES »
Expression : l'air satisfait de celui qui sait que le problème est déjà réglé.
Scène : le burger qui rebondit. Ton chiffre d'affaires, sans outil.

**EP020** · décor SALLE · texte « AJOUTER UNE RÉSERVATION »
Expression : l'air satisfait de celui qui sait que le problème est déjà réglé.
Scène : le chien qui a réservé. Lui, il a réservé.

**EP021** · décor SALLE · texte « CRÉER TES POSTES »
Expression : l'air de quelqu'un qui a déjà vu ça cent fois, un sourcil levé.
Scène : chef contre imprimante. Le vrai ennemi du service.

**EP022** · décor SALLE · texte « MARKETPLACE DE PROMPTS »
Expression : un sourire en coin, parfaitement serein au milieu du désastre.
Scène : la facture qui fait pleurer. Mille euros par mois.

**EP023** · décor SALLE · texte « CALENDRIER IA AVEC »
Expression : faussement dépité, la main sur le front, mais l'œil qui rit.
Scène : l'aspirateur robot. Ton automatisation actuelle.

**EP024** · décor SALLE · texte « CRÉER SITE PAR »
Expression : l'air satisfait de celui qui sait que le problème est déjà réglé.
Scène : la mouette braqueuse. Encore une commission en moins.

**EP025** · décor SALLE · texte « CAMPAGNE 100 % »
Expression : l'air de quelqu'un qui a déjà vu ça cent fois, un sourcil levé.
Scène : le mixeur sans couvercle. Quand tu lances une promo sans données.

**EP026** · décor SALLE · texte « ENVOYER LISTE COURSES »
Expression : un sourire en coin, parfaitement serein au milieu du désastre.
Scène : le ballon qui explose. Ton stock avant le week-end.

**EP029** · décor SALLE · texte « LIRE SES PRÉVISIONS »
Expression : l'air de quelqu'un qui a déjà vu ça cent fois, un sourcil levé.
Scène : les douze assiettes. Toi, gérant, en 2026.

**EP030** · décor SALLE · texte « ACADEMY »
Expression : l'air de quelqu'un qui a déjà vu ça cent fois, un sourcil levé.
Scène : le pingouin en cuisine. Le nouveau, jour 1.

**EP031** · décor BUREAU · texte « ÉTIQUETTES DLC »
Expression : un sourire en coin, parfaitement serein au milieu du désastre.
Scène : l'avalanche de tupperware. C'est quoi, ça ?

**EP032** · décor BUREAU · texte « MA CARTE »
Expression : faussement dépité, la main sur le front, mais l'œil qui rit.
Scène : la sauce trop forte. Ta recette « au feeling ».

**EP033** · décor BUREAU · texte « MOUVEMENTS DE STOCK »
Expression : l'air satisfait de celui qui sait que le problème est déjà réglé.
Scène : le rôti disparu. Tu as tout préparé. Presque.

**EP034** · décor BUREAU · texte « PROCESS »
Expression : l'air de quelqu'un qui a déjà vu ça cent fois, un sourcil levé.
Scène : le bouchon rebelle. Chaque service, une improvisation.

**EP035** · décor BUREAU · texte « LIRE SES PRÉVISIONS »
Expression : un sourire en coin, parfaitement serein au milieu du désastre.
Scène : le parasol fugitif. Ta terrasse, un jour de vent.

**EP036** · décor BUREAU · texte « UN SEUL ABONNEMENT »
Expression : faussement dépité, la main sur le front, mais l'œil qui rit.
Scène : l'addition. Toi, devant tes abonnements.

**EP037** · décor BUREAU · texte « CRÉER UN SHIFT »
Expression : l'air satisfait de celui qui sait que le problème est déjà réglé.
Scène : le dormeur debout. Fermeture. Troisième soir d'affilée.

**EP038** · décor BUREAU · texte « MA LISTE COURSES »
Expression : l'air de quelqu'un qui a déjà vu ça cent fois, un sourcil levé.
Scène : le chariot fou. Le réappro du lundi.

**EP039** · décor BUREAU · texte « GÉRER ET NO-SHOWS »
Expression : un sourire en coin, parfaitement serein au milieu du désastre.
Scène : le ballon dans la soupe. L'imprévu du service.

**EP040** · décor BUREAU · texte « AJOUTER UN MOUVEMENT »
Expression : un sourire en coin, parfaitement serein au milieu du désastre.
Scène : la chèvre au potager. Ton stock de basilic.

**EP041** · décor BUREAU · texte « SORTIE INGRÉDIENTS PRODUCTION »
Expression : faussement dépité, la main sur le front, mais l'œil qui rit.
Scène : le poulet fugueur. Ton contrôle des portions.

**EP042** · décor BUREAU · texte « MCP RAPIDOCMS IRIS »
Expression : l'air satisfait de celui qui sait que le problème est déjà réglé.
Scène : la nappe et le vent. Tout faire seul.

**EP044** · décor BUREAU · texte « COMMANDER PAR QR »
Expression : un sourire en coin, parfaitement serein au milieu du désastre.
Scène : les six stylos. Prendre la commande en 2026.

**EP045** · décor BUREAU · texte « STATISTIQUES PAR MODULE »
Expression : faussement dépité, la main sur le front, mais l'œil qui rit.
Scène : la chambre froide. Personne ne sait où tu es.

**EP061** · décor CUISINE · texte « RAPPORT HACCP »
Expression : l'air de quelqu'un qui a déjà vu ça cent fois, un sourcil levé.
Scène : le badge introuvable. Ton système de pointage.

**EP062** · décor CUISINE · texte « ROUTINE DU JOUR »
Expression : un sourire en coin, parfaitement serein au milieu du désastre.
Scène : la photo de pointage. Je te jure, j'étais là à 8 h.

---

## Contrôle avant de rendre la main

- 39 fichiers dans `public/vignettes/`, tous en couleur ;
- 39 `posterUrl` mis à jour, aucun autre champ touché ;
- aucun second logo sur aucune image ;
- deux images prises au hasard dans la même saison montrent deux scènes
  différentes ;
- le visage du chef est le même sur les 39, et c'est celui de la photo jointe.
