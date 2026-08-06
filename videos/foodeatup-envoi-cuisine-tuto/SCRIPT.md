# Tutoriel — Envoyer une commande en cuisine (FoodEatUp)

Module `service-commande` (Service Multi-Canal, catégorie « Flux de Service & KDS »),
sujet **7a-03 « Envoyer en Cuisine en direct »** (`videos/CATALOGUE-157-TUTORIELS.md`
ligne 100) — 1er tutoriel publié pour ce module (0/3 avant celui-ci).

Assets fournis par Michael :
- `assets/intro.jpg` = carte "ENVOI DIRECT CUISINE" (fournie).
- `assets/outro.jpg` = carte CTA FoodEatUp générique (même fichier, md5 identique, que
  l'outro déjà réutilisé sur toute la série — aucune régénération).
- `assets/screen.mp4` = rush 1920×828, 25 fps, 28,48 s (`Envoyer_la_commande_en_cuisine.mp4`).

## Déroulé du rush (analyse frame-by-frame, `ffmpeg -vf fps=...`)

| t | Écran | Action |
|---:|---|---|
| 0,0–4,2 s | Commandes (Aujourd'hui) | Vue d'ensemble : filtres (À confirmer/Confirmées/En cuisine/Prêtes/Servies/Annulées), 3 commandes Web actives. CMD-2026-00100 en **« En attente »**. |
| ≈4,2 s | Commandes | **Clic sur « Confirmer »** (CMD-2026-00100). Bouton vert, bbox mesurée par seuillage couleur : centre (253, 637), taille 252×63 px. |
| 4,6–7,2 s | Commandes | Toast **« CMD-2026-00100 confirmée — envoyée en cuisine »**, badge passe à « Confirmée », barre de progression « Cuisine 0/2 » apparaît. |
| 7,4–14,2 s | **Écran KDS** (« KDS · GoSushi Démo », poste **Chaud**) | Coupure vers l'écran cuisine : tickets #100 et #101, plats détaillés, allergènes (GLUTEN, LAIT, POISSON…), minuteur par ticket, bouton « BUMP CHAUD ». |
| 14,4–19,5 s | Commandes | Retour à la liste : commande CMD-2026-00102 déjà passée « Prête » (toast), puis **clic sur « Prête »** pour CMD-2026-00101 (bbox ≈ centre (253, 670), 252×62 px). |
| 19,5–28,48 s | Commandes | Toast **« CMD-2026-00101 prête »**, filtres mis à jour : *0 À confirmer · 1 Confirmées · 2 Prêtes*. |

## Outil MCP FoodEatUp correspondant

`mcp__FoodEatUp__update_order_status(establishment_id, order_id, status)` — le statut
`confirmee` déclenche précisément l'envoi en cuisine montré dans la vidéo (le bump KDS
lui-même relève d'un autre outil, `update_kds_item_status`, non repris ici pour rester
sur l'action "cuisine" telle que titrée : *Envoyer en Cuisine en direct*).

Prompt proposé (identique vidéo + fiche Lovable) :

> Confirme la commande [numéro de commande] pour mon établissement FoodEatUp
> (ID [ID établissement]) afin de l'envoyer en cuisine.

Réponse assistant (mockup) : « Bien sûr ! Je confirme cette commande et je l'envoie en
cuisine… »

## Script voix off proposé (9 lignes, voix Adam FR `TGAegA0zNRi8I6nUdq3i`)

| # | Texte | Ancrage |
|---|---|---|
| N0 | Envoyer une commande en cuisine sur FoodEatUp&nbsp;? En un clic, c'est fait. | carte d'intro |
| N1 | Vos commandes du jour s'affichent ici, tous canaux confondus. | segment A — vue Commandes |
| N2 | Cliquez sur Confirmer pour l'envoyer directement en cuisine. | zoom-punch clic Confirmer |
| N3 | La commande passe en préparation, votre équipe est prévenue aussitôt. | toast "envoyée en cuisine" |
| N4 | Sur l'écran cuisine, chaque ticket affiche les plats, les allergènes et le temps écoulé. | écran KDS |
| N5 | Une fois prêtes, marquez les commandes en un clic&nbsp;: plus aucun oubli en salle. | zoom-punch clic Prête + toast |
| N6 | Vous pouvez aussi confirmer une commande depuis Claude&nbsp;: copiez ce prompt, remplacez les crochets. | séquence Claude — étage 1+2 (reveal + copié) |
| N7 | Collez-le dans la conversation&nbsp;: votre commande part en cuisine en quelques secondes. | séquence Claude — étage 3 (mockup chatbot) |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui&nbsp;! | carte de fin (CTA) |

## Découpage prévu (moteur standard de la série, `build.py`)

Intro (carte, ~3,8 s) → A (vue Commandes, banni "1 · Vos commandes du jour") → B
(zoom-punch Confirmer) → C (toast "envoyée en cuisine") → D (écran KDS, banni "2 ·
Réception en cuisine (KDS)") → E (retour Commandes, banni "3 · Suivi jusqu'à Prête",
zoom-punch clic Prête) → claude1/2/3 (séquence partagée `_shared/claude_prompt_sequence.py`)
→ outro CTA. Durées de segment calées sur la durée mesurée de chaque ligne VO une fois
l'audio généré (règle du workflow — jamais l'inverse).

---

**STOP validation — ne pas générer l'audio ElevenLabs ni monter la vidéo avant validation
explicite de ce script par Michael**, conformément à `FOODEATUP-TUTORIELS-WORKFLOW.md`.
