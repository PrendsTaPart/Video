# Épisode 10 · J'ai automatisé mes 4 chaînes YouTube avec l'IA

Format vertical 1080 × 1920 : une version de 120 s et une version courte de 45 s.

**Rien n'a été publié.** Aucun outil d'écriture n'a été appelé pendant l'audit : aucune publication, aucune suppression, aucune modification de chaîne, aucun changement d'autopilote.

## Livrables

| Livrable | Fichier |
|---|---|
| Vidéo principale (120 s) | `renders/episode10-youtube-publisher_1080x1920.mp4` |
| Version courte (45 s) | `renders/episode10-youtube-publisher_45s_1080x1920.mp4` |
| Miniature « J'AI AUTOMATISÉ 4 CHAÎNES YOUTUBE » | `renders/miniature-episode10-1080x1920.jpg` |
| Voix off (Noé, ElevenLabs) et mixage | `audio/` |
| Sous-titres SRT et ASS | `sous-titres/` |
| Captures réelles (pages publiques) | `captures/` |
| Composition HTML | `composition/` |

## Audit

### Sources

- **Projet Lovable `8013cc12` (YouTube Publisher Bot).**
  - Code lu : route `_authenticated/autopilot.tsx`, cron `api/public/cron/autopilot`, serveur MCP.
  - Feuille de route : l'autopilote est marqué terminé (page, moteur de score, file, cron quotidien, outils). Le paiement (Paddle) est en attente.
- **Site public `youtube.rapidocms.com`**, capturé le 26/10.
  - Galerie des vidéos partagées : FoodEatUp 87, RapidoCRM 71, Plan-it 18, RapidoCMS 16, soit 192.
  - Ce sont des vidéos *partagées dans la galerie*, pas le total publié sur chaque chaîne.
- **Manifeste MCP public** : 86 outils, chacun aussi préfixé `yt_`. Parmi eux : `list_channels`, `list_videos`, `get_channel_status`, `get_channel_analytics`, `schedule_video`, `set_autopilot`, `get_slot_scores`, `queue_autopilot`.
- **MCP social FoodEatUp** (pour comprendre, en lecture seule).
  - File de diffusion à venir : EP522 → EP531 (série UpEatFood).
  - Aucun relevé de statistiques YouTube enregistré.

### Limite : le MCP YouTube n'est pas connecté

Le MCP YouTube n'était pas connecté dans cette session. `yt_list_channels`, `yt_get_channel_status`, `yt_list_videos` et `yt_get_channel_analytics` n'ont donc **pas** pu être appelés.

Les chiffres suivants viennent de ton relevé et sont présentés à l'écran comme « non revérifiés » :
- 4 chaînes ;
- 354 entrées dans le catalogue, en précisant qu'il ne s'agit pas de 354 vidéos publiées ;
- des Shorts FoodEatUp programmés jusqu'au 31/10.

Pour revérifier, ajoute le connecteur `youtube-publisher-pro` et je relance l'audit en lecture seule.

### Écart avec le brief

Le brief cite « Formation BraindCode » comme quatrième chaîne. La galerie montre **Plan-it** (« Plan-it par BraindCode »). La vidéo affiche Plan-it.

### Statut des fonctionnalités

Légende : ✓ vérifié · ? non vérifié · — pas encore.

