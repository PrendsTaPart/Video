# Progression de la série des 157 tutoriels FoodEatUp

Source de vérité : **`src/data/tutorials.ts`** sur le projet Lovable FoodEatUp
Academy (`project_id: 55ff35b7-c442-42c4-950c-8c7fd420c645`), pas ce fichier —
qui n'est qu'un instantané pour le suivi côté dépôt vidéo. Le total de **157**
vient de la somme des `expectedCount` du tableau `modules` du même fichier
(14+20+8+7+4+6+5+3+3+24+20+30+10+3 = 157). Pour rafraîchir ce tableau : compter
les occurrences de `moduleSlug: "<slug>"` dans `tutorials.ts` (via
`mcp__Lovable__read_file`) et comparer à `expectedCount`.

## État au 2026-08-04

**71 / 157 publiés (45 %).**

| moduleSlug | Nom | Publiés | Attendus | Reste |
|---|---|---:|---:|---:|
| `equipe-planning` | Équipe, Planning & RH | 19 | 20 | 1 |
| `haccp` | Hygiène & HACCP | 16 | 30 | 14 |
| `configuration` | Configuration Boutique | 15 | 14 | ✅ dépassé (+1) |
| `comptabilite` | Comptabilité & Achats | 10 | 10 | ✅ complet |
| `stockvision-ai` | StockVision AI | 7 | 20 | 13 |
| `predibot` | PrediBot (Agent IA Directeur) | 2 | 3 | 1 |
| `hubrise-livraisons` | HubRise & Livraisons | 1 | 4 | 3 |
| `site-web-vitrine` | Site Web & Vitrine | 0 | 8 | 8 |
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

## Ajouté le 2026-08-07

- `pointer-son-service-cote-employe` — module `equipe-planning`, item 15
  "Pointer son Service (pauses & photo)". Comblait le dernier placeholder
  "à venir" du module (`equipe-planning` passe donc à 20/20, module complet
  sur ce dépôt — sous réserve de vérifier `tutorials.ts` en direct, plusieurs
  sessions publiant en parallèle). **Rush inexploitable** : le fichier envoyé
  pour ce dossier est le même fichier Drive mal étiqueté déjà documenté sur
  `creer-ses-roles-et-permissions` (montre Accueil/QR code/Rôles, pas le flux
  de pointage employé). Montage carte-based construit à la place à partir de
  la vraie capture produit `pointage.png` + un graphique illustratif pour le
  volet photo anti-fraude — voir `videos/foodeatup-pointer-service-tuto/SCRIPT.md`
  pour le détail et la marche à suivre si un vrai rush est fourni plus tard.
  RapidoCMS (vidéo + vignette) + Lovable mis à jour, GitHub poussé sur
  `claude/foodeatup-video-tutorials-x5a46z`. LinkedIn non demandé.

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
