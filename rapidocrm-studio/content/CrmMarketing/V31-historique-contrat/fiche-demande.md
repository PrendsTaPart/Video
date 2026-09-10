# Fiche fonctionnelle — consigne de rédaction

## Règle absolue

Chaque affirmation doit être **traçable** : soit à une frame de l'enregistrement,
soit à un schéma d'outil MCP. Renseigne `sources` pour chaque bloc, par exemple
`{"champs_cles": "schéma create_facture", "a_quoi_ca_sert": "frame 00:12"}`.
Ce que tu ne peux pas vérifier va dans `a_verifier` — jamais dans une affirmation.

## Étapes observées à l'écran

- 1. Ouvrir l'historique des contrats (0.5s → 6.5s)
- 2. Lire le tableau des contrats (6.5s → 9.8s)
- 3. Ouvrir le contrat (9.8s → 12.3s)
- 4. Parcourir le contrat, page par page (12.3s → 17.9s)

## Outils MCP retenus

- `list_contrats` — Lister les contrats clients, filtrables par statut et expiration.
  paramètres : statut, entreprise_id, date_debut, date_fin, q, limit


## Rappels de fond

- `a_quoi_ca_sert` : le bénéfice métier en deux phrases, **côté utilisateur**,
  pas côté logiciel.
- `prompt_claude` : une phrase qui fait la même chose que la démo, avec ses
  variables entre crochets et l'outil MCP visé.
- `erreurs_frequentes` : ce qui bloque réellement, observé ou documenté par un
  schéma (champ non modifiable après création, statut non transitionnable…).

Schéma complet : `src/schema/index.ts` → `FicheSchema`.
