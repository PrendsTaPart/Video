# Fiche fonctionnelle — consigne de rédaction

## Règle absolue

Chaque affirmation doit être **traçable** : soit à une frame de l'enregistrement,
soit à un schéma d'outil MCP. Renseigne `sources` pour chaque bloc, par exemple
`{"champs_cles": "schéma create_facture", "a_quoi_ca_sert": "frame 00:12"}`.
Ce que tu ne peux pas vérifier va dans `a_verifier` — jamais dans une affirmation.

## Étapes observées à l'écran

- 1. Ouvrir sa fiche profil (0.0s → 10.0s)
- 2. Renseigner son identité (10.0s → 17.0s)
- 3. Ajouter numéro et adresse (17.0s → 24.0s)
- 4. Sauvegarder (24.0s → 28.0s)
- 5. Compléter la fiche entreprise (28.0s → 44.0s)
- 6. Adresse et couleur des factures (44.0s → 63.0s)

## Outils MCP retenus

- `get_profile` — Profil : renvoie les informations de profil de l'utilisateur connecté. Lecture seule.
  paramètres : (aucun)
- `get_company` — Entreprise : renvoie les informations de la société émettrice (nom, SIRET, adresse, coordonnées). Lecture seule.
  paramètres : (aucun)
- `update_commercial_profil` — Met à jour le profil d'un commercial. Écriture — non utilisé par ce pipeline.
  paramètres : id*, payload
- `get_user` — Utilisateurs : fiche d'un utilisateur par son identifiant. Lecture seule. N'expose aucun mot de passe.
  paramètres : id*
- `update_entreprise` — Met à jour une entreprise cliente. Écriture — non utilisé par ce pipeline. Son schéma renseigne les champs d'une fiche entreprise.
  paramètres : nom, email, siret, adresse, code_postal, ville, telephone, site_web

## Divergences à traiter

- Divergence : « Champ e-mail » (14.0s) ne correspond à aucun paramètre des outils MCP retenus — à décrire depuis la frame, pas depuis un schéma.
- Divergence : « Champ numéro » (17.0s) ne correspond à aucun paramètre des outils MCP retenus — à décrire depuis la frame, pas depuis un schéma.
- Divergence : « Sélecteur de couleur de la charte des factures » (58.0s) ne correspond à aucun paramètre des outils MCP retenus — à décrire depuis la frame, pas depuis un schéma.

## Rappels de fond

- `a_quoi_ca_sert` : le bénéfice métier en deux phrases, **côté utilisateur**,
  pas côté logiciel.
- `prompt_claude` : une phrase qui fait la même chose que la démo, avec ses
  variables entre crochets et l'outil MCP visé.
- `erreurs_frequentes` : ce qui bloque réellement, observé ou documenté par un
  schéma (champ non modifiable après création, statut non transitionnable…).

Schéma complet : `src/schema/index.ts` → `FicheSchema`.
