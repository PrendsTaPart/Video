# Épisode 8 · Je pilote mes projets, mes équipes et mes agents IA avec RapidoRH

Vertical 1080 × 1920, 120 s (+ version de 43,3 s). Voix Noé (ElevenLabs, `eleven_v4`). **Rien n'a été publié. Aucune donnée réelle n'a été lue ni modifiée.**

## Livrables

| Livrable | Fichier |
|---|---|
| Vidéo principale (120 s) | `renders/episode8-rapidorh_1080x1920.mp4` |
| Version courte (43,3 s) | `renders/episode8-rapidorh_45s_1080x1920.mp4` |
| Miniature « Je pilote mes équipes et mes agents IA » | `renders/miniature-episode8-1080x1920.jpg` |
| Schéma d'architecture des routines | `renders/schema-architecture-routines.jpg` |
| Voix off et mixage | `audio/` |
| Sous-titres SRT et ASS | `sous-titres/` |
| Captures de la démo locale | `captures/` |
| Jeu de démo, réponses MCP, composition | `composition/` |

## La démonstration : RapidoRH lancé en local, projet de démo

Ton espace RapidoRH en ligne est vide (0 projet, 0 utilisateur). Je n'y ai rien créé.

J'ai lancé **le code du dépôt `PrendsTaPart/rapido-RH`** sur ma machine de travail :
- Laravel, base SQLite jetable, clés Passport locales ;
- le jeu de démonstration vient de `composition/seed_demo.php`.

Contenu du jeu de démonstration :
- **une entreprise** « BraindCode · DÉMO » ;
- **6 personnes fictives**, toutes marquées « (démo »), adresses `@demo.local` ;
- **3 projets :** FoodEatUp · Daily Brief, RapidoCMS · Bibliothèque v2, Série vidéo IA ;
- **14 tâches**, avec statuts, priorités et échéances ;
- **les rôles et les départements** de l'entreprise de démo.

Tout ce qui est filmé est l'**interface réelle** de RapidoRH :
- le tableau de bord, la liste des projets et le Kanban ;
- les utilisateurs (colonne salaire et adresses floutées), les rôles et les départements ;
- l'agenda.

Les appels MCP sont **réels**, faits sur le serveur local `/mcp/rapidorh` (JSON-RPC, jeton Passport local), en lecture seule :

| Appel | Réponse |
|---|---|
| `initialize` | « Rapido RH Server » 0.0.1, protocole 2025-06-18 |
| `tools/list` | 24 outils exposés |
| `get-projects-list-tool` | 3 projets en cours, chef de projet, équipe, avancement |
| `get-project-tasks-tool` (projets 1, 2, 3) | 14 tâches, dont 7 urgentes ; une en retard (échéance 25/10, en cours) |
| `create-task-tool` | **Aperçu seulement, non exécuté** : « En attente de ma validation » |

Le « plan du jour » montré à l'écran est déduit de ces réponses.

## Rapport d'audit : ce qui existe vraiment

