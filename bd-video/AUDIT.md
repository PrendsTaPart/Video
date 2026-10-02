# Étape 0 — Audit du dépôt

> **La Brigade augmentée** en vidéo · inventaire de ce qui existe et de ce qu'on peut réutiliser.
> Généré le 2026-10-02 par `bd-video/scripts/audit_media.py`. Le détail média par média est dans
> [`assets/catalog.json`](assets/catalog.json).

## En bref

| | Fichiers suivis | Uniques (après dédoublonnage md5) | Poids |
|---|---:|---:|---:|
| Vidéos | 617 | 592 · 6 h 00 de durée cumulée | 4,34 Go |
| Sons | 1 986 | 1 544 · 2 h 36 de durée cumulée | 0,46 Go |
| Images | 1 466 | 1 003 | 0,87 Go |
| Polices | 347 | 83 | 0,01 Go |
| Sous-titres | 1 | 1 | — |
| **Total** | **4 417** | **3 223** | **5,7 Go** |

**Ce qu'on retient pour le film :**

- **Aucun média existant ne vient de la BD.** Les dessins, le texte et les portraits viendront de Figma
  (étape 1). Le dépôt fournit seulement l'habillage, les bruitages, les logos et quelques inserts.
- **On réutilise :** les **41 bruitages uniques**, les **logos FoodEatUp**, le **logo animé** (sting) de
  `lancement-foodeatup-v1`, la structure d'outro de la saison 2, les **245 captures du logiciel**
  (pour la série « une case, une fonction ») et la police **Bangers**.
- **On refait :** **toutes les musiques**. Les 14 pistes uniques sont des maquettes, ElevenLabs Music
  ou catalogue HeyGen, et aucune n'a l'ambiance d'une partie de la BD. Pareil pour **toutes les voix**,
  les 1 479 pistes portent le texte d'autres vidéos.
- **On ignore :** les rendus finaux (110), les voix off des autres vidéos, les images d'illustration
  et les exemples livrés avec les skills HyperFrames.
- **Outil de montage :** HyperFrames en local (CLI `hyperframes` 0.8.112, vérifié dans ce conteneur).
  Le rendu local ne coûte rien. Voir la recommandation plus bas.

## Méthode

- **Périmètre :** les fichiers suivis par Git (`git ls-files`), sous-dossiers et LFS compris, hors `node_modules`.
- **Métadonnées :** `ffprobe` relève la durée, la résolution, le ratio, les fps, les codecs vidéo et audio et le débit.
- **Doublons :** empreinte md5. Le champ `doublon_de` renvoie à la première occurrence.
  Par exemple, la même musique `track.loop.mp3` est copiée dans 27 dossiers.
- **Présence de voix :**
  - `oui` : le fichier est rangé dans un dossier `vo/`, `voice/` ou `voix/`.
  - Sinon, `webrtcvad` mesure la part de trames « parole » sur les 90 premières secondes. On note `probable` à ≥ 35 %, `possible` entre 12 et 35 %, `non` en dessous.
  - ⚠️ Ce détecteur confond souvent la musique et la voix : toutes les musiques ressortent en `probable`. Le champ `parole_ratio` reste disponible pour trier.
- **Usage proposé :** des règles sur le chemin du fichier (voir `classify()` dans le script).
  Chaque média reçoit une `categorie`, un `usage` et une `recommandation`.
- **LFS :** seuls 2 fichiers sont dans LFS, des exemples d'un skill HyperFrames
  (`changelog-video/assets/bg-pattern.mp4`, `bgm.mp3`). Ce sont des pointeurs non téléchargés, donc sans intérêt ici.

## Classement par usage

| Catégorie | Uniques | Recommandation | Commentaire |
|---|---:|---|---|
| Logo / identité FoodEatUp (images) | 28 | ✅ à réutiliser | Logos PNG, mais **la référence reste Figma** (règle « Marques ») |
| Logo animé / intro / outro (vidéos) | 71 | ✅ à réutiliser (en partie) | Sting FoodEatUp, outros de la saison 2 (gabarit) |
| Intro / outro (images, cartes tuto 16:9) | 107 | ❌ à ignorer | Cartes d'intro des tutoriels, mauvais format |
| Logos tiers (Claude, OpenAI, Mistral…) | 5 | ⚠️ tel quel, seulement si la BD les montre | Prendre de préférence ceux de la page 88 dans Figma |
| Plans Seedance (saison 2) | 34 | 🟡 insert ponctuel | Michael en prise de vue réelle IA, 720×1280. Style différent de la BD |
| Plans Higgsfield réalistes | 49 | 🟡 insert ponctuel | Cuisine, salle, caisse. 16:9 en majorité, sans son |
| Captures du logiciel | 245 vidéos + 60 images | ✅ à réutiliser | Série bonus « une case, une fonction » |
| Bruitages (sfx) | 41 | ✅ à réutiliser | Ticket qui s'imprime, scanner, encaissement, ambiance cuisine, etc. |
| Musiques | 14 | 🔁 à refaire | Maquettes IA. Une ambiance par partie à produire (étape 2) |
| Voix off | 1 479 | ❌ à ignorer | Texte d'autres vidéos |
| Habillage (frames, snapshots) | 250 | 🟡 référence de style | Images de gabarits HTML déjà rendus, pas des éléments animables |
| Polices | 1 + 82 | ✅ Bangers / ❌ le reste | Comic Neue absente, à charger depuis Google Fonts |
| Rendus finaux | 110 | ❌ à ignorer | Vidéos déjà montées (référence seulement) |
| Plans divers, images diverses | 82 + 476 | ❌ à ignorer | Hors sujet pour la BD |
| Exemples des skills HyperFrames | 70 | ❌ à ignorer | Sauf les 19 sfx Pixabay, comptés dans les bruitages |

