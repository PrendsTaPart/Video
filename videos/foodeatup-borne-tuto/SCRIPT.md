# Tutoriel — Installer la borne d'accueil FoodEatUp (module Équipe & Planning)

Troisième vidéo du module `equipe-planning` (suite de "Établir un contrat et son
salaire"). Durée livrée : **37,0 s** — H.264 High/yuv420p, AAC 48 kHz stéréo,
faststart. Audio : true peak **-7,3 dBFS**. Decode 0 erreur, moov avant mdat
(faststart confirmé).

## Ce que montre le rush

Le rush (15,56 s, capture Chrome 1920x1020 @60fps — chrome navigateur rogné, canevas
final 1920x822) montre la page publique de la borne d'accueil
(`foodeatup.com/employee/qr/<jeton>`, accessible via QR code) : écran "Qui êtes-vous ?"
listant les employés → sélection de la carte "Soulayma Abdenbi" → écran "Saisissez
votre pin" (clavier numérique, 4 chiffres) → une fois le PIN saisi, deux choix
apparaissent : "Pointer" (pointage horaire) ou "Mon espace" (espace personnel) → clic
sur "Mon espace" → tableau de modules limité au rôle de l'employée (manager :
Tableau de bord, Mon planning, Stocks, Produits, Recettes, Carte & Menu, Production,
Fournisseurs, Courses, Clients, Factures, Devis) → remontée en haut de page montrant
l'en-tête complet de l'application avec l'avatar "SA" connecté.

## Voix off (7 lignes, voix Adam FR `TGAegA0zNRi8I6nUdq3i`)

| # | Texte | Durée | Segment |
|---|---|---:|---|
| N0 | Installer la borne d'accueil pour vos employés dans FoodEatUp ? Voici comment ça marche. | 4,41 s | intro |
| N1 | Chaque employé retrouve son profil sur la borne, accessible depuis une tablette ou un téléphone. | 5,28 s | A — grille "Qui êtes-vous ?" |
| N2 | Il sélectionne son profil, puis saisit son code PIN personnel. | 3,24 s | clic carte employé → C — écran PIN |
| N3 | D'un tap, il pointe ses heures, ou accède directement à son espace personnel. | 4,55 s | D — choix Pointer / Mon espace |
| N4 | Son espace affiche uniquement les modules autorisés par son rôle : planning, stocks, recettes, et plus encore. | 6,50 s | clic "Mon espace" → F — grille de modules |
| N5 | Chaque connexion est identifiée et son pointage enregistré automatiquement. | 4,26 s | G — en-tête complet, connectée |
| N6 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (CTA, réutilisé tel quel) |

N6 réutilisé tel quel (texte générique identique à tous les tutos précédents) — zéro
crédit ElevenLabs dépensé sur cette ligne. Pas de séquence "Utiliser avec Claude" sur
cette vidéo : voir plus bas.

## Découpage

Segments dimensionnés généreusement (leçon des tutos précédents — mesurer chaque
ligne VO réelle avant de fixer la durée du segment, pas l'inverse) : la première
tentative avait des segments bien trop courts pour les lignes VO réellement générées
(jusqu'à 9,3 s de dérive sur N5) ; corrigé en élargissant A/C/D/F/G et l'intro.

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 5,00 s | INSTALLER LA BORNE D'ACCUEIL |
| A | 0,00 → 1,00 | 6,00 s | grille "Qui êtes-vous ?" (ralenti ~6x, écran quasi statique) |
| B | 4,85 → 5,15 | 0,90 s | **zoom-punch** sur la carte "Soulayma Abdenbi" (1502, 335) |
| C | 5,30 → 6,00 | 3,50 s | écran "Saisissez votre pin", "Bonjour Soulayma Abdenbi" |
| D | 6,00 → 9,55 | 5,00 s | saisie du PIN (points qui se remplissent) → "Pointer" / "Mon espace" |
| E | 9,55 → 9,85 | 0,90 s | **zoom-punch** sur "Mon espace" (1614, 641) |
| F | 11,00 → 13,20 | 7,00 s | grille de modules "mon espace" |
| G | 13,20 → 15,557 | 4,50 s | remontée en haut, en-tête complet, avatar "SA" |
| outro | carte | 6,26 s | CTA |

Coordonnées de clic mesurées sur les frames extraites du rush **après** rognage du
chrome navigateur (`crop=1920:822:0:197` appliqué une fois en amont dans `build.py`,
puis toutes les mesures de clic faites dans ce repère déjà rogné).

## Pas de séquence "Utiliser avec Claude"

Aucun outil `mcp__FoodEatUp__*` ne couvre l'appairage borne/PIN : c'est une action
libre-service de l'employé sur une tablette partagée (scan d'un QR public, saisie
d'un code PIN), pas un geste d'administration côté API — même raisonnement que la
séquence QR de `foodeatup-jarvis-tuto`. Pas de prompt inventé ; section absente à la
fois de la vidéo et de la fiche Lovable (`claudePrompt` non renseigné).

## Animations

Mêmes principes que toute la série : Ken Burns sur les cartes, xfade (0,28 s),
bandeaux d'étape, encadré orange pulsant sur les 2 clics (carte employé, "Mon
espace"). Pas de clip avatar, pas de mini-animation dédiée sur ce tutoriel (rien à
illustrer au-delà de ce que montre déjà l'écran).

## Statut publication

Montage terminé et checklist de compatibilité passée (H.264 High/yuv420p, AAC 48 kHz
stéréo, faststart, peak -7,3 dBFS, 0 erreur de décodage). Demande explicite de
Michael de produire et publier cette vidéo avec astuces du chef et prompt Lovable
(message du 2026-08-03) : vidéo et vignette hébergées via URL GitHub raw sur la
branche `claude/foodeatup-tutorial-video-vn7udf` (RapidoCMS non disponible dans
cette session). Lovable : tutoriel `installer-la-borne-daccueil` ajouté dans
`src/data/tutorials.ts` (module `equipe-planning`), avec `chefTip` mais sans
`claudePrompt` (pas d'outil MCP correspondant).
