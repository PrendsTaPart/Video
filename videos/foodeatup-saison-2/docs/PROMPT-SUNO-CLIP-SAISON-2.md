# Clip musical de la saison 2 — « TRENTE FILMS »

Le prompt Suno de la chanson du clip musical de « Michael fait son cinéma »,
saison 2. Les clips sortent le **samedi**, les épisodes en semaine (règle du
catalogue Social FoodEatUp).

Deux clips existent déjà et fixent la méthode : `le-clash` (Drill FR × R&B,
144 BPM mesurés pour 142 demandés, 3 min 23) et
`il-etait-une-fois-un-restaurant` (piano-voix, 90,7 BPM mesurés pour 92
demandés, 4 min 30). **Le BPM demandé n'est jamais le BPM obtenu** : la grille
de montage se construit sur le tempo *mesuré* après génération, pas sur celui
qu'on a écrit dans le prompt.

---

## Ce que la chanson doit permettre au montage

La matière du clip, ce sont les **60 plans de la saison** (30 épisodes × 2
scènes) plus les 30 outros. La chanson est donc écrite pour qu'un couplet
corresponde à une série de gags et que le refrain corresponde aux écrans.

| Partie | Ce qu'elle porte à l'image | Durée visée |
|---|---|---|
| Intro | l'accordage, le clap, le rideau | 12 s |
| Couplet 1 | les épisodes 1 à 8 — la journée qui déraille | 32 s |
| Pré-refrain | la question qui revient tous les soirs | 16 s |
| Refrain | les écrans, un geste par plan | 24 s |
| Couplet 2 | les épisodes 9 à 24 — l'escalade | 32 s |
| Refrain | idem, plans différents | 24 s |
| Pont | un seul plan, sans coupe — l'écran qui bascule | 24 s |
| Refrain final | les 30 épisodes en accéléré | 28 s |
| Outro | le logo, « Coupez. » | 12 s |

≈ **3 min 05**. Assez long pour donner à chaque épisode une seconde et demie
sans que le montage devienne un stroboscope.

---

## 1. Champ « Style of Music »

```text
French cinematic pop-funk, big-screen title-sequence energy: punchy brass stabs, staccato strings, tight funk drums with a live snare, walking electric bass, Rhodes and clavinet, occasional harpsichord and timpani for the movie-trailer moments. Male lead vocal in French, warm mid-range baritone, spoken-sung on the verses, full and anthemic on the chorus, layered gang vocals on the hook. 112 BPM, A minor, straight 4/4 with a half-time bridge. Clean modern mix, wide stereo brass, punchy low end, no autotune, no lo-fi, no trap hi-hats. Ends on a single clean orchestral hit, then silence.
```

## 2. Champ « Title »

```text
TRENTE FILMS
```

## 3. Champ « Lyrics »

```text
[Intro — orchestra tuning, one clapperboard snap]
Moteur.
Ça tourne.

[Couplet 1]
Sept heures, la lumière s'allume,
le rideau monte sur la salle.
Deux clients, une seule table :
ça commence en western fatal.
Le contrôle sonne à la porte,
il veut les relevés d'hier.
J'ai le rôle, j'ai pas le texte,
et la caméra tourne quand même.

[Pré-refrain]
Chaque jour un genre différent,
chaque soir la même question :
qui a nettoyé, qui a signé,
qui se souvient, qui a compté ?

[Refrain]
Trente films, un restaurant,
trente galères, un seul écran.
J'ai plus besoin de m'en souvenir,
c'est écrit, ça peut revenir.
Trente films, un restaurant —
Michael fait son cinéma.

[Couplet 2]
Dimanche, le brunch des zombies,
la file s'étire jusqu'au trottoir.
Le livreur tourne à droite trois fois,
il finit dans un champ, le soir.
Dix palettes d'oignons en cuisine —
j'avais dit dix, j'avais dit ça.
Le stock recompte, moi je m'incline :
le chiffre change à chaque fois.

[Pré-refrain]
Il manque cinq euros à la caisse,
il manque un nom sur le planning.
Trois congés le même samedi,
et c'est moi qui les ai signés.

[Refrain]
Trente films, un restaurant,
trente galères, un seul écran.
J'ai plus besoin de m'en souvenir,
c'est écrit, ça peut revenir.
Trente films, un restaurant —
Michael fait son cinéma.

[Pont — half-time, piano and voice only, no drums]
Un geste.
Un seul.
Le statut bascule,
la case s'allume.
Personne n'applaudit.
C'est réglé.
C'est tout.

[Refrain final — full band, gang vocals]
Trente films, un restaurant,
trente galères, un seul écran.
J'ai plus besoin de m'en souvenir,
c'est écrit, ça peut revenir.
Trente films, un restaurant,
trente genres et une seule caméra.
Un système qui travaille avec moi —
Michael fait son cinéma.

[Outro — one clean orchestral hit, then silence]
Coupez.
```

---

## Réglages Suno

| Champ | Valeur |
|---|---|
| Mode | **Custom** (les paroles comptent, l'auto-génération les réécrit) |
| Instrumental | non |
| Style | le bloc ci-dessus, tel quel |
| Exclude styles | `trap, autotune, lo-fi, drill, reggaeton, country` |
| Weirdness / Style influence | faibles — on veut une chanson lisible, pas une expérimentation |

Générer **deux prises**. Les balises `[Intro]`, `[Pont]`, `[Outro]` ne sont pas
toujours respectées : garder la prise où le pont retombe vraiment (batterie
absente) — c'est le seul endroit du clip où un plan tient sans coupe, et sans
ce creux le parti pris ne se voit pas.

## Après génération, avant montage

1. Mesurer le tempo réel (`scripts/tempo.py` du clip `le-clash`) : le BPM
   demandé n'est jamais celui obtenu.
2. Transcrire et aligner les paroles officielles sur l'audio — c'est ce qui
   permet de faire tomber une coupe sur un mot et pas à peu près.
3. Construire la timeline sur les 60 plans de la saison, une source différente
   à chaque coupe, aucune fenêtre consommée deux fois.
4. Déposer par `publier_clip_musical` (master, court, paysage, carré, teaser,
   proxy), puis `lien_public` une fois la page YouTube en ligne.
