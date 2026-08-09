# 01 — BIBLE PERSONNAGES
## Traits canoniques VERROUILLÉS — La Brigade Végéfruitée

---

## Règle d'or de la cohérence

Seedance verrouille l'identité par **image de référence**, pas par texte. Mais la doc Higgsfield impose ce qu'on appelle le **« double-bind »** : il faut *à la fois* joindre l'image de référence *et* redécrire le personnage en texte dans le prompt. Sinon le modèle hallucine des traits.

D'où le protocole en 3 temps, à faire **une seule fois** puis à réutiliser pour toute la série :

```
Étape A — générer les portraits canoniques (RapidoCMS generate_image)
Étape B — les valider + les uploader dans la bibliothèque RapidoCMS
Étape C — les joindre comme références Seedance AVANT d'écrire le prompt
          (les références passent en premier, jamais après)
```

⚠️ **Ne jamais régénérer un portrait canonique validé.** Si un épisode a besoin d'une nouvelle pose, on repart du portrait via `images_to_image`, jamais de zéro.

---

## Cast de l'épisode 1

### 🍅 TOM ATEMAN — le chef
**Rôle :** patron, straight man, celui qui prend le contrôle
**Module :** briefing du jour / tableau de bord

| Trait | Valeur VERROUILLÉE |
|---|---|
| Corps | Tomate mûre, peau rouge profond brillante, subsurface scattering doux, calice vert 5 branches sur le dessus |
| Yeux | Grands, expressifs, cartoon, iris marron |
| Accessoire 1 | Lunettes de vue fines, rectangulaires, monture noire |
| Accessoire 2 | Casquette blanche portée **à l'envers** |
| Tenue | Veste de chef blanche ouverte, manches retroussées |
| Membres | Bras et jambes fins, style cartoon, mains à 4 doigts |
| Taille | ~ taille d'un enfant de 6 ans par rapport à la cuisine |
| Voix (ElevenLabs) | Masculine, 30 ans, posée, chaleureuse, débit normal |
| Signature de jeu | Ne cligne pas des yeux quand il est calme. Un doigt levé avant chaque décision. |

*Verbatim 2021 conservé :* « J'ai 27 ans, je suis plutôt beau gosse, et assez cultivé. Je passe partout et m'adapte à tout. »

---

### 🥔 MAMA BATATA — la manager
**Rôle :** fait douze choses en même temps, ne délègue rien
**Module :** RH, planning, contrats, congés

| Trait | Valeur VERROUILLÉE |
|---|---|
| Corps | Pomme de terre allongée, peau beige-doré mate, petits « yeux » de tubercule visibles |
| Yeux | Doux, cernés légers |
| Accessoire 1 | Sac à main porté au bras **en permanence, même en cuisine** |
| Accessoire 2 | Téléphone coincé entre l'épaule et la joue |
| Tenue | Tablier bistro bordeaux, torchon à la ceinture |
| Voix | Féminine, 35-40 ans, douce, débit rapide, légèrement essoufflée |
| Signature de jeu | Ne pose jamais rien. Tient toujours 3 objets. |

---

### 🥕 ROTT-K LA CAROTTE — l'hygiène
**Rôle :** rabat-joie qui a toujours raison
**Module :** HACCP, relevés T°, DLC, traçabilité

| Trait | Valeur VERROUILLÉE |
|---|---|
| Corps | Carotte orange vif, fanes vertes touffues sur le dessus |
| Yeux | Mi-clos, sceptiques |
| Accessoire 1 | Long collier en bois style bohème |
| Accessoire 2 | Sonde de température dans la poche poitrine + calepin |
| Tenue | Blouse blanche courte, charlotte parfois |
| Voix | Féminine, 40-45 ans, douce mais coupante, articulation nette |
| Signature de jeu | Regarde la caméra une demi-seconde après chaque désastre. |

---

### 🥦 BRO LE BROCOLI — l'analyste *(personnage-clé)*
**Rôle :** parle une seule fois par épisode. Sa réplique déclenche le retournement.
**Module :** BI / analytics / PrediBot

| Trait | Valeur VERROUILLÉE |
|---|---|
| Corps | Brocoli vert, tête en fleurettes denses, tige claire |
| Yeux | Calmes, grands, très peu de clignements |
| Accessoire 1 | Casque audio over-ear bleu `#147AFF` autour du cou |
| Accessoire 2 | Tablette tenue à deux mains, écran bleu |
| Tenue | Sweat gris uni, capuche baissée |
| Voix | Féminine, 25 ans, neutre, calme, presque monocorde — **contraste total avec le chaos** |
| Signature de jeu | Immobile pendant que tout bouge. **Toujours éclairée en bleu par son écran.** |

