# Fiche fonctionnelle — consigne de rédaction

## Règle absolue

Chaque affirmation doit être **traçable** : soit à une frame de l'enregistrement,
soit à un schéma d'outil MCP. Renseigne `sources` pour chaque bloc, par exemple
`{"champs_cles": "schéma create_facture", "a_quoi_ca_sert": "frame 00:12"}`.
Ce que tu ne peux pas vérifier va dans `a_verifier` — jamais dans une affirmation.

## Étapes observées à l'écran

- 1. Trouver la section Agent ia (0.0s → 4.0s)
- 2. Repérer les autres réglages de la page (4.0s → 8.0s)
- 3. Coller sa propre clé api (8.0s → 12.0s)
- 4. Enregistrer (12.0s → 14.5s)
- 5. Laisser vide pour la clé du serveur (14.5s → 22.0s)

## Outils MCP retenus

- `get_agent_vocal_config` — Affiche la configuration de l'agent vocal IA : pitch, secteur, objectif d'appel, ton de voix, catalogue produits, minutes de crédit restantes et statut Twilio. Lecture seule.
  paramètres : (aucun)

## Divergences à traiter

- Divergence : « Clé api agent ia » (10.0s) ne correspond à aucun paramètre des outils MCP retenus — à décrire depuis la frame, pas depuis un schéma.

## Rappels de fond

- `a_quoi_ca_sert` : le bénéfice métier en deux phrases, **côté utilisateur**,
  pas côté logiciel.
- `prompt_claude` : une phrase qui fait la même chose que la démo, avec ses
  variables entre crochets et l'outil MCP visé.
- `erreurs_frequentes` : ce qui bloque réellement, observé ou documenté par un
  schéma (champ non modifiable après création, statut non transitionnable…).

Schéma complet : `src/schema/index.ts` → `FicheSchema`.
