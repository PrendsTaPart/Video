# Tutoriel — Retrouver ses documents, paie & contrat (module Équipe & Planning)

Quatorzième vidéo du module `equipe-planning` (catalogue #19). Durée
livrée : **64,72 s** — H.264 High/yuv420p, AAC LC 48 kHz stéréo, faststart
(moov avant mdat confirmé). Audio : max **-7,1 dBFS** / mean -23,3 dBFS.
Decode 0 erreur.

## Ce que montre le rush

Le rush (48,9 s, capture Chrome 1920x1020 @60fps — chrome navigateur rogné,
canevas final 1920x828) montre l'espace employé "Mon coin RH" : tableau de
bord → menu avatar (Mes modules, Dashboard, Planning, Congés, Performances,
**Profil**, Déconnexion) → page Profil : aperçu du contrat en cours (type,
établissement, responsable, salaire, durée) → section "Informations
personnelles" (état civil, coordonnées non renseignées) → "Modifier les
informations" ouvre un panneau à onglets éditable (État civil / Coordonnées
/ Santé — y compris IBAN/BIC, contact d'urgence) → onglet "Contrat" : "Voir
plus" ouvre le détail complet (temps de travail hebdomadaire, jours
travaillés, intitulé de l'emploi, puis onglet Paie : rémunération, primes,
indemnité de transport) → onglet "Documents" : carte d'identité et contrat
de travail déjà déposés, bouton "Importer un document" (nom + glisser-
déposer PDF/JPG/PNG, 10 Mo max).

## Voix off (6 lignes, voix Adam FR `TGAegA0zNRi8I6nUdq3i`)

| # | Texte | Durée | Segment |
|---|---|---:|---|
| N0 | Où retrouver son contrat, ses fiches de paie, et modifier ses informations personnelles ? Voici l'espace Profil, côté employé. | 6,92 s | intro |
| N1 | Chaque employé retrouve un aperçu de son contrat : type, établissement, responsable, salaire, et durée. | 6,87 s | C — aperçu du contrat |
| N2 | Il peut aussi mettre à jour ses informations personnelles : état civil, coordonnées, ou données de santé. | 6,16 s | D/F — informations personnelles |
| N3 | L'onglet Contrat détaille le temps de travail, la rémunération, les primes et les indemnités. | 5,28 s | G/I — détail contrat & paie |
| N4 | L'onglet Documents rassemble sa carte d'identité et son contrat de travail, et permet d'en importer de nouveaux. | 5,85 s | J/L — documents |
| N5 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (CTA, réutilisé tel quel depuis `foodeatup-borne-tuto`) |

N5 réutilisé tel quel (texte générique identique aux tutos précédents) —
zéro crédit ElevenLabs dépensé sur cette ligne.

## Découpage

Segments dimensionnés dès le départ à partir des durées VO réellement
mesurées — **dérive nulle dès le premier montage**.

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 7,50 s | RETROUVER SES DOCUMENTS PAIE & CONTRAT |
| A | 0,20 → 2,00 | 3,00 s | tableau de bord "Mon coin RH" |
| B | 3,15 → 3,45 | 0,90 s | **zoom-punch** sur "Profil" (menu avatar) |
| C | 6,00 → 8,00 | 7,50 s | aperçu du contrat en cours |
| D | 9,00 → 9,90 | 6,00 s | section informations personnelles |
| E | 10,00 → 10,30 | 0,90 s | **zoom-punch** sur "Modifier les informations" |
| F | 12,00 → 21,00 | 7,00 s | panneau à onglets (état civil/coordonnées/santé) |
| G | 24,00 → 27,00 | 6,00 s | onglet Contrat, résumé |
| H | 27,50 → 27,80 | 0,90 s | **zoom-punch** sur "Voir plus" |
| I | 28,50 → 33,50 | 6,50 s | détail contrat & paie |
| J | 36,00 → 38,00 | 6,00 s | onglet Documents, liste |
| K | 40,00 → 40,30 | 0,90 s | **zoom-punch** sur "Importer un document" |
| L | 42,00 → 44,00 | 5,00 s | modale d'import |
| M | 46,00 → 48,89 | 4,00 s | retour à l'aperçu |
| outro | carte | 6,20 s | CTA |

Transitions : `fade` sur les enchaînements continus (intro→A, C→D, D→E, G→H,
J→K, M→outro), `slideleft` sur les coupures de contexte (A→B, B→C, E→F,
F→G, H→I, I→J, K→L, L→M).

## Pas de séquence "Utiliser avec Claude"

Aucun outil `mcp__FoodEatUp__*` ne couvre l'édition détaillée des
informations personnelles (état civil, sécurité sociale, RIB, contact
d'urgence) ni l'import de documents côté employé : `update_employee` ne
prend que prénom/nom/email/téléphone/rôle, et `list_employee_documents` est
une lecture seule côté manager — aucun des deux ne correspond à ce que
montre le rush. Même raisonnement que `foodeatup-borne-tuto` et
`foodeatup-conge-employe-tuto` : action self-service de l'employé sur son
propre profil, pas un geste d'administration API. Pas de prompt inventé ;
section absente à la fois de la vidéo et de la fiche Lovable (`claudePrompt`
non renseigné).

## Animations

Mêmes principes que toute la série : Ken Burns sur les cartes, xfade
(0,28 s), bandeaux d'étape, encadré orange pulsant sur les 3 clics (Profil,
Modifier les informations, Voir plus, Importer un document — 4 clics au
total). Pas de mini-animation dédiée : le rush illustre déjà nativement le
parcours (profil, édition, contrat détaillé, documents).

## Statut publication

Montage terminé et checklist de compatibilité passée (H.264 High/yuv420p,
AAC 48 kHz stéréo, faststart, peak -7,1 dBFS, 0 erreur de décodage). Vidéo
et vignette hébergées via URL GitHub raw sur la branche
`claude/foodeatup-tutorial-video-vn7udf`. Lovable : tutoriel
`retrouver-ses-documents-paie-et-contrat` à ajouter dans
`src/data/tutorials.ts` (module `equipe-planning`, subcategory "19 -
retrouver ses documents, paie et contrat"), avec `chefTip` mais sans
`claudePrompt`.
