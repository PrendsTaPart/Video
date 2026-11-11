# Fiche fonctionnelle — consigne de rédaction

## Règle absolue

Chaque affirmation doit être **traçable** : soit à une frame de l'enregistrement,
soit à un schéma d'outil MCP. Renseigne `sources` pour chaque bloc, par exemple
`{"champs_cles": "schéma create_facture", "a_quoi_ca_sert": "frame 00:12"}`.
Ce que tu ne peux pas vérifier va dans `a_verifier` — jamais dans une affirmation.

## Étapes observées à l'écran

- 1. Ouvrir l'onglet dépenses (0.0s → 6.5s)
- 2. Lire le tableau des dépenses (6.5s → 13.5s)
- 3. Filtrer et trier la liste (13.5s → 21.5s)
- 4. Ouvrir le menu d'une dépense (21.5s → 27.5s)
- 5. Remonter à la fiche de l'entreprise (27.5s → 31.5s)

## Outils MCP retenus

(aucun outil ne correspond — dis-le dans a_verifier)

## Divergences à traiter

- Divergence : « listes déroulantes Statut et Entreprise » (15.0s) ne correspond à aucun paramètre des outils MCP retenus — à décrire depuis la frame, pas depuis un schéma.

## Rappels de fond

- `a_quoi_ca_sert` : le bénéfice métier en deux phrases, **côté utilisateur**,
  pas côté logiciel.
- `prompt_claude` : une phrase qui fait la même chose que la démo, avec ses
  variables entre crochets et l'outil MCP visé.
- `erreurs_frequentes` : ce qui bloque réellement, observé ou documenté par un
  schéma (champ non modifiable après création, statut non transitionnable…).

Schéma complet : `src/schema/index.ts` → `FicheSchema`.
