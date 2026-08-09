# 02 — ÉPISODE 1 : « LA RENTRÉE »
## La Brigade Végéfruitée × FoodEatUp — 40 secondes

---

## Structure de production

| Bloc | Durée | Timecode | Fabriqué par | Format natif |
|---|---|---|---|---|
| **Thumbnail / cover** | fixe | — | RapidoCMS `generate_image` (Claude Code) | 1080×1350 + 1080×1920 |
| **A — HOOK** | 10 s | 00:00 → 00:10 | **Higgsfield / Seedance — VOUS, à la main** | 9:16 |
| **B — CORPS** | 15 s | 00:10 → 00:25 | **Higgsfield / Seedance — VOUS, à la main** | 9:16 |
| **C — MOTION DESIGN** | 15 s | 00:25 → 00:40 | Remotion (Claude Code) | 9:16 |
| **Voix off FR** | 40 s | continue | ElevenLabs (Claude Code) | — |

> **Pourquoi le corps fait 15 s et pas 24 s.** Seedance 2.0 plafonne à 15 s ; Seedance 2.5 monte à 30 s mais sa disponibilité publique sur Higgsfield est encore inégale selon les comptes. **15 s tourne partout.** Une variante 24 s est fournie dans le doc 03 si votre compte a bien la 2.5 active.

---

## Décision de production n°1 : PAS de lip-sync

Les personnages ne parlent **jamais** en gros plan. Trois raisons :

1. Seedance génère du mouvement de bouche approximatif → un doublage français par-dessus se voit immédiatement.
2. Vous voulez la voix ElevenLabs — donc la voix doit être **libre** du timing image.
3. 85 % des vues Reels/LinkedIn se font **son coupé**. Les punchlines doivent être lisibles à l'écran de toute façon.

**Conséquence :** dialogues joués en plan large / mi-large, gestuelle expressive, et **sous-titres animés** brûlés au montage. La voix off de Navy porte le récit.

---

## BLOC A — HOOK (00:00 → 00:10)

**Intention :** installer le désastre en 3 secondes, retenir en 10.

**Plan 1 (0–5 s)** — Cuisine morte, premier matin de septembre. Housses de protection sur le pass, un néon qui clignote, calendrier bloqué sur juillet, herbes fanées, cagettes fournisseur non ouvertes contre la porte de service. Tom, seul au centre, **fixe l'objectif**, impassible. Il tire lentement la housse du pass — un nuage de poussière monte dans les rais de lumière. Il ne cligne pas des yeux. Derrière lui, hors focus, quelque chose de métallique tombe.

**Plan 2 (5–10 s)** — Whip-pan à gauche puis retour sec sur Tom en gros plan. Il lève un doigt. Derrière lui la cuisine explose : cagettes qui basculent, alarme, silhouettes qui courent en panique.

### Voix off
| TC | Voix | Texte |
|---|---|---|
| 00:00,5 | Navy | *1ᵉʳ septembre. 8h02. Le restaurant rouvre.* |
| 00:04,0 | Navy | *Lui, c'est Tom. Il pense que ça va bien se passer.* |
| 00:08,0 | Navy | *Il a tort.* |

### Sous-titre à l'écran
`8h02. Premier jour.` puis `Il a tort.` (gros, blanc `#FFFFFF`, ombre portée)

---

## BLOC B — CORPS (00:10 → 00:25)

**Intention :** le chaos choral — un module FoodEatUp par plan — puis le retournement.

**Plan 1 (10–12 s)** — Plan large de la cuisine en pleine panique. Ail & Oignon franchissent la porte de service avec des cagettes manifestement fausses, Oignon agitant un bon de livraison chiffonné. Betterave traverse le cadre en trottinette, plateau vide. *(gag visuel de fond)*

**Plan 2 (12–14,5 s)** — Mama Batata, sac à main au bras, téléphone coincé à l'oreille, tient trois torchons et un classeur ; un planning mural vide se décroche derrière elle et tombe.

**Plan 3 (14,5–17 s)** — Rott-K ouvre une chambre froide : un souffle de vapeur froide, elle recule d'un pas, tourne lentement la tête **vers l'objectif** une demi-seconde, puis referme la porte.

**Plan 4 (17–20 s)** — Firase filme tout au selfie stick en tournant sur elle-même, radieuse, pendant que tout s'effondre autour. Don Citrone entre en salle, regarde sa montre, ressort.

**Plan 5 (20–25 s)** — **Le retournement.** Tout le monde se fige. Contre-plongée lente sur Brocoli, immobile au fond, tablette à deux mains, **le visage éclairé en bleu `#147AFF`**. Elle lève les yeux. Le chaos s'arrête. Tom traverse le cadre, prend la tablette. La lumière bleue se répand sur le pass en cuivre — le chaud et le froid se rencontrent. Dernier plan : la brigade entière, alignée, immobile, éclairée bleu.

