# Fiche fonctionnelle — consigne de rédaction

## Règle absolue

Chaque affirmation doit être **traçable** : soit à une frame de l'enregistrement,
soit à un schéma d'outil MCP. Renseigne `sources` pour chaque bloc, par exemple
`{"champs_cles": "schéma create_facture", "a_quoi_ca_sert": "frame 00:12"}`.
Ce que tu ne peux pas vérifier va dans `a_verifier` — jamais dans une affirmation.

## Étapes observées à l'écran

- 1. Ouvrir « Ajouter un PDF » depuis la fiche (1.0s → 5.0s)
- 2. Nommer le document (5.0s → 11.5s)
- 3. Choisir le fichier et l'ajouter (11.5s → 17.0s)
- 4. Retrouver la fiche et ses documents (17.0s → 24.3s)

## Outils MCP retenus

- `get_entreprise` — Détail complet d'une entreprise (tous les champs, pas seulement nom/statut).
  paramètres : id*

## Divergences à traiter

- Divergence : « Champ Nom du fichier » (10.0s) ne correspond à aucun paramètre des outils MCP retenus — à décrire depuis la frame, pas depuis un schéma.

## Rappels de fond

- `a_quoi_ca_sert` : le bénéfice métier en deux phrases, **côté utilisateur**,
  pas côté logiciel.
- `prompt_claude` : une phrase qui fait la même chose que la démo, avec ses
  variables entre crochets et l'outil MCP visé.
- `erreurs_frequentes` : ce qui bloque réellement, observé ou documenté par un
  schéma (champ non modifiable après création, statut non transitionnable…).

Schéma complet : `src/schema/index.ts` → `FicheSchema`.
