# Tutoriel — Archiver ses dépenses en les reliant à ses livraisons (Comptabilité) FoodEatUp

Module **Comptabilité**, sous-catégorie proposée « Relier ses achats à ses livraisons »
(⚠️ nom exact du sous-dossier Drive à confirmer, pas d'accès Drive depuis cet environnement —
même réserve que sur le tuto précédent).

Rush fourni : `assets/screen.mp4` (1920×828, 25 fps, 35,72 s) — module Livraisons puis Comptabilité.
Carte d'ouverture fournie : `assets/intro.jpg` (« RELIER SES ACHATS AUX LIVRAISONS COMPTABILITÉ »).
Carte de fin : `assets/outro.jpg` — même fichier (md5 identique) que sur toute la série, réutilisé tel quel.

## Déroulé du rush (analyse frame-by-frame, 1 img/s)

| t | Écran |
|---:|---|
| 0–6 s | « Gestion des livraisons » : liste de cartes livraison (n° commande, fournisseur, dates prévue/reçue, mode, prix), scroll |
| 6–7 s | Clic sur **Voir le détail** d'une carte (fournisseur « louay ») |
| 7–9 s | Détail de la livraison : badge Livrée, date prévue/effective, prix, tableau « Produits livrés » (produit, qté commandée, qté reçue, température) |
| 9–10 s | Scroll vers la section Facture, clic sur **Ajouter une facture** |
| 10–15 s | Modal « Importer une facture » : bandeau « Cette facture sera liée à la livraison #2896 », zone glisser-déposer (PDF/JPG/PNG, 10 Mo max), clic **Choisir un fichier** |
| 15–18 s | Barre de progression IA : 15 % → 43 % → 100 %, libellés « Document reçu — en attente du worker… », « Extraction des données en cours… », « Analyse terminée ! » |
| 18–20 s | Écran de résultat : Informations détectées (fournisseur, n° facture, date), Fournisseur, Livraison associée, tableau Produits (2 nouveaux, avec lien « + Ajouter au catalogue »), clic **Valider et enregistrer** |
| 20–22 s | Modal de confirmation « Facture validée ! 0 prix mis à jour. Dépense enregistrée dans votre comptabilité. » → clic **Voir la dépense** |
| 22–26 s | Fiche dépense `EXP-3BE67E` : Informations (numéro, date d'achat, référence facture fournisseur, mode de paiement, catégorie), Résumé (Sous-total HT 400 €, TVA 80 €, Total TTC 480 €) |
| 26–28 s | Clic sur le menu hamburger → section **Comptabilité** dépliée (Mes commandes, Factures, Devis, **Dépenses**, E-Reporting, Archives légales, Clients, Fournisseurs) |
| 28–35 s | Page Comptabilité, onglet **Dépenses** : cartes (839 Total payées, 329 En attente de paiement, 0 Total devis reçu), tableau des dépenses — la fiche `#EXP-3BE67E` créée à l'instant apparaît dans la liste (En attente, 480,00 €) |

## Outil MCP FoodEatUp correspondant

`mcp__FoodEatUp__create_expense(establishment_id, items[], supplier_id?,
supplier_invoice_reference?, purchase_date?, payment_method?, status?, category?, notes?)` —
couvre directement l'essentiel de ce qui est montré : fournisseur, référence facture, lignes de
produits (nom/quantité/prix unitaire), totaux calculés automatiquement, dépense archivée dans
Comptabilité. Pas de champ « livraison associée » côté MCP (aucun `link_expense_to_delivery`
exposé), donc le prompt enregistre directement la dépense plutôt que de reproduire l'étape
d'import OCR — même bénéfice pour le restaurateur (dépense archivée sans ressaisie).

Séquence Claude en fin de vidéo (template partagé `videos/_shared/claude_prompt_sequence.py`,
réutilisé tel quel).

**Prompt (identique côté vidéo et côté fiche Lovable `claudePrompt`) :**

> Enregistre une dépense pour mon établissement FoodEatUp (ID [ID établissement]) : fournisseur
> [nom du fournisseur], produit [désignation] x[quantité] à [prix unitaire] € HT, référence
> facture [référence facture fournisseur].

Réplique assistant (`CLAUDE_RESPONSE`) : « Bien sûr ! J'enregistre cette dépense pour votre
établissement… »

## Voix off proposée (9 lignes, voix Adam FR `TGAegA0zNRi8I6nUdq3i`) — **BROUILLON, PAS ENCORE VALIDÉ**

| # | Texte | Ancrage prévu |
|---|---|---|
| N0 | Relier vos achats à vos livraisons sur FoodEatUp ? Archivez vos dépenses en un clic. | carte d'intro |
| N1 | Depuis Gestion des livraisons, ouvrez le détail d'une livraison reçue. | clic « Voir le détail » |
| N2 | Cliquez sur Ajouter une facture pour l'associer directement à cette livraison. | clic « Ajouter une facture » |
| N3 | Déposez le PDF ou la photo de la facture : l'IA analyse et extrait les données en quelques secondes. | modal import + progression OCR |
| N4 | Vérifiez le fournisseur et les produits détectés, puis validez pour enregistrer la dépense. | écran résultat + clic Valider |
| N5 | Votre dépense apparaît aussitôt dans Comptabilité, avec son détail et son statut de paiement. | fiche dépense + liste Dépenses |
| N6 | Vous pouvez aussi enregistrer une dépense depuis Claude : copiez ce prompt, remplacez les crochets. | étage 1+2 (reveal + copié) |
| N7 | Collez-le dans la conversation : votre dépense est archivée en quelques secondes. | étage 3 (mockup chatbot) |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | carte de fin (CTA) |

N8 est la ligne CTA générique déjà utilisée sur toute la série — candidate à copier telle quelle
(`.mp3` déjà généré sur les tutos précédents) une fois le script validé.

## Statut

**Script en attente de validation de Michael — aucune VO ElevenLabs générée, aucun montage
lancé** (règle « STOP obligatoire » de `FOODEATUP-TUTORIELS-WORKFLOW.md`, étape 3).
