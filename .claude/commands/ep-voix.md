---
description: Génère la VO française via ElevenLabs, une piste par réplique + timing JSON
---

# /ep-voix

Étape 3 du pipeline.

## Garde-fou (bloquant)

Refuse de s'exécuter si `manifest.json.pipeline.ep-data.status != "done"`.

## Étapes

1. Lire `episodes/ep01-la-rentree/voix/ep01.voix.json` pour le script et le timing.
2. Pour chaque réplique, appeler `text_to_speech` (ElevenLabs) avec la voix et les réglages
   correspondants :
   - **NAVY** — stability 0.45 / similarity_boost 0.80 / style 0.35. Pause marquée avant
     « Il a tort. »
   - **BROCOLI** — stability 0.75 / similarity_boost 0.85 / style 0.10. Aucune emphase.
3. Sauver chaque piste audio dans `episodes/ep01-la-rentree/voix/` (une par réplique,
   nommée par timecode).
4. Mettre à jour le JSON de timing avec les chemins des fichiers générés.
5. Mettre à jour `manifest.json.pipeline.ep-voix.status = "done"`.
