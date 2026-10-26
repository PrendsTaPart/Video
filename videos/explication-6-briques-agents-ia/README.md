# Vidéo explicative : les 6 briques d'une équipe d'agents IA

Indépendante de la série. Elle explique MCP, Skills, Agents, Plugins, Hooks et base de connaissance à partir du dépôt `PrendsTaPart/Plugin-Claude-MCP-BraindCode-` (commit `f126def`).
**Rien n'a été publié.**

## Livrables

| Livrable | Fichier |
|---|---|
| Vidéo pédagogique 16:9, 3 min 00 (YouTube, LinkedIn) | `renders/6-briques-agents-ia_1920x1080.mp4` |
| Version verticale 59 s (Instagram, TikTok, Shorts) | `renders/6-briques-agents-ia_vertical-60s_1080x1920.mp4` |
| Six animations individuelles (une par brique, 18 à 26 s, sous-titrées) | `renders/animations/brique-1-mcp.mp4` … `brique-6-connaissance.mp4` |
| Miniature « MCP + SKILLS + AGENTS + PLUGINS + HOOKS » | `renders/miniature-6-briques-1280x720.jpg` |
| Voix off | `audio/voix-off-noe.mp3` (ElevenLabs, voix Noé, accélérée ×1,06) · § Script |
| Sous-titres SRT (+ ASS) | `sous-titres/` (version 16:9 et version verticale) |
| Publication LinkedIn, description YouTube, sources | ci-dessous |

## Ce qui a été vérifié dans le code (et comment c'est montré)

