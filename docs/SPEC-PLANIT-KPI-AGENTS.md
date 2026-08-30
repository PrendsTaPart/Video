# Spécification Plan'It — exposer l'activité des agents

> **Plan'It n'est pas un projet Lovable, son backend non plus.** Ce document est
> une spécification écrite, pas un patch. Aucun fichier de `PrendsTaPart/planit`,
> `planit-app` ou `FastAPI-RAG` n'est modifié par la session qui l'a produite.
>
> Elle s'appuie sur un audit du code au commit `7287aed`.

---

## Ce que Plan'It a déjà — et qui change tout

L'instinct serait de construire un module de suivi des agents. **Il ne faut
pas** : le socle de mesure existe et il est bon.

| Ce qui existe | Où |
|---|---|
| `TaskExecution` — chaque exécution de tâche, son statut, son résultat, son erreur | `app/Models/TaskExecution.php` |
| `McpToolRun` — chaque appel d'outil MCP : `mcp_key`, `tool_name`, `status`, `duration_ms`, `agent_run_id` | `app/Models/McpToolRun.php` |
| `AiCreditUsage` — chaque appel payant, **avec `agent_slug`**, déjà agrégé `by_agent` | `BillingUsageController` |
| Le module KPI complet — `KpiDefinition`, `KpiSnapshot`, `KpiWidget`, `KpiTrigger`, `KpiTriggerEvent` | `KpiController`, `InternalKpiCollector` |
| **`RoutineKpi`** — `baseline_value`, `current_delta`, `verdict`, `runs_since_baseline`, `credits_since_baseline` | `app/Models/RoutineKpi.php` |
| `GET /api/kpi/home` sert déjà `loops` : routine, KPI, référence, écart, verdict | `routes/api.php` |

`RoutineKpi`, c'est la doctrine Loop-Engineering **déjà en base**. Personne n'a
à la réinventer.

## Les deux manques, précisément

### 1 · La jointure agent ↔ routine n'existe pas

Trois chaînes vivent côte à côte et ne se rejoignent jamais :

```
RoutineKpi     →  KPI ↔ tâche          (une routine et son objectif)
AiCreditUsage  →  agent_slug ↔ coût    (ce qu'un agent dépense)
McpToolRun     →  agent_run_id ↔ outil (ce qu'un run a appelé)
```

`McpToolRun` porte `agent_run_id` — une référence **opaque** vers les
`orch_agent_runs` de FastAPI — mais **ni `task_id`, ni `agent_slug`**. On sait
donc ce que coûte un agent, et ce que produit une routine. Jamais quel agent a
servi quelle routine.

### 2 · Aucune sortie lisible par un tiers

Tout le module KPI est sous `auth:sanctum`, scopé à l'utilisateur courant. Les
cinq endpoints signés `verify.fastapi.signature` existants vont tous dans
l'autre sens (FastAPI → Laravel). Rien ne sort.

### 3 · L'admin ne voit rien de l'exploitation

`routes/admin-api.php` couvre utilisateurs, prompts, serveurs et outils MCP,
catalogue plugins/skills/agents **en lecture seule**, facturation complète,
dashboard, workflows.

**Aucune route `tasks`, `executions`, `kpi` ni `routines`.** L'agent y est une
fiche de catalogue (`CatalogController::agents` : index + upload de logo) : pas
d'activité, pas de taux de succès, pas de routine. `by_agent` donne le **coût**
d'un agent, jamais son **résultat**.

---

## Les trois changements

### A · Deux colonnes sur `mcp_tool_runs`

```php
// database/migrations/xxxx_add_agent_and_task_to_mcp_tool_runs.php
$table->foreignId('task_id')->nullable()->constrained('tasks')->nullOnDelete();
$table->string('agent_slug')->nullable()->index();
```

et les deux ajoutés au `$fillable` de `App\Models\McpToolRun`.

**C'est le changement décisif, et il est presque gratuit** : FastAPI connaît
déjà `task_id` et `agent_slug` au moment où il appelle
`POST /internal/mcp/execute-tool` — il les mesure déjà pour la facturation
(`AiCreditUsage`). Il suffit qu'il les joigne à la charge utile, et que
`McpExecutionController` les persiste.

Nullable des deux côtés : un appel d'outil hors tâche et hors agent reste
légitime (un utilisateur dans le chat), et rien de l'existant ne casse.

### B · Un endpoint signé, en sortie

```php
// routes/api.php — au milieu des autres routes internes signées
Route::middleware('verify.fastapi.signature')
    ->get('/internal/agents/activity',
        [\App\Http\Controllers\API\internal\AgentActivityController::class, 'index']);
```

