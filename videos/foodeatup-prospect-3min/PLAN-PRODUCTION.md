# FoodEatUp — Vidéo prospect « 4 IA » (16:9, cible 3 min)

Analyse du script `script/script-source-v1.md` + plan de production, à valider avant
toute génération de voix (règle étape 3 de `videos/FOODEATUP-TUTORIELS-WORKFLOW.md`).

---

## 1. Diagnostic du script

### 1.1 Le point bloquant : la voix off ne remplit que la moitié du temps

216 mots de voix off au total. À un débit publicitaire naturel français (~155 mots/min,
le débit d'Adam sur les autres vidéos du dépôt), ça donne :

| Scène | Mots | VO estimée | Slot annoncé | Silence à combler |
|---|---:|---:|---:|---:|
| S1 Accroche | 35 | ~13 s | 15 s | 2 s ✅ |
| S2 Présentation | 29 | ~11 s | 15 s | 4 s ✅ |
| S3 IA Commandes | 27 | ~10 s | 30 s | **20 s** ⚠️ |
| S4 IA Cuisine | 32 | ~12 s | 30 s | **18 s** ⚠️ |
| S5 IA Pilotage | 28 | ~11 s | 30 s | **19 s** ⚠️ |
| S6 IA Réseaux sociaux | 50 | ~19 s | 45 s | **26 s** ⚠️ |
| S7 Clôture | 15 | ~6 s | 15 s | 9 s ⚠️ |
| **Total** | **216** | **~83 s** | **180 s** | **~97 s** |

Autrement dit : en l'état, le script fait **1 min 25 de parole pour 3 min de vidéo**.
Deux issues possibles, il faut trancher :

- **Option A — « serré » (~1 min 45 – 2 min).** On garde le texte tel quel, on monte
  serré sur les démos écran. C'est le format le plus efficace en prospection froide
  (LinkedIn/site : le taux de complétion s'effondre après 90 s).
- **Option B — « 3 min tenues ».** On garde la durée cible, mais il faut **~95 s de
  matière en plus** : soit 2-3 phrases de VO supplémentaires par scène (bénéfice chiffré,
  objection levée), soit des séquences de démonstration écran commentées, soit un
  témoignage client. Je peux écrire ces lignes en plus, mais ça reste ton arbitrage
  éditorial. **Recommandation : Option A**, plus une version 30-45 s pour les réseaux.

### 1.2 Corrections de texte à faire avant enregistrement

1. S1 : « les cartes à mettre **à jours** » → « à jour ».
2. S3 : « **Plus d'erreurs, plus d'attente** » — à l'oral, la liaison rend la phrase
   ambiguë (on entend « plusse d'erreurs » = *davantage* d'erreurs). Proposition :
   « **Fini les erreurs. Fini l'attente.** Même en plein coup de feu. »
3. S2/S6 : « 4 intelligences artificielles » puis « IA Commandes / IA Cuisine / IA
   Pilotage / IA Réseaux sociaux » — il faut le **nommage officiel produit** (dans le
   dépôt les briques existantes s'appellent *Jarvis*, *PrédiBot*, *StockVision*…).
   Soit on aligne le script sur les noms produit, soit on assume des noms génériques,
   mais pas les deux à moitié.
4. S6 : le texte à l'écran dit « en un clic », la VO dit « d'un geste » et « en quelques
   secondes » → harmoniser une seule promesse.
5. Notes de prod : les chiffres suggérés (« -30 % de gaspillage », « +X h/semaine ») ne
   doivent être affichés que **s'ils sont sourçables** (mesure client, étude interne) —
   sinon c'est une allégation risquée sur une vidéo commerciale.

### 1.3 Points produit à confirmer (impact direct sur le tournage écran)

| Promesse du script | Ce que je vois dans le dépôt / le connecteur | À confirmer |
|---|---|---|
| Prise de commande **au téléphone** par IA | aucune capture, aucun tuto | La fonction existe-t-elle en prod ? |
| Commande **borne** | ✅ `videos/foodeatup-borne-tuto/assets/screen.mp4` | — |
| Commande **en ligne** | ✅ `foodeatup-boutique-tuto`, `foodeatup-vitrine-tuto` | — |
| IA cuisine (stocks/DLC/fournisseurs/plannings/RH) | ✅ 6 captures réelles disponibles | — |
| Pilotage **par WhatsApp** | Jarvis existe (`foodeatup-jarvis-tuto`) mais c'est l'assistant **in-app** ; côté API je ne vois que des *templates* WhatsApp | Le Q/R temps réel sur WhatsApp est-il livré ? |
| IA réseaux sociaux (alerte stock → recette → carte → campagne) | Les briques existent côté API (`propose_campaigns`, `launch_campaign`, `update_dish`) mais **aucune capture écran** du parcours complet | Le parcours en un clic existe-t-il tel quel à l'écran ? |

C'est le point le plus important : **la scène 6 est le clou du spot et c'est justement
celle dont je n'ai aucune image**.

---

## 2. Ce qui est déjà réutilisable dans le dépôt (rien à racheter)

- **17 plans b-roll restaurant** (Higgsfield, 1280×720, 24 fps) — `hero-video/assets/video/`
  (chef, serveur, directeur cohérents entre les plans, personnages déjà « castés »).
- **+31 plans 16:9 jamais rapatriés** repérés dans la bibliothèque Higgsfield (404 vidéos au
  total) — sélection et liens dans `HIGGSFIELD-PLANS.md`, index complet dans
  `higgsfield-index.json`. Plusieurs collent au script au mot près (pass saturé avec les trois
  tablettes et le téléphone qui vibre, notifications qui s'empilent, « il valide d'un geste »,
  générique logo 5 s).
- **~70 captures écran réelles du produit** en 1920×828 — `videos/foodeatup-*-tuto/assets/screen.mp4`.
- **Charte + logos officiels** — `videos/shared-images/brand/` (mascotte, mark, horizontal),
  bleu `#007BFF`/`#147AFF`, orange `#FFA500`, crème `#FCF9E6`, encre `#0F1A23`.
- **Typo** : Poppins 400/600/700/800 (`videos/rapidocms-presentation-4min/assets/fonts/`).
  La police de marque **Goodly n'est pas dans le dépôt** (substitut Poppins/Fredoka).
- **Musique** : `videos/stories-foodeatup-30j/audio/bgm.mp3` (piste studio déjà utilisée)
  + `hero-video/assets/music/` (3 pistes IA « tension / résolution » — placeholders).
- **SFX** : 16 sons dans `hero-video/assets/sfx/` (notification, validation, scanner, cloche…).
- **Moteur de montage** : pipeline Python + ffmpeg déjà éprouvé
  (`videos/foodeatup-demo-generale/build_seqs.py` + `build_final.py`), 1920×1080, 30 fps,
  VO ElevenLabs, loudnorm par ligne, cartes typo, Ken Burns, sous-titres incrustés.
  ffmpeg a été installé dans cet environnement, le rendu est donc faisable ici.

---

## 3. Découpage technique proposé (scène par scène)

> Les plans Higgsfield candidats, scène par scène, sont listés dans `HIGGSFIELD-PLANS.md`.

| # | Visuel | Source | État |
|---|---|---|---|
| S1 | Rush : gérant aux 7 onglets, serveur aux 3 tablettes, brigade en cuisine, carnet DLC | `hero-directeur-sept-onglets`, `hero-serveur-trois-tablettes`, `hero-brigade-deux-langues`, `hero-chef-carnet-dlc` | ✅ dispo |
| S1 | Post-it « TOMATES – PÉREMPTION J-3 » + Instagram « il y a 15 jours » | incrustation motion design par-dessus le plan frigo | 🟡 à fabriquer |
| S2 | Le gérant souffle + sting logo | `hero-portrait-directeur` + `foodeatup-mark-eight.png` | ✅ dispo |
| S3 | Split 3 canaux → écran cuisine | borne ✅ / en ligne ✅ / **téléphone ❌** ; KDS : `hero-kds-mural` | 🟡 1 canal manquant |
| S4 | Alerte rupture → commande fournisseur → planning | `predibot-tuto`, `dlc-tuto`, `commande-fournisseur-tuto`, `planning-poste-tuto`, `employes-tuto` | ✅ dispo |
| S5 | Conversation WhatsApp (2 questions / 2 réponses) | **aucune capture** → mockup animé (bulles, frappe, réponse chiffrée) | 🟡 à fabriquer |
| S6 | Alerte stock → recette suggérée → carte à jour → campagne IG/FB | **aucune capture** → mockup animé en 4 temps | 🟡 à fabriquer |
| S7 | Gérant serein en salle + carte logo + CTA | `hero-serveur-place-client`, `hero-portrait-chef`, logo | ✅ dispo (manque le lien RDV) |

Les mockups (🟡) sont **cohérents avec tes notes de production** (« interfaces IA en
mockups épurés ») : je les fabrique en motion design aux couleurs de la charte, sans
appeler Higgsfield (règle du dépôt : aucune nouvelle génération vidéo).

---

## 4. Ce dont j'ai besoin de toi

### 4.1 Décisions (bloquantes — 5 réponses courtes suffisent)

1. **Durée** : Option A serrée (~1 min 45) ou Option B (3 min, j'écris ~95 s de VO en plus) ?
2. **Formats livrés** : 16:9 seul, ou 16:9 + 9:16 (+ éventuellement un cut 30 s pour la pub) ?
3. **Voix off** : Adam FR (`TGAegA0zNRi8I6nUdq3i`, celle des autres vidéos FoodEatUp) ou
   une voix féminine (Anaïs `5OnMHwgTFgvPVwE8jP6B`, déjà utilisée en narration) ?
4. **Sous-titres incrustés** oui/non (recommandé : oui, LinkedIn/Meta se regardent sans son).
5. **Nommage des 4 IA** : noms génériques du script, ou noms produit (Jarvis, PrédiBot…) ?

### 4.2 Éléments à me fournir

6. **Le lien exact de prise de RDV** (+ un QR code si tu veux l'afficher) — le script dit
   « [lien / contact] ».
7. **Les chiffres de preuve** si tu en veux (scène 6/7) et leur source.
8. **La police Goodly** (`.woff2`/`.ttf`) si tu l'as ; sinon je reste sur Poppins.
9. **La musique** : je pars sur `bgm.mp3` du studio, sauf si tu as une piste sous licence
   pour un usage publicitaire (le script demande une montée en tension puis un apaisement —
   ça peut demander 2 pistes ou une piste avec un vrai break).
10. **3 enregistrements d'écran manquants** (format habituel : 1920×828, sans son) :
    - la prise de commande **par téléphone** (si la fonction existe) ;
    - une **conversation WhatsApp** de pilotage (2 questions / 2 réponses, données réelles ou démo) ;
    - le parcours **alerte stock → recette promo → carte mise à jour → campagne publiée**.
    ➡️ Si ces écrans n'existent pas encore, dis-le moi : je les fabrique en **mockups animés**
    (c'est jouable et propre), mais il faut alors valider que la vidéo montre une interface
    de démonstration et pas une capture produit.

### 4.3 Technique

11. **Clé ElevenLabs** : le dépôt attend `ELEVENLABS_API_KEY` (jamais commitée). Je peux
    aussi passer par le connecteur ElevenLabs de la session — dis-moi ce que tu préfères.
12. **Validation du script final avant TTS** — règle du dépôt, je ne génère pas la voix
    avant ton OK écrit.

---

## 5. Ce que je fais dès que j'ai le feu vert

1. Script V2 corrigé + minuté ligne par ligne (`script/script-v2.json`) → validation.
2. VO ElevenLabs, une ligne par bloc, loudnorm par ligne.
3. Dérushage des captures produit (sélection des segments utiles, zoom-punch sur les clics).
4. Mockups animés (WhatsApp, campagne réseaux sociaux, post-it/alerte).
5. Montage `build.py` en 1920×1080 / 30 fps + BGM + SFX + sous-titres + carte CTA tenue ≥ 5 s.
6. Livrables : `output/foodeatup-prospect.mp4`, poster, `.vtt`, version 9:16 et cut court
   si demandés, puis upload RapidoCMS si tu veux le planifier.

**Estimation** : ~1 journée de production une fois les décisions §4.1 prises et les
captures §4.2.10 reçues (ou l'accord pour les mockups).
