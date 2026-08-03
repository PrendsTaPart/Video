# Tutoriel — Classer ses factures dans les dépenses (module Comptabilité & Achats)

Durée livrée : **51,56 s** — H.264 High/yuv420p, AAC LC 48 kHz stéréo,
faststart (moov avant mdat confirmé). Audio : peak **-7,2 dBFS**. Decode 0 erreur.

## Ce que montre le rush

Le rush (48 s, capture 1920x828 @25fps, pas de chrome navigateur à rogner)
montre le module Comptabilité > Dépenses : liste des dépenses (onglets
Facture/Devis/Dépenses, statistiques Total payées/En attente de
paiement/Total devis reçu) → clic "Créer une dépense" → formulaire (date
d'achat, référence facture fournisseur, fournisseur "carrefour") → zone
"Joindre la facture" (glisser-déposer ou "Choisir un fichier", PDF/JPG/PNG
max 10 Mo) → upload de `Facture_FAC-2026-00006.pdf`, confirmation avec
coche verte → recherche et ajout d'un article ("Gâteau patate", quantité
10, prix HT 6,50 €, description) → catégorie de dépense "Desserts" →
statut "Payée" → clic "Enregistrer" → retour à la liste (nouvelle ligne
#D20260003, carrefour, Payée, 65,00 €) → menu Action (3 points) →
"Visualiser" → fiche détail de la dépense : informations, résumé, statut,
section "Facture fournisseur uploadée" avec bouton "Télécharger", fiche
fournisseur, tableau des produits achetés — c'est l'historique de la
dépense, avec la facture jointe consultable à tout moment.

## Voix off (8 lignes, voix Adam FR `TGAegA0zNRi8I6nUdq3i`)

| # | Texte | Durée | Segment |
|---|---|---:|---|
| N0 | Comment classer vos factures dans vos dépenses FoodEatUp ? Voici comment faire, jusqu'à l'historique. | 5,20 s | intro |
| N1 | Depuis l'onglet Dépenses, retrouvez tous vos achats : total payé, en attente de paiement, et devis reçus. | 6,09 s | A — liste des dépenses |
| N2 | Cliquez sur Créer une dépense, puis renseignez la date d'achat, la référence de facture et le fournisseur. | 5,93 s | C — formulaire (date/référence/fournisseur) |
| N3 | Glissez directement le PDF ou la photo de la facture fournisseur : elle est jointe à la dépense. | 5,69 s | D — joindre la facture |
| N4 | Ajoutez les articles achetés avec leur quantité et leur prix, puis choisissez la catégorie de dépense. | 5,88 s | E — article + catégorie |
| N5 | Choisissez le statut, payée ou en attente, et cliquez sur Enregistrer : la dépense apparaît aussitôt dans la liste. | 6,64 s | F — statut + enregistrer |
| N6 | Retrouvez-la à tout moment dans l'historique : la facture jointe reste consultable et téléchargeable en un clic. | 5,75 s | G2 — fiche détail / historique |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 4,91 s | carte de fin (CTA) |

Pas de N7 / séquence "Utiliser avec Claude" : `create_expense` (MCP) ne
gère pas l'upload de fichier, qui est l'action centrale de cette vidéo
(joindre la facture) — conformément à la règle du workflow, pas de prompt
inventé quand l'action n'a pas d'équivalent MCP exact.

## Découpage

Segments dimensionnés sur les durées VO réellement mesurées — dérive
nulle au premier montage recalibré (`offsets:` = `anchors:` dans le build).

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 6,00 s | CLASSER SES FACTURES DANS LES DÉPENSES |
| A | 0,30 → 2,60 | 6,30 s | liste des dépenses, statistiques |
| B | 2,90 → 3,30 | 1,00 s | transition — clic "Créer une dépense" |
| C | 5,00 → 8,80 | 6,50 s | date d'achat, référence facture, fournisseur |
| D | 9,60 → 14,20 | 6,20 s | zone "Joindre la facture", upload PDF, confirmation |
| E | 18,00 → 24,00 | 6,40 s | recherche produit, quantité/prix/description, catégorie |
| F | 26,00 → 30,30 | 7,15 s | statut "Payée", clic "Enregistrer" |
| G1 | 32,00 → 36,50 | 2,00 s | transition — retour liste, menu Action → Visualiser |
| G2 | 39,50 → 46,50 | 6,30 s | fiche détail : facture jointe, fournisseur, produits |
| outro | carte | 6,06 s | CTA |

Transitions : `fade` sur les enchaînements continus (intro→A, A→B, C→D,
D→E, E→F, G2→outro), `slideleft` sur les coupures de contexte (B→C,
F→G1, G1→G2).

## Animations

Mêmes principes que toute la série : Ken Burns sur les cartes intro/outro,
xfade (0,28 s) sur chaque coupe, bandeaux d'étape numérotés (1 à 6). Pas de
zoom-punch sur cette vidéo (pas de coordonnées de clic mesurées au pixel
près pour ce rush) — à la différence de `changer-les-statuts-dune-facture`,
qui en avait quatre.

## Astuce du chef (proposée pour Lovable)

Joindre systématiquement la facture PDF ou la photo au moment de la
création de la dépense — pas après coup — pour ne jamais avoir à
rechercher un justificatif au moment d'une déclaration ou d'un contrôle :
il reste attaché à la dépense, consultable et téléchargeable depuis sa
fiche détail (l'historique), avec le statut (Payée / En attente / Décliné)
toujours visible en un coup d'œil.

## Statut publication

Montage terminé et checklist de compatibilité passée (H.264 High/yuv420p,
AAC 48 kHz stéréo, faststart, peak -7,2 dBFS, 0 erreur de décodage).
**En attente de validation de Michael avant toute publication** (règle du
workflow : ni Lovable, ni RapidoCMS/LinkedIn tant que le retour explicite
n'est pas reçu).
