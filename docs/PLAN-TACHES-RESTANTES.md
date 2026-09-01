# Ce qui reste à faire — hors production vidéo

*État au 30 août 2026, après la mise en production des cinq dépôts.*

Ce plan ne couvre pas le montage des épisodes ni les visuels manquants : c'est
de la production vidéo, elle a sa propre file. Il couvre tout le reste.

---

## Où on en est

**Livré et fusionné sur la branche par défaut des cinq dépôts :**

| Dépôt | Ce qui y est |
|---|---|
| `hubspot-hub-nav` | le hub expose sa carte — 6 outils MCP en lecture seule |
| `food-series-hub` | CI débloquée, WhatsApp, `deposer_episode`, `episodes_du_module` |
| `foodeatup-guide-star` | `tutoriels_du_module` — l'index du hub retourné, 170 tutoriels |
| `foodeatup-site` | `contenus_du_module` + `module`/`ecran` sur articles et posts |
| `Video` | les 30 épisodes rattachés, 3 routines, les garde-fous, 3 documents |

**Ce qui n'est pas encore vrai en production :** les serveurs MCP déployés
servent toujours le build d'avant la fusion. Vérifié à l'instant —
`lister_episodes` et `list_articles` répondent, mais sans `module_logiciel`.
Rien n'est testable tant que Lovable n'a pas resynchronisé.

---

## Le chemin critique

Trois dépendances commandent tout l'ordre. Les ignorer, c'est construire des
écrans qui affichent du vide.

```
Resynchronisation Lovable  ──▶  tester les 4 MCP  ──▶  faire tourner les routines
                                                              │
Plan'It mesure (2 colonnes) ──▶ BraindCode affiche  ◀─────────┘
                                                              
Rattacher les articles      ──▶  contenus_du_module sert à quelque chose
```

---

## 1 · Mise en service — à faire en premier, tout en dépend

### 1.1 · Resynchroniser Lovable sur les quatre projets
Ouvrir chaque projet dans Lovable et vérifier qu'il a pris le dernier commit de
`main`. **Contrôle qui tranche** : appeler `lister_episodes` sur le catalogue
social — si la réponse porte `module_logiciel`, la synchronisation est faite.

### 1.2 · Vérifier que la migration du site est passée
`foodeatup-site` porte `20260830150000_module_ecran_logiciel.sql`, que je n'ai
pas pu appliquer (pas les droits sur le projet Supabase `qhymwtbficupnidrupno`).
Lovable l'applique à la synchronisation. **Contrôle** : `contenus_du_module`
répond au lieu d'échouer sur une colonne inconnue.

