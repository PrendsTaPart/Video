# FoodEatUp — usine à 150 vidéos de 30 s

Montage local en ffmpeg à partir d'assets **déjà produits**. Aucune génération :
ni Higgsfield, ni HeyGen, ni image. On récupère, on monte, on contrôle.

Plusieurs comptes Claude Code travaillent sur ce dépôt en parallèle.
**Les règles de session sont dans [`CLAUDE.md`](CLAUDE.md) — à lire en premier.**

## Démarrer une session

```bash
export FEU_OWNER="prenom@boite.fr"
./scripts/status.sh                  # qui fait quoi, ce qui manque
./scripts/claim-episode.sh           # réserve le premier épisode libre
# … dépose les 3 assets, puis :
./scripts/build-episode.sh EP0xx     # monte + contrôle
```

## Anatomie des 30 secondes

| Segment | Plage | Contenu | Voix | Source |
|---|---|---|---|---|
| A | 0 → 7 | clip Higgsfield + hook incrusté + punchline à 5,0 s | son du clip + ElevenLabs | `assets/hooks/` |
| sting | 7 → 9 | logo motion | — | `templates/COMMUN_sting_BC.mp4` |
| B + C | 9 → 16 | « Le problème : dix logiciels » | VO_A, VO_B | idem |
| **D** | **16 → 26** | **avatar 45 % / logiciel 55 %** | **HeyGen seul** | `assets/avatar/` + `assets/software/` |
| E | 26 → 30 | signature de fin | VO_C | `templates/COMMUN_E.mp4` |

Les 13 s de `templates/` sont **identiques sur les 150** — vérifié en comparant
les masters de référence EP001 et EP020. C'est ce qui rend 150 épisodes faisables.
Ce qui change par épisode : trois fichiers et trois textes, rien d'autre.

## Arborescence

```
CLAUDE.md              règles de session (concurrence, interdits, contrôle)
content/
  episodes.json        source de vérité des 150 — PR dédiée pour la modifier
  briefs/              11 documents de référence (prompts, montage, VO)
templates/             les 13 s réutilisées + logo + musique + whoosh
assets/hooks|avatar|software|vo/
build/                 intermédiaires (non versionné)
dist/tiktok|instagram|youtube|facebook|linkedin/
scripts/
  claim-episode.sh     réserve un épisode, crée la branche ep/EPxxx
  release-episode.sh   rend un épisode
  next-episode.sh      prochain épisode libre
  build-episode.sh     monte puis contrôle
  qc-episode.sh        contrôle bloquant
  status.sh            tableau de bord
  bootstrap-state.py   régénère state/episodes/ depuis episodes.json
state/
  episodes/EPxxx.json  un fichier par épisode — jamais de fichier partagé
  claims/EPxxx.json    réservations ; le push est le verrou
```

## Concurrence

Un épisode = une réservation = une branche `ep/EPxxx`. La réservation est un
fichier poussé sur la branche d'intégration : **le `git push` est le point
d'arbitrage**. Deux sessions qui visent le même épisode, la seconde voit son push
rejeté, annule et repart sur un autre — sans intervention.

L'état est éclaté en un fichier par épisode précisément pour que deux sessions
qui avancent en parallèle ne modifient jamais la même ligne.

## Contrôle bloquant

Durée 30,0 ±0,2 · 1080×1920 @30 · −14 LUFS ±1 · peak ≤ −1 dBTP · première frame
non noire · logo présent à 1/15/29 s. Un master qui échoue reste dans `build/`.

## Charte relevée sur les masters de référence

| | valeur | remarque |
|---|---|---|
| fond | `#FAF6E3` (sable) | échantillonné sur le master, **pas** le `#0B0B0F` du brief |
| badge logo | 250 × 93 px à (795, 57) | haut-droite, constant sur les 30 s |
| lit musical | ≈ −28 dBFS | plancher inter-phrases, continu de 0 à 30 s |

## Points ouverts

1. **Le brief et les masters de référence divergent sur le segment D.** Le brief
   décrit un split avatar/logiciel ; EP001 et EP020 tels que livrés n'ont aucun
   avatar sur 16 → 26 (logiciel plein cadre, voix ElevenLabs). Le build suit le brief.
2. **Les briefs se contredisent entre eux** : `00-PIPELINE.md` parle de 30 épisodes,
   d'un découpage 16,5 → 26,0 et d'un logo bas-droite ; `01-STRUCTURE-VIDEO-TYPE.md`
   et le brief 150 disent 16,0 → 26,0. C'est le brief 150 qui fait foi ici.
3. **Screencast ultra-large** (1920×828) : padé sans rognage, il n'occupe que 466 px
   sur 1056. Lisible mais petit — un rush 16:9 remplirait mieux.
4. **Avatar de 8,3 s pour un slot de 10 s** : dernière frame clonée, musique
   maintenue. Un rendu HeyGen de 10 s supprimerait le figé.
5. **Le Drive de production n'est pas installé** : le ZIP `DRIVE-150-EPISODES` n'a
   pas été déployé, seul `EP001` existe et `_COMMUN` est vide. `content/episodes.json`
   reconstitue la source de vérité en attendant.
