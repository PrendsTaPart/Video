# Prompt Lovable — la saison 6 et ses 30 vignettes

Un seul tour. À coller dans Lovable **avec les dix images des végé-fruités en
pièces jointes**.

---

## Le message

Les dix images jointes sont la Brigade Végé-Fruitée : La Fraise, Tomate Man,
L'Ail, La Pomme de Terre, Don Citrone, L'Oignon, La Betterave, Le Brocoli, La
Carotte, Le Navet. Elles sont déjà dans le projet, dans `public/brand/brigade/`.

La **saison 6 — « L'orchestration du restaurant »** vient d'entrer dans les
données : trente épisodes, EP151 à EP180. Elle renverse la série. Les cinq
premières saisons montrent le logiciel et mettent le chef en vedette. Celle-ci
montre le **restaurant**, et met en vedette **les végé-fruités** : ils y sont
une équipe d'agents IA qui fabrique la communication d'une maison, chacun avec
la main sur un outil réel.

Génère les **30 vignettes** listées plus bas et fais pointer chaque `posterUrl`
dessus.

### Ce que tu changes, et rien d'autre

1. Chaque image dans `public/vignettes/EPxxx.jpg`, format 9:16, 1080 × 1920.
2. Le seul champ `posterUrl` de ces 30 épisodes dans `src/data/series.ts`.

**Ne touche à aucun autre champ de `src/data/series.ts` ni à `src/data/contenu.ts`.**
Ces fichiers sont générés par l'usine à vidéos et poussés depuis le dépôt. La
saison 6 y a déjà ses trente épisodes, ses cent cinquante publications, ses arcs
et ses agents. Une régénération de ta part les écraserait.

### Ce qui change par rapport aux vignettes des saisons 1 à 5

| | Saisons 1 à 5 | Saison 6 |
|---|---|---|
| Vedette | le chef, photo réaliste | **le végé-fruité**, illustration 3D |
| Bandeau | crème #FCF9E6, texte marine | **bleu RapidoCMS #03A9F5, texte blanc** |
| Sujet | le logiciel | le restaurant |

Les deux styles coexistent : ne refais pas les vignettes des saisons 1 à 5.

### Le personnage ne se redessine pas

Chaque bloc nomme **un** végé-fruité et un seul. Prends son image jointe comme
référence et garde-le à l'identique : mêmes proportions, mêmes couleurs, même
tenue, même accessoire. C'est la même brigade sur les trente épisodes — et sur
tout le reste du site, où ces mêmes images sont déjà affichées. Une version
redessinée se verrait immédiatement à côté de l'originale.

### Le gabarit, identique sur les 30

> Illustration 3D, cadrage vertical 9:16, même style que l'image de référence
> jointe. Le personnage **{VÉGÉFRUITÉ}** gardé à l'identique — ne le redessine
> pas. Il est **la vedette** : il occupe les deux tiers du cadre, au premier
> plan, tourné vers l'objectif. Scène : **{SCÈNE}**. Décor derrière lui :
> **{DÉCOR}**, laissé flou et discret — c'est un fond, pas un sujet. Aucun humain
> photoréaliste dans l'image, aucun écran de logiciel lisible. Bande bleu
> RapidoCMS **#03A9F5** en haut du cadre sur un cinquième de la hauteur, portant
> UNIQUEMENT le texte **« {TEXTE} »** en typographie arrondie très grasse,
> **blanc**, centré. Aucun autre texte, aucun logo ajouté, pas de filigrane, pas
> de bordure décorative.

### Les cinq décors, un par arc

- **PASS** — le plat en très gros plan sur le pass, vapeur et reflets ; lumière
  rasante de studio culinaire.
- **SALLE DU SOIR** — la salle préparée pour le soir, tables dressées, lumières
  basses ; lumière chaude de début de service.
- **RÉSERVES** — la cuisine et les réserves avant l'ouverture, inox nu, cagettes ;
  lumière crue du matin.
- **TABLE** — une table en salle vue à hauteur de convive, verres et nappe ;
  lumière douce de fin de repas.
- **DEVANTURE** — la devanture et le comptoir, ardoise et carte affichée ; plein
  jour, lumière franche.

### Trois défauts déjà vus, à ne pas reproduire

1. **Pas de grisé cuit dans le fichier.** Aucun épisode de la saison 6 n'est
   encore tourné, et pourtant les trente images doivent être en couleur. Le
   statut est un état d'affichage, le site le pose en CSS.
2. **Un seul logo, et il n'est pas dans l'image.** N'ajoute aucun badge, aucune
   marque redessinée. Le bandeau bleu suffit à dire RapidoCMS.
3. **Une scène par épisode.** Un même végé-fruité revient trois fois dans la
   saison : ses trois images doivent montrer trois scènes différentes. Si les
   trois se ressemblent, le bloc n'a pas été lu.

---

## Les 30 épisodes

**EP151** · vedette **La Fraise** · décor PASS · texte « PLAT FILMÉ COMME »
Scène : le plat, filmé comme une pub. Regarde-le une seconde.

**EP152** · vedette **Tomate Man** · décor PASS · texte « RECETTE PLAT SIGNATURE »
Scène : la recette du plat signature. On ne cache rien.

**EP153** · vedette **L'Ail** · décor PASS · texte « PLAT SEMAINE »
Scène : le plat de la semaine. Cette semaine seulement.

