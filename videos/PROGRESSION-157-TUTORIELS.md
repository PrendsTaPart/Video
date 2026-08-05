# Progression de la série des 157 tutoriels FoodEatUp

Source de vérité : **`src/data/tutorials.ts`** sur le projet Lovable FoodEatUp
Academy (`project_id: 55ff35b7-c442-42c4-950c-8c7fd420c645`), pas ce fichier —
qui n'est qu'un instantané pour le suivi côté dépôt vidéo. Le total de **157**
vient de la somme des `expectedCount` du tableau `modules` du même fichier
(14+20+8+7+4+6+5+3+3+24+20+30+10+3 = 157). Pour rafraîchir ce tableau : compter
les occurrences de `moduleSlug: "<slug>"` dans `tutorials.ts` (via
`mcp__Lovable__read_file`) et comparer à `expectedCount`.

## État au 2026-08-04

**79 / 157 publiés (50 %)** — `marketing-fidelite` recompté en direct sur
`tutorials.ts` le 2026-08-05 (8 `videoUrl` non vides sur 24), n'apparaissait qu'en
doublon obsolète (0/24) dans ce tableau jusqu'ici : le saut de 72→79 vient de
cette correction de ligne, pas d'un rythme de production soudain — voir
avertissement plus haut.

| moduleSlug | Nom | Publiés | Attendus | Reste |
|---|---|---:|---:|---:|
| `equipe-planning` | Équipe, Planning & RH | 19 | 20 | 1 |
| `haccp` | Hygiène & HACCP | 17 | 30 | 13 |
| `marketing-fidelite` | Marketing, Fidélité & Iris | 8 | 24 | 16 |
| `configuration` | Configuration Boutique | 15 | 14 | ✅ dépassé (+1) |
| `comptabilite` | Comptabilité & Achats | 10 | 10 | ✅ complet |
| `stockvision-ai` | StockVision AI | 7 | 20 | 13 |
| `predibot` | PrediBot (Agent IA Directeur) | 2 | 3 | 1 |
| `hubrise-livraisons` | HubRise & Livraisons | 1 | 4 | 3 |
| `site-web-vitrine` | Site Web & Vitrine | 0 | 8 | 8 |
| `caisse-pos` | Caisse POS & Matériel | 0 | 7 | 7 |
| `caroline-ia` | Agent IA Caroline | 0 | 6 | 6 |
| `reservation-salle` | Réservations & Plan de salle | 0 | 5 | 5 |
| `service-commande` | Service Multi-Canal | 0 | 3 | 3 |
| `kds-cuisine` | Écran Cuisine (KDS) | 0 | 3 | 3 |
| **Total** | | **79** | **157** | **78** |

`configuration` dépasse son `expectedCount` d'origine (15 publiés pour 14
attendus) — le chiffre attendu est une estimation de départ, pas un plafond ;
ne pas bloquer dessus.

## Ajoutés cette session (2026-08-04)

- `tenir-sa-liste-de-courses` — module `stockvision-ai` (add/edit/delete sur la
  liste de courses, prompt Claude `create_supplier_order`).
- `creer-sa-fiche-plat-pour-production` — module `haccp` (créer un plat +
  ingrédients + date/quantité de production, prompts Claude `create_recipe` +
  `create_production_plan`).

## Ajoutés cette session (2026-08-05)

- `archiver-ses-documents-de-nettoyage` — module `haccp` (upload/aperçu/
  renommage d'un document dans le dossier HACCP > Documents > Nettoyage et
  désinfection, pas de `claudePrompt` — aucun outil MCP correspondant).
- `resultats-des-sondages-historique` — module `marketing-fidelite` (partage
  du lien sondage, réponse client, consultation des résultats agrégés,
  `claudePrompt` sur `get_survey_results`).

## Modules à zéro tutoriel — prioriser si on veut couvrir toute la série

`site-web-vitrine`, `caisse-pos`, `caroline-ia`, `reservation-salle`,
`marketing-fidelite` (le plus gros, 24 attendus), `service-commande`,
`kds-cuisine`. Vérifier dans `references/mcp-plugins-video-catalog.md` et les
outils `mcp__FoodEatUp__*` quels cas d'usage de ces modules ont un outil MCP
correspondant, pour préparer scripts + `claudePrompt(s)` en amont du prochain
rush fourni par Michael.