Paramètres : `depuis`, `jusqu_a` (ISO 8601), `agent_slug` (optionnel),
`user_id` (optionnel).

Réponse, par agent et par période :

```json
{
  "periode": { "depuis": "...", "jusqu_a": "..." },
  "agents": [{
    "agent_slug": "editorial",
    "executions": 42,
    "succes": 39,
    "echecs": 3,
    "taux_succes": 0.929,
    "duree_ms_mediane": 3120,
    "credits": 128.4,
    "routines": [{
      "task_id": 17,
      "nom": "Publication du jour",
      "executions": 21,
      "succes": 20,
      "derniere_execution": "2026-08-30T08:04:12Z",
      "kpi": {
        "cle": "articles_publies",
        "baseline": 2.0,
        "valeur_courante": 3.4,
        "delta_percent": 70.0,
        "verdict": "positif"
      }
    }]
  }]
}
```

Les données viennent de : `McpToolRun` (exécutions, statuts, durées) jointe sur
les deux colonnes nouvelles, `AiCreditUsage` (crédits, déjà par `agent_slug`),
`Task` (le nom de la routine) et `RoutineKpi` + `KpiSnapshot` (référence, écart,
verdict — **déjà calculés**, on les lit).

> **Signé, jamais public.** Le middleware `verify.fastapi.signature` (HMAC-SHA256)
> est déjà la convention du dépôt pour les échanges machine. Aucun jeton
> utilisateur ne transite, aucun jeton OAuth n'est lu — la règle « FastAPI ne
> déchiffre jamais un jeton » reste intacte, on ne fait que la traverser dans
> l'autre sens.

### C · Deux pages d'administration

**Aucune table nouvelle.** Ce sont des lectures admin de ce qui existe.

**`GET /admin/agents`** — `AgentAdminController::index`
Une ligne par `agent_slug` rencontré : exécutions, taux de succès, durée
médiane, crédits, routines servies, dernière activité. Filtres par période.
`GET /admin/agents/{slug}` : le détail, ses routines, ses 50 dernières
exécutions avec erreur.

**`GET /admin/routines`** — `RoutineAdminController::index`
Une ligne par `Task` planifiée : propriétaire, cadence, dernière exécution,
exécutions et échecs sur 30 jours, verdict `RoutineKpi`, écart contre référence.
Deux filtres qui portent tout l'intérêt de la page : **`en_echec`** (au moins un
échec sur les 5 dernières) et **`silencieuse`** (aucune exécution depuis deux
fois la cadence).

Les deux dans le groupe `->middleware(['auth:sanctum', 'admin'])` existant.

---

## Le pont vers BraindCode

Une tâche planifiée Laravel (`app/Console`), quotidienne, qui lit
`/internal/agents/activity` sur les dernières 24 h et appelle
`ingerer_activite_agent` du MCP BraindCode.

**La clé d'idempotence est déjà là** : `McpToolRun.id`, ou
`TaskExecution.id`, font une `cle_execution` stable. Un rejeu n'écrira jamais
deux fois — c'est ce que garantit le contrat côté BraindCode.

Réglage : jeton OAuth BraindCode en variable d'environnement, échec silencieux
avec journalisation (ce pont ne doit jamais faire tomber une exécution de
tâche), et une trace par lot envoyé.

---

## Ce que cette spécification ne demande pas

- **Aucune modification de `FastAPI-RAG`** au-delà de joindre deux champs qu'il
  possède déjà à un appel qu'il fait déjà.
- **Aucune table nouvelle.** Deux colonnes, un endpoint, deux contrôleurs de
  lecture, une tâche planifiée.
- **Aucun changement du module KPI.** `RoutineKpi` fait déjà le travail ; on le
  lit, on ne le refait pas.
- **Aucune écriture depuis l'admin** sur les agents ou les routines. Piloter
  reste un geste de l'utilisateur propriétaire, dans l'application.

## Ordre de mise en œuvre

1. Les deux colonnes (migration + `$fillable` + `McpExecutionController`), et
   côté FastAPI joindre `task_id` et `agent_slug` à l'appel signé.
2. **Attendre.** Sans données, les pages sont vides et invérifiables. Quelques
   jours d'exécutions réelles suffisent.
3. L'endpoint signé et les deux pages admin, qui se vérifient alors sur du vrai.
4. Le pont vers BraindCode en dernier — c'est celui qui a le moins d'effet si on
   se trompe, et le plus de valeur une fois les trois premiers en place.
