# FoodEatUp — usine à 150 vidéos de 30 s

Montage local en ffmpeg à partir d'assets **déjà produits**. Aucune génération :
ni Higgsfield, ni HeyGen, ni image. On récupère, on monte, on contrôle.

## État : EP001 monté et conforme

```bash
./scripts/build-episode.sh EP001   # monte + contrôle
./scripts/qc-episode.sh   EP001    # contrôle seul
```

## Anatomie des 30 secondes

| Segment | Plage | Contenu | Voix | Source |
|---|---|---|---|---|
| A | 0 → 7 | clip Higgsfield + hook incrusté + punchline | son du clip + ElevenLabs | `assets/hooks/EPxxx.mp4` |
| sting | 7 → 9 | logo motion | — | `build/COMMUN_sting_BC.mp4` |
| B + C | 9 → 16 | « Le problème : dix logiciels » | ElevenLabs VO_A, VO_B | idem |
| **D** | **16 → 26** | **avatar 45 % / logiciel 55 %** | **HeyGen seul** | `build/EPxxx_D.mp4` |
| E | 26 → 30 | signature de fin | ElevenLabs VO_C | `build/COMMUN_E.mp4` |

`COMMUN_sting_BC.mp4` (9 s) et `COMMUN_E.mp4` (4 s) sont **identiques sur les 150** :
vérifié en comparant les masters de référence EP001 et EP020, image par image sur
ces plages. 13 des 30 secondes sont donc déjà produites, une fois pour toutes.

## Ce qui change d'un épisode à l'autre

Trois fichiers, rien d'autre : `assets/hooks/EPxxx.mp4`, `assets/avatar/EPxxx.mp4`,
`assets/software/EPxxx.mp4`.

## Charte relevée sur les masters de référence

| | valeur | relevé |
|---|---|---|
| fond | `#FAF6E3` (sable) | échantillonné sur le master, **pas** le `#0B0B0F` du brief |
| badge logo | 250 × 93 px à (795, 57) | haut-droite, constant sur les 30 s |
| lit musical | ≈ −28 dBFS | plancher inter-phrases, continu de 0 à 30 s |
| loudness | −13,9 LUFS · peak −1,9 dBTP | conforme à la cible −14 ±1 |

## Contrôle bloquant

`qc-episode.sh` vérifie durée 30,0 ±0,2 · 1080×1920 @30 · −14 LUFS ±1 ·
peak ≤ −1 dBTP · première frame non noire · logo présent à 1 s / 15 s / 29 s.
Un master qui échoue reste dans `build/`.

## Points ouverts

1. **Le brief et les masters de référence divergent sur le segment D.** Le brief
   décrit un split avatar/logiciel ; EP001 et EP020 tels que livrés n'ont **aucun
   avatar** sur 16 → 26 (logiciel plein cadre sur fond flouté, commenté en voix
   ElevenLabs). Le build actuel suit le brief.
2. **Le screencast MCP est un 1920×828** : padé sans rognage dans le slot 1080×1056,
   il n'occupe que 466 px de haut. Lisible mais petit. Un rush 16:9 ou 4:3 remplirait
   mieux — à arbitrer.
3. **L'avatar fait 8,3 s pour un slot de 10 s.** Dernière frame clonée de 24,3 à 26,0,
   musique maintenue. Un rendu HeyGen de 10 s supprimerait le figé.
4. **La musique** est `assets/brand/bgm.mp3`, reprise du projet `foodeatup-promo-9x16`
   et calée au niveau de la référence. Le stem exact n'est pas récupérable depuis un
   master mixé ; si le fichier d'origine existe, le déposer ici suffit.
5. **`03-episodes.json` n'est pas encore sur le Drive** : le ZIP
   `DRIVE-150-EPISODES-FoodEatUp.zip` n'a pas été installé. Seul `EP001` existe
   (SAISON 1), `_COMMUN` est vide. La suite du pipeline en dépend.
