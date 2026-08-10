# Usine FoodEatUp — règles de session

Plusieurs personnes, plusieurs comptes Claude Code, plusieurs sessions en même
temps sur ce dépôt. Ces règles existent pour que deux sessions ne se marchent
jamais dessus. Lis-les avant de toucher quoi que ce soit.

## 1. Zéro génération payante

Ce dépôt **récupère** et **monte**. Il ne génère pas.

| Outil | Autorisé | Interdit |
|---|---|---|
| Higgsfield | `show_generations`, `show_generation_by_ids` (relire un job déjà payé) | `generate_video`, `generate_image`, `motion_control`, `upscale_*`, `reframe`, `shorts_studio_*`, `generate_3d` et toute variante `_batch` |
| HeyGen | rien | `render_video`, `compose` |
| RapidoCMS | `upload_file_tool`, `create_draft_tool`, `schedule_draft_tool` | `generate_image`, `images_to_image` |
| ElevenLabs | `text_to_speech` pour une VO **absente** | régénérer une VO existante |

Recadrage, incrustations, transitions, logo : **ffmpeg local**. Gratuit,
reproductible, corrigeable sans repasser par une IA.

S'il manque un plan Higgsfield, on ne le génère pas : on donne le prompt à
l'humain (il est dans `content/briefs/02-` à `06-HIGGSFIELD-S*.md`) et on marque
l'épisode `manquant`.

## 2. Un épisode = une réservation = une branche

Ne travaille **jamais** sur un épisode sans l'avoir réservé.

```bash
export FEU_OWNER="prenom@boite.fr"   # une fois par session
./scripts/claim-episode.sh           # prend le premier libre, crée la branche ep/EPxxx
./scripts/claim-episode.sh EP042     # ou un épisode précis
```

Le verrou, c'est le `git push` du fichier de réservation. Si deux sessions
réservent le même épisode à la même seconde, la seconde voit son push rejeté,
annule sa réservation et repart sur un autre épisode — automatiquement.

Quand tu as fini : PR de `ep/EPxxx` vers la branche d'intégration. Si tu
abandonnes, `./scripts/release-episode.sh EPxxx` pour rendre l'épisode.

## 3. Un fichier par épisode, jamais de fichier partagé

`state/episodes/EPxxx.json` et `state/claims/EPxxx.json` : un fichier par
épisode. Deux sessions qui avancent sur deux épisodes touchent deux fichiers
différents, donc git fusionne sans conflit.

**Ne crée jamais un `state/pipeline.json` global.** C'est la seule façon
garantie de provoquer un conflit à chaque commit.

`content/episodes.json` est la source de vérité des 150. Elle se modifie par PR
dédiée, jamais au fil d'un épisode.

## 4. `templates/` ne se touche pas pendant un épisode

| Fichier | Ce que c'est | Durée |
|---|---|---|
| `COMMUN_sting_BC.mp4` | sting logo + VO_A + VO_B | 9 s |
| `COMMUN_E.mp4` | signature de fin + VO_C | 4 s |
| `logo_foodeatup.png` | badge, 250×93, posé à (795, 57) | — |
| `bgm.mp3` | lit musical, calé à −28 dBFS | — |
| `sfx_transition.mp3` | whoosh du changement de voix à 16 s | — |

Ces 13 secondes sont **identiques sur les 150**. Les modifier change les 150
épisodes d'un coup : PR dédiée, revue par quelqu'un d'autre, jamais dans une
branche `ep/`.

## 5. L'anatomie des 30 secondes ne se négocie pas

| Segment | Plage | Voix | Source |
|---|---|---|---|
| A | 0 → 7 | son du clip + punchline ElevenLabs à 5,0 | `assets/hooks/EPxxx.mp4` |
| sting + B + C | 7 → 16 | VO_A, VO_B | `templates/` |
| **D** | **16 → 26** | **HeyGen seul** | `assets/avatar/` + `assets/software/` |
| E | 26 → 30 | VO_C | `templates/` |

**Entre 16,0 et 26,0 il n'y a qu'une voix : celle de l'avatar.** Deux sources
actives sur cette plage = épisode rejeté. C'est vérifié par `qc-episode.sh`.

Le beat comique du clip tombe à 5,0 s. Si le clip généré décale ce beat, on
change de clip — on ne recale pas le montage.

## 6. Ce qu'on transmet à l'humain pour chaque épisode

Deux choses, et rien d'autre :

1. **Le script HeyGen — le texte seul.** Pas de bloc de réglages, pas de gabarit,
   pas de consignes de cadrage. Juste la phrase que l'avatar doit dire. Les
   réglages HeyGen sont déjà en place côté humain, les répéter est du bruit.
2. **Le lien Drive de la vidéo logiciel**, pointant sur le fichier exact du
   chapitre — pas sur le dossier du module.

Le hook Higgsfield est déjà généré : `content/hooks-higgsfield.json` donne le
rendu par épisode. Ne redemande pas un plan qui existe.

## 7. Rien ne passe en `dist/` sans contrôle

```bash
./scripts/build-episode.sh EPxxx   # monte puis contrôle
./scripts/qc-episode.sh   EPxxx    # contrôle seul
```

Durée 30,0 ±0,2 · 1080×1920 @30 · −14 LUFS ±1 · peak ≤ −1 dBTP · première frame
non noire · logo présent à 1/15/29 s. Un master qui échoue reste dans `build/`
et part au rapport. **Le pipeline ne s'arrête jamais sur un épisode incomplet** :
on marque, on passe au suivant.

## 8. Binaires

`build/` n'est pas versionné. Les rushes bruts (`*_src.mp4`) non plus. Les
masters de `dist/` sont versionnés — c'est le livrable. Les assets déposés à la
main (`assets/hooks`, `assets/avatar`, `assets/software`) sont versionnés pour
qu'une autre session puisse remonter un épisode sans redemander les fichiers.

## 9. Publication

Tout part en **brouillon** dans RapidoCMS. La planification exige un `--confirm`
explicite. Rien n'est publié sans validation humaine.

## Où regarder

```bash
./scripts/status.sh              # qui travaille sur quoi, ce qui manque
./scripts/status.sh --manquants  # le détail épisode par épisode
./scripts/next-episode.sh        # le prochain épisode libre
```

`content/briefs/` contient les 11 documents de référence : pipeline, anatomie,
les 150 prompts Higgsfield par saison, les 150 scripts HeyGen, les textes
ElevenLabs, la spécification de montage.
