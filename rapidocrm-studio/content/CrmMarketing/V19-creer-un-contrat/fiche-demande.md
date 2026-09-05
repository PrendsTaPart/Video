# Fiche fonctionnelle — consigne de rédaction

## Règle absolue

Chaque affirmation doit être **traçable** : soit à une frame de l'enregistrement,
soit à un schéma d'outil MCP. Renseigne `sources` pour chaque bloc, par exemple
`{"champs_cles": "schéma create_facture", "a_quoi_ca_sert": "frame 00:12"}`.
Ce que tu ne peux pas vérifier va dans `a_verifier` — jamais dans une affirmation.

## Étapes observées à l'écran

- 1. Ouvrir « Créer un contrat » depuis la fiche (1.0s → 4.5s)
- 2. Choisir un modèle dans la bibliothèque (4.5s → 9.5s)
- 3. Vérifier le destinataire du contrat (9.5s → 15.0s)
- 4. Fixer les dates de début et de fin (15.0s → 26.0s)
- 5. Choisir le modèle d'e-mail et envoyer (26.0s → 31.0s)
- 6. Lire la confirmation (31.0s → 39.0s)

## Outils MCP retenus

- `list_contrat_templates` — Lister les templates de contrat disponibles.
  paramètres : search, limit
- `list_contrats` — Lister les contrats clients, filtrables par statut et expiration.
  paramètres : statut, entreprise_id, date_debut, date_fin, q, limit

## Divergences à traiter

- Divergence : « Liste Choisir template mail » (28.0s) ne correspond à aucun paramètre des outils MCP retenus — à décrire depuis la frame, pas depuis un schéma.

## Rappels de fond

- `a_quoi_ca_sert` : le bénéfice métier en deux phrases, **côté utilisateur**,
  pas côté logiciel.
- `prompt_claude` : une phrase qui fait la même chose que la démo, avec ses
  variables entre crochets et l'outil MCP visé.
- `erreurs_frequentes` : ce qui bloque réellement, observé ou documenté par un
  schéma (champ non modifiable après création, statut non transitionnable…).

Schéma complet : `src/schema/index.ts` → `FicheSchema`.
