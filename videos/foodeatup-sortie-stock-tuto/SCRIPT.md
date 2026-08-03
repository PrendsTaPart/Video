# Tutoriel — Sortir ses ingrédients du stock de la production

Module StockVision AI. Durée livrée : **51,8 s** — H.264 High/yuv420p, AAC 48 kHz
stéréo, faststart. Audio : true peak **-7,25 dBFS** (dans la marge cible du
pipeline). Decode 0 erreur, moov avant mdat (faststart confirmé).

## Ce que montre le rush (51,8 s de source, 1920x828)

Validation complète d'une production (« Dragon Roll », 29 portions) via l'assistant
en 3 étapes, puis vérification de l'effet sur le stock :

1. **Mes productions** — 8 productions « Prêt à produire », cartes recette/plat avec
   portions planifiées, date et ingrédients manquants.
2. **Valider la production** → modal, étape 1 **Quantités** : quantité planifiée 29 →
   quantité produite 29, efficacité 100 %.
3. Étape 2 **Contrôle HACCP** : température de contrôle 63 °C (badge « Conforme HACCP
   ≥ 63 °C »), contrôle qualité OK, contrôle hygiène Conforme, notes de production.
4. Étape 3 **Confirmation** : récapitulatif complet + bandeau « En validant, le stock
   sera mis à jour automatiquement et la production passera en historique HACCP » →
   **Confirmer et valider**.
5. Retour à la liste : le compteur passe de **8 à 7** productions prêtes.
6. Menu **StockVision AI → Stocks** → bouton **Mouvement de stock**.
7. **Mouvements de Stock** : une ligne **Sortie** par ingrédient consommé (Riz à sushi
   5800 g, Algues nori 58 unités, Anguille grillée 1450 g, Sauce teriyaki 870 ml,
   Avocat 2320 g…), motif « Production: Dragon Roll », plus une ligne **Entrée** de
   29 portions de Dragon Roll (« Production terminée »).
8. **Détails du Mouvement** d'une sortie (Riz à sushi, Sortie, 5800 g, date, utilisateur).

C'est le cœur du tutoriel : le restaurateur ne saisit **aucune sortie de stock à la
main** — valider la production déstocke les ingrédients de la recette et enstocke le
produit fini, avec traçabilité complète.

## Voix off (10 lignes)

| # | Texte | Durée | Segment |
|---|---|---:|---|
| N0 | Sortir ses ingrédients du stock sur FoodEatUp : c'est automatique. | 3,58 s | intro |
| N1 | Sur une production prête, cliquez sur Valider la production. | 3,00 s | A + clic B |
| N2 | Étape 1 : confirmez la quantité réellement produite, l'efficacité se calcule toute seule. | 5,15 s | C |
| N3 | Étape 2 : saisissez la température de contrôle, la qualité et l'hygiène. | 4,44 s | D |
| N4 | Étape 3 : vérifiez le récapitulatif, puis confirmez et validez. | 4,13 s | E + clic F |
| N5 | Le stock est mis à jour tout seul, et la production passe en historique HACCP. | 5,04 s | G |
| N6 | Dans Gestion des stocks, chaque ingrédient sorti est tracé, avec le motif de la production. | 5,25 s | H + clic I + J |
| N7 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | 4,41 s | étages 1+2 (réutilisé) |
| N8 | Collez-le dans la conversation : votre production est validée et votre stock ajusté en quelques secondes. | 5,56 s | étage 3 |
| N9 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (CTA, réutilisé) |

N7/N9 réutilisés tels quels depuis `foodeatup-tva-tuto/vo/` (N6/N8 là-bas — texte
générique, zéro crédit ElevenLabs dépensé). N8 est **spécifique** à ce tutoriel
(nomme la production et le stock), conformément à la règle du workflow.

