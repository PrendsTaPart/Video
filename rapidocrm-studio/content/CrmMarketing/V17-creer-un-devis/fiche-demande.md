# Fiche fonctionnelle — consigne de rédaction

## Règle absolue

Chaque affirmation doit être **traçable** : soit à une frame de l'enregistrement,
soit à un schéma d'outil MCP. Renseigne `sources` pour chaque bloc, par exemple
`{"champs_cles": "schéma create_facture", "a_quoi_ca_sert": "frame 00:12"}`.
Ce que tu ne peux pas vérifier va dans `a_verifier` — jamais dans une affirmation.

## Étapes observées à l'écran

- 1. Ouvrir « Créer un devis » depuis la fiche (1.0s → 4.5s)
- 2. Logo et charte graphique du devis (4.5s → 8.5s)
- 3. Choisir le produit, les montants suivent (8.5s → 14.0s)
- 4. Fixer les dates du devis (14.0s → 19.0s)
- 5. Délai de paiement, mentions légales, statut (19.0s → 28.0s)
- 6. Mode de paiement, totaux et enregistrement (28.0s → 32.8s)
- 7. Retrouver le devis dans l'activité de la fiche (32.8s → 38.0s)

## Outils MCP retenus

- `list_devis` — Lister les devis avec filtres (statut, entreprise, recherche, période).
  paramètres : statut, entreprise_id, q, periode, limit

## Divergences à traiter

- Divergence : « Carte produit « identité visuelle » » (10.5s) ne correspond à aucun paramètre des outils MCP retenus — à décrire depuis la frame, pas depuis un schéma.
- Divergence : « Date de début » (16.0s) ne correspond à aucun paramètre des outils MCP retenus — à décrire depuis la frame, pas depuis un schéma.
- Divergence : « Mode de paiement et totaux » (30.0s) ne correspond à aucun paramètre des outils MCP retenus — à décrire depuis la frame, pas depuis un schéma.

## Rappels de fond

- `a_quoi_ca_sert` : le bénéfice métier en deux phrases, **côté utilisateur**,
  pas côté logiciel.
- `prompt_claude` : une phrase qui fait la même chose que la démo, avec ses
  variables entre crochets et l'outil MCP visé.
- `erreurs_frequentes` : ce qui bloque réellement, observé ou documenté par un
  schéma (champ non modifiable après création, statut non transitionnable…).

Schéma complet : `src/schema/index.ts` → `FicheSchema`.
