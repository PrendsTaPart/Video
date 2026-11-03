# Tutoriel — Tenir ses dépenses avec StockVision AI

Dossier Drive « Comptabilité » (module `comptabilite`). Rush fourni : 32,16 s,
1920x828 @25fps, sans son (`assets/screen.mp4`). Cartes intro/outro fournies
par Michael (`TENIR SES DÉPENSES STOCKVISION AI.jpg` / `page_fin_vid..jpg`).

## Ce que montre le rush (et ce qu'il ne montre pas)

Le rush montre le parcours **StockVision AI** (OCR de facture) de bout en bout :
depuis une livraison, import d'une facture fournisseur (PDF/JPG/PNG), analyse
automatique par l'IA (barre de progression « Analyse en cours… »), écran de
validation des produits détectés, clic sur « Valider et enregistrer », puis
consultation de la dépense créée automatiquement dans la Facturation (lignes,
TVA, total TTC). **Aucune saisie manuelle d'une dépense (formulaire vide) et
aucune action de suppression n'apparaissent à l'écran** — malgré le nom du
fichier source (« Modifications, Création et suppression des dépenses »),
seule la création via StockVision AI est démontrée dans ces 32 secondes.
Documenté tel quel, sans rien inventer (même principe que sur les tutoriels
produits/fournisseurs).

Côté MCP, seuls `create_expense`, `list_expenses` et `get_expense` existent —
pas de `update_expense` ni `delete_expense`. Le prompt Claude ci-dessous ne
couvre donc que la création (`create_expense`), avec des lignes structurées
en équivalent manuel du parcours OCR montré à l'écran (même logique que les
tutoriels ingrédients/produits : un prompt "direct" quand l'action existe
côté MCP, sans fabriquer d'UI d'édition/suppression qui n'a pas d'équivalent
outil).

## Voix off (9 lignes)

| # | Texte | Durée | Segment |
|---|---|---:|---|
| N0 | Fini la saisie manuelle de vos dépenses avec StockVision AI. | 3,11 s | intro |
| N1 | Depuis une livraison, importez la facture de votre fournisseur. | 3,37 s | B — bouton Ajouter une facture |
| N2 | L'intelligence artificielle analyse le document et extrait les données en quelques secondes. | 4,55 s | D — analyse StockVision AI |
| N3 | Vérifiez les produits détectés, puis validez la facture. | 3,06 s | E — écran de validation |
| N4 | Cliquez sur Valider et enregistrer : la dépense est aussitôt créée. | 3,89 s | clic Valider → succès |
| N5 | Retrouvez le détail complet : lignes, TVA et total TTC, directement dans votre comptabilité. | 6,50 s | G — fiche dépense (bénéfice) |
| N6 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | 4,41 s | étages 1+2 (réutilisé depuis tva/produits) |
| N7 | Collez-le dans la conversation : votre dépense est enregistrée en quelques secondes. | 4,00 s | étage 3 |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (CTA, réutilisé) |

N6/N8 réutilisés tels quels depuis `foodeatup-produits-tuto/vo/` (texte
générique — zéro crédit ElevenLabs dépensé). N0-N5/N7 générés en voix Adam FR
(`TGAegA0zNRi8I6nUdq3i`).

## Découpage

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 3,00 s | TENIR SES DÉPENSES STOCKVISION AI |
| A | 0,20 → 4,00 | 2,60 s | liste « Gestion des livraisons », clic sur une livraison |
| B | 4,00 → 6,75 | 2,00 s | détail de la livraison, scroll jusqu'à la section Facture |
| P1 | 6,75 → 7,05 | 0,90 s | **zoom-punch** sur + Ajouter une facture (1587, 496) |
| C | 7,05 → 8,75 | 1,80 s | modale « Importer une facture », dépôt du fichier |
| D | 8,75 → 16,50 | 4,60 s | barre de progression StockVision AI (0 → 100 %) |
| E | 16,50 → 20,85 | 3,80 s | écran « Validation de la facture », produits détectés |
| P2 | 20,85 → 21,15 | 0,90 s | **zoom-punch** sur Valider et enregistrer (1538, 554) |
| F | 21,15 → 22,75 | 1,60 s | modale « Facture validée ! » + clic Voir la dépense |
| G | 22,75 → 32,16 | 5,80 s | fiche Dépense EXP-0C9C28 : infos, produits achetés, notes |
| claude1 | carte générée | 6,00 s | reveal — prompt en gros, fond crème |
| claude2 | carte générée | 3,00 s | confirmation « Copié dans le presse-papiers ! » |
| claude3 | carte générée | 6,00 s | mockup chatbot Claude |
| outro | carte | 6,00 s (auto-étendue si besoin) | CTA |

Coordonnées mesurées par extraction de frames réelles (`work/frames*/`) sur le
rush source, pas au jugé. Segment D fortement accéléré (7,75 s → 4,60 s,
×1,68) pour ne pas laisser tourner la barre de progression à l'écran plus que
nécessaire, tout en restant lisible.

## Séquence Claude — module partagé

`mcp__FoodEatUp__create_expense(establishment_id, items[]{name, quantity,
unit_price, tax_rate?}, category?, supplier_id?, purchase_date?,
payment_method?, status?, notes?, supplier_invoice_reference?)` existe —
schéma vérifié :

> Enregistre une dépense pour mon établissement FoodEatUp (ID [ID
> établissement]) : [produit] x[quantité] à [prix unitaire] euros HT, TVA
> [taux]%, auprès du fournisseur [nom du fournisseur].

Même texte côté fiche Lovable (`claudePrompt`).

## Astuce du chef (proposée pour la fiche Lovable)

StockVision AI lit vos factures fournisseurs et crée la dépense toute seule —
plus besoin de ressaisir chaque ligne à la main. Le statut initial est
« En attente » : passez-le en « Payée » une fois le règlement effectué, pour
garder une comptabilité à jour en temps réel.

## Animations

Mêmes principes que toute la série : Ken Burns sur les cartes, xfade
(0,28 s), bandeaux d'étape (accents restaurés partout — pas d'apostrophe,
voir bug ingrédients), encadré orange pulsant sur les 2 clics principaux
(Ajouter une facture / Valider et enregistrer). Pas de clip avatar dans ce
dossier.

## Statut publication

Vidéo à livrer à Michael pour validation avant publication RapidoCMS/LinkedIn/Lovable.
