# Fiche fonctionnelle — consigne de rédaction

## Règle absolue

Chaque affirmation doit être **traçable** : soit à une frame de l'enregistrement,
soit à un schéma d'outil MCP. Renseigne `sources` pour chaque bloc, par exemple
`{"champs_cles": "schéma create_facture", "a_quoi_ca_sert": "frame 00:12"}`.
Ce que tu ne peux pas vérifier va dans `a_verifier` — jamais dans une affirmation.

## Étapes observées à l'écran

- 1. Partir du tableau de bord (0.0s → 10.0s)
- 2. Lire ce que l'on paie (10.0s → 20.0s)
- 3. Renseigner son adresse e-mail (20.0s → 32.0s)
- 4. Saisir sa carte (32.0s → 50.0s)
- 5. Compléter titulaire et pays (50.0s → 58.0s)
- 6. Payer (58.0s → 63.0s)
- 7. Suivre la liste de configuration (63.0s → 68.2s)

## Outils MCP retenus

- `get_revenue_summary` — Résumé du chiffre d'affaires à partir des factures et devis. Lecture seule.
  paramètres : periode

## Divergences à traiter

- Divergence : « champ E-mail » (22.0s) ne correspond à aucun paramètre des outils MCP retenus — à décrire depuis la frame, pas depuis un schéma.
- Divergence : « Informations de la carte » (34.0s) ne correspond à aucun paramètre des outils MCP retenus — à décrire depuis la frame, pas depuis un schéma.
- Divergence : « date d'expiration et CVC » (44.0s) ne correspond à aucun paramètre des outils MCP retenus — à décrire depuis la frame, pas depuis un schéma.
- Divergence : « Nom du titulaire et Pays ou région » (52.0s) ne correspond à aucun paramètre des outils MCP retenus — à décrire depuis la frame, pas depuis un schéma.

## Rappels de fond

- `a_quoi_ca_sert` : le bénéfice métier en deux phrases, **côté utilisateur**,
  pas côté logiciel.
- `prompt_claude` : une phrase qui fait la même chose que la démo, avec ses
  variables entre crochets et l'outil MCP visé.
- `erreurs_frequentes` : ce qui bloque réellement, observé ou documenté par un
  schéma (champ non modifiable après création, statut non transitionnable…).

Schéma complet : `src/schema/index.ts` → `FicheSchema`.
