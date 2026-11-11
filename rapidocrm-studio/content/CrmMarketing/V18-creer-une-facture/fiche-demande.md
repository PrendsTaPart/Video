# Fiche fonctionnelle — consigne de rédaction

## Règle absolue

Chaque affirmation doit être **traçable** : soit à une frame de l'enregistrement,
soit à un schéma d'outil MCP. Renseigne `sources` pour chaque bloc, par exemple
`{"champs_cles": "schéma create_facture", "a_quoi_ca_sert": "frame 00:12"}`.
Ce que tu ne peux pas vérifier va dans `a_verifier` — jamais dans une affirmation.

## Étapes observées à l'écran

- 1. Ouvrir « Créer une facture » depuis la fiche (0.8s → 3.5s)
- 2. Logo et charte graphique de la facture (3.5s → 8.0s)
- 3. Choisir le produit à facturer (8.0s → 15.0s)
- 4. Laisser les montants se calculer (15.0s → 22.0s)
- 5. Délai, mentions légales et statut (22.0s → 27.5s)
- 6. Mode de paiement, totaux et enregistrement (27.5s → 31.0s)
- 7. Retrouver la facture dans l'activité de la fiche (31.0s → 34.0s)

## Outils MCP retenus

- `list_factures` — Lister les factures du CRM (en attente, payées, etc.).
  paramètres : statut, periode, limit

## Divergences à traiter

- Divergence : « Produit « Pack site vitrine » » (14.0s) ne correspond à aucun paramètre des outils MCP retenus — à décrire depuis la frame, pas depuis un schéma.
- Divergence : « Dates de début et de fin » (19.0s) ne correspond à aucun paramètre des outils MCP retenus — à décrire depuis la frame, pas depuis un schéma.
- Divergence : « Mode de paiement et totaux » (29.0s) ne correspond à aucun paramètre des outils MCP retenus — à décrire depuis la frame, pas depuis un schéma.

## Rappels de fond

- `a_quoi_ca_sert` : le bénéfice métier en deux phrases, **côté utilisateur**,
  pas côté logiciel.
- `prompt_claude` : une phrase qui fait la même chose que la démo, avec ses
  variables entre crochets et l'outil MCP visé.
- `erreurs_frequentes` : ce qui bloque réellement, observé ou documenté par un
  schéma (champ non modifiable après création, statut non transitionnable…).

Schéma complet : `src/schema/index.ts` → `FicheSchema`.
