# Épisode 4 · Les coulisses : je monte mes vidéos avec mes agents IA

Vertical 1080 × 1920, 96 s (+ version de 30,5 s). **Rien n'a été publié.** Un brouillon RapidoCMS est préparé, sans programmation (voir § Démonstration).

## Livrables

| Livrable | Fichier |
|---|---|
| Vidéo principale (96 s) | `renders/episode4-coulisses_1080x1920.mp4` |
| Version courte (30,5 s) | `renders/episode4-coulisses_30s_1080x1920.mp4` |
| Miniature « Je monte mes vidéos avec mes agents IA » | `renders/miniature-episode4-1080x1920.jpg` |
| Schéma du workflow réellement utilisé | `renders/schema-workflow-episode4.jpg` |
| Voix off, storyboard | § ci-dessous · `audio/voix-off-noe.mp3` |
| Sous-titres SRT | `sous-titres/` |
| Publications LinkedIn et Instagram | § ci-dessous |

## Audit des outils : ce qui existe vraiment

**Dépôt `PrendsTaPart/Video`** (branche par défaut : `claude/hyperframes-reels-studio-9f0b63`)
- `studio-video/` : studio de Reels **HyperFrames** (`npx hyperframes render`), plus `heygen_avatar.py`.
- Projets Remotion, FFmpeg, Whisper, ElevenLabs et HeyGen présents dans de nombreux dossiers `videos/`.
- `.claude/skills/` : routines `publication-du-jour`, `trous-de-publication` et `episode-multicanal`, en version d'essai.
- `.claude/settings.json` : hook `garde-fous.sh` qui bloque les envois, suppressions et paiements, plus un journal des appels MCP.

**Plugin Vidéo `rapido-video`** (marketplace BraindCode)
- Skill `montage-express` : `monter.py`, 13 recettes FFmpeg (probe, normalize, concat, cut, xfade, overlay-logo, reframe, speed, extract-audio, mix avec sidechain, remove-silence, burn-srt, title-card, preset).
- `sous_titres.py` : Whisper local → SRT → incrustation.
- Skill `motion-design-remotion` : en mode aperçu tant que la licence Remotion n'est pas tranchée.
- MCP : RapidoCMS et Higgsfield.

**RapidoCMS (MCP)**
- Bibliothèque : `upload_file_tool`, `list_all_files`, `add_asset`.
- Marques : `get_brand`, `create_brand`, `edit_brand`.
- Brouillons : `create_draft_tool`, `edit_draft_tool`, `list_drafts_tool`.
- Programmation : `schedule_draft_tool`, `list_scheduled_posts`, `cancel_schedules_post`.
- Campagnes et statistiques : `create_campagne`, `post_insights`, `ingishts_campagne`.
- Comptes : `list_connected_accounts` (LinkedIn actif, **TikTok expiré**).
- Site rapidocms.com capturé. Le back-office demande une connexion : il n'est pas montré.

### Comment les trois épisodes ont été réellement faits

| Étape | Qui, avec quoi | Automatisé ? |
|---|---|---|
| Brief, idée | toi (prompt) | humain |
| Audit des sources (dépôts, sites, Drive, Lovable, Gmail) | Claude Code (git, Playwright, MCP Drive / Lovable / Gmail) | Claude |
| Vérification des faits (NFC « Bientôt », pas de sondages dans le menu, aucun commit le 24/10, 77 agents) | Claude, puis tes décisions sur le cadrage | Claude + humain |
| Script et storyboard | Claude, validé par toi | Claude + humain |
| Voix off et musique | MCP ElevenLabs (voix Noé, `eleven_v4` ; Music v2.5) | Claude |
| Horodatage des mots | faster-whisper (installé pendant la session) | Claude |
| Scènes animées | compositions HTML écrites par Claude, rendues image par image avec Playwright (4 processus) | Claude |
| Mixage, ducking, sous-titres incrustés, versions courtes | FFmpeg (filtres écrits par Claude, mêmes briques que `rapido-video`) | Claude |
| Recettes `rapido-video` | utilisées **dans cet épisode** : probe, cut, xfade et preset reels sur les 3 épisodes (`demo-rapido-video/journal.txt`) | Claude |
| Bibliothèque, brouillon, programmation | MCP RapidoCMS (vidéo du lundi : brouillon 1821 → publication 1731 à 15 h 45) | Claude, sur ton feu vert |
| Feu vert de publication, accord de Soulayma | toi | humain |

**Honnêteté :** les épisodes 1 à 3 n'ont pas été montés avec `rapido-video` ni avec le studio HyperFrames. Ils l'ont été avec des scripts écrits pour l'occasion (FFmpeg + Whisper + Playwright), qui reprennent les mêmes briques. C'est ce que dit la voix off (« Claude a aussi écrit des scènes animées en HTML, rendues image par image »). Le plugin, lui, est réellement utilisé dans cet épisode pour l'intro.

## Démonstration réelle (cas pratique : les trois épisodes)

