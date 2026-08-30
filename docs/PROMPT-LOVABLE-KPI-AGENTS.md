# Prompt Lovable — Suivi et KPI des agents IA (plugin BraindCode)

> À coller dans le projet Lovable **plugin-braindcode** (`rapido-plugins-mcp`).
> Il ajoute l'écran de pilotage des agents et les trois outils MCP qui
> l'alimentent. Il ne réécrit rien de la famille KPI existante : il la branche.

---

## Le contexte à connaître avant d'écrire une ligne

Le serveur MCP de ce projet expose **53 outils** répartis en quatre familles :
prompts & KB, routines & boucles, registre MCP, et **KPI & pilotage**
(`definir_kpi`, `enregistrer_kpi`, `enregistrer_kpi_lot`, `serie_kpi`,
`tableau_de_bord`, `alertes_kpi`, `rattacher_kpi_routine`,
`promouvoir_routine`, `rendre_verdict_routine`,
`enregistrer_execution_routine`, `journal_routine`, `auditer_routines`).

Ce vocabulaire est **juste et complet**. Le problème n'est pas ce qu'il dit,
c'est **qui le remplit** : aujourd'hui, uniquement un humain ou un agent qui
raconte ce qu'il a fait. Rien ne lit un orchestrateur. Conséquences, toutes
observables :