| Brique | Constat dans le dépôt | À l'écran |
|---|---|---|
| Totaux | 33 plugins (`.claude-plugin/marketplace.json`), 544 `SKILL.md`, 77 agents. Ce dernier total exclut 3 fichiers internes de `rapido-suite/skills/skill-creator`. | Compteurs |
| MCP | 33 fichiers `.mcp.json`, un par plugin. `foodeatup/.mcp.json` → `https://foodeatup.com/api/mcp` (http). | Fichier réel. Tableau de stocks **marqué « Données de démonstration »** : aucun appel n'a été fait sur des données client. |
| Skill | `foodeatup/skills/reappro-fournisseurs/SKILL.md` : workflow `list_low_stocks` → regroupement par fournisseur → `create_supplier_order` après validation ; garde-fou « Jamais de commande fournisseur sans validation explicite ». | Extrait réel, abrégé |
| Agents | `chef-restaurateur` (ratios food cost ≤ 30 %, masse salariale ≤ 35 %, marge ~70 %, seuils lus dans `./rapido-kb/`), `directeur-commercial` (rapidocrm), `directeur-general` (rapido-suite), `cfo-virtuel` (rapido-startup), `community-manager` (rapidocms). | Extrait réel + fiches |
| Plugins | Structure réelle de `foodeatup/` : `.claude-plugin/`, `.mcp.json`, `agents/` (5), `skills/` (27), `hooks/`, `reference/`. Installation : `/plugin marketplace add …` puis `/plugin install foodeatup@rapido` (README). | Arborescence, `marketplace.json` (extrait), capture du site |
| Hooks | Nombre de plugins par événement : PreToolUse 33, Stop 25, SessionStart 9, PostToolUse 6 (UserPromptSubmit 1). Les deux scripts du plugin foodeatup ont été **exécutés** : `anti-donnee-inventee.sh` → `"deny"` si `equipment_id` absent ; `garde-destructif.sh` → `"ask"` (le mécanisme d'approbation de Claude Code). | Sortie réelle du terminal |
| Connaissance | Le dossier `rapido-kb/` n'existe pas dans le dépôt : c'est volontaire, la KB vit chez le client et n'est jamais versionnée (README). Le dépôt fournit le gabarit `rapido-kb-template/` (entreprise, processus-internes, charte-graphique, ton-et-accroches…). | Gabarit réel, comparaison KB / historique |

**Nuances dites ou montrées :**
- `create_supplier_order` **n'est pas** dans le matcher du hook `garde-destructif`. La validation de la commande fournisseur vient de la règle du Skill (une consigne au modèle) et du mode de permissions de Claude Code, pas d'un hook déterministe.
- Le Skill de réapprovisionnement part des stocks bas (`is_low`) : **il ne fait pas de prévision sur trois jours**. La demande « pour les trois prochains jours » est montrée avec cette précision et des données de démonstration.

## Script (voix off)

> Tout le monde parle d'agents IA. Mais comment faire pour qu'une IA ne se contente plus de répondre à des questions, et puisse réellement travailler avec nos logiciels ? Un agent IA performant, ce n'est pas seulement un bon prompt. C'est un rôle, des compétences, des outils, des règles et des automatismes. Six briques. Voyons-les une par une.
>
> Première brique : les MCP, pour Model Context Protocol. Ce sont les mains de l'IA : un protocole qui lui permet de se brancher sur les outils de l'entreprise. Dans le plugin FoodEatUp, une seule ligne de configuration pointe vers le serveur MCP du logiciel. L'agent peut alors, par exemple, consulter les stocks d'un restaurant. Attention : un MCP donne accès aux fonctions autorisées pour le compte connecté. À lui seul, il ne garantit ni l'autonomie, ni la sécurité.
>
> Deuxième brique : les Skills, le savoir-faire. L'IA peut lire les stocks, mais sait-elle quoi en faire ? Un Skill est un fichier, SKILL.md, qui décrit une méthode : quand l'utiliser, les étapes, les règles. Le Skill de réapprovisionnement, par exemple, enchaîne : détecter les stocks bas, regrouper par fournisseur, faire valider, puis commander. Le Skill définit la méthode. Il ne déclenche rien tout seul.
>
> Troisième brique : les agents, les employés spécialisés. Un agent, c'est un rôle, un objectif et des instructions. Le chef-restaurateur raisonne en ratios : food cost, masse salariale, marge. Le directeur commercial pilote le pipeline. Le directeur général croise les signaux. Le catalogue en compte soixante-dix-sept. Un agent reçoit une mission, choisit ses outils et produit un résultat, dans les limites de sa configuration.
>
> Quatrième brique : les plugins, le paquet. Un plugin regroupe des Skills, des agents, des commandes, des Hooks et ses connexions MCP, pour tout installer en une fois. La marketplace BraindCode en propose trente-trois : FoodEatUp, RapidoCRM, RapidoCMS, RapidoRH, Plan'It… Dans Claude Code, deux commandes suffisent : ajouter la marketplace, puis installer le plugin.
>
> Cinquième brique : les Hooks, les réflexes. Un Hook se déclenche sur un événement précis : avant l'appel d'un outil, après, au démarrage d'une session, ou à la fin d'une réponse. Contrairement au modèle, un Hook est déterministe : il réagit toujours de la même façon. Dans FoodEatUp, un Hook refuse un relevé de température sans équipement identifié, et un autre impose une confirmation avant toute action destructrice. Mais attention : une vraie validation humaine passe par un mécanisme d'approbation. Un Hook seul ne fait pas toute la sécurité.
>
> Sixième brique : la connaissance de l'entreprise. Sans contexte, même un agent bien équipé ne connaît ni vos règles, ni vos objectifs, ni vos procédures. La base de connaissance, un dossier rapido-kb créé chez vous, contient vos seuils, vos processus, votre charte et votre ton. Elle persiste d'une session à l'autre, contrairement à l'historique d'une conversation. Et elle n'est jamais publiée dans le dépôt.
>
> Assemblons tout. Un restaurateur demande : analyse mes stocks et prépare mes achats fournisseurs pour les trois prochains jours. Le chef-restaurateur reçoit l'objectif. Il charge le Skill de réapprovisionnement. Le MCP FoodEatUp fournit les données autorisées. La base de connaissance donne les seuils. L'agent prépare ses recommandations. Les Hooks et les permissions encadrent les actions sensibles. Et le restaurateur valide avant toute commande.
>
> C'est en assemblant ces briques qu'on passe d'un chatbot à une équipe d'agents IA spécialisés, capables de réaliser des missions dans les outils de l'entreprise. C'est ce que nous construisons avec BraindCode. À retrouver sur plugin.braindcode.com.

## Storyboard et chapitres

| Temps | Section |
|---|---|
| 0:00 | Accroche : une IA isolée, puis connectée à FoodEatUp, RapidoCRM, RapidoCMS, RapidoRH et Plan'It |
| 0:16 | Brique 1 · MCP : `.mcp.json` réel, stocks de démonstration, limites |
| 0:38 | Brique 2 · Skills : `SKILL.md` réel, chaîne détecter → regrouper → valider → commander |
| 0:59 | Brique 3 · Agents : `chef-restaurateur.md`, 4 autres agents, compteur 77, mission → outils → résultat |
| 1:19 | Brique 4 · Plugins : arborescence, `marketplace.json`, site, commandes d'installation |
| 1:38 | Brique 5 · Hooks : 4 événements, déterministe ou modèle, exécution réelle deny / ask, limites |
| 2:04 | Brique 6 · Connaissance : gabarit `rapido-kb`, KB persistante ou historique |
| 2:24 | Démonstration en 7 étapes (données de démonstration) |
| 2:45 | Conclusion : les six briques et plugin.braindcode.com |

**Version verticale (59 s)** : 8 extraits de la même voix (accroche, une phrase clé par brique, conclusion). L'image 16:9 est au centre, le titre de la brique au-dessus et les sous-titres en dessous.

## Description YouTube

> Comment passer d'un chatbot à une équipe d'agents IA qui travaille vraiment avec vos logiciels ? On décompose l'architecture en six briques, avec les vrais fichiers de la marketplace open source BraindCode (33 plugins, 544 skills, 77 agents).
>
> 0:00 Pourquoi un bon prompt ne suffit pas
> 0:16 MCP : les mains de l'IA
> 0:38 Skills : le savoir-faire
> 0:59 Agents : les employés spécialisés
> 1:19 Plugins : le paquet installable
> 1:38 Hooks : les réflexes déterministes
> 2:04 Base de connaissance : la mémoire métier
> 2:24 Démo : stocks et achats fournisseurs, avec validation humaine
> 2:45 Conclusion
>
> Les données de stock de la démo sont fictives. Aucune donnée client n'est montrée.
> Marketplace : https://plugin.braindcode.com · Code : https://github.com/PrendsTaPart/Plugin-Claude-MCP-BraindCode-
>
> #AgentsIA #ClaudeCode #MCP #IA #Restauration #FoodEatUp #BraindCode

## Publication LinkedIn (pédagogique)

> Un agent IA performant, ce n'est pas seulement un bon prompt.
>
> C'est six briques, que j'ai décortiquées en 3 minutes avec les vrais fichiers de notre marketplace open source :
>
> 1️⃣ MCP : les mains. L'accès aux outils, limité aux fonctions autorisées.
> 2️⃣ Skills : le savoir-faire. Un fichier SKILL.md qui décrit la méthode, sans rien déclencher seul.
> 3️⃣ Agents : les employés spécialisés. Un rôle, un objectif, des instructions.
> 4️⃣ Plugins : le paquet. Skills, agents, hooks et MCP installés en deux commandes.
> 5️⃣ Hooks : les réflexes. Déterministes, ils bloquent ou demandent confirmation avant une action sensible.
> 6️⃣ Base de connaissance : la mémoire métier. Vos seuils, vos procédures, votre charte, persistants d'une session à l'autre.
>
> Ce qui m'a le plus marqué en le montant : un Hook seul ne fait pas la sécurité, et un Skill ne remplace pas une validation humaine. Ce sont les briques ensemble qui font un collaborateur fiable.
>
> 🎥 La vidéo complète (3 min) ⬇️
> 🔗 plugin.braindcode.com
>
> #IA #AgentsIA #ClaudeCode #MCP #Automatisation #PME #BraindCode

## Sources

- Dépôt `PrendsTaPart/Plugin-Claude-MCP-BraindCode-` (commit `f126def`) : `README.md`, `.claude-plugin/marketplace.json`, `foodeatup/.mcp.json`, `foodeatup/skills/reappro-fournisseurs/SKILL.md`, `foodeatup/agents/chef-restaurateur.md`, `foodeatup/hooks/hooks.json` et ses deux scripts (exécutés), les 33 `hooks/hooks.json` (comptage des événements), `reference/registre-routines.md`, `rapido-kb-template/`.
- Captures de plugin.braindcode.com (`/competences`), prises le 26/10/2026.
- Voix et musique : ElevenLabs.
