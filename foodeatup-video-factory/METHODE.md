# La méthode — d'un prompt à un épisode publié

Le mode d'emploi opératoire de la série. `CLAUDE.md` fixe les règles ; ce
document dit qui fait quoi, dans quel ordre, et ce qui casse quand on saute une
étape.

Un épisode traverse cinq mains : Higgsfield fait rire, HeyGen explique, le Drive
montre, Claude Code assemble, RapidoCMS diffuse. Aucune de ces étapes ne peut
commencer avant que la précédente ait rendu son fichier — sauf une, et c'est tout
l'intérêt du rythme décrit plus bas.

## Le rythme : toujours un épisode d'avance

**Avant de monter l'épisode N, on donne à l'humain le paquet de l'épisode N+1.**
Il produit ses deux fichiers pendant que la machine monte le précédent. Sans ce
décalage, chacun attend l'autre et la chaîne tourne à moitié de sa vitesse.

Le paquet, c'est **deux choses, et rien d'autre** :

1. **Le script HeyGen** — le texte seul. Pas de bloc de réglages, pas de gabarit,
   pas de consigne de cadrage : ils sont déjà en place côté humain, les répéter
   est du bruit.
2. **Le lien Drive du chapitre** — le fichier exact, jamais le dossier du module.
   C'est l'erreur la plus coûteuse de la série : un lien de module oblige
   l'humain à chercher, et il se trompe de chapitre une fois sur cinq.

## Étape 1 — Le plan comique (Higgsfield)

Le prompt de chaque épisode est déjà écrit dans
`content/prompts-higgsfield.json`. Dix secondes, vertical 9:16, sans texte
incrusté ni filigrane — le montage ajoute les siens.

**On ne génère jamais un plan depuis une session Claude.** Si le plan manque, on
donne le prompt à l'humain, qui le lance lui-même dans Higgsfield. Les 32
premiers existent ; EP008 est le seul des 33 premiers à ne pas en avoir.

Le beat comique doit tomber à **5,0 s**. Si le clip généré le décale, on change
de clip — on ne recale pas le montage, sinon la punchline arrive sur un temps
mort et la vidéo perd son ressort.

Le clip doit tenir **9,5 s utiles**. À 7 s, la chute était coupée en plein
milieu : c'est ce qui a fait passer le master de 35 à 37,5 s.

## Étape 2 — Les deux fichiers de l'humain

**L'avatar HeyGen.** Il doit dire le script fourni, ni plus ni moins. La fenêtre
utile fait 9,4 s ; au-delà, le montage accélère la parole et ça s'entend. Le
script est calibré pour tenir dedans — le rallonger de deux mots suffit à faire
passer l'`atempo` au-dessus de 1,12. EP001 est parti à 1,26 et on l'entend.

**Le screencast du logiciel.** Dix secondes prises dans la vidéo du chapitre.
Attention : **le module Caisse POS n'a aucune vidéo dans le Drive** — ses sept
chapitres ne contiennent que des JPG. HubRise et KDS ont le même trou. En tout,
32 des 150 épisodes attendent un tournage. `content/drive-map.json` dit lesquels.

## Étape 3 — Le montage (Claude Code)

```bash
./scripts/build-segment-a.sh EPxxx "Texte du hook"
./scripts/build-episode.sh EPxxx          # monte, puis contrôle
```

L'anatomie ne se négocie pas : A 0→9,5 · sting+B+C 9,5→18,5 · **D 18,5→28,5 où
seul l'avatar parle** · E 28,5→32,5 · sting de marque 32,5→37,5.

Quatre pièges, tous rencontrés, tous mesurés :

- **`loudnorm` ne va pas dans le filtergraph.** Sur une entrée de 2 s il décale
  les PTS de sortie, et le `atrim` suivant supprime la voix — la punchline
  ressortait à −240 dBFS, c'est-à-dire un silence parfait. On normalise dans une
  passe séparée.
