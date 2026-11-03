# Tutoriel — Déclarer son e-reporting (module Comptabilité & Achats)

Deuxième vidéo du module `comptabilite` (catalogue #9, Comptabilité & Achats).
Durée livrée : **57,24 s** — H.264 High/yuv420p, AAC LC 48 kHz stéréo,
faststart (moov avant mdat confirmé). Audio : max **-7,0 dBFS** / mean
-22,8 dBFS. Decode 0 erreur.

## Ce que montre le rush

Le rush (51,84 s, capture 1920x828 @25fps, pas de chrome navigateur à
rogner) montre le module Comptabilité > Facture, onglet E-Reporting :
statistiques (Déclarées, En attente, En retard), prochaine échéance,
tableau par période (Total HT, TVA, Statut, Date déclaration) → menu Action
d'une période en retard → "Déclarer la période" → statistiques mises à jour
→ retour aux Factures (badge Conformité 2026 actualisé) → détail d'une
facture "Payée" → menu "Téléchargements et options" (Télécharger PDF
Factur-X, Télécharger XML CII, Archiver légalement, PDF standard, Télécharger
UBL) → génération du Factur-X, badge "✓ Factur-X" visible dans la liste →
onglet Archives légales (N° facture, Montant, Date d'archivage, Expire le à
10 ans, Hash SHA-256) → "Vérifier l'intégrité" → modale "Vérification
d'intégrité" confirmant "Facture intègre".

## Voix off (7 lignes, voix Adam FR `TGAegA0zNRi8I6nUdq3i`)

| # | Texte | Durée | Segment |
|---|---|---:|---|
| N0 | Comment déclarer son e-reporting et archiver légalement ses factures dans FoodEatUp ? Voici comment faire. | 5,62 s | intro |
| N1 | L'onglet E-Reporting récapitule vos déclarations par période : combien sont déclarées, en attente, ou en retard. | 6,64 s | C — stats + tableau par période |
| N2 | Un clic sur Déclarer la période, et l'e-reporting de cette période est transmis, en un instant. | 5,04 s | E — période déclarée |
| N3 | Depuis une facture, générez aussi son Factur-X ou son XML, aux formats exigés par la réforme 2026. | 7,13 s | F/H — Téléchargements et options |
| N4 | L'onglet Archives légales conserve chaque facture dix ans, avec son empreinte numérique unique. | 5,20 s | K — Archives légales, Hash SHA-256 |
| N5 | Un clic suffit pour vérifier qu'une facture archivée n'a jamais été modifiée. | 4,21 s | M — Vérification d'intégrité |
| N6 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (CTA, réutilisé tel quel depuis `foodeatup-borne-tuto`) |

N6 réutilisé tel quel (texte générique identique aux tutos précédents) —
zéro crédit ElevenLabs dépensé sur cette ligne.

## Découpage

Segments dimensionnés dès le départ à partir des durées VO réellement
mesurées — **dérive nulle dès le premier montage**.

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 6,50 s | DÉCLARER SON E-REPORTING COMPTABILITÉ |
| A | 0,20 → 2,00 | 3,00 s | module Comptabilité, liste des factures |
| B | 2,50 → 2,80 | 0,90 s | **zoom-punch** sur l'onglet "E-Reporting" |
| C | 6,00 → 9,00 | 7,50 s | stats + tableau par période |
| D | 9,30 → 9,60 | 0,90 s | **zoom-punch** sur "Déclarer la période" |
| E | 10,00 → 12,50 | 5,50 s | période déclarée, stats actualisées |
| F | 21,00 → 24,00 | 6,00 s | détail d'une facture payée |
| G | 26,30 → 26,60 | 0,90 s | **zoom-punch** sur "Téléchargements et options" |
| H | 27,00 → 30,00 | 6,50 s | menu (PDF Factur-X, XML, Archiver, UBL) |
| I | 36,00 → 39,00 | 4,00 s | retour à la liste, Factur-X généré |
| J | 43,50 → 43,80 | 0,90 s | **zoom-punch** sur l'onglet "Archives légales" |
| K | 45,00 → 46,00 | 6,00 s | archives, Hash SHA-256, expiration 10 ans |
| L | 46,30 → 46,60 | 0,90 s | **zoom-punch** sur "Vérifier l'intégrité" |
| M | 48,00 → 50,50 | 5,00 s | modale "Facture intègre" |
| outro | carte | 6,20 s | CTA |

Transitions : `fade` sur les enchaînements continus (intro→A, A→B, C→D, F→G,
I→J, K→L, M→outro), `slideleft` sur les coupures de contexte (B→C, D→E,
E→F, G→H, H→I, J→K, L→M).

## Pas de séquence "Utiliser avec Claude"

Aucun outil `mcp__FoodEatUp__*` ne couvre la déclaration e-reporting, la
génération Factur-X/XML, l'archivage légal ou la vérification d'intégrité
par hash : ce sont des fonctionnalités de conformité réglementaire propres
au produit, pas des endpoints API (`update_invoice_status` gère les statuts
métier, mais aucun de ces quatre gestes de conformité). Pas de prompt
inventé ; section absente à la fois de la vidéo et de la fiche Lovable
(`claudePrompt` non renseigné).

## Animations

Mêmes principes que toute la série : Ken Burns sur les cartes, xfade
(0,28 s), bandeaux d'étape, encadré orange pulsant sur les 5 clics (onglet
E-Reporting, Déclarer la période, Téléchargements et options, onglet
Archives légales, Vérifier l'intégrité). Pas de mini-animation dédiée :
le rush illustre déjà nativement le parcours de conformité complet.

## Astuce du chef — conformité 2026

L'astuce du chef publiée sur Lovable explique le lien entre les trois
fonctionnalités : l'e-reporting doit être déclaré à échéance régulière
(mensuelle) auprès de l'administration ; le Factur-X/XML est le format de
facture électronique structuré exigé par la réforme ; l'archivage légal (10
ans, hash SHA-256) prouve qu'une facture n'a jamais été modifiée après
émission — les trois ensemble couvrent l'obligation de conformité facture
électronique 2026.

## Statut publication

Montage terminé et checklist de compatibilité passée (H.264 High/yuv420p,
AAC 48 kHz stéréo, faststart, peak -7,0 dBFS, 0 erreur de décodage). Vidéo
et vignette hébergées via URL GitHub raw sur la branche
`claude/foodeatup-tutorial-video-vn7udf`. Lovable : tutoriel
`declarer-son-ereporting` à ajouter dans `src/data/tutorials.ts` (module
`comptabilite`, subcategory "9 - déclarer son e-reporting"), avec `chefTip`
mais sans `claudePrompt`. Deuxième vidéo du module Comptabilité & Achats.
