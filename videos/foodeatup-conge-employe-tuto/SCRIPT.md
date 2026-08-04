# Tutoriel — Poser un congé et une absence, côté employé (module Équipe & Planning)

Onzième vidéo du module `equipe-planning` (catalogue #17 — voir
`CATALOGUE-157-TUTORIELS.md`). Durée livrée : **58,92 s** — H.264 High/yuv420p,
AAC LC 48 kHz stéréo, faststart (moov avant mdat confirmé). Audio : max
**-7,2 dBFS** / mean -21,2 dBFS. Decode 0 erreur.

## Ce que montre le rush

Le rush (34,28 s, capture Chrome 1920x1020 @60fps — chrome navigateur rogné,
canevas final 1920x828) montre la page employé des congés
(`foodeatup.com/employee/26/leaves`) : tableau de bord "Bonjour, soulayma !"
avec le solde de congés (acquis, soldé, pris, en attente) → une demande
"Congés payés" déjà en attente de vérification → clic sur "Ajouter une
absence" → modale "Demande d'absence" : choix du type (Congé personnel),
description optionnelle, unité (Heures / Demi-journées / Jours), dates de
début et de fin, pièce jointe optionnelle → clic sur "Enregistrer" → la
nouvelle demande apparaît aussitôt en tête de la liste "en attente de
vérification", avec le badge "En attente" dans les dernières demandes.

## Voix off (8 lignes, voix Adam FR `TGAegA0zNRi8I6nUdq3i`)

| # | Texte | Durée | Segment |
|---|---|---:|---|
| N0 | Besoin de poser un congé ou une absence ? Voici comment faire, côté employé, en toute autonomie. | 5,85 s | intro |
| N1 | Chaque employé retrouve, dans son espace personnel, son solde de congés : jours acquis, soldés, pris, et en attente de validation. | 7,71 s | A — tableau de bord, solde de congés |
| N2 | Les demandes déjà envoyées restent visibles ici, avec leur statut, en attente ou validées par l'employeur. | 6,30 s | B — demande "Congés payés" en attente |
| N3 | Un clic sur Ajouter une absence, et l'employé choisit le type d'absence : congé payé, congé personnel, ou autre. | 7,05 s | D — modale "Demande d'absence" |
| N4 | Il précise ensuite s'il compte en heures, en demi-journées ou en jours complets, et peut ajouter une description à sa demande. | 6,92 s | F — "Congé personnel" sélectionné, "Jours" |
| N5 | Il choisit sa date de début et sa date de fin, et peut joindre un justificatif si besoin, au format PDF, JPG ou PNG. | 8,36 s | G — dates de début/fin, pièce jointe |
| N6 | La demande part aussitôt en attente de validation, et son solde de congés se met à jour automatiquement dès qu'elle est approuvée. | 6,87 s | I — nouvelle demande "en attente" |
| N7 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (CTA, réutilisé tel quel depuis `foodeatup-borne-tuto`) |

N7 réutilisé tel quel (texte générique identique aux tutos précédents) —
zéro crédit ElevenLabs dépensé sur cette ligne.

## Découpage

Segments dimensionnés directement à partir des durées VO réellement mesurées
(leçon appliquée dès le premier montage cette fois, après les dérives
rencontrées sur `foodeatup-borne-tuto` et `foodeatup-accueil-role-tuto`) :
première tentative à 0,31–0,92 s de dérive sur N2/N3/N4/N5/N6/N7 (grâce au
calcul préalable, déjà bien plus faible que les tentatives précédentes),
deux ajustements ciblés (segments A, D, F, G, I légèrement élargis) ont
suffi pour converger à **dérive nulle**.

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 6,50 s | POSER UN CONGÉ CÔTÉ EMPLOYÉ |
| A | 0,20 → 1,80 | 8,50 s | tableau de bord, solde de congés |
| B | 2,30 → 4,80 | 6,45 s | demande "Congés payés" déjà en attente |
| C | 5,00 → 5,30 | 0,90 s | **zoom-punch** sur "Ajouter une absence" |
| D | 6,60 → 9,60 | 7,00 s | modale "Demande d'absence" |
| E | 9,85 → 10,15 | 0,90 s | **zoom-punch** sur "Sélectionner le type" |
| F | 11,00 → 14,50 | 8,20 s | "Congé personnel", unité "Jours" |
| G | 18,00 → 24,50 | 8,30 s | dates de début/fin, pièce jointe |
| H | 24,70 → 25,00 | 0,90 s | **zoom-punch** sur "Enregistrer" |
| I | 26,00 → 30,50 | 7,50 s | nouvelle demande "en attente", solde mis à jour |
| outro | carte | 6,20 s | CTA |

Transitions : `fade` sur les enchaînements continus (intro→A, A→B, C→D, E→F,
F→G, I→outro), `slideleft` sur les coupures de contexte (B→C, D→E, G→H,
H→I).

## Pas de séquence "Utiliser avec Claude"

Aucun outil `mcp__FoodEatUp__*` ne couvre la création d'une demande de congé
côté employé : `approve_leave`, `reject_leave` et `list_leaves` sont tous des
actions côté manager (validation/consultation), il n'existe pas de
`create_leave`/`request_leave` pour l'auto-saisie d'un employé. Même
raisonnement que `foodeatup-borne-tuto` (appairage PIN) et
`foodeatup-jarvis-tuto` (scan QR) : une action de self-service employé, pas
un geste d'administration côté API. Pas de prompt inventé ; section absente à
la fois de la vidéo et de la fiche Lovable (`claudePrompt` non renseigné).

## Animations

Mêmes principes que toute la série : Ken Burns sur les cartes, xfade
(0,28 s), bandeaux d'étape, encadré orange pulsant sur les 3 clics ("Ajouter
une absence", "Sélectionner le type", "Enregistrer"). Pas de mini-animation
dédiée : le rush illustre déjà nativement le parcours (solde avant/après,
badge "En attente").

## Statut publication

Montage terminé et checklist de compatibilité passée (H.264 High/yuv420p,
AAC 48 kHz stéréo, faststart, peak -7,2 dBFS, 0 erreur de décodage). Demande
de Michael de se placer côté employé pour cette vidéo (message du
2026-08-03) : vidéo et vignette hébergées via URL GitHub raw sur la branche
`claude/foodeatup-tutorial-video-vn7udf`. Lovable : tutoriel
`poser-un-conge-cote-employe` à ajouter dans `src/data/tutorials.ts` (module
`equipe-planning`, subcategory "17 - poser un congé côté employé"), avec
`chefTip` mais sans `claudePrompt` (pas d'outil MCP correspondant, action
self-service employé).
