# Épisode 5 · Je donne un objectif à Claude, mes agents IA recherchent mes futurs clients

Vertical 1080 × 1920, 120 s (+ version de 45 s). **Rien n'a été publié. Aucun prospect n'a été contacté, aucune recherche n'a été lancée, aucune donnée n'a été écrite.**

## Livrables

| Livrable | Fichier |
|---|---|
| Vidéo principale (120 s) | `renders/episode5-prospection_1080x1920.mp4` |
| Version courte (45 s) | `renders/episode5-prospection_45s_1080x1920.mp4` |
| Miniature « Claude trouve mes futurs clients » | `renders/miniature-episode5-1080x1920.jpg` |
| Schéma Claude → MCP Prospection → Prospects → Qualification → Campagne → Suivi | `renders/schema-workflow-prospection.jpg` |
| Voix off (Noé, ElevenLabs), mixage | `audio/` |
| Sous-titres SRT et ASS | `sous-titres/` |
| Script, storyboard, publications, audit | ci-dessous |

## Audit en lecture seule (MCP Prospection, 26/10/2026)

| Appel | Réponse réelle |
|---|---|
| `prospection_terms` (sans ajout) | 18 régions, 25 spécialités (dont Restaurant, Bar et brasserie, Boulangerie-pâtisserie, Traiteur, Food truck) |
| `prospection_history` | 50 dernières recherches, 1 786 résultats au total. Le 26/10 : 18 recherches « Bar et brasserie » de 40 résultats chacune, soit 720. Les 5 dernières (PACA, Pays de la Loire, Occitanie, Nouvelle-Aquitaine, Normandie) : **200 résultats**. Avant : garages automobiles (23/10), organisateurs d'événements (22/10) |
| `list_logs` | Le 26/10 : « Bar et brasserie — [région] : 5 clients ajoutés » pour les 18 régions (source `mcp`) |
| `list_clients` (Bar et brasserie) | 200 fiches lues : **90 créées le 26/10**, 90 le 09/10, 20 le 11/09. Toutes au statut « nouveau ». 139 avec e-mail, 197 avec téléphone, 199 avec site |
| `list_email_templates` | 2 modèles : « BraindCode — Cas clients » et « prospection clients rapidocms ». **Aucun modèle FoodEatUp** |
| `list_message_templates` | 1 SMS et 1 texte d'appel (offre RapidoCMS) |
| `list_emails` | Les 200 derniers : 105 envoyés le 26/10 et 95 le 23/10, vers 10 h (Paris). Offres RapidoCMS et BraindCode, statut « envoye » |
| `list_sms`, `list_calls` | Envois de septembre (RapidoCMS). Nombreux SMS en échec sur des numéros fixes. Les appels restent au statut « queued » |
| `list_calendar_posts` | Publications de septembre au statut « posté » |
| `list_linkedin_connections`, `stripe_stats` | Non consultés pour la vidéo : rien à montrer sans données personnelles ni chiffre d'affaires |
| Plan'It `list_routines` | **0 routine** |
| n8n | Pas d'accès depuis cette session. D'après le plugin, `run_prospection` et `send_email` passent par des webhooks n8n |

**Plugin `rapido-prospector`** (marketplace BraindCode) :
- 4 agents : chasseur, rédacteur de séquences, programmateur de contenus, contrôleur conformité et mesure ;
- 12 commandes, 20 skills, 7 hooks (garde-conformité, garde-envois, anti-doublon, journal…).

Son contrat : aucun envoi sans accord sur cet envoi. Un e-mail sans identité ni désinscription est refusé, un SMS sans STOP aussi. Les appels automatisés sont désactivés par défaut.

### ⚠️ Points de conformité à corriger avant toute campagne

1. **Les 200 derniers e-mails envoyés ne contiennent aucun lien de désinscription.** Les deux modèles d'e-mail n'en ont pas non plus. Avec le plugin, ces envois auraient été refusés par le hook de conformité.
2. **Le modèle SMS n'a pas de mention STOP.**
3. **Appels automatisés.**
   - Des appels en synthèse vocale ont été lancés en septembre.
   - Le plugin les désactive par défaut et marque sa note juridique « à faire valider par un juriste ».
   - À trancher avec un juriste avant de reprendre.
4. Pour la vidéo, les noms des établissements sont masqués et aucune coordonnée n'apparaît. Les numéros visibles dans les journaux ne sont montrés nulle part.

### Démonstration (8 étapes, lecture seule)

1. **Objectif.** Le prompt est affiché à l'écran.
2. **Régions et spécialités.** `prospection_terms`.
3. **Historique.** `prospection_history`.
4. **Résultats et prospects.** `list_clients` et `list_logs`, noms masqués.
5. **Modèles.** `list_email_templates` et `list_message_templates`.
6. **Campagne FoodEatUp en brouillon** (texte de la vidéo, non enregistré) :
   - objet : « Votre brasserie, pilotée depuis une seule application » ;
   - identité de l'expéditeur, lien de désinscription, politique de confidentialité.
7. **Rapport.** Créer le modèle FoodEatUp, tester sur 10 établissements, relance J+3 à valider, sans SMS ni appel.
8. **Validation.** `send_email` et `add_email_template` non appelés : **en attente de ta validation**.

