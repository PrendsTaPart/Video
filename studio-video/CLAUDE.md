# Mon Studio Reels — Mémoire personnelle (LIRE EN PREMIER)

C'est le studio de Michael pour fabriquer des Reels Instagram (vidéo verticale) avec HyperFrames.
Ce fichier est relu à chaque session : toute nouvelle préférence donnée par Michael doit être
ajoutée ici, pour ne jamais avoir à la réexpliquer.

## Format vidéo

- **1080×1920** (vertical, 9:16), **30 images/seconde** — configuré par défaut dans `index.html`
  (`data-width="1080"`, `data-height="1920"`, viewport 1080×1920). Rendu avec `npx hyperframes render`
  (fps 30 par défaut, pas besoin de préciser `--fps`).

## Identité de marque — FoodEatUp

Michael parle du produit **FoodEatUp** (« une infinité de solutions pour gérer votre
restaurant »). Charte graphique officielle fournie par Michael (PDF) :

- **Couleurs** :
  - Fond par défaut : **crème `#FCF9E6`**
  - Texte / encre : **marine foncé `#0F1A23`**
  - Accent primaire : **bleu `#007BFF`**
  - Accent secondaire / CTA : **orange `#FFA500`**
  - Répartition : fond crème + texte marine pour la lisibilité, bleu et orange pour les accents,
    icônes, surlignages, CTA. Variables CSS déjà posées dans `index.html`
    (`--foodeatup-bg`, `--foodeatup-ink`, `--foodeatup-blue`, `--foodeatup-orange`).
- **Police de marque** : **Goodly** (ronde, sympa, cohérente avec le logo chef souriant).
  - ⚠️ Le fichier réel de la police Goodly n'a pas été fourni. En attendant, **Fredoka**
    (Google Fonts, vendorée localement dans `assets/vendor/fonts/Fredoka-Variable.woff2`) sert de
    remplaçant temporaire visuellement proche (ronde, bold, friendly). Dès que Michael fournit le
    vrai fichier Goodly (`.woff2`/`.ttf`), le déposer dans `assets/vendor/fonts/` et mettre à jour
    le `@font-face` dans `index.html` (déclaré sous le nom `"Goodly"`, donc aucun autre changement
    nécessaire ailleurs dans les compositions).
- **Logo** : mascotte chef souriant, style contour bleu — toujours utiliser les vrais assets de
  marque ci-dessous, jamais une recréation approximative (theSVG ne les a pas : FoodEatUp n'est
  pas une marque publique dans son catalogue — theSVG reste utile pour les vrais logos tiers
  mentionnés dans une vidéo, ex. Claude, GitHub, etc.).
- Fichiers logo officiels fournis par Michael, dans `assets/brand/logo/` :
  - `foodeatup-logo-horizontal.png` — logo complet horizontal, pastille bleue, texte blanc,
    "OO" orange/blanc (variante sur fond bleu, pour usage sur fond clair/neutre en incrustation).
  - `foodeatup-logo-mascot.png` — logo horizontal avec mascotte chef intégrée dans le "O", fond
    transparent, contour bleu (variante la plus polyvalente, à privilégier en incrustation coin).
  - `foodeatup-mark-eight.png` — le symbole seul (le "8"/mascotte chef, sans texte), fond
    transparent, pour les usages où seul le pictogramme est nécessaire (favicon-like, sting final).
- Charte graphique complète (PDF) sauvegardée dans `assets/brand/Charte_graphique_FoodEatUp.pdf`
  pour référence.

## Structure narrative

- Découper le discours en sections logiques : accroche, principe, preuve, étapes, prix,
  bénéfice, appel à l'action... **Une animation par section** (une sous-composition ou un bloc
  de clips dédié par section).
- Par défaut : **écran scindé** — la tête de Michael recadrée en bas, l'animation au-dessus.
  **Plein écran** uniquement quand une section le mérite (la tête disparaît derrière le visuel).

## Règle d'or du motion design

- Le motion design est **100% visuel** : schémas, icônes, flux, comparaisons.
- **Jamais** de gros texte qui répète ce qui est déjà dit à l'oral — la voix + les sous-titres
  suffisent pour le texte. Le visuel **ajoute** de l'info, il ne la redit pas.
