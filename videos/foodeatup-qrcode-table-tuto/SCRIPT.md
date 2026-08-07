# Tutoriel — Scanner le QR code de la table

Module `reservation-salle` (catégorie Agent IA Caroline & Salle), entrée **05
« Scanner le QR Code de la table »** du catalogue 157 tutoriels. Durée livrée :
**45,40 s** — H.264 High/yuv420p, 1920×828, AAC 48 kHz stéréo, faststart.
Audio : true peak **-7,28 dBFS** (marge confortable).

Écrans couverts : Plan de salle (sélection table QA3, génération + copie du
QR code de la table) puis vue client après scan (« Commander » : carte
Entrée/Autres, panier, validation) et confirmation en cuisine. Le tunnel
« nouvel onglet Google » du rush (29,6 s → 38,0 s, artefact d'enregistrement,
onglet vide) et le bloc paiement fractionné en fin de rush (58 s → 76 s) ne
sont pas retenus — hors sujet du titre, à reprendre dans un futur tutoriel
« Payer l'addition ».

## Voix off (8 lignes)

| # | Texte | Durée | Segment |
|---|---|---:|---|
| N1 | Vos clients commandent aujourd'hui sans attendre un serveur : il leur suffit de scanner le QR code de leur table. | 6,09 s | carte intro |
| N2 | Depuis le plan de salle, sélectionnez la table puis cliquez sur QR code de la table. | 4,73 s | A → B (sélection table, clic QR) |
| N3 | Le client scanne, arrive directement sur la carte de sa table et découvre le menu. | 4,36 s | B → C (QR généré → page Commander) |
| N4 | Il choisit ses plats, les ajoute au panier et valide sa commande en quelques secondes. | 4,36 s | C → D (ajout Pizza puis California Roll/Gyoza) |
| N5 | La commande part directement en cuisine, sans aller-retour avec un serveur — et il peut même régler l'addition depuis son téléphone. | 7,00 s | E → F (clic Commander → confirmation) |
| N6 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | 4,41 s | Claude étage 1+2 *(réutilisé tel quel depuis `foodeatup-qrcode-tuto/vo/`, même texte générique — pas de nouvel appel ElevenLabs)* |
| N7 | Collez-le dans la conversation : la commande de la table est créée et envoyée en cuisine en quelques secondes. | 5,62 s | Claude étage 3 |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin *(réutilisé tel quel)* |

Voix Adam FR (`TGAegA0zNRi8I6nUdq3i`), ElevenLabs `eleven_multilingual_v2`.
Script validé par Michael avant génération (règle STOP du workflow).

## Découpage

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 6,30 s | COMMANDER PAR QR CODE (visuel fourni par Michael) |
| A | 19,00 → 24,90 | 4,00 s | Plan de salle : sélection table QA3 |
| B | 24,90 → 29,70 | 3,20 s | **zoom-punch** clic « QR code de la table » (1568, 497) → modal QR + « Copier le lien » |
| C | 38,00 → 44,30 | 4,50 s | Page Commander (vue client) : Entrée, **zoom-punch** clic « + » Pizza (1822, 358) |
| D | 44,30 → 53,60 | 4,50 s | Autres : ajout California Roll + Gyoza (accéléré, panier → 40,80 €) |
| E | 53,60 → 54,40 | 0,80 s | **zoom-punch** clic « Commander · 40,80 € » (948, 783) |
| F | 54,40 → 58,00 | 4,50 s | Confirmation « Commande transmise en cuisine ! » |
| claude1 | carte générée | 3,00 s | reveal — prompt en gros, fond crème |
| claude2 | carte générée | 2,30 s | confirmation « Copié dans le presse-papiers ! » |
| claude3 | carte générée | 5,30 s | mockup chatbot Claude |
| outro | carte | 9,67 s | CTA (étendue automatiquement pour couvrir N8) |

Coordonnées mesurées par extraction de frames pleine résolution (1920×828,
`fps=1` puis `fps=2` autour de chaque clic). Bandeaux d'étape en PNG/overlay
(pas de `drawbox` animé — piège connu de la série, voir
`FOODEATUP-TUTORIELS-WORKFLOW.md`).

## Séquence Claude — module partagé

Action du rush avec un équivalent MCP direct : `create_order(establishment_id,
items[], table_id, covers)` crée la commande liée à la table (génère
automatiquement facture + devis). QR code / plan de salle sont de l'état/de la
génération client-side sans action serveur équivalente — pas de prompt inventé
pour ce bloc-là.

> Crée une commande pour la table [Numéro de table] de mon établissement
> FoodEatUp (ID [ID établissement]) : [Quantité] × [Nom du plat] à [Prix
> unitaire] €, pour [Nombre de couverts] couverts.

Même texte côté fiche Lovable (`claudePrompt`).

## Vérifications effectuées

- QA visuelle : frame extraite à l'offset réel de chacune des 8 lignes VO
  (`ffmpeg -ss <off> -frames:v 1`) — chaque ligne tombe sur un visuel
  cohérent avec son texte (aucune ligne ne joue sur le mauvais segment).
- Peak level final vérifié sur le fichier encodé (`astats`) : -7,28 dBFS.
- Vignette YouTube = image d'ouverture fournie par Michael, resize neutre
  1280×720 (pas de redesign), `out/thumbnail-youtube.jpg` (120 Ko).

## Statut publication

Vidéo + vignette livrées à Michael pour validation. **Pas de publication**
(RapidoCMS / LinkedIn / Lovable) tant que le retour n'est pas explicite —
règle STOP du workflow.
