---
description: Upload bibliothèque RapidoCMS + brouillons LinkedIn/Facebook/Instagram + campagne FoodEatUp (brouillon)
---

# /ep-publish

Étape 6 (finale) du pipeline.

## Garde-fou (bloquant)

Refuse de s'exécuter si `manifest.json.pipeline.ep-montage.status != "done"`.

## Rappel n°2 du CLAUDE.md — brouillons uniquement

**Aucune planification, aucun envoi de campagne sans confirmation écrite.**
`create_campagne` et `create_draft_tool` créent des brouillons ; `schedule_draft_tool` et
`launch_campaign` sont **interdits par défaut**.

## Étapes

1. Uploader tous les livrables de `episodes/ep01-la-rentree/exports/` dans la bibliothèque
   RapidoCMS (`upload_file_tool`).
2. Créer les brouillons (jamais planifiés) pour chaque canal, avec le copy de
   `episodes/ep01-la-rentree/05-DECLINAISONS.md` :
   - Instagram (Reel principal, teaser, 3 extraits, carrousel, stories)
   - LinkedIn (1:1, copy long + variante courte)
   - Facebook (9:16)
3. Créer la campagne FoodEatUp en **brouillon uniquement** via `create_campaign`
   (FoodEatUp MCP) — ne jamais lancer.
4. Lister à l'utilisateur tous les brouillons créés avec leurs liens/IDs pour relecture.
5. Mettre à jour `manifest.json.pipeline.ep-publish.status = "done"` et
   `definition_of_done` en conséquence — **seulement** après confirmation que rien n'a été
   planifié ni lancé.
