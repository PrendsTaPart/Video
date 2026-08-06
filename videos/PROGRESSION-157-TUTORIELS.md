# Progression de la série des 157 tutoriels FoodEatUp

Source de vérité : **`src/data/tutorials.ts`** sur le projet Lovable FoodEatUp
Academy (`project_id: 55ff35b7-c442-42c4-950c-8c7fd420c645`), pas ce fichier —
qui n'est qu'un instantané pour le suivi côté dépôt vidéo. Le total de **157**
vient de la somme des `expectedCount` du tableau `modules` du même fichier
(14+20+8+7+4+6+5+3+3+24+20+30+10+3 = 157). Pour rafraîchir ce tableau : compter
les occurrences de `moduleSlug: "<slug>"` dans `tutorials.ts` (via
`mcp__Lovable__read_file`) et comparer à `expectedCount`.

## État au 2026-08-04 (table ci-dessous non recomptée depuis, voir note 2026-08-06 sur `site-web-vitrine`)

**71 / 157 publiés (45 %)** au 2026-08-04 ; +1 le 2026-08-06
(`commander-via-site-vocal-qrcode`) → **72 / 157 (46 %)**, mais ce total
reste indicatif tant que les autres modules n'ont pas été recomptés sur
`tutorials.ts` en direct (voir avertissement ci-dessus).

| moduleSlug | Nom | Publiés | Attendus | Reste |
|---|---|---:|---:|---:|
| `equipe-planning` | Équipe, Planning & RH | 19 | 20 | 1 |
| `haccp` | Hygiène & HACCP | 16 | 30 | 14 |
| `configuration` | Configuration Boutique | 15 | 14 | ✅ dépassé (+1) |
| `comptabilite` | Comptabilité & Achats | 10 | 10 | ✅ complet |
| `stockvision-ai` | StockVision AI | 7 | 20 | 13 |
| `predibot` | PrediBot (Agent IA Directeur) | 2 | 3 | 1 |
| `hubrise-livraisons` | HubRise & Livraisons | 1 | 4 | 3 |
| `site-web-vitrine` | Site Web & Vitrine | 9 | 9 | ✅ complet (dépassé, voir note 2026-08-06) |
| `caisse-pos` | Caisse POS & Matériel | 0 | 7 | 7 |
| `caroline-ia` | Agent IA Caroline | 0 | 6 | 6 |
| `reservation-salle` | Réservations & Plan de salle | 0 | 5 | 5 |
| `marketing-fidelite` | Marketing, Fidélité & Iris | 0 | 24 | 24 |
| `service-commande` | Service Multi-Canal | 0 | 3 | 3 |
| `kds-cuisine` | Écran Cuisine (KDS) | 0 | 3 | 3 |
| **Total** | | **71** | **157** | **86** |

`configuration` dépasse son `expectedCount` d'origine (15 publiés pour 14
attendus) — le chiffre attendu est une estimation de départ, pas un plafond ;
ne pas bloquer dessus.

## Ajoutés le 2026-08-06

- `commander-via-site-vocal-qrcode` — module `site-web-vitrine` (rush fourni
  par Michael : parcours de commande sur le site vitrine ; agent vocal et QR
  code à table introduits en VO + carte dédiée, non filmables). Prompts
  Claude `list_orders` filtré par `channel` (vitrine/agent_vocal/sur_place).
  9ème tutoriel du module (`expectedCount` du module passé de 8 à 9 sur
  Lovable — ce constat a aussi révélé que le module `site-web-vitrine`,
  encore à 0 dans ce tableau, était en réalité déjà à 8/8 sur le site réel
  avant cet ajout : ce tableau local a pris du retard sur `tutorials.ts`,
  comme documenté pour d'autres modules — ne pas s'y fier seul pour planifier
  la suite, vérifier `tutorials.ts` en direct).
- `placer-un-client-a-table` — module `reservation-salle` (rush fourni par
  Michael : check-in d'une réservation + réassignation de table via
  Modifier). Prompt Claude `checkin_reservation`, correspondance exacte.
  Complète une fiche placeholder déjà présente sur le site ("en cours de
  tournage", `order: 4`) — pas de nouvelle entrée créée, `expectedCount` du
  module inchangé.

## Ajoutés cette session (2026-08-04)

- `tenir-sa-liste-de-courses` — module `stockvision-ai` (add/edit/delete sur la
  liste de courses, prompt Claude `create_supplier_order`).
- `creer-sa-fiche-plat-pour-production` — module `haccp` (créer un plat +
  ingrédients + date/quantité de production, prompts Claude `create_recipe` +
  `create_production_plan`).

## Modules à zéro tutoriel — prioriser si on veut couvrir toute la série

`site-web-vitrine`, `caisse-pos`, `caroline-ia`, `reservation-salle`,
`marketing-fidelite` (le plus gros, 24 attendus), `service-commande`,
`kds-cuisine`. Vérifier dans `references/mcp-plugins-video-catalog.md` et les
outils `mcp__FoodEatUp__*` quels cas d'usage de ces modules ont un outil MCP
correspondant, pour préparer scripts + `claudePrompt(s)` en amont du prochain
rush fourni par Michael.