### 1.3 · Brancher le connecteur MCP du hub
`hubspot-hub-nav` expose `/mcp` pour la première fois. Personne ne l'a encore
ajouté comme connecteur — il faut le faire là où les agents doivent l'appeler
(Claude, Plan'It, les autres projets). Sans lui, `ou_faire_ca` n'est appelable
par personne et le fil conducteur reste théorique.

### 1.4 · Essai de bout en bout
Partir de `ou_faire_ca("relevé de températures")` et vérifier qu'on obtient
l'écran, son lien profond, ses outils, puis ses tutoriels
(`tutoriels_du_module`), ses épisodes (`episodes_du_module`) et ses articles
(`contenus_du_module`). **C'est le seul essai qui prouve que le fil conducteur
existe.** Tant qu'il n'a pas été fait, on a du code, pas un système.

---

## 2 · Le fil conducteur : la plomberie est posée, les données non

### 2.1 · Rattacher les articles du site à leur écran ⚠️ le trou le plus visible
Les colonnes `module_logiciel` et `ecran_logiciel` existent sur `articles` et
`posts_sociaux`. **Elles sont vides.** `contenus_du_module` répondra donc
« aucun contenu » sur tous les écrans, ce qui est exact et inutile.

Une quarantaine d'articles à rattacher. Deux façons, et la seconde est
meilleure : à la main via `update_article`, ou en écrivant une routine qui
propose un rattachement par article (les mots-clés et le pilier suffisent
souvent) et le fait valider. Le rattachement des épisodes vidéo a suivi
exactement cette méthode — la recherche du hub propose, un humain tranche les
cas où le mot ne dit pas l'écran.

**Sans cette étape, la vague 1 ne sert à rien côté site.**

### 2.2 · `journaliser_formation` sur le hub
Le seul pont du plan initial qui n'est pas livré. La trace « cette leçon a été
vue » ne peut pas s'écrire dans l'Académie : ce serveur est public et sans
authentification, y écrire ouvrirait une base publique en écriture. Elle va
donc côté hub, qui a déjà `/journal`, l'authentification et l'établissement.

Ce n'est pas un petit travail : le MCP du hub est aujourd'hui **entièrement en
lecture seule**, six outils, aucune écriture. Il faut une table Supabase, le
premier outil d'écriture, et la règle de consentement qui va avec.

### 2.3 · Les tutoriels sans écran
170 tutoriels sur ~173 sont rattachés. Vérifier les restants — soit ils
appartiennent à un écran que `hubs.ts` ne référence pas encore, soit ils
n'enseignent pas d'écran, et c'est légitime.

---

## 3 · Le pont KPI — le plus gros chantier restant

L'ordre compte : **Plan'It mesure d'abord, BraindCode affiche ensuite.**
Construire l'écran avant la mesure donne un tableau de zéros.

### 3.1 · Plan'It + FastAPI : la jointure manquante — *à faire en premier*
Deux colonnes sur `mcp_tool_runs` (`task_id`, `agent_slug`), et FastAPI qui les
joint à l'appel signé `/internal/mcp/execute-tool` — **il les connaît déjà**, il
les mesure pour la facturation. C'est le changement le moins coûteux du lot et
celui dont tout le reste dépend.

Puis **attendre**. Quelques jours d'exécutions réelles, sans quoi les pages
suivantes sont vides et invérifiables.

📄 `docs/SPEC-PLANIT-KPI-AGENTS.md` — spécification complète, avec les fichiers
exacts à toucher. ⚠️ Plan'It n'est pas un projet Lovable : c'est du Laravel et
du Python à écrire à la main.

### 3.2 · Plan'It : l'endpoint signé et les deux pages admin
`GET /internal/agents/activity`, puis les pages **Agents** et **Routines**.
Aucune table nouvelle — ce sont des lectures de `TaskExecution`, `McpToolRun`,
`AiCreditUsage` et `RoutineKpi`, qui existent déjà.

### 3.3 · BraindCode : les trois outils et l'écran de pilotage
`lister_agents`, `obtenir_agent`, `ingerer_activite_agent`, plus
`routines_silencieuses` et les extensions de `tableau_de_bord`. Le prompt est
écrit et prêt à coller dans Lovable.

📄 `docs/PROMPT-LOVABLE-KPI-AGENTS.md`

### 3.4 · Le pont quotidien
Une tâche planifiée Laravel qui lit `/internal/agents/activity` sur 24 h et
appelle `ingerer_activite_agent`. À faire **en dernier** : c'est celui qui a le
moins d'effet si on se trompe, et le plus de valeur une fois les trois autres
en place.

---

## 4 · Les routines : les faire vivre

### 4.1 · Trois exécutions, quatorze jours
Les trois routines en essai (`publication-du-jour`, `trous-de-publication`,
`episode-multicanal`) ne se promeuvent pas avant. **Une routine qui a marché
une fois a eu de la chance.**

### 4.2 · Les trois suivantes, pas avant la semaine prochaine
La limite de trois nouvelles par semaine n'est pas décorative : au-delà, on
n'observe plus, on empile. Candidates, toutes appuyées sur les ponts livrés :

- **I4 · plat du jour multicanal** *(vendable)* — `get_daily_brief` →
  `ou_faire_ca` → `create_social_post`
- **D6 · relais manuels du jour** — la file WhatsApp, profil LinkedIn et TikTok
  à coller, en une liste par jour
- **A1 · écrans nus** — les écrans sans vidéo ni tutoriel ni article, vers la
  file de production

### 4.3 · Mesurer, enfin
Aujourd'hui les routines appellent `enregistrer_execution_routine`, qui est
déclaratif. Elles ne deviennent pilotables qu'une fois 3.3 livré.

---

## 5 · Le projet commercialisation

### 5.1 · Lancer la recherche
📄 `docs/PROMPT-CLAUDE-CHAT-COMMERCIALISATION.md`, à coller dans une
conversation Claude. Prévoir deux ou trois échanges — il demande ses questions
avant de rédiger.

### 5.2 · Transformer le résultat
Les prompts système deviennent des skills, les objectifs chiffrés deviennent
des KPI (`definir_kpi` puis `rattacher_kpi_routine`), le tableau de bord
personnel devient l'onglet « Moi » de `/pilotage`.

**Rien de tout cela ne se lance avant que le pont KPI existe** : des agents
commerciaux non mesurés, c'est exactement ce qu'on cherche à ne plus faire.

---

## 6 · Dette technique — quand il y aura du temps

### 6.1 · Le lint de `foodeatup-site`
**4 827 problèmes**, dont l'essentiel de mise en forme. Même situation que
`food-series-hub` avant sa remise au format : la CI ne dit plus rien. Le remède
est connu et a marché — étendre `.prettierignore` aux générés, `npm run format`
sur le reste, puis fermer les vraies erreurs à la main. Compter une PR séparée,
jamais mêlée à du code.

### 6.2 · Les deux `any` du site
`outputs.ts:198` (`avecSorties`) et les deux `.update(patch as any)` de
`articles.ts`. Pré-existants, sans effet tant que 6.1 n'est pas fait.

---

## L'ordre que je recommande

| Ordre | Tâche | Pourquoi maintenant |
|---|---|---|
| 1 | **1.1 → 1.4** mise en service et essai de bout en bout | rien n'est vrai avant |
| 2 | **3.1** les deux colonnes Plan'It + FastAPI | la mesure met des jours à s'accumuler, elle doit démarrer tôt |
| 3 | **2.1** rattacher les articles | sans quoi un tiers du fil conducteur reste vide |
| 4 | **3.2 → 3.3** l'endpoint, les pages, l'écran BraindCode | sur des données réelles, pas sur du vide |
| 5 | **4.1** faire tourner les routines | en parallèle, l'horloge des 14 jours tourne |
| 6 | **5.1** la recherche commercialisation | elle ne bloque personne, elle peut démarrer quand vous voulez |
| 7 | **2.2** `journaliser_formation` | le plus gros travail pour le moins d'effet immédiat |
| 8 | **6.1** le lint du site | à faire avant que la CI ne serve vraiment |
