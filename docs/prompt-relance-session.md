# Prompt de relance — nouvelle session Claude Code

Tu reprends le travail de Michael Kebail-Ali sur sa série vidéo « Mon quotidien d'entrepreneur avec l'IA » et sur son site lien-en-bio.

## Dépôts
- `PrendsTaPart/michael-au-quotidien` : site (TanStack Start + Lovable, projet Lovable `255f6f6f-ae7c-4ba7-8c89-c6e431c71eef`, https://michael.foodeatup.fr). Travailler sur `main`, `git pull --rebase` avant chaque push (Lovable pousse aussi sur `main`), puis déployer avec `deploy_project`. Avant de pousser : `npx tsc --noEmit`, `npx vitest run` et `npm run build` doivent passer.
- `PrendsTaPart/Video` : livrables vidéo dans `videos/episodeNN-…/`, branche `ccr-ba06575d-u3dbto`.

## Méthode (obligatoire)
Appelle d'abord l'outil MCP `obtenir_methode_video` du serveur Journal FoodEatUp. Il donne la voix ElevenLabs (Noé, `7pDdnNI6PhXmAp0pXFZm`, `eleven_multilingual_v2`), le format, la charte, la structure des scènes et les interdits.
En bref :
- vidéo 120 s et short 45 s, 1080 × 1920 ;
- composition HTML `render(t)`, rendue en images avec Playwright, puis mixée, sous-titrée et encodée avec ffmpeg ;
- héberger la vidéo dans la bibliothèque RapidoCMS (`upload_file_tool`) ;
- créer la vidéo en brouillon sur le site (`creer_video`).

## Règles permanentes
- Ne rien publier ni envoyer sans validation de Michael.
- Ne contacter aucun prospect.
- Aucune donnée, capture ou résultat inventé ; masquer les données personnelles et les secrets.
- Logos officiels uniquement ; aucune image d'une personne sans autorisation.
- Jamais de nouvelle vidéo Higgsfield.
- Ne pas consulter Social FoodEatUp ; ne pas citer Lüks Coffee.
- Production en lecture seule sauf autorisation.
- Campagnes et posts en brouillon ; les contacts des formulaires ne sont pas des abonnés marketing sans consentement.

## État au 28/10/2026
- Épisodes 31, 33 et 34 : publiés sur le site.
- Épisode 34 (Salle Live) : livrables dans `videos/episode34-salle-live/`. Les écrans de la console n'ont pas été filmés (il faut un compte de démonstration).
- Outil MCP `obtenir_methode_video` : en ligne sur `main`.

## Reste à faire
1. **Épisode 32** (« À 19 h, j'ai confié à Claude mon système de nurturing ») :
   - la fiche existe en brouillon sur le site, sans vidéo ;
   - produire la vidéo 120 s, le short, la miniature, les sous-titres et les posts ;
   - créer la campagne email et les publications sociales en brouillon ;
   - publier seulement après accord de Michael.
2. **Épisode 35** (« J'ai offert à ma sœur un site web et des agents IA ») :
   - la planche de style et la prévisualisation sont dans `videos/episode35-la-chaine-fraternelles-preview/` ; lire `episode35-elements-recuperes.md` ;
   - **attendre la validation de Michael avant le rendu** ;
   - charte : Deep Rose #BC4792, Soft Pink #E080B4, Light Gray #ECF0F3, noir ; polices Inter et Dancing Script ; logo officiel ;
   - aucune image de sa sœur ni de bénévoles identifiables, aucun extrait de Koh-Lanta ;
   - les séquences sur les agents IA restent marquées « Possibilité » tant qu'aucune preuve réelle n'est fournie ;
   - les exports Canva propres demandent le connecteur Canva ou des fichiers déposés par Michael.
3. **Envoi des emails** : les secrets Resend (`RESEND_API_KEY`, `EMAIL_EXPEDITEUR`) ne sont pas configurés. Le signaler, ne pas contourner.
4. **Formations 31 et 32 et lead magnet 32** : toujours en brouillon ; les publier seulement sur accord.
5. **Nouvel épisode « Mes projets » FoodEatUp** (31 octobre → 2 novembre 2026) : brief ci-dessous.

## Brief « Ce qu'on a construit sur FoodEatUp ces deux derniers jours »
Épisode « Mes projets » du Journal FoodEatUp, projet FoodEatUp :
- appeler `obtenir_projet` pour la charte et les assets ;
- 2 à 3 minutes ;
- montrer à un restaurateur ce qui est arrivé dans son logiciel du 31 octobre au 2 novembre 2026.

Règles d'écriture :
- aucun mot technique (pas « API », « MCP », « serveur », « base de données », « migration », « webhook », « jeton ») ;
- dire « votre assistant IA », « automatiquement », « en un clic » ;
- vouvoyer le restaurateur, phrases courtes, ton chaleureux ;
- chaque module suit le même schéma : problème vécu en service → ce que fait maintenant FoodEatUp → bénéfice ;
- aucun chiffre, prix ni résultat qui ne soit pas écrit dans le brief ;
- écrans : uniquement de vraies captures du compte de démonstration FoodEatUp, jamais redessinées ; logo officiel FoodEatUp.

⚠️ La liste des modules livrés sur la période n'est pas dans ce brief : la demander à Michael (ou la relever dans les commits réels des dépôts FoodEatUp sur la période) avant d'écrire le script.

Commence par vérifier l'état réel (`lister_videos`, `git log`) puis propose le plan à Michael.
