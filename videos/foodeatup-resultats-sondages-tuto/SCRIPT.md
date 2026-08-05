# Tutoriel — Résultats des sondages (historique)

Module **Marketing, Fidélité & Iris**, catalogue `videos/CATALOGUE-157-TUTORIELS.md`
module 8, entrée 18 : « Résultats des **Sondages** (historique) ». Fiche Lovable
préexistante en placeholder (`slug: "resultats-des-sondages-historique"`, "en cours de
tournage", `videoUrl: ""`) — à mettre à jour, pas à dupliquer. Sondage voisin
(`creer-un-sondage-fidelite`, #17) laissé intact — pas les mêmes intrants.

Rush fourni par Michael (`assets/screen.mp4`, 1920x828, 25 fps, **30,80 s**, voix off
100% ElevenLabs comme le reste de la série).

## Ce que montre le rush

1. **0,00 → ~4,00 s** — Fidélité & jeux, onglet **Sondages** : carte « sondage express »
   (Actif, 3 questions, déclencheur lien/QR, récompense 15 pts), boutons **Lien /
   Résultats (0) / Modifier / Supprimer**.
2. **~4,00 → ~6,00 s** — Clic **Lien** → confirmation **« Lien copié ✓ »**.
3. **~6,00 → ~8,00 s** — Ouverture du lien : page publique du sondage (vue client,
   « GoSushi Démo »), chargement.
4. **~8,00 → ~18,50 s** — Remplissage du sondage côté client (démo) : note 4/5 étoiles,
   score de recommandation **5** (échelle 0-10), case **« service »** cochée pour « qu'avez-
   vous le plus apprécié », email optionnel laissé vide, clic **« Envoyer mes réponses »**.
5. **~19,00 → ~20,50 s** — Confirmation **« Merci pour votre avis ! »**.
6. **~20,50 → ~22,50 s** — Retour côté marchand, onglet Sondages.
7. **~22,50 → 30,80 s** — Clic **Résultats** → page **« Sondage express — 1 réponse(s) »** :
   Note moyenne **4/5**, **Score NPS : -100** (cohérent : une seule réponse à 5/10 classe
   en détracteur sur l'échelle NPS, donc 100% détracteurs), détail « Qu'avez-vous le plus
   apprécié » — Service : 1.

## Voix off (9 lignes) — brouillon, en attente de validation Michael

| # | Texte | Segment |
|---|---|---|
| N0 | Retrouvez les résultats de vos sondages fidélité, en un coup d'œil. | intro |
| N1 | Depuis Fidélité et jeux, onglet Sondages, retrouvez votre sondage actif. | A — page + carte sondage |
| N2 | Partagez le lien ou le QR code : vos clients répondent en quelques secondes. | B — clic Lien + copié |
| N3 | Note, score de recommandation, ce qu'ils ont préféré : trois questions, une récompense en points. | C — remplissage démo |
| N4 | Une fois la réponse envoyée, retrouvez-la aussitôt dans Résultats. | D — merci + retour + clic Résultats |
| N5 | Note moyenne, score NPS, réponses détaillées : tout est calculé automatiquement. | E — page résultats |
| N6 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | claude1+2 (réutilisable) |
| N7 | Collez-le dans la conversation : les résultats de votre sondage s'affichent aussitôt. | claude3 (spécifique) |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | carte de fin CTA (réutilisable) |

Voix Adam FR — Instructor (`TGAegA0zNRi8I6nUdq3i`, `eleven_multilingual_v2`). N6/N8
candidats à la réutilisation telle quelle depuis `foodeatup-tva-tuto/vo/`.

## Séquence Claude — module partagé

Outil trouvé : `get_survey_results(establishment_id, survey_id)` — correspondance
directe et sans réserve avec l'écran « Résultats » montré dans le rush (moyennes, NPS,
répartitions).

> Affiche les résultats de mon sondage fidélité (ID [ID du sondage]) pour mon
> établissement FoodEatUp (ID [ID établissement]).

Même texte côté fiche Lovable (`claudePrompt`).

## Découpage prévu (à affiner au montage)

| Seg | Source | Contenu |
|---|---|---|
| intro | carte (fournie par Michael) | RÉSULTATS SONDAGES |
| A | 0,00 → ~4,00 | onglet Sondages, carte "sondage express" |
| B | ~4,00 → ~6,00 | clic Lien + "Lien copié" (zoom-punch) |
| C | ~8,00 → ~18,50 | remplissage démo du sondage (étoiles, NPS, checkbox, envoyer) |
| D | ~19,00 → ~22,50 | merci + retour marchand + clic Résultats (zoom-punch) |
| E | ~22,50 → 30,80 | page Résultats (moyenne, NPS, détail réponses) |
| claude1 | carte générée | reveal — prompt en gros, fond crème |
| claude2 | carte générée | confirmation « Copié dans le presse-papiers ! » |
| claude3 | carte générée | mockup chatbot Claude |
| outro | carte (fournie par Michael, CTA générique réutilisée) | CTA |

## Assets reçus

- `assets/intro.jpg` — carte "RÉSULTATS SONDAGES" (fournie).
- `assets/outro.jpg` — carte CTA générique FoodEatUp (hash MD5 identique à celle déjà
  utilisée sur toute la série — zéro travail de design).
- `assets/screen.mp4` — rush 1920x828, 25 fps, 30,80 s.

## Statut

**Script validé.** VO générée (ElevenLabs Adam FR Instructor pour N0-N5/N7 ; N6/N8
réutilisées telles quelles depuis `foodeatup-tva-tuto/vo/`, texte identique).

**Montage terminé** — `out/foodeatup-resultats-sondages-tuto-v1.mp4`, **53,00 s**,
H.264 High/yuv420p, 1920×828, 25 fps, AAC 48 kHz stéréo, +faststart (moov avant mdat
confirmé), decode 0 erreur. Peak audio **-7,23 dBFS**. Bandeaux d'étape avec le
correctif `drawtext` double-passage. Zoom-punch vérifié sur le bouton "Résultats".
Séquence Claude vérifiée avec accents français corrects. Chaque ligne VO vérifiée
dans la fenêtre de son segment visuel. Vignette `out/thumbnail-youtube.jpg` (1280×720,
crop neutre de la carte d'intro).

**Publiée** (2026-08-05). Livrée à Michael pour validation (`SendUserFile`) → validée
("tu peux publier") → publication :

- Upload RapidoCMS (vidéo + vignette) via `upload_file_tool` → S3 :
  `foodeatup-resultats-sondages-tuto-v1` / `-thumbnail`.
- Fiche Lovable préexistante en placeholder (`resultats-des-sondages-historique`) mise à
  jour avec vidéo/vignette/étapes/astuce du chef/prompt Claude plutôt que dupliquée
  (commit `69d1d3b`).
- Site redéployé (`deploy_project`) → https://foodeatup-guide-star.lovable.app
- Pas de créneau LinkedIn programmé dans cette session (non demandé).