**Entonnoir montré** (sans mélanger les étapes) : 720 résultats → 90 enregistrés → 0 qualifié → 0 contacté par une campagne FoodEatUp → réponses non mesurées → ventes « — ». Aucun revenu n'est cité.

## Voix off

> Après avoir construit mes applications, mes agents IA et mes outils de communication, il me reste une question essentielle : comment trouver des clients ?
>
> Aujourd'hui, je peux simplement demander à Claude de rechercher des restaurants ou des brasseries dans les régions qui m'intéressent. Je lui donne un objectif… et une règle : ne contacter personne sans ma validation.
>
> Grâce au MCP que j'ai développé pour Prospector Hub, Claude peut consulter les régions et les spécialités, lancer des recherches autorisées, et retrouver les résultats directement dans mon logiciel. Derrière, ce sont des workflows n8n qui font les recherches.
>
> Par exemple, mes cinq dernières recherches, sur les bars et brasseries, ont retourné deux cents résultats sur cinq régions. Et le logiciel garde l'historique des recherches et des établissements enregistrés. Deux cents résultats de recherche : pas deux cents clients.
>
> Mais trouver une entreprise ne suffit pas. Il faut vérifier les informations, comprendre son activité, éviter les doublons, et préparer une approche pertinente. Aujourd'hui, quatre-vingt-dix bars et brasseries ont été enregistrés : ils sont encore au statut « nouveau ».
>
> Ensuite, les routines prennent le relais : préparer les messages, suivre les campagnes, proposer les relances, analyser les résultats. Claude orchestre les étapes avec les outils autorisés. Mais pour qu'une routine tourne seule, elle doit être configurée dans un orchestrateur, comme n8n ou Plan'It.
>
> Mon système gère aussi plusieurs canaux : e-mails, SMS, LinkedIn et appels automatisés, avec des règles : l'identité de l'expéditeur, la désinscription, et mon accord avant chaque envoi.
>
> Mon objectif, ce n'est pas d'envoyer des milliers de messages au hasard. C'est de construire une prospection intelligente, ciblée et mesurable, pilotée depuis Claude.

## Storyboard

| Temps | Scène | Images |
|---|---|---|
| 0–9 | Accroche | Écran de connexion réel de Prospector Hub, Michael (pose), logos Claude, FoodEatUp, BraindCode, « Comment trouver des clients ? » |
| 9–19,2 | L'objectif | Le prompt tapé dans Claude, la règle en orange, pastille « Ne contacte personne sans ma validation » |
| 19,2–32,2 | Le MCP | Réponse réelle de `prospection_terms`, outils du MCP, webhook n8n, enregistrement sur accord |
| 32,2–45,1 | Résultats | Les 5 dernières recherches (5 × 40), compteur 200, « 200 RÉSULTATS DE RECHERCHE ≠ 200 CLIENTS » |
| 45,1–58,3 | Qualification | Entonnoir réel (720 → 90 → 0 → 0 → non mesuré → —), 5 prospects masqués au statut « nouveau » |
| 58,3–75,9 | Démo, sans voix | Brouillon d'e-mail FoodEatUp, 5 contrôles (dont « aucun modèle FoodEatUp »), rapport, « En attente de ma validation » |
| 75,9–90,6 | Routines | 4 étapes, ce qui existe (modèles, calendrier, journal, 0 routine Plan'It), « à configurer dans n8n ou Plan'It » |
| 90,6–101,1 | Canaux | E-mail, SMS (STOP), LinkedIn, appels (désactivés par défaut), « Aucun envoi pendant ce tournage » |
| 101,1–110 | Conclusion | « Pas au hasard. Ciblée. Mesurable. Pilotée depuis Claude. », Michael |
| 110–120 | Carton | BRAINDCODE × CLAUDE × PROSPECTOR HUB · « Des objectifs. Des agents IA. Des opportunités commerciales. » |

**Version 45 s** : accroche → objectif → résultats → conclusion → carton.

## Publications

**LinkedIn**
> Je donne un objectif à Claude. Mes agents IA cherchent mes futurs clients.
>
> Mon prompt : « Analyse mes dernières prospections, identifie les nouveaux établissements et prépare une campagne adaptée à FoodEatUp. Ne contacte personne sans ma validation. »
>
> Derrière, Prospector Hub, mon logiciel, et son serveur MCP : régions, spécialités, historique, établissements enregistrés, modèles de messages.
>
> Les chiffres du jour, sans les maquiller :
> 🔎 5 recherches = 200 résultats (bars et brasseries, 5 régions)
> 📇 90 établissements enregistrés aujourd'hui, tous au statut « nouveau »
> ✋ 0 contacté pour FoodEatUp : la campagne est en brouillon, elle attend mon accord
>
> 200 résultats de recherche, ce ne sont pas 200 clients. La vraie valeur, c'est la qualification, le ciblage et la mesure.
>
> #Prospection #IA #ClaudeCode #MCP #FoodEatUp #BuildInPublic

**Instagram**
> Claude cherche mes futurs clients 🔎
> 200 résultats ≠ 200 clients
> Qualifier, cibler, mesurer… et valider avant d'envoyer ✋
> #prospection #ia #claude #entrepreneur #foodeatup