### Voix off
| TC | Voix | Texte |
|---|---|---|
| 00:10,5 | Navy | *Le stock a fondu. Le planning est vide. Les résas de septembre sont… quelque part.* |
| 00:15,0 | Navy | *Ail et Oignon ont livré la mauvaise commande. Carotte a trois semaines de relevés en retard.* |
| 00:19,5 | Navy | *Et Brocoli n'a toujours rien dit.* |
| 00:21,5 | **Brocoli** | *Et si vos données bossaient pour vous, plutôt que l'inverse ?* |

### Sous-titres à l'écran (pastilles module, bleu `#147AFF`)
`STOCK` → `PLANNING` → `HACCP` → `RÉSAS` → *(silence)*

---

## BLOC C — MOTION DESIGN (00:25 → 00:40)

Fond `#0B0B0F`. Typo blanche. Accent `#147AFF`. Zéro image générée — c'est du Remotion, donc net, propre, et **modifiable sans re-générer**.

| TC | À l'écran | Voix off (Navy) |
|---|---|---|
| 25,0 → 26,0 | Logo FoodEatUp qui s'allume en bleu sur noir | — |
| 26,0 → 31,0 | 6 pastilles qui claquent en cascade : **STOCK · ÉQUIPE · HACCP · RÉSAS · CAISSE · AVIS** puis fusionnent en un seul rectangle | *FoodEatUp. Le stock, l'équipe, l'hygiène, les résas, la caisse, les avis. Un seul écran.* |
| 31,0 → 34,0 | Bloc chiffres, **uniquement si sourcés** : `{{CA_MOIS}}` · `{{COUVERTS}}` · `{{RUPTURES_EVITEES}}` | *L'IA lit tes chiffres.* |
| 34,0 → 37,0 | Grande accroche : **« TU REPRENDS LE CONTRÔLE. »** | *Tu reprends le contrôle.* |
| 37,0 → 39,0 | CTA : **« La rentrée, c'est maintenant → foodeatup.com »** | *La rentrée, c'est maintenant.* |
| 39,0 → 40,0 | **Betterave traverse en trottinette de droite à gauche et efface la ligne de CTA — le logo reste.** Puis carton : *La suite au prochain épisode.* | *La suite… au prochain épisode.* |

> Le gag de Betterave qui efface le texte est **repris à l'identique de votre scénario 2021** (où c'était Courge). C'est la signature de fin de la série — elle doit être dans **tous** les épisodes.

---

## Script voix off complet — à donner à ElevenLabs

Fichier machine : `voix/ep01.voix.json` (généré par le pipeline).

```
[NAVY]  1er septembre. 8h02. Le restaurant rouvre.
[NAVY]  Lui, c'est Tom. Il pense que ça va bien se passer.
[NAVY]  Il a tort.
[NAVY]  Le stock a fondu. Le planning est vide. Les résas de septembre sont… quelque part.
[NAVY]  Ail et Oignon ont livré la mauvaise commande. Carotte a trois semaines de relevés en retard.
[NAVY]  Et Brocoli n'a toujours rien dit.
[BROCOLI]  Et si vos données bossaient pour vous, plutôt que l'inverse ?
[NAVY]  FoodEatUp. Le stock, l'équipe, l'hygiène, les résas, la caisse, les avis. Un seul écran.
[NAVY]  L'IA lit tes chiffres.
[NAVY]  Tu reprends le contrôle.
[NAVY]  La rentrée, c'est maintenant.
[NAVY]  La suite… au prochain épisode.
```

**Direction de jeu ElevenLabs**
- **NAVY** — grave, complice, pince-sans-rire, tempo lent. *Stability 0.45 / Similarity 0.80 / Style 0.35.* Marquer une vraie pause avant « Il a tort. »
- **BROCOLI** — neutre, calme, presque monocorde, aucune emphase. *Stability 0.75 / Similarity 0.85 / Style 0.10.* C'est le contraste qui fait la réplique.

---

## Règle chiffres (non négociable)

`{{CA_MOIS}}`, `{{COUVERTS}}`, `{{RUPTURES_EVITEES}}` sont remplis par le pipeline depuis le MCP FoodEatUp (`finance_summary`, `get_daily_brief`, `list_low_stocks`).

**Si une valeur est absente, le pipeline supprime le carton — il ne l'invente pas.** Un chiffre non sourcé dans une communication commerciale française, c'est une pratique commerciale trompeuse (art. L.121-2 du Code de la consommation).
