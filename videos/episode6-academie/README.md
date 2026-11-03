# Épisode 6 · J'ai créé une école pour former mes employés IA

*Comment FoodEatUp Academy transforme Claude en collaborateur métier.*

Vertical 1080 × 1920, 118,5 s (+ version de 45,7 s), style bande dessinée. **Rien n'a été publié, rien n'a été écrit dans l'Academy.**

## Livrables

| Livrable | Fichier |
|---|---|
| Vidéo principale (118,5 s) | `renders/episode6-academie_1080x1920.mp4` |
| Version courte (45,7 s) | `renders/episode6-academie_45s_1080x1920.mp4` |
| Miniature « J'ai créé une école pour mes employés IA » | `renders/miniature-episode6-1080x1920.jpg` |
| Schéma Academy → MCP → Claude → Agent → Routine → KPI → Amélioration | `renders/schema-academy-mcp-claude-agent-routine-kpi.jpg` |
| Voix off (Noé, ElevenLabs `eleven_v4`), mixage | `audio/` |
| Sous-titres SRT et ASS (118 s et 45 s) | `sous-titres/` |
| Captures réelles du site | `captures/` |
| Script de voix off, storyboard, publications, rapport de vérification | ci-dessous |

## Rapport : ce qui a été vérifié

Audit en **lecture seule** du MCP « Formation FoodEatUp », le 26/10/2026, avec le compte `cocuisinage.social` (rôle apprenant).

**Aucun appel d'écriture** : pas de `remember`, `configure_routine`, `create_routine`, `set_agent_state`, `log_routine_run` ni `set_routine_verdict`.

| Appel | Réponse réelle | Dans la vidéo |
|---|---|---|
| `describe_server` | 191 outils (122 en lecture, 69 en écriture). Toute écriture demande `confirm=true`, sinon aperçu. V0 → V1 après 3 exécutions ; V1 → V2 avec un KPI et 14 jours de mesures. Verdicts : gardée, ajustée, arrêtée. Autonomie : Aperçu, Brouillon, Confirmé | Scènes 3 et 6, schéma |
| `get_claude_brief` | Mémoire vide, savoir d'équipe vide, 0 mission validée, une décision du responsable | Scène 4 |
| `recall` | `notes: []`, `propositions_en_attente: []` | Scène 4 |
| `list_decisions` | « prescripteurs : 20 », depuis le 11/10/2026 | Scène 4 |
| `list_formations` | Parcours dont FoodEatUp (12 missions), Marketing (7), Prospection (7), Piloter FoodEatUp par son MCP (4)… | Scène 3 |
| `list_agents` | 6 agents : Accueil des demandes, Relance et devis, Prescripteurs, Contenus, Veille, Pilotage. Tous **« à configurer »**, autonomie Aperçu, gouvernance « validation humaine », KPI vide | Scène 5 |
| `list_routines` | 20 routines, **toutes en V0**, aucun verdict | Scène 6 |
| `get_kpi_dashboard` | 0 KPI suivi, 0 mesure | Scène 8, schéma |
| `list_connectors` | 11 connecteurs proposés, aucun coché | Non montré |
| `get_mission("F3")` | « Stocks et commandes fournisseurs ». Règle : « préparer, montrer, attendre l'accord » | Démo |
| `check_quiz_answer("f3q1", 0)` | correct : « Un humain » envoie la commande | Démo |
| `check_routine_prompt` (routine stock proposée) | 6/6 : objectif, sources, limite, rendu, critère d'arrêt, accord humain | Démo |
| `list_learners`, `team_report` | « Réservé au responsable » | Non montré |

Le site formation.foodeatup.fr est capturé sur ses pages publiques (`/`, `/formations` : « Quatre-vingt-cinq formations… 464 missions »). Les autres pages demandent une connexion et ne sont pas montrées.

### Garde-fous respectés dans le texte et l'image

- **Mémoire.** La voix off précise : « Ces notes sont réinjectées dans son contexte de travail : le modèle n'est pas réentraîné. »
- **Agents.** Tous apparaissent avec le tampon « à configurer ». Aucun n'est présenté comme en service.
- **Routines.** Le texte dit « Pour qu'elles tournent seules, il faut un orchestrateur réellement configuré », et l'écran ajoute : « Ce n'est pas encore le cas. »
- **Démo de l'agent Stock (aperçu seulement).**
  - `configure_routine` n'a **pas** été appelé.
  - L'agent Stock n'est pas créé et la routine n'est pas activée : elles attendent ta validation.
  - Prompt de la routine proposée : voir § Routine proposée.