- **Style : fun et énergique.** Rebonds (`back.out`, `elastic.out`), couleurs vives (bleu/orange
  FoodEatUp), rythme rapide, effets ludiques. Éviter les transitions trop sobres/lentes par défaut.

## Logos de marque

- Toujours les **vrais logos**, récupérés via le skill **theSVG** (`glincker/thesvg`, installé),
  dans leurs vraies couleurs officielles. Jamais d'approximation ou de logo réinventé.

## Sous-titres

- Une seule ligne à la fois (jamais deux).
- Blocs de **2 à 6 mots**, coupés là où la phrase respire naturellement.
- Jamais de point final. Jamais de coupure qui laisse une phrase en plan (pas de coupure au
  milieu d'un groupe de sens).
- **Style : Reels/TikTok bold.** Texte blanc, gras, contour noir épais (classe `.subtitle` déjà
  posée dans `index.html` : `-webkit-text-stroke`, `paint-order: stroke fill`), positionné en bas
  de l'écran. Police Goodly (voir "Identité de marque").

## Son (SFX / musique)

- Catalogue HeyGen (recherche en langage naturel) via le skill `hyperframes-media` — auth requise :
  voir "Setup technique" ci-dessous.
- Dossier `assets/sfx/` : y ranger tous les effets sonores utilisés. Si Michael dépose des sons
  perso (ex. exports CapCut), **les réutiliser en priorité** avant d'aller en chercher un nouveau
  dans le catalogue.
- Dossier `assets/music/` : musiques de fond.
- Dossier `assets/raw/` : vidéos brutes déposées par Michael avant dérush.
- **Règle** : pour chaque transition, apparition ou surlignage à l'écran, choisir le son qui colle,
  le télécharger dans `assets/sfx/`, et le poser **pile sur l'événement visuel**, à un volume
  **sous la voix** de Michael. Comme c'est nous qui fabriquons l'animation, le timing exact de
  chaque transition est connu — pas d'approximation sur le placement.
- **Musique de fond** : pas de morceau récurrent — choisir la musique et les SFX au cas par cas
  selon le sujet de chaque vidéo.
- **Quirk pipeline audio (confirmé 2×, 2026-07)** : le wrapper `audio.mjs` du skill
  product-launch-video choisit HeyGen dès que `HEYGEN_API_KEY` est présent → échec si le
  storyboard spécifie une voix ElevenLabs. Pour forcer ElevenLabs, appeler le moteur directement :
  `node /root/.claude/skills/hyperframes-media/scripts/audio.mjs --only tts --provider elevenlabs
  --voice <voice_id> --lang fr`. Autre bug connu : les passes `fetch-sfx` / `--only` **écrasent la
  section `voices` d'`audio_meta.json`** — garder les `transcript.json` whisper (ex.
  `/tmp/promo_transcripts/`) et reconstruire `audio_meta.json` en Python après coup.

## Système de dérush automatique (pour chaque vidéo brute reçue)

Michael se filme en lisant son texte au prompteur, phrase par phrase, avec des blancs et des
prises ratées ou refaites. Pour chaque vidéo brute déposée dans `assets/raw/` :

1. **Transcription locale (Whisper, rien ne part en ligne)** :
   ```bash
   npx hyperframes transcribe assets/raw/<video> --model small --language fr
   ```
   Produit un transcript mot-à-mot avec timestamps (`transcript.json`).

2. **Détection des silences (points de coupe réels)** avec ffmpeg :
   ```bash
   ffmpeg -i assets/raw/<video> -af silencedetect=noise=-30dB:d=0.5 -f null - 2>&1 | grep silence
   ```
   Ajuster le seuil `noise` (dB) et la durée min `d` (secondes) si la vidéo est bruitée ou si les
   silences sont très courts.

3. **Sélection de la meilleure prise** de chaque phrase du script (s'appuyer sur le script fourni
   par Michael pour identifier quelle prise correspond à quelle phrase) ; jeter les blancs,
   hésitations et prises ratées.

4. **Découpe** : couper **uniquement** dans les silences détectés à l'étape 2, jamais au milieu
   d'un mot. **Ne jamais deviner un timestamp** — se baser uniquement sur les sorties des outils
   (transcript + silencedetect).

