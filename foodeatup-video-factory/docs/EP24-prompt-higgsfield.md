# EP24 « La mouette braqueuse » — plan à générer

Seul hook manquant des 30. Rien n'est généré automatiquement (CLAUDE.md §1) :
ce fichier existe pour que l'humain le lance depuis l'interface Higgsfield et
dépose le MP4 dans `assets/hooks/EP24.mp4`. L'assemblage se fait ensuite tout
seul.

## Pourquoi aucun plan existant ne convient

L'historique Higgsfield du compte contient 111 vidéos. Les seuls plans de vol
de nourriture sont déjà pris :

| Plan | Épisode |
|---|---|
| pigeon qui pique une frite sur une terrasse (`f4469aa1`) | EP09 « Le pigeon voleur » |
| raton laveur et la baguette (`0efe4da0`) | EP14 « Le raton laveur » |
| main d'enfant qui rafle la dernière frite (`23dc55f7`) | EP17 « Le ninja de la frite » |

Les réutiliser casserait la règle « une séquence par épisode, aucun doublon ».

## Paramètres

| | |
|---|---|
| Modèle | `seedance_2_5` (celui des 29 autres hooks) |
| Format | 9:16 vertical, 720p, `bitrate_mode: high` |
| Durée | 10 s |
| Audio | activé |
| Reference elements | aucun |

## Prompt

```
Vertical 9:16, 10 seconds, photorealistic, handheld seaside terrace, bright
overcast light, 4K. NO text overlay, NO subtitles, NO watermark, NO logo. A
seagull stands on the railing of a seaside restaurant terrace, staring at an
untouched burger on a table below with open criminal intent. At 5 seconds it
drops in one clean swoop, seizes the burger whole and beats back up out of
frame. Final 2 seconds: the empty plate, a single lettuce leaf still spinning
on the tablecloth. Audio: seaside terrace ambience, gulls, a sudden heist-movie
sting on the swoop, wingbeats receding. No music bed.
```

## Après réception

```bash
# déposer le MP4 dans assets/hooks/EP24.mp4, puis :
python scripts/02_generate_vo.py --episode EP24     # punchline + pitch de démo
python scripts/03_assemble.py --episode EP24 --format tiktok_30
python scripts/03_assemble.py --episode EP24 --format linkedin_45
python scripts/04_publish_rapidocms.py --episode EP24 --start 2026-08-17
```

Le hook et la punchline sont figés dans `config/episodes.json` — ne pas les
réécrire (CLAUDE.md §4) :

- hook : « Encore une commission en moins. »
- punchline : « Récupère tes commandes en direct. »
- démo : capture `vitrine`
