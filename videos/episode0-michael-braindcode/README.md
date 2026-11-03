# Épisode 0 · Michael, BraindCode et mon écosystème IA

Vertical 1080 × 1920, 118 s (+ version de 45,4 s). **Rien n'a été publié.**

## Livrables

| Livrable | Fichier |
|---|---|
| Vidéo principale (118 s) | `renders/episode0-michael-braindcode_1080x1920.mp4` |
| Version courte (45,4 s) | `renders/episode0-michael-braindcode_45s_1080x1920.mp4` |
| Miniature avec la photo et le logo BraindCode | `renders/miniature-episode0-1080x1920.jpg` |
| Voix off (Noé, ElevenLabs), mixage | `audio/` |
| Sous-titres SRT et ASS | `sous-titres/` |
| Storyboard, publications, sources | ci-dessous |

## Recherche et vérification

**MCP Formation FoodEatUp** (connecté, lecture seule) :
- `get_build_braindcode` (relevé du 07/10) : promesse « Nos logiciels sont ouverts », 4 logiciels MCP, 1 orchestrateur (Plan'It), 37 outils MCP.
- `get_plugin_showcase` : marketplace Rapido, licence Apache 2.0, installation dans Claude Code, claude.ai et Plan'It.
- `list_library` :
  - fiche « BraindCode : l'entreprise et l'équipe » (agence et éditeur fondé par Michael Kebail-Ali, Aubervilliers, développement à Tunis, « vingt ans chef de cuisine, premier commercial ») ;
  - « Texte 4 — Vision du fondateur » (« un logiciel par métier, chacun pilotable par un agent ; l'humain garde la décision ») ;
  - « CE7 » (le fondateur raconte, il ne vend pas).
- `get_claude_brief`, `list_agents`, `list_routines`, `list_decisions` : déjà lus pour l'épisode 6. Résultat : 6 agents « à configurer », 20 routines en V0, une décision. Ces chiffres ne sont pas repris ici.

**Sites officiels capturés le 26/10/2026** : braindcode.com, foodeatup.com, rapidosoftware.com, startupforge.fr, plugin.braindcode.com, rapidocms.com, build.braindcode.com, planit.braindcode.com (redirigé vers la connexion). Les bandeaux cookies ont été refusés avant capture.

**Chiffres affichés**, tous relevés :
- 443 commits dans le dépôt Video ;
- marketplace : 33 plugins, 544 skills, 77 agents (comptés dans le dépôt, et affichés aussi sur plugin.braindcode.com) ;
- 191 outils dans le MCP de l'Academy ;
- Lüks Coffee Recipes : 409 commits, 36 PR.

Aucune certification, aucun chiffre commercial, aucun résultat n'est annoncé. Les distinctions listées dans la bibliothèque (French Tech Tremplin, etc.) ne sont **pas** reprises.

## Photo, logo et voix

- **Photo.** `brand/linkedin/michael/braindcode-profil.jpg`, la photo de profil officielle BraindCode du dépôt growth-loop-academy. C'est la vraie photo de Michael, non générée. Poses officielles : `brand/poses/`.
- **Logo.** `brand/chartes/braindcode.png`, le fichier officiel, proportions respectées.
- **Parcours en cuisine.** Aucune photo réelle trouvée. La scène utilise les planches de la BD de l'Academy, signalées à l'écran « Illustration · la BD de FoodEatUp Academy ». La photo « égérie » en cuisine du site de l'Academy n'est pas utilisée : rien ne permet de dire si elle est réelle ou générée.
- **Voix.**
  - La bibliothèque évoque une « voix clonée de Michael, avec consentement ».
  - Aucune voix de ce type n'existe dans l'espace ElevenLabs connecté : les voix « Michael » trouvées appartiennent à d'autres personnes.
  - J'ai donc gardé la voix de la série (Noé, `eleven_v4`), sans imiter ta voix. Si tu as un modèle vocal autorisé, donne-moi son identifiant et je régénère la voix off.

## Voix off

> Salut, moi c'est Michael. Je suis entrepreneur, fondateur de BraindCode, et depuis plusieurs années, je construis des solutions pour aider les entreprises à travailler autrement grâce à la technologie.
>
> À la base, j'ai passé près de vingt ans dans la restauration, comme chef cuisinier. J'ai appris à gérer les équipes, les stocks, les fournisseurs, les clients et les imprévus. Et j'ai découvert à quel point les entreprises avaient besoin de meilleurs outils.
>
> C'est cette expérience du terrain qui m'a donné envie de créer des solutions concrètes. Aujourd'hui, avec BraindCode, on développe des logiciels, des applications et des agents IA capables d'accompagner les entreprises dans leur quotidien.
>
> Au fil du temps, j'ai construit un écosystème de solutions connectées. FoodEatUp pour les restaurateurs. RapidoSoftware pour la gestion des entreprises. StartupForge pour accompagner les entrepreneurs. Et des outils qui permettent de connecter les agents IA à tous ces logiciels.
>
> Aujourd'hui, je ne veux plus seulement créer des logiciels que les humains utilisent. Je veux aussi construire des équipes d'agents IA capables d'utiliser ces logiciels, d'apprendre des procédures métier et de nous aider à atteindre nos objectifs.
>
> Et j'ai décidé de partager cette aventure avec vous. Pas seulement les réussites, mais aussi les idées, les tests, les développements, les difficultés, et tout ce qu'on construit au quotidien.
>
> À partir d'aujourd'hui, je vais vous présenter chaque jour mon histoire et mon travail du jour. Bienvenue dans mon quotidien. Bienvenue dans l'univers BraindCode.

## Storyboard

| Temps | Scène | Images |
|---|---|---|
| 0–12 | Qui suis-je ? | Photo de profil officielle, « MICHAEL », « ENTREPRENEUR & FONDATEUR DE BRAINDCODE », logo officiel |
| 12–24,6 | Mon parcours | 4 planches de la BD (illustration signalée), pastilles équipes, stocks, fournisseurs, clients, imprévus, « Besoin de meilleurs outils » |
| 24,6–36,6 | BraindCode | Logo, braindcode.com sur tablette, « LOGICIELS • APPLICATIONS • AGENTS IA » |
| 36,6–50,6 | L'écosystème | 4 cartes avec captures réelles : FoodEatUp, RapidoSoftware (CRM, CMS, RH), StartupForge, Plugins et Plan'It |
| 50,6–62,4 | Les vraies interfaces, sans voix | 10 captures réelles : FoodEatUp, hub, RapidoCRM, RapidoCMS, RapidoSoftware, StartupForge, marketplace, Build, Plan'It |
| 62,4–74,4 | Ma vision | Agents IA reliés par MCP à 6 logiciels. DES OUTILS CONNECTÉS → DES AGENTS IA → DES COMPÉTENCES → DES OBJECTIFS. Mission réelle de l'épisode 9 |
| 74,4–84 | Pourquoi cette série | Miniatures des épisodes 1, 4, 6, 9. Idées, tests, développements, difficultés |
| 84–93,6 | Les coulisses, sans voix | Terminal avec les chiffres relevés des dépôts, Michael à l'ordinateur |
| 93,6–102,4 | Ma promesse | Photo, « Chaque jour : mon histoire et mon travail du jour », « Bienvenue… » |
| 102,4–109,6 | Au programme | Miniatures des épisodes 5, 9, 6, 4 |
| 109,6–118 | Carton | MICHAEL × BRAINDCODE · MON QUOTIDIEN D'ENTREPRENEUR AVEC L'IA · UN NOUVEL ÉPISODE CHAQUE JOUR |

**Version 45 s** : qui suis-je → écosystème → vision → promesse.

## Publications

**LinkedIn**
> Salut, moi c'est Michael.
>
> Avant d'écrire du code, j'ai passé près de vingt ans en cuisine, comme chef. Les équipes, les stocks, les fournisseurs, les clients, les imprévus : j'ai vu de près ce qui manque aux entreprises, de meilleurs outils.
>
> C'est pour ça que j'ai créé BraindCode. On y développe des logiciels, des applications et des agents IA :
> 🍽 FoodEatUp pour les restaurateurs
> 🧩 RapidoSoftware (RapidoCRM, RapidoCMS, RapidoRH) pour la gestion des entreprises
> 🚀 StartupForge pour accompagner les entrepreneurs
> 🔌 des plugins et des connexions MCP pour que les agents IA utilisent tous ces logiciels
>
> À partir d'aujourd'hui, je partage chaque jour mon histoire et mon travail du jour : les réussites, mais aussi les tests, les ratés et les coulisses.
>
> Bienvenue dans mon quotidien. Bienvenue dans l'univers BraindCode.
>
> #Entrepreneur #IA #BuildInPublic #BraindCode #FoodEatUp

**Instagram**
> Épisode 0 👋 Moi c'est Michael
> 20 ans en cuisine 👨‍🍳 → fondateur de BraindCode 💻
> Logiciels, applications, agents IA
> Un nouvel épisode chaque jour 🎬
> #entrepreneur #ia #buildinpublic #braindcode #foodeatup

## Sources visuelles

| Visuel | Provenance |
|---|---|
| Photo de profil | `growth-loop-academy/public/brand/linkedin/michael/braindcode-profil.jpg` |
| Poses de Michael | `growth-loop-academy/public/brand/poses/` |
| Logo BraindCode | `growth-loop-academy/public/brand/chartes/braindcode.png` |
| Planches BD (cuisine) | `growth-loop-academy/public/brand/bd-accueil/1, 2, 3, 7.webp` |
| Sites | Captures Playwright du 26/10/2026 (8 sites) |
| Écrans RapidoCRM, RapidoCMS, hub FoodEatUp | `growth-loop-academy/public/brand/logiciels/` et `projets/` |
| Miniatures des épisodes | `Video/videos/*/renders/miniature-*.jpg` |
| Musique | Bibliothèque de la série (ElevenLabs Music, sans voix) |
