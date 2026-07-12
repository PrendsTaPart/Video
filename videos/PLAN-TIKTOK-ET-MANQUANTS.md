# Plan TikTok + vidéos manquantes — état au 2026-07-11 (17h35 UTC)

Demande de Michael : « continue toutes les vidéos au format tiktok et ajoute et planifie
les vidéos manquantes ». État des lieux, actions faites, et plan prêt à exécuter.

## 🔴 Deux blocages de compte confirmés par test (2026-07-11)

1. **TikTok** — `create_draft_tool` (tiktok, account_id 5 = BraindCode, seul compte TikTok
   connecté) → **refusé** : « account_id invalide : ce compte n'existe pas pour ce réseau ou
   n'appartient pas au propriétaire du token » (statut `expired` dans
   `list_connected_accounts`). **Aucun brouillon ni post TikTok possible** tant que le compte
   TikTok n'est pas ré-autorisé dans RapidoCMS avec permission de publication.
2. **BUG RapidoCMS — contrôle d'expiration figé au 18/07/2026** (≠ vraie expiration).
   `schedule_draft_tool` refuse toute `post_date ≥ 2026-07-19` : « La date choisie est
   supérieure à la date d'expiration de votre compte ». **Ce n'est PAS l'abonnement** :
   Michael confirme une expiration réelle au **2027-06-28**.
   Caractérisation (tests 2026-07-12, compte 321) :
   - `2026-07-18 08:00` → **accepté** (post créé puis annulé pour ne pas doubler E8).
   - `2026-07-19 08:00` → **refusé**.
   - `2027-06-01` (avant l'expiration réelle) → **refusé** aussi.
   - Coupure **fixe** au 2026-07-18 (identique les 11 et 12/07 → pas une fenêtre glissante).
   - Incohérence prouvant le bug : des posts sont **déjà planifiés 2026-07-20 → 07-31**
     dans le système (série BraindCode S1/S2, ids 310→329, statut=0). Le compte héberge
     donc des posts au-delà du 18/07, mais l'endpoint de création les refuse.
   - Hypothèse pour l'équipe RapidoCMS : la validation compare `post_date` à un champ
     interne périmé (fin d'essai / date de token non mise à jour au renouvellement),
     au lieu de la vraie date d'abonnement (2027-06-28). **À corriger côté backend.**
   - Impact : **impossible de planifier après le 18/07** (E9→E30 série-30, stories S08+,
     vague TikTok, tutoriel 5 min) tant que le champ n'est pas corrigé.

## ✅ Fait aujourd'hui (dans la fenêtre encore ouverte)

| Action | Détail |
|---|---|
| Teaser FoodEatUp planifié | LinkedIn FoodEatUp (draft 454 → post **380**) + Facebook FoodEatUp (draft **478** créé → post **381**), **18/07 12:00** — dernier créneau avant expiration |
| Brouillons Stories S08–S10 créés | S08 Ingrédients (IG **470** / FB **471**), S09 Recettes & food cost (IG **473** / FB **474**), S10 Composer ma carte (IG **476** / FB **477**) — contenu vérifié image par image ; cibles : 19, 20, 21/07 à 17:00 (FB) / 17:10 (IG) **après renouvellement** |
| Verticales manquantes uploadées | `FoodEatUp - Comptabilite (TikTok vertical)` et `FoodEatUp - Configurateur (TikTok vertical)` ajoutées à la bibliothèque CMS (depuis les rendus 9:16 du repo). `fe-teaser` est déjà vertical 1080×1920 |
| État série-30 mis à jour | `serie-30-routines/serie-etat.json` : blocages re-testés et datés |

## 📋 À exécuter dès le renouvellement RapidoCMS (avant/au 18/07 !)

1. `schedule_draft_tool(437, 2026-07-19, 08:00:00)` — série-30 **E9** LinkedIn BraindCode.
2. Stories : `schedule_draft_tool` → 471 (19/07 17:00), 470 (19/07 17:10), 474 (20/07 17:00),
   473 (20/07 17:10), 477 (21/07 17:00), 476 (21/07 17:10).
3. Reprendre la production **E10→E30** série-30 (`auto_loop.reprise`) — nécessite aussi
   `HEYGEN_API_KEY` (absent de cet environnement, `.env` non commité).

## 📋 Vague TikTok — prête à lancer dès ré-autorisation du compte TikTok

Toutes les vidéos verticales 1080×1920 disponibles en bibliothèque CMS. Proposition :
1 post/jour à 18:00 (Europe/Paris), compte TikTok BraindCode (seul connecté — confirmer si
un compte TikTok FoodEatUp doit être ajouté pour les contenus FoodEatUp).

| Ordre | Vidéo (bibliothèque CMS) | Série |
|---|---|---|
| 1 | FoodEatUp - Promo (TikTok vertical) | FoodEatUp modules |
| 2 | FoodEatUp - HACCP (TikTok vertical) | FoodEatUp modules |
| 3 | FoodEatUp - Equipe Planning (TikTok vertical) | FoodEatUp modules |
| 4 | FoodEatUp - StockVisionAI (TikTok vertical) | FoodEatUp modules |
| 5 | FoodEatUp - Comptabilite (TikTok vertical) | FoodEatUp modules |
| 6 | FoodEatUp - Configurateur (TikTok vertical) | FoodEatUp modules |
| 7 | FoodEatUp - Caroline (TikTok vertical) | FoodEatUp modules |
| 8 | fe-teaser | FoodEatUp |
| 9–17 | Serie 30 routines - E1 … E9 | série-30 (1/jour) |
| 18 | Rapido S1E1 - RapidoRH (TikTok) | série Rapido |
| 19 | Rapido S1E2 - Recruté en Rapido (TikTok) | série Rapido |
| 20–29 | story-s01 … story-s10 | stories 30 jours FoodEatUp |

Captions : reprendre celles des brouillons LinkedIn/FB homologues (déjà rédigées, hashtags
à adapter TikTok). Les épisodes suivants de chaque série rejoignent la file au fil de la prod.

## ⛔ Production bloquée (hors planification)

- **Série-30 E10→E30** et **série Rapido S1E3→S4E7** : nécessitent `HEYGEN_API_KEY` /
  `ELEVENLABS_API_KEY` (absents de ce clone).
- **Tutoriel FoodEatUp 5 min** : en attente de validation du plan (PR #2) + clé HeyGen.
