# Tutoriel — Commander ses cartes NFC pour le badge (module Équipe & Planning)

Treizième vidéo du module `equipe-planning` (catalogue #10). Durée livrée :
**50,84 s** — H.264 High/yuv420p, AAC LC 48 kHz stéréo, faststart (moov avant
mdat confirmé). Audio : max **-7,3 dBFS** / mean -21,8 dBFS. Decode 0 erreur.

## Ce que montre le rush

Le rush (34,08 s, capture 1920x828 @25fps, pas de chrome navigateur à
rogner) montre la page de configuration du QR code de pointage : QR actif,
statistiques → scroll vers les réglages de sécurité (niveau, rayon,
tolérance) et la section "Accès des employés" (PIN déjà défini, badge NFC
en option) → section "Badges NFC & cartes marketing" (cartes PVC + puce
imprimées, 2,5 €/carte) → clic "Générer badge" pour Alice Charbit → un
identifiant unique de badge est créé (`BADGE-KKWQESIS5MBH268Y`) → clic
"Commander les badges NFC" → modale de sélection des employés (Alice + Jean,
2 cartes, 6,50 € dont 1,50 € de marge) → clic "Confirmer la commande" →
commande enregistrée (mode local, envoi à l'imprimeur Printags dès que la
clé API est activée).

## Voix off (7 lignes, voix Adam FR `TGAegA0zNRi8I6nUdq3i`)

| # | Texte | Durée | Segment |
|---|---|---:|---|
| N0 | Envie de faire pointer votre équipe par badge, sans code PIN ni smartphone ? Voici comment commander des cartes NFC personnalisées. | 7,11 s | intro |
| N1 | Chaque employé peut avoir son propre badge, en complément de son code PIN, pour pointer ou se connecter au logiciel. | 6,50 s | B — Accès des employés |
| N2 | Dans le module Équipe, la section Badges NFC propose des cartes PVC avec puce imprimée, pour deux euros cinquante la carte. | 8,18 s | C — Badges NFC & cartes marketing |
| N3 | Un clic sur Générer badge, et un identifiant unique de pointage est aussitôt créé pour cet employé. | 5,67 s | E — badge généré |
| N4 | Sélectionnez les employés à équiper, et validez la commande : chaque badge encode l'identifiant de pointage qui lui est propre. | 6,53 s | G — modale "Commander les badges NFC" |
| N5 | La commande est enregistrée, prête à être imprimée et envoyée par votre partenaire cartes NFC. | 5,51 s | I — commande enregistrée |
| N6 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (CTA, réutilisé tel quel depuis `foodeatup-borne-tuto`) |

N6 réutilisé tel quel (texte générique identique aux tutos précédents) —
zéro crédit ElevenLabs dépensé sur cette ligne.

## Découpage

Segments dimensionnés dès le départ à partir des durées VO réellement
mesurées. Première tentative : dérive de 0,1 à 1,38 s sur N2-N6 (segments
C/E/G/I un peu trop courts) — corrigé en un seul passage (C, E, G, I
élargis) → **dérive nulle**.

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 7,50 s | COMMANDER SES CARTES NFC POUR LE BADGE |
| A | 0,20 → 1,00 | 3,00 s | page QR actif |
| B | 6,00 → 8,00 | 7,20 s | Accès des employés (PIN défini) |
| C | 9,00 → 9,60 | 8,20 s | Badges NFC & cartes marketing, tarif |
| D | 9,90 → 10,20 | 0,90 s | **zoom-punch** sur "Générer badge" |
| E | 12,00 → 13,00 | 5,60 s | identifiant de badge créé |
| F | 13,80 → 14,10 | 0,90 s | **zoom-punch** sur "Commander les badges NFC" |
| G | 16,00 → 19,50 | 6,50 s | modale de sélection + prix |
| H | 19,60 → 19,90 | 0,90 s | **zoom-punch** sur "Confirmer la commande" |
| I | 24,00 → 27,00 | 6,50 s | commande enregistrée |
| outro | carte | 7,41 s (étendue) | CTA |

Transitions : `fade` sur les enchaînements continus (intro→A, B→C, C→D, E→F,
G→H, I→outro), `slideleft` sur les coupures de contexte (A→B, D→E, F→G,
H→I).

## Pas de séquence "Utiliser avec Claude"

Aucun outil `mcp__FoodEatUp__*` ne couvre la commande de cartes physiques
NFC : c'est une action matérielle/logistique (impression PVC, expédition par
un partenaire externe Printags), pas un geste d'administration API — même
raisonnement que `foodeatup-borne-tuto` (appairage PIN) et
`foodeatup-jarvis-tuto` (scan QR). Pas de prompt inventé ; section absente à
la fois de la vidéo et de la fiche Lovable (`claudePrompt` non renseigné).

## Animations

Mêmes principes que toute la série : Ken Burns sur les cartes, xfade
(0,28 s), bandeaux d'étape, encadré orange pulsant sur les 3 clics (Générer
badge, Commander les badges NFC, Confirmer la commande). Pas de
mini-animation dédiée : le rush illustre déjà nativement le parcours (badge
généré, prix calculé, commande confirmée).

## Statut publication

Montage terminé et checklist de compatibilité passée (H.264 High/yuv420p,
AAC 48 kHz stéréo, faststart, peak -7,3 dBFS, 0 erreur de décodage). Vidéo
et vignette hébergées via URL GitHub raw sur la branche
`claude/foodeatup-tutorial-video-vn7udf`. Lovable : tutoriel
`commander-ses-cartes-nfc` à ajouter dans `src/data/tutorials.ts` (module
`equipe-planning`, subcategory "10 - commander ses cartes NFC pour le
badge"), avec `chefTip` mais sans `claudePrompt`.
