# Prompt de reprise — série « Mes projets en pub » (épisodes 93 à 124) et site michael.foodeatup.fr

Tu reprends un travail en cours pour Michael (Journal de Michael, michael.foodeatup.fr). Dépôt `PrendsTaPart/Video`, branche `ccr-a304295a-7288w6` (crée-la depuis origin si absente, pousse uniquement dessus). Lis d'abord `CLAUDE.md` à la racine : ses règles priment sur tout.

## Règles non négociables
- **Une seule prise** pour toute génération (voix ElevenLabs, image) : `generations_count=1`. Ne jamais relancer une génération « pour comparer ». Jamais de vidéo Higgsfield (si un plan vidéo manque, donner le prompt à Michael).
- **Aucun chiffre dans les voix off** (nombre de projets, de vidéos, d'épisodes…) : les projets et vidéos évoluent. Pas de chiffre figé à l'écran non plus (badge « MES PROJETS EN PUB », pas « 30 »). Le n° d'épisode dans le badge est autorisé.
- Aucun prix, résultat, client ou écran inventé. Pas de terme technique : on dit « équipier », jamais « serveur ». Tutoiement, ton simple.
- Logos officiels uniquement. Portrait de Michael : photo en veste (`videos/_journal-63-72/commun/michael-rond.png`), jamais la photo en tenue de chef.
- Toute image IA est signalée à l'écran (« Image d'illustration générée par IA ») et ajoutée à la bibliothèque (`ajouter_media`, source « Génération IA … », tag du slug du projet). Avant toute image : chercher dans `lister_assets` / `lister_medias` / kit du projet. Appeler `estimer_cout_generation_ia` avant une génération payante.
- Chaque nouvel asset lié à un projet (image, capture, vignette, vidéo) est rattaché au projet (`ajouter_media` avec le tag du slug, ou `ajouter_asset_projet`).
- **Rien n'est publié sur les réseaux, et aucun email n'est envoyé, sans l'accord explicite de Michael.** Tout naît en brouillon.
- Jamais de clé ou secret dans le chat. Pas d'identifiant de modèle dans les commits ; terminer les messages de commit par les lignes d'attribution fournies par ta session.

## État au 31/10/2026
- **Pilotes validés par Michael** : 93 (intro de la série) et 94 (pub FoodEatUp Caisse Mobile), version sans chiffres.
  - `videos/episode93-mes-30-projets/` et `videos/episode94-pub-caisse-mobile/` (script.txt, voix/voix.mp3, cfg.json, spec.json, assets/, index.html, MP4 rendu).
