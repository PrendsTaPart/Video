# Progression de la série des 157 tutoriels FoodEatUp

Source de vérité : **`src/data/tutorials.ts`** sur le projet Lovable FoodEatUp
Academy (`project_id: 55ff35b7-c442-42c4-950c-8c7fd420c645`), pas ce fichier —
qui n'est qu'un instantané pour le suivi côté dépôt vidéo. Le total de **157**
vient de la somme des `expectedCount` du tableau `modules` du même fichier
(14+20+8+7+4+6+5+3+3+24+20+30+10+3 = 157). Pour rafraîchir ce tableau : compter
les occurrences de `moduleSlug: "<slug>"` dans `tutorials.ts` (via
`mcp__Lovable__read_file`) et comparer à `expectedCount`.

## État au 2026-08-05

**73 / 157 publiés (46 %).** (Le compteur homepage Lovable affiche 123/157 —
écart déjà documenté ailleurs, voir `LOVABLE-FOODEATUP-DOCS.md` : d'autres
branches/sessions publient en parallèle sans que ce fichier de suivi local
en ait toujours trace. Ce tableau ne couvre que ce qui a été produit *depuis
ce dépôt*.)

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
| `marketing-fidelite` | Marketing, Fidélité & Iris | 1 | 24 | 23 |
| `caisse-pos` | Caisse POS & Matériel | 0 | 7 | 7 |
| `caroline-ia` | Agent IA Caroline | 0 | 6 | 6 |
| `reservation-salle` | Réservations & Plan de salle | 0 | 5 | 5 |
| `service-commande` | Service Multi-Canal | 0 | 3 | 3 |
| `kds-cuisine` | Écran Cuisine (KDS) | 0 | 3 | 3 |
| **Total** | | **73** | **157** | **84** |

`configuration` dépasse son `expectedCount` d'origine (15 publiés pour 14
attendus) — le chiffre attendu est une estimation de départ, pas un plafond ;
ne pas bloquer dessus.

## Ajoutés cette session (2026-08-05)

- `connecter-son-domaine` — module `site-web-vitrine` (premier tutoriel du
  module : saisie du domaine, clic Connecter, copie de l'enregistrement
  CNAME, clic Vérifier maintenant ; prompt Claude `get_domain_status`). Rush
  et cartes intro/outro fournis par Michael. Voir
  `videos/foodeatup-domaine-tuto/SCRIPT.md`.
- `debloquer-les-avis-clients` — module `marketing-fidelite` (premier
  tutoriel du plus gros module du catalogue : achat/activation de l'option
  "Avis & réputation Google" à 29€/mois via paiement Stripe ; pas de prompt
  Claude, achat d'abonnement = aucun outil MCP correspondant, même cas que
  `choisir-son-abonnement`). Rush et cartes intro/outro fournis par Michael.
  Voir `videos/foodeatup-avis-abonnement-tuto/SCRIPT.md`.

## Ajoutés session précédente (2026-08-04)

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
