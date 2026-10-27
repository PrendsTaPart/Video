# Vidéo 27 — Audit n8n (vérifié le 27/10/2026)

Lecture seule via le connecteur N8n. Aucun workflow exécuté ni modifié.

## Instance

**789 workflows** au total, dont environ 200 brouillons techniques nommés `_tmp_extract` créés le 25/10 et inactifs. Ils sont à archiver pour assainir l'instance.

## Workflows de la vidéo

| Workflow | ID | Statut | Constat |
|---|---|---|---|
| 🤖 RapidoRH — WF1 Dispatcher Agents IA (OpenAI) | OSaoko9YezKMCEUy | actif · 22 nœuds · CRON 9 h + webhook | Conforme au schéma de la vidéo : lecture des tâches Todo par MCP RapidoRH (`get-project-tasks-tool`), agent GPT-4o avec outils MCP, passage en Done. **Mais les 8 dernières exécutions sont en erreur** (22/10 → 26/10, chaque jour à 9 h New York) : « Could not connect to your MCP server. Authentication failed » sur `rh.rapidosoftware.com/mcp/rapidorh`. **Le jeton Bearer RapidoRH a expiré** ; aucune exécution réussie conservée. |
| MCP FoodEatUp V2 | w6dURv9azjK5rC0b | actif · 6 déclencheurs | n8n exposé comme serveur MCP (groupes d'outils) ; aucune exécution conservée |
| RapidoATS- CV Process (parse + scoring) | 1FyhxtH8DibCi058 | actif | description : « clés en dur ($env bloqué sur cette instance) » |
| Méga Employé IA — Tâches quotidiennes | 8rjqaG2aNFugM5Ly | non retrouvé par recherche de nom | non vérifié |
| BraindCode Super Agent — OpenClaw MCP | C59E3fwcRDxFzOqE | actif · déclencheur MCP | 8 outils annoncés ; comportement autonome non vérifié |

## Mise à jour de la vidéo

La mention « non revérifié » est remplacée par « Vérifié dans n8n · 22 nœuds · en erreur depuis le 22/10 : jeton RapidoRH expiré ». La voix dit « j'ai un workflow qui récupère les tâches… » : c'est vrai sur le plan de la conception, mais il ne tourne pas en ce moment.

## À corriger

1. Renouveler le jeton Bearer RapidoRH (credential « Bearer Auth account ») du dispatcher.
2. Webhook `rh-dispatcher` sans authentification : en ajouter une.
3. **`$env` est bloqué sur l'instance**. Plusieurs workflows contournent ce blocage avec des **clés en dur** (RapidoATS, WC2026_1), à migrer vers des credentials.
4. Archiver les ~200 `_tmp_extract`.
