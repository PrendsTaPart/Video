# Tutoriel — Configurer Caroline (voix & prompts)

Module Lovable `caroline-ia` (Agent IA Caroline & Salle), catalogue 6a-01
« Configurer Caroline (voix & prompts) » — `videos/CATALOGUE-157-TUTORIELS.md`.
Premier tutoriel du module `caroline-ia` (0/6 avant cette session).

Durée livrée : **43,0 s** — H.264 High/yuv420p, AAC 48 kHz stéréo, faststart.
Audio : true peak **-7,2 dBFS** (mesuré sur le MP4 final).

## Ce que montre le rush

Rush (65,60 s, fourni par Michael, `configurer_caroline_voix__prompts.mp4`,
1920x828) montre **deux choses à la suite, toutes deux en capture d'écran réelle** :

1. **Agent IA Caroline > Configuration voix** : prompt système (personnalité
   de Caroline), section Voix & téléphone (voix « Caroline féminine,
   chaleureuse », langue Français, numéro de l'agent), message d'accueil
   édité en direct, clic sur **Enregistrer** → toast « Configuration
   enregistrée ».
2. **Menu profil > Marketplace de prompts** : produit phare « Foodeatup mcp »
   (URL `https://foodeatup.com/api/mcp`), filtres par catégorie (Stock &
   Appro, Carte & Recettes, Commandes, Réservations, Finance, RH, Production,
   HACCP, Système, Orchestration) → filtre **Commandes(4)** → copie du prompt
   « Crée une commande (génère automatiquement facture + devis) » → collé
   dans **Claude.ai** → Claude orchestre (« Pensant à la création... » puis
   « Orchestrant la création de commande avec gestion automatique
   facture-devis »).

Ce rush est le premier de la série où la séquence « utilisez-le avec Claude »
est **filmée en réel** (Marketplace de prompts du produit lui-même) plutôt que
reconstituée avec le module `_shared/claude_prompt_sequence.py` — pas de carte
générée ici, juste des segments réels avec zoom-punch, comme le reste de la
vidéo.

## Voix off (9 lignes)

Voix Adam FR (`TGAegA0zNRi8I6nUdq3i`), `eleven_multilingual_v2`. N8 réutilisé
tel quel depuis `foodeatup-conformite-tuto/vo/N8.mp3` (texte générique — zéro
crédit ElevenLabs dépensé).

| # | Texte | Durée | Ancrage |
|---|---|---:|---|
| N0 | Configurer la voix et les prompts de Caroline sur FoodEatUp ? Deux minutes suffisent. | 4,49 s | carte d'intro |
| N1 | Dans Agent IA Caroline, réglez la voix, la langue et le numéro de votre agent vocal. | 4,73 s | A (prompt système + voix/langue/numéro) |
| N2 | Personnalisez le message d'accueil que Caroline utilise pour répondre à vos clients. | 4,21 s | B (message d'accueil édité) |
| N3 | Cliquez sur Enregistrer : la configuration est appliquée aussitôt. | 3,60 s | clic C + D (toast) |
| N4 | Depuis votre profil, ouvrez la Marketplace de prompts FoodEatUp. | 3,42 s | clic E (avatar) + F (menu) + clic G (Marketplace) |
| N5 | Filtrez par catégorie et copiez un prompt prêt à l'emploi, ici pour créer une commande. | 4,68 s | H (marketplace + filtre Commandes) + clic I (copier) |
| N6 | Collez-le dans Claude : il orchestre aussitôt vos outils FoodEatUp à votre place. | 4,26 s | K (prompt collé) + clic L (envoyer) |
| N7 | Voix sur-mesure, prompts prêts à l'emploi : Caroline et Claude travaillent pour vous, en coulisses. | 5,75 s | M (Claude orchestre) |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (CTA, réutilisée) |

## Découpage

