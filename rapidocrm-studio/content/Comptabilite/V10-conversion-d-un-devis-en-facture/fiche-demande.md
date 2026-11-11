# Fiche fonctionnelle — consigne de rédaction

## Règle absolue

Chaque affirmation doit être **traçable** : soit à une frame de l'enregistrement,
soit à un schéma d'outil MCP. Renseigne `sources` pour chaque bloc, par exemple
`{"champs_cles": "schéma create_facture", "a_quoi_ca_sert": "frame 00:12"}`.
Ce que tu ne peux pas vérifier va dans `a_verifier` — jamais dans une affirmation.

## Étapes observées à l'écran

- 1. Ouvrir le devis à convertir (0.0s → 6.0s)
- 2. Signer le devis et enregistrer (6.0s → 29.0s)
- 3. Lire ce que le logiciel annonce (29.0s → 34.0s)
- 4. Passer à l'onglet facture (34.0s → 46.0s)
- 5. Retrouver la facture créée (46.0s → 55.5s)

## Outils MCP retenus

- `list_devis` — sans description
  paramètres : (aucun)
- `list_factures` — sans description
  paramètres : (aucun)

## Divergences à traiter

- Divergence : « onglet facture » (36.0s) ne correspond à aucun paramètre des outils MCP retenus — à décrire depuis la frame, pas depuis un schéma.

## Rappels de fond

- `a_quoi_ca_sert` : le bénéfice métier en deux phrases, **côté utilisateur**,
  pas côté logiciel.
- `prompt_claude` : une phrase qui fait la même chose que la démo, avec ses
  variables entre crochets et l'outil MCP visé.
- `erreurs_frequentes` : ce qui bloque réellement, observé ou documenté par un
  schéma (champ non modifiable après création, statut non transitionnable…).

Schéma complet : `src/schema/index.ts` → `FicheSchema`.