5. **Sortie** : un montage serré en 1080×1920, plus une timeline exploitable pour caler les
   sous-titres et le timing du motion design. Si l'audio grésille, le nettoyer (ex. filtre
   `afftdn` / `highpass` ffmpeg selon le problème).

## Setup technique (pour la mémoire de l'agent, pas pour Michael)

- **ffmpeg** et **Node.js ≥22** installés sur cette machine.
- Skills HyperFrames + theSVG installés (`~/.claude/skills/`).
- **Quirk connu** : `npx hyperframes@<version épinglée>` (ex. `hyperframes@0.7.26`) échoue
  silencieusement (exit 1, aucune sortie) dans cet environnement. Toujours utiliser
  `npx hyperframes <commande>` **sans** épingler de version — c'est ce que `package.json` utilise
  désormais (scripts corrigés lors du setup initial).
- **Quirk connu** : toute install npm qui tire `onnxruntime-node` peut échouer avec `ECONNRESET`
  car son script d'install tente de télécharger des binaires CUDA (GPU) inutiles ici. Toujours
  lancer les installs avec `ONNXRUNTIME_NODE_INSTALL_CUDA=skip` dans l'environnement.
- **Règle importante** : Chrome headless (utilisé par `hyperframes validate`/`render`) ne passe
  pas par le proxy réseau de cet environnement et ne peut donc pas charger de script externe
  (ex. `<script src="https://cdn.../gsap.min.js">`) → `npx hyperframes validate` timeout sur la
  navigation. **Toujours vendorer les libs JS en local** dans `assets/vendor/` (ex.
  `npm install gsap` puis copier `node_modules/gsap/dist/gsap.min.js` vers
  `assets/vendor/gsap.min.js`, et référencer `assets/vendor/gsap.min.js` dans le `<script src>`
  au lieu d'un CDN). C'est aussi plus conforme à la règle "no network fetches" du framework.
- **Auth HeyGen (bibliothèque de sons / TTS)** : pas encore connectée dans cet environnement
  (l'OAuth navigateur `npx hyperframes auth login` ne fonctionne pas dans un container headless).
  Michael doit fournir une clé API HeyGen (app.heygen.com/settings/api) à configurer via
  `HEYGEN_API_KEY`, sinon les workflows retombent sur les moteurs locaux (Kokoro pour la voix,
  MusicGen pour la musique — nécessitent `pip install kokoro-onnx soundfile` /
  `pip install transformers torch soundfile numpy`).
- Preview local : `npm run dev` (arrière-plan) → `http://localhost:3002`. Dans un environnement
  cloud isolé, cette URL n'est pas accessible depuis le navigateur de Michael — seulement utile
  pour l'inspection interne de l'agent, ou en local sur sa machine.
- **Quirk connu (2026-07-08, hyperframes 0.7.42)** : `npx hyperframes snapshot` a un bug de seek —
  les timelines GSAP restent à ~2-4s de temps « horloge murale » après le chargement de la page au
  lieu d'être positionnées à l'instant demandé (symptôme : sous-titres du début affichés à 20s+,
  frames longues « en retard » sur leur timeline interne, résultat NON déterministe entre deux runs).
  Le pipeline `render`, lui, est exact (vérifié image par image). **QA fiable** : rendre en
  `--quality draft` puis extraire les instants avec
  `ffmpeg -ss <t> -i draft.mp4 -frames:v 1 out.png` (une commande ffmpeg PAR instant — enchaîner
  plusieurs `-ss/-i/sortie` dans une seule commande mappe mal les entrées). Ne pas conclure à un bug
  de composition sur la seule foi d'une planche-contact snapshot.
- **Attention au cwd des commandes en arrière-plan** : le répertoire de travail persiste entre les
  appels Bash — toujours préfixer les renders par `cd <projet> &&` explicite.
- **Librairie d'images partagée** : `videos/shared-images/` (committée) — `brand/` (logos) +
  `characters/` (personnages 3D cartoon générés via RapidoCMS, fond off-white #F7F9FC, accents
  #1E9BF0, chef cohérent : jeune homme, toque/veste blanches). **Réutiliser ces personnages**
  d'une vidéo à l'autre avant d'en générer de nouveaux ; pour un nouveau projet, copier le PNG
  voulu dans `<projet>/public/` (chemins HyperFrames relatifs à la racine du projet). Voir le
  README de la librairie pour l'inventaire.
- **Voix directe ElevenLabs (propre)** : pour forcer Adam (ou toute voix ElevenLabs) sans la
  reconstruction manuelle, écrire un `audio_request.json` (`{provider:"elevenlabs", voice:"<id>",
  lang:"fr", lines:[{id,text}]}`) et appeler le moteur média directement
  (`node <MEDIA_DIR>/scripts/audio.mjs --request audio_request.json --hyperframes . --out
  audio_engine_meta.json --only tts --provider elevenlabs --lang fr`, clé exportée depuis
  `studio-video/.env`), puis convertir en shape PL + ajouter BGM/SFX en Python. Si whisper renvoie
  0 mot ou détecte la mauvaise langue sur une ligne, re-transcrire avec
  `npx hyperframes transcribe <wav> --model small --language fr`.
- **Branche par défaut = branche de travail** : sur ce repo, `claude/hyperframes-reels-studio-*`
  est la branche par défaut (HEAD) ; les autres branches y sont mergées via PR. On ne crée donc
  PAS de PR pour cette branche (pas de merge vers soi-même) — pousser directement dessus est
  l'état final.

## Vidéos hors-Reels (16:9, autres marques)

Le projet peut aussi produire des vidéos ponctuelles hors du système Reels vertical par défaut
(ex. explainers produit 16:9 pour une autre marque que FoodEatUp). Dans ce cas :

- Construire une composition à part dans `compositions/<nom>.html` (jamais dans `index.html`,
  réservé aux Reels FoodEatUp verticaux) — voir `npx hyperframes render --composition
  compositions/<nom>.html`.
- Voix ElevenLabs choisie pour les contenus "produit tech / pédagogique" : **Adam - Instructor**
  (`voice_id: TGAegA0zNRi8I6nUdq3i`), français, ton professionnel posé. Clé API dans `.env`
  (`ELEVENLABS_API_KEY`, jamais commitée).

## RÈGLE STANDING — Sauvegarde de CHAQUE vidéo dans RapidoCMS (demandé par Michael 2026-07-09)

**À chaque vidéo générée**, une fois le MP4 rendu, poussé sur GitHub, l'archiver dans la
**bibliothèque RapidoCMS** (`upload_file_tool` avec `type:"video"`) pour ne perdre aucune
production. `upload_file_tool` exige une **URL publique** (pas de fichier local) : après avoir
commité/poussé le MP4, récupérer son `download_url` via `mcp__github__get_file_contents`
(chemin du .mp4 dans le repo) puis le passer à `upload_file_tool(type:"video", name:"<projet>",
file_url:"<download_url>")`. C'est une SAUVEGARDE systématique, distincte d'une publication réseaux
(qui reste sur demande explicite). Rattraper aussi les vidéos déjà rendues non encore archivées.

## Orthographe de marque — « FoodEatUp » (demandé par Michael 2026-07-09)

Le nom s'écrit **exactement `FoodEatUp`** — F, E et U majuscules, tout attaché, aucune autre
graphie (pas « Foodeatup », « FoodEatup », « Food Eat Up »). **Whisper le mal-transcrit
systématiquement** dans les sous-titres karaoké (« Fooditup », « Food It Up », « Foodie top »).
→ **Règle : avant le rendu final, corriger les sous-titres sur le texte VERBATIM du `SCRIPT.md`**
(a minima le nom de marque, idéalement toute la ligne), puis régénérer `captions.mjs build` et
re-corriger le gsap CDN → `assets/vendor/gsap.min.js`. Ne jamais livrer une vidéo dont le rail de
sous-titres affiche une graphie fautive de FoodEatUp. Méthode : réécrire les `words` de chaque voix
dans `audio_meta.json` avec les mots du script (timings interpolés proportionnellement sur les
timings Whisper), puis rebuild.

## Multi-marques — charte par projet (demandé par Michael 2026-07-09)

Le studio sert plusieurs marques de l'agence. **Toujours choisir la charte + le logo selon le
projet.**

- **FoodEatUp** (charte par défaut actuelle) : fond off-white `#F7F9FC`, texte navy `#1B2A41`,
  UN accent bleu `#1E9BF0` (vert `#059669` réservé aux coches de validation) ; typo **Poppins**
  (titres 600-800) + **Inter** (body). Logos : `videos/shared-images/brand/foodeatup-logo-mascot.png`
  (+ `foodeatup-mark-eight.png`). Personnages 3D cartoon cohérents dans
  `videos/shared-images/characters/` — **réutiliser** avant d'en générer de nouveaux.
- **BraindCode** : charte + logo **à fournir plus tard** par Michael. Quand reçus : les stocker
  dans `videos/shared-images/braindcode/` (brand + éventuels personnages), les documenter ici, et
  remixer `frame.md` sur ces tokens pour les projets BraindCode. Ne pas réutiliser la charte
  FoodEatUp pour un projet BraindCode.

## Publication — RapidoCMS (MCP)

Le serveur MCP **RapidoCMS** (`mcp__RapidoCMS__*`) est connecté et donne accès à la publication
sur les réseaux sociaux directement depuis cette session. Pas besoin de reconnexion.

### Comptes connectés (`company_id: 321`)

Récupérables à tout moment via `list_connected_accounts` (peut changer, toujours revérifier
avant de publier). État constaté le 2026-07-02 :

- **Facebook** : Foodeatup (`201499969703551`), Cocuisinage By Foodeatup (`114822143406613`),
  Prendstapart (`766096339928845`), RapidoSoftware (`223318770858972` et `198505523347506`),
  BraindCode, Plan'It, SUNLIGHT, Cocuisinage.braindcode, Avatalk, et une page perso non-pro.
- **LinkedIn (pages)** : FoodEatUp (`68807312`), FoodEatUp TN (`106239843`), Prendstapart.braindcode
  (`109181306`), RapidoSoftware (`101119107`), Rapidosoftware TN (`106240828`), BraindCode
  (`101119080`), Bootcamp StartupForge (`111309218`).
- **LinkedIn (profil perso)** : Michael_Kebail (`6Z5izYBhkC`).
- **Instagram** : BraindCode (`17841401924902629`), Cocuisinage (`17841428088027945`), Plan'It
  (`17841477770894918`), Rapido Software (`17841473451404310`). **Pas de compte Instagram FoodEatUp
  connecté actuellement** — à vérifier/ajouter si besoin pour les Reels FoodEatUp.
- **TikTok** : aucun compte connecté actuellement.

⚠️ Toujours confirmer avec Michael la page exacte avant de publier — plusieurs comptes portent des
noms proches (ex. 3 pages "FoodEatUp"-like, 2 pages RapidoSoftware sur Facebook).

### Workflow de publication (recette testée le 2026-07-02)

1. **Obtenir une URL publique du fichier vidéo/image** — `upload_file_tool` a besoin d'une URL
   publique, pas d'un fichier local. Le plus fiable dans cet environnement : committer/pousser le
   fichier sur la branche, puis récupérer une URL de téléchargement via l'outil GitHub
   `get_file_contents` (repo `PrendsTaPart/Video`) — il renvoie une `download_url` signée
   (raw.githubusercontent.com avec `?token=...`), **valable seulement quelques minutes** : l'utiliser
   immédiatement, ne pas la stocker. (`hyperframes publish` vers hyperframes.dev NE fonctionne PAS
   pour ça — ça publie une page de projet à réclamer, pas un lien direct vers le fichier rendu.)
2. **Importer dans la bibliothèque RapidoCMS** : `upload_file_tool(type, name, file_url)` → renvoie
   un `file_url` stable sur S3 (`rapido-software.s3.eu-west-3.amazonaws.com/...`), à réutiliser.
3. **Créer le brouillon** : `create_draft_tool(post_name, social_type, account_id, post_type,
   media_type, media_source="biblio", media_url, media_caption)`. `post_type` = `mediatext` pour
   vidéo/image + légende. `account_id` = le `account_id` du compte visé (voir liste ci-dessus).
4. **Publier** : il n'existe pas d'outil "publier maintenant" dédié — utiliser `schedule_draft_tool`
   avec une date/heure très proche du présent. Pièges rencontrés :
   - `post_heure` doit être au format `H:i:s` avec des **deux-points** (`23:35:00`), pas des tirets
     malgré ce que dit la description de l'outil.
   - Le serveur compare l'heure programmée à son horloge en **heure de Paris (Europe/Paris,
     UTC+1/+2)**, pas en UTC — si on envoie l'heure UTC courante ça revient "dans le passé". Toujours
     calculer l'heure de Paris actuelle et viser quelques minutes plus tard.
5. Autres outils utiles : `list_scheduled_posts` (vérifier), `cancel_schedules_post` (annuler),
   `post_insights` (stats après publication), `add_post_campagne`/`remove_post_campagne` (regrouper
   des posts dans une campagne), `list_all_files` (bibliothèque existante, éviter de ré-uploader).

### Autres capacités RapidoCMS disponibles (non testées, à explorer si besoin)

- **Cartes digitales / NFC** : `add_digital_card`, `edit_digital_card`, `delete_digital_card`,
  `list_digital_card`, `list_card_templates`, `assign_card_template`, `add_card_page_link`,
  `edit_card_page`, `delete_card_page_link`, `list_card_page`.
- **Templates de post** : `create_post_template` (HTML/CSS custom, type poste/carte de visite/carte NFC).
- **Génération d'image** : `generate_image`.
- **Prompts réutilisables** : `add_prompt`, `edit_prompt`, `delete_prompt`, `list_prompts`.
- **Campagnes** : `create_campagne`, `edit_campagne`, `delete_campagne`, `list_campagnes`,
  `list_posts_campagne`, `ingishts_campagne` (stats de campagne).
- **Infos compte** : `get_brand`, `get_company`, `get_profile`.

## HeyGen — clarification importante (2026-07-02)

Un connecteur MCP `HyperFrames_by_HeyGen` a été autorisé, mais **ce n'est PAS un générateur
d'avatar humain 3D avec synchronisation labiale**. C'est une version hébergée du même outil
HyperFrames qu'on utilise déjà en local (animations HTML/CSS). Ses propres instructions précisent
que, depuis un agent avec accès au système de fichiers (comme cette session), ses outils de
création (`compose`, `render_video`) sont **désactivés** au profit des skills locaux déjà
installés — seuls les outils de lecture (`list_projects`, `get_project`, `get_project_status`,
`get_render_status`) restent disponibles, et ne servent à rien pour notre usage.
**Pour un vrai avatar IA humain (type intro présentée par un avatar), il faudrait passer par le
produit HeyGen Avatar / Studio directement (app.heygen.com), qui est distinct de ce connecteur et
n'est pas branché ici.**

## HeyGen Avatar API — avatar « Mika » (branché le 2026-07-02)

Michael a fourni une vraie clé API HeyGen (`HEYGEN_API_KEY`, stockée dans `/home/user/Video/.env`
— **racine du dépôt, partagée par tous les projets vidéo**, jamais commitée). Ceci donne accès à
la vraie **API Avatar HeyGen** (REST directe, `https://api.heygen.com`, header `X-Api-Key`) —
distincte du connecteur MCP `HyperFrames_by_HeyGen` (qui, lui, ne sert à rien pour nous, voir
au-dessus). C'est aussi le même credential que la chaîne TTS de `hyperframes-media` (voir
`references/tts.md`) : avec cette clé, les prochains rendus peuvent utiliser la voix HeyGen native
(meilleurs word-timestamps, pas de passe Whisper séparée) au lieu d'ElevenLabs/Kokoro — à évaluer
au cas par cas.

**Il n'y a pas d'avatar nommé « Michael » sur ce compte.** Michael a choisi d'utiliser à la place
l'avatar existant **« Mika »** pour animer son personnage dans les prochaines vidéos :

- `avatar_group_id`: `648209ec82414565864f1771aa1d763e` (nom du groupe : "Mika", 2 déclinaisons)
- `avatar_id` (déclinaison principale, motion, statut `completed`) : `648209ec82414565864f1771aa1d763e`
- `avatar_id` (déclinaison "Mika Paysage", statut `completed`) : `bd56633302aa4790a8d526fe2ee6b63f`
- `default_voice_id` associé : `f6dec6ea26b6484eb142cc8224abb1fc`
- Il existe aussi un groupe plus développé, **« Storytelling Mika: IA (1) »**
  (`avatar_group_id: eedc9989b8964af8a7d94a143579243f`, 12 déclinaisons) — pas encore exploré,
  à regarder si l'avatar principal ne convient pas pour un usage donné.
- Autres avatars perso disponibles sur ce compte (non choisis par défaut, mais utilisables si
  demandé) : **Ethan** (`avatar_group_id: dc5e0096b3e74c289955653fd2937a4c`), **Matthew**
  (`avatar_group_id: a04bfe8e5aed42518495dde3a31731ad`).
- Pour retrouver/rafraîchir ces infos : `GET /v2/avatar_group.list` (liste des groupes perso) puis
  `GET /v2/avatar_group/{group_id}/avatars` (déclinaisons + `avatar_id` exacts à l'intérieur d'un
  groupe). `GET /v2/avatars` liste le catalogue public (1281 avatars stock, inutile pour Mika qui
  est un avatar perso). ⚠️ Ces appels peuvent être lents dans cet environnement (jusqu'à ~60-90s
  pour `/v2/avatars`, le proxy réseau semble ajouter de la latence sur ce host) — prévoir un
  `--max-time` généreux (60-90s) et ne pas conclure à une panne trop vite.

**Génération vidéo (pas encore testée de bout en bout dans ce projet — à valider avant un usage
en production) :**

```bash
POST https://api.heygen.com/v2/video/generate
Header: X-Api-Key: $HEYGEN_API_KEY
Body:
{
  "video_inputs": [{
    "character": { "type": "avatar", "avatar_id": "648209ec82414565864f1771aa1d763e", "avatar_style": "normal" },
    "voice": { "type": "text", "input_text": "<texte à dire>", "voice_id": "f6dec6ea26b6484eb142cc8224abb1fc" },
    "background": { "type": "color", "value": "#0B1E33" }
  }],
  "dimension": { "width": 1920, "height": 1080 }
}
```

Renvoie un `video_id` ; poller `GET /v2/video_status.get?video_id=<id>` jusqu'à `status: completed`
pour récupérer l'URL du rendu final. Usage prévu : générer un clip d'intro avec l'avatar Mika qui
parle, puis l'intégrer comme clip `<video>` dans la composition HyperFrames (comme n'importe quel
asset vidéo utilisateur) plutôt que de tenter de le recréer en HTML/CSS.

