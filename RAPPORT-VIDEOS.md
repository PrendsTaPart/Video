# 📊 Rapport vidéos — état de production (2026-07-11)

## Mise à jour 2026-08-06

Nouveau tutoriel FoodEatUp Academy : **Configurer Caroline (voix & prompts)**
(`videos/foodeatup-caroline-voix-tuto/`) — premier du module `caroline-ia`
(0/6 → 1/6). Script + voix ElevenLabs (Adam FR) + montage + vignette, publié
sur RapidoCMS, programmé LinkedIn/Facebook FoodEatUp le 2026-08-21 07h
(rotation pleine jusqu'au 2026-08-20), et ajouté sur Lovable (remplace le
placeholder préexistant du module). Voir `videos/PROGRESSION-157-TUTORIELS.md`
pour le suivi 157 tutoriels et `videos/LOVABLE-FOODEATUP-DOCS.md` pour la
fiche complète.

## 1) Total réalisé
**~34 fichiers vidéo rendus** (≈ 25 contenus uniques, certains en 2 formats 16:9 + 9:16).

### A. Série « 30 routines » (TikTok 9:16) — **9 / 30**
✅ Faits : **E1→E9** (C'est quoi une routine, un MCP, le plugin, skills/agents, business plan, mémoire, prévisionnel, du plan aux tâches, prépare ma journée).

### B. Série « Rapido » (4 saisons × 7 = 28) — **2 / 28**
✅ Faits : **S1E1** (RapidoRH), **S1E2** (Recruté en Rapido).

### C. FoodEatUp — **~17 fichiers**
✅ Modules (16:9 **+** 9:16) : **HACCP, Équipe/Planning, StockVision, Compta, Configurateur, Caroline, Promo** (7×2=14) · **Teaser** (1) · **Tuto 5 min vertical** (1) · **Tutoriel 5 min 16:9** (1).

### D. RapidoCMS / BraindCode — **6 fichiers**
✅ **Carousel RapidoCMS** (standard + TikTok), **Carousel Calendrier**, **Carousel Éditeur**, **Formation écosystème 5 min**, **MCP Claude en 3 étapes**.

---

## 2) À réaliser (manquant)

### 🔴 Série « 30 routines » — **21 manquantes**
E10 Le brief du lundi · E11 Trouve 20 prospects · E12 Le cold email · E13 Où en sont mes deals · E14 Récupère ton argent · E15 Un mois de contenu · E16 Le post parfait · E17 L'article qui ranke · E18 Ta 1re pub · E19 Ce qui marche · E20 Fais parler tes clients · E21 La sentinelle cash · E22 Ton CFO du lundi · E23 Les 3 chiffres · E24 Combien vaut un client · E25 Recrute sans te tromper · E26 L'arrivée parfaite · E27 Qui est en surchauffe · E28 Automatise sans IA · E29 Le board pack · E30 L'entreprise qui tourne seule.

### 🔴 Série « Rapido » — **26 manquantes**
- **S1 (RapidoRH)** : E3 Onboardé · E4 Le projet monté · E5 Le daily · E6 Agenda & congés · E7 La semaine RH bouclée (5)
- **S2 (RapidoCMS)** : E1→E7 (contenu, visuel, calendrier, publié, carte digitale, brand-review, perf) (7)
- **S3 (RapidoCRM)** : E1→E7 (vente, prospecté, pipeline, facturé, campagne, client relancé, perf co) (7)
- **S4 (Orchestration)** : E1→E7 (écosystème, client 360, lundi briefé, impayés, CODIR, automatisé n8n, grand final) (7)

### 🟠 FoodEatUp — **7 shorts** (plan prêt, `videos/foodeatup-tutoriel-5min/shorts-plan.md`)
1 short vertical par phase (compte, fondations, MCP, contenu IA, RH, HACCP, exploitation).

**➡️ Total à produire ≈ 54 vidéos** (21 + 26 + 7), hors variantes.

---

## 3) État de publication RapidoCMS
- **151 posts planifiés** au calendrier (déc. 2025 → 31/07/2026), majorité **texte/image** (calendrier marketing).
- **Nos vidéos rendues** sont **peu/pas** planifiées comme posts vidéo sur les comptes cibles :
  - LI RapidoSoftware `101119107` : 4 posts · LI FoodEatUp `68807312` : 40 (marketing) · LI Michael `6Z5izYBhkC` : **1** · FB RapidoSoftware : 5 · FB FoodEatUp : 3.
- ✅ Pipeline d'upload validé : dépôt public → URL raw → `upload_file_tool` → S3 → prêt pour `create_draft` + `schedule`.

## 3bis) Publication réalisée aujourd'hui (2026-07-11)
✅ **Bibliothèque RapidoCMS** : **25 vidéos uploadées** (fe-*, carousel-*, rapido-*, mcp-claude, serie30-e01→e09).
✅ **Planifié à 17:00 (LinkedIn FoodEatUp `68807312` + Facebook FoodEatUp `201499969703551`)** — 8 vidéos, 1/jour :
| Date | Vidéo | Posts |
|------|-------|-------|
| 11/07 | Tutoriel 5 min | LI #345 · FB #346 |
| 12/07 | HACCP | LI #347 · FB #349 |
| 13/07 | Équipe RH | LI #350 · FB #351 |
| 14/07 | StockVision | LI #352 · FB #353 |
| 15/07 | Compta & Factures | LI #354 · FB #355 |
| 16/07 | Configurateur Carte | LI #356 · FB #357 |
| 17/07 | Cas Caroline | LI #358 · FB #359 |
| 18/07 | Promo | LI #360 · FB #361 |

= **16 posts vidéo planifiés**, tous avec hook + présentation.

### ⛔ Bloqueurs (le reste n'a PAS pu être planifié)
1. **Compte RapidoCMS expire le ~18/07/2026** : toute date **≥ 19/07 est refusée** (« date supérieure à la date d'expiration »). → Bloque : **FoodEatUp Teaser** + **les 16 vidéos RapidoSoftware/BraindCode** (carousels, formation, mcp-claude, Rapido S1E1/E2, Série-30 E1→E9). **Action : renouveler le compte**, je planifie ensuite tout le reste, 1/jour à 17h.
2. **LinkedIn Michael Kebail** (`6Z5izYBhkC`, profil perso) : `create_draft_tool` refuse l'ID (« account id field must be a number »). Les profils LinkedIn (non numériques) ne sont pas planifiables via cet outil. **Action : fournir un ID numérique / publication manuelle**, ou confirmer qu'on reste sur les pages (LI+FB) par marque.
3. Orphelin : post FB HACCP **#348** (25/07) — doublon non supprimable via l'outil (erreur Graph API), ne publiera pas (date > expiration). À retirer manuellement.

## 4) Comptes cibles (connectés, actifs)
| Marque | LinkedIn | Facebook | Profil perso |
|---|---|---|---|
| RapidoSoftware | `101119107` | `223318770858972` | — |
| FoodEatUp | `68807312` | `201499969703551` | — |
| Michael Kebail | — | — | `6Z5izYBhkC` (linkedin_profile) |
