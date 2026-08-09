# FoodEatUp — Série TikTok « Cas concrets »
## 10 vidéos : problème chiffré → solution en images → résultat → punchline

Plan complet, vérifié contre le Drive (`1LpWivm0KEPwX5XhNHiw08426NjT6PXHC`) et contre la
bibliothèque Higgsfield déjà générée (`hero-video/assets/video/`), le 2026-08-09.

**Mise à jour 2026-08-09** : les deux blocs fixes du montage (HOOK 0–3s et PUNCHLINE
33–36s) sont produits — voir `foodeatup-cas-concrets/motion/` (projet HyperFrames,
`renders/hook-intro.mp4` instancié sur le hook vidéo 1, `renders/punchline-outro.mp4`
identique sur les 10 vidéos, thumbnail TikTok dans `motion/thumbnail/`). Assets de marque
fournis par Michael (logo mascotte, mark "8", logo carte bleue, photo réelle du chef) —
déjà présents dans le dépôt (`studio-video/assets/brand/`), rien de nouveau à ajouter.
Détail et ce qui reste à trancher : `foodeatup-cas-concrets/motion/README.md`.

---

## Le format

Chaque vidéo suit exactement la même mécanique, ~36 secondes, vertical 9:16 :

```
0 – 3 s    HOOK          Un chiffre qui pique. Texte plein cadre + plan court.
3 – 11 s   LE PROBLÈME   Généré sur Higgsfield (ou réutilisé, voir règle ci-dessous). 8 s. Muet, ambiance seule.
11 – 25 s  LA SOLUTION   Capture écran FoodEatUp récupérée du Drive. 14 s.
25 – 33 s  LE RÉSULTAT   Avatar HeyGen face caméra. 8 s. Il parle.
33 – 37 s  PUNCHLINE     Carton logo. 4 s (voir ci-dessous).
```

**Pourquoi ce découpage marche sur TikTok** : le hook chiffré arrête le pouce, le problème
crée l'identification, la capture écran apporte la preuve — c'est le seul moment où on
montre le produit —, et l'avatar humanise la conclusion. Aucun de ces quatre blocs n'est
décoratif.

**Punchline fixe sur les 10** (mise à jour 2026-08-09, produite dans
`foodeatup-cas-concrets/motion/`) :

> FoodEatUp.
> Avant. Pendant. Après le service.
> Plus de chiffre. Moins de gaspillage.