| Seg | Source | Sortie | Contenu |
|---|---:|---:|---|
| intro | carte | 4,90 s | CONFIGURER CAROLINE VOIX & PROMPTS |
| A | 0,30 → 8,00 | 5,20 s | Configuration voix : prompt système + voix/langue/numéro |
| B | 8,00 → 18,70 | 4,60 s | message d'accueil édité |
| C | 18,70 → 19,30 | 0,90 s | **zoom-punch** sur Enregistrer (845, 722) |
| D | 19,30 → 23,60 | 3,50 s | toast « Configuration enregistrée » |
| E | 23,60 → 24,00 | 0,70 s | **zoom-punch** sur l'avatar profil (1723, 124) |
| F | 24,00 → 25,60 | 2,60 s | menu profil ouvert (Marketplace de prompts) |
| G | 25,60 → 26,00 | 0,70 s | **zoom-punch** sur « Marketplace de prompts » (1600, 327) |
| H | 27,00 → 35,60 | 4,60 s | Marketplace : produit phare + filtres + Commandes(4) |
| I | 35,60 → 36,00 | 0,70 s | **zoom-punch** sur l'icône copier, « Crée une commande » (527, 584) |
| K | 39,50 → 44,50 | 4,30 s | Claude.ai : prompt collé, en attente d'envoi |
| L | 46,70 → 47,10 | 0,70 s | **zoom-punch** sur le bouton envoyer (1673, 710) |
| M | 47,10 → 56,00 | 5,80 s | Claude orchestre (Pensant… → Orchestrant…) |
| outro | carte | 7,53 s | CTA (auto-étendue depuis 6,20 s pour absorber ~1,3 s de dérive résiduelle) |

Coordonnées des boutons eyeballées sur frames extraites (`ffmpeg -vf fps=2`
sur des fenêtres ciblées). Coupure franche (cut noir de ~3 s dans le rush,
changement d'application) entre H/I et K **volontairement sautée** : la
source K reprend directement à 39,50 s (Claude déjà ouvert, prompt déjà
collé) — le fondu `slideleft` masque la coupure plus proprement que les
frames noires du rush brut.

## Pas de séquence Claude synthétique

Contrairement au reste de la série, **aucune carte générée** (pas de
`_shared/claude_prompt_sequence.py`) : le rush capture déjà, en vrai, le
copier-coller du prompt FoodEatUp vers Claude.ai. Le prompt correspond à
l'outil `mcp__FoodEatUp__create_order` (existe, schéma vérifié) :

> Pour mon établissement (ID [ID établissement]), crée une commande (génère
> automatiquement facture + devis). Peut être liée à une table (sur place).
> Demande-moi les informations nécessaires.

Même texte côté fiche Lovable (`claudePrompt`).

## Bug de bannière évité (drawbox vs t)

`banner()` copié initialement depuis le template `foodeatup-conformite-tuto`
utilisait `drawbox` animé sur `t` pour le filet orange + la plaque bleue —
piège déjà documenté plusieurs fois dans `FOODEATUP-TUTORIELS-WORKFLOW.md`
(`drawbox` n'évalue pas `t` sur cet ffmpeg 6.1.1, la boîte ne se dessine
jamais). Repéré ici en QA visuelle (texte blanc nu, sans plaque, sur le fond
sombre de Claude.ai) avant livraison. Corrigé en reprenant la version
`drawtext` + `box=1` du `build.py` de référence
(`videos/foodeatup-mouvement-stock-tuto/build.py`) : la plaque colorée est le
`box` de `drawtext` lui-même, qui réévalue bien `t` par frame.

## Animations

Mêmes principes que toute la série : Ken Burns sur les cartes, xfade (0,28 s,
alternance fade/slideleft), zoom-punch 1,20x sur les 5 clics, bandeaux
d'étape. Pas de clip avatar (VO ElevenLabs uniquement).

## Vignette

`assets/intro.jpg` (image fournie par Michael, `CONFIGURER_CAROLINE_VOIX__PROMPTS.jpg`)
réutilisée telle quelle, recadrée 1280x720 sans retouche créative →
`out/thumbnail-youtube.jpg` (116 Ko).

## Publication

Pipeline exécuté de bout en bout sur demande explicite de Michael (script,
voix, montage, QA, thumbnail, puis publication RapidoCMS + Lovable + mise à
jour du dépôt) — demande groupée couvrant les étapes de validation
intermédiaires, même principe que `foodeatup-conformite-tuto`.