1. Une routine qui tourne réellement ailleurs (Plan'It, Claude Code) n'apparaît
   nulle part ici. Le tableau de bord ne montre que le déclaré.
2. **L'agent n'existe pas comme entité.** `prompts_pour_agent` prend un nom
   d'agent en texte libre. On ne peut donc pas répondre à « qu'a fait l'agent
   Éditorial cette semaine ».
3. **Une routine qui s'est tue reste « conforme ».** `auditer_routines` juge la
   complétude d'une fiche (objectif chiffré, garde-fou), jamais sa dernière
   exécution. C'est pourtant la panne la plus fréquente et la seule invisible.
4. **Aucun coût par routine ni par agent.** `promouvoir_routine` est donc une
   décision prise à l'aveugle, alors que c'est exactement la décision qu'il sert.

**Ne recrée pas** `definir_kpi`, `enregistrer_kpi_lot`, `serie_kpi`,
`tableau_de_bord` ni `alertes_kpi`. Ils existent, ils sont bons, on s'appuie
dessus.

---

## Ce qu'il faut construire

### 1 · Le modèle de données

Trois tables nouvelles, et **une seule** idée : un agent est une entité, et son
activité s'écrit toute seule.

**`agents`** — le registre.

| Colonne | Type | Rôle |
|---|---|---|
| `id` | uuid | |
| `slug` | text, unique | l'identifiant employé partout ailleurs (`editorial`, `production-video`, `commercial`) |
| `nom` | text | libellé humain |
| `role` | text | ce dont il répond, en une phrase |
| `proprietaire` | uuid → utilisateur | qui en répond côté humain |
| `mcp_utilises` | text[] | clés des serveurs MCP qu'il a le droit d'appeler |
| `statut` | enum `actif` / `suspendu` / `archive` | |
| `cree_le`, `modifie_le` | timestamptz | |

**`agent_executions`** — le journal machine, une ligne par exécution.

| Colonne | Type | Rôle |
|---|---|---|
| `id` | uuid | |
| `agent_id` | uuid → `agents` | |
| `routine_id` | uuid → routines, **nullable** | une exécution hors routine reste légitime |
| `cle_execution` | text, **unique** | l'idempotence : un rejeu n'écrit pas deux fois |
| `source` | enum `planit` / `claude_code` / `manuel` | d'où vient la mesure |
| `statut` | enum `succes` / `echec` / `partiel` | |
| `demarre_le`, `termine_le` | timestamptz | |
| `duree_ms` | int | |
| `credits` | numeric, nullable | coût, quand la source le connaît |
| `outils_appeles` | jsonb | `[{mcp, outil, statut}]` — ce qu'il a réellement fait |
| `objectif_atteint` | boolean, nullable | `null` = pas mesurable sur cette exécution |
| `resume` | text | une phrase, pas un journal complet |
| `erreur` | text, nullable | |

**`agent_routines`** — le rattachement agent ↔ routine (n-n), avec la cadence
attendue :

| Colonne | Type |
|---|---|
| `agent_id`, `routine_id` | uuid, clé primaire composite |
| `cadence_attendue_heures` | int — **c'est ce qui rend le silence détectable** |
| `actif` | boolean |

> **Le silence se détecte parce que la cadence est déclarée.** Sans
> `cadence_attendue_heures`, « cette routine ne tourne plus » n'est pas une
> question à laquelle on peut répondre : on ne sait pas à quoi comparer.

RLS : chaque table est isolée par compte, comme les tables KB existantes.

### 2 · Les trois outils MCP nouveaux

**`lister_agents`** *(lecture, OAuth)* — les agents du compte : slug, nom, rôle,
statut, nombre de routines rattachées, **dernière activité**, exécutions et taux
de succès sur 7 et 30 jours, crédits sur 30 jours. Filtres : `statut`,
`silencieux_seulement`.

**`obtenir_agent`** *(lecture, OAuth)* — un agent en détail : sa fiche, ses
routines avec cadence attendue et dernière exécution de chacune, ses 20
dernières exécutions, ses KPI rattachés via `rattacher_kpi_routine` avec leur
verdict courant, et sa dépense par semaine sur 8 semaines.

**`ingerer_activite_agent`** *(écriture, OAuth)* — **le point d'entrée machine**,
et la seule vraie nouveauté d'architecture.

```
{
  agent: "editorial",              // slug ; créé au vol s'il n'existe pas encore
  source: "planit" | "claude_code",
  executions: [{
    cle_execution: "...",          // idempotent : rejouer n'écrit pas deux fois
    routine: "d5-publication-du-jour",   // slug de routine, optionnel
    statut: "succes" | "echec" | "partiel",
    demarre_le: "2026-08-30T08:00:00Z",
    termine_le: "2026-08-30T08:04:12Z",
    credits: 12.4,                 // optionnel
    outils_appeles: [{ mcp: "foodeatup_site", outil: "publier_les_articles_du_jour", statut: "succes" }],
    objectif_atteint: true,        // optionnel
    resume: "3 articles publiés, 1 reporté faute de visuel.",
    erreur: null
  }]
}
```

Contraintes, à tenir dans le code et pas seulement dans la description :

- **Idempotent par `cle_execution`.** Un rejeu met à jour, ne duplique pas.
- **Lot borné** à 200 exécutions par appel ; au-delà, refuser avec un message
  qui dit de découper.
- **Aucune modération.** C'est une mesure, pas une proposition : contrairement
  à `proposer_routine`, ça s'écrit directement. Une mesure qui attend une
  validation humaine n'est plus une mesure.
- **Rendre le détail par ligne** : acceptées, mises à jour, refusées avec le
  motif. Un lot à moitié écrit doit se lire dans la réponse.

### 3 · Les deux extensions d'outils existants

**`routines_silencieuses`** — nouvel outil, ou paramètre de `auditer_routines`
si ça te paraît plus juste au vu du code existant. Rend les routines actives
dont la dernière exécution dépasse `cadence_attendue_heures × 2`, triées par
retard décroissant, avec : routine, agent, cadence attendue, dernière
exécution, retard en heures.

**`tableau_de_bord`** gagne trois blocs : coût par agent, coût par routine, et
les routines silencieuses. Sans casser sa sortie actuelle — on ajoute, on ne
remplace pas.

**`auditer_routines`** gagne un critère : une routine complète mais silencieuse
n'est plus « conforme », elle est « conforme mais à l'arrêt ». Ce n'est pas la
même décision.

---

## L'écran — `/pilotage`

Deux onglets, parce qu'il y a deux questions différentes et qu'elles ne se
répondent pas avec la même vue.

### Onglet « Mes agents »

**En tête, quatre chiffres** : agents actifs · exécutions sur 7 jours · taux de
succès sur 7 jours · crédits sur 30 jours. Chacun avec son écart contre la
période précédente.

**Bandeau d'alerte, uniquement s'il y a lieu** — jamais un bandeau vide :
« 2 routines ne tournent plus » et « 1 agent en échec répété », en rouge, qui
mènent au détail filtré.

**La table des agents** : agent · routines · dernière activité · exécutions 7 j ·
taux de succès (barre, pas un pourcentage nu) · crédits 30 j · statut.
Une ligne dont la dernière activité dépasse la cadence attendue porte une
pastille orange. Clic → la fiche de l'agent.

**La fiche d'un agent** : sa raison d'être en une phrase, ses routines avec pour
chacune la cadence attendue et le temps depuis la dernière exécution, ses KPI
rattachés avec référence / valeur courante / écart / verdict, sa dépense
hebdomadaire, et le journal de ses 20 dernières exécutions — statut, durée,
résumé, et l'erreur quand il y en a une.

### Onglet « Moi »

**Ce n'est pas le même écran vu autrement, c'est une autre question.** Le
premier onglet répond à « mes agents travaillent-ils » ; celui-ci répond à
« qu'est-ce qui m'attend, moi ».

- **Ce qui attend un geste humain** : les propositions de routine en modération,
  les alertes KPI non décidées (`alertes_kpi`), les verdicts de boucle à rendre
  (`rendre_verdict_routine`), les routines mûres pour promotion (3 exécutions et
  14 jours — `promouvoir_routine`). Chaque ligne porte le geste, pas seulement
  l'information.
- **Mes KPI à moi** : les KPI dont je suis propriétaire, avec leur série.
- **Ma semaine** : réutilise `ma_semaine` et `mes_rappels`, déjà là.

Une ligne d'attente doit dire **depuis quand** elle attend. Une file sans âge
ne se priorise pas.

---

## Ce qui alimentera cet écran

Deux sources, et il faut que l'écran le dise :

1. **Plan'It** appellera `ingerer_activite_agent` après chaque exécution de
   tâche. Une spécification Laravel séparée décrit ce côté-là ; Plan'It n'est
   pas un projet Lovable et son code ne se modifie pas d'ici.
2. **Les routines Claude Code** appelleront le même outil en fin de course.

D'ici là, l'écran doit être **honnête sur le vide** : « aucune activité
enregistrée — connectez une source » plutôt qu'un tableau de zéros qui laisse
croire que les agents ne font rien.

---

## Deux règles à ne pas contourner

**La mesure n'est pas une proposition.** Toute la famille écriture de ce serveur
passe par modération humaine, et c'est bien : une routine proposée par une
machine doit être relue. `ingerer_activite_agent` est l'exception, et elle est
fondée — ce n'est pas un avis, c'est un fait constaté. Ne le fais pas passer par
la file de modération : il s'y noierait et le tableau de bord resterait vide.

**Un compteur ne s'invente jamais.** La règle du serveur (« si la donnée manque,
écrire "à vérifier" ») vaut ici aussi : `objectif_atteint` à `null` s'affiche
« non mesuré », pas « échec ». Un coût inconnu s'affiche « — », pas « 0 ».

---

## Vérification

1. `lister_agents` sur un compte vide rend une liste vide et un message clair,
   pas une erreur.
2. Deux appels de `ingerer_activite_agent` avec la même `cle_execution`
   produisent **une** ligne, la seconde marquée mise à jour.
3. Une routine avec `cadence_attendue_heures = 24` et une dernière exécution
   il y a 50 h apparaît dans `routines_silencieuses`, et disparaît dès qu'une
   exécution est ingérée.
4. `tableau_de_bord` montre le coût par agent après ingestion, et ses blocs
   existants sont inchangés.
5. L'onglet « Moi » ne montre que des lignes qui appellent un geste — si tout
   est traité, il le dit et ne montre rien.
