# Tutoriel — Mes dépenses fournisseur FoodEatUp (Comptabilité)

Module Comptabilité, dossier Drive « 7- Mes dépenses fournisseur » — fichier
vérifié via `mcp__Google_Drive__search_files` (taille identique,
20 311 360 octets). Durée livrée : **60,20 s** — H.264 High/yuv420p, AAC
48 kHz stéréo, faststart. Audio : max -4,5 dBFS. Sans avatar HeyGen.

Rush riche (79,3 s) : liste des dépenses → création → date d'achat/référence
facture/fournisseur/joindre la facture → recherche produit → quantité/
description/total → catégorie/statut → enregistrer → retour à la liste.
Le rush montre ensuite visualiser/supprimer une dépense existante — hors
périmètre de cette vidéo (focalisée sur la création, même choix que pour
`foodeatup-creer-devis-tuto`).

## Voix off (10 lignes)

| # | Texte | Durée | Segment |
|---|---|---:|---|
| N1 | Retrouvez toutes vos dépenses fournisseurs : payées, en attente, déclinées, avec leur montant total. | 6,22 s | A |
| N2 | Cliquez sur Créer une dépense pour enregistrer un nouvel achat. | 3,11 s | A2 (zoom-punch) |
| N3 | Indiquez la date d'achat, la référence de la facture, le fournisseur, et joignez directement le fichier de la facture. | 5,98 s | B |
| N4 | Recherchez le produit acheté : son prix se remplit automatiquement depuis votre catalogue. | 4,96 s | C (zoom-punch) |
| N5 | Ajustez la quantité, la description se complète toute seule, et le total se recalcule en direct. | 5,43 s | D |
| N6 | Choisissez une catégorie de dépense et son statut de paiement : payée, en attente, ou déclinée. | 5,75 s | E |
| N7 | Enregistrez : votre dépense apparaît aussitôt dans la liste, avec son montant TTC. | 5,04 s | F (zoom-punch) |
| N8 | Vous pouvez aussi demander ça à Claude : copiez ce prompt, remplacez les crochets. | 4,31 s | étages 1+2 |
| N9 | Collez-le dans la conversation : votre dépense fournisseur est enregistrée en quelques secondes. | 5,25 s | étage 3 |
| N10 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (réutilisée) |

## Découpage

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 2,50 s | SAISIR SES DÉPENSES FOURNISSEUR |
| A | 0,00 → 4,00 | 7,00 s | Liste des dépenses (Facture/Devis/Dépenses), stats, tableau |
| A2 | 6,00 → 6,80 | 4,00 s | **zoom-punch** sur « Créer une dépense » |
| B | 8,00 → 11,00 | 7,00 s | Date d'achat, référence facture, fournisseur (Épicerie Fine du Cap), joindre la facture (upload) |
| C | 32,60 → 33,40 | 6,00 s | **zoom-punch** sur l'option « Plateau GoSushi 28 pcs » dans l'autocomplétion |
| D | 40,00 → 42,00 | 6,50 s | Quantité (40), description auto-remplie, Sous-total HT/TVA/Total TTC |
| E | 47,00 → 49,00 | 7,00 s | Catégorie de dépense (Sucré & desserts), statut (En attente) |
| F | 58,00 → 58,40 | 6,00 s | **zoom-punch** sur la nouvelle ligne #D20260002 dans la liste (1 342,32 €, En attente) |
| claude1 | carte générée | 2,50 s | reveal — prompt en gros, fond crème |
| claude2 | carte générée | 2,50 s | confirmation « Copié dans le presse-papiers ! » |
| claude3 | carte générée | 6,00 s | mockup chatbot Claude |
| outro | carte | 6,20 s | CTA |

## Séquence Claude — module partagé

Correspond à `create_expense(establishment_id, items[], supplier_id,
supplier_invoice_reference, purchase_date, category, status,
payment_method)` — mêmes champs que ceux remplis à l'écran (produit,
quantité, prix, fournisseur, référence facture, catégorie, statut). Aucun
champ MCP pour le fichier de facture joint : le prompt reste donc scopé aux
données, sans mentionner l'upload.

> Enregistre une dépense chez le fournisseur [nom du fournisseur],
> référence facture [référence], avec [quantité] [nom du produit] à
> [prix]€ HT, catégorie [catégorie], statut [payée / en attente / déclinée],
> pour mon établissement FoodEatUp (ID [ID établissement]).

## Statut publication

Vidéo à livrer à Michael pour validation avant publication RapidoCMS/
LinkedIn/Lovable. RapidoCMS non autorisé dans cette session — publication
CMS/LinkedIn en attente dans tous les cas.
