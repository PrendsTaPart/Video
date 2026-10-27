# Vidéo 20 · Audit des MCP et des capacités (26–27/10/2026)

## Capacités confirmées (appels réels, lecture seule)

| Source | Appel | Résultat |
|---|---|---|
| FoodEatUp Formation | `describe_server` | niveaux d'autonomie Aperçu / Brouillon / Confirmé ; étapes V0 → V1 (3 exécutions) → V2 (KPI + 14 jours) ; verdicts gardée / ajustée / arrêtée ; toute écriture demande `confirm=true` |
| | `get_claude_brief` | compte connecté : apprenant « Growth Hacker & Commercial », 0 mission validée |
| | `get_brand_guidelines` | palette, typographies, 13 logos de logiciels et 8 logos de chartes (voir `video-20-brand-guidelines.json`) |
| | `list_agents` | **6 agents** : Accueil des demandes, Relance et devis, Prescripteurs, Contenus, Veille, Pilotage. **Tous « à configurer »**, autonomie Aperçu, gouvernance « validation humaine », sans KPI ni cible ni point d'arrêt renseignés |
| | `list_routines` | **20 routines**, toutes en **V0**, aucun verdict ; 6 ont un prompt complet (dont « Traitement des demandes entrantes » et les routines LinkedIn / appels / groupes) |
| | `list_routine_templates` | guide du loop-engineering : observer, planifier, agir dans la limite d'autonomie, enregistrer la mesure, rendre compte ; six blocs de prompt (objectif, sources, limite, rendu, critère d'arrêt, accord humain) |
| | `get_agent_brief` (Pilotage) | adresses MCP : foodeatup.com/api/mcp, crm.rapidosoftware.com/mcp, cms.rapidosoftware.com/mcp, rh.rapidosoftware.com/mcp, planit.braindcode.com/mcp |
| | `list_connectors` | 11 connecteurs attendus, **aucun coché** dans ce compte |
| | `list_tunnels` | blocs du tunnel avec agent responsable ; `etat_workflow` vide partout |
| | `list_kpi_catalog(agents)` | 5 indicateurs (routines en service, verdicts rendus, taux d'exécution, écarts MCP, alertes traitées) |
| | `get_kpi_dashboard(mois)` | **0 indicateur suivi, 0 mesure** |
| | `get_report_brief(vendredi)` | structure en 6 diapositives ; tous les indicateurs « non suivi » |
| Plan'It (vidéo 18) | `list_tasks`, `list_routines`, `get_calendar`, `list_pending_routine_actions` | 0 tâche, 0 routine, calendrier vide, 0 action en attente |
| | `list_mcp_servers` | 8 connecteurs branchés (FoodEatUp 193 outils, RapidoCRM 131, RapidoCMS 45, RapidoRH 22, Plan'It 63…) |

## Intégrations non vérifiées

- Aucune exécution de routine ni délégation d'agent n'a été observée.
- Agent « Formation » : n'existe pas ; seul le connecteur pédagogique Tutoriel FoodEatUp existe.
- Les MCP RapidoCRM / RapidoCMS / RapidoRH n'ont pas été rappelés pour cette vidéo (vus dans les vidéos 8, 15 et 17).

## Éléments illustratifs (signalés à l'écran)

- L'animation « Plan'It distribue le travail » : les agents sont réels, les tâches qui circulent sont une illustration (« aucune exécution montrée »).
- L'objectif « 20 nouveaux clients » : fictif.
- La grille de 100 agents : illustration (« aujourd'hui, 6 agents en préparation »).

## Tableau de pilotage montré (données réelles)

Tâches planifiées 0 · exécutées 0 · en échec 0 · livrables 0 · en attente de validation 0 · KPI mesurés 0.
