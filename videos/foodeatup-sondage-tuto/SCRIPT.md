# Tutoriel — Créer un sondage fidélité (module « Marketing, Fidélité & Iris », 17/24)

**Statut : PUBLIÉ (2026-08-05).** Validation de Michael reçue pour la série ("tu peux
publier"). Rush fourni : `assets/screen.mp4` (70,04 s, 1920x828, 25 fps). Intro card :
`assets/intro.jpg` (« CRÉER UN SONDAGE »). Outro card : `assets/outro.jpg` (identique aux
tutos précédents, réemployée telle quelle).

Livrable final : `out/foodeatup-sondage-tuto-v1.mp4` (51,80 s, H.264 High/yuv420p, AAC
48kHz stéréo, faststart, peak -7,3 dBFS).

## Déroulé du rush

| t | Écran |
|---:|---|
| 0,0 → 1,85 s | Page **Fidélité & jeux**, onglet **Sondages**, état vide (« Aucun sondage ») |
| ≈ 1,9 s | **Clic** « Créer un sondage » |
| 2,0 → 23,0 s | Modal **Nouveau sondage** : titre (« sondage express »), déclencheur (Post-commande → Lien/QR autonome), récompense en points |
| 23,0 → 42,0 s | Ajout de questions : Note 1-5, NPS 0-10, Texte libre |
| 42,0 → 64,8 s | Ajout d'une question **Choix multiples** + options tapées une à une (« service, cuisine, ambiance, prix ») + case Question obligatoire |
| ≈ 64,9 s | **Clic** « Enregistrer le sondage » |
| 65,0 → 67,0 s | Rechargement de la liste (flash « Aucun sondage », coupé au montage) |
| 67,0 → 70,0 s | Carte finale : « sondage express » **Actif**, 3 question(s), déclencheur lien/QR, récompense 15 pts, toast « Sondage enregistré ✓ » |

Montage très compressé (rush de 70 s → vidéo de ~52 s) : la frappe des champs (titre,
options) est accélérée ~2,5 à 3,3x plutôt que montrée en temps réel, même principe que le
segment carte bancaire de `foodeatup-abonnement-tuto`.

## Script VO (voix Adam FR ElevenLabs, `TGAegA0zNRi8I6nUdq3i`)

| # | Texte | Placement |
|---|---|---|
| N0 | Envie de connaître l'avis de vos clients ? Créez un sondage en quelques clics, directement dans votre programme de fidélité. | carte d'intro |
| N1 | Depuis Fidélité et jeux, ouvrez l'onglet Sondages, puis cliquez sur Créer un sondage. | page + clic |
| N2 | Donnez un titre à votre sondage, choisissez son déclencheur — après une commande, ou via un lien ou QR code — et fixez sa récompense en points. | modal titre/déclencheur/récompense |
| N3 | Ajoutez vos questions : une note sur 5, un score de recommandation NPS, ou une question en texte libre. | questions simples |
| N4 | Pour une question à choix multiples, listez vos options séparées par des virgules, et cochez Question obligatoire si besoin. | choix multiples + options |
| N5 | Cliquez sur Enregistrer le sondage : il apparaît aussitôt actif, prêt à collecter les avis de vos clients. | clic + carte finale |
| N6 | Chaque réponse alimente vos statistiques clients, et peut même récompenser vos convives en points de fidélité. | bénéfice |
| N7 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | carte de fin (CTA) |

## Cas d'usage Claude

Pas d'outil MCP pour la **création** d'un sondage (action UI uniquement). En revanche
`mcp__FoodEatUp__list_surveys` couvre un usage naturel complémentaire (lister ses sondages
actifs) : ajouté en `claudePrompt` sur la fiche Lovable. Les **résultats** détaillés d'un
sondage (`get_survey_results`) sont laissés au tutoriel dédié déjà prévu au catalogue
(item 18 « Résultats des Sondages (historique) ») pour éviter le chevauchement.

## Publication

- **RapidoCMS** : vidéo `fe-sondage-tuto`, vignette `fe-sondage-tuto-thumb`.
- **Lovable** (`project_id 55ff35b7-c442-42c4-950c-8c7fd420c645`) : module
  `marketing-fidelite`, slug `creer-un-sondage-fidelite`. Une fiche placeholder
  existait déjà sous ce même slug (section "17 · Jeux & sondages", créée par une
  autre session, `durationSeconds: 0`, contenu "en cours de tournage") — l'agent
  Lovable l'a détectée et mise à jour avec le contenu réel plutôt que de créer un
  doublon.
- **GitHub** : commit sur `claude/foodeatup-video-tutorials-mgemxu`.
