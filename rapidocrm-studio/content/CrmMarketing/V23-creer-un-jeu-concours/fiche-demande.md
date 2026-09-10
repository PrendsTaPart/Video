# Fiche fonctionnelle — consigne de rédaction

## Règle absolue

Chaque affirmation doit être **traçable** : soit à une frame de l'enregistrement,
soit à un schéma d'outil MCP. Renseigne `sources` pour chaque bloc, par exemple
`{"champs_cles": "schéma create_facture", "a_quoi_ca_sert": "frame 00:12"}`.
Ce que tu ne peux pas vérifier va dans `a_verifier` — jamais dans une affirmation.

## Étapes observées à l'écran

- 1. Ouvrir les jeux depuis la fiche entreprise (1.0s → 5.0s)
- 2. Choisir un modèle de jeu (5.0s → 10.0s)
- 3. Les trois étapes de personnalisation (10.0s → 15.0s)
- 4. Régler l'apparence et voir l'aperçu (15.0s → 24.0s)
- 5. Décrire les lots à gagner (24.0s → 30.5s)
- 6. Revenir à la fiche (30.5s → 34.2s)

## Outils MCP retenus

- `list_jeux_concours` — Tool RapidoCRM (Marketing) : list_jeux_concours. Utiliser ce tool pour cette action metier.
  paramètres : id, statut, periode, q, limit

## Divergences à traiter

- Divergence : « Bloc Cadeaux » (26.0s) ne correspond à aucun paramètre des outils MCP retenus — à décrire depuis la frame, pas depuis un schéma.

## Rappels de fond

- `a_quoi_ca_sert` : le bénéfice métier en deux phrases, **côté utilisateur**,
  pas côté logiciel.
- `prompt_claude` : une phrase qui fait la même chose que la démo, avec ses
  variables entre crochets et l'outil MCP visé.
- `erreurs_frequentes` : ce qui bloque réellement, observé ou documenté par un
  schéma (champ non modifiable après création, statut non transitionnable…).

Schéma complet : `src/schema/index.ts` → `FicheSchema`.
