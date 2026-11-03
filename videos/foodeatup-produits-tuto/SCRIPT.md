# Tutoriel — Créer ses produits FoodEatUp

Dossier Drive « Configuration de ces produits ». Durée livrée : **43,8 s** —
H.264 High/yuv420p, AAC 48 kHz stéréo, faststart. Audio : true peak **-7,3 dBFS**.
Decode 0 erreur, moov avant mdat (faststart confirmé).

## Ce que montre le rush (et ce qu'il ne montre pas)

Le rush montre la création d'UN produit prêt-à-vendre (« Pâte de piment fermentée ») :
photo, nom, description, catégorie, quantité, TVA, prix HT. **Aucune UI d'affiliation à
une recette ou à des ingrédients n'apparaît à l'écran** (confirmé aussi côté MCP :
`create_product` n'expose que name/price_by_unit/unit/stock_quantity/description/
is_promotion — pas de champ recette/ingrédient). Michael a expliqué par message la
logique métier plus large :

- un produit peut être **prêt-à-vendre sans recette** (ex. un moelleux au chocolat
  acheté déjà préparé) → la liste de courses ajoute alors **le produit lui-même** ;
- ou un produit peut être **affilié à une recette** (ex. un moelleux au chocolat maison)
  → la liste de courses ajoute alors **les ingrédients de la recette**.

Cette logique n'est pas visible dans ce rush : elle est documentée dans l'astuce du
chef côté Lovable plutôt qu'inventée à l'écran, même principe que sur fournisseurs et
ingrédients.

## Voix off (9 lignes)

| # | Texte | Durée | Segment |
|---|---|---:|---|
| N0 | Créer un produit sur FoodEatUp, en quelques clics. | 2,95 s | intro |
| N1 | Cliquez sur Nouveau produit pour commencer. | 2,12 s | clic Nouveau produit |
| N2 | Ajoutez une photo, un nom et une description. | 2,59 s | C — photo/nom/description |
| N3 | Choisissez sa catégorie, sa quantité, sa TVA et son prix. | 3,47 s | D — catégorie/quantité/TVA/prix |
| N4 | Cliquez sur Ajouter : votre produit apparaît aussitôt dans le catalogue. | 4,08 s | clic Ajouter → succès |
| N5 | Vos produits alimentent directement votre liste de courses, selon votre stock et vos recettes. | 5,04 s | F — résultat (bénéfice, précision de Michael) |
| N6 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | 4,41 s | étages 1+2 (réutilisé) |
| N7 | Collez-le dans la conversation : votre produit est créé en quelques secondes. | 4,02 s | étage 3 |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (CTA, réutilisé) |

N6/N8 réutilisés tels quels depuis `foodeatup-tva-tuto/vo/` (texte générique — zéro
crédit ElevenLabs dépensé).

## Découpage

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 3,00 s | CRÉER SES PRODUITS |
| A | 0,20 → 2,00 | 2,50 s | liste « Produits », catégories, 0 produit |
| B | 2,00 → 2,35 | 0,90 s | **zoom-punch** sur Nouveau produit (1671, 306) |
| C | 3,00 → 24,00 | 6,00 s | photo, nom « pâte de piment fermentée », description |
| D | 24,00 → 44,00 | 6,00 s | catégorie « Fruits et légumes », quantité 15, TVA 8%, prix 6,50€ |
| E | 44,00 → 44,35 | 0,90 s | **zoom-punch** sur Ajouter (1683, 605) |
| F | 44,50 → 59,60 | 6,00 s | toast « Succès ! » + carte produit dans le catalogue |
| claude1 | carte générée | 6,00 s | reveal — prompt en gros, fond crème |
| claude2 | carte générée | 3,00 s | confirmation « Copié dans le presse-papiers ! » |
| claude3 | carte générée | 6,00 s | mockup chatbot Claude |
| outro | carte | 6,20 s | CTA |

Coordonnées mesurées par seuillage colorimétrique sur les frames réelles.
Étages Claude élargis (vs. défaut [2.20,1.30,2.50]) pour absorber la dérive de N5/N6
sans la répercuter — vérifié par simulation puis à l'image (t=27s → reveal, t=33s →
mockup chatbot, correctement alignés).

## Séquence Claude — module partagé

`mcp__FoodEatUp__create_product(establishment_id, name, price_by_unit, unit,
stock_quantity?, description?, is_promotion?)` existe — schéma vérifié :

> Crée le produit [nom], prix HT [prix]€, unité [unité], quantité en stock [quantité],
> pour mon établissement FoodEatUp (ID [ID établissement]).

Même texte côté fiche Lovable (`claudePrompt`).

## Animations

Mêmes principes que toute la série : Ken Burns sur les cartes, xfade (0,28 s), bandeaux
d'étape (accents restaurés partout — pas d'apostrophe, voir bug ingrédients), encadré
orange pulsant sur les 2 clics. Pas de clip avatar dans ce dossier.

## Statut publication

**Validée par Michael et publiée le 2026-08-02.** RapidoCMS : vidéo + vignette uploadées
(`foodeatup-produits-tuto-v1` / `-thumbnail`), draft LinkedIn créé et programmé le
2026-08-07 16h00. Lovable : tutoriel `creer-ses-produits` ajouté (structure
`claudePrompts[]` + `chefTipAvatar`, cohérente avec la fiche ingrédients), avec un
second prompt "photo du code-barres" demandé par Michael, en plus du prompt direct
`create_product`.