## Préférences validées avec Michael

Calibration faite le 2026-07-02 :

- Sous-titres : style Reels/TikTok bold (blanc, contour noir épais, bas d'écran).
- Identité visuelle : charte FoodEatUp (fond crème, texte marine, accents bleu/orange) — voir
  "Identité de marque" ci-dessus.
- Police de titre : Goodly (police de marque), remplacée temporairement par Fredoka en attendant
  le vrai fichier.
- Style de motion : fun et énergique.
- Musique de fond : pas de morceau récurrent, choix au cas par cas.
- Sons perso : Michael peut en déposer dans `assets/sfx/` — à réutiliser en priorité.
- Première vidéo : part d'un **script écrit** (pas de vidéo brute pour l'instant) — donc pas de
  dérush à lancer tout de suite ; attendre le script + le sujet.

---

# HyperFrames Composition Project

## Skills — USE THESE FIRST

**Always invoke the relevant skill before writing or modifying compositions.** Skills encode framework-specific patterns (e.g., `window.__timelines` registration, `data-*` attribute semantics, shader-compatible CSS rules) that are NOT in generic web docs. Skipping them produces broken compositions.

**Doing anything with HyperFrames?** Start at `/hyperframes` — it tells you what HyperFrames can do and which skill or workflow handles your intent (make a video, TTS / BGM, prep footage, author / animate, render, install blocks), and routes every "make me a video" request to the right workflow. Read it first, especially when there's no project context to orient you. The video workflows it routes to:

