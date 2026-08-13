# Prompt Lovable — l'atelier de la saison 6

À coller dans Lovable. Aucune image à joindre : tout est déjà dans le dépôt.

---

## Le message

La saison 6 vient de recevoir, pour chacun de ses trente épisodes, de quoi le
**refaire chez soi** : un prompt Higgsfield, un script HeyGen, un prompt de
montage pour Claude Code, un prompt de publication pour RapidoCMS. Ils sont dans
`src/data/contenu.ts`, champs `kit` et `scriptHeygen`, déjà poussés.

Le composant qui les affiche existe aussi — `src/components/AtelierSaison6.tsx`,
branché en bas de la moitié RapidoCMS des pages d'épisode. **Ne le refais pas.**

Ce qui manque, c'est de rendre cette promesse visible ailleurs que tout en bas
d'une page d'épisode. Trois choses à faire, et rien d'autre.

### 1. Une page dédiée : `/atelier`

Une page dans la charte RapidoCMS — `zone-rapido`, fond blanc, Arial, bleu
`#03A9F5` — qui explique la méthode une bonne fois, avec la Brigade
Végé-Fruitée en guides.

Structure :

- **Le titre** : « Faites vos vidéos de restaurant vous-même ». Sous-titre : une
  phrase qui dit qu'aucun logiciel de montage n'est nécessaire.
- **La planche des dix agents** : réutilise `<PlancheAgents />` de
  `src/components/PlancheAgents.tsx`. Ne réécris pas la liste, elle vit dans
  `src/data/agents.ts`.
- **Les trois étapes en grand**, avec pour chacune le végé-fruité qui la porte,
  le nom de l'outil, et le bouton qui l'ouvre :
  1. **Higgsfield** — La Fraise. Le plan comique de dix secondes.
  2. **Claude Code** — Tomate Man. Le montage et les treize contrôles.
  3. **RapidoCMS** — La Betterave. Les cinq réseaux programmés.
- **Un exemple complet et déroulable** : prends l'épisode EP151 et montre ses
  trois prompts réels avec `<AtelierSaison6 />`. C'est la preuve que la page ne
  promet rien qu'elle ne montre.
- **Le pied** : deux boutons, « Créer un compte RapidoCMS » et « Voir la
  saison 6 ».

Ajoute le lien « L'atelier » dans la navigation principale, entre « La méthode »
et « RapidoCMS ».

### 2. Un rappel sur la page de la saison 6

Sur `/series/le-coup-de-feu/saison/6`, au-dessus de la grille des épisodes :
un bandeau `carte-rapido` avec un végé-fruité, une phrase — « Chacun de ces
trente épisodes vient avec les prompts pour le refaire chez vous » — et le
bouton vers `/atelier`.

Sur les cinq autres saisons, ce bandeau ne s'affiche pas.

### 3. Une pastille sur les cartes d'épisode de la saison 6

Dans `GrilleEpisodes`, les épisodes qui ont un `kit` non vide portent une petite
pastille « Recette fournie ». Discrète : une pastille bleue, pas un badge de
promotion.

---

## Ce que tu ne touches pas

- **`src/data/series.ts` et `src/data/contenu.ts`** — générés par l'usine à
  vidéos et poussés depuis le dépôt. Les prompts, les publications, les statuts
  et les liens RapidoCMS y sont déjà. Une régénération de ta part les écraserait.
- **`src/components/AtelierSaison6.tsx`, `PlancheAgents.tsx`, `Brigade.tsx`,
  `src/data/agents.ts`, `src/data/brigade.ts`** — ils existent et fonctionnent.
  Importe-les, ne les réécris pas.
- **Les vignettes** — elles font l'objet d'un message séparé.

## Deux règles de fond

**Les crochets restent visibles.** Dans tout prompt affiché, `[TON PLAT]` et ses
semblables doivent être surlignés. `AtelierSaison6` le fait déjà ; si tu affiches
un prompt ailleurs, fais pareil. Un bloc uniforme se copie sans qu'on remarque
qu'il reste des trous.

**Un végé-fruité n'est pas une décoration.** Chacun porte un outil réel, nommé.
N'en ajoute aucun qui n'aurait rien derrière lui, et ne change pas les
attributions : elles sont dans `agents.ts` et doivent rester d'accord avec le
générateur de l'usine.

## Contrôle avant de rendre la main

- `/atelier` existe, est dans la navigation, et affiche les trois prompts réels
  d'EP151 ;
- le bandeau n'apparaît que sur la saison 6 ;
- les crochets sont surlignés partout où un prompt s'affiche ;
- `series.ts` et `contenu.ts` sont inchangés — vérifie le diff avant de rendre.
