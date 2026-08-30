---
name: episode-multicanal
description: Déposer un épisode vidéo monté sur toutes ses pièces et préparer sa sortie sur les six réseaux. Utiliser après un montage, ou quand on demande « dépose l'épisode NN », « prépare la sortie de l'épisode », « publie l'épisode ». Une seule vidéo, un seul lien de stockage — seul le contenu du poste change d'un réseau à l'autre.
---

# Publication multicanale d'un épisode · routine E5

## Objectif chiffré

**Un épisode monté est déposé et préparé sur ses six réseaux en un passage**,
sans qu'aucune pièce reste sur une ancienne URL.

## La règle de saison

**Une seule vidéo, un seul lien de stockage.** Le master 9:16 part tel quel sur
Instagram, WhatsApp, Facebook, TikTok, YouTube et LinkedIn ; seul le texte du
post change. Cette règle vaut pour tous les épisodes à venir, pas seulement
celui-ci.

Elle est tenue par l'outil, pas par la discipline : `deposer_episode` écrit la
même URL sur les six pièces en un appel, avec **un seul contrôle** de l'URL.
Six appels de `publier_video` faisaient six contrôles du même fichier et
laissaient, quand l'un échouait, un épisode sur cinq réseaux avec l'ancienne
vidéo sur le sixième.

## Garde-fous

- **`publier_video` ne sert plus qu'à corriger une pièce isolée.** Pour un
  dépôt complet, c'est `deposer_episode`.
- **Rien ne se programme sans `valide`.** Un agent constate qu'un fichier
  répond (`pret`) ; il ne décide pas qu'une vidéo est bonne. La validation est
  un geste humain dans `/admin/production`.
- **L'URL doit être servie en `video/mp4`.** L'URL brute de GitHub sort en
  `application/octet-stream` et le catalogue la refuse : passer par la
  bibliothèque RapidoCMS.
- **Aucune génération Higgsfield.** Si un plan manque, rendre le prompt à
  l'humain — texte et Reference Elements — pour qu'il le génère lui-même.

## Marche à suivre

1. **`dossier_montage`** sur l'épisode — l'état des pièces, les sources, ce
   qui manque. Lire `manquant` avant tout le reste.
2. **`deposer_episode`** avec l'identifiant et l'URL RapidoCMS du master. Lire
   `echecs` : une pièce qui n'a pas basculé se voit là, et nulle part ailleurs.
3. **`dossier_publication_video`** — compte par compte : la vidéo en URL
   absolue, la légende, et le brouillon RapidoCMS déjà rempli (`social_type`,
   `account_id`, `media_url`, `media_caption`). **Ne jamais inventer un
   `account_id`.**
4. Les six réseaux ne se traitent pas pareil, et c'est normal :
   - **RapidoCMS** publie Instagram, Facebook, TikTok et la page LinkedIn.
   - **YouTube** passe par son propre MCP : titre ≤ 100 caractères `#Shorts`
     compris, description avec le lien de l'épisode, tags, URL du short.
   - **WhatsApp et le profil LinkedIn** se relaient depuis le téléphone :
     préparer le clip et la légende, puis `marquer_publications` une fois le
     relais fait par l'humain.
5. **`episodes_du_module`** pour vérifier que l'épisode ressort bien sur son
   écran — c'est le contrôle que la clé partagée est en place, et il coûte un
   appel.
6. **`enregistrer_execution_routine`** (BraindCode).

## Ce qu'il faut rendre à la fin

- **Les six pièces et leur état** après dépôt, avec l'URL commune.
- **Les brouillons créés**, réseau par réseau, avec leur créneau.
- **À relayer à la main** — WhatsApp, profil LinkedIn : le lien du média et la
  légende, prêts à coller.
- **Ce qui attend un humain** : la validation, s'il en manque une.
