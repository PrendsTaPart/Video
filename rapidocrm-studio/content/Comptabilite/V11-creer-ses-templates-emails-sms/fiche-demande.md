# Fiche fonctionnelle — consigne de rédaction

## Règle absolue

Chaque affirmation doit être **traçable** : soit à une frame de l'enregistrement,
soit à un schéma d'outil MCP. Renseigne `sources` pour chaque bloc, par exemple
`{"champs_cles": "schéma create_facture", "a_quoi_ca_sert": "frame 00:12"}`.
Ce que tu ne peux pas vérifier va dans `a_verifier` — jamais dans une affirmation.

## Étapes observées à l'écran

- 1. Ouvrir la page des templates SMS (0.0s → 5.8s)
- 2. Nommer le template (5.8s → 11.5s)
- 3. Écrire le message (11.5s → 18.0s)
- 4. Ajouter le bouton et valider (18.0s → 24.0s)
- 5. Retrouver le template dans la liste (24.0s → 30.0s)

## Outils MCP retenus

- `list_templates_sms` — sans description
  paramètres : (aucun)
- `get_template` — sans description
  paramètres : (aucun)

## Divergences à traiter

- Divergence : « champ Nom du template » (8.0s) ne correspond à aucun paramètre des outils MCP retenus — à décrire depuis la frame, pas depuis un schéma.
- Divergence : « zone de texte du message » (14.0s) ne correspond à aucun paramètre des outils MCP retenus — à décrire depuis la frame, pas depuis un schéma.
- Divergence : « liste Ajouter un CTA » (20.0s) ne correspond à aucun paramètre des outils MCP retenus — à décrire depuis la frame, pas depuis un schéma.

## Rappels de fond

- `a_quoi_ca_sert` : le bénéfice métier en deux phrases, **côté utilisateur**,
  pas côté logiciel.
- `prompt_claude` : une phrase qui fait la même chose que la démo, avec ses
  variables entre crochets et l'outil MCP visé.
- `erreurs_frequentes` : ce qui bloque réellement, observé ou documenté par un
  schéma (champ non modifiable après création, statut non transitionnable…).

Schéma complet : `src/schema/index.ts` → `FicheSchema`.
