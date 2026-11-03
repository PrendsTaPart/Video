# Tutoriel — Créer une traçabilité simplifiée

Module HACCP, sous-catégorie « Traçabilité simplifiée (photo express, sans produit ni lot) ».
Source : `assets/screen.mp4` (1920x828, 41,28 s, H.264/AAC), fourni par Michael, avec
`assets/intro.jpg` (carte d'ouverture fournie) et `assets/outro.jpg` (carte CTA générique,
réutilisée telle quelle depuis les tutos précédents).

**STATUT : brouillon soumis à validation — aucune VO générée, aucun montage lancé.**

## Analyse de la vidéo source (frames extraites à ffmpeg)

Déroulé réel observé (timestamps sur `screen.mp4`) :

| t | Écran |
|---:|---|
| 0,0 – 3,6 s | Page « Traçabilité » : 2 cartes, « Traçabilité simplifiée » (bleu, icône appareil photo) et « Traçabilité complète » (orange) |
| ~3,6 s | Clic sur la flèche de la carte « Traçabilité simplifiée » |
| 4,0 – 5,7 s | Modal « Traçabilité simplifiée » : bouton « Prendre une photo » |
| ~5,7 s | Clic sur « Prendre une photo » → activation de l'appareil photo |
| 6,0 – 8,0 s | Aperçu caméra (cadre noir dans cet enregistrement) + bouton « Prendre la photo » |
| ~8,0 s | Clic sur « Prendre la photo » → photo capturée |
| 8,3 – 9,0 s | Vignette capturée + lien « Reprendre une photo » ; Date et Heure déjà pré-remplies (28/07/2026, 13:22) ; bouton Enregistrer actif |
| 10 – 12 s | *(artefact d'enregistrement, à couper au montage)* second clic sur « Reprendre une photo » → erreur navigateur « Erreur d'accès à la caméra : Permission dismissed », fermée via OK. Pas une étape produit, ne sera ni montrée ni commentée. |
| 12 – 29 s | Saisie du champ « Remarques optionnelles » (texte « remarques ») — beaucoup de temps mort réel, sera compressé au montage |
| ~34 – 36 s | Clic sur « Enregistrer » → retour à la page Traçabilité |
| 36 – 41 s | Page Traçabilité (état final) |

## Voix off (8 lignes, voix Adam FR `TGAegA0zNRi8I6nUdq3i`)

| # | Texte | Ancrage |
|---|---|---|
| N0 | Besoin de tracer un plat sans perdre de temps ? La traçabilité simplifiée fait ça en une photo. | carte d'intro |
| N1 | Ouvrez le module Traçabilité, et cliquez sur la carte Traçabilité simplifiée. | clic sur la carte |
| N2 | Cliquez sur Prendre une photo pour activer l'appareil photo. | clic « Prendre une photo » |
| N3 | Prenez la photo : pas besoin de sélectionner un produit ni un numéro de lot. | clic « Prendre la photo » / vignette capturée |
| N4 | La date et l'heure se remplissent toutes seules ; ajoutez une remarque si vous le souhaitez. | champ Remarques |
| N5 | Cliquez sur Enregistrer : votre traçabilité est aussitôt ajoutée à l'historique. | clic Enregistrer |
| N6 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | séquence Claude — étage 1+2 (reveal + copié) |
| N7 | Collez-le dans la conversation : votre traçabilité simplifiée est enregistrée en quelques secondes. | séquence Claude — étage 3 (mockup chatbot) |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | carte de fin (CTA) — **réutilise le .mp3 existant**, ne pas régénérer |

Durée cible totale visée : ~40-45 s (comparable aux tutos HACCP déjà publiés : 41-64 s).

## Découpage envisagé

- Carte intro (image fournie par Michael)
- A — page Traçabilité (0,2→3,6 recadré court, ~2,0 s)
- B — zoom-punch sur la flèche de la carte « Traçabilité simplifiée »
- C — modal, bouton « Prendre une photo » (~1,5 s)
- D — zoom-punch sur « Prendre une photo »
- E — aperçu caméra + « Prendre la photo » (~1,5 s)
- F — zoom-punch sur « Prendre la photo »
- G — vignette capturée + Date/Heure pré-remplies (~1,5 s)
- H — remarque tapée dans le champ (segment recomposé/accéléré, l'attente réelle de la vidéo source n'est pas gardée telle quelle)
- I — zoom-punch sur « Enregistrer »
- J — retour page Traçabilité (~1,3 s)
- claude1/2/3 — séquence Claude partagée (`videos/_shared/claude_prompt_sequence.py`)
- Carte outro (CTA, image réutilisée)

Le passage « erreur caméra / Reprendre une photo » (10-12 s dans la source) est purement un
aléa de l'enregistrement (pas de caméra réelle disponible côté machine d'enregistrement) : il
est **coupé au montage**, ni montré ni commenté en VO — ce n'est pas un comportement du
produit à documenter.

## Séquence Claude — outil MCP identifié

`mcp__FoodEatUp__create_haccp_tracabilite(establishment_id, type="simple", remarques=...)`
correspond exactement à l'action « Traçabilité simplifiée » (le paramètre `type` vaut
`"simple"` par défaut, sans `lot`/`reference_id` requis — c'est la différence documentée avec
`type: "complete"`, qui correspond à la carte « Traçabilité complète »). Séquence à 3 temps
(reveal → copié → mockup chatbot Claude) via le module partagé, prompt identique côté vidéo et
côté fiche Lovable (`claudePrompt`) :

> Crée une traçabilité simplifiée avec la remarque [remarque optionnelle] pour mon
> établissement FoodEatUp (ID [ID établissement]).

## Fiche Lovable prévue (`howItWorks` / `whatItsFor` / `chefTip`)

Textes déjà rédigés lors d'un essai précédent (voir historique) et repris à l'identique pour
la republication après validation :

- **howItWorks** : ouvrir le module Traçabilité → carte « Traçabilité simplifiée » → « Prendre
  la photo » (sans produit ni lot) → date/heure pré-remplies + remarque optionnelle →
  Enregistrer.
- **whatItsFor** : preuve de traçabilité en quelques secondes pour ce qui n'a pas de référence
  produit/lot précise (plat du jour, buffet, préparation maison).
- **chefTip** : réserver la traçabilité simplifiée aux plats sans référence produit claire ;
  garder la traçabilité complète pour les produits à lot/DLC stricts — les deux cohabitent
  dans le même historique.

## Prochaines étapes (bloquées tant que ce script n'est pas validé)

1. Validation du texte VO ci-dessus par Michael (ce document).
2. Génération des 7 nouvelles lignes VO (N0-N7 ; N8 réutilisé tel quel) via ElevenLabs, voix
   Adam FR.
3. Montage (`build.py`) avec le moteur commun de la série (setpts, zoom-punch, loudnorm par
   ligne, séquence Claude partagée).
4. Livraison de la vidéo finie à Michael pour validation (deuxième STOP obligatoire, avant
   toute publication).
5. Une fois validée seulement : upload RapidoCMS, remplacement de l'entrée Lovable actuelle
   (actuellement publiée avec la vidéo brute, à corriger), et schedule LinkedIn.
