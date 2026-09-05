# Fiche fonctionnelle — consigne de rédaction

## Règle absolue

Chaque affirmation doit être **traçable** : soit à une frame de l'enregistrement,
soit à un schéma d'outil MCP. Renseigne `sources` pour chaque bloc, par exemple
`{"champs_cles": "schéma create_facture", "a_quoi_ca_sert": "frame 00:12"}`.
Ce que tu ne peux pas vérifier va dans `a_verifier` — jamais dans une affirmation.

## Étapes observées à l'écran

- 1. Ouvrir « Envoyer une newsletter » (0.5s → 4.0s)
- 2. Dire à qui la newsletter part (4.0s → 8.5s)
- 3. Fixer la date et l'heure d'envoi (8.5s → 14.5s)
- 4. Choisir le modèle de newsletter (14.5s → 17.5s)
- 5. Lire la confirmation (17.5s → 20.0s)

## Outils MCP retenus

- `list_newsletters` — Tool RapidoCRM (Marketing) : list_newsletters. Utiliser ce tool pour cette action metier.
  paramètres : id, statut, periode, q, limit
- `list_campagnes` — Tool RapidoCRM (Marketing) : list_campagnes. Utiliser ce tool pour cette action metier.
  paramètres : id, statut, periode, q, limit

## Divergences à traiter

- Divergence : « Liste déroulante Envoyé à » (7.0s) ne correspond à aucun paramètre des outils MCP retenus — à décrire depuis la frame, pas depuis un schéma.
- Divergence : « Champ Date et heure d'envoi » (10.0s) ne correspond à aucun paramètre des outils MCP retenus — à décrire depuis la frame, pas depuis un schéma.
- Divergence : « Correction de l'heure d'envoi » (13.0s) ne correspond à aucun paramètre des outils MCP retenus — à décrire depuis la frame, pas depuis un schéma.
- Divergence : « Modèle de newsletter » (16.0s) ne correspond à aucun paramètre des outils MCP retenus — à décrire depuis la frame, pas depuis un schéma.

## Rappels de fond

- `a_quoi_ca_sert` : le bénéfice métier en deux phrases, **côté utilisateur**,
  pas côté logiciel.
- `prompt_claude` : une phrase qui fait la même chose que la démo, avec ses
  variables entre crochets et l'outil MCP visé.
- `erreurs_frequentes` : ce qui bloque réellement, observé ou documenté par un
  schéma (champ non modifiable après création, statut non transitionnable…).

Schéma complet : `src/schema/index.ts` → `FicheSchema`.