## Découpage

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 4,20 s | SORTIR SES INGRÉDIENTS DU STOCK |
| A | 0,50 → 4,60 | 2,60 s | Mes productions, 8 prêtes à produire |
| B | 4,85 → 5,20 | 0,90 s | **zoom-punch** sur Valider la production (734, 662) |
| C | 5,60 → 10,10 | 4,80 s | étape 1 — quantité planifiée 29 → produite 29, efficacité 100 % |
| D | 11,00 → 19,20 | 5,00 s | étape 2 — température 63 °C conforme, qualité OK, hygiène conforme |
| E | 19,40 → 22,45 | 3,20 s | étape 3 — récapitulatif + bandeau « stock mis à jour automatiquement » |
| F | 22,50 → 22,85 | 0,90 s | **zoom-punch** sur Confirmer et valider (1216, 680) |
| G | 28,50 → 34,00 | 5,40 s | retour liste, compteur 8 → 7 |
| H | 34,20 → 39,60 | 2,80 s | menu StockVision AI → Stocks → Gestion des stocks |
| I | 39,75 → 40,10 | 0,90 s | **zoom-punch** sur Mouvement de stock (1378, 356) |
| J | 41,00 → 47,00 | 4,40 s | Mouvements de Stock — Sorties « Production: Dragon Roll » + Entrée 29 portions |
| K | 47,60 → 51,60 | 2,80 s | Détails du Mouvement (Riz à sushi, Sortie, 5800 g) |
| claude1 | carte générée | 3,40 s | reveal — prompt en gros, fond crème |
| claude2 | carte générée | 2,40 s | confirmation « Copié dans le presse-papiers ! » |
| claude3 | carte générée | 6,00 s | mockup chatbot Claude |
| outro | carte | 6,17 s (auto-étendue) | CTA |

Coordonnées des 3 boutons relevées sur les frames réelles (espace source 1920x828).
Bandeaux d'étape vérifiés sans apostrophe avant build (piège `drawtext`, voir
ingrédients) — assertion ajoutée dans `banner()` pour bloquer le cas à l'avenir.

## Calage voix/image

Dérive maximale 1,93 s (N6), volontairement absorbée plutôt que forcée à zéro : chaque
ligne a été vérifiée segment par segment sur les offsets réels imprimés par `build.py`.

- N4 démarre sur E (récapitulatif) et se termine sur le clic F « Confirmer et valider ».
- N5 couvre G (liste rafraîchie) et déborde ~1,9 s sur le début de H (ouverture du menu).
- N6 démarre en fin de H, court sur le clic I puis sur J (le tableau des mouvements) —
  c'est exactement l'image que la ligne décrit.
- N7 est audible sur les étages 1 et 2, N8 sur l'étage 3 seul (étages élargis à
  3,40 / 2,40 / 6,00 s pour absorber la dérive sans la répercuter).

## Séquence Claude — module partagé

`mcp__FoodEatUp__validate_production(establishment_id, production_id,
produced_quantity, temperature_log?, notes?)` existe — schéma vérifié : il couvre
exactement les 3 étapes du modal (quantité produite, température HACCP, notes) et
sa description confirme « met à jour le stock automatiquement ».

> Valide la production [nom de la recette] (ID [ID production]) avec [quantité]
> portions réellement produites et une température de contrôle de [température]
> degrés, pour mon établissement FoodEatUp (ID [ID établissement]).

« degrés » écrit en toutes lettres plutôt que `°C` — cohérent avec le rendu PIL et
sans risque de casse d'encodage dans le prompt copié-collé.

Second prompt côté fiche Lovable (`claudePrompts[]`, même logique que ingrédients et
produits) : `get_production_ingredients` pour contrôler les ingrédients manquants
**avant** de lancer la production (les cartes du rush affichent « 6 ingrédient(s)
manquant(s) »).

## Animations

Mêmes principes que toute la série : Ken Burns sur les cartes, xfade (0,28 s),
bandeaux d'étape, encadré orange pulsant sur les 3 clics. Pas de clip avatar dans
ce dossier.

## Statut publication

Vidéo livrée à Michael et publiée sur le site Lovable (FoodEatUp Academy) à sa
demande explicite dans le même message. Pas de programmation LinkedIn sur cette
vidéo (non demandée).