- `/product-launch-video` — a **product** URL or brief / script → 60-90s product launch / SaaS / promo video.
- `/website-to-video` — a **general** website / URL → a video _of_ the site (tour / showcase / social clip from captured visuals); a product **launch / promo** is `/product-launch-video`.
- `/faceless-explainer` — arbitrary text (topic / article / notes), **no URL, no website capture** → 60-90s faceless explainer.
- `/embedded-captions` — an existing talking-head video (MP4) → the same footage with captions / subtitles added (rail + embed, or pure-cinematic embed); the footage itself is untouched.
- `/talking-head-recut` — an existing talking-head / interview / podcast video (MP4) → the same footage **packaged with designed graphic overlays** (kinetic titles, lower-thirds, data callouts, pull-quotes, side panels, pip) synced to the transcript; the clip plays unchanged underneath. (Plain captions/subtitles → `/embedded-captions`.)
- `/pr-to-video` — a GitHub PR (URL / `owner/repo#N` / "this PR") → 30-90s code-change explainer (changelog / feature reveal / fix / refactor).
- `/motion-graphics` — a short (typically under 10s) design-led **motion graphic**, motion-is-the-message, no narration: kinetic type, a stat / number count-up, a chart, a logo sting, a lower-third / overlay, or an animated tweet / headline / captured-page highlight; rendered to MP4 or a transparent overlay. Longer / narrated / custom → `/general-video`.
- `/general-video` — fallback for any other video (title card, longer brand / sizzle reel, multi-scene montage, static loop, custom composition); the original hyperframes authoring flow, any length.

