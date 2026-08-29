# Épisode 01 « Le duel » — provenance des plans

**Aucune génération Higgsfield n'a été lancée** (règle `CLAUDE.md`). Les deux plans de 10 s
existaient déjà dans la bibliothèque du compte et ont été **réutilisés tels quels**.

| Plan | Generation ID Higgsfield | Modèle | Fichier |
|---|---|---|---|
| Scène 1 — « Midi pile » | `2855b8b2-37c8-441f-8b56-58c02c6b1fe1` | seedance_2_5 | `source/ep01-scene1.mp4` |
| Scène 2 — « Table pour trois » | `bd80afd3-8ad9-4eb5-ae1b-1103625f677e` | seedance_2_5 | `source/ep01-scene2.mp4` |

Sources d'origine : 720×1280, 24 fps, ~10,0 s, audio AAC 32 kHz (dialogue français + ambiance
générés dans la même passe). Les prompts stockés côté Higgsfield correspondent mot pour mot aux
fiches `prompts/ep01-le-duel.md`, à une différence près : la référence visage y est passée en
`<<<image_1>>>` (Reference Element) au lieu de `@Image 1`.

## Ce qui a été fabriqué ici

| Sortie | Contenu |
|---|---|
| `ep01-le-duel.mp4` | **Le master** : scène 1 + scène 2 + outro, 1080×1920, 30 fps, 30,1 s |
| `ep01-outro-muet.mp4` | L'outro seul, 10 s, SFX uniquement (pas de voix off) |
| `ep01-thumb.png` | Miniature spec : image de l'outro à 2,5 s + titre |
| `ep01-thumb-hook.png` | Miniature alternative : le gros plan de la scène 1 + la réplique du hook |
| `scene2-last-frame.png` | Dernière image de la scène 2, plaque de départ de l'outro |

Les deux sources 720p sont remontées en 1080×1920 (lanczos) et converties en 30 fps pour tenir le
format de saison. `work/` contient les intermédiaires (300 images de l'outro, segments normalisés,
piste SFX) — non versionné.

## Reconstruire

```bash
node scripts/render-outro.mjs 1      # 300 images → outro sans son + miniature
# puis le mux SFX et le concat (voir l'historique de commande dans ce dossier)
```

## Calage des SFX dans l'outro (secondes)

`clap` 0,40 · `tick` 2,40 / 2,73 / 3,07 (les deux noms en conflit) · `whoosh` 5,60 (l'assignation
en un tap) · `tick` 7,33 / 7,67 / 8,00 (les trois cartes modules) · `whoosh` 8,95 + `impact` 9,00
(le logo).

## ⚠️ Manque : la voix off

La voix off de l'épisode (« Deux clients, une table ? Avec FoodEatUp, la réservation vérifie la
place avant vous. ») **n'a pas pu être générée** : le connecteur ElevenLabs renvoie
`Failed to generate audio` sur chaque prise (8 tentatives, modèles `eleven_multilingual_v2` et
`eleven_turbo_v2_5`, voix `Adam - Instructor` `TGAegA0zNRi8I6nUdq3i`), et aucune clé API locale
n'est présente dans cet environnement. Le master livré porte donc l'audio Seedance des deux scènes
puis un outro **SFX seuls**.

Pour compléter dès que la voix est disponible : déposer `vo.mp3` et remonter l'outro avec la voix
démarrant à **2,0 s** et finissant avant **9,0 s**, SFX sous la voix.
