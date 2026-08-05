# Tutoriel — Gérer les récompenses fidélité

Module **Marketing, Fidélité & Iris**, catalogue `videos/CATALOGUE-157-TUTORIELS.md`
module 8, entrée 13 : « Gérer les **Récompenses** fidélité ». Fiche Lovable préexistante
en placeholder (`slug: "gerer-les-recompenses-fidelite"`, "en cours de tournage",
`videoUrl: ""`) — à mettre à jour, pas à dupliquer.

Rush fourni par Michael (`assets/screen.mp4`, 1920x828, 25 fps, **88,48 s**, piste vidéo
uniquement — voix off 100% ElevenLabs comme le reste de la série).

## Ce que montre le rush

1. **0,00 → ~4,00 s** — Page **Fidélité & jeux**, onglet **Récompenses** : 4 indicateurs
   (Membres fidélité 4, Points en circulation 15, Points distribués 25, Bons à valider 0),
   **Catalogue de récompenses**, légende *« Produit = plat offert · Bon € = réduction ·
   Avantage = validé en salle. Stock vide = illimité. »*
2. **~4,00 → ~30,00 s** — **Modifie une récompense existante** : « 5 EUR offerts »
   (type Bon €) → change le **Type** en **Produit**, sélectionne le **Plat** « Chirashi
   Saumon (19.90 €) », modifie le **Libellé**, ajuste le **Coût en points** (10→80), le
   **Stock** (→100) et le **Quota / client** (→5). Coche **Récompense active** déjà
   cochée.
3. **~30,00 → ~32,50 s** — Clic **« Enregistrer le catalogue »** → confirmation
   **« Catalogue enregistré ✓ »**.
4. **~35,00 → ~58,00 s** — **Ajoute une nouvelle récompense** (bouton **+ Récompense**) :
   Type **Bon €**, Libellé « Bon 5 € », Coût en points 100, **Valeur (€)** 5, Quota/client
   5, Stock illimité (placeholder).
5. **~61,00 → 88,48 s** — **Ajoute une troisième récompense** : Type **Avantage** (pas de
   champ Plat ni Valeur — juste Libellé/Coût/Stock/Quota), Libellé « café offert »,
   Coût en points 2, Quota/client 10. Clic **« Enregistrer le catalogue »** →
   confirmation finale **« Catalogue enregistré ✓ »** (dernière frame du rush).

## Voix off (10 lignes) — brouillon, en attente de validation Michael

| # | Texte | Segment |
|---|---|---|
| N0 | Gérez tout votre catalogue de récompenses fidélité, en quelques clics. | intro |
| N1 | Depuis Fidélité et jeux, onglet Récompenses, retrouvez votre catalogue existant. | A — page + légende |
| N2 | Trois types de récompenses : Produit pour un plat offert, Bon euro pour une réduction, Avantage pour un service validé en salle. | A — légende |
| N3 | Modifiez une récompense en changeant son type, son plat et son coût en points. | B — édition récompense 1 |
| N4 | Ajustez le stock et le quota par client, puis cliquez sur Enregistrer le catalogue. | B/C — stock/quota + save |
| N5 | Ajoutez une nouvelle récompense en un clic : ici, un bon de cinq euros. | D — nouvelle récompense Bon € |
| N6 | Ou un avantage comme un café offert, sans plat à sélectionner : de quoi varier vos récompenses. | E — récompense Avantage |
| N7 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | claude1+2 (réutilisable depuis un tuto existant) |
| N8 | Collez-le dans la conversation : votre récompense est créée en quelques secondes. | claude3 (spécifique) |
| N9 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | carte de fin CTA (réutilisable) |

Voix Adam FR — Instructor (`TGAegA0zNRi8I6nUdq3i`, `eleven_multilingual_v2`). N7/N9
candidats à la réutilisation telle quelle depuis `foodeatup-tva-tuto/vo/` (texte
identique à N6/N8 de cette référence).

## Séquence Claude — module partagé

