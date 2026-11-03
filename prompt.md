# prompt.md — relance des vidéos tutoriels FoodEatUp

Prompt à donner à l'agent qui reprend la production des vidéos tutoriels. Mis à jour le 03/11/2026 (audit : 171 vidéos).

## Ta mission

Produire les vidéos manquantes des fiches de l'Académie FoodEatUp (https://tutoriel.foodeatup.com/), une à une,
puis les publier pour qu'elles apparaissent dans le logiciel FoodEatUp.

Source de vérité de la liste : **`mouna.md`** du dépôt `PrendsTaPart/stockvisionai` (générée par
`scripts/academie/generer_mouna.py`). Dans ce dépôt : `tutoriels-foodeatup/` (liste, dossiers Drive, un script
de voix off et un plan de tournage par vidéo). Lire d'abord `tutoriels-foodeatup/README.md`.

## Chaîne de production (une vidéo = un dossier Google Drive)

Dossier Drive racine : https://drive.google.com/drive/folders/1LpWivm0KEPwX5XhNHiw08426NjT6PXHC
Arborescence : `16 - À TOURNER/NN - module/NNN - Titre de la vignette (slug)/01-vignette (Zied)` et `02-rushes (Mouna)` (identifiants dans `tutoriels-foodeatup/drive-dossiers.json`). Montage et publication : bibliothèque RapidoCMS.

1. **Vignette** — Zied : PNG 1280×720, titre exact de la liste, charte FoodEatUp (bleu #0066FF, orange #FFA500, bleu nuit #0F1A23).
2. **Rushes** — Mouna : capture d'écran du logiciel, tournée sur le **restaurant école** (Configuration › Mode école),
   jamais sur les données d'un vrai client.
3. **Montage + voix** — Claude (toi) : MP4 1080p, 40 à 90 s, voix Adam `TGAegA0zNRi8I6nUdq3i`, ElevenLabs `eleven_v4`, une prise, script `tutoriels-foodeatup/scripts/NNN-slug.md`,
   sous-titres .srt, aucun prix ni chiffre inventé, outils de `academie-pipeline/`.
4. **Publication** — Claude : YouTube, puis lien YouTube posé sur la fiche de l'Académie (projet Lovable
   `55ff35b7-c442-42c4-950c-8c7fd420c645`). Ensuite, dans `stockvisionai`, régénérer le catalogue
   (`python3 scripts/academie/generer_catalogue.py` avec le dépôt `foodeatup-guide-star-227b4772` cloné à côté),
   PR vers `production`. La vidéo apparaît alors seule : bouton info (popup tutoriel) de l'écran, onglet Apprendre
   du Chef, « En savoir plus » des missions du mode école, guide « Cette page ».

## Règles

- Ne marque jamais une vidéo publiée tant que le lien YouTube ne répond pas.
- Une vidéo à la fois : vignette + rushes présents dans Drive avant le montage ; sinon, passe à la suivante et note le manque.
- Tiens à jour, à la fin de chaque séance, la colonne « état » dans `RAPPORT-VIDEOS.md` de ce dépôt.

## Liste

Voir `tutoriels-foodeatup/mouna.md` (171 vidéos, titres de vignette, dossiers Drive, remarques de tournage).
