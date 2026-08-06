# Tutoriel — Dessiner son plan de salle / QR code à table FoodEatUp

**BROUILLON — en attente de validation (règle `FOODEATUP-TUTORIELS-WORKFLOW.md` étape 3 :
STOP obligatoire avant de générer la VO ou de monter quoi que ce soit).**

Rush fourni : `assets/screen.mp4` — 1920x828, 25 fps, 40,0 s, H.264/AAC.
Carte d'ouverture fournie : `assets/intro.jpg` (« DESSINER SON PLAN DE SALLE / QR CODE À
TABLE », mascotte + QR code, identique au gabarit des autres vignettes).
Carte de fin : `assets/outro.jpg` réutilisée telle quelle (gabarit CTA générique de la série).

## Ce que montre le rush

1. **Plan de salle** — vue d'ensemble : 8 tables, 0 libre, 4 occupées, 1 réservée,
   taux d'occupation 63 %. Tables organisées par onglets de zone : *Toutes (8)*,
   *Salle principale (3)*, *Terrasse (3)*. Grille visuelle avec couvert et addition
   en cours par table (T3, T4, QA3, T5, T6, T7, QA2, Terrasse 1...), code couleur par
   statut (Libre/Réservée/Occupée/Nettoyage/Bloquée).
2. **Sélection d'une table (T3, 4 couverts, Occupée)** — panneau latéral : bouton
   « Changer le statut » (Libre/Réservée/Occupée/Nettoyage/Bloquée), commande en cours
   affichée (CMD-2026-00105 · 0,00 €), bouton bleu **QR code de la table**.
3. **Génération du QR code** — clic sur « QR code de la table » → carte « QR — T3 » :
   QR code généré, lien `http://127.0.0.1:8000/t/kcitjh4dir35` affiché en clair, légende
   « Le client scanne pour voir sa commande et la carte. », boutons **Télécharger** /
   **Copier le lien**.
4. **Clic sur « Copier le lien »** → confirmation « Lien copié : ... » puis ouverture du
   lien dans un nouvel onglet, qui atterrit directement sur la page client.
5. **Vue client (« Gosushi démo », Table T3 · Terrasse)** — commande cmd-2026-00105
   confirmée, boutons **Appeler un serveur** / **Demander l'addition** / **Payer
   l'addition** (seul ou à plusieurs), carte par catégories (« Entrée » : Dragon Roll
   6 pcs 45,00 €, Pizza 15,00 €, « Autres »...), pied de page « Propulsé par FoodEatUp ».
6. Retour à la carte QR puis au plan de salle en vue d'ensemble (boucle de clôture).