| Fonction | Codée | Configurée | Testée | Exécutée | Preuve |
|---|---|---|---|---|---|
| Galerie publique des vidéos | ✓ | ✓ | ✓ | ✓ | Site en ligne, 192 vidéos partagées |
| Serveur MCP (86 outils) | ✓ | ✓ | ? | ? | Manifeste public. Appels non faits : MCP non connecté |
| Programmation des Shorts | ✓ | ? | ? | ? | Ton relevé (jusqu'au 31/10), non revérifié |
| Autopilote | ✓ | ? | ? | — | Code et feuille de route ; activation non vérifiée, `set_autopilot` non appelé |
| Tests A/B des miniatures | ✓ | ? | ? | ? | Seuil de 95 % dans le code. L'exemple de la page d'accueil est marqué « illustratif » |
| Analyses (vues, interactions) | ✓ | ? | ? | ? | Aucun chiffre affiché |
| Paiement des crédits | — | — | — | — | Demande par e-mail ; Paddle en attente |

**La vidéo ne dit pas que l'autopilote choisit les heures tout seul.** Elle dit qu'il est *capable de proposer* des créneaux, et affiche « Autopilote activé ? non vérifié ».

## Voix off

La voix est Noé (ElevenLabs), pas un clone de ta voix. Une phrase a été ajustée pour rester exacte : « j'avais déjà des Shorts programmés… lors de mon dernier relevé ».

> Aujourd'hui, je vais vous montrer comment j'ai automatisé mes 4 chaînes YouTube. Et pour ça, j'ai développé mon propre logiciel, connecté directement à mes agents IA.
>
> Avec plusieurs logiciels et projets à présenter, je devais gérer différentes chaînes, préparer les vidéos, écrire les titres, programmer les publications et suivre les résultats. J'ai donc décidé de centraliser tout ça.
>
> J'ai construit YouTube Publisher Bot avec Lovable. Depuis une seule interface, je peux organiser mes vidéos, gérer leurs informations, retrouver l'historique et visualiser mon calendrier de publication.
>
> Mais la vraie différence, c'est que j'ai connecté ce logiciel à un MCP YouTube. Mes agents IA peuvent consulter mes chaînes, récupérer les vidéos, analyser les données et préparer des actions directement depuis Claude.
>
> Sur FoodEatUp, j'avais déjà des Shorts programmés sur plusieurs jours lors de mon dernier relevé. Et mon système dispose aussi d'un autopilote, capable de proposer des créneaux de publication à partir de l'historique de la chaîne.
>
> Et une fois les vidéos publiées, je peux exploiter les données pour comprendre ce qui fonctionne. Les vues, les interactions et les performances. L'objectif, c'est que mes agents m'aident à améliorer les prochaines publications.
>
> Mon objectif n'est pas seulement d'automatiser YouTube, c'est de construire une équipe d'agents IA capables de travailler avec mes propres logiciels pendant que je me concentre sur les produits et les clients. Et demain, je vous présenterai un nouveau projet et mon travail du jour.

## Storyboard

| Temps (s) | Scène | Images |
|---|---|---|
| 0–10 | Accroche | Photo officielle. Les 4 chaînes convergent vers YouTube Publisher Bot. « 4 CHAÎNES. UN SEUL SYSTÈME. » |
| 10–21,3 | Pourquoi | Pages réelles des 4 chaînes. Tâches : préparer, écrire, programmer, suivre. « Tout centraliser » |
| 21,3–31,4 | L'application | Logo Lovable. Accueil (visuels d'exemple signalés), vidéos publiées, page de chaîne, connexion. Le calendrier, derrière la connexion, n'est pas filmé |
| 31,4–41,6 | Les 4 chaînes (sans voix) | Galerie : 87 / 71 / 18 / 16 vidéos partagées |
| 41,6–53,4 | Le MCP | Claude → MCP YouTube → Publisher Bot. 86 outils. « 354 entrées ≠ 354 vidéos publiées ». « Non revérifié » |
| 53,4–64 | Programmation et autopilote | Shorts (ton relevé), page, score, file et cron codés. « Activé ? non vérifié » |
| 64–78,5 | Statuts (sans voix) | Tableau codé / configuré / testé / exécuté |
| 78,5–88,9 | Analyse | Vues, interactions, performances : « — ». « Aucun chiffre inventé » |
| 88,9–95,8 | La boucle (sans voix) | Contenu → programmation → publication → analyse → amélioration |
| 95,8–108,4 | Conclusion | Photo. « Une équipe d'agents IA qui travaille avec mes propres logiciels ». « Demain : un nouveau projet » |
| 108,4–120 | Carton | BRAINDCODE × YOUTUBE PUBLISHER BOT × CLAUDE · MON QUOTIDIEN D'ENTREPRENEUR À L'ÈRE DE L'IA |

La version de 45 s enchaîne : accroche → MCP → programmation et autopilote → conclusion.

## Publications (brouillons, à valider)

**LinkedIn**

> J'ai automatisé mes 4 chaînes YouTube. Pas avec un outil du marché : avec le mien.
>
> FoodEatUp, RapidoCRM, RapidoCMS, Plan-it… Chaque logiciel a sa chaîne. Préparer, titrer, programmer, suivre : c'était devenu un métier à part.
>
> Alors j'ai construit YouTube Publisher Bot avec Lovable, et je l'ai branché à un serveur MCP. Résultat : mes agents IA consultent mes chaînes, récupèrent les vidéos et préparent les actions depuis Claude.
>
> Ce qui tourne, ce qui est prêt, ce qui reste à vérifier :
> ✅ 192 vidéos partagées dans la galerie publique
> ✅ 86 outils MCP déclarés
> 🟠 un autopilote codé, capable de proposer des créneaux à partir de l'historique, pas encore vérifié en production
>
> Je ne me contente plus d'utiliser des outils IA. Je développe les miens et je les connecte à mes agents.
>
> #IA #YouTube #MCP #Claude #Lovable #BuildInPublic #BraindCode

**Instagram / TikTok**

> J'ai automatisé 4 chaînes YouTube 🤖📺
> Mon propre logiciel + un MCP + Claude
> Codé ✅ · testé 🟠 · la suite demain
> #ia #youtube #claude #entrepreneur #buildinpublic

**YouTube Shorts**

- **Titre :** J'ai automatisé mes 4 chaînes YouTube avec l'IA #Shorts
- **Description :** J'ai développé YouTube Publisher Bot avec Lovable et je l'ai connecté à un serveur MCP pour que mes agents IA (Claude) gèrent mes chaînes FoodEatUp, RapidoCRM, RapidoCMS et Plan-it. Ce qui est codé, ce qui est testé, ce qui reste à vérifier. Épisode 10 de « Mon quotidien d'entrepreneur avec l'IA ». youtube.rapidocms.com
- **Tags :** IA, YouTube, automatisation, MCP, Claude, Lovable, agents IA, entrepreneur, BraindCode, build in public
