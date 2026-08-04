# Tutoriel — Suivre ses performances, côté employé (module Équipe & Planning)

Quinzième vidéo du module `equipe-planning` (catalogue #18). Durée
livrée : **36,84 s** — H.264 High/yuv420p, AAC LC 48 kHz stéréo, faststart
(moov avant mdat confirmé). Audio : max **-7,3 dBFS** / mean -21,6 dBFS.
Decode 0 erreur.

## Ce que montre le rush

Le rush (18,4 s, capture Chrome 1920x1020 @60fps — chrome navigateur rogné,
canevas final 1920x828) montre l'espace employé : "Mon planning" (bref) →
menu avatar (Mes modules, Dashboard, Planning, Congés, **Performances**,
Profil, Déconnexion) → clic "Performances" → tableau de bord : score global
en anneau (131, "À améliorer") avec légende Excellent/Moyen/À améliorer →
"Classement de l'équipe" (3 employés avec score et taux de présence) + "Rang
1/15" + "Moyenne d'équipe : 103" → "Historique des performances" (barres
Semaine 1 à 5).

## Voix off (6 lignes, voix Adam FR `TGAegA0zNRi8I6nUdq3i`)

| # | Texte | Durée | Segment |
|---|---|---:|---|
| N0 | Comment suivre ses performances au quotidien, côté employé ? Voici son tableau de bord personnel. | 5,46 s | intro |
| N1 | Depuis le menu de son profil, l'employé accède directement à ses performances. | 4,26 s | A/B — menu avatar |
| N2 | Un score global et un indicateur, excellent, moyen, ou à améliorer, résument sa performance récente. | 6,53 s | C — score en anneau |
| N3 | Il retrouve aussi son classement dans l'équipe, avec le score et le taux de présence de chacun. | 4,96 s | D — classement de l'équipe |
| N4 | Un historique semaine par semaine permet de suivre sa progression dans le temps. | 4,08 s | E — historique des performances |
| N5 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (CTA, réutilisé tel quel depuis `foodeatup-borne-tuto`) |

N5 réutilisé tel quel (texte générique identique aux tutos précédents) —
zéro crédit ElevenLabs dépensé sur cette ligne.

## Découpage

Segments dimensionnés à partir des durées VO réellement mesurées. Première
tentative avec une dérive de 0,51 à 0,62 s sur N2-N4 (segments A/C/D un peu
trop courts) — corrigé en un seul passage → **dérive nulle**.

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 6,00 s | SUIVRE SES PERFORMANCES CÔTÉ EMPLOYÉ |
| A | 0,20 → 1,50 | 4,20 s | "Mon planning" (aperçu bref) |
| B | 3,60 → 3,90 | 0,90 s | **zoom-punch** sur "Performances" (menu avatar) |
| C | 6,00 → 7,50 | 7,70 s | score en anneau, légende |
| D | 8,00 → 10,00 | 6,10 s | classement de l'équipe, rang |
| E | 11,00 → 14,00 | 4,50 s | historique des performances |
| F | 16,00 → 18,40 | 3,00 s | retour en haut de page |
| outro | carte | 6,20 s | CTA |

Transitions : `fade` sur tous les enchaînements (rush court, essentiellement
continu — pas de coupure de contexte franche hormis l'ouverture du menu
avatar).

## Pas de séquence "Utiliser avec Claude"

Aucun outil `mcp__FoodEatUp__*` ne calcule ni n'expose ce score de
performance employé (ring, classement d'équipe, historique) : c'est une
métrique interne au produit, pas un endpoint API exposé. Même raisonnement
que les autres tutos côté employé de cette série (`foodeatup-borne-tuto`,
`foodeatup-conge-employe-tuto`, `foodeatup-documents-tuto`). Pas de prompt
inventé ; section absente à la fois de la vidéo et de la fiche Lovable
(`claudePrompt` non renseigné).

## Animations

Mêmes principes que toute la série : Ken Burns sur les cartes, xfade
(0,28 s), bandeaux d'étape, encadré orange pulsant sur le clic ("Performances"
dans le menu avatar). Pas de mini-animation dédiée : le rush illustre déjà
nativement le tableau de bord (score, classement, historique).

## Statut publication

Montage terminé et checklist de compatibilité passée (H.264 High/yuv420p,
AAC 48 kHz stéréo, faststart, peak -7,3 dBFS, 0 erreur de décodage). Vidéo
et vignette hébergées via URL GitHub raw sur la branche
`claude/foodeatup-tutorial-video-vn7udf`. Lovable : tutoriel
`suivre-ses-performances-cote-employe` à ajouter dans `src/data/tutorials.ts`
(module `equipe-planning`, subcategory "18 - suivre ses performances côté
employé"), avec `chefTip` mais sans `claudePrompt`.

## Note sur la vidéo #15

Le fichier fourni pour "Pointer son Service (pauses & photo)" fait
exactement la même taille en octets (31 001 599) que le rush déjà utilisé
pour `foodeatup-accueil-role-tuto` (#14), et une frame extraite confirme
qu'il s'agit bien du même contenu (grille de modules "Mon espace"), pas des
pauses/pointage entrée-sortie. Vidéo non montée dans cette session — en
attente du bon fichier.