**Porting an existing composition?** `/remotion-to-hyperframes` translates a Remotion (React) composition into HyperFrames HTML — a source migration, separate from the creation workflows above.

The domain skills (`/hyperframes-core`, `/hyperframes-animation`, `/hyperframes-creative`, `/hyperframes-cli`, `/hyperframes-media`, `/hyperframes-registry`) and the full capability map live inside `/hyperframes` — it is the single source of truth for which skill handles which intent.

> **Tailwind v4 projects** (`hyperframes init --tailwind`): see `/hyperframes-core` → `references/tailwind.md`.

> **Skills not available or need updating?** Run `npx skills add heygen-com/hyperframes`
> and restart the agent session so the new skills load.

## Commands

```bash
npm run dev          # start the preview server (long-running — keep it alive in background)
npm run check        # lint + validate + inspect
npm run render       # render to MP4
npm run publish      # publish and get a shareable link
npx hyperframes lint --verbose  # include info-level findings
npx hyperframes lint --json     # machine-readable output for CI
npx hyperframes docs <topic> # reference docs in terminal
```

> **`npm run dev` is a long-running server, not a one-shot command.** It blocks until stopped.
> In Claude Code, always run it with `run_in_background: true`. Never run it as a foreground
> command — it will time out and the server will die, breaking the browser preview.

