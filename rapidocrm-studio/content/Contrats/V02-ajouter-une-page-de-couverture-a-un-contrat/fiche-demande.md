# Fiche fonctionnelle — consigne de rédaction

## Règle absolue

Chaque affirmation doit être **traçable** : soit à une frame de l'enregistrement,
soit à un schéma d'outil MCP. Renseigne `sources` pour chaque bloc, par exemple
`{"champs_cles": "schéma create_facture", "a_quoi_ca_sert": "frame 00:12"}`.
Ce que tu ne peux pas vérifier va dans `a_verifier` — jamais dans une affirmation.

## Étapes observées à l'écran

- 1. Ouvrir la liste des templates de contrat (0.5s → 4.8s)
- 2. Ouvrir le choix de la couverture (4.8s → 9.5s)
- 3. Choisir la couverture et confirmer (9.5s → 15.5s)
- 4. Voir la couverture en tête du contrat (19.5s → 26.0s)

## Outils MCP retenus

- `list_contrats` — Lister les contrats clients, filtrables par statut et expiration. Lecture seule.
  paramètres : q, statut, entreprise_id, date_debut, date_fin, limit
- `list_contrat_templates` — Lister les templates de contrat disponibles. Lecture seule.
  paramètres : search, limit
- `get_contrat` — Détail complet d'un contrat client. Lecture seule.
  paramètres : id*

## Divergences à traiter

- Divergence : « Vignette « Page de couverture — contrat » » (11.0s) ne correspond à aucun paramètre des outils MCP retenus — à décrire depuis la frame, pas depuis un schéma.

## Rappels de fond

- `a_quoi_ca_sert` : le bénéfice métier en deux phrases, **côté utilisateur**,
  pas côté logiciel.
- `prompt_claude` : une phrase qui fait la même chose que la démo, avec ses
  variables entre crochets et l'outil MCP visé.
- `erreurs_frequentes` : ce qui bloque réellement, observé ou documenté par un
  schéma (champ non modifiable après création, statut non transitionnable…).

Schéma complet : `src/schema/index.ts` → `FicheSchema`.