- **Michael.** Ses poses détourées et le fondateur en BD proviennent du dossier officiel `public/brand/` du dépôt `growth-loop-academy`, cité par `get_brand_guidelines`.

### Choix artistiques et écarts

- **Style BD.** Planches `bd-accueil` de l'Academy, contours noirs épais, bulles, récitatifs crème, trame de points bleus.
  - La planche 6 (petits robots) est écartée, conformément à la consigne « pas de robots humanoïdes ».
  - Les portraits `agents-ia/*` ne sont pas utilisés : ils ne correspondent pas aux 6 agents réels de l'Academy.
- **Charte (`get_brand_guidelines`).**
  - Nuit #0F1A23, bleu #007BFF, orange #FFA500, crème #FCF9E6.
  - Sous-titres crème sur bande nuit.
  - Logo officiel en bas à droite : le fichier `foodeatup.webp` dans une pastille blanche, avec la mention « Academy », comme dans l'en-tête du site.
- **Police.** Goodly n'est pas déployée : `formation.foodeatup.fr/fonts/goodly/` renvoie 404. J'ai utilisé Poppins, la police déjà présente dans le dépôt.
- **Écartés.**
  - Les captures `premiers-pas/claude/memoire*.webp` montrent la mémoire de Claude.ai, pas celle de l'Academy.
  - L'image de la mission F3 redirige vers la connexion.
- **Plugin Vidéo.** Il n'a pas servi pour cet épisode. Les scènes sont du HTML rendu image par image avec Playwright, puis assemblé avec FFmpeg : mixage avec ducking et sous-titres incrustés.

### Routine proposée (non créée)

```
Objectif : chaque matin, repérer les produits en stock bas du restaurant et préparer une proposition de commande par fournisseur.
Sources : le MCP FoodEatUp (list_low_stocks, list_suppliers) et la mission F3 « Stocks et commandes fournisseurs ».
Limite : lecture seule ; aucune commande créée ni envoyée ; dix produits au plus.
Tu rends : la liste des produits en stock bas, la quantité proposée et le fournisseur, en cinq lignes de résumé.
Critère d'arrêt : tous les produits en stock bas passés en revue, ou « aucun stock bas aujourd'hui » en une ligne.
Ne publie rien et n'envoie rien : prépare, puis attends mon accord.
```

Pour la créer, il faut ton feu vert, puis `configure_routine` avec `confirm=true`, rattachée à un agent en autonomie Aperçu.

## Voix off

> Aujourd'hui, tout le monde parle d'employés IA. Mais il y a une question que presque personne ne pose : comment est-ce qu'on les forme à leur métier ?
>
> Dans mes entreprises, j'ai développé beaucoup de logiciels et de connexions MCP. Mais donner des outils à une intelligence artificielle ne suffit pas. Elle doit aussi comprendre nos méthodes, nos règles et nos objectifs.
>
> J'ai donc développé FoodEatUp Academy. Une plateforme de formation avec des parcours, des missions, des quiz, des exercices et un suivi des compétences.
>
> Et j'ai connecté cette Académie directement à Claude, grâce à son propre MCP. Claude peut consulter les formations, récupérer les procédures, et utiliser les connaissances adaptées à ses missions.
>
> J'ai aussi ajouté une mémoire. Claude peut retrouver les préférences, les objectifs, les corrections et les méthodes qui ont fonctionné. Ces notes sont réinjectées dans son contexte de travail : le modèle n'est pas réentraîné. Et certaines connaissances peuvent être validées par le responsable, pour être partagées avec toute l'équipe.
>
> Ensuite, je peux préparer des agents spécialisés : commercial, marketing, gestion, formation ou pilotage. Chaque agent possède un rôle, des outils autorisés et des objectifs à atteindre.
>
> Et c'est là que ça devient intéressant. Je peux définir des routines, leur donner un objectif, mesurer les résultats, et décider si la méthode doit être conservée, améliorée ou arrêtée. Pour qu'elles tournent seules, il faut un orchestrateur réellement configuré.
>
> Mon objectif, ce n'est pas simplement d'avoir des agents IA qui répondent à des questions. C'est de construire une équipe qui connaît nos métiers, utilise nos outils, suit nos objectifs, et améliore progressivement ses méthodes. Et demain, je vous montrerai une nouvelle étape de cette aventure.

