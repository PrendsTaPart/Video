# Prompts Higgsfield — plans verticaux à générer (9:16)

Ce sont les **seuls plans qui me manquent** pour finir le film. Tout le reste est déjà
monté (maquettes d'interface, cartes de marque, sous-titres, musique).

> **Rappel de la règle du dépôt** (`CLAUDE.md`) : je ne génère rien moi-même. Ces prompts
> sont à coller dans l'interface Higgsfield. Modèle **Seedance 2.5**, comme le reste de ta
> bibliothèque.

## Réglages communs

| Paramètre | Valeur |
|---|---|
| Modèle | Seedance 2.5 |
| Format | 9:16 vertical · 1080×1920 · 24 im/s |
| Durée | 10 s |
| Reference Elements | voir la colonne « Perso. » de chaque plan |

**Personnages déjà enregistrés dans ton workspace** (à sélectionner dans l'interface, ou
via le placeholder `<<<id>>>` si tu passes par l'API) :

| Rôle | Nom de l'élément | ID |
|---|---|---|
| Chef | `chef-hero` | `c841147a-6375-4c5e-b146-e45c1cab7e99` |
| Serveuse | `serveur-hero` | `a8f9dfa9-47cf-4ba3-86f8-93ab0b4a11c1` |
| Gérant | `directeur-hero` | `2f3b8e65-a41d-429a-abf7-5df04baddf7a` |

**Bloc de style à mettre en tête de chaque prompt** (repris de tes prompts existants, avec
deux contraintes de cadrage ajoutées pour le montage vertical) :

```
Vertical 9:16, 10 secondes, 1080p, 24 im/s. PAS de texte incrusté, PAS de sous-titres,
PAS de filigrane, PAS de logo, AUCUNE légende gravée dans l'image, AUCUNE marque tierce
identifiable, AUCUN écran affichant une interface lisible.
Style : documentaire publicitaire photoréaliste, grain fin, caméra portée douce,
profondeur de champ courte, lumière naturelle. Pas de rendu 3D, pas d'aspect banque d'images.
CADRAGE : l'action utile tient dans le tiers central de l'image. Le tiers bas reste dégagé
(sous-titres incrustés au montage) et le haut du cadre reste calme (incrustations d'interface).
Un seul personnage visible, jamais de doublon ni de silhouette en arrière-plan.
```

---

## Scène 1 — l'accroche (4 plans, ambiance froide et saturée)

**P1 · Le pass qui déborde** — Perso. : `chef-hero`
```
Cuisine professionnelle en plein service, 12 h 30. Pass en inox saturé : des tickets de
commande froissés accrochés à un rail, trois tablettes allumées côte à côte sur une
étagère, un téléphone qui vibre sur le plan de travail. Le chef est au milieu, il tend la
main vers le téléphone, se ravise, attrape un ticket. Caméra portée à hauteur de poitrine,
légère dérive latérale. Fin de plan : il reste immobile deux secondes, dépassé.
```

**P2 · Le téléphone qui déborde** — Perso. : aucun
```
Plongée verticale stricte sur un téléphone posé à plat sur un comptoir en zinc, personne
dans le cadre. Des pastilles de notification s'allument les unes après les autres, en
désordre, jusqu'à saturer l'écran. Caméra strictement fixe. Fin de plan : l'écran reste
allumé, saturé. Aucun texte lisible, aucune icône de marque identifiable.
```

**P3 · Les DLC à la main** — Perso. : `chef-hero`
```
Le chef, veste blanche, écrit des dates de péremption à la main dans un carnet à spirale
posé sur un plan de travail en inox. Expression fatiguée, résignée. Il referme le carnet,
regarde brièvement hors champ. Caméra portée en légère plongée sur le carnet, puis remontée
lente vers son visage. Lumière froide de cuisine. Rien de lisible sur les pages.
```

**P4 · Le gérant tard le soir** — Perso. : `directeur-hero`
```
Petit bureau de restaurant, tard le soir, une seule lampe allumée. Le gérant en chemise
bleu clair est assis devant un ordinateur portable, le visage éclairé par l'écran ; il
passe d'une fenêtre à l'autre, se frotte les yeux, s'adosse à sa chaise. Caméra fixe en
légère contre-plongée depuis l'autre côté du bureau. Écran jamais lisible, aucune interface
reconnaissable.
```

## Scène 2 — la respiration

**P5 · Il souffle** — Perso. : `directeur-hero`
```
Le gérant sort de la salle, s'adosse au mur d'un couloir de service, souffle, s'assied deux
secondes sur un tabouret et sort son téléphone de sa poche. Le brouhaha du service reste en
arrière-plan flou. Caméra portée qui l'accompagne puis s'immobilise. Bascule progressive
d'une lumière froide vers une lumière plus chaude pendant le plan. Écran du téléphone
éteint ou hors champ.
```

## Scène 5 — le pilotage depuis le téléphone

**P6 · Détendu, il tape un message** — Perso. : `directeur-hero`
```
Le gérant, détendu, adossé au comptoir d'une salle en fin de service, tape un message sur
son téléphone à deux pouces, esquisse un sourire, relève la tête. Cadrage taille, il occupe
le tiers central, le téléphone bien visible mais l'écran ÉTEINT (aucune interface affichée).
Caméra fixe, très légère respiration. Lumière chaude de fin de journée.
```
> L'écran doit rester éteint : la conversation WhatsApp est incrustée au montage.

## Scène 6 — les tomates (le clou du spot)

**P7 · La cagette de tomates** — Perso. : `chef-hero`
```
Le chef ouvre la porte d'une chambre froide, un souffle de vapeur s'échappe. Il en ressort
avec une cagette de tomates grappe bien mûres, la pose sur un plan de travail en inox et
en prend une dans la main. Caméra portée qui le suit de trois quarts, puis descend sur la
cagette. Lumière froide de réserve qui bascule vers la lumière chaude de la cuisine.
```

**P8 · Macro tomates** — Perso. : aucun
```
Macro sur des tomates grappe posées sur un plan de travail en inox, gouttes d'eau,
lumière chaude rasante, très faible profondeur de champ. Lent panoramique latéral de
quelques centimètres. Aucune main, aucun personnage, aucun texte.
```

## Scène 7 — la sérénité retrouvée

**P9 · L'accueil en salle** — Perso. : `serveur-hero`
```
Salle de bistrot en service du soir, pleine mais calme, plusieurs tables occupées. La
serveuse en chemise noire et demi-tablier marine accueille un client à l'entrée, échange un
sourire, l'installe à une table. Caméra portée qui les suit à distance respectueuse.
Lumière chaude, ambiance sereine. Visages des clients de dos ou flous.
```

**P10 · Le chef repose une assiette et sourit** — Perso. : `chef-hero`
```
Le chef pose une assiette dressée au pass, recule d'un pas, regarde la salle par le passe
et sourit franchement, puis retourne à son plan de travail. Caméra fixe cadrée sur le pass,
courte profondeur de champ. Lumière chaude de lampe chauffante. Aucun écran allumé dans le
cadre.
```

---

## Ordre de priorité

Si tu ne veux en générer qu'une partie, commence par ces quatre — ce sont ceux qui portent
le film : **P1** (l'accroche), **P5** (la bascule), **P6** (le pilotage), **P9** (la
clôture). Les six autres ont un remplaçant acceptable dans les plans 16:9 existants,
recadrés en bandeau.

Dès que tu déposes les .mp4 dans `videos/foodeatup-prospect-9x16/assets/hf/`, je remplace
les bandeaux recadrés par les plans natifs — le reste du montage ne bouge pas.