### 1. Intro / outro / logo animé FoodEatUp

| Fichier | Durée | Format | Usage proposé |
|---|---:|---|---|
| `videos/lancement-foodeatup-v1/composition/logo-sting/sting-in.mp4` | 1,5 s | 1080×1920 · 30 fps · h264+aac | ✅ ouverture d'épisode, logo animé |
| `videos/lancement-foodeatup-v1/composition/logo-sting/sting-out.mp4` | 2,0 s | 1080×1920 · 30 fps · h264+aac | ✅ fermeture, avant le CTA |
| `videos/tutoriels-foodeatup/fiche-00-ouvrir-son-compte/assets/brand/sting-outro.mp4` | 4,0 s | 1080×1920 · 30 fps · muet | 🟡 variante d'outro |
| `videos/foodeatup-saison-2/outro/template.html` + `renders/epNN/epNN-outro*.mp4` | 12 s | 1080×1920 · 30 fps | 🟡 **gabarit** : on reprend la mécanique (punchline → logo → CTA), pas le texte |
| `studio-video/assets/brand/logo-v2/foodeatup-logo-on-blue-card.png` | — | 451×170 | ✅ carton final sur fond bleu nuit |
| `videos/foodeatup-tuto-5min/assets/logo/foodeatup.png` | — | 1470×510 | ✅ logo haute définition (repli si Figma n'a pas mieux) |
| `videos/tutoriels-foodeatup/fiche-00-ouvrir-son-compte/assets/brand/logo-foodeatup-blanc.png` | — | 267×71 | ✅ logo blanc pour fond sombre (petit) |
| `hero-video/assets/brand/foodeatup-mark-eight.png` | — | 73×146 | 🟡 pictogramme « 8 » (petit) |
| `videos/planit-academy/assets/white_logo.png` | — | 372×432 | 🟡 logo Plani't, si la BD le montre (partie 5) |

> Les logos PNG du dépôt sont petits, souvent moins de 600 px. Pour respecter la règle « Marques », on exporte
> en priorité les logos réels de la **page 88 de la BD** dans Figma (étape 1). Ceux du dépôt servent de repli.

### 2. Plans réutilisables

**Les séries nommées dans le brief n'existent pas dans le dépôt sous ces noms.** Aucun fichier ni document
ne s'appelle « Le Coup de Feu », « Michael remonte le temps » ou « LE CLASH ». Voici ce qui s'en rapproche :

| Série | Où | Plans | Format | Verdict pour la BD |
|---|---|---:|---|---|
| Saison 2 « Michael fait son cinéma » (Seedance via Higgsfield) | `videos/foodeatup-saison-2/renders/epNN/source/` · index [`BIBLIOTHEQUE-PLANS.md`](../videos/foodeatup-saison-2/BIBLIOTHEQUE-PLANS.md) | 32 plans de 10 s + 2 prises alternatives | 720×1280 · 24 fps · son | 🟡 C'est Michael en prise de vue réelle IA, pas en BD. Mélangé aux cases, ça casse le style. À garder pour les déclinaisons « coulisses » ou un renvoi en fin d'épisode |
| Hero vidéo (Higgsfield) | `hero-video/assets/video/` | 17 | 1280×720 · 24 fps · muet | 🟡 Plans d'ambiance (cuisine vide le matin, KDS mural, ticket Z). Utiles pour une version LinkedIn « métier » |
| Stories Higgsfield hf2/hf3 | `instagram-stories/assets/video/hf2/` | 28 | 16:9 en majorité, 4 en 9:16 | 🟡 Même usage que la ligne au-dessus |
| Boucles de marque | `studio-video/assets/brand/loops/` | 5 | 640×374 · 15 fps | ❌ Résolution trop faible |
| Saison 1 « serie-30 » (avatar Mika) | `videos/serie-30-routines/mika-assets/raw/` | 5 | — | ❌ Autre personnage, autre univers |
| Tutoriels (captures écran) | `videos/*-tuto/assets/screen.mp4`, `videos/_captures/`, `planit-tuto-*` | 245 | 16:9 et 9:16 | ✅ Série « une case, une fonction » : une case de BD, puis la vraie fonction à l'écran |

> **Rappel `CLAUDE.md`** : aucun nouveau plan Higgsfield ne sera généré. Les plans « hero » de l'étape 3
> passent par l'image-to-video ElevenLabs (Veo / Kling / Seedance via ElevenLabs), sur devis et après ton accord.
> Les prompts Veo 3 seront fournis dans `veo3_prompts.md` pour que tu puisses les lancer toi-même.

### 3. Musiques et jingles

| Fichier | Durée | Origine / droits | Verdict |
|---|---:|---|---|
| `hero-video/assets/music/musique-sans.mp3` · `musique-avec.mp3` · `musique-resolution-finale.mp3` | 30 s · 45 s · 15 s | ElevenLabs Music, marquées **« placeholder IA, à recomposer »** (`hero-video/README.md`) | 🔁 Le trio sans → avec → résolution colle aux parties 1 et 2. On peut s'en inspirer, mais il faut refaire des pistes plus longues |
| `videos/*/assets/bgm/track.mp3` / `track.loop.mp3` (27 copies identiques + 12) | 36–56 s | Catalogue HeyGen (`media-use`), requête « light corporate uplifting underscore » | ❌ Ton « corporate », hors sujet |
| `videos/planit-product-launch/assets/music/planit-ambient-pad.mp3` | 65 s | Non documentée | 🟡 Possible fond « futuriste » pour la partie 5, droits à vérifier |
| `videos/planit-academy/assets/audio/musique-produit.mp3` | 70 s | Non documentée | ❌ |
| `videos/carousel-calendrier/audio/bgm.mp3` | 36 s | Non documentée (PCM dans un .mp3) | ❌ |

**Droits :** seul `studio-video/.agents/skills/media-use/audio/assets/sfx/CREDITS.md` documente une licence
(bruitages **Pixabay**, usage commercial libre). Aucune musique du dépôt n'a de licence écrite.
Il faut donc refaire les 7 ambiances, comme le prévoit l'étape 2.

**Bruitages déjà disponibles** pour les effets demandés :

| Effet demandé | Fichier existant |
|---|---|
| Ticket qui s'imprime | `hero-video/assets/sfx/son-imprimante-z.mp3`, `son-etiqueteuse.mp3` |
| Écran qui s'allume / notification | `hero-video/assets/sfx/son-commande-recue.mp3`, `son-iris-publie.mp3`, `son-jarvis-ecoute.mp3`, `media-use/…/sfx/notification.mp3`, `chime.mp3` |
| Ambiance cuisine (friture, service) | `hero-video/assets/sfx/son-ambiance-cuisine-service.mp3`, `son-ambiance-salle-service.mp3` |
| Cloche du passe | `hero-video/assets/sfx/son-clin-passe-take1..3.mp3` (placeholder IA) |
| Bip scanner / caisse | `son-scanner-bip.mp3`, `son-encaissement.mp3`, `son-badge-pointage.mp3` |
| Transitions de BD (pop, whoosh, impact) | `media-use/…/sfx/pop.mp3`, `riser.mp3`, `impact-bass-1/2.mp3`, `click.mp3` (Pixabay) |
| **Téléphone qui sonne** | ❌ absent, à générer (ElevenLabs Sound Effects, étape 2) |
| **Friture isolée** | ❌ absente (seulement dans l'ambiance), à générer |

### 4. Habillages (lower-thirds, transitions, sous-titres, polices)

| Élément | Où | Verdict |
|---|---|---|
| Police **Bangers** (titres de la BD) | `studio-video/.agents/skills/embedded-captions/modes/standard/fonts/files/bangers-latin-400-normal.woff2` | ✅ À copier dans `bd-video/` |
| Police **Comic Neue Bold** (textes de la BD) | — | ❌ Absente. À charger depuis Google Fonts (licence OFL) |
| Sous-titres incrustés (karaoké, mots minutés) | Skill `embedded-captions` + `audio_meta.json` (format `words[]`) des projets `foodeatup-*` | ✅ Même mécanique, avec le style BD (cartouche crème, Comic Neue) |
| Transitions | `videos/*/transitions.mjs` (crossfade, push-slide), skill `seam-craft` | 🟡 À compléter : passage de case en case, page qui tourne |
| Lower-thirds / pastilles | Rien de réutilisable tel quel (gabarits Poppins/Inter, autre charte) | 🔁 À créer : bulle + pastille ronde du personnage, d'après Figma |
| Autres polices (Inter, Poppins, Manrope, Sora…) | 82 fichiers | ❌ Pas dans la charte BD |

## Scripts et projets existants

| Outil | Où | Réutilisable ? |
|---|---|---|
| **HyperFrames (local)** | `studio-video/` (skills dans `.agents/skills/`), ~30 projets `videos/*/hyperframes.json` | ✅ **Oui, outil de montage principal.** CLI `npx hyperframes` 0.8.112 opérationnel ici (`lint`, `validate`, `render`). Rendu local en MP4 H.264, sans coût |
| HyperFrames (MCP HeyGen, hébergé) | — | ⚠️ `compose` et `render_video` sont **désactivés depuis Claude Code**, qui a accès au disque local. Le serveur refuse l'appel et renvoie vers les skills locaux. Seuls `list_projects`, `get_project` et `get_render_status` restent utilisables. **Conséquence pour l'étape 4 :** les projets seront des compositions HyperFrames dans `bd-video/`, rendues en local, sans `project_id` HeyGen. Si tu veux quand même un projet sur le site HeyGen, il faut le lancer depuis Claude.ai |
| Montage ffmpeg de la saison 2 | `videos/foodeatup-saison-2/scripts/monter-episode.sh`, `render-outro.mjs`, `build.mjs` | ✅ Recettes ffmpeg à reprendre : calage voix/bruitages, version muette, miniature, dernière image |
| Assemblage HyperFrames type | `videos/serie-30-routines/` (`captions.mjs`, `assemble-index.mjs`, `transitions.mjs`, `build-episode.sh`) | ✅ Chaîne VO → sous-titres → frames → transitions → rendu à reprendre |
| Moteur audio (`audio_meta.json`, volume BGM 0,18 sous la voix) | `videos/foodeatup-*/audio_engine_meta.json` | ✅ Bonne base pour le ducking. Ajouter une normalisation `loudnorm` à −14 LUFS |
| Génération vidéo hero | `hero-video/hero-build.js`, `hero-video/scripts/` | 🟡 Référence (data JSON → composition) |
| Synchro Drive | `scripts/sync-videos-to-drive.sh` | ✅ Pour stocker les rendus lourds hors Git (voir plus bas) |
| Remotion | Seulement le skill `remotion-to-hyperframes` (conversion) | ❌ Pas de projet Remotion |
| n8n | — | ❌ Aucun workflow n8n dans le dépôt |

## Recommandations

| Quoi | Décision |
|---|---|
| Dessins, texte, portraits, logos | **À extraire de Figma** (étape 1). Rien à réutiliser dans le dépôt |
| Bruitages (41) | **À réutiliser.** Il manque le téléphone et la friture isolée, à générer |
| Logo animé (sting-in / sting-out) | **À réutiliser** en ouverture et fermeture |
| Gabarit d'outro saison 2 | **À adapter** (« Une seule saisie, pas dix » + CTA) |
| Captures du logiciel (245) | **À réutiliser** pour la série « une case, une fonction » |
| Plans Seedance / Higgsfield (83) | **À ignorer dans le film** (style réaliste ≠ BD) · possible en déclinaison LinkedIn |
| Musiques (14) | **À refaire** : 7 ambiances, une par partie, plus l'épilogue |
| Voix (1 479) | **À ignorer** : nouveau casting à l'étape 2 |
| Police Bangers | **À réutiliser** · Comic Neue à ajouter (Google Fonts) |
| Chaîne de montage | **HyperFrames local + recettes ffmpeg de la saison 2** |

## Points d'attention avant la suite

1. **Poids du dépôt :** il pèse déjà 5,4 Go, avec seulement 2 fichiers dans LFS. Pour `bd-video/renders/` (film + épisodes
   + déclinaisons ≈ 1 à 2 Go attendus), je propose :
   - de suivre `bd-video/renders/**/*.mp4` et `bd-video/audio/**` dans **Git LFS** (`.gitattributes`) ;
   - **ou** de garder les rendus hors Git et de les pousser sur Drive avec `scripts/sync-videos-to-drive.sh`,
     le lien allant dans le README.
   👉 À toi de choisir. Par défaut : LFS pour l'audio, Drive pour les rendus vidéo.
2. **Branche :** le travail est sur `feat/bd-video`, comme demandé.
3. **Connecteurs :** Figma, ElevenLabs et RapidoCMS répondent. `Social_FoodEatUp` et `rapidocms_site` ne se
   sont pas connectés dans cette session, mais l'étape 6 utilise `Rapidocms`, qui fonctionne.
4. **Voix de Mickael :** aucun enregistrement fourni. On part sur une voix existante de `creative_list_voices`,
   comme le prévoit la règle « Voix ».

## Relancer l'audit

```bash
pip install webrtcvad-wheels   # détection de voix (facultatif)
python3 bd-video/scripts/audit_media.py
```