**Ce que le rush ne montre pas** : la création d'une zone ou d'une table elle-même
(« Éditer » / ajout d'une nouvelle table sur le plan) — le rush part d'un plan déjà
dessiné (8 tables réparties sur 2 zones) pour se concentrer sur la génération du QR code
et l'expérience client qui en découle. Le titre « Dessiner son plan de salle » couvre
donc à la fois la structure (zones + tables, déjà en place ici) et son usage concret
(QR code par table → commande autonome). Une pop-up McAfee (antivirus local, hors
produit) apparaît furtivement vers 17 s pendant le téléchargement — à ne pas garder
dans le montage final (recadrage/masquage sur ce segment).

## Voix off (proposition — 9 lignes, voix Adam FR `TGAegA0zNRi8I6nUdq3i`)

| # | Texte | Segment |
|---|---|---|
| N0 | Dessiner son plan de salle sur FoodEatUp, en quelques clics. | intro |
| N1 | Organisez vos tables par zones, comme Salle principale ou Terrasse. | A — vue d'ensemble |
| N2 | Sélectionnez une table pour voir son statut et sa commande en cours. | B — sélection T3 |
| N3 | Cliquez sur QR code de la table pour générer son QR code personnalisé. | clic + C — QR généré |
| N4 | Vos clients le scannent et arrivent directement sur la carte de leur table. | D — copie du lien / ouverture |
| N5 | Ils commandent, demandent l'addition et payent, seuls ou à plusieurs, sans appeler personne. | E — vue client Gosushi |
| N6 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | étages 1+2 (réutilisé depuis `foodeatup-tva-tuto/vo/`) |
| N7 | Collez-le dans la conversation : votre plan de salle est configuré en quelques secondes. | étage 3 |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | carte de fin (CTA, réutilisé) |

N6/N8 réutilisables tels quels (texte générique identique à `foodeatup-tva-tuto`) — zéro
crédit ElevenLabs supplémentaire pour ces deux lignes si le texte est approuvé sans
changement.

## Découpage (approximatif — affiné au montage avec seuillage colorimétrique)

| Seg | Source | Contenu |
|---|---|---|
| intro | carte | DESSINER SON PLAN DE SALLE / QR CODE À TABLE |
| A | 0,0 → 6,0 | Plan de salle, vue d'ensemble, onglets de zones |
| B | 6,0 → 8,3 | **zoom-punch** sélection table T3 → panneau statut + commande |
| C | 8,3 → 17,8 | clic **QR code de la table** (zoom-punch) → carte QR générée |
| D | 17,8 → 23,8 | clic **Copier le lien** → confirmation → ouverture nouvel onglet |
| E | 23,8 → 30,0 | vue client « Gosushi démo » : carte, boutons appel/addition/paiement |
| F | 30,0 → 40,0 | retour QR puis plan de salle (boucle, coupé/raccourci si trop long) |
| claude1 | carte générée | reveal — prompt en gros, fond crème |
| claude2 | carte générée | confirmation « Copié dans le presse-papiers ! » |
| claude3 | carte générée | mockup chatbot Claude |
| outro | carte | CTA |

## Séquence Claude — module partagé

Le titre du tutoriel correspond à la construction du plan de salle : deux outils MCP
couvrent exactement cette action (zone puis table dedans), dans l'ordre logique de
construction (même si ce rush précis part d'un plan déjà dessiné) :

`mcp__FoodEatUp__create_zone(establishment_id, name, color?)` +
`mcp__FoodEatUp__create_table(establishment_id, name, capacity?, zone_id?, shape?)`

> Crée une zone [nom de la zone, ex. Terrasse] dans mon plan de salle, puis ajoute une
> table [nom de la table, ex. T3] de [nombre] couverts dans cette zone, pour mon
> établissement FoodEatUp (ID [ID établissement]).

Même texte côté fiche Lovable (`claudePrompt`).

## Fiche Lovable (`src/data/tutorials.ts`) — proposition

- `slug`: `dessiner-son-plan-de-salle`
- `moduleSlug`: `configuration` (suite logique après `creer-ses-produits`, 11e vidéo Configuration)
- `subcategory`: `11 - dessiner son plan de salle`
- `howItWorks`: [
  "Ouvrez Plan de salle et organisez vos tables par zone (Salle principale, Terrasse...).",
  "Sélectionnez une table pour voir son statut et sa commande en cours.",
  "Cliquez sur QR code de la table pour générer son QR code personnalisé.",
  "Téléchargez-le ou copiez le lien pour l'imprimer sur la table.",
  "Vos clients scannent, consultent la carte et commandent, demandent l'addition et payent — seuls ou à plusieurs.",
  ]
- `whatItsFor`: "Un QR code par table transforme chaque table en point de commande
  autonome : moins d'allers-retours en salle, service plus fluide, addition réglée
  directement par le client."
- `chefTip` (à confirmer avec Michael — logique métier non visible à l'écran, comme pour
  fournisseurs/produits) : ex. rappeler qu'on peut imprimer les QR en lot pour toute une
  zone, ou que le lien reste valable même si la table change de statut.
- `claudePrompt`: identique au prompt ci-dessus.

## Statut publication

**Brouillon.** En attente de validation du script par Michael avant génération VO
(ElevenLabs), montage, puis livraison (`SendUserFile`) et — seulement après un second OK
explicite — publication RapidoCMS + LinkedIn + Lovable + mise à jour du tableau
« Tutoriels publiés » dans `videos/LOVABLE-FOODEATUP-DOCS.md`.