Outil trouvé : `upsert_loyalty_reward(establishment_id, kind, label, points_cost,
plat_id?, amount?, stock?, active?, reward_id?)` — correspondance directe et complète :
`kind` couvre les 3 types vus à l'écran (`product`/`amount`/`perk`), et l'outil sert
aussi bien la création que la modification (`reward_id` optionnel). Meilleure
correspondance MCP rencontrée sur la série jusqu'ici — aucune réserve à signaler.

> Crée une récompense de fidélité de type [Produit / Bon € / Avantage], intitulée
> [libellé], à [coût en points] points, pour mon établissement FoodEatUp (ID [ID
> établissement]).

Même texte côté fiche Lovable (`claudePrompt`).

## Découpage prévu (à affiner au montage)

| Seg | Source | Contenu |
|---|---|---|
| intro | carte (fournie par Michael) | GÉRER LES RÉCOMPENSES |
| A | 0,00 → ~4,00 | page Fidélité & jeux, KPIs, légende des 3 types |
| B | ~4,00 → ~28,00 | édition récompense 1 : Bon €→Produit, plat, libellé, points |
| C | ~28,00 → ~32,50 | stock/quota + clic Enregistrer + confirmation (zoom-punch) |
| D | ~35,00 → ~58,00 | nouvelle récompense Bon € (5 €) |
| E | ~61,00 → 88,48 | nouvelle récompense Avantage (café offert) + save final |
| claude1 | carte générée | reveal — prompt en gros, fond crème |
| claude2 | carte générée | confirmation « Copié dans le presse-papiers ! » |
| claude3 | carte générée | mockup chatbot Claude |
| outro | carte (fournie par Michael, CTA générique réutilisée) | CTA |

Rush riche (3 récompenses démontrées) — la vidéo finale sera probablement plus longue
que la moyenne de la série (~70-90 s au lieu de 50-60 s) pour laisser respirer chaque
type de récompense plutôt que de tout compresser.

## Assets reçus

- `assets/intro.jpg` — carte "GÉRER LES RÉCOMPENSES" (fournie).
- `assets/outro.jpg` — carte CTA générique FoodEatUp (hash MD5 identique à celle déjà
  utilisée sur toute la série — zéro travail de design).
- `assets/screen.mp4` — rush 1920x828, 25 fps, 88,48 s.

## Statut

**Script validé.** VO générée (ElevenLabs Adam FR Instructor pour N0-N6/N8 ; N7/N9
réutilisées telles quelles depuis `foodeatup-tva-tuto/vo/`, texte identique).

**Montage terminé** — `out/foodeatup-gerer-recompenses-tuto-v1.mp4`, **70,64 s**,
H.264 High/yuv420p, 1920×828, 25 fps, AAC 48 kHz stéréo, +faststart (moov avant mdat
confirmé), decode 0 erreur. Peak audio **-7,30 dBFS** (marge saine sous le limiteur
`alimiter=0.6`). Bandeaux d'étape avec le correctif `drawtext` double-passage (pas
`drawbox`). Deux zoom-punch vérifiés (bouton "Enregistrer le catalogue", 1er et 2e
clics, coordonnées mesurées par seuillage colorimétrique sur chaque frame de clic
réelle — la position y diffère car le catalogue a une ligne de plus au 2e clic).
Séquence Claude vérifiée avec accents français corrects. Chaque ligne VO vérifiée dans
la fenêtre de son segment visuel (script de vérification dédié) — un léger débordement
de N2 sur le segment B (0,2 s) jugé sans conséquence (même contexte visuel). Vignette
`out/thumbnail-youtube.jpg` (1280×720, crop neutre de la carte d'intro).

**Publiée** (2026-08-05). Livrée à Michael pour validation (`SendUserFile`) → validée
("je valide") → publication :

- Upload RapidoCMS (vidéo + vignette) via `upload_file_tool` → S3 :
  `foodeatup-gerer-recompenses-tuto-v1` / `-thumbnail`.
- Fiche Lovable préexistante en placeholder (`gerer-les-recompenses-fidelite`) mise à
  jour avec vidéo/vignette/étapes/astuce du chef/prompt Claude plutôt que dupliquée
  (commit `9085bae`).
- Site redéployé (`deploy_project`) → https://foodeatup-guide-star.lovable.app
- Pas de créneau LinkedIn programmé dans cette session (non demandé).
