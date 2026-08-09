---
description: Contrôle qualité + normalisation des 2 MP4 sources (Higgsfield, déposés manuellement)
---

# /ep-ingest

Étape 4 du pipeline. Aucun MCP — uniquement ffprobe/ffmpeg local.

## Garde-fou (bloquant)

Refuse de s'exécuter si `manifest.json.pipeline.ep-voix.status != "done"`.

## Rappel n°1 du CLAUDE.md

**Cette commande n'appelle jamais le MCP Higgsfield.** Les 2 vidéos sont générées
manuellement par l'humain dans l'interface Higgsfield et déposées dans
`episodes/ep01-la-rentree/sources/`.

## Étapes

1. Vérifier la présence de :
   - `episodes/ep01-la-rentree/sources/A_hook.mp4` (10 s attendues)
   - `episodes/ep01-la-rentree/sources/B_corps.mp4` (15 s attendues, ou 24 s si variante
     Seedance 2.5)
   - **Si l'un des deux manque : arrête-toi net et demande-le à l'utilisateur.** Ne fabrique
     rien à la place.
2. `ffprobe` sur chaque fichier : durée, résolution (attendu 9:16), framerate, codec.
3. Lancer `scripts/normalize.sh` pour uniformiser format/framerate avant montage.
4. Signaler tout écart avec la checklist de recette de
   `episodes/ep01-la-rentree/prompts/03-PROMPTS-HIGGSFIELD.md` (un rendu qui rate un point
   est refusé — pas de compromis).
5. Mettre à jour `manifest.json.pipeline.ep-ingest.status = "done"`.
