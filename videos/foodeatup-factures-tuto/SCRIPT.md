# Tutoriel — Créer une facture (FoodEatUp) · Script voix off (FR)

**Script validé par Michael le 2026-08-04.** Montage terminé, en attente de validation de la
vidéo (STOP obligatoire avant publication — voir `FOODEATUP-TUTORIELS-WORKFLOW.md`).

Module Lovable : **Comptabilité** (`comptabilite`). Sous-catégorie Drive (image d'ouverture
fournie) : « Créer une facture comptabilité ». Voix : Adam FR / Adam-Instructor (ElevenLabs,
`TGAegA0zNRi8I6nUdq3i`) — même voix que toute la série. Rush source : `assets/screen.mp4`
(1920x828, 25 fps, 80,49 s).

Durée livrée : **54,96 s** — H.264 High/yuv420p, AAC 48 kHz stéréo, faststart. Audio : true
peak **-7,27 dBFS**. Decode 0 erreur, moov avant mdat (faststart confirmé).

## Ce que montre le rush

Écran « Facturation » (onglets Facture / Devis / Dépenses, KPIs Total payées / En attente de
paiement / Total devis reçu) → clic **Créer une facture** → nouvelle page de formulaire :

1. Sélection du client (« Sélectionnez un client » / client occasionnel), numéro de TVA
   intracommunautaire (optionnel), référence de commande (optionnelle).
2. Recherche d'un produit (« lait » → suggestion **+ Créer le produit "lait"** si absent du
   catalogue, ou sélection d'un produit existant — ici « Lait de la ferme jaouda »).
3. Ligne article : quantité, prix HT, TVA % par ligne.
4. Application d'une offre (« Choisir une offre » → offre appliquée avec son propre prix/TVA).
5. TVA globale (%), remise (montant + unité € ou %).
6. Dates : date de facture (obligatoire), date d'échéance.
7. Mode de paiement (Espèces / Carte bleue / Virement bancaire / Chèque), mentions légales
   libres, option d'envoi de la facture par e-mail directement depuis FoodEatUp.
8. Pendant la saisie, un **indicateur de conformité Factur-X (2026)** progresse en direct
   (63 % → 75 % → 88 % → 100 %) avec la liste des champs manquants (date d'échéance, au moins
   une ligne article, TVA renseignée) — utile accroche produit (facturation électronique
   obligatoire en France à partir de 2026).
9. Clic **Enregistrer** (ou **Brouillon**) → état de chargement (« Création en cours... ») →
   retour à la liste, nouvelle facture visible avec son ID, statut, conformité, total TTC.
10. Menu d'action par ligne : Visualiser / Modifier / Télécharger / Supprimer.

`mcp__FoodEatUp__create_invoice` correspond directement à cette action (établissement, lignes
avec désignation/quantité/prix unitaire HT/TVA ligne, TVA globale, remise, dates, mode de
paiement) → séquence de fin « cas d'usage + prompt Claude » applicable (3 temps, module
partagé `_shared/claude_prompt_sequence.py`), comme pour tva/catégories/fournisseurs/produits.

## Voix off (11 lignes)

| # | Texte | Durée | Segment |
|---|---|---:|---|
| N0 | Facturer vos clients à la main ? Avec FoodEatUp, votre facture est prête en quelques clics. | 4,83 s | intro |
| N1 | Cliquez sur Créer une facture. | 1,62 s | clic Créer une facture |
| N2 | Choisissez votre client, et complétez son numéro de TVA si besoin. | 4,00 s | C — client / TVA |
| N3 | Recherchez un produit dans votre catalogue, ou créez-le à la volée. | 3,47 s | D — recherche produit |
| N4 | Fixez la quantité, le prix et la TVA, et appliquez une offre ou une remise si besoin. | 5,20 s | E — qty/prix/TVA/offre |
| N5 | Renseignez la date de facture et la date d'échéance. | 2,69 s | F — dates/remise |
| N6 | Choisissez le mode de paiement, puis cliquez sur Enregistrer. | 3,06 s | F2 — relecture + clic Enregistrer |
| N7 | Votre facture est aussitôt conforme à la norme Factur-X 2026, et prête à télécharger ou à envoyer par e-mail. | 6,50 s | H — résultat (conformité 100%) |
| N8 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | 4,41 s | étages 1+2 (réutilisé) |
| N9 | Collez-le dans la conversation : votre facture est créée en quelques secondes. | 4,31 s | étage 3 |
| N10 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (CTA, réutilisé) |

