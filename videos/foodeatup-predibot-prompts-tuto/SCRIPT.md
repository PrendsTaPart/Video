# Tutoriel — Parler à PrediBot avec nos prompts (module PrediBot, Agent IA Directeur)

Troisième et dernière vidéo attendue du module **PrediBot (Agent IA Directeur)** (`predibot`,
2/3 déjà publiées : `predire-ses-commandes`, `foodeatup-predibot-suggestions-tuto`), catalogue
`videos/CATALOGUE-157-TUTORIELS.md` § 11b : « 03 Parler à **PrediBot** avec nos prompts ».

Intrants reçus de Michael (dans le chat, pas via un dossier Drive) :
- `assets/screen.mp4` — capture d'écran réelle (62,9 s, 1526x1032, 25 fps), conversation
  WhatsApp avec **PredBot** (StockVisionAI), pas un enregistrement de clics dans l'app.
- `assets/intro.jpg` — carte d'ouverture fournie telle quelle ("AGENT GESTION STOCK", visuel
  homme en costume + REJOIGNEZ-NOUS), utilisée sans redesign (règle du workflow).
- `assets/outro.jpg` — carte de fin CTA, **identique** (md5 vérifié) à celle déjà utilisée sur
  toute la série (ex. `foodeatup-predibot-suggestions-tuto/assets/outro.jpg`).

## Ce que montre le rush

Contrairement aux tutos "clic dans l'app", ce rush est un fil de conversation WhatsApp avec
l'agent IA StockVisionAI (alias **PredBot**) qui répond en langage naturel et agit réellement
dans FoodEatUp :
1. `~4,5–14s` — **"Liste mes stocks"** → liste des derniers articles ajoutés (sur 182 au
   total), avec ruptures marquées **CRITIQUE**, seuils, emplacement, fournisseur, péremption.
2. `~14–21s` — **"Liste mes recettes"** → fiches techniques (catégorie, temps de préparation,
   portions, ingrédients) sur 32 recettes au total.
3. `~21–27s` — **"vérifie le fournisseur louay"** → fiche fournisseur complète (ID, adresse,
   ville, téléphone, email, statut, fiabilité) avec lien direct vers la fiche FoodEatUp.
4. `~27–31s` — **"Crée une commande fournisseur"** → l'agent redemande les champs requis (ID
   fournisseur, produit, quantité, unité, date prévue, prix optionnel).
5. `~36,5–40s` — l'utilisateur fournit les champs (fournisseur 109, Paprika fumé, 3 kg,
   2026-08-19) → confirmation avec référence `CMD-20260710151345-109` et emails envoyés.
6. `~31–36,5s` — bascule vers l'app FoodEatUp réelle, écran **Gestion des Livraisons** :
   preuve que l'action de l'agent écrit vraiment dans le logiciel, pas une simulation.
7. `~48–62s` — **"Génère le dashboard stock"** → bascule vers le **Dashboard Stock FoodEatUp**
   généré à la volée : 39 stocks critiques, 193 835,36 € de valeur totale, 26 fournisseurs
   actifs, graphique quantité/seuil et tableau détaillé.