Distillée du positionnement complet de Michael (« le logiciel qui gère ton resto avant
pendant et après le service et qui fait communiquer les données pour augmenter ton chiffre
d'affaires et réduire ton gaspillage et optimiser ton équipe tout en gérant tes ventes et
ton HACCP ») — gardé : le cycle complet (avant/pendant/après) qui est la promesse la plus
différenciante et la plus courte à dire, et les deux résultats les plus chiffrables
(chiffre d'affaires ↑, gaspillage ↓). Volontairement coupé de la punchline : équipe
optimisée, ventes et HACCP gérés — ces bénéfices-là sont déjà **prouvés par les vidéos
elles-mêmes** (la vidéo 5 démontre l'équipe, la vidéo 6 démontre HACCP, etc.), la punchline
n'a donc pas besoin de les redire, elle doit rester courte pour s'installer en étant répétée
dix fois. Si les cinq bénéfices doivent absolument être dans le carton final, dis-le et je
rallonge.

---

## Règle du dépôt : Higgsfield en dernier recours

`CLAUDE.md` interdit de générer de nouveaux plans via l'API/MCP Higgsfield. Avant d'écrire
un prompt à générer, ce plan a donc été confronté à la bibliothèque déjà produite dans
`hero-video/assets/video/` (17 plans, personnages Karim/Léa/Marc cohérents via Reference
Elements Higgsfield, voir `hero-video/data/hero.json → characters`). Résultat :

- **2 vidéos peuvent réutiliser un plan existant tel quel** (vidéos 6 et 10, détail plus
  bas) — aucun appel Higgsfield nécessaire.
- **8 vidéos n'ont pas d'équivalent dans la bibliothèque** (la mise en scène demandée est
  trop spécifique : poubelle de gaspillage, téléphone qui sonne dans le vide, planning
  raturé un dimanche soir, assiette amputée d'une part, etc.). Pour celles-ci, le prompt
  Higgsfield est fourni **à donner à l'utilisateur pour génération manuelle dans
  l'interface Higgsfield** — ce dépôt n'appelle pas l'API.

Si tu génères ces 8 plans manuellement, utilise en Reference Element le **character sheet
du chef Karim** déjà utilisé sur `hero-video` (`referenceElementId:
c841147a-6375-4c5e-b146-e45c1cab7e99`, voir `hero-video/assets/image/characters/chef-character-sheet.png`)
plutôt que d'en recréer un nouveau : ça garde le même visage sur l'ensemble de la
bibliothèque FoodEatUp (site + série hero + cette série TikTok).

---

## Ce qui a été vérifié dans le Drive (2026-08-09)

Le dossier est organisé en **module → sujet → fichiers**, avec dans chaque sujet le .mp4
de démonstration, une vignette et une page de fin. Sur les 10 vidéos : **6 assets
confirmés avec nom de fichier exact**, **2 sujets existent dans le Drive mais le .mp4 n'est
pas encore tourné** (seule la vignette de couverture est présente), **2 sujets restent à
confirmer** (le module suggéré ne contient pas de contenu qui corresponde clairement au
hook). Détail vidéo par vidéo ci-dessous.

---

## Blocs constants

**BLOC HIGGSFIELD** (en tête de chaque prompt problème, quand un nouveau plan est nécessaire)

> Plan unique continu de 8 secondes, vertical 9:16, 4K, 24 images/seconde, style
> documentaire, grain fin. Palette froide et désaturée : gris #8A9099, surfaces #EDEEF0,
> encre #3A3F45. Lumière plate de néon, sans chaleur. Référence image 1 = photo du chef :
> visage, morphologie et tenue à conserver strictement à l'identique. Son d'ambiance seul,
> aucune voix, aucune musique. Aucune coupe, aucun personnage dupliqué, aucun texte à
> l'écran, aucun logo, aucune marque ni application identifiable, aucun sous-titre.

**BLOC HEYGEN** (en tête de chaque prompt résultat)

> Vidéo avatar de 8 secondes, format vertical 9:16, 1080 × 1920. Avatar : homme, la
> quarantaine, veste de cuisine blanche col ouvert, cadrage buste, regard caméra. Décor :
> cuisine professionnelle floutée en arrière-plan, tons chauds. Voix française masculine,
> ton posé et direct, débit naturel, pas de ton commercial. Sous-titres désactivés — ils
> sont ajoutés au montage. Aucun logo, aucun texte incrusté.

*Note* : le connecteur branché sur ce compte est HyperFrames, l'outil de composition.
L'avatar parlant se crée dans HeyGen Studio ; HyperFrames sert ensuite à assembler si tu
veux automatiser le montage.

---

# VIDÉO 1 — 250 couverts, 10 fidèles

**Hook (texte plein cadre) :** *250 couverts aujourd'hui. 10 clients fidèles.*
**Asset solution :** `7 - Module Marketing / 12 - BOOSTER LA FIDÉLITÉ / Créer un programme fidélité.mp4`
✅ **confirmé** (11,6 Mo, présent dans le dossier)

```
[BLOC HIGGSFIELD]
Action : fin de service, le chef debout au comptoir regarde une salle qui se vide, les
tables se libèrent une à une, les clients sortent sans un mot ni un regard vers lui. Il
reste seul devant l'entrée.
Caméra : plan fixe depuis le fond de la salle, très légère avancée.
Son : chaises, porte, brouhaha qui s'éteint.
Fin de plan : la salle vide, lui de dos.
```

*Pas d'équivalent exact dans `hero-video/assets/video/` — `hero-salle-vide-matin.mp4`
existe mais montre une salle vide générique (plan "je descends voir"), pas la scène de
clients qui partent un à un. À générer manuellement dans Higgsfield avec le prompt
ci-dessus.*

```
[BLOC HEYGEN]
Script exact : « Tu ne perds pas des clients. Tu ne les reconnais pas. Le programme se
déclenche à la première visite, et le deuxième passage arrive tout seul. »
```

---

# VIDÉO 2 — 12 kilos à la poubelle

**Hook :** *12 kilos jetés dimanche soir. Encore.*
**Asset solution :** `5- MODULE STOCKVISION AI — 20 vidéos / 3- Ma carte - Prédictions des commandes en fonction de vos ventes et production / Prédictions des commandes en fonction de vos ventes et production.mp4`
✅ **confirmé** (7,3 Mo) — un second fichier existe dans le même sous-dossier,
`Script_3_-_PRÉDIRE_SES_COMMANDES_VENTES_&_PRODUCTION.mp4` (3,5 Mo), probablement une
version script/brute : utiliser le premier.

```
[BLOC HIGGSFIELD]
Action : 23 h, le chef ouvre une poubelle de cuisine et y verse le contenu d'un bac gastro
encore plein, produits intacts. Il referme le couvercle du pied, mâchoire serrée, et
essuie ses mains sur son tablier.
Caméra : plongée fixe sur la poubelle, puis léger recul jusqu'à son visage.
Son : couvercle métallique, cuisine à l'arrêt.
Fin de plan : lui immobile devant la poubelle fermée.
```

*Pas d'équivalent dans la bibliothèque existante. À générer manuellement dans Higgsfield.*

```
[BLOC HEYGEN]
Script exact : « Trois ans de ventes, jour par jour, météo comprise. Tu produis ce que tu
vas vendre, pas ce que tu crois vendre. »
```

---

# VIDÉO 3 — 47 appels manqués

**Hook :** *47 appels manqués ce mois-ci. Combien de tables ?*
**Asset solution :** `13 - Module Caroline (Agent IA Vocale) / 2 - RÉÉCOUTER SES APPELS ET RÉSERVATIONS / réécouter ses appels et réservations.mp4`
✅ **confirmé** (18,2 Mo)

```
[BLOC HIGGSFIELD]
Action : 20 h 15, plein rush. Un téléphone vibre et sonne sur un comptoir, personne autour.
Au second plan flou, l'équipe court dans tous les sens. Le téléphone finit par s'arrêter,
l'écran s'éteint.
Caméra : gros plan fixe sur le téléphone, arrière-plan en mouvement.
Son : sonnerie insistante, service saturé, voix non intelligibles.
Fin de plan : le téléphone éteint, immobile.
```

*Pas d'équivalent dans la bibliothèque existante (`hero-video` documente lui-même un "GAP:
pas de plan répondeur dédié généré" et réemploie temporairement un autre plan). À générer
manuellement dans Higgsfield.*

```
[BLOC HEYGEN]
Script exact : « Caroline décroche à la première sonnerie. Elle prend la réservation, elle
la place, et tu la retrouves le matin. Même à minuit. »
```

---

# VIDÉO 4 — 38 € d'écart, trois soirs de suite

**Hook :** *38 euros d'écart. Trois soirs de suite.*
**Asset solution :** `11 - Module Caisse POS & Matériel / 7 - SUIVRE LES ÉCARTS CAISSE HISTORIQUE`
⚠️ **sujet présent dans le Drive mais .mp4 pas encore tourné** — seule la vignette de
couverture (`SUIVRE LES ÉCARTS CAISSE HISTORIQUE.jpg`) existe pour l'instant. Sous-dossier
voisin `6 - CLÔTURER SA CAISSE LE Z DE CAISSE` (même module) dans le même état : vignette
seule, pas de vidéo. **À reproduire cette vidéo seulement une fois l'un des deux tournages
livré**, ou à remonter avec un autre asset caisse déjà disponible en attendant.

```
[BLOC HIGGSFIELD]
Action : 1 h du matin, comptoir. Le chef recompte des pièces et des billets neutres étalés
devant lui, s'arrête, recommence depuis le début, se frotte le visage.
Caméra : macro fixe sur les mains et l'argent, puis remontée lente sur son visage fatigué.
Son : tintement de pièces, silence de salle vide.
Fin de plan : ses mains posées à plat sur la pile, immobiles.
```

*Pas d'équivalent dans la bibliothèque existante — `hero-caisse-ticket-z.mp4` montre le
geste "avec solution" (impression du ticket Z), pas le comptage manuel du problème. À
générer manuellement dans Higgsfield.*

```
[BLOC HEYGEN]
Script exact : « L'écart, tu le vois au moment où il se crée, pas trois jours après. Et le
Z se fait en quarante secondes. »
```

---

# VIDÉO 5 — Trois heures chaque dimanche

**Hook :** *3 heures chaque dimanche. Pour un planning.*
**Asset solution :** `2 - MODULE ÉQUIPE & PLANNING — 20 vidéos / 6-Affichages et impression du planning Équipe par employé ou par poste de travail / Affichages et impression du planning Équipe par employé ou par poste de travail.mp4`
✅ **confirmé** (16,9 Mo)

```
[BLOC HIGGSFIELD]
Action : dimanche 22 h, table de salon. Le chef, en tenue civile, rature un planning
imprimé, efface, recommence, repose son stylo. Derrière lui, une pièce éclairée d'où
viennent des voix, sans lui.
Caméra : plan fixe à hauteur de table, léger recul final qui révèle la pièce.
Son : intérieur calme, stylo sur papier, voix lointaines non intelligibles.
Fin de plan : lui de dos, la feuille toujours raturée.
```

*Pas d'équivalent dans la bibliothèque existante. À générer manuellement dans Higgsfield.*

```
[BLOC HEYGEN]
Script exact : « Tu déplaces deux créneaux, tu publies, chacun reçoit le sien. Cinq
minutes. Ton dimanche, tu le récupères. »
```

---

# VIDÉO 6 — Trois mois de relevés manquants

**Hook :** *Contrôle surprise. 3 mois de relevés manquants.*
**Asset solution :** `4- MODULE HACCP — 30 vidéos / 30- Retrouver et exporté les Historique du module HACCP / Retrouver et exporté les Historique du module HACCP.mp4`
✅ **confirmé** (23,7 Mo)

```
[HIGGSFIELD — RÉUTILISATION, PAS DE NOUVELLE GÉNÉRATION]
Réutiliser tel quel : hero-video/assets/video/hero-chef-carnet-dlc.mp4
```

C'est le seul plan de la bibliothèque `hero-video` qui colle presque mot pour mot au beat
demandé : dans `hero.json → S1 → s1-chef`, ce plan illustre déjà *« Les DLC, je les note
sur un carnet… je les ressaisirai ce soir, si j'y pense »*, repris en S5 pour *« Le
contrôle, c'est jeudi… je remplirai le classeur mercredi soir, de mémoire »* — exactement
le point de douleur de cette vidéo (classeur/carnet incomplet, angoisse du contrôle).
Recadrer/retimer sur 8 s au montage plutôt que d'en générer un nouveau : conforme à la
règle du dépôt (réutiliser un plan déjà généré avant d'en produire un autre).

```
[BLOC HEYGEN]
Script exact : « Dix secondes par relevé, tous les jours. Le jour du contrôle, tu sors
douze mois d'historique en trois secondes. »
```

---

# VIDÉO 7 — Un tiers de l'assiette

**Hook :** *30 % de commission. Sur chaque livraison.*
**Asset solution :** `6 - Module Mon Site`
⚠️ **à confirmer** — les 8 sous-dossiers actuels de ce module (Réservations & horaires,
Activer l'éditeur web, Ajouter du contenu pro, Connecter ton domaine, Personnaliser ton
site, Choisir ton template, Créer un site par IA, Gérer tes pages) ne contiennent pas de
sujet explicitement "commande en ligne/boutique". La fonctionnalité de commande en ligne
existe probablement plutôt côté StockVisionAI ("Ma carte" / configuration boutique, voir
Vidéo 1 de ce module dans la feuille "Plan de Formation Vidéos - StockVisionAi V2") ou dans
un module Boutique séparé pas encore drivé sous ce nom. À rouvrir manuellement avant
tournage.

```
[BLOC HIGGSFIELD]
Action : macro sur une assiette dressée avec soin ; la main du chef entre dans le cadre et
en retire une part entière d'un geste net, laissant un vide dans la composition. Il regarde
l'assiette amputée.
Caméra : macro fixe en légère plongée, puis léger recul sur son visage.
Son : couvert sur porcelaine, cuisine calme.
Fin de plan : l'assiette incomplète, immobile.
```

*Pas d'équivalent dans la bibliothèque existante. À générer manuellement dans Higgsfield.*

```
[BLOC HEYGEN]
Script exact : « Le client commande sur ton site, sur ta carte, à ton prix. La marge reste
dans ta caisse. »
```

---

# VIDÉO 8 — Le plat qui te fait perdre de l'argent

**Hook :** *Ton plat le plus vendu. 12 % de marge.*
**Asset solution :** `3- MODULE COMPTABILITÉ — 10 vidéos`
⚠️ **à confirmer** — les 10 sujets de ce module (fournisseurs, clients, devis, factures,
statuts, dépenses, e-reporting, commandes) ne couvrent pas le coût de recette / marge par
plat. Ce contenu correspond plutôt à StockVisionAI → module Configuration → *« Configuration
de ces recette et étape recette »* (Vidéo 11 de la feuille "Plan de Formation Vidéos -
StockVisionAi V2") — dossier Drive à confirmer, pas localisé avec certitude lors de cette
passe.

```
[BLOC HIGGSFIELD]
Action : le chef pose fièrement une assiette signature sous une lampe, recule d'un pas,
bras croisés, satisfait. Puis son regard se fige, il se penche vers l'assiette.
Caméra : macro sur l'assiette, recul lent jusqu'au plan poitrine.
Son : cuisine silencieuse, porcelaine.
Fin de plan : lui immobile devant l'assiette, expression qui change.
```

*Pas d'équivalent dans la bibliothèque existante. À générer manuellement dans Higgsfield.*

```
[BLOC HEYGEN]
Script exact : « Chaque recette est chiffrée à l'ingrédient près. Tu sais lequel te
nourrit, et lequel te coûte. »
```

---

# VIDÉO 9 — Dernier post : mars

**Hook :** *Dernier post Instagram : mars.*
**Asset solution :** `7 - Module Marketing / 24 - CALENDRIER IA AVEC IRIS / Visualiser le Calendrier de communication de Iris.mp4`
✅ **confirmé** (20,1 Mo) — le second dossier proposé initialement (`6 - CAMPAGNE 100% IA`)
n'existe pas sous ce nom dans le Drive actuel ; celui-ci (`24 - CALENDRIER IA AVEC IRIS`)
est le bon.

```
[BLOC HIGGSFIELD]
Action : le chef dresse une assiette magnifique et l'envoie au pass sans la photographier.
Son téléphone reste posé contre une bouteille d'huile, écran éteint, tout le long du plan.
Caméra : travelling latéral serré qui suit l'assiette, puis retour sur le téléphone éteint.
Son : cuisine en activité, assiette sur inox.
Fin de plan : le téléphone éteint au premier plan, la cuisine active derrière.
```

*Pas d'équivalent dans la bibliothèque existante. À générer manuellement dans Higgsfield.*

```
[BLOC HEYGEN]
Script exact : « Ta cuisine produit du contenu tous les jours. Iris l'écrit, le programme,
et tu valides d'un geste. »
```

---

# VIDÉO 10 — Quatre tablettes, deux commandes perdues

**Hook :** *4 tablettes. 2 commandes perdues samedi.*
**Asset solution :** `12 - Module HubRise & Livraisons / 4 - CENTRALISER LES COMMANDES FLUX LIVRAISON`
⚠️ **sujet présent dans le Drive mais .mp4 pas encore tourné** — seule la vignette de
couverture existe pour l'instant. **À reproduire une fois ce tournage livré.**

```
[HIGGSFIELD — RÉUTILISATION POSSIBLE EN ATTENDANT, PAS DE NOUVELLE GÉNÉRATION]
hero-video/assets/video/hero-serveur-trois-tablettes.mp4
```

Plan existant le plus proche : trois tablettes (Uber, livraison, salle) jonglées par le
serveur — même idée de canaux qui se chevauchent que "quatre tablettes, alertes qui se
chevauchent". Ce n'est pas un mot-à-mot (3 tablettes au lieu de 4, pas d'alertes visuelles
sur les écrans), donc à évaluer au montage : soit on l'utilise en l'état en ajustant le
hook (« 3 tablettes » au lieu de « 4 »), soit on considère que l'écart est trop grand et on
donne le prompt ci-dessous à générer manuellement.

```
[BLOC HIGGSFIELD — si le plan existant ne convient pas]
Action : quatre tablettes alignées sur une étagère de cuisine s'allument en décalé, chacune
avec sa propre alerte. Le chef se retourne de l'une à l'autre sans parvenir à suivre, puis
s'arrête net, les bras le long du corps.
Caméra : plan serré fixe sur l'étagère, puis pivot vers le chef immobile.
Son : alertes qui se chevauchent, cuisine sous tension.
Fin de plan : lui face aux quatre écrans allumés.
```

```
[BLOC HEYGEN]
Script exact : « Tous les canaux arrivent au même endroit, dans le même ordre. Un seul
écran, et plus rien ne se perd. »
```

---

## Montage — ce qu'il faut respecter

**Le recadrage des captures d'écran.** Les assets Drive sont des captures de logiciel, donc
en format horizontal. Ne les colle pas telles quelles en 9:16 avec deux bandes noires :
recadre sur la zone active et anime un lent zoom vers l'élément qui compte. Une capture qui
remplit le cadre convainc, une capture en timbre-poste ne montre rien.

**Le rythme.** 14 secondes de capture écran, c'est long pour TikTok. Coupe dans l'asset :
garde les deux ou trois gestes utiles, accélère les temps morts à 1,5×.

**Les sous-titres.** Brûlés sur toute la durée, y compris sur le passage HeyGen. Même style
sur les dix vidéos.

**Le hook.** Le chiffre doit être lisible en une demi-seconde, gros, sur fond marine. C'est
le seul moment où le texte est le sujet.

---

## État de préparation, résumé

| # | Vidéo | Asset solution | Plan « problème » |
|---|---|---|---|
| 1 | Fidélité | ✅ confirmé | à générer (Higgsfield) |
| 2 | Gaspillage | ✅ confirmé | à générer (Higgsfield) |
| 3 | Appels manqués | ✅ confirmé | à générer (Higgsfield) |
| 4 | Écart de caisse | ⚠️ .mp4 pas encore tourné | à générer (Higgsfield) |
| 5 | Planning | ✅ confirmé | à générer (Higgsfield) |
| 6 | HACCP | ✅ confirmé | ✅ **réutilise** `hero-chef-carnet-dlc.mp4` |
| 7 | Commissions livraison | ⚠️ module à confirmer | à générer (Higgsfield) |
| 8 | Marge plat | ⚠️ module à confirmer | à générer (Higgsfield) |
| 9 | Réseaux sociaux | ✅ confirmé (dossier corrigé) | à générer (Higgsfield) |
| 10 | Tablettes | ⚠️ .mp4 pas encore tourné | possible réutilisation `hero-serveur-trois-tablettes.mp4` |

## Ce que je conseille

Produis la **vidéo 1** d'abord — asset confirmé, et le cas de la fidélité est le plus
universel des dix. Elle sert de patron pour les neuf autres.

Publie-les **une par jour**, dans l'ordre : fidélité, gaspillage, appels, caisse, planning,
HACCP, commissions, marge, réseaux, livraisons. La série alterne les douleurs d'argent et
les douleurs de temps, ce qui évite l'effet catalogue.

Pour les vidéos 4 et 10, attendre que les tournages Drive correspondants soient livrés (ou
tourner en interne les deux sujets manquants) avant de les produire — inverser leur ordre
de passage avec une autre vidéo de la liste en attendant ne casse pas l'alternance
argent/temps.

Pour les vidéos 7 et 8, confirmer le bon module/sous-dossier Drive avant tournage : celui
indiqué au départ ne contient pas de sujet correspondant au hook.