- **Le mixage de D écrête.** Voix + lit + whoosh sommés sans normalisation
  tapaient à +2,8 dBTP : l'avatar distordait. `normaliser-segment.sh` cale
  chaque segment à −21 LUFS / −9 dBTP avant l'assemblage.
- **La normalisation finale se boucle sur le master encodé**, pas sur le WAV.
  L'AAC fait remonter la crête très inégalement : même WAV à −1,8 dBTP, un
  épisode sortait à −1,8 et un autre à −0,3.
- **Le contrôle de respiration est relatif.** Un seuil en dBFS ne veut rien dire
  quand le gain final dépend du clip de l'épisode ; on compare le silence à la
  voix de l'avatar, 12 dB d'écart minimum.

Un master qui échoue reste dans `build/` et part au rapport. **La chaîne ne
s'arrête jamais sur un épisode incomplet** : on marque, on passe au suivant.

## Étape 4 — Les cinq publications

Elles sont déjà écrites. `scripts/gen-publications.py` produit, pour chaque
épisode, cinq textes **volontairement différents** :

| Réseau | Heure | Ce qui change |
|---|---|---|
| LinkedIn | 08:00 | le bénéfice métier avant l'anecdote, 4 mots-dièse |
| YouTube | 10:00 | un titre pensé comme une requête, description longue, 12 balises |
| Facebook | 12:00 | le lien dans le corps, texte long, 7 mots-dièse |
| Instagram | 18:30 | pas d'URL — elle n'est pas cliquable, on renvoie en bio |
| TikTok | 19:00 | deux lignes, 5 mots-dièse |

Les horaires sont décalés pour qu'un même épisode ne tombe pas cinq fois au même
moment sur cinq fils.

**RapidoCMS publie sur quatre de ces cinq réseaux.** YouTube reste manuel : le
serveur ne l'expose pas. Ne pas laisser croire le contraire dans l'interface.

## Étape 5 — La vignette

Trois choses à fournir au générateur, et rien d'autre : **le prompt** (déjà écrit
dans `promptVignette`), **la photo du chef**, **le lien de la vidéo montée**.

Le chef ne se redessine pas. Même visage, même toque, même tablier au logo. C'est
la même personne sur les 150 épisodes — c'est ce qui fait une série plutôt qu'une
collection.

Trois défauts constatés sur le premier jet, à corriger au prochain lot :

- le grisé des épisodes non sortis était **cuit dans le fichier** au lieu d'être
  posé en CSS : la vignette resterait grise le jour de la publication ;
- un **second logo**, non officiel, apparaissait en bas à droite, en plus de
  celui du tablier ;
- la **scène était identique** d'un épisode à l'autre, alors que chaque prompt
  décrit un gag précis.

## Étape 6 — La publication

```bash
./scripts/gen-lot-lovable.py     # état des lots
```

**Rien ne part à Lovable tant que dix épisodes ne sont pas montés.** Un tour
coûte la même chose qu'il traite un épisode ou dix : quinze tours pour les 150
vignettes, au lieu de cent cinquante.

Avant d'envoyer un lot, il faut avoir versé dans la bibliothèque RapidoCMS, pour
chacun des dix épisodes : **le master monté** et **le clip Higgsfield source**.
`upload_file_tool` n'accepte qu'une URL publique — les fichiers passent donc
d'abord par `dist/` du dépôt.

Tout part en **brouillon**. La planification exige un `--confirm` explicite.

## Ce qui bloque aujourd'hui

| Épisode | Ce qui manque |
|---|---|
| EP004, EP009, EP011, EP012 | pas de vidéo de chapitre dans le Drive |
| EP008 | pas de plan Higgsfield |
| 32 épisodes au total | chapitre sans vidéo — voir `drive-map.json` |

Un épisode bloqué ne prend pas de place dans le calendrier ni dans un lot : il
s'y insère quand son fichier existe. Sinon un seul chapitre manquant gèlerait
dix vignettes et une semaine de diffusion.
