# Épisode 07 « La bombe » — provenance

**Aucune génération Higgsfield n'a été lancée** (règle `CLAUDE.md`). Les deux plans de 10 s
existaient déjà dans la bibliothèque du compte et sont **réutilisés tels quels**.

| Plan | Generation ID Higgsfield | Fichier |
|---|---|---|
| Scène 1 — « Laquelle ? » | `e56f4ebb-11f5-4b28-921b-dba58f4a57f5` | `source/ep07-scene1.mp4` |
| Scène 2 — « C'est sûr » | `035aa95b-f8d8-4ec8-9899-05d804dc1f4d` | `source/ep07-scene2.mp4` |
| Scène 1, prise alternative | `fb1f1b8d-a9bb-430e-8e55-27c7a6e659a1` | `source/ep07-scene1-prise-alternative.mp4` |

> Deux prises de scène 1 : la retenue (la plus récente) fait dire à la cliente « Je suis allergique aux haricots verts » et à Michael « Elle m'a dit quel légume déjà ? » ; l'alternative suit la fiche au mot près (« aux noix » / « C'est laquelle ? »). La scène 2 est déclarée 16:9 dans les paramètres Higgsfield mais sort bien en 720×1280.

Sources d'origine : 720×1280, 24 fps, ~10 s, audio AAC 32 kHz (dialogue français et ambiance
générés dans la même passe). Les prompts stockés côté Higgsfield correspondent à la fiche
`prompts/ep07-la-bombe.md`, à une différence près : la référence visage y est passée en
`<<<image_1>>>` (Reference Element) au lieu de `@Image 1`.

## Sorties

| Fichier | Contenu |
|---|---|
| `ep07-la-bombe.mp4` | **Le master** : scène 1 + scène 2 + transition + animation, 1080×1920, 30 fps, 32,1 s |
| `ep07-outro.mp4` | L'outro seul, 12 s, voix off + SFX |
| `ep07-outro-muet.mp4` | L'outro seul, 12 s, SFX uniquement |
| `vo.mp3` | La voix off de l'épisode, normalisée |
| `ep07-thumb.png` | Miniature : le plan figé du début de l'outro + le titre |
| `scene2-last-frame.png` | Dernière image de la scène 2, plaque de départ de l'outro |

## Voix off

| | |
|---|---|
| Voix | **Adam - Instructor** `TGAegA0zNRi8I6nUdq3i`, modèle `eleven_multilingual_v2` |
| Transition (commune aux 30 épisodes) | « Cette scène aurait pu être évitée ? » — prise `sZWCVMCGg2WgpYJb4j3c` (2,04 s), calée à 2,1 s |
| Ligne de l'épisode | « Un allergène, ça se sait avant de servir. FoodEatUp l'affiche sur chaque recette et sur votre site. » |
| Prise retenue | `SqBe2fOcW98hvFyd4JLQ` (5,85 s) |
| Calage | démarre à **4,60 s**, se termine à **10,45 s** (fenêtre : avant 11,0 s) ✅ |

Les prises ElevenLabs sortent très bas : chacune est normalisée à −16 LUFS / −1,5 dBTP.
L'outro est ensuite calé au niveau de saison (−18,5 LUFS), puis le master entier est normalisé
à −16 LUFS en gain linéaire (loudnorm deux passes), le standard des plateformes.

## Calage des SFX dans l'outro (secondes)

`clap` 0,40 · `whoosh` 2,00 (la punchline de transition) · `tick` 4,40 / 4,73 / 5,07
(l'élément clé qui devient des données) · `whoosh` 7,60 (l'action en un tap) · `tick`
9,33 / 9,67 / 10,00 (les cartes modules) · `whoosh` 10,95 + `impact` 11,00 (le logo).

## Reconstruire

```bash
./scripts/monter-episode.sh 07
```

---
Fichier généré par `scripts/sources.mjs` depuis `renders/sources.json`, ne pas éditer à la main.
