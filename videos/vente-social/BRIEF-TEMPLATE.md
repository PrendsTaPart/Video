# 🧾 Workflow de production — 1 vidéo de vente (à partir du plan-20)

Pour lancer une vidéo, remplis ce brief (les `V##` viennent de `plan-20.md`) :

```
Produis la vidéo de vente {V##} définie dans plan-20.md, en réutilisant le studio (BIBLE.md + templates).
- Pilier : {Problème→Solution / Démo 1 phrase / Fondateur / Preuve / Pédagogie / Coulisses}
- Produit : {FoodEatUp / RapidoCMS / RapidoRH / RapidoCRM / Écosystème}
- Angle / douleur : {hook 0-3 s}
- Message unique : {la seule idée à retenir}
- Template : {T1 / T2 / T3}
- Canaux : {TikTok, Reels, Facebook} et/ou {LinkedIn}
- Durée : {15-30 s vertical / 30-45 s LinkedIn}
- Captures : {fichiers écran}
- Prompt à mettre en scène (si démo) : {version courte 5-7 s}
```

## Ce que je produis pour chaque vidéo
1. **Script VO** (≤ 60 mots pour 15-30 s) : hook douleur (0-3 s) → démo/preuve → CTA « Réservez votre démo, lien en bio ». Règle **« vous pilotez, l'IA exécute »**.
2. **Storyboard** plan par plan (timecode, visuel, texte ≤ 6 mots/carton, VO), zones safe verticales.
3. **Visuels manquants** via RapidoCMS `generate_image` (charte produit, **aucun texte incrusté**) → upload biblio + copie locale.
4. **Composition** avec le template T# (`templates/studio.py`) : Mika hook, scène chat Claude si démo, lower-third produit, CTA.
5. **Exports** : master **9:16** (TikTok/Reels/FB) + version **1:1 ou 16:9** LinkedIn (caption founder-led Mo).
6. **STOP preview** → rendu seulement après GO (lot par lot).
7. **Caption + 3-5 hashtags** par canal (`#restaurant #IA #FoodEatUp #gestion` + spécifiques).

## Livraison
`videos/vente-social/{V##}/` (script, storyboard, assets, composition, renders).
**Planification RapidoCMS** : `create_draft_tool` → `schedule_draft_tool` (`post_heure "HH:MM:SS"`, `media_source "biblio"`), rattaché à la campagne **« Vente Social 2026 »** via un **post planifié** (`add_post_campagne`).
