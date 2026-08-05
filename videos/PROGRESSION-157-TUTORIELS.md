# Progression de la série des 157 tutoriels FoodEatUp

Source de vérité : **`src/data/tutorials.ts`** sur le projet Lovable FoodEatUp
Academy (`project_id: 55ff35b7-c442-42c4-950c-8c7fd420c645`), pas ce fichier —
qui n'est qu'un instantané pour le suivi côté dépôt vidéo. Le total de **157**
vient de la somme des `expectedCount` du tableau `modules` du même fichier
(14+20+8+7+4+6+5+3+3+24+20+30+10+3 = 157). Pour rafraîchir ce tableau : compter
les occurrences de `moduleSlug: "<slug>"` dans `tutorials.ts` (via
`mcp__Lovable__read_file`) et comparer à `expectedCount`.

## État au 2026-08-05 (recompté en direct sur `src/data/tutorials.ts`)

**111 / 157 publiés (71 %)** — `videoUrl` non vide, compté via `mcp__Lovable__read_file`
+ script Python (regex par bloc `moduleSlug`/`videoUrl`), pas via ce tableau qui datait
du 2026-08-04 et annonçait 71/157. **Écart de +40 en une journée sans que ce dépôt ait
produit 40 vidéos** : confirme la fragmentation déjà documentée plus bas — plusieurs
sessions publient en parallèle sur ce même projet Lovable. Le compteur d'accueil du site
est même passé de 106 à 110 pendant la publication d'un seul tutoriel par cette session
(voir `LOVABLE-FOODEATUP-DOCS.md`, entrée `ciblage-et-consentement-clients`).

| moduleSlug | Nom | Publiés | Entrées (stubs inclus) | Attendus | Reste |
|---|---|---:|---:|---:|---:|
| `configuration` | Configuration Boutique | 15 | 15 | 14 | ✅ dépassé (+1) |
| `equipe-planning` | Équipe, Planning & RH | 20 | 21 | 20 | ✅ dépassé (+1 entrée, 20 publiées) |
| `haccp` | Hygiène & HACCP | 28 | 30 | 30 | 2 |
| `stockvision-ai` | StockVision AI | 19 | 19 | 20 | 1 |
| `comptabilite` | Comptabilité & Achats | 8 | 10 | 10 | 2 |
| `predibot` | PrediBot (Agent IA Directeur) | 5 | 7 | 3 | ✅ dépassé (entrées > attendu d'origine) |
| `marketing-fidelite` | Marketing, Fidélité & Iris | 10 | 24 | 24 | 14 |
| `site-web-vitrine` | Site Web & Vitrine | 6 | 8 | 8 | 2 |
| `service-commande` | Service Multi-Canal | 1 | 3 | 3 | 2 |
| `hubrise-livraisons` | HubRise & Livraisons | 0 | 4 | 4 | 4 |
| `caisse-pos` | Caisse POS & Matériel | 0 | 7 | 7 | 7 |
| `caroline-ia` | Agent IA Caroline | 0 | 6 | 6 | 6 |
| `reservation-salle` | Réservations & Plan de salle | 0 | 5 | 5 | 5 |
| `kds-cuisine` | Écran Cuisine (KDS) | 0 | 3 | 3 | 3 |
| **Total** | | **112** (instantané 2026-08-05 après-midi, avant d'autres publications concurrentes) | **162** | **157** | — |

Le total "Entrées" (162) dépasse 157 car plusieurs modules ont désormais plus de stubs
que leur `expectedCount` d'origine (estimation de départ, pas un plafond — voir note
existante sur `configuration`) : ne pas bloquer dessus, seul `videoUrl` non vide compte
comme "publié".

## Ajoutée cette session (2026-08-05)

- `ciblage-et-consentement-clients` — module `marketing-fidelite`, **première vidéo
  publiée de ce module** (9 y sont maintenant, sur 24 stubs). Remplit une fiche stub
  préexistante (`order: 9`) plutôt que d'en créer une nouvelle. Prompts Claude
  `list_rfm_segments` (consultation segments RFM) + `create_campaign` (`claudePrompts[]`).
  Détail complet : `LOVABLE-FOODEATUP-DOCS.md` (tableau "Tutoriels publiés") et
  `videos/foodeatup-ciblage-consentement-tuto/SCRIPT.md`.
- `suivre-ses-credits-sms-whatsapp` — module `marketing-fidelite` (10/24 sur ce module
  après celle-ci). Remplit une autre fiche stub préexistante. Pas de `claudePrompt` :
  aucun outil MCP ne lit le solde de crédits/quotas. Détail complet :
  `LOVABLE-FOODEATUP-DOCS.md` et `videos/foodeatup-credits-com-tuto/SCRIPT.md`.

## Ajoutés session précédente (2026-08-04)

- `tenir-sa-liste-de-courses` — module `stockvision-ai` (add/edit/delete sur la
  liste de courses, prompt Claude `create_supplier_order`).
- `creer-sa-fiche-plat-pour-production` — module `haccp` (créer un plat +
  ingrédients + date/quantité de production, prompts Claude `create_recipe` +
  `create_production_plan`).

## Modules encore à zéro tutoriel publié

`hubrise-livraisons`, `caisse-pos`, `caroline-ia`, `reservation-salle`, `kds-cuisine`.
`marketing-fidelite` a désormais son premier tutoriel (`ciblage-et-consentement-clients`)
mais reste très ouvert (9/24). Vérifier dans `references/mcp-plugins-video-catalog.md` et
les outils `mcp__Foodeatup__*` quels cas d'usage de ces modules ont un outil MCP
correspondant, pour préparer scripts + `claudePrompt(s)` en amont du prochain rush fourni
par Michael. **Avant de choisir un sujet dans l'un de ces modules, relire
`src/data/tutorials.ts` en direct** (fragmentation active, ce tableau peut déjà être
dépassé au moment où il est lu).
