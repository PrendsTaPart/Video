# ÉTAPE 0 — Exploration du dépôt & plan d'exécution

> Vidéo « FoodEatUp — le tutoriel complet en 5 minutes » — 16:9 1920×1080, VO française,
> avatar Mika en ouverture de chaque chapitre, visuels de transition RapidoCMS.

## 1. Pipeline existant identifié

Le dépôt contient déjà un pipeline complet et éprouvé pour exactement ce format —
**`videos/rapido-formation-5min/`** (16:9, 3:45, livré) est le gabarit de référence :

- **Corps de vidéo** : compositions HyperFrames **locales** (HTML/GSAP, skills
  `/hyperframes` installés), frames par scène dans `compositions/frames/`, storyboards
  `STORYBOARD-A/B/C.md` → `captions.mjs` → `assemble-index.mjs` → `npm run check` →
  `npm run render` (rendu MP4 local, gratuit).
- **Clips avatar Mika** : **API HeyGen Avatar REST directe** (`POST /v2/video/generate`,
  avatar_id `648209ec82414565864f1771aa1d763e`, voix `f6dec6ea26b6484eb142cc8224abb1fc`),
  clip MP4 téléchargé puis intégré au montage. C'est la seule action payante du pipeline.
- **Montage final** : concat ffmpeg (clips Mika + corps HyperFrames), BGM en loop,
  loudnorm -16 LUFS, sous-titres corrigés sur le verbatim du script (règle FoodEatUp).
- **Charte FoodEatUp vidéo** (studio-video/CLAUDE.md + shared-images) : fond off-white
  `#F7F9FC`, texte navy `#1B2A41`, accent bleu `#1E9BF0`, Poppins/Inter, logos dans
  `videos/shared-images/brand/`, personnages 3D réutilisables dans
  `videos/shared-images/characters/`.
- **RapidoCMS** : `generate_image` (visuels sans texte incrusté) + `upload_file_tool`
  (`company_id 321`, archivage systématique de chaque MP4 rendu — règle standing).

### ⚠️ Point d'arbitrage : MCP HyperFrames vs pipeline local

Le connecteur MCP `HyperFrames_by_HeyGen` est branché, mais ses propres instructions
(et la mémoire du studio, confirmée le 2026-07-02) indiquent que **`compose` et
`render_video` sont désactivés depuis un agent CLI avec système de fichiers** (notre cas)
— ils renvoient un rejet pointant vers les skills locaux. Deux options :

- **Option A (recommandée)** — pipeline local éprouvé : compositions HyperFrames dans le
  repo (`npm run render`, gratuit, QA image par image) + clips Mika via l'API HeyGen
  Avatar (payant, validé avant lancement). C'est la recette qui a produit toutes les
  vidéos du repo, dont la formation 16:9 de 3:45.
- **Option B** — tenter quand même `mcp compose` pour obtenir un projet hébergé
  app.heygen.com avec lien de preview partageable ; risque de rejet documenté, et
  l'avatar Mika devra de toute façon passer par l'API Avatar.

## 2. Accès & secrets

| Accès | État |
|---|---|
| MCP RapidoCMS (`generate_image`, `upload_file_tool`) | ✅ connecté (company_id 321) |
| MCP HyperFrames by HeyGen (lecture) | ✅ connecté |
| MCP HyperFrames `compose`/`render_video` | ⚠️ documenté comme rejeté depuis cet environnement |
| `HEYGEN_API_KEY` (`/home/user/Video/.env`) | ❌ **absent de ce clone** (jamais commité — normal) → **bloquant pour les clips Mika + TTS HeyGen** |
| `ELEVENLABS_API_KEY` (`studio-video/.env`) | ❌ absent → bloquant pour la VO Adam ElevenLabs |

→ **Michael doit refournir la/les clés** (HEYGEN_API_KEY a minima) avant les étapes 4-5,
sinon repli sur TTS local Kokoro (qualité moindre) et pas d'avatar Mika possible.

## 3. Inventaire des captures (20/20 sauvegardées)

Uploads copiés dans **`assets/screens/foodeatup/`** avec les noms du mapping, après
vérification visuelle de chaque image. **2 écarts vs le mapping imposé** :

| Attendu (mapping) | Reçu à la place | Contenu réel vérifié |
|---|---|---|
| `mes-productions.png` (Ch.7) | `tableau-de-bord.png` | Tableau de bord (stock critique, valeur stock, rotation, graphes) |
| `creer-devis.png` (Ch.7) | `ajout-ingredient.png` | Formulaire « Ajout d'un Ingrédient » (stock, allergènes, nutrition) |

Proposition : `ajout-ingredient.png` → **Ch.4** (produits/ingrédients/recettes, il y a sa
place naturelle) et `tableau-de-bord.png` → **Ch.7** (exploitation/pilotage/PrediBot).
Les 18 autres correspondent exactement au mapping.

## 4. Dossier de travail

`videos/foodeatup-tutoriel-5min/` créé avec `script/`, `storyboard/`,
`assets-generes/`, `composition/`.

## 5. Divergence de branche

Le prompt demande une branche `feature/video-tutoriel-foodeatup-5min`, mais cette session
est contrainte à la branche **`claude/foodeatup-tutoriel-video-5l4uoa`** (consigne
système : ne jamais pousser ailleurs). Tout le travail sera livré sur cette branche.
