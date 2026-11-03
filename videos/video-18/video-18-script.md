# Vidéo 18 · Je dirige mes agents IA ! (Plan'It)

Format vertical 1080 × 1920, 59 s. Voix Noé (ElevenLabs, eleven_v4). **Lecture seule : aucune tâche, routine, campagne ni message n'a été créé ou envoyé.**

## Voix off

> Aujourd'hui, je vais te montrer comment je dirige mon équipe d'agents IA.
>
> Parce que créer un agent IA, c'est bien… Mais quand tu commences à en avoir plusieurs, il faut aussi organiser leur travail !
>
> Alors, j'ai développé Plan'It. C'est l'outil qui me permet de planifier des tâches, de connecter mes MCP et de suivre mes routines.
>
> Je donne un objectif : « Organise ma campagne commerciale FoodEatUp de la semaine. » L'orchestrateur choisit les bons outils : RapidoCRM pour les campagnes, FoodEatUp pour l'agenda marketing.
>
> Ensuite, j'en fais des tâches ou des routines, avec le coût affiché avant chaque exécution.
>
> Et grâce aux connexions MCP, mes agents travaillent directement avec mes logiciels.
>
> Mais rien de sensible ne part sans mon accord : les envois, les publications et les suppressions attendent ma validation.
>
> Je retrouve ensuite les tâches, leur avancement et les résultats dans une seule application.
>
> Pour l'instant, je teste encore mes premières routines. Mais avant, j'organisais moi-même le travail de mes IA. Maintenant, c'est Plan'It qui l'organise.
>
> Mon objectif ? Construire une véritable équipe d'employés IA qui travaille avec mes logiciels !

## Changements par rapport à ton script

- « définir un objectif, préparer les prompts, choisir les outils » est montré avec un **vrai appel** `route_orchestrator` sur ta demande ;
- ajout du coût affiché avant exécution (`estimate_routine_cost`) et de la validation humaine (`list_destructive_tools`) ;
- ajout de « Pour l'instant, je teste encore mes premières routines » : ton compte n'a aujourd'hui **aucune** routine active ;
- « Avant, je devais organiser le travail de mes IA. Maintenant, j'utilise Plan'It pour organiser leur travail » disait deux fois la même chose : reformulé en « j'organisais moi-même… Maintenant, c'est Plan'It qui l'organise ».

## Ordre suivi

1. **MCP Plan'It** (lecture seule) : 63 outils. `list_tasks` 0, `list_routines` 0, `list_prompts` 0, `list_active_loops` 0, `list_pending_routine_actions` 0, `get_calendar` (26/10–01/11) vide, `get_kpi_home` 25 crédits et 0 action sur 7 jours, `list_mcp_servers` 8 connecteurs (Plan'It natif 63 outils, FoodEatUp 193, RapidoCRM 131, RapidoCMS 45, RapidoRH 22, plugins BraindCode 53, carte FoodEatUp 201, Braincast 38).
   - `route_orchestrator("Organise ma campagne commerciale FoodEatUp de la semaine…")` : retient `rapidocrm.list_campagnes`, `rapidocrm.list_newsletters`, `foodeatup.get_marketing_calendar`, `foodeatup.add_marketing_event`, `plugin_braindcode.ma_semaine` ; **agents : []**. RapidoCMS n'est pas retenu par l'orchestrateur sur cette phrase.
   - `estimate_routine_cost` (brouillon hebdomadaire) : 1 crédit par exécution, 4 par mois, base « flat_price » (pas une mesure).
   - `recommend_routines` : 5 candidats (crédits consommés, actions livrées, taux de réussite, jours d'autonomie, coût par action). **Rien n'a été créé.**
   - `list_destructive_tools` : 10 outils à confirmation obligatoire (run_routine_now, accept_routine_proposal, apply_routine_improvement, resume_routine, pause_routine, delete_task, delete_prompt, remove_mcp_server, remove_kpi_widget, unsubscribe_event).
2. **Dépôt `planit-app`** (Flutter 1.0.0+1, Clean Architecture, flutter_bloc, Dio, Sanctum) : modules tasks (tâches, routines, calendrier, historique, propositions et améliorations de routines), chat (orchestrateur en SSE, délégation à des sous-agents du catalogue `agent_start → agent_done`, événement `confirmation_required` avec `McpConfirmationToolEntity`), mcp, api-connection, catalog (skills/plugins), notification (FCM), dashboard (KPI, activité hebdo).
3. **Site Plan'It** (`plani-t.fr`, projet Lovable f0a60f70) : « Vos tâches avancent, même quand vous êtes occupé », « Coût affiché avant chaque action », « Rien ne part sans votre accord », 7 agents du catalogue (Orchestrateur, Léo/FoodEatUp, Nina/RapidoCRM, Théo/RapidoCMS, Sam/RapidoRH, Iris/Studio, Marc/Directeur). Les scènes du site (« neuf relances envoyées », « 18 devis dormants »…) sont des **illustrations du site** : elles ne sont pas reprises comme résultats.
4. **Académie Plan'It** (MCP Tutoriels Plani't) : 43 tutoriels, 28 vidéos en ligne. Les écrans de l'app montrés dans la vidéo viennent de ses tutoriels (compte de démonstration) : tâches (tuto 11), MCP (13), tableau de bord (04).

## Les cinq rôles du scénario

| Rôle | Agent du catalogue Plan'It | Dans ton compte |
|---|---|---|
| Stratégie | Marc, le Directeur | non configuré |
| Communication | Théo, RapidoCMS | non configuré |
| Commercial | Nina, RapidoCRM | non configuré |
| Organisation | Sam, RapidoRH | non configuré |
| Contrôle | L'Orchestrateur | `route_orchestrator` répond, mais ne délègue à aucun agent |

À l'écran : « Rôles du scénario · agents du catalogue Plan'It, pas encore en service dans mon compte ».

## Ce qui n'est pas démontré

- Aucune exécution réelle de routine ni de tâche (0 dans le compte).
- La délégation multi-agents existe dans le code (SSE), mais n'a pas été vue tourner ; les tutoriels « Faire travailler plusieurs agents ensemble » et « Confirmer une action sensible » sont encore **à produire** dans l'Académie.
- Notifications FCM : présentes dans le code, non testées ici.
