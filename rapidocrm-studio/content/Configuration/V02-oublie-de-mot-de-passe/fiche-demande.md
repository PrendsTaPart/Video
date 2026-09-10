# Fiche fonctionnelle — consigne de rédaction

## Règle absolue

Chaque affirmation doit être **traçable** : soit à une frame de l'enregistrement,
soit à un schéma d'outil MCP. Renseigne `sources` pour chaque bloc, par exemple
`{"champs_cles": "schéma create_facture", "a_quoi_ca_sert": "frame 00:12"}`.
Ce que tu ne peux pas vérifier va dans `a_verifier` — jamais dans une affirmation.

## Étapes observées à l'écran

- 1. Ouvrir « mot de passe oublié » (0.0s → 6.0s)
- 2. Saisir son adresse e-mail (6.0s → 13.5s)
- 3. Recevoir le lien de réinitialisation (13.5s → 21.5s)
- 4. Choisir un nouveau mot de passe (21.5s → 34.0s)
- 5. Se reconnecter (34.0s → 45.0s)
- 6. Retrouver son tableau de bord (45.0s → 51.1s)

## Outils MCP retenus

- `list_users` — Utilisateurs : liste les utilisateurs de l'entreprise. Lecture seule. Ne gère ni la connexion ni le mot de passe.
  paramètres : id, q, limit, statut, periode
- `get_user` — Utilisateurs : fiche d'un utilisateur par son identifiant. Lecture seule. N'expose aucun mot de passe.
  paramètres : id*, q
- `create_user` — Utilisateurs : crée un utilisateur dans une entreprise déjà ouverte. Écriture — non utilisé par ce pipeline. Ne couvre ni l'inscription initiale ni la réinitialisation de mot de passe.
  paramètres : payload
- `get_dashboard_general_stats` — KPIs complets du tableau de bord général (CRM, marketing, commercial, facturation).
  paramètres : periode
- `get_dashboard_kpis` — Indicateurs clés du tableau de bord.
  paramètres : periode

## Divergences à traiter

- Divergence : « Champ adresse e-mail » (7.5s) ne correspond à aucun paramètre des outils MCP retenus — à décrire depuis la frame, pas depuis un schéma.
- Divergence : « Champ nouveau mot de passe » (23.0s) ne correspond à aucun paramètre des outils MCP retenus — à décrire depuis la frame, pas depuis un schéma.
- Divergence : « Champ de confirmation du mot de passe » (28.0s) ne correspond à aucun paramètre des outils MCP retenus — à décrire depuis la frame, pas depuis un schéma.
- Divergence : « Champ mot de passe de la page de connexion » (40.0s) ne correspond à aucun paramètre des outils MCP retenus — à décrire depuis la frame, pas depuis un schéma.

## Rappels de fond

- `a_quoi_ca_sert` : le bénéfice métier en deux phrases, **côté utilisateur**,
  pas côté logiciel.
- `prompt_claude` : une phrase qui fait la même chose que la démo, avec ses
  variables entre crochets et l'outil MCP visé.
- `erreurs_frequentes` : ce qui bloque réellement, observé ou documenté par un
  schéma (champ non modifiable après création, statut non transitionnable…).

Schéma complet : `src/schema/index.ts` → `FicheSchema`.