Segments `31–36,5s` et `36,5–40s` sont réordonnés au montage (commande d'abord confirmée dans
le chat, puis preuve dans l'app) pour une lecture plus naturelle que l'ordre brut du rush.
`0–4,5s` (reliquat d'un défilement RH sans rapport, avant le premier message du rush) est coupé.

## Voix off (9 lignes, voix Adam FR `TGAegA0zNRi8I6nUdq3i`, `eleven_multilingual_v2`)

| # | Texte | Ancrage |
|---|---|---|
| N0 | Suivre son stock, ses recettes et ses fournisseurs en plein coup de feu, sans ouvrir dix écrans ? Il suffit d'écrire à PrediBot, l'agent IA de FoodEatUp. | intro + A |
| N1 | Liste mes stocks : et voilà vos derniers articles, avec les ruptures signalées en critique. | A (fin) / B |
| N2 | Liste mes recettes : vos fiches techniques, ingrédients et temps de préparation, en un message. | B |
| N3 | Vérifiez un fournisseur d'un coup, coordonnées et fiabilité comprises, avant de passer commande. | C |
| N4 | Vous pouvez même créer votre commande fournisseur depuis la conversation : produit, quantité, date — envoyée. | D + F + E |
| N5 | Un dernier message, et PrediBot génère votre dashboard stock complet : valeur du stock, fournisseurs actifs, alertes en direct. | G |
| N6 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | claude1 (réutilisé tel quel, `.mp3` copié depuis `foodeatup-predibot-suggestions-tuto/vo/N6.mp3`) |
| N7 | Collez-le dans la conversation : votre commande fournisseur est créée en quelques secondes. | claude3 |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | outro (réutilisé tel quel, `.mp3` copié depuis `foodeatup-predibot-suggestions-tuto/vo/N8.mp3`) |

Durées mesurées (`ffprobe`) : N0 9,87s · N1 4,96s · N2 5,51s · N3 5,28s · N4 6,69s · N5 7,78s ·
N6 4,41s · N7 4,83s · N8 5,02s — total voix ≈ 54,4s + 8×0,22s de gap ≈ 56,1s.

## Découpage (cibles recalibrées sur la durée des lignes VO ci-dessus)

| Seg | Source | Cible | Contenu |
|---|---|---:|---|
| intro | carte | 2,60 s | AGENT GESTION STOCK (image fournie) |
| A | 4,50 → 14,00 | 13,50 s (ralenti ~0,70×) | "Liste mes stocks" + réponse (ruptures CRITIQUE) — allongé pour absorber la fin de N0 + tout N1 sans déborder sur B |
| B | 14,00 → 21,00 | 6,00 s | "Liste mes recettes" + réponse |
| C | 21,00 → 27,00 | 6,00 s | "vérifie le fournisseur louay" + fiche fournisseur |
| D | 27,00 → 31,00 | 4,00 s | "Crée une commande fournisseur" — l'agent demande les champs |
| F | 36,50 → 40,00 | 5,00 s | Champs fournis + confirmation (réf. CMD-…) |
| E | 31,00 → 36,50 | 4,50 s | Preuve dans l'app réelle — Gestion des Livraisons |
| G | 48,00 → 62,00 | 10,00 s | "Génère le dashboard stock" → Dashboard Stock FoodEatUp |
| claude1 | carte générée | 2,20 s | reveal — prompt en gros, fond crème |
| claude2 | carte générée | 1,30 s | confirmation « Copié dans le presse-papiers ! » |
| claude3 | carte générée | 2,50 s | mockup chatbot Claude |
| outro | carte | 6,20 s (auto-étendue si besoin) | CTA |

Pas de zoom-punch : ce rush est un défilement de conversation, pas des clics sur boutons UI —
aucune coordonnée de bouton à mesurer (contrairement aux tutos "clic dans l'app").

## Séquence Claude — module partagé

Outil correspondant exactement à ce que montre le rush : `mcp__Foodeatup__create_supplier_order
(establishment_id, fournisseur_id, items[{ingredient_id, quantity, unit}], date_prevue)`.

> Crée une commande fournisseur pour mon établissement FoodEatUp (ID [ID établissement])
> auprès du fournisseur [ID fournisseur] : [quantité] [unité] de [ingrédient], livraison
> prévue le [date prévue].

Même texte côté fiche Lovable (`claudePrompt`).

## Animations

Mêmes principes que toute la série (`FOODEATUP-TUTORIELS-WORKFLOW.md`) : `setpts` pour la
vitesse (jamais `zoompan` sur la vidéo réelle), bandeaux d'étape rendus en PNG PIL (pas de
`drawbox` animé sur `t` — piège documenté, `t` vaut l'épaisseur du trait sur cet ffmpeg 6.1.1),
xfade 0,28 s partout, cartes intro/outro en fond flou + overlay net. Pas de clip avatar (voix
ElevenLabs sur toute la vidéo). Séquence "Utilisez cette fonctionnalité avec Claude" en 3 temps,
module partagé `videos/_shared/claude_prompt_sequence.py`. Aucune apostrophe dans les textes de
bandeau (piège déjà rencontré sur `foodeatup-ingredients-tuto`).

## Statut — publiée

Validée par Michael le 2026-08-04 (« publi sur lovable et Rapidocms »). Publiée sur Lovable
(`src/data/tutorials.ts`, module `stockvision-ai`, slug `gerer-son-stock-par-whatsapp`, commit
`f82f83ab`) — voir `LOVABLE-FOODEATUP-DOCS.md` pour le détail de la collision de slug évitée
avec `parler-a-predibot-avec-nos-prompts` (module `predibot`, déjà pris par une autre session
sur un rush différent). **RapidoCMS non publiée** : aucun connecteur `mcp__RapidoCMS__*`
disponible dans cette session — `videoUrl`/`thumbnailUrl` sur Lovable pointent temporairement
sur le raw GitHub de cette branche, à remplacer par les URLs S3 RapidoCMS dès que le connecteur
est accessible. LinkedIn non demandé pour cette vidéo.
