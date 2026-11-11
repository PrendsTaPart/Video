---
description: Produit un tutoriel RapidoCRM Académie de bout en bout
argument-hint: <module> <numero>
---

Produis le tutoriel **$1 V$2** de RapidoCRM Académie, de l'enregistrement d'écran
jusqu'à la page publiée.

Avant de commencer, lis `CLAUDE.md` : le ton, la charte et les règles de
traçabilité y sont non négociables.

## Marche à suivre

1. Lance `npm run tuto -- $1 $2`.
2. La chaîne s'arrête chaque fois qu'un **appel MCP** est requis : elle écrit une
   demande dans `content/$1/V$2*/mcp/*.demande.json`. Exécute l'outil MCP indiqué,
   dépose le JSON de réponse dans le fichier `.reponse.json` correspondant, puis
   relance la même commande.
3. Elle s'arrête aussi quand un **travail de rédaction** est requis
   (`analyse.json`, `fiche.json`, `script.json`) : suis la consigne écrite à côté
   (`*-demande.md`), écris le fichier attendu, relance.
4. **Point d'arrêt 1** — présente-moi un résumé lisible : le hook retenu et ses
   3 alternatives, la punchline retenue et ses 3 alternatives, la durée estimée,
   et tout avertissement de débit. Attends mon choix avant de continuer.
5. **Point d'arrêt 2** — après le rendu de prévisualisation, donne-moi le chemin
   du fichier et attends ma validation.
6. Après la QA verte, enchaîne les trois publications.

Ces deux points d'arrêt ne sont jamais contournés.

## À la fin

Affiche en clair, sur trois lignes :

- **Page** : l'URL du tutoriel sur l'Académie
- **YouTube** : l'URL de la vidéo
- **AWS** : le lien du master 16:9 dans la bibliothèque RapidoCMS

Puis la durée finale et le nombre de mots de la transcription.
