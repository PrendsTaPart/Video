# Le sting B/C — ce qui a été mesuré, ce qui reste à trancher

Le passage de « dix logiciels » à « huit » touche le carton commun aux 337
épisodes, `templates/COMMUN_sting_BC.mp4` (9 s, collé tel quel par
`build-episode.sh` entre le segment A et le segment D). Voici l'état relevé sur
le fichier lui-même — rien ici n'est déduit d'un brief.

## Ce que dit le sting, exactement

Transcription du rendu (ElevenLabs Scribe, français à 99,2 %) :

> « Aujourd'hui, tu gères ton restaurant avec dix logiciels, mille euros par
> mois et aucun ne se parle. Tout ça change avec FoodEatUp. »

Deux phrases, pas une. Et ce n'est pas le texte du brief `10-BRIEF-150.md`
(VO_A « Marre d'avoir dix logiciels… » / VO_B « FoodEatUp, le logiciel qui fait
jouer tes données… ») : le sting a été monté sur un texte réécrit.

À l'image, la même phrase est écrite : « LE PROBLÈME / DIX LOGICIELS », dix
pastilles, « 1 000 € PAR MOIS », « ET AUCUN NE SE PARLE ». Remplacer le son
seul laisserait donc trois contradictions à l'écran.

## `assets/vo/fixed/VO_BC.mp3` n'est pas la voix du sting

Le fichier existe, dure 7,34 s et dit le même texte, mais ce n'est pas la prise
incrustée dans le rendu : corrélée à la voix extraite du sting, elle donne
0,035 — deux prises différentes. Aucun script du dépôt ne le lit, non plus.
**Le remplacer ne change rien au sting.**

## Le rendu se refait

`scripts/build-sting-BC.py` reconstruit le carton à partir du rendu d'origine,
en ne changeant que le mot du titre et le nombre de pastilles.

- La police est **Anton** : à hauteur de capitale égale, elle rend « DIX
  LOGICIELS » en 517 px contre 515 mesurés (0,4 %), et les trois autres lignes
  à moins de 1 %.
- Les pastilles ne sont pas redessinées, elles sont **découpées dans le rendu**.
- L'ouverture (l'animation du logo, 0 → 2,2 s) est **reprise telle quelle**.
- Le lit musical est `templates/bgm.mp3` à partir de 3,18181 s, gain 0,2867 :
  ce calage explique 88,9 % de l'énergie de la bande-son d'origine.

Contrôle : reconstruit à l'identique (`--nombre dix --icones 1..10`), le rendu
retombe sur l'original à **0 pixel près en vertical**, 1 à 2 px en horizontal,
et un écart moyen de 2,4/255 sur les 270 images — l'anticrénelage du texte.

La version livrée pour relecture est `templates/COMMUN_sting_BC_huit.mp4`
(9,000 s, −21,8 LUFS contre −21,7 à l'original). **Elle ne remplace pas le
gabarit publié** : le fichier d'origine est intact tant que personne n'a validé.

## Trois décisions qui ne sont pas les miennes

1. **La voix.** Trois prises de la voix maison du projet (`Adam - Instructor`,
   `eleven_multilingual_v2`) sont dans `assets/vo/fixed/` : `VO_BC_huit.mp3`
   (7,42 s, celle montée), `VO_BC_huit-prise1.mp3` (7,29 s) et
   `-prise2.mp3` (7,89 s). Le créneau du sting fait 7,42 s : la prise retenue y
   tombe sans étirement. Les réglages du projet (stability 0,55 ·
   similarity 0,80 · style 0,15) ne sont pas exposés par le connecteur utilisé —
   le timbre est donc à valider à l'oreille.
2. **Quelles deux pastilles disparaissent.** Le rendu proposé garde les huit
   premières dans l'ordre d'affichage (reçu, livraison, calendrier,
   organigramme, horloge, fiches, mégaphone, avis) et retire les deux
   dernières. `--icones` prend n'importe quelle liste.
3. **Trois épisodes disent « dix » dans leur texte** — EP013 (« Dix logiciels.
   Dix notifications. »), EP120 (« Réunion de tes dix logiciels. ») et EP022
   (punchline « Pour dix logiciels qui ne se parlent même pas. »). Leurs plans
   Higgsfield sont déjà générés : corriger le texte veut dire les régénérer, ce
   que `CLAUDE.md` interdit à un agent. À arbitrer.
