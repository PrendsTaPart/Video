# La queue animée RapidoCMS — et la règle des soixante secondes

Les trente dernières secondes de chaque épisode, plus le montage et les contrôles que tous
les épisodes partagent. Un épisode n'a qu'un pilote de quelques lignes ; tout le reste est ici.

## La règle

| Bloc | Durée | Timecode |
|---|---|---|
| Film Higgsfield | 30 s | 00:00 → 00:30 |
| Transition « COUPEZ » | 3 s | 00:30 → 00:33 |
| Méthode — les cinq étapes | 20 s | 00:33 → 00:53 |
| Hook de fin — la punchline | 7 s | 00:53 → 01:00 |

Une minute, format vertical 1080×1920 à 30 ips. `scripts/verifier.mjs` contrôle cette
structure sur chaque épisode et sort en erreur si un bloc a changé de durée.

## Ce qui change d'un épisode à l'autre, et ce qui ne change pas

**Ne change jamais** : les visuels de la méthode et de l'orchestration, les six lignes de
voix off des étapes (`audio/vo-etapes-2a7.wav`), les logos, la charte, le montage.

**Change à chaque épisode** : le numéro de séquence et le titre sur l'ardoise, la ligne
d'ouverture, la punchline de fin. Cela fait **deux lignes à générer chez ElevenLabs par
épisode** — quelques centimes — et rien d'autre.

Les six lignes fixes ne sont jamais regénérées : elles coûteraient des crédits et, surtout,
feraient varier le timbre au milieu du film. Générer une ligne d'épisode avec une autre
voix que celle de `module.json` s'entend immédiatement.

## Les trois blocs

**La transition (3 s).** Noir plein sur quatre images — la coupe franche du film —, puis
l'ardoise monte du bas : SCÈNE, PRISE, le titre de l'épisode. Le bâton claque à 31,0 s,
l'image tressaute deux images, « COUPEZ » arrive et le tout s'ouvre sur le fond clair.

**La méthode (20 s).** Les logos RapidoCMS et ElevenLabs arrivent au centre puis se rangent
en haut du cadre. Cinq cartes d'étape, 2,6 s chacune, jamais deux à l'écran en même temps,
avec une jauge en bas qui dit où l'on en est — « 3 / 5 ». Puis l'orchestration : RapidoCMS
au centre, Claude, Higgsfield, ElevenLabs et HeyGen en orbite, chacun relié par un trait
qui se trace, le centre qui pulse à chaque branchement, et les cinq réseaux en cascade.

**Le hook de fin (7 s).** La punchline en deux temps — le fait du film, puis la promesse —
la seconde ligne en bleu, le logo, et l'appel à l'action. Fondu au fond clair.

## Lancer

Depuis un dossier d'épisode :

```bash
npm run queue      # les deux lignes de voix off + les 900 images de la queue
npm run monter     # bloc film + queue, niveaux, exports, vignette
npm run verifier   # structure, format, durée, niveau, coupes, sous-titres
npm run build      # les trois à la suite
npm run queue -- --apercu 31,34,44,55   # juste des images, pour juger sans tout rendre
```

## Deux points de méthode

**Le niveau se cale bloc par bloc, pas sur l'assemblage.** Le film sort de Higgsfield très
bas — entre −24 et −26 LUFS — quand la queue est mixée ici, vers −15. Normaliser le film
entier ne ferait que déshabiller l'un pour habiller l'autre : chaque bloc est donc mesuré
et calé sur −14 LUFS *avant* d'être collé. `loudnorm`, même en deux passes, ratait la cible
de 3 dB sur ces extraits ; une mesure EBU R128 suivie d'un gain fixe et d'un limiteur à
−1,5 dBTP tombe juste, et le contrôle le revérifie sur le fichier livré.

**L'animation est déterministe.** Aucun hasard dans le gabarit — la secousse du clap
elle-même est calculée sur le numéro d'image. Deux rendus du même épisode donnent le même
fichier, ce qui rend les contrôles utiles.
