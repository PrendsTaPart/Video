# Suivi de la série — 157 tutoriels

**À relire à chaque nouvelle vidéo produite**, en parallèle du tableau "Tutoriels publiés"
de `LOVABLE-FOODEATUP-DOCS.md`.

## Le chiffre 157 — résolu (2026-08-04)

Le total communiqué par Michael (157) est **exact et vérifiable directement dans le code
du site Lovable** : `src/data/tutorials.ts` (projet `foodeatup-guide-star`,
`55ff35b7-c442-42c4-950c-8c7fd420c645`) définit 14 modules avec un champ `expectedCount`
chacun, dont la somme fait **157 pile** :

| moduleSlug | Nom | Catégorie | expectedCount |
|---|---|---|---:|
| `configuration` | Configuration Boutique | Configuration Boutique | 14 |
| `equipe-planning` | Équipe, Planning & RH | Équipe, Planning & RH | 20 |
| `site-web-vitrine` | Site Web & Vitrine | Site Web & Vitrine | 8 |
| `caisse-pos` | Caisse POS & Matériel | Caisse POS & Matériel | 7 |
| `hubrise-livraisons` | HubRise & Livraisons | HubRise & Livraisons | 4 |
| `caroline-ia` | Agent IA Caroline | Agent IA Caroline & Salle | 6 |
| `reservation-salle` | Réservations & Plan de salle | Agent IA Caroline & Salle | 5 |
| `service-commande` | Service Multi-Canal | Flux de Service & KDS | 3 |
| `kds-cuisine` | Écran Cuisine (KDS) | Flux de Service & KDS | 3 |
| `marketing-fidelite` | Marketing, Fidélité & Iris | Marketing, Fidélité & Iris | 24 |
| `stockvision-ai` | StockVision AI | StockVision AI | 20 |
| `haccp` | Hygiène & HACCP | Hygiène & HACCP | 30 |
| `comptabilite` | Comptabilité & Achats | Comptabilité & PrediBot | 10 |
| `predibot` | PrediBot (Agent IA Directeur) | Comptabilité & PrediBot | 3 |
| | | **Total** | **157** |

Ce périmètre est **beaucoup plus large** que l'audit Drive du 2026-08-02
(`FAISABILITE-SERIE-TUTORIELS.md`, 92 dossiers / 5 modules) : 9 modules supplémentaires
(site-web-vitrine, caisse-pos, hubrise-livraisons, caroline-ia, reservation-salle,
service-commande, kds-cuisine, marketing-fidelite, predibot) ont été ajoutés au périmètre
depuis, sans que ce dépôt git en ait gardé la trace (aucun sous-dossier Drive audité pour
eux à ce jour dans ce checkout).

## ⚠️ Constat important : le suivi local de ce dépôt est en retard sur l'état réel

En lisant `src/data/tutorials.ts` en direct le 2026-08-04, **74 tutoriels étaient déjà
publiés sur le site avant même l'ajout de celui de cette session** (traçabilité complète
HACCP) — très loin des 10 listées dans le tableau "Tutoriels publiés" de
`LOVABLE-FOODEATUP-DOCS.md`, et le planning LinkedIn (`list_scheduled_posts`) est rempli
2 posts/jour jusqu'au 2026-08-25 sur des dizaines de sujets qui ne sont pas non plus dans
ce dépôt git. Autrement dit : **d'autres sessions/instances ont produit et publié un
volume important de vidéos directement sur Lovable/RapidoCMS sans que le travail ne soit
resynchronisé dans ce dépôt** (pas de `SCRIPT.md`, pas de dossier `videos/foodeatup-*`
correspondant pour la plupart).

**Recommandation** : pour connaître l'avancement réel à un instant T, interroger
`src/data/tutorials.ts` du projet Lovable (source de vérité vivante) plutôt que le tableau
de ce dépôt, qui ne reflète que les vidéos produites *via ce dépôt git*. Idéalement,
resynchroniser ce dépôt (au moins les `SCRIPT.md`) avec ce qui existe déjà côté Lovable,
pour que les prochaines sessions ne redécouvrent pas cet écart.

## Avancement réel (mesuré le 2026-08-04)

| Statut | Nombre | Détail |
|---|---:|---|
| Déjà sur Lovable avant cette session | 74 | Comptés via `grep -c howItWorks: src/data/tutorials.ts` — répartition par module non entièrement vérifiée (`moduleSlug` compte 73/74, à 1 près) |
| Ajoutée par cette session (HACCP) | 1 | `creer-une-tracabilite-complete` — RapidoCMS + Lovable faits ; LinkedIn **pas encore programmé** (voir ci-dessous) |
| **Total publié (Lovable)** | **75** | |
| **Restant sur les 157** | **82** | Pas de détail par module fiable pour l'instant — nécessiterait de compter `moduleSlug` précisément dans `tutorials.ts` |

## LinkedIn — non traité pour cette vidéo

Le compte LinkedIn `FoodEatUp` (id 27, `account_id 68807312`) a un planning **déjà rempli
par ailleurs jusqu'au 2026-08-25** (2 créneaux/jour, 7h et 16h) avec des sujets qui ne
sont pas dans ce dépôt — signe d'une production concurrente active sur ce même compte. Un
doublon de créneau a même été repéré (2026-08-16 07:00, deux `job_id` différents). Plutôt
que de risquer un conflit d'écriture sur ce planning partagé, la vidéo traçabilité
complète n'a **pas** été programmée sur LinkedIn — à faire une fois un créneau confirmé
sans collision (au-delà du 2026-08-25, ou en coordination avec qui gère cette rotation).

## Prochaine action

1. Si possible, demander confirmation que `src/data/tutorials.ts` + le planning LinkedIn
   du compte FoodEatUp sont bien la source de vérité à jour (et savoir qui d'autre y
   publie en parallèle, pour éviter les collisions comme celle du 2026-08-16).
2. Resynchroniser ce dépôt : soit en ajoutant les `SCRIPT.md` manquants pour les 74
   vidéos déjà publiées mais absentes d'ici, soit en documentant explicitement que ce
   dépôt ne couvre qu'une partie de la production.
