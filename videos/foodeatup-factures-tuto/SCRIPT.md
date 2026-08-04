# Tutoriel — Créer une facture (FoodEatUp) · Script voix off (FR) — DRAFT, non validé

Module Lovable : **Comptabilité** (`comptabilite`). Sous-catégorie Drive (image d'ouverture
fournie) : « Créer une facture comptabilité ». Voix : Adam FR / Adam-Instructor (ElevenLabs,
`TGAegA0zNRi8I6nUdq3i`) — même voix que toute la série. Rush source : `assets/screen.mp4`
(1920x828, 25 fps, 80,49 s).

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

## Voix off — proposition (10 lignes)

| # | Texte |
|---|---|
| N0 | Facturer vos clients à la main ? Avec FoodEatUp, votre facture est prête en quelques clics. |
| N1 | Cliquez sur Créer une facture. |
| N2 | Choisissez votre client, et complétez son numéro de TVA si besoin. |
| N3 | Recherchez un produit dans votre catalogue, ou créez-le à la volée. |
| N4 | Fixez la quantité, le prix et la TVA, et appliquez une offre ou une remise si besoin. |
| N5 | Renseignez la date de facture et la date d'échéance. |
| N6 | Choisissez le mode de paiement, puis cliquez sur Enregistrer. |
| N7 | Votre facture est aussitôt conforme à la norme Factur-X 2026, et prête à télécharger ou à envoyer par e-mail. |
| N8 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. |
| N9 | Collez-le dans la conversation : votre facture est créée en quelques secondes. |
| N10 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! |

N8 et N10 sont **réutilisables tels quels** depuis `foodeatup-produits-tuto/vo/` (texte
générique identique) — zéro crédit ElevenLabs dépensé sur ces deux lignes. N9 est spécifique
(« votre facture est créée ») donc à générer.

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

## À valider avant de continuer

1. Le texte des lignes N0–N7 (N8/N10 déjà figées, réutilisées ; N9 sera généré une fois le
   reste validé).
2. Le prompt Claude et l'astuce du chef ci-dessus.
3. Le nom de slug proposé : `creer-une-facture` (sous-catégorie affichée : « Créer une
   facture »), dossier vidéo `videos/foodeatup-factures-tuto/`.

**Conformément à la règle du pipeline (`FOODEATUP-TUTORIELS-WORKFLOW.md`), aucune génération
audio ni montage ne démarre avant validation explicite de ce script.**