> Sa réplique unique finit **toujours** par une question ouverte. C'est la marque de fabrique reprise de la fiche 2021.

---

### 🧄🧅 AIL & OIGNON — les livreurs
**Rôle :** râlent, sentent mauvais, indispensables
**Module :** fournisseurs, stocks, réappro, ruptures

| Trait | Valeur VERROUILLÉE |
|---|---|
| Oignon | Bulbe jaune-orangé, pousses vertes hautes, sourcils froncés en permanence, **grand** |
| Ail | Tête d'ail blanche nacrée, visage espiègle, joues roses, **petit** (moitié de la taille d'Oignon) |
| Accessoire commun | Sacoche banane marron ringarde + gilet réfléchissant jaune |
| Accessoire Oignon | Bon de livraison chiffonné |
| Voix | Oignon : masculine, grave, rauque, agacée. Ail : masculine, aiguë, rapide, moqueuse |
| Signature de jeu | Ne sont **jamais** dans le même cadre à moins de 50 cm l'un de l'autre. |

---

### 🍓 FIRASE LA FRAISE — la com
**Rôle :** filme tout, ne vend rien
**Module :** campagnes, avis clients, réseaux

| Trait | Valeur VERROUILLÉE |
|---|---|
| Corps | Fraise rouge brillante, akènes jaunes visibles, collerette verte |
| Accessoire | Smartphone en perche, toujours en mode selfie |
| Tenue | Veste crop rose pâle, barrette |
| Voix | Féminine, 22 ans, aiguë, enthousiaste, débit très rapide |
| Signature de jeu | Le smartphone entre dans le cadre avant elle. |

---

### 🍠 NAVY LE NAVET — le narrateur
**Rôle :** **casse le 4ᵉ mur.** Voix off de toute la série. Porte le CTA.
**Module :** la voix de la marque

| Trait | Valeur VERROUILLÉE |
|---|---|
| Corps | Navet blanc et violet, fanes vertes courtes |
| Accessoire | Serviette de sport autour du cou + chrono |
| Tenue | Débardeur gris |
| Voix | Masculine, 32 ans, **grave**, complice, ton de documentaire pince-sans-rire |
| Signature de jeu | Le seul personnage autorisé à regarder l'objectif plus d'une seconde. |

*Repris directement de votre scénario 2021, où Navy rattrape déjà la caméra qui s'éloigne.*

---

### 🫐 BETTERAVE — le runner
**Rôle :** vitesse, chaos, gag visuel. **Efface le CTA à la fin de chaque épisode.**
**Module :** salle, réservations, KDS

| Trait | Valeur VERROUILLÉE |
|---|---|
| Corps | Betterave rouge-pourpre en forme de goutte, **très petit** |
| Accessoire | Trottinette + plateau de service tenu d'une main |
| Voix | Masculine, jeune, aiguë, débit ultra rapide |
| Signature de jeu | Traverse toujours l'écran de **droite à gauche**. |

> Gag de fin repris à l'identique de votre scénario 2021 (où c'était Courge). Il passe assez bas pour effacer la phrase **sans effacer le logo**.

---

### 🍋 DON CITRONE — le client
**Rôle :** toujours pressé, jamais content. Pont avec le flyer citron déjà produit.
**Module :** commande en ligne, fidélité

| Trait | Valeur VERROUILLÉE |
|---|---|
| Corps | Citron jaune vif, deux feuilles vertes, **identique au flyer existant** |
| Accessoire | Montre au poignet qu'il regarde toutes les 2 secondes |
| Voix | Masculine, 50 ans, impatiente, débit saccadé |

---

## Ce qui est VARIABLE d'un épisode à l'autre

Tout le reste ci-dessus est verrouillé. Ne varient jamais que :

- **le décor** (cuisine / salle / réserve / quai de livraison / bureau)
- **l'heure et la lumière** (aube froide → cuivre chaud → bleu nuit)
- **l'action et l'émotion**
- **le cadre et le mouvement de caméra**
- **les accessoires de scène** (pas les accessoires de personnage)

C'est la séparation *canon verrouillé / axes de scène variables* qui permet de tenir 9 épisodes sans dérive visuelle.

---

## Interdits absolus dans tous les prompts

- ❌ Aucun nom de film, studio d'animation, réalisateur ou artiste vivant
- ❌ Aucune marque tierce visible (logos de fournisseurs, concurrents)
- ❌ Aucun visage humain photoréaliste
- ❌ Aucun chiffre de performance non sourcé à l'écran
- ❌ Aucune allégation santé (on est en B2B logiciel, pas en nutrition)
