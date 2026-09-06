# Fiche fonctionnelle — consigne de rédaction

## Règle absolue

Chaque affirmation doit être **traçable** : soit à une frame de l'enregistrement,
soit à un schéma d'outil MCP. Renseigne `sources` pour chaque bloc, par exemple
`{"champs_cles": "schéma create_facture", "a_quoi_ca_sert": "frame 00:12"}`.
Ce que tu ne peux pas vérifier va dans `a_verifier` — jamais dans une affirmation.

## Étapes observées à l'écran

- 1. Ouvrir « Prendre un rendez-vous » (1.0s → 6.0s)
- 2. Donner un titre au rendez-vous (6.0s → 16.0s)
- 3. Fixer le créneau, début et fin (16.0s → 44.0s)
- 4. Choisir les invités et les organisateurs (44.0s → 56.0s)
- 5. Type de rendez-vous, rappel et mode d'envoi (56.0s → 66.0s)
- 6. Ajouter une note et enregistrer (66.0s → 73.0s)

## Outils MCP retenus

- `list_rdvs` — Tool RapidoCRM (Agenda et Evenements) : list_rdvs. Utiliser ce tool pour cette action metier.
  paramètres : id, statut, periode, q, limit
- `get_today_schedule` — Programme agenda de la période : rendez-vous et événements.
  paramètres : periode

## Divergences à traiter

- Divergence : « Champ Titre » (13.0s) ne correspond à aucun paramètre des outils MCP retenus — à décrire depuis la frame, pas depuis un schéma.
- Divergence : « Champ De du créneau » (22.0s) ne correspond à aucun paramètre des outils MCP retenus — à décrire depuis la frame, pas depuis un schéma.
- Divergence : « Champ A du créneau » (40.0s) ne correspond à aucun paramètre des outils MCP retenus — à décrire depuis la frame, pas depuis un schéma.
- Divergence : « Liste des invités proposés » (48.0s) ne correspond à aucun paramètre des outils MCP retenus — à décrire depuis la frame, pas depuis un schéma.
- Divergence : « Type de rendez-vous, rappel et mode d'envoi » (58.0s) ne correspond à aucun paramètre des outils MCP retenus — à décrire depuis la frame, pas depuis un schéma.
- Divergence : « Informations complémentaires » (67.0s) ne correspond à aucun paramètre des outils MCP retenus — à décrire depuis la frame, pas depuis un schéma.

## Rappels de fond

- `a_quoi_ca_sert` : le bénéfice métier en deux phrases, **côté utilisateur**,
  pas côté logiciel.
- `prompt_claude` : une phrase qui fait la même chose que la démo, avec ses
  variables entre crochets et l'outil MCP visé.
- `erreurs_frequentes` : ce qui bloque réellement, observé ou documenté par un
  schéma (champ non modifiable après création, statut non transitionnable…).

Schéma complet : `src/schema/index.ts` → `FicheSchema`.