## Documentation

**For quick reference**, use the local CLI docs command (no network required):

```bash
npx hyperframes docs <topic>
```

Topics: `data-attributes`, `gsap`, `compositions`, `rendering`, `examples`, `troubleshooting`

**For full documentation**, discover pages via the machine-readable index — do NOT guess URLs:

```
https://hyperframes.heygen.com/llms.txt
```

## Project Structure

- `index.html` — main composition (root timeline)
- `compositions/` — sub-compositions referenced via `data-composition-src`
- `meta.json` — project metadata (id, name)
- `transcript.json` — whisper word-level transcript (if generated)

## Linting — ALWAYS RUN AFTER CHANGES

After creating or editing any `.html` composition, **always** run the full check before considering the task complete:

```bash
npm run check
```

Fix all errors before presenting the result. Inspect warnings should be reviewed before rendering.

## Key Rules

1. Every timed element needs `data-start`, `data-duration`, and `data-track-index`
2. Elements with timing **MUST** have `class="clip"` — the framework uses this for visibility control
3. Timelines must be paused and registered on `window.__timelines`:
   ```js
   window.__timelines = window.__timelines || {};
   window.__timelines["composition-id"] = gsap.timeline({ paused: true });
   ```
4. Videos use `muted` with a separate `<audio>` element for the audio track
5. Sub-compositions use `data-composition-src="compositions/file.html"` to reference other HTML files
6. Only deterministic logic — no `Date.now()`, no `Math.random()`, no network fetches
