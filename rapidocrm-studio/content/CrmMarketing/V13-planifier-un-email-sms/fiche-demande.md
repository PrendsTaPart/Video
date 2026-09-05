# Fiche fonctionnelle — consigne de rédaction

## Règle absolue

Chaque affirmation doit être **traçable** : soit à une frame de l'enregistrement,
soit à un schéma d'outil MCP. Renseigne `sources` pour chaque bloc, par exemple
`{"champs_cles": "schéma create_facture", "a_quoi_ca_sert": "frame 00:12"}`.
Ce que tu ne peux pas vérifier va dans `a_verifier` — jamais dans une affirmation.

## Étapes observées à l'écran

- 1. Ouvrir le panneau Communication de la fiche (0.5s → 4.0s)
- 2. Choisir « Planifier un SMS » (4.0s → 6.5s)
- 3. Dire à qui le SMS part (6.5s → 10.5s)
- 4. Choisir le modèle de SMS (10.5s → 14.0s)
- 5. Fixer la date et l'heure d'envoi (14.0s → 20.5s)
- 6. Valider la planification (20.5s → 25.3s)

## Outils MCP retenus

- `list_templates_sms` — Lister les templates SMS disponibles.
  paramètres : search, limit
- `list_templates_email` — Lister les templates email disponibles pour campagnes et workflows.
  paramètres : search, limit

## Divergences à traiter

- Divergence : « Liste déroulante « Envoyé à » » (9.0s) ne correspond à aucun paramètre des outils MCP retenus — à décrire depuis la frame, pas depuis un schéma.
- Divergence : « Modèle de template SMS « Création de devis » » (12.0s) ne correspond à aucun paramètre des outils MCP retenus — à décrire depuis la frame, pas depuis un schéma.
- Divergence : « Champ Date et heure d'envoi » (15.0s) ne correspond à aucun paramètre des outils MCP retenus — à décrire depuis la frame, pas depuis un schéma.
- Divergence : « Correction de l'heure d'envoi » (19.0s) ne correspond à aucun paramètre des outils MCP retenus — à décrire depuis la frame, pas depuis un schéma.

## Rappels de fond

- `a_quoi_ca_sert` : le bénéfice métier en deux phrases, **côté utilisateur**,
  pas côté logiciel.
- `prompt_claude` : une phrase qui fait la même chose que la démo, avec ses
  variables entre crochets et l'outil MCP visé.
- `erreurs_frequentes` : ce qui bloque réellement, observé ou documenté par un
  schéma (champ non modifiable après création, statut non transitionnable…).

Schéma complet : `src/schema/index.ts` → `FicheSchema`.
