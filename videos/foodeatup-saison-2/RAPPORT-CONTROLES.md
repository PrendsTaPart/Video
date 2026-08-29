# Rapport de contrôles — Saison 2

Généré par `npm run build` (`scripts/build.mjs`) sur 30 épisodes / 60 prompts Seedance.

## Ce qui est vérifié automatiquement
1. 30 épisodes, numéros uniques, 2 scènes par épisode.
2. Chaque module affiché en carte existe dans la liste des libellés FoodEatUp autorisés.
3. « FoodEatUp » n'est jamais prononcé par l'avatar Seedance (réservé à la voix off).
4. Aucun mineur mentionné dans les prompts (filtre de contenu Higgsfield).
5. Aucun mot de la liste « à éviter » du lexique voix dans les répliques.
6. Dialogues en guillemets français, au moins 3 plans par scène.
7. Voix off tenant dans la fenêtre de 7 s (2,0 s → 9,0 s).

## Ce qui reste à l'œil humain
Identité de Michael d'une scène à l'autre · absence de texte lisible généré par Seedance ·
compréhension sans le son · clap à 0,4 s · logo intact de 9 à 10 s.

## Résultat

✅ Aucune erreur bloquante.

| Épisode | Niveau | Détail |
|---|---|---|
| 04 | ALERTE | voix off ≈ 7.7 s (fenêtre 7 s) — variante courte proposée dans la fiche. |
| 13 | ALERTE | voix off ≈ 8.4 s (fenêtre 7 s) — variante courte proposée dans la fiche. |
| 14 | ALERTE | voix off ≈ 8.0 s (fenêtre 7 s) — variante courte proposée dans la fiche. |
| 16 | ALERTE | voix off ≈ 7.6 s (fenêtre 7 s) — variante courte proposée dans la fiche. |
| 17 | ALERTE | voix off ≈ 8.7 s (fenêtre 7 s) — variante courte proposée dans la fiche. |
| 18 | ALERTE | voix off ≈ 8.7 s (fenêtre 7 s) — variante courte proposée dans la fiche. |
| 20 | ALERTE | voix off ≈ 7.5 s (fenêtre 7 s) — variante courte proposée dans la fiche. |
| 21 | ALERTE | voix off ≈ 7.5 s (fenêtre 7 s) — variante courte proposée dans la fiche. |
| 23 | ALERTE | voix off ≈ 8.9 s (fenêtre 7 s) — variante courte proposée dans la fiche. |
| 25 | ALERTE | voix off ≈ 7.7 s (fenêtre 7 s) — variante courte proposée dans la fiche. |
| 26 | ALERTE | voix off ≈ 7.5 s (fenêtre 7 s) — variante courte proposée dans la fiche. |
| 28 | ALERTE | voix off ≈ 7.1 s (fenêtre 7 s) — variante courte proposée dans la fiche. |
| 29 | ALERTE | voix off ≈ 7.7 s (fenêtre 7 s) — variante courte proposée dans la fiche. |

