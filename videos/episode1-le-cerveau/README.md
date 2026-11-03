# Épisode 1 · « Le cerveau » : j'ai construit mon équipe d'agents IA

Premier épisode de la série (épisode 2 : `../dimanche-4-apps-1-jeu/` ; épisode 3 : `../lundi-foodeatup-store/`).
Vidéo verticale 1080 × 1920, H.264 30 i/s, AAC, environ −15 LUFS. **Rien n'a été publié.**

## Livrables

| # | Livrable | Fichier |
|---|---|---|
| 1 | Vidéo principale (91 s) | `renders/episode1-le-cerveau_1080x1920.mp4` |
| 2 | Version courte (30,5 s) | `renders/episode1-le-cerveau_30s_1080x1920.mp4` |
| 3 | Miniature « J'ai construit mon équipe IA » | `renders/miniature-episode1-1080x1920.jpg` |
| 4 | Voix off complète | § Voix off + `audio/voix-off-noe.mp3` |
| 5 | Sous-titres SRT (+ ASS) | `sous-titres/` |
| 6–7 | Publications LinkedIn et Instagram | § Publications |
| 8 | Storyboard détaillé | § Storyboard |
| 9 | Sources visuelles et démonstrations | § Sources |

## Vérifications faites avant le montage, et décisions

**1. Rien n'a été fait le samedi 24 octobre dans le dépôt des plugins.**
- `PrendsTaPart/Plugin-Claude-MCP-BraindCode-` n'a **aucun commit le 24/10**.
- Le dernier sprint date du **dimanche 25/10, de 10 h à 15 h (heure de Paris)**. Il crée ou refond six plugins : `foodeatup-tutoriel`, `rapido-employe`, `planit`, `rapido-prospector`, `braindcode-build`, `rapido-youtube`. Il ajoute aussi l'intégration TikTok de `rapidocms`.
- Le lot précédent date du 19/10 ; le gros du catalogue, de juillet.
- Le samedi, la seule activité visible est sur le site de l'Académie (`growth-loop-academy`, via Lovable : e-mails marketing et bulle WhatsApp).

→ **Décision validée avec toi :** un épisode **sans date**, « Le cerveau ». La voix ne dit plus « ce samedi ». L'accroche montre le vrai `git log` du sprint du 25/10.

**2. Les chiffres de la plateforme.**
- Ceux du brief (25 plugins / 129 compétences / 38 agents) ne correspondent à aucun état vérifiable.
- Le site affiche 33 / 544 / 77 en titre, mais 32 / 524 / 71 dans ses compteurs, sur la même page.
- Le dépôt compte aujourd'hui **33 plugins** (`marketplace.json`), **544 SKILL.md** et **77 agents**. J'ai écarté 3 fichiers internes du skill `skill-creator`, qui ne sont pas des agents. La page GitHub du site donne la même chose : « 33 plugins, 544 compétences, 77 agents IA, 85 commandes ».
- À la fin du samedi 24, l'état était de 27 plugins, 414 compétences et 47 agents.

→ **Décision validée :** les chiffres du dépôt aujourd'hui, présentés comme « dans le catalogue aujourd'hui ».

**3. Démonstration.** Aucune exécution d'agent n'est montrée. La scène « mission concrète » affiche la **procédure réelle**, sans résultat inventé :
- le skill `foodeatup/skills/reappro-fournisseurs/SKILL.md` et sa règle « Jamais de commande fournisseur sans validation explicite de l'utilisateur » ;
- le hook `garde-destructif` du plugin FoodEatUp, qui bloque paiements, publications et suppressions ;
- la mention « Aucune exécution n'est montrée ».

Aucun secret ni aucune donnée client n'apparaît. La vidéo ne parle ni de paiement ni de publication autonomes.

## Voix off (voix ElevenLabs « Noé », comme les épisodes 2 et 3 ; ce n'est pas ta voix)

