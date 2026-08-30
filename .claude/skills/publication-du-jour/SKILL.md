---
name: publication-du-jour
description: La sortie éditoriale du jour, de bout en bout — articles du site, posts sociaux, vidéo de l'épisode programmé. Utiliser chaque matin, ou quand on demande « qu'est-ce qui sort aujourd'hui », « lance la publication du jour », « le brief éditorial ». Ne publie jamais sur un réseau sans qu'un humain ait validé la pièce.
---

# Publication du jour · routine D5

## Objectif chiffré

Que rien de programmé pour aujourd'hui ne reste au sol. **Zéro contenu daté
d'aujourd'hui encore en brouillon à midi.**

## Garde-fous

- **Aucune publication sociale d'un épisode non `valide`.** `valide` se pose
  par un humain dans `/admin/production` ; aucun outil ne l'expose. Un épisode
  `pret` se prépare, il ne part pas.
- **Aucun envoi direct** — pas d'e-mail, pas de SMS, pas de message. On dépose
  des brouillons ; un humain envoie.
- **Aucune suppression, aucune dépublication.** Si quelque chose semble devoir
  sortir de la file, le dire et s'arrêter.
- En cas de doute sur un contenu, **le laisser et le signaler**. Une sortie
  manquée se rattrape ; une sortie ratée reste en ligne.

## Marche à suivre

1. **`routine_du_jour`** (site) — la vue d'ensemble : ce qui est programmé,
   ce qui manque, ce qui bloque. C'est le seul appel qui décide de la suite ;
   si elle ne rend rien à faire, s'arrêter là et le dire en une phrase.
2. **`publier_les_articles_du_jour`** (site) — les articles arrivés à échéance.
   Lire les refusés : un article refusé pour visuel manquant n'est pas le même
   problème qu'un article refusé pour statut.
3. **`publier_les_posts_du_jour`** (site) — les posts sociaux du jour.
4. **`prochaines_publications`** (catalogue social) — l'épisode vidéo du jour,
   s'il y en a un. Puis **`dossier_publication_video`** sur son identifiant :
   il rend, compte par compte, la vidéo en URL absolue, la légende et le
   brouillon RapidoCMS déjà rempli.
5. Pour chaque compte dont la pièce est `valide` et le créneau à venir :
   `upload_file_tool` → `create_draft_tool` → `schedule_draft_tool` (RapidoCMS).
   **WhatsApp, le profil LinkedIn et TikTok se relaient à la main** : préparer
   le clip et la légende, et les lister à la fin pour l'humain.
   **YouTube ne passe pas par RapidoCMS** : sa ligne va au MCP YouTube.
6. **`enregistrer_execution_routine`** (BraindCode) — clore la boucle : ce qui
   est parti, ce qui a échoué, ce qui attend une validation humaine. Une
   routine dont l'exécution n'est pas mesurée ne se pilote pas.

## Ce qu'il faut rendre à la fin

Cinq lignes au plus :

- **Parti** — combien d'articles, combien de posts, quels réseaux.
- **À relayer à la main** — la liste, avec le lien du média et la légende.
- **Bloqué** — quoi et pourquoi, en une phrase par ligne bloquée.
- **En attente de validation humaine** — les pièces `pret` mais pas `valide`.
- **Rien à faire** si c'est le cas. Le dire franchement vaut mieux qu'un
  rapport qui donne l'illusion du travail.
