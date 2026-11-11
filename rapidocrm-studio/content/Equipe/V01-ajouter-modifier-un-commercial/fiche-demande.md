# Fiche fonctionnelle — consigne de rédaction

## Règle absolue

Chaque affirmation doit être **traçable** : soit à une frame de l'enregistrement,
soit à un schéma d'outil MCP. Renseigne `sources` pour chaque bloc, par exemple
`{"champs_cles": "schéma create_facture", "a_quoi_ca_sert": "frame 00:12"}`.
Ce que tu ne peux pas vérifier va dans `a_verifier` — jamais dans une affirmation.

## Étapes observées à l'écran

- 1. Ouvrir la page Commerciaux (0.0s → 5.0s)
- 2. Ouvrir le formulaire (5.0s → 12.0s)
- 3. Nommer le commercial et sa fonction (12.0s → 24.0s)
- 4. Renseigner ses coordonnées (24.0s → 38.0s)
- 5. Ajouter sa photo (38.0s → 47.0s)
- 6. Fixer ses objectifs mensuels (47.0s → 54.8s)
- 7. Lire l'avertissement d'activation (54.8s → 65.5s)

## Outils MCP retenus

- `list_commerciaux` — Lister les commerciaux avec statut actif/inactif et objectifs. Lecture seule.
  paramètres : q, statut, limit
- `get_commercial` — Afficher le détail d'un commercial avec objectifs et performance. Lecture seule.
  paramètres : id*
- `get_user_performance` — Performance d'un commercial (id fourni) ou de tous les commerciaux : objectifs, envois, taux. Lecture seule.
  paramètres : id

## Divergences à traiter

- Divergence : « champs Nom et Prénom » (13.0s) ne correspond à aucun paramètre des outils MCP retenus — à décrire depuis la frame, pas depuis un schéma.
- Divergence : « champ Fonction » (20.0s) ne correspond à aucun paramètre des outils MCP retenus — à décrire depuis la frame, pas depuis un schéma.
- Divergence : « champ Email » (25.0s) ne correspond à aucun paramètre des outils MCP retenus — à décrire depuis la frame, pas depuis un schéma.
- Divergence : « champs Numéro et Adresse » (30.0s) ne correspond à aucun paramètre des outils MCP retenus — à décrire depuis la frame, pas depuis un schéma.
- Divergence : « champ Code postal » (40.0s) ne correspond à aucun paramètre des outils MCP retenus — à décrire depuis la frame, pas depuis un schéma.
- Divergence : « champ Image, bouton parcourir » (47.0s) ne correspond à aucun paramètre des outils MCP retenus — à décrire depuis la frame, pas depuis un schéma.
- Divergence : « section « Objectifs mensuels de l'utilisateur » » (51.0s) ne correspond à aucun paramètre des outils MCP retenus — à décrire depuis la frame, pas depuis un schéma.

## Rappels de fond

- `a_quoi_ca_sert` : le bénéfice métier en deux phrases, **côté utilisateur**,
  pas côté logiciel.
- `prompt_claude` : une phrase qui fait la même chose que la démo, avec ses
  variables entre crochets et l'outil MCP visé.
- `erreurs_frequentes` : ce qui bloque réellement, observé ou documenté par un
  schéma (champ non modifiable après création, statut non transitionnable…).

Schéma complet : `src/schema/index.ts` → `FicheSchema`.
