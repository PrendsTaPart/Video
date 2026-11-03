# Vidéo 16 · Mon IA forme mes clients ! (FoodEatUp Academy + MCP pédagogique)

Format vertical 1080 × 1920, 56 s. Voix Noé (ElevenLabs, eleven_v4). **Rien n'a été publié ni modifié : lecture seule.**

## Voix off

> Aujourd'hui, je vais te montrer comment j'ai automatisé une partie de la formation et du support client de FoodEatUp.
>
> Parce que développer un logiciel, c'est une chose… Mais expliquer à chaque client comment l'utiliser, c'en est une autre !
>
> Alors, j'ai créé FoodEatUp Academy : cent soixante-treize tutoriels vidéo en ligne, sur deux cent trente prévus. Et surtout, j'ai connecté toute cette documentation à Claude et ChatGPT grâce à mon MCP.
>
> Maintenant, un restaurateur peut simplement demander : « Comment je fais un relevé de température ? »
>
> L'IA retrouve le bon tutoriel, lui donne la vidéo, en carte ou en lien selon l'application, lui explique les étapes, et peut même lui proposer un quiz ! Elle peut aussi créer un parcours de formation adapté à son métier.
>
> Et ce MCP ne fait qu'enseigner : il ne touche jamais aux données du restaurant.
>
> Avant, mes clients devaient chercher dans les tutoriels. Maintenant, c'est l'IA qui trouve le bon tutoriel et leur apprend à utiliser le logiciel. Et ce n'est que le début de mon service client automatisé !

## Ce qui est réel (appels MCP « Tuto FoodEatUp » du 26/10)

| Outil | Résultat réel utilisé à l'écran |
|---|---|
| `capacites_foodeatup` / catalogue | 230 fiches, 173 vidéos en ligne (le site Academy affiche « 173 vidéos en ligne sur 230 ») |
| `rechercher_tutoriels("relevé de température")` | 5 résultats ; le premier est `relever-une-temperature-equipement` (0:38) |
| `carte_tutoriel` | renvoie un lien de ressource et un HTML `ui://` avec la vidéo ; **affiché dans un navigateur**, pas dans Claude ni ChatGPT |
| `lecteur_video_tutoriel` | URL de la vidéo, YouTube, 8 étapes |
| `quiz_tutoriel` | 3 questions (QCM, ordre, ouverte) |
| `parcours_apprentissage(débutant, HACCP, 15 min)` | 5 leçons : classeur 0:48, équipements 0:51, température 0:38, nettoyage 0:40, étiquettes 1:02 |

La vidéo du tutoriel montrée dans la carte est le vrai tutoriel « Relever une température d'équipement ».

## Ce qui n'est pas vérifié

- Le rendu de la carte HTML **dans Claude.ai ou ChatGPT** n'a pas été testé : dans Claude Code, elle arrive en texte. D'où la mention « en carte ou en lien selon l'application » et la légende à l'écran.
- Aucune fausse capture de Claude ou de ChatGPT : la question est mise en scène dans une bulle neutre, la réponse vient des sorties brutes du MCP.
- « Service client automatisé » : seule la partie formation/support par tutoriels existe ; la suite (agents de support) est annoncée comme une prochaine étape.

## Changements par rapport à ton script

- « 173 tutoriels » devient « 173 tutoriels en ligne sur 230 prévus » (chiffre du MCP) ;
- « lui donne la vidéo » précisé « en carte ou en lien selon l'application » ;
- ajout de la phrase « ce MCP ne fait qu'enseigner : il ne touche jamais aux données du restaurant » (le serveur est public et en lecture seule).