## Storyboard

| Temps | Scène | Images |
|---|---|---|
| 0–10,2 | Accroche | Titre BD sur la planche 1 de l'Academy, puis Michael (pose « réfléchit ») et deux bulles : « Tout le monde parle d'employés IA… » et « … mais comment on les forme à leur métier ? » |
| 10,2–21,7 | Le problème | Liste réelle de mes connexions MCP. Michael, index levé. Pastilles « nos méthodes · nos règles · nos objectifs ». Récitatif « sait appuyer sur les boutons, pas encore comment on travaille » |
| 21,7–31,2 | L'Academy | Logo officiel. Deux captures réelles du catalogue BD. Pastilles « parcours, missions, quiz, exercices, suivi des compétences » |
| 31,2–41,8 | Le MCP | Academy ↔ Claude. Réponses réelles de `describe_server`, `list_formations` et `get_mission("F3")` |
| 41,8–57,7 | La mémoire | Notes → contexte → modèle inchangé, tampon « pas réentraîné ». Réponses réelles de `get_claude_brief`, `recall` et `list_decisions` |
| 57,7–68,1 | Les agents | Les 5 familles citées, puis les 6 agents réels de `list_agents`, tamponnés « à configurer » |
| 68,1–81,4 | Les routines | V0 → V1 → V2. Tampons gardée / ajustée / arrêtée. `list_routines` : 20 routines en V0. Avertissement sur l'orchestrateur |
| 81,4–97,3 | Démo réelle, sans voix | Planche en 4 cases : mission F3, quiz f3q1 ✓, routine 6/6, `configure_routine` non appelé (tampon « aperçu ») |
| 97,3–111,3 | La boucle | Academy → MCP → Claude → Agent → Routine → KPI → Amélioration. Michael, bras ouverts. État réel : 6 agents à configurer · 20 routines V0 · 0 KPI |
| 111,3–118,5 | Carton | « J'AI CRÉÉ UNE ÉCOLE POUR MES EMPLOYÉS IA » · « Demain : une nouvelle étape » · formation.foodeatup.fr |

**Version 45 s** : accroche → Academy → agents → routines → carton.

## Publications

**LinkedIn**
> Tout le monde parle d'employés IA. Presque personne ne parle de leur formation.
>
> Brancher Claude sur mes logiciels (FoodEatUp, RapidoCRM, RapidoCMS, Plan'It…) lui donne des mains. Pas nos méthodes.
>
> J'ai donc créé FoodEatUp Academy : des parcours, des missions, des quiz et un suivi des compétences. Puis je l'ai connectée à Claude par son propre serveur MCP, avec 191 outils.
>
> 🧠 Une mémoire : préférences, corrections et méthodes qui ont marché, relues en début de conversation. Le modèle n'est pas réentraîné ; ses notes lui sont redonnées.
> 👥 Des agents préparés : un rôle, des connecteurs autorisés, un objectif. Aujourd'hui, ils sont tous « à configurer ».
> 🔁 Des routines mesurées : V0 → V1 → V2, puis un verdict humain chaque vendredi (gardée, ajustée ou arrêtée). Pour qu'elles tournent seules, il faudra un orchestrateur.
>
> Dans la vidéo, je forme un futur agent Stock : mission, quiz, première routine notée 6/6… et rien n'est créé sans mon accord.
>
> L'objectif : une équipe qui connaît nos métiers et améliore ses méthodes.
>
> #IA #ClaudeCode #MCP #Formation #FoodEatUp #BuildInPublic

**Instagram**
> J'ai créé une école pour mes employés IA 🎓
> Academy → MCP → Claude → Agent → Routine → KPI → Amélioration
> La mémoire est relue, pas réentraînée 🧠
> Rien ne part sans mon accord ✋
> #ia #claude #formation #foodeatup #entrepreneur #buildinpublic
