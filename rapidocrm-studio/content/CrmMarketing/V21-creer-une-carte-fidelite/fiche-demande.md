# Fiche fonctionnelle — consigne de rédaction

## Règle absolue

Chaque affirmation doit être **traçable** : soit à une frame de l'enregistrement,
soit à un schéma d'outil MCP. Renseigne `sources` pour chaque bloc, par exemple
`{"champs_cles": "schéma create_facture", "a_quoi_ca_sert": "frame 00:12"}`.
Ce que tu ne peux pas vérifier va dans `a_verifier` — jamais dans une affirmation.

## Étapes observées à l'écran

- 1. Ouvrir l'assistant de carte de fidélité (1.0s → 7.0s)
- 2. Choisir la taille de la carte (7.0s → 12.0s)
- 3. Choisir le modèle de carte (12.0s → 16.0s)
- 4. Relire le récapitulatif et enregistrer (16.0s → 20.7s)
- 5. Retrouver la carte dans les programmes de fidélité (20.7s → 25.7s)

## Outils MCP retenus

- `list_programmes_fidelite` — Liste les programmes de fidélité créés dans votre espace, avec l'entreprise associée et ses statistiques (nombre de clients, points offerts, gains offerts).
  paramètres : (aucun)
- `list_cartes_fidelite` — Liste les cartes de fidélité des contacts, avec les statistiques (points offerts, nombre de clients, gains offerts).
  paramètres : programme_id, q, statut, date_debut, date_fin, limit

## Divergences à traiter

- Divergence : « Les trois tailles de carte proposées » (9.0s) ne correspond à aucun paramètre des outils MCP retenus — à décrire depuis la frame, pas depuis un schéma.
- Divergence : « Modèles de carte, étape Design et paramétrage » (13.0s) ne correspond à aucun paramètre des outils MCP retenus — à décrire depuis la frame, pas depuis un schéma.

## Rappels de fond

- `a_quoi_ca_sert` : le bénéfice métier en deux phrases, **côté utilisateur**,
  pas côté logiciel.
- `prompt_claude` : une phrase qui fait la même chose que la démo, avec ses
  variables entre crochets et l'outil MCP visé.
- `erreurs_frequentes` : ce qui bloque réellement, observé ou documenté par un
  schéma (champ non modifiable après création, statut non transitionnable…).

Schéma complet : `src/schema/index.ts` → `FicheSchema`.