1. **Récupération des sources** : planches de captures réelles (fiches Play, rendus Flutter, sites, jeu).
2. **Script et storyboard** : vérifications affichées à l'écran, avec les vrais constats.
3. **Préparation du montage dans le plugin Vidéo** : `monter.py probe` sur les 3 épisodes → `cut` × 3 → `xfade` × 2 → `preset --platform reels`. Le rendu de 11,3 s (`demo-rapido-video/intro-reels.mp4`) ouvre l'épisode.
4. **Voix et sous-titres** : ElevenLabs + Whisper (mots horodatés), chronologie réelle de l'épisode du lundi (voix, 36 sous-titres).
5. **Export vertical** : 1080 × 1920, version longue et version courte.
6. **Préparation du post dans RapidoCMS** : réponses réelles de l'outil (upload, brouillon 1821, programmation 1731, TikTok expiré).
7. **Brouillon pour validation** : cet épisode 4 est déposé dans la bibliothèque RapidoCMS et un **brouillon LinkedIn est créé sans programmation** (voir l'identifiant dans le récapitulatif de la session).

## Voix off

> Vous avez vu mes trois dernières vidéos ? Aujourd'hui, je vous montre comment elles ont été réalisées, avec mes outils IA.
>
> Tout commence par une idée, des captures d'écran, des démonstrations, et un prompt. Claude lit mes dépôts, mes sites et mes fichiers, vérifie ce qui existe vraiment, puis propose le scénario.
>
> Mon plugin Vidéo, rapido-video, apporte les recettes de montage : couper, assembler, mixer la voix et la musique, sous-titrer avec Whisper, exporter au bon format. Pour ces épisodes, Claude a aussi écrit des scènes animées en HTML, rendues image par image.
>
> Au lieu d'assembler à la main, je décris le résultat. Claude enchaîne : la voix off générée avec ElevenLabs, les mots calés à la seconde près, la musique qui baisse sous la voix, les sous-titres incrustés, puis les versions longues et courtes.
>
> Ensuite, RapidoCMS prend le relais : la vidéo part dans la bibliothèque, un brouillon est créé pour le réseau choisi, et la publication est programmée dans le calendrier.
>
> Ce qui reste humain : valider le scénario, les chiffres, l'accord des personnes citées, et le feu vert de publication.
>
> Une idée devient un scénario, puis une vidéo, puis un contenu prêt à être diffusé. Mon objectif, ce n'est pas seulement de créer des vidéos plus vite. C'est de construire une chaîne de production réutilisable, de l'idée jusqu'à la publication.

## Storyboard

| Temps | Scène | Images |
|---|---|---|
| 0–12 | Accroche | Intro de 11,3 s assemblée par `rapido-video` à partir des 3 épisodes |
| 12–25 | Point de départ | Planches réelles des sources, puis les 5 vérifications réelles de Claude |
| 25–41,8 | Plugin Vidéo | Liste des recettes de `monter.py`, journal réel des commandes du jour, 6 images rendues de l'épisode du lundi |
| 41,8–56,2 | Montage | Chronologie réelle de l'épisode du lundi (images, voix, musique, 36 sous-titres), mots horodatés par Whisper, avant/après |
| 56,2–67 | RapidoCMS | Réponses réelles du MCP (upload, brouillon 1821, programmation 1731, TikTok expiré), capture de rapidocms.com |
| 67–75 | Humain | Les 4 validations réelles de cette production |
| 75–88,6 | Workflow | 9 étapes, avec le rôle de chacun (Claude ou humain) |
| 88,6–96 | Carton | PLUGIN VIDÉO × CLAUDE × RAPIDOCMS — « De l'idée à la vidéo. De la vidéo à la communication. » |

**Version 30 s** : accroche → plugin Vidéo → RapidoCMS → carton.

## Publications

**LinkedIn**
> Je ne monte plus mes vidéos comme avant.
>
> Mes 3 derniers épisodes (agents IA, 4 applis et un jeu, le FoodEatUp Store) ont été produits avec Claude, mon plugin Vidéo et RapidoCMS. Voici les coulisses, sans filtre :
>
> ✅ Claude audite mes dépôts et mes sites, et corrige le scénario quand une fonction n'existe pas encore (le paiement NFC, par exemple).
> ✅ La voix off, les mots horodatés, la musique qui baisse sous la voix, les sous-titres, les versions 9:16 : enchaînés par Claude.
> ✅ rapido-video apporte les recettes de montage (couper, enchaîner, exporter au format Reels).
> ✅ RapidoCMS reçoit la vidéo, crée le brouillon et programme la publication.
> ✋ Ce qui reste à moi : valider le scénario, les chiffres, l'accord des personnes citées, et le feu vert de publication.
>
> L'objectif n'est pas seulement d'aller plus vite. C'est une chaîne de production réutilisable, de l'idée à la publication.
>
> #IA #ClaudeCode #Vidéo #Marketing #RapidoCMS #BuildInPublic

**Instagram**
> Les coulisses de mes vidéos 🎬
> Idée → script → voix IA → montage → sous-titres → brouillon → publication
> Claude + mon plugin Vidéo + RapidoCMS 🤖
> Et moi, je valide ✋
> #ia #montagevideo #claude #rapidocms #contentcreator #buildinpublic
