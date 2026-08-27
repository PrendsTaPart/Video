# Fiche fonctionnelle — consigne de rédaction

## Règle absolue

Chaque affirmation doit être **traçable** : soit à une frame de l'enregistrement,
soit à un schéma d'outil MCP. Renseigne `sources` pour chaque bloc, par exemple
`{"champs_cles": "schéma create_facture", "a_quoi_ca_sert": "frame 00:12"}`.
Ce que tu ne peux pas vérifier va dans `a_verifier` — jamais dans une affirmation.

## Étapes observées à l'écran

- 1. Nommer l'entreprise (0.0s → 9.0s)
- 2. Renseigner l'e-mail de l'entreprise (9.0s → 18.0s)
- 3. Saisir le SIRET (18.0s → 26.0s)
- 4. Valider la création (26.0s → 28.5s)
- 5. Définir son mot de passe (28.5s → 35.0s)
- 6. Entrer dans son espace (35.0s → 51.1s)

## Outils MCP retenus

- `create_entreprise` — Créer une entreprise cliente (nom requis, coordonnées validées). Écriture — non utilisé par ce pipeline, mais son schéma fait foi sur les champs et leur caractère obligatoire.
  paramètres : nom*, email, siret, dirigeant, naf, adresse, code_postal, ville, telephone, site_web, domaine
- `list_entreprises` — Liste les entreprises enregistrées dans le C.R.M., avec nom, e-mail, SIRET, dirigeant et domaine. Lecture seule.
  paramètres : limit, q
- `rechercher_entreprise_siret` — Recherche une entreprise à partir de son numéro de SIRET. Lecture seule.
  paramètres : siret*
- `get_entreprise` — Fiche d'une entreprise par son identifiant. Lecture seule.
  paramètres : id*

## Divergences à traiter

- Divergence : « Champ e-mail de l'entreprise » (12.0s) ne correspond à aucun paramètre des outils MCP retenus — à décrire depuis la frame, pas depuis un schéma.
- Divergence : « Champs du nouveau mot de passe » (30.0s) ne correspond à aucun paramètre des outils MCP retenus — à décrire depuis la frame, pas depuis un schéma.

## Rappels de fond

- `a_quoi_ca_sert` : le bénéfice métier en deux phrases, **côté utilisateur**,
  pas côté logiciel.
- `prompt_claude` : une phrase qui fait la même chose que la démo, avec ses
  variables entre crochets et l'outil MCP visé.
- `erreurs_frequentes` : ce qui bloque réellement, observé ou documenté par un
  schéma (champ non modifiable après création, statut non transitionnable…).

Schéma complet : `src/schema/index.ts` → `FicheSchema`.
