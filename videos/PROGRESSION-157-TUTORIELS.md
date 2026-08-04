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
| `site-web-vitrine` | Site Web & Vitrine | 1 | 8 | 7 |
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

## Ajoutés cette session (2026-08-04)

- `tenir-sa-liste-de-courses` — module `stockvision-ai` (add/edit/delete sur la
  liste de courses, prompt Claude `create_supplier_order`).
- `creer-sa-fiche-plat-pour-production` — module `haccp` (créer un plat +
  ingrédients + date/quantité de production, prompts Claude `create_recipe` +
  `create_production_plan`).
- `choisir-son-template` — module `site-web-vitrine` (1ère vidéo du module ;
  remplit la fiche placeholder déjà en place, pas une nouvelle entrée créée).
  Bibliothèque de templates > filtre par catégorie > Aperçu grandeur nature >
  Utiliser > confirmation (sauvegarde auto), prompt Claude
  `apply_site_template`. Dossier `videos/foodeatup-choisir-template-tuto/`.
  `videoUrl`/`thumbnailUrl` pointent temporairement sur le raw GitHub de la
  branche `claude/foodeatup-video-tutorial-8ddbi5` (connecteur RapidoCMS
  indisponible dans cette session) — à remplacer par les URLs S3 RapidoCMS dès
  que le connecteur est disponible.
  ⚠️ Ce tableau (71/157) est déjà en retard sur le site Lovable réel (86/157
  au moment de cette édition, voir avertissement en tête de fichier) — le
  compteur `site-web-vitrine` ci-dessus est corrigé (0→1) mais le total
  général n'a pas été recalculé pour éviter d'écraser les ajouts d'autres
  sessions concurrentes ; se fier à `tutorials.ts` pour le vrai total.

## Modules à zéro tutoriel — prioriser si on veut couvrir toute la série

`caisse-pos`, `caroline-ia`, `reservation-salle`, `marketing-fidelite` (le
plus gros, 24 attendus), `service-commande`, `kds-cuisine`. `site-web-vitrine`
a maintenant sa première vidéo (`choisir-son-template`), reste 7. Vérifier
dans `references/mcp-plugins-video-catalog.md` et les outils
`mcp__FoodEatUp__*` quels cas d'usage de ces modules ont un outil MCP
correspondant, pour préparer scripts + `claudePrompt(s)` en amont du prochain
rush fourni par Michael.
