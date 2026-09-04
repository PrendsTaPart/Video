# Lecture visuelle de l'enregistrement

Durée : 17.9 s · 2 changement(s) d'écran détecté(s) à
9.8s, 12.3s.

Les frames sont dans `frames/` : `seconde-XXXX.jpg` (une par seconde) et
`rupture-XXX-<t>s.jpg` (haute définition, aux changements d'écran).

Lis-les et écris `analyse.json` en décrivant, pour chaque moment :

- **l'écran affiché** — nom de la page ou de la modale (`ecrans`)
- **l'action réalisée** — clic, saisie, sélection, validation, ouverture, défilement
- **la zone concernée**, en coordonnées normalisées `{x, y, w, h}` (0 → 1)
- **le texte visible pertinent** — libellés de boutons, titres de champs

Puis regroupe les actions en **3 à 7 étapes logiques**, chacune avec un titre
court à l'infinitif (« Ouvrir la fiche entreprise », « Renseigner le SIRET »).

## Confidentialité — obligatoire

Liste dans `zones_sensibles` **toute donnée réelle visible** : email, téléphone,
SIRET, IBAN, nom de client. Indique `t`, `fin` et `zone` : le rendu les floutera.
Une donnée oubliée ici part en ligne.

## Schéma attendu

Voir `src/schema/index.ts` → `AnalyseSchema`. Les indices déterministes
(ruptures, curseur, liste des frames) sont dans `analyse-brute.json`.