| Fonction | Dans le code | Remarque |
|---|---|---|
| Projets (responsable, équipe, dates, statut, taille) | ✅ | `app/Models/Project.php` |
| Tâches (À faire, En cours, Terminée ; Urgent, Moyenne, Faible) et Kanban par listes | ✅ | `Task`, `TaskList` |
| Historique des tâches | ✅ | `TaskHistory`, écrit par `CreateTask` et `MoveTask` |
| Dailies (temps passé par tâche) | ✅ | `Daily`, `DailyTask` |
| Rôles, permissions (36), départements | ✅ | Gates définies depuis la table `permissions` |
| Serveur MCP `/mcp/rapidorh` (`auth:api`) | ✅ | 24 outils exposés. Les fichiers `GetPayrollsTool`, `GetLeaveRequestsTool`, `GetProjectsTool` et `GetUserTasksTool` existent mais ne sont pas exposés |
| Champ « agent IA » sur une tâche ou un utilisateur | ❌ | Une tâche est assignée à une personne |
| Tâches planifiées, files d'attente, routines | ❌ | Pas de planificateur dans le code. Une routine a besoin d'un orchestrateur externe (Claude Code, Plan'It, n8n) |
| Envoi d'e-mail ou de WhatsApp par le MCP | ✅ outils | Non appelés |

**RapidoRH n'est donc pas présenté comme un orchestrateur autonome.** Le tableau « humains et agents » de la vidéo est une **illustration** ; un encart le dit à l'écran.

Je n'ai lu aucune information confidentielle de collaborateurs : pas de salaires, pas de paie, pas de contacts privés.

## Routine proposée (non activée)

**Brief quotidien des projets BraindCode**
- **Déclenchement :** chaque matin à 8 h 30, seulement après validation du responsable.
- **Orchestrateur :** Claude Code, Plan'It ou n8n.
- **Entrées :** projets en cours, tâches ouvertes, priorités, échéances, responsables (`get-projects-list-tool`, `get-project-tasks-tool`).
- **Actions :** consulter, repérer les tâches importantes, résumer, proposer les prochaines actions, signaler les blocages (retards, urgences sans avancement).
- **Sortie :** un rapport quotidien, trois priorités par projet, les décisions à prendre, les actions qui demandent une validation.
- **Règles :**
  - pas de suppression ;
  - pas de modification de rôle ;
  - pas de création d'employé ;
  - pas de changement de statut arbitraire ;
  - chaque écriture (`create-task-tool`, `move-task-tool`) passe par une validation humaine ;
  - chaque action exécutée est journalisée.

## Voix off

> Aujourd'hui, je développe plusieurs logiciels, je travaille avec des collaborateurs et je construis des agents IA. Mais comment organiser tout ce monde, pour que chacun sache ce qu'il doit faire ?
>
> Pour ça, j'ai développé RapidoRH. Un outil qui me permet de centraliser mes projets, mes équipes, les responsabilités et le travail à réaliser.
>
> Chaque projet a son responsable, ses collaborateurs, ses dates et ses tâches, avec leur priorité. Je peux savoir où en est le travail, et ce qu'il reste à faire.
>
> J'organise mes collaborateurs par rôles et par départements, et je leur donne accès aux informations dont ils ont besoin.
>
> Mais le plus intéressant, c'est que j'ai connecté RapidoRH à Claude grâce à son MCP. Je peux lui demander d'analyser mes projets, de retrouver les tâches prioritaires et de préparer le travail de la journée.
>
> Et avec mes routines, je peux aller plus loin : préparer les tâches du matin, détecter les blocages, suivre les échéances et proposer les prochaines actions. Une routine, il faut un orchestrateur pour la lancer : Claude Code, Plan'It ou n8n.
>
> Mon objectif, c'est de faire travailler les humains et les agents IA dans une organisation cohérente. Les humains prennent les décisions importantes, les agents exécutent les missions autorisées, et RapidoRH permet de suivre le travail.
>
> Pour moi, le véritable enjeu de l'IA, ce n'est pas seulement d'avoir des agents intelligents. C'est de savoir organiser leur travail, mesurer leurs résultats, et les faire collaborer avec les humains.
>
> Et demain, je vous montrerai une nouvelle étape de mon quotidien d'entrepreneur avec l'IA.

## Storyboard

| Temps | Scène | Images |
|---|---|---|
| 0–11 | Le problème | Projets, collaborateurs, Claude Code, agents IA en vrac, Michael qui réfléchit, « Qui fait quoi ? » |
| 11–21 | Ma solution | Logo RapidoRH, tableau de bord réel, « Démo locale · entreprise et personnes fictives » |
| 21–30 | Mes projets | Liste réelle des projets ; responsable, collaborateurs, dates, tâches, priorités |
| 30–40,8 | Kanban (sans voix) | Zooms sur le Kanban réel (Urgent, échéances) |
| 40,8–45,9 | Mes équipes | Utilisateurs (salaires floutés), rôles, départements |
| 45,9–56 | Claude est connecté | Prompt, appels MCP réels sur la démo |
| 56–71,6 | Le plan du jour (sans voix) | En retard, aujourd'hui, demain ; aperçu de `create-task-tool` non exécuté, « En attente de ma validation » |
| 71,6–83,4 | Routines | Brief quotidien en 6 étapes ; Claude Code, Plan'It, n8n ; « Proposée, pas activée » |
| 83,4–95,6 | Humains et agents | Tableau responsable / tâche / agent ou routine / échéance / statut, encart « illustration » |
| 95,6–105,6 | Conclusion | Organiser, mesurer, collaborer |
| 105,6–120 | Carton | RAPIDORH × CLAUDE × BRAINDCODE · « DES PROJETS. DES ÉQUIPES. DES AGENTS IA. UNE ORGANISATION. » |

## Publications (à valider)

**LinkedIn**

> Avoir des agents IA, c'est bien. Mais si personne ne sait sur quel projet ils travaillent, on crée surtout du désordre.
>
> Pour organiser BraindCode, j'ai développé RapidoRH : projets, responsables, tâches, priorités, rôles, départements. Et je l'ai connecté à Claude par un serveur MCP.
>
> Le matin, je lui demande : « Consulte mes projets, trouve les tâches prioritaires, prépare le plan du jour, ne modifie rien. » Il lit les projets et les tâches, repère ce qui est en retard et propose. Toute création de tâche attend ma validation.
>
> Les humains décident. Les agents exécutent ce qui est autorisé. RapidoRH garde la trace.
>
> (Démo tournée sur un projet fictif, en local.)
>
> #IA #MCP #Claude #Management #BuildInPublic #BraindCode

**Instagram**

> Mes équipes + mes agents IA = une seule organisation 🧩
> RapidoRH × Claude
> L'IA propose, je valide ✅
> #ia #management #claude #entrepreneur #braindcode