> Pendant longtemps, on développait des logiciels pour que les humains travaillent dessus. Maintenant, je construis des compétences et des agents IA pour que les logiciels puissent aussi travailler avec nous.
>
> Première étape : connecter nos outils métier à Claude grâce aux MCP. Restaurant, CRM, marketing, ressources humaines… Chaque logiciel devient accessible à des agents autorisés.
>
> Mais donner accès aux outils ne suffit pas. Il faut apprendre aux agents comment travailler. D'où les Skills : des compétences qui expliquent les procédures, les règles métier et les étapes à suivre. Il y en a aujourd'hui cinq cent quarante-quatre dans le catalogue.
>
> Ensuite, les agents, organisés par métier : directeur général, directeur commercial, marketing, finance, restaurant… Chacun avec son rôle, ses compétences et ses outils. Soixante-dix-sept agents au total.
>
> Par exemple, un agent peut repérer les stocks bas d'un restaurant et préparer une commande fournisseur. Mais rien ne part sans validation : une commande, un paiement ou une publication attend toujours votre accord.
>
> Et pour rendre tout ça accessible, il y a la marketplace BraindCode : trente-trois plugins à installer dans Claude Code, avec une base de connaissance pour le contexte de votre entreprise.
>
> Le plus intéressant ? Cette équipe IA ne va pas seulement utiliser nos logiciels. Elle va aussi nous aider à en construire de nouveaux. Et dimanche, je suis passé à la pratique.

## Storyboard (91 s)

