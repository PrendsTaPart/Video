# Tutoriel — Synchro Google Avis

Module `marketing-fidelite` (Marketing, Fidélité & Iris), catalogue 157 tutoriels,
entrée "02 Synchro Google Avis clients" (voir `videos/CATALOGUE-157-TUTORIELS.md`).

Intrants fournis par Michael : carte d'ouverture `SYNCHRO_GOOGLE_AVIS.jpg`, carte de
fin `page_fin_vid..jpg` (générique, réutilisée telle quelle), écran `Connecter_Google_
pour_récupérer_les_avis_clients.mp4` (1920x828, 48.77s).

Pas de séquence "Utilisez cette fonctionnalité avec Claude" : aucun outil
`mcp__FoodEatUp__*` ne correspond à la connexion/synchronisation du compte Google
(flux OAuth) — `list_reviews` / `reply_review` / `moderate_review` gèrent des avis déjà
synchronisés, pas la connexion elle-même. Règle "pas de prompt inventé"
(`FOODEATUP-TUTORIELS-WORKFLOW.md`) appliquée : `claudePrompt` absent côté vidéo et
côté fiche Lovable.

Durée livrée : **36,56 s** — H.264 High/yuv420p, AAC 48 kHz stéréo, faststart.
Audio : true peak **-7,1 dBFS** (mesuré sur le MP4 final).

## Voix off (Adam FR, `TGAegA0zNRi8I6nUdq3i`)

| # | Texte | Durée | Placement |
|---|---|---:|---|
| N0 | Recevoir vos avis Google directement dans FoodEatUp ? Ça se fait en quelques clics. | 4,31 s | carte d'intro |
| N1 | Depuis Avis clients, cliquez sur Connecter Google. | 2,69 s | page Avis clients + clic |
| N2 | Choisissez votre compte Google, puis autorisez l'accès à votre fiche d'établissement. | 4,44 s | chooser + consentement Google |
| N3 | Retour sur Avis clients : le badge Google connecté confirme la liaison. | 4,00 s | page reconnectée |
| N4 | Un clic sur Synchroniser, et vos avis Google remontent pour modération. | 4,00 s | clic Synchroniser |
| N5 | Copiez le lien de dépôt et partagez-le sur vos tickets pour récolter plus d'avis. | 4,31 s | clic Lien de dépôt + toast copié |
| N6 | Tous vos avis sont réunis au même endroit : rien ne se publie sans votre validation. | 4,31 s | plan large de fin |
| N7 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,09 s | carte de fin (CTA) |

## Découpage

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 4,60 s | SYNCHRO GOOGLE AVIS |
| A | 0,20 → 5,30 | 3,30 s | page Avis clients, bandeau "1 - Avis clients" |
| B | 5,30 → 5,65 | 0,95 s | **zoom-punch** sur « Connecter Google » (1642, 328) |
| C | 7,00 → 20,60 | 5,30 s | chooser + consentement Google, bandeau "2 - Compte Google" |
| D | 34,30 → 38,00 | 4,30 s | retour connecté, bandeau "Google connecte" |
| E | 38,00 → 39,60 | 4,00 s | **zoom-punch** sur « Synchroniser » (1662, 165) |
| F | 42,50 → 43,60 | 1,60 s | **zoom-punch** sur « Lien de dépôt » (1055, 323), bandeau "Lien copie" |
| G | 43,60 → 48,60 | 6,50 s | plan large de fin, page calme |
| outro | carte | 8,22 s (auto-étendue) | CTA |

Coupes volontaires :
- **20,6 → 34,3 s** — détour involontaire par le menu hamburger (le screen recording
  navigue vers Avis clients par le menu au lieu d'y rester après le retour Google ;
  sans valeur pédagogique, coupé net).
- **39,6 → 42,5 s** — clic Synchroniser suivi d'un toast **"Server Error"** : artefact
  du compte de démo (pas de vraie fiche Google Business connectée en formation), pas le
  comportement réel du produit. Coupé, la vidéo enchaîne directement sur le clic Lien de
  dépôt (qui, lui, fonctionne et affiche bien "Lien de dépôt copié").

## Piège rencontré — coordonnées de bouton dépendantes du scroll

`BTN_SYNC` mesuré une première fois sur la frame de retour connecté (34,3 s, page en
haut) donnait (1663, 328) — zoom-punch placé dans le vide sur le rendu (cf. capture à
t=18,5 s de la v1). En cause : au moment réel du clic Synchroniser (~38-39 s), la page
est scrollée ~163 px plus bas (en-tête hors champ). Corrigé en mesurant chaque
coordonnée sur la frame exacte du clic (`ffmpeg -ss <t> -frames:v 1`), pas sur une
frame voisine — même piège que documenté pour les bandeaux dans
`FOODEATUP-TUTORIELS-WORKFLOW.md`. Valeur corrigée : (1662, 165).

## Point de vigilance — dimensionner les segments sur la VO, pas l'inverse

Premier passage : E/F/G trop courts (1,05 + 1,50 + 3,60 s) pour porter N4+N5+N6
(4,00 + 5,85 + 5,67 s) sans déborder — dérive de 3,75 à 11,3 s accumulée jusqu'à la
carte de fin (extension à 17,56 s). Corrigé en deux temps : raccourci N5 et N6 (texte
moins long, ré-généré) et redimensionné E (1,05 → 4,00 s, ralenti car peu de mouvement
réel dans le rush à cet endroit) + fusion de l'ancien F/G en un seul plan large plus
long. Extension finale de la carte de fin ramenée à 8,22 s.

## Animations

Mêmes principes que le reste de la série : Ken Burns sur les cartes fixes, xfade
(0,28 s) à chaque raccord, bandeaux d'étape en 2 `drawtext` (`box=1`, pas `drawbox`
animé sur `t` — silencieusement ignoré par cet ffmpeg 6.1.1), encadré orange pulsant
sur chaque clic. Aucun clip avatar, voix ElevenLabs de bout en bout.
