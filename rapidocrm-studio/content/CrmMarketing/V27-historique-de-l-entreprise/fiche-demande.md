# Fiche fonctionnelle — consigne de rédaction

## Règle absolue

Chaque affirmation doit être **traçable** : soit à une frame de l'enregistrement,
soit à un schéma d'outil MCP. Renseigne `sources` pour chaque bloc, par exemple
`{"champs_cles": "schéma create_facture", "a_quoi_ca_sert": "frame 00:12"}`.
Ce que tu ne peux pas vérifier va dans `a_verifier` — jamais dans une affirmation.

## Étapes observées à l'écran

- 1. Ouvrir le panneau Entreprise de la fiche (1.0s → 6.5s)
- 2. Ouvrir l'historique de l'entreprise (6.5s → 10.5s)
- 3. Parcourir les neuf journaux (10.5s → 14.5s)
- 4. Choisir le journal à consulter (14.5s → 17.8s)

## Outils MCP retenus

- `get_entreprise` — Détail complet d'une entreprise (tous les champs, pas seulement nom/statut).
  paramètres : id*
- `get_interaction_stats` — Statistiques d'interactions (emails, SMS, appels, RDV...) par type.
  paramètres : entreprise_id, periode


## Rappels de fond

- `a_quoi_ca_sert` : le bénéfice métier en deux phrases, **côté utilisateur**,
  pas côté logiciel.
- `prompt_claude` : une phrase qui fait la même chose que la démo, avec ses
  variables entre crochets et l'outil MCP visé.
- `erreurs_frequentes` : ce qui bloque réellement, observé ou documenté par un
  schéma (champ non modifiable après création, statut non transitionnable…).

Schéma complet : `src/schema/index.ts` → `FicheSchema`.