| Temps | Scène | Images | Lexique à l'écran |
|---|---|---|---|
| 0–11 | Le cerveau | « Avant : des logiciels pour que les humains travaillent dessus » / « Maintenant : des agents IA qui travaillent avec nous », terminal avec le vrai `git log` du sprint du 25/10, logos FoodEatUp, RapidoCRM, RapidoCMS, RapidoRH, Plan'It | — |
| 11–23,6 | MCP | Claude au centre ; FoodEatUp (restaurant), RapidoCRM (CRM), RapidoCMS (marketing), RapidoRH (RH) se branchent au mot près ; « Seulement les agents autorisés » | **MCP** : l'accès aux outils et aux données métier, selon les autorisations |
| 23,6–38,4 | Skills | Téléphone qui défile sur plugin.braindcode.com/competences ; le vrai `SKILL.md` de `reappro-fournisseurs` (nom, description, garde-fous) ; compteur 544 | **Skill** : la méthode (étapes, règles métier, procédures) |
| 38,4–52,4 | Agents | Organigramme des vrais fichiers d'agents : directeur général, directeur commercial, responsable marketing, CFO virtuel, chef-restaurateur ; compteur 77 | **Agent** : un rôle, un objectif, des compétences et des outils |
| 52,4–65 | Mission concrète | Workflow réel « Repérer les stocks bas → Préparer la commande → ✋ Validation humaine → Commander, après accord » ; « Paiement · publication · suppression : bloqués sans votre clic » | **Workflow** : des étapes enchaînées, avec des validations |
| 65–75,8 | Marketplace | Téléphone sur plugin.braindcode.com (accueil, cas d'usage, GitHub, sécurité) ; compteur 33 plugins ; commandes d'installation réelles du README | **Knowledge Base** : le contexte propre à votre entreprise |
| 75,8–85,4 | Teasing | « Cette équipe va aussi nous aider à construire » ; les vraies captures des 4 applis et de Rush arrivent ; « Et dimanche… place à la pratique » | — |
| 85,4–91 | Carton noir | ÉPISODE 1 : LE CERVEAU / DIMANCHE : LES APPLICATIONS / À SUIVRE… / logo BraindCode | — |

**Version 30 s** : accroche (0–9,9) → mission concrète avec la validation humaine (9,9–20,1) → teasing de dimanche (20,1–28,9) → carton (28,9–30,5).

## Sources

| Visuel | Statut | Source |
|---|---|---|
| `git log` du sprint du 25/10 | réel | `PrendsTaPart/Plugin-Claude-MCP-BraindCode-`, heures UTC |
| `SKILL.md` de `reappro-fournisseurs`, garde-fous | réel | `foodeatup/skills/reappro-fournisseurs/SKILL.md` |
| Hook de blocage | réel | `foodeatup/hooks/hooks.json` (`garde-destructif.sh`) |
| Organigramme des agents | réel (noms de fichiers) | `rapido-suite`, `rapidocrm`, `rapidocms`, `rapido-startup`, `foodeatup` /agents |
| Commandes d'installation | réel | `README.md` du dépôt |
| Pages de la marketplace | captures réelles | plugin.braindcode.com : `/`, `/competences`, `/github`, `/securite`, prises le 26/10 |
| Schéma MCP, cartes du lexique | animation explicative | composée pour la vidéo |
| Captures des 4 applis et de Rush | réelles | voir `../dimanche-4-apps-1-jeu/README.md` |
| Logos | officiels | `growth-loop-academy/public/brand/chartes/` |
| Voix, musique | IA | ElevenLabs (voix Noé `eleven_v4` ; musique de l'épisode 2, sans paroles) |

## Publications

### LinkedIn (personnelle)

> Pendant longtemps, on développait des logiciels pour que les humains travaillent dessus.
> Maintenant, je construis des compétences et des agents IA pour que les logiciels puissent aussi travailler avec nous.
>
> Épisode 1 de la série : le cerveau.
>
> 🔌 Les MCP donnent à Claude l'accès à nos outils métier (FoodEatUp, RapidoCRM, RapidoCMS, RapidoRH), selon des autorisations.
> 📘 Les Skills lui apprennent la méthode : étapes, règles métier, garde-fous. 544 aujourd'hui dans le catalogue.
> 👥 Les agents ont un rôle : directeur général, directeur commercial, marketing, CFO, chef-restaurateur… 77 au total.
> 🔁 Les workflows enchaînent les étapes, avec des validations.
> 🧠 La base de connaissance apporte le contexte de chaque entreprise.
>
> Et une règle non négociable : une commande, un paiement ou une publication attend toujours une validation humaine.
>
> Tout est réuni dans la marketplace BraindCode : 33 plugins pour Claude Code, open source → plugin.braindcode.com
>
> La suite ? Cette équipe IA m'aide maintenant à construire de nouveaux logiciels. Épisode 2 : quatre applications et un jeu vidéo en un dimanche.
>
> #IA #AgentsIA #Claude #MCP #BraindCode #FoodEatUp #Entrepreneuriat #BuildInPublic

### Instagram

> Épisode 1 : le cerveau 🧠
>
> Pas un chatbot de plus : une équipe d'agents IA qui sait utiliser nos logiciels 👇
> 🔌 MCP = l'accès aux outils
> 📘 Skills = la méthode (544)
> 👥 Agents = les rôles (77)
> ✋ Et rien ne part sans validation humaine
>
> 33 plugins sur plugin.braindcode.com
> Épisode 2 : les applis 📱
>
> #ia #agentsia #claude #mcp #braindcode #foodeatup #startup #buildinpublic #entrepreneur

## Contrôle

- [x] Chiffres vérifiés dans le dépôt et sur le site ; date de travail vérifiée dans git, et pas attribuée au samedi.
- [x] Lexique MCP / Skill / Agent / Knowledge Base / Workflow expliqué à l'écran en une ligne chacun.
- [x] Aucun agent présenté comme autonome sur les actions sensibles ; validation humaine montrée avec la règle réelle.
- [x] Aucune exécution, aucun résultat commercial ni aucun secret inventé.
- [x] Transition vers l'épisode du dimanche.
- [x] Pas de robot humanoïde : uniquement des interfaces et des fichiers réels.

## Reconstruire

Assets (`a/`) : captures `web2/` de plugin.braindcode.com, logos (`growth-loop-academy/public/brand/chartes/`), vignettes des applis (épisode 2), polices Manrope. Rendu : `node scripts/render.js frames 0 2730` (sert `composition.html` en `index.html` sur le port 8779). Mixage : `scripts/mix-91s.ffmpeg.txt`. Version courte : `scripts/montage-30s.ffmpeg.txt`.
