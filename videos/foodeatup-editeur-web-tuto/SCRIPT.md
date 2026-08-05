# Tutoriel — Activer l'abonnement Éditeur de site (module « Site Web & Vitrine », 01/08)

**Statut : PUBLIÉ (2026-08-05).** Validation explicite de Michael reçue en cours de
session ("tu peux publier"). Livrable final : `out/foodeatup-editeur-web-tuto-v1.mp4`
(34,28 s, H.264 High/yuv420p, AAC 48kHz stéréo, faststart, peak -7,3 dBFS).

## Publication

- **RapidoCMS** : vidéo `fe-editeur-web-tuto`, vignette `fe-editeur-web-tuto-thumb`
  (`https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/...`).
- **Lovable** (`project_id 55ff35b7-c442-42c4-950c-8c7fd420c645`, `src/data/tutorials.ts`) :
  slug final `activer-abonnement-editeur-web` (renommé par l'agent Lovable depuis
  `activer-labonnement-editeur-web` proposé — correction grammaticale bienvenue),
  module `site-web-vitrine`, `order: 1`, section "Activer l'éditeur". Les 7 autres
  vidéos du module (order 2 à 8) avaient été publiées entre-temps par d'autres
  sessions en parallèle — le module est maintenant complet (8/8).
- **GitHub** : commit sur `claude/foodeatup-video-tutorials-mgemxu` (assets, vo/,
  build.py, out/).
- LinkedIn / RapidoCMS planning social : non fait (non demandé explicitement pour
  cette vidéo).

Rush fourni : `assets/screen.mp4` (16,88 s, 1920x828, 25 fps, H.264/AAC).
Intro card : `assets/intro.jpg` (« ACTIVER L'ÉDITEUR WEB »).
Outro card : `assets/outro.jpg` — identique (même poids fichier, 174 269 o) à l'outro déjà
réutilisée sur `foodeatup-abonnement-tuto` et les tutos suivants : pas de redesign, réemploi tel quel.

## Déroulé du rush (analyse par extraction de frames, contact sheets 2 fps)

| t | Écran |
|---:|---|
| 0,0 → 3,5 s | Page **Abonnement** : plan actuel (StockVision + OCR + Prédiction + HACCP), prochaine facturation |
| 3,5 → 6,0 s | Scroll vers les **packs** (StockVision seul / +OCR+HACCP / 99€) |
| 6,0 → 8,0 s | Scroll vers **Options & modules** : cartes Éditeur de site IA (29€/mois), Jarvis (49€/mois), Marketing & Commercial (99€/mois) |
| ≈ 8,5 s | **Clic** « Ajouter cette option » sous la carte **Éditeur de site IA** |
| 9,0 → 12,5 s | Modal **« Changer de plan »** : Plan Éditeur de site IA, 29,00€, Total 29,00€, champ code promo |
| ≈ 12,8 s | **Clic** « Continuer vers le paiement » |
| 13,5 → 14,5 s | Transition / chargement |
| 14,5 → 16,88 s | **Stripe checkout** : « S'abonner à Éditeur de site IA — 29,00€/mois » puis écran **« Confirmez votre identité »** (code par SMS) — le rush s'arrête ici (dernière frame noire), avant l'écran de confirmation finale |

⚠️ **Point d'attention** : contrairement à `foodeatup-abonnement-tuto` (qui allait jusqu'à
« Abonnement activé ! »), ce rush coupe en plein flux Stripe, avant la confirmation. Parti
sur l'option **« pas d'écran de succès inventé »** (même règle déjà appliquée sur
`foodeatup-recettes-tuto`, cf. `LOVABLE-FOODEATUP-DOCS.md`) : la vidéo se termine sur l'étape
de vérification d'identité, avec une ligne VO qui annonce le résultat sans montrer un écran
qu'on n'a pas capturé. À confirmer avec Michael — sinon fournir la suite du rush.

## Proposition de script VO (voix Adam FR ElevenLabs, `TGAegA0zNRi8I6nUdq3i`, même ton que les tutos précédents)

| # | Texte | Durée cible | Placement |
|---|---|---:|---|
| N0 | Pour créer et personnaliser votre site, activez d'abord l'option Éditeur de site IA. | ~4,5 s | carte d'intro |
| N1 | Depuis votre Abonnement, ouvrez la section Options & modules. | ~3,2 s | scroll options |
| N2 | Cliquez sur Ajouter cette option, sous Éditeur de site IA à 29€ par mois. | ~4,0 s | clic zoom-punch |
| N3 | Le récapitulatif s'affiche : 29€, facturation mensuelle. | ~3,0 s | modal Changer de plan |
| N4 | Cliquez sur Continuer vers le paiement. | ~2,5 s | clic zoom-punch |
| N5 | Confirmez votre identité avec le code reçu, puis validez votre moyen de paiement. | ~4,5 s | Stripe / vérification |
| N6 | Une fois validé, votre éditeur de site est activé et prêt à personnaliser votre vitrine. | ~4,0 s | bénéfice |
| N7 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | ~5,0 s | carte de fin (CTA) |

Pas de séquence Claude 3-temps (« Reveal / Copié / Chatbot ») : aucun outil `mcp__FoodEatUp__*`
ne couvre l'activation d'un abonnement/option de facturation — cohérent avec la règle du
workflow (ne pas fabriquer de prompt Claude, cf. `foodeatup-contrat-tuto`,
`foodeatup-notifications-tuto`, etc., même cas).

## Fiche Lovable (draft, `src/data/tutorials.ts`, module `site-web-vitrine`)

- `slug`: `activer-son-abonnement-editeur-web`
- `howItWorks`: ["Ouvrez Abonnement puis Options & modules", "Cliquez sur Ajouter cette option sous Éditeur de site IA (29€/mois)", "Vérifiez le récapitulatif (29€, facturation mensuelle) et cliquez sur Continuer vers le paiement", "Confirmez votre identité et validez votre moyen de paiement"]
- `whatItsFor`: "Débloquer l'éditeur de site pour créer et personnaliser votre vitrine en ligne vous-même."
- `chefTip`: à rédiger — piste : rappeler que cette option s'ajoute au pack principal sans le remplacer, et que le premier mois inclut souvent un essai gratuit (à vérifier sur l'écran réel avant de l'affirmer).
- `claudePrompt`: absent (pas d'outil MCP correspondant).

## Prochaine étape

**STOP obligatoire (règle du projet, voir `FOODEATUP-TUTORIELS-WORKFLOW.md` et
`LOVABLE-FOODEATUP-DOCS.md`)** : ne pas générer l'audio ElevenLabs ni monter la vidéo tant que
ce script n'est pas validé par Michael. Après validation (ou ajustements demandés), passage
au montage `build.py`, puis nouvelle validation obligatoire sur le rendu final avant toute
publication (Lovable, GitHub, RapidoCMS, LinkedIn).