- **Moteur** : `videos/pubs-projets/engine/pub.py <dossier>` lit `spec.json` + `cfg.json` et écrit l'`index.html` HyperFrames 1080x1920 (scènes : hook, photo, reveal, feature, card, cta, wall, chips ; sous-titres karaoké ; avatar 3D ; musique). **Copie le dossier 94 comme modèle** (package.json, hyperframes.json, meta.json, .gitignore, assets/avatar-*.png, assets/musique.mp3).
- **Plan** : `videos/pubs-projets/plan.json` (ordre des 30 projets 94→123, exclusions, structure d'une pub). Flows de voix : `videos/pubs-projets/voix-flows.json` (à compléter à chaque épisode).
- **Données projets** : `videos/_journal-63-72/commun/ecrans-projets/` (`<slug>-desktop.jpg`, `<slug>-mobile.jpg`, `content.json`, `struct.json`, `faq.json`, `pages.json` = contenus réels relevés sur les sites) ; logos officiels dans `videos/_journal-63-72/commun/logos-projets/`.
- **Site** : toutes les pages projet et les 7 projets qui étaient indisponibles sont publiés. Intro cinématographique avec voix (sans chiffres) en ouverture du site, son activé par défaut (repli « Activer le son » si le navigateur bloque) ; MP4 sur RapidoCMS : `intro-accueil-1920x1080.mp4`, `intro-accueil-1080x1920.mp4`. Un message a été envoyé à Lovable (projet `255f6f6f-ae7c-4ba7-8c89-c6e431c71eef`) : nouveaux sous-titres WebVTT, retirer les nombres écrits en dur, vérifier l'affichage des sections. Lovable ne déploie pas : Michael republie lui-même.

- **Publié le 31/10** : épisodes 93 (`episode-93-mes-projets-passent-en-pub`) et 94 (`episode-94-la-commande-a-table-l-encaissement-dans-la-poche`) sur le Journal ; MP4 et vignettes dans RapidoCMS ; tous les projets et toutes les pages projet publiés ; site redéployé.
- **Réseaux** : comptes actifs dans RapidoCMS = LinkedIn page RapidoCMS (`146076025`) et Instagram RapidoCMS (`17841429685571827`). Instagram Rapido Software, Facebook RapidoSofware, LinkedIn RapidoSoftware et profil LinkedIn de Michael sont expirés ; **aucun compte TikTok ni YouTube** n'est connecté : ces deux réseaux sont mis à l'agenda du Journal (`planifier_publication`) pour une publication à la main. Programmation : une pub par jour à 18 h (93 le 31/10, 94 le 01/11, puis 95 le 02/11, etc.). Format d'heure de `schedule_draft_tool` : `H:i:s` ; `planifier_publication` veut une date ISO en UTC (`…Z`).
- Michael a donné son accord le 31/10 pour publier les épisodes de la série et les programmer sur les réseaux dans cette cadence, une fois chaque lot validé par lui en vidéo.

## Travail à réaliser, dans l'ordre

### 1. FAQ manquantes des pages projet
Pages publiées sans FAQ : foodeatup, rapidocrm, rapidocms, plan-it, rapidosoftware, rapidorh, braindcode, braindcode-build, braindcode-plugins, formation-entrepreneurs, releasesync, rapidomeet, plateforme-assurance, citycar, la-chaine-fraternelles, foodeatup-laboratoire, foodeatup-borne-drive, fiche-technique-foodeatup, villa-beach, coach-cuisine, alto. Il manque aussi souvent « Comment ça marche » (`etapes_fonctionnement`).
- Pour chacune : `obtenir_page_projet`, puis lire le **site réel** du projet (Playwright ; accordéons radix : cliquer chaque bouton et lire `[aria-labelledby=id]`) et `content.json`/`struct.json`.
- Écrire 4 à 6 questions/réponses **uniquement à partir de ce que dit le site** (rien d'inventé : ni prix, ni chiffre, ni fonction absente). Compléter les étapes si le site les décrit.
- `modifier_page_projet` (sections fournies seulement), puis `publier_page_projet` (accord donné par Michael le 31/10 pour publier ces pages).
- Vérifier en ligne : `/projets/<slug>` affiche « Questions fréquentes ».

### 2. Hero de l'accueil sans chiffres
`videos/hero-accueil/index.html` et `mobile/index.html` affichent des compteurs « 46 projets » et « 130+ vidéos » (ids `n1`, `n2`, tweens vers 46 et 130). Les remplacer par une formule sans chiffre (ex. « Des projets » / « Des vidéos chaque semaine »), `npx hyperframes check`, snapshot, rendu des deux formats, upload RapidoCMS **sous les mêmes noms** (`hero-accueil-1920x1080.mp4`, `hero-accueil-1080x1920.mp4`) avec une URL raw GitHub sur le commit.

### 3. Les 29 pubs 95 → 123 (ordre de `plan.json`)
Pour chaque projet :
1. `obtenir_projet`, `obtenir_page_projet`, `lister_assets(projet_slug)` : hook, punchline, bénéfices, charte (couleurs → `theme` du spec), écrans, icônes, mockups, cartes du kit Lovable.
2. **Script** (8 lignes, ~25 s) : punchline → problème vécu → ce que ça coûte → révélation « Voici <nom> » → 3 bénéfices concrets → CTA (« clique sur le lien et essaie… »). Aucun chiffre. Vérifier avec `preparer_episode` / `obtenir_methode_video`.
3. **Voix** : `creative_generate_speech`, voix Noé `7pDdnNI6PhXmAp0pXFZm`, `eleven_v4`, `generations_count=1`. Télécharger dans `voix/voix.mp3`, noter flow + generation dans `voix-flows.json`.
4. **Alignement** : `python3 videos/_journal-63-72/engine/build_cfg.py <dossier>` (supprimer `voix/words.json` s'il existe d'une ancienne voix).
5. **Assets** : télécharger écrans/kit/logo dans `assets/`. Image IA d'ambiance pour la scène « problème » seulement si rien n'existe (une prise, `bytedance-seedream-5-pro`, signalée à l'écran, ajoutée à la bibliothèque).
6. **spec.json** sur le modèle du 94 (badge « MES PROJETS EN PUB », `avatar` sur 2-3 lignes sans masquer le texte), `python3 videos/pubs-projets/engine/pub.py <dossier>`, `npx hyperframes check`, `npx hyperframes snapshot --at …` et **regarder** la planche avant de rendre.
7. **Rendu au premier plan** (un rendu en arrière-plan est annulé quand la commande parente se termine) : `cd <dossier> && timeout 1500 npx hyperframes render -o <dossier>.mp4`.
8. Vignette au design des couvertures projet (`videos/mes-projets/vignettes/` : `data.json` + `node make.js`, ou `generer_couvertures_projet`), jamais une image extraite de la vidéo.
9. Commit + push par lot de quelques épisodes ; upload RapidoCMS (`upload_file_tool`, URL raw GitHub sur le commit) ; rattacher vidéo et vignette au projet.

Nommage des dossiers : `videos/episode<NN>-pub-<slug-court>/`.

### 4. Épisode 124 — la méthode
Comment ces pubs ont été faites : contexte projet récupéré par le MCP du Journal → script → voix en une prise → alignement → moteur HyperFrames → rendu → publication. Montrer de vrais écrans (planches de snapshot, spec.json, bibliothèque). Mêmes règles, sans chiffres.

### 5. Préparer la publication (sans rien envoyer)
Pour chaque épisode 93 → 124 : `creer_video` (série quotidien, numéro d'épisode, projet lié), `planifier_publication` (une par jour à partir de la date que Michael choisira), dépôt RapidoCMS, posts TikTok / Instagram / LinkedIn / YouTube préparés via la skill `episode-multicanal` / `preparer_publication`. **Tout reste en brouillon** : présenter le calendrier à Michael et attendre son accord avant `publier_video` ou toute diffusion.

## Pièges connus
- `ajouter_media` : `source` ≤ 200 caractères.
- ffmpeg : mettre `-ss` **avant** `-i` pour découper (sinon fondus décalés et segment muet).
- HyperFrames : `check --json` doit être sans erreur ; contraste des textes gris (assombrir le fond si l'outil le signale).
- Lovable : `send_message` avec `wait=false` ; lire les réponses avec jq (réponses très longues).
- Ne pas appeler `modifier_projet` / `ajouter_asset_projet` en rafale sans vérifier que les couvertures actives le restent (`couvertures_a_activer` dans la réponse).

## Fin de mission
Envoyer à Michael les MP4 par lots pour validation, un récapitulatif (épisodes faits, images IA générées et leur coût, ce qui reste en brouillon), et lui rappeler de republier le site dans Lovable.
