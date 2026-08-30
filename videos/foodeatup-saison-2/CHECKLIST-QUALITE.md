# Checklist qualité avant publication

## Automatisé — `npm run check` (voir `RAPPORT-CONTROLES.md`)

1. 30 épisodes, numéros uniques, 2 scènes par épisode.
2. Chaque module affiché en carte existe dans la liste des libellés FoodEatUp autorisés.
3. « FoodEatUp » n'est jamais prononcé par l'avatar Seedance.
4. Aucun mineur mentionné dans les prompts (filtre de contenu Higgsfield).
5. Aucun mot de la liste « à éviter » du lexique voix dans les répliques.
6. Dialogues en guillemets français, au moins 3 plans par scène.
7. Voix off tenant dans sa fenêtre (4,6 s → 11,0 s).

## À l'œil, sur chaque épisode monté

- [ ] Michael a le même visage, la même coiffure, la même tenue sur les deux scènes.
- [ ] Aucun texte lisible généré par Seedance (enseigne, ticket, écran, sous-titre).
- [ ] Chaque réplique est compréhensible sans sous-titres.
- [ ] La chute est claire avant la fin de la scène 2 et Michael regarde la caméra.
- [ ] Le clap « COUPEZ ! » arrive à 0,4 s de l'outro.
- [ ] Les noms de modules affichés existent dans FoodEatUp.
- [ ] Le logo FoodEatUp est intact, centré, seul à l'écran de 9 à 10 s.
- [ ] La vidéo se comprend sans le son.

## Corrections

Visage qui dérive → **Region edit**. Un plan raté → **Shot re-generate**. Jamais de re-roll complet.
