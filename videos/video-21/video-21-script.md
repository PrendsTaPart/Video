# Vidéo 21 · Je forme mes employés IA !

Format vertical 1080 × 1920, 70 s. Voix Noé (ElevenLabs, eleven_v4). Logos : dépôt `video-20/assets/logos` (chartes officielles de FoodEatUp Formation).

## Voix off

> Tout le monde crée des agents IA. Mais qui leur apprend à faire correctement leur travail ?
>
> Aujourd'hui, je vais te montrer comment je forme mes employés IA. Parce qu'avoir une équipe d'agents IA, c'est bien… Mais si tes agents ne connaissent pas ton entreprise, tes méthodes et tes logiciels, ils vont faire n'importe quoi !
>
> Alors, j'ai développé une Academy. J'y organise mes formations, mes connaissances métier, mes prompts et les compétences nécessaires à chaque mission.
>
> Prenons un agent chargé d'éviter les ruptures de stock. Il apprend d'abord la procédure FoodEatUp : du stock bas à la commande préparée, jamais envoyée seule.
>
> Grâce aux MCP, il accède aux bons outils, et seulement à ceux-là.
>
> Ensuite, il passe le quiz. Sa consigne de départ est notée zéro sur six… Il la complète : six sur six !
>
> L'objectif, ce n'est pas seulement qu'une IA sache répondre. C'est qu'elle sache quoi faire, comment le faire, avec quels outils, et comment vérifier le résultat. Et la validation finale reste humaine.
>
> Avant, je formais des employés pour utiliser mes logiciels. Maintenant, je construis aussi les formations de mes employés IA !
>
> Et toi, tu formerais ton premier agent IA à quel métier ?

## Ce qui a été réellement appelé (MCP FoodEatUp Formation, 27/10, lecture seule)

| Étape | Outil | Résultat |
|---|---|---|
| Apprendre | `learn_task("Analyser les stocks… avant une rupture")` | aucune tâche outillée connue ; mission **F3 « Stocks et commandes fournisseurs »** ; verdict « suis la mission, fais une première fois en Aperçu, puis retiens la procédure (remember) » |
| | `get_mission(F3)` | 4 pas : produits sous le seuil → liste d'achats → commandes préparées par fournisseur → l'humain envoie |
| S'équiper | (outils cités par F3) | `list_low_stocks`, `get_shopping_list`, `list_suppliers`, `create_orders_from_shopping_list` (prépare, n'envoie pas) |
| S'entraîner | `get_quiz(F3)` + `check_quiz_answer` | 3 réponses données par l'agent, **3 justes**, corrigées par le serveur |
| Être évalué | `check_routine_prompt` | la consigne brute « Analyse les stocks et prépare les achats fournisseurs. » obtient **0/6** ; la consigne complétée (objectif, sources, limite, rendu, critère d'arrêt, accord humain) obtient **6/6** |

## Ce que la plateforme prend en charge (d'après `describe_server`)

- **Mémoire** : `remember` / `recall` / `archive_memory`. Le savoir d'équipe est validé par le responsable (`review_team_memory`).
- **Exercices pratiques** : `start_practical_exercise` en mode démonstration (établissement de démo, autonomie Aperçu ou Brouillon, n'écrit rien), puis `submit_exercise_evidence`.
- **Validation** : `verify_practical_result` ; la vérification finale reste humaine.
- **Mise en service d'un agent** : `set_agent_state` « en service » exige une routine V1, un KPI et un point d'arrêt.

## Limites

- « Agent Ruptures de stock » est un **agent de démonstration** : il n'existe pas dans `list_agents`, qui compte les 6 agents de la vidéo 20, tous « à configurer ».
- L'exercice n'a pas été lancé sur des données de restaurant. Les établissements accessibles (53, 58) ne sont pas des établissements de démonstration ; aucune donnée de stock n'est montrée.
- La page de mission F3 demande une connexion : la vidéo montre les pages publiques de l'Academy (captures de l'épisode 6) et les sorties des outils.
- Les erreurs de la séquence « n'importe quoi » sont une illustration, signalée à l'écran.