**EP154** · vedette **La Fraise** · décor PASS · texte « MENU MIDI QUINZE »
Scène : le menu du midi en quinze secondes. Midi. Quinze secondes.

**EP155** · vedette **Don Citrone** · décor PASS · texte « PLAT REVIENT »
Scène : le plat qui revient. Vous l'avez réclamé.

**EP156** · vedette **Tomate Man** · décor PASS · texte « DESSERT QU'ON NE »
Scène : le dessert qu'on ne montre jamais. Ce que tu ne vois jamais.

**EP157** · vedette **La Betterave** · décor SALLE DU SOIR · texte « ÉVÉNEMENT RESTO »
Scène : un événement au resto. Vendredi 12, ici.

**EP158** · vedette **Le Brocoli** · décor SALLE DU SOIR · texte « DIFFUSE MATCH »
Scène : on diffuse le match. On diffuse le match.

**EP159** · vedette **Don Citrone** · décor SALLE DU SOIR · texte « FÊTEZ VOTRE ANNIVERSAIRE »
Scène : fêtez votre anniversaire ici. C'est ton anniversaire.

**EP160** · vedette **La Betterave** · décor SALLE DU SOIR · texte « SOIRÉE THÈME »
Scène : la soirée à thème. Un soir, une cuisine.

**EP161** · vedette **La Pomme de Terre** · décor SALLE DU SOIR · texte « BRUNCH DIMANCHE »
Scène : le brunch du dimanche. Dimanche, on ouvre à dix heures.

**EP162** · vedette **Le Brocoli** · décor SALLE DU SOIR · texte « PRIVATISER SALLE »
Scène : privatiser la salle. Toute la salle, rien que vous.

**EP163** · vedette **L'Oignon** · décor RÉSERVES · texte « SIX HEURES MATIN »
Scène : six heures du matin. Six heures du matin.

**EP164** · vedette **L'Oignon** · décor RÉSERVES · texte « PRODUCTEUR »
Scène : le producteur. À cinquante kilomètres d'ici.

**EP165** · vedette **Le Navet** · décor RÉSERVES · texte « PORTRAIT D'UN SERVEUR »
Scène : portrait d'un serveur. Elle t'accueille depuis quatre ans.

**EP166** · vedette **Tomate Man** · décor RÉSERVES · texte « COUP FEU VU »
Scène : le coup de feu, vu de la cuisine. Vingt heures quinze.

**EP167** · vedette **Le Navet** · décor RÉSERVES · texte « POSTE QU'ON NE »
Scène : le poste qu'on ne montre jamais. Le poste qu'on ne montre jamais.

**EP168** · vedette **L'Oignon** · décor RÉSERVES · texte « COURSES CHEF »
Scène : les courses du chef. Six heures, au marché.

**EP169** · vedette **La Fraise** · décor TABLE · texte « L'AVIS QU'ON AFFICHE »
Scène : l'avis qu'on affiche. On lit tout. Même celui-là.

**EP170** · vedette **Don Citrone** · décor TABLE · texte « CLIENT MARDI »
Scène : le client du mardi. Même table depuis six ans.

**EP171** · vedette **La Pomme de Terre** · décor TABLE · texte « TABLE DOUZE »
Scène : la table de douze. Douze personnes, une addition.

**EP172** · vedette **Le Brocoli** · décor TABLE · texte « JE COMMANDE DEPUIS »
Scène : je commande depuis mon canapé. Je commande depuis mon canapé.

**EP173** · vedette **La Carotte** · décor TABLE · texte « GLUTEN STRESS »
Scène : sans gluten, sans stress. Sans gluten. Vraiment.

**EP174** · vedette **La Pomme de Terre** · décor TABLE · texte « PREMIER RENDEZ VOUS »
Scène : le premier rendez-vous. Premier rendez-vous.

**EP175** · vedette **L'Ail** · décor DEVANTURE · texte « QR CODE TABLE »
Scène : le qr code à table. Scanne, commande, c'est tout.

**EP176** · vedette **L'Ail** · décor DEVANTURE · texte « CARTE CHANGE SAISON »
Scène : la carte change de saison. La carte change lundi.

**EP177** · vedette **Le Navet** · décor DEVANTURE · texte « RECRUTE »
Scène : on recrute. On recrute. Voilà la vérité.

**EP178** · vedette **La Betterave** · décor DEVANTURE · texte « EMPORTER ÇA REFROIDISSE »
Scène : à emporter, sans que ça refroidisse. Chaud à l'arrivée.

**EP179** · vedette **La Carotte** · décor DEVANTURE · texte « JOUR FERMETURE »
Scène : le jour de fermeture. Fermé le lundi.

**EP180** · vedette **La Carotte** · décor DEVANTURE · texte « AN RESTAURANT »
Scène : un an de restaurant. Un an. Les vrais chiffres.

---

## Contrôle avant de rendre la main

- 30 fichiers dans `public/vignettes/`, EP151 à EP180, tous en couleur ;
- 30 `posterUrl` mis à jour, aucun autre champ touché ;
- le bandeau est bleu #03A9F5 à texte blanc sur les trente, jamais crème ;
- chaque végé-fruité est identique à son image de référence ;
- les trois épisodes d'un même personnage montrent trois scènes différentes ;
- aucune vignette des saisons 1 à 5 n'a bougé.
