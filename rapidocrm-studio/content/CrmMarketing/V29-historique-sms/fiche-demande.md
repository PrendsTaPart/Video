# Fiche fonctionnelle — consigne de rédaction

## Règle absolue

Chaque affirmation doit être **traçable** : soit à une frame de l'enregistrement,
soit à un schéma d'outil MCP. Renseigne `sources` pour chaque bloc, par exemple
`{"champs_cles": "schéma create_facture", "a_quoi_ca_sert": "frame 00:12"}`.
Ce que tu ne peux pas vérifier va dans `a_verifier` — jamais dans une affirmation.

## Étapes observées à l'écran

- 1. Ouvrir l'historique des SMS (0.5s → 6.5s)
- 2. Lire le tableau des envois (6.5s → 10.0s)
- 3. Rouvrir un SMS envoyé (10.0s → 13.0s)
- 4. Revenir à la liste (13.0s → 14.2s)

## Outils MCP retenus

- `get_interaction_stats` — Statistiques d'interactions (emails, SMS, appels, RDV...) par type.
  paramètres : entreprise_id, periode
- `list_templates_sms` — Lister les templates SMS disponibles.
  paramètres : search, limit


## Rappels de fond

- `a_quoi_ca_sert` : le bénéfice métier en deux phrases, **côté utilisateur**,
  pas côté logiciel.
- `prompt_claude` : une phrase qui fait la même chose que la démo, avec ses
  variables entre crochets et l'outil MCP visé.
- `erreurs_frequentes` : ce qui bloque réellement, observé ou documenté par un
  schéma (champ non modifiable après création, statut non transitionnable…).

Schéma complet : `src/schema/index.ts` → `FicheSchema`.
