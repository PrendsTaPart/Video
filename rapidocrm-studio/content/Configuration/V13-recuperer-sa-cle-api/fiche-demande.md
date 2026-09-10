# Fiche fonctionnelle — consigne de rédaction

## Règle absolue

Chaque affirmation doit être **traçable** : soit à une frame de l'enregistrement,
soit à un schéma d'outil MCP. Renseigne `sources` pour chaque bloc, par exemple
`{"champs_cles": "schéma create_facture", "a_quoi_ca_sert": "frame 00:12"}`.
Ce que tu ne peux pas vérifier va dans `a_verifier` — jamais dans une affirmation.

## Étapes observées à l'écran

- 1. Ouvrir l'onglet Tokens api (0.0s → 4.0s)
- 2. Créer un nouveau token (4.0s → 14.0s)
- 3. Fixer une date d'expiration (14.0s → 19.0s)
- 4. Cocher les permissions (19.0s → 28.0s)
- 5. Générer le token (28.0s → 34.0s)
- 6. Relire ses permissions (34.0s → 39.0s)
- 7. Révoquer un token (39.0s → 43.2s)

## Outils MCP retenus

- `list_entreprises` — CRM : liste les entreprises de la base. Lecture seule. C'est la ressource appelée par l'exemple curl affiché sous le tableau des tokens.
  paramètres : limit, q, statut, periode

## Divergences à traiter

- Divergence : « champ Nom du token » (8.0s) ne correspond à aucun paramètre des outils MCP retenus — à décrire depuis la frame, pas depuis un schéma.
- Divergence : « champ Date d'expiration » (15.0s) ne correspond à aucun paramètre des outils MCP retenus — à décrire depuis la frame, pas depuis un schéma.
- Divergence : « colonne Lire du tableau des permissions » (20.0s) ne correspond à aucun paramètre des outils MCP retenus — à décrire depuis la frame, pas depuis un schéma.

## Rappels de fond

- `a_quoi_ca_sert` : le bénéfice métier en deux phrases, **côté utilisateur**,
  pas côté logiciel.
- `prompt_claude` : une phrase qui fait la même chose que la démo, avec ses
  variables entre crochets et l'outil MCP visé.
- `erreurs_frequentes` : ce qui bloque réellement, observé ou documenté par un
  schéma (champ non modifiable après création, statut non transitionnable…).

Schéma complet : `src/schema/index.ts` → `FicheSchema`.
