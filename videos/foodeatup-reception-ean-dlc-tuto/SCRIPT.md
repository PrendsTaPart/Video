# Tutoriel — Scanner le code EAN et la DLC (Contrôle à réception) FoodEatUp

Module HACCP / Contrôle à réception. Rush fourni par Michael : `assets/screen.mp4`
(47,96 s, 1920x828, piste audio native silencieuse à -91 dB — VO entièrement
ElevenLabs). Pas de clip avatar.

## Ce que montre le rush

1. "Réception du jour" : liste des commandes à contrôler (0,0 → 5,0 s).
2. Ouverture d'une commande livrée ("Livrée") : tableau "Produits livrés" avec
   Qté commandée / Qté reçue / Température / Action (6,0 → 8,7 s).
3. Clic sur le menu d'action "..." de la ligne produit → 4 options : **Photo
   DLC**, **DLC manuelle**, **Température**, **Scanner produit** (8,7 s).
4. Photo DLC : prise de photo de l'étiquette, saisie de la Date DLC,
   "Enregistrer" → toast "DLC enregistrée" (9,5 → 30,5 s).
5. Réouverture du menu d'action → **Température** : ajustement (+4,0°C →
   +4,5°C), "Enregistrer" → toast "Température enregistrée" (32,0 → 36,5 s).
6. Réouverture du menu d'action → **Scanner produit** : viseur caméra "Pointez
   vers le code-barres" (38,0 → 42,0 s).
7. Résultat : la ligne produit passe à "Complété", avec DLC et température
   renseignées (45,0 → 47,96 s).

## Voix off (9 lignes)

| # | Texte | Durée | Segment |
|---|---|---:|---|
| N0 | Après une livraison, contrôlez chaque produit reçu directement depuis FoodEatUp. | 4,21 s | intro + A |
| N1 | Ouvrez la commande livrée pour retrouver la liste des produits. | 3,06 s | B |
| N2 | Depuis l'action sur un produit, ajoutez sa DLC : par photo de l'étiquette, ou en saisissant la date. | 6,03 s | clic C + D |
| N3 | Modifiez la température de réception du produit en quelques secondes. | 3,37 s | clic F + G |
| N4 | Et scannez le code-barres du produit pour l'identifier instantanément. | 3,53 s | clic I + J |
| N5 | Chaque produit reçu est ainsi tracé : DLC, température et référence, prêts pour vos contrôles HACCP. | 7,97 s | K — bénéfice |
| N6 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | 4,41 s | claude1+2 |
| N7 | Collez-le dans la conversation : l'étiquette HACCP du produit est créée en quelques secondes. | 5,75 s | claude3 |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (réutilisé de `foodeatup-produits-tuto/vo/N8.mp3`) |

## Découpage

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 2,60 s | SCANNER LE CODE EAN ET LA DLC |
| A | 0,00 → 2,00 | 2,40 s | "Réception du jour", commandes à contrôler |
| B | 6,00 → 8,70 | 3,60 s | Commande livrée, tableau "Produits livrés" |
| C | 8,70 → 9,30 | 0,70 s | **zoom-punch** sur le menu d'action "..." (1683, 424) |
| D | 9,50 → 29,50 | 6,00 s | Photo DLC : photo + date + Enregistrer |
| E | 30,00 → 30,50 | 1,00 s | Toast "DLC enregistrée" |
| F | 32,00 → 32,50 | 0,70 s | **zoom-punch** sur le menu d'action (1683, 424) |
| G | 33,00 → 35,50 | 3,20 s | Température : +4,0°C → +4,5°C, Enregistrer |
| H | 36,00 → 36,50 | 1,00 s | Toast "Température enregistrée" |
| I | 38,00 → 38,50 | 0,70 s | **zoom-punch** sur le menu d'action (1683, 424) |
| J | 40,00 → 42,00 | 3,50 s | Scanner produit : viseur caméra |
| K | 45,00 → 47,96 | 8,50 s | Produit "Complété" (DLC + température) |
| claude1 | carte générée | 2,20 s | reveal — prompt en gros, fond crème |
| claude2 | carte générée | 1,30 s | confirmation « Copié dans le presse-papiers ! » |
| claude3 | carte générée | 2,50 s | mockup chatbot Claude |
| outro | carte | 6,20 s (auto-étendue si besoin) | CTA |

Coordonnées mesurées sur les frames réelles. Même bouton de menu ("...") réutilisé
pour les 3 zoom-punchs (Photo DLC, Température, Scanner produit s'ouvrent tous
depuis le même menu contextuel) — répétition volontaire pour ancrer le geste.

## Séquence Claude — module partagé

`mcp__Foodeatup__create_haccp_label(establishment_id, ingredient_name, dlc?,
temperature?, storage_location?, lot_number?, ...)` couvre exactement DLC +
température d'un produit reçu (le scan EAN lui-même est une action caméra,
sans équivalent MCP — non montré côté Claude).

> Voici la photo de l'étiquette du produit reçu : [joindre la photo]. Crée
> l'étiquette HACCP correspondante (DLC, température de réception) pour mon
> établissement FoodEatUp (ID [ID établissement]).

Même texte côté fiche Lovable (`claudePrompts[0]`), + un second prompt direct
sans photo (`claudePrompts[1]`) :

> Crée une étiquette HACCP pour [nom du produit] reçu aujourd'hui, avec une
> DLC au [date] et une température de réception de [température]°C, pour mon
> établissement FoodEatUp (ID [ID établissement]).

## Animations

Mêmes principes que la série : `setpts` pour la vitesse, zoom-punch en crop
fixe (3x, même bouton), bandeaux en position statique (bug `drawbox`
eval=init documenté sur `foodeatup-predibot-suggestions-tuto`), xfade 0,28 s,
cartes intro/outro en fond flou + overlay net, séquence Claude 3 temps
(module partagé `videos/_shared/claude_prompt_sequence.py`).

## Statut publication

Vidéo montée suite à la demande explicite de Michael. Publication Lovable
uniquement (FoodEatUp Academy, module HACCP), comme demandé.