N8 et N10 réutilisés tels quels depuis `foodeatup-produits-tuto/vo/` (texte générique
identique) — zéro crédit ElevenLabs dépensé sur ces deux lignes.

## Découpage

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 3,00 s | CRÉER UNE FACTURE COMPTABILITÉ |
| A | 0,20 → 10,00 | 2,50 s | liste « Facturation », KPIs, 0 facture sélectionnée |
| B | 10,00 → 10,35 | 0,90 s | **zoom-punch** sur Créer une facture (1681, 171) |
| C | 10,60 → 20,00 | 5,00 s | client, numéro de TVA intracommunautaire, référence |
| D | 20,00 → 34,00 | 5,00 s | recherche produit, suggestion de création, sélection |
| E | 34,00 → 50,00 | 6,00 s | quantité, prix HT, TVA ligne, offre appliquée |
| F | 50,00 → 58,50 | 4,00 s | TVA globale, dates, remise |
| F2 | 62,00 → 65,10 | 4,00 s | relecture (client/TVA/mode de paiement/totaux) |
| G | 65,10 → 65,45 | 0,90 s | **zoom-punch** sur Enregistrer (1690, 320) |
| H | 65,50 → 78,49 | 6,00 s | chargement puis conformité 100 % + retour liste |
| claude1 | carte générée | 6,00 s | reveal — prompt en gros, fond crème |
| claude2 | carte générée | 3,00 s | confirmation « Copié dans le presse-papiers ! » |
| claude3 | carte générée | 6,00 s | mockup chatbot Claude |
| outro | carte | 6,20 s | CTA |

La fenêtre 58,5-62,0 s du rush (relecture redondante déjà couverte par C-F) est coupée du
montage, comme pratiqué sur produits/ingrédients pour éviter de re-montrer des champs déjà
vus. Coordonnées mesurées sur les frames réelles (`work/frames*/`, non versionné).

## Séquence Claude (cas d'usage) — prompt proposé

`mcp__FoodEatUp__create_invoice(establishment_id, items[{name, quantity, unit_price,
tax_rate?}], client_id?, tax_rate?, discount_amount?, due_date?, invoice_date?,
payment_method?, notes?)`

> Crée une facture pour [nom du client], avec [désignation produit] x[quantité] à
> [prix unitaire]€ HT (TVA [taux]%), remise de [montant]€, échéance au [date d'échéance],
> paiement par [mode de paiement], pour mon établissement FoodEatUp (ID [ID établissement]).

Même texte côté fiche Lovable (`claudePrompt`).

## Astuce du chef (proposition, pour la fiche Lovable)

« La conformité Factur-X n'est pas cosmétique : à partir de 2026, la facturation électronique
devient obligatoire pour toutes les entreprises en France. FoodEatUp vous evite les mauvaises
surprises en vérifiant vos factures en temps réel. »

## Statut

Slug retenu : `creer-une-facture` (sous-catégorie affichée : « Créer une facture »), dossier
vidéo `videos/foodeatup-factures-tuto/`.

**Script validé par Michael le 2026-08-04. VO générée, montage terminé, checklist de
compatibilité passée. En attente de validation de la vidéo montée avant publication
(RapidoCMS, LinkedIn, Lovable) — conformément à la règle du pipeline
(`FOODEATUP-TUTORIELS-WORKFLOW.md`).**
