---
name: trous-de-publication
description: Trouver les écrans du logiciel dont on n'a jamais parlé, et proposer de quoi les combler avec ce qui existe déjà. Utiliser une fois par semaine, ou quand on demande « de quoi parler », « les trous du calendrier », « quels sujets manquent ». Ne crée que des idées d'article au statut brouillon.
---

# Trous de publication · routine D4

## Objectif chiffré

**Réduire chaque semaine le nombre d'écrans sans aucun contenu.** On mesure le
nombre d'écrans couverts par au moins un article, un épisode ou un tutoriel ;
il doit monter, jamais descendre.

## Pourquoi cette routine existe

Le calendrier éditorial se remplissait par sujets — ce dont on avait envie de
parler. Le logiciel, lui, a des écrans que personne n'a jamais expliqués. Cette
routine part de la carte plutôt que de l'envie, et **ne propose que ce qui
s'appuie sur du matériel existant** : un écran qui a déjà son épisode vidéo et
son tutoriel n'attend qu'un article, et cet article s'écrit vite.

## Garde-fous

- **Aucun contenu publié, aucun contenu programmé.** Cette routine crée des
  idées au statut `idee`. Rien d'autre.
- **Aucune génération de plan vidéo.** La règle du dépôt est ferme : on
  cherche d'abord dans la bibliothèque Higgsfield existante, et si rien ne
  convient, on rend le prompt à l'humain — on n'appelle pas Higgsfield.
- **Trois propositions au maximum par exécution.** Une liste de vingt trous ne
  se traite pas ; trois se traitent dans la semaine.

## Marche à suivre

1. **`ecrans_sans_couverture`** (hub) — les écrans sans outil MCP, sans
   tutoriel, ou au lien à reprendre. Les trois manques sont distincts : un
   écran sans outil ne se pilote pas, un écran sans tutoriel ne s'apprend pas.
   Ne pas les confondre dans la sortie.
2. **`get_publishing_gaps`** (site) — les trous du calendrier éditorial.
3. Pour chaque écran candidat, les trois questions symétriques, avec le même
   couple `module` + `ecran` :
   - **`contenus_du_module`** (site) — a-t-on écrit dessus ?
   - **`episodes_du_module`** (catalogue social) — a-t-on tourné dessus ?
   - **`tutoriels_du_module`** (Académie) — l'enseigne-t-on ?
4. **Classer par facilité, pas par manque.** Un écran qui a déjà sa vidéo et
   son tutoriel mais pas d'article est le meilleur candidat : la matière
   existe, il ne manque que la rédaction. Un écran sans rien est le plus
   coûteux — le signaler, ne pas le proposer en premier.
5. **`create_article_idea`** (site) sur les trois meilleurs, en passant
   `module_logiciel` et `ecran_logiciel` : sans quoi le prochain passage de
   cette routine croira le trou toujours ouvert.
6. **`enregistrer_execution_routine`** (BraindCode) avec le nombre d'écrans
   couverts, pour que la série se trace.

## Ce qu'il faut rendre à la fin

- **Les trois idées créées**, avec pour chacune l'écran visé et ce qui existe
  déjà pour l'appuyer (l'épisode, le tutoriel, leurs liens).
- **Les écrans nus** — sans vidéo ni tutoriel ni article : à traiter, mais
  c'est un chantier de production, pas de rédaction. Les nommer, ne pas les
  transformer en idées d'article.
- **Le compte** : combien d'écrans couverts cette semaine, combien la
  précédente.
