# Vidéo 27 — Architecture MCP

## Trois niveaux

1. **Logiciels** : FoodEatUp, RapidoCRM, RapidoCMS, RapidoRH, RapidoATS, StartupForge. Chacun garde sa base, ses API, ses règles métier et son interface.
2. **Serveurs MCP** : une interface standardisée qui expose des capacités autorisées. Le MCP ne remplace ni l'API métier ni le contrôle d'accès.
3. **Agents et orchestrateurs** : Claude, ChatGPT, OpenClaw et n8n. n8n planifie, déclenche et coordonne ; un workflow n8n peut lui-même servir de serveur MCP.

## Serveurs MCP réellement connectés à cette session (27/10/2026)

Outils montrés dans la vidéo, présents dans les catalogues :

| Serveur | Exemples d'outils |
|---|---|
| RapidoCRM | `search_entreprises`, `create_devis`, `get_contact`, `list_segments` |
| RapidoCMS | `create_draft_tool`, `schedule_draft_tool`, `list_all_files`, `list_connected_accounts` |
| FoodEatUp (produit) | `list_stocks`, `list_haccp_temperatures`, `list_recipes`, `create_supplier_order` |
| RapidoRH | `get-project-tasks-tool`, `move-task-tool`, `create-task-tool` |

Garde-fous constatés sur ces serveurs : écritures en deux temps avec `confirm: true` sur plusieurs d'entre eux, brouillons par défaut, aucune dépense ni commande sans validation. Le détail est dans les vidéos 15, 17, 20 et 24.

## À ne pas confondre

- Un **déclencheur MCP dans n8n** (workflow exposé comme serveur MCP) n'est pas un **serveur MCP développé dans le logiciel** (Laravel, FastMCP…).
- L'autoroute est une métaphore de **réutilisation et de standardisation**, pas de vitesse de transport des données.
