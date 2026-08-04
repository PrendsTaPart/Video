# Suivi des vidéos tutoriels FoodEatUp — dépôt GitHub

Source de vérité : dossier Drive `1LpWivm0KEPwX5XhNHiw08426NjT6PXHC`, ré-audité le
2026-08-04 (le premier audit du 2026-08-02, dans `FAISABILITE-SERIE-TUTORIELS.md`, ne
portait que sur 5 des 10 modules aujourd'hui présents dans le Drive).

## Total vérifié aujourd'hui : 137 vidéos (pas encore 157)

5 nouveaux modules ont été ajoutés dans le Drive le 2026-08-03 (Mon Site, Marketing,
Service, KDS, Réservation), en plus des 5 modules déjà connus. Les 2 dossiers qui
manquaient dans le module 1 (Configuration) au 2026-08-02 ont aussi été comblés.

**Écart avec les 157 annoncés : 20 vidéos.** Non résolu — deux hypothèses posées dès le
2026-08-02 et toujours valables : nouveaux dossiers à venir, ou déclinaisons 9x16 hors de
cette arborescence. À confirmer avec Michael avant de considérer 157 comme la cible finale.

| # | Module | Dossiers Drive | Publiées | Restantes |
|---|---|---:|---:|---:|
| 1 | Configuration | 14 | 10 | 4 |
| 2 | Équipe & Planning | 20 | 0 | 20 |
| 3 | Comptabilité | 10 | 0 | 10 |
| 4 | HACCP | 30 | 1 | 29 |
| 5 | StockVision AI | 20 | 0 | 20 |
| 6 | Mon Site | 8 | 0 | 8 |
| 7 | Marketing | 24 | 0 | 24 |
| 8 | Service | 3 | 0 | 3 |
| 9 | KDS | 3 | 0 | 3 |
| 10 | Réservation | 5 | 0 | 5 |
| | **Total** | **137** | **11** | **126** |

## Publiées (11/137)

| # | Module | Sous-dossier Drive | Slug | Vidéo/vignette | claudePrompt |
|---|---|---|---|---|---|
| 1 | Configuration | 0 - Inscription, e-mail de confirmation | `creer-son-compte` | RapidoCMS | non |
| 2 | Configuration | 1 - monte votre boutique | `monter-sa-boutique` | RapidoCMS | non |
| 3 | Configuration | 2 - choisit votre abonnement | `choisir-son-abonnement` | RapidoCMS | non |
| 4 | Configuration | 3 - profil entreprise | `configurer-son-profil-entreprise` | RapidoCMS | non |
| 5 | Configuration | 4 - vos taux de TVA | `parametrer-sa-tva` | RapidoCMS | oui — `create_tva` |
| 6 | Configuration | 7 - vos catégories | `creer-ses-categories` | RapidoCMS | oui — `create_category` |
| 7 | Configuration | 5 - vos fournisseurs | `ajouter-ses-fournisseurs` | RapidoCMS | oui — `create_supplier` |
| 8 | Configuration | 9 - vos ingrédients | `saisir-ses-ingredients` | RapidoCMS | oui, 2 prompts |
| 9 | Configuration | 8 - vos unités | `regler-ses-unites` | RapidoCMS | non |
| 10 | Configuration | 10 - vos produits | `creer-ses-produits` | RapidoCMS | oui, 2 prompts |
| 11 | HACCP | 14 - Retrouver toutes vos production | `consulter-ses-productions-en-cours` | **GitHub raw** (voir note) | oui — `list_production_plans` |

## Note sur la publication de la vidéo #11 (2026-08-04)

Le connecteur RapidoCMS, utilisé pour héberger les vidéos/vignettes des 10 premiers
tutoriels (URLs S3 stables), **n'est pas installé pour cet espace de travail dans cette
session** (vérifié via la liste des connecteurs). La vidéo et la vignette de
`consulter-ses-productions-en-cours` sont donc servies depuis le dépôt GitHub
(`raw.githubusercontent.com`, branche `claude/foodeatup-video-tutorials-u4ljhv` — qui est
la branche par défaut de ce dépôt) plutôt que depuis RapidoCMS. Aucun draft LinkedIn
programmé pour cette vidéo (dépendait aussi de RapidoCMS pour l'upload). À corriger dès que
RapidoCMS est reconnecté : migrer `videoUrl`/`thumbnailUrl` vers RapidoCMS et programmer
le post LinkedIn en retard.

## Modules 6 à 10 : pas encore dans le modèle de données Lovable

`src/data/tutorials.ts` (voir `LOVABLE-FOODEATUP-DOCS.md`) ne connaît que les 5
`moduleSlug` d'origine (`configuration`, `equipe-planning`, `comptabilite`, `haccp`,
`stockvision-ai`). Les 5 nouveaux modules Drive (Mon Site, Marketing, Service, KDS,
Réservation, 43 vidéos) n'ont pas encore de `moduleSlug` ni de section sur le site — à
créer avec Michael avant de commencer à produire dans ces modules.
