# Fiche fonctionnelle — consigne de rédaction

## Règle absolue

Chaque affirmation doit être **traçable** : soit à une frame de l'enregistrement,
soit à un schéma d'outil MCP. Renseigne `sources` pour chaque bloc, par exemple
`{"champs_cles": "schéma create_facture", "a_quoi_ca_sert": "frame 00:12"}`.
Ce que tu ne peux pas vérifier va dans `a_verifier` — jamais dans une affirmation.

## Étapes observées à l'écran

- 1. Ouvrir la page Produits (0.0s → 5.0s)
- 2. Nommer le produit et lui donner une image (5.0s → 18.0s)
- 3. Fixer sa période et sa nature (18.0s → 30.0s)
- 4. Renseigner le prix et la TVA (30.0s → 38.0s)
- 5. Décrire le produit (38.0s → 43.5s)
- 6. Retrouver la fiche dans la liste (43.5s → 60.5s)

## Outils MCP retenus

- `list_products` — Liste les produits et offres de l'entreprise. Lecture seule.
  paramètres : q, statut, limit, periode
- `get_product` — Détail complet d'un produit ou d'une offre : prix, TVA, description. Lecture seule.
  paramètres : id*
- `list_programmes_fidelite` — Liste les programmes de fidélité de l'espace, avec l'entreprise associée et ses statistiques : nombre de clients, points offerts, gains offerts. Lecture seule.
  paramètres : (aucun)

## Divergences à traiter

- Divergence : « champ Nom du produit » (8.0s) ne correspond à aucun paramètre des outils MCP retenus — à décrire depuis la frame, pas depuis un schéma.
- Divergence : « zone Image du produit, bouton parcourir » (13.0s) ne correspond à aucun paramètre des outils MCP retenus — à décrire depuis la frame, pas depuis un schéma.
- Divergence : « champs Date de début et Date de fin » (20.0s) ne correspond à aucun paramètre des outils MCP retenus — à décrire depuis la frame, pas depuis un schéma.
- Divergence : « champ Nature » (26.0s) ne correspond à aucun paramètre des outils MCP retenus — à décrire depuis la frame, pas depuis un schéma.
- Divergence : « champs Prix ht, Pourcentage tva et Prix ttc » (32.0s) ne correspond à aucun paramètre des outils MCP retenus — à décrire depuis la frame, pas depuis un schéma.

## Rappels de fond

- `a_quoi_ca_sert` : le bénéfice métier en deux phrases, **côté utilisateur**,
  pas côté logiciel.
- `prompt_claude` : une phrase qui fait la même chose que la démo, avec ses
  variables entre crochets et l'outil MCP visé.
- `erreurs_frequentes` : ce qui bloque réellement, observé ou documenté par un
  schéma (champ non modifiable après création, statut non transitionnable…).

Schéma complet : `src/schema/index.ts` → `FicheSchema`.
