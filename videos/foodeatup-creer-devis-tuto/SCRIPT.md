# Tutoriel — Créer un devis FoodEatUp (Comptabilité)

Module Comptabilité, dossier Drive « 3- Créer un devis » — fichier vérifié via
`mcp__Google_Drive__search_files` (taille identique, 18 051 969 octets).
Durée livrée : **66,08 s** — H.264 High/yuv420p, AAC 48 kHz stéréo,
faststart. Audio : max -7,3 dBFS. Sans avatar HeyGen.

Rush riche (99,3 s) : liste des devis → création → client/délai/paiement →
recherche produit → quantité/prix/TVA → remise globale/TVA globale/devise →
acompte demandé → enregistrer & envoyer → confirmation → retour à la liste.
Le rush montre ensuite modifier/supprimer un devis existant — hors périmètre
de cette vidéo (focalisée sur la création, à la demande de Michael) ; matière
pour une future vidéo dédiée si besoin.

## Voix off (10 lignes)

| # | Texte | Durée | Segment |
|---|---|---:|---|
| N1 | Retrouvez tous vos devis d'un coup d'œil : brouillons, envoyés, signés, avec leur montant total. | 6,22 s | A |
| N2 | Cliquez sur Créer un devis pour commencer. | 2,04 s | A2 (zoom-punch) |
| N3 | Choisissez le client, le délai de paiement, et le mode de règlement souhaité. | 4,36 s | B |
| N4 | Recherchez un produit ou une recette : son prix et sa TVA se remplissent automatiquement. | 5,43 s | C (zoom-punch) |
| N5 | Ajustez la quantité si besoin, le total se recalcule instantanément. | 3,89 s | D |
| N6 | Appliquez une remise globale, une TVA, et demandez si besoin un acompte : le solde restant s'affiche automatiquement. | 6,95 s | E (zoom-punch) |
| N7 | Envoyez le devis par email en un clic : votre client reçoit un lien sécurisé pour le consulter et le signer, et il apparaît aussitôt dans votre liste. | 9,01 s | F1+F2 (zoom-punch x2) |
| N8 | Vous pouvez aussi demander ça à Claude : copiez ce prompt, remplacez les crochets. | 4,26 s | étages 1+2 |
| N9 | Collez-le dans la conversation : votre devis est créé en quelques secondes. | 4,26 s | étage 3 |
| N10 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (réutilisée) |

## Découpage

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 2,50 s | CRÉER UN DEVIS COMPTABILITÉ |
| A | 0,00 → 4,00 | 7,00 s | Liste des devis (Facture/Devis/Dépenses), stats, tableau |
| A2 | 3,70 → 4,30 | 3,00 s | **zoom-punch** sur « Créer un devis » |
| B | 5,50 → 8,00 | 5,50 s | Client (co-cuisinage), délai (30 jours), mode de règlement |
| C | 12,60 → 13,40 | 6,00 s | **zoom-punch** sur l'option « Salmon Maki » dans l'autocomplétion |
| D | 24,00 → 26,00 | 6,00 s | Quantité/Prix HT/TVA de l'article, Total HT |
| E | 44,00 → 46,00 | 8,50 s | **zoom-punch** sur remise globale, TVA globale, devise, acompte demandé (30 % → 398,10 €, solde 928,90 €) |
| F1 | 60,00 → 61,20 | 4,50 s | **zoom-punch** sur « Enregistrer & Envoyer » |
| F2 | 63,30 → 64,30 | 5,50 s | **zoom-punch** sur le toast « Devis créé avec succès et envoyé par email » |
| G | 69,00 → 71,00 | 5,00 s | Retour à la liste, nouveau devis « En attente » |
| claude1 | carte générée | 2,40 s | reveal — prompt en gros, fond crème |
| claude2 | carte générée | 2,50 s | confirmation « Copié dans le presse-papiers ! » |
| claude3 | carte générée | 5,00 s | mockup chatbot Claude |
| outro | carte | 6,20 s | CTA |

## Séquence Claude — module partagé

Correspond à `create_quote(establishment_id, items[], client_id,
discount_amount, tax_rate, advance_percentage, payment_method, quote_date,
validity_date)` — mêmes champs que ceux remplis à l'écran (produit,
quantité, prix, TVA, remise, acompte).

> Crée un devis pour le client [nom du client], avec [quantité] [nom du
> produit] à [prix]€ HT (TVA [taux]%), pour mon établissement FoodEatUp
> (ID [ID établissement]).

## Statut publication

Vidéo à livrer à Michael pour validation avant publication RapidoCMS/
LinkedIn/Lovable. RapidoCMS non autorisé dans cette session — publication
CMS/LinkedIn en attente dans tous les cas.
