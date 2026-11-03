# Vidéo 23 · Mon IA gère mes réunions ! (RapidoMeet)

Format vertical 1080 × 1920, 70 s. Voix Noé (ElevenLabs, eleven_v4). Identité RapidoMeet : violet #7C3AED et fuchsia #E91E8C (icône et `index.css` du dépôt).

## Voix off

> Aujourd'hui, je vais te montrer comment j'ai créé une IA qui transforme mes réunions en tâches.
>
> Parce que les réunions, c'est bien… Mais combien de fois on sort d'une réunion avec plein d'idées, des décisions… et personne ne sait vraiment qui doit faire quoi ?
>
> Alors, j'ai développé RapidoMeet. J'enregistre la réunion, ou j'importe l'audio. La conversation est transcrite avec Whisper.
>
> Ensuite, Gemini en tire un résumé, les décisions, et les tâches, avec leur responsable, leur échéance… et la phrase exacte qui les a fait naître.
>
> Imagine : on décide de lancer une nouvelle extension FoodEatUp. Préparer une démo, créer une campagne, contacter les clients intéressés.
>
> RapidoMeet range les tâches dans son tableau de suivi. Il peut préparer les fiches prospects pour RapidoCRM et les contenus pour RapidoCMS… mais chaque écriture attend ma validation.
>
> Pour RapidoRH, il sait déjà lire les projets. Y créer les tâches directement, c'est la prochaine étape.
>
> Et je reste honnête : le projet est livré à quatre-vingt-trois pour cent. Je termine la sécurité avant de l'ouvrir à mes clients.
>
> Avant, je terminais mes réunions avec une liste de choses à faire. Maintenant, chaque réunion peut devenir un plan d'action.
>
> Et toi, combien de temps tu perds à faire tes comptes rendus de réunion ?

## Changements par rapport à ton script

- « préparer automatiquement les actions » est précisé : les tâches vont dans le tableau de RapidoMeet (`db_save_task`). Les écritures RapidoCRM et RapidoCMS demandent une validation (`router.ts`).
- « je peux retrouver le travail à faire dans RapidoRH » devient « il sait déjà lire les projets ; y créer les tâches, c'est la prochaine étape ». Le code ne prévoit que `rh_list_*` et `rh_get_*`.
- Ajout de l'état réel : 83 % du backlog livré, la sécurité est en cours.

La réunion de la vidéo est **fictive** (participants A et B) : aucune réunion réelle n'a été traitée.
