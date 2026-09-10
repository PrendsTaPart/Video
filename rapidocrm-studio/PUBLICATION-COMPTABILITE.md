# Module Comptabilité — état de publication

Domaine servi par l'Académie : **`tutoriel.rapido-crm.com`**.
`academie.rapidosoftware.com` et `tutoriel.rapidocrm.com` n'ont aucun
enregistrement DNS ; le second est pourtant ce que `creer_tutoriel` et
`publier_tutoriel` renvoient dans leur champ `url`. Correction à faire côté
serveur. Les descriptions YouTube et les `publication.json` portent désormais
le domaine qui répond.

## En ligne

| # | Tutoriel | YouTube | Durée | Page |
|---|----------|---------|-------|------|
| 1 | Créer et modifier une facture | HSQazBmzAS4 | 88 s | 05-creer-modifier-une-facture |
| 3 | Changer le statut d'une facture | _kcUjdX4dxs | 61 s | 05-gestion-des-statuts-d-une-facture |
| 4 | Renseigner le mode de paiement | FYSMeqjGEwk | 60 s | 05-mode-de-paiement-des-factures |
| 5 | Retrouver une facture | Dm13SaU-lsg | 73 s | 05-historique-des-factures |
| 8 | Mode de paiement d'un devis | TRHFe2fP7sI | 57 s | 05-mode-de-paiement-des-devis |

## Envois YouTube planifiés

Le quota YouTube est de 10 000 unités par jour, un envoi en coûte ~1 600 :
cinq envois par jour au plus. Le quota du 5 septembre était épuisé après V08,
les cinq derniers tutoriels sont donc planifiés en mode `upload_at_time` sur
la chaîne RapidoCRM (`UCXyptH13bJF7AVr2TZJWA-Q`).

| # | Tutoriel | Envoi prévu (Paris) | Planification |
|---|----------|---------------------|---------------|
| 9 | Signer un devis à l'écran | 06/09 10:00 | 3e46c764-4cab-4a9f-a8ed-04182d9a9cd6 |
| 10 | Convertir un devis en facture | 06/09 14:00 | 0295134c-1d0e-4f90-84ed-b5432c9cad44 |
| 11 | Créer un template SMS | 07/09 10:00 | 6bac78eb-e2cc-4ba6-996e-01af3442a9b2 |
| 12 | Retrouver un devis dans l'historique | 07/09 14:00 | 58c1f927-9dfe-44d7-8250-a7500bf55bcf |
| 14 | Suivre ses dépenses | 08/09 10:00 | d5b71d35-7c1e-4ac1-b17d-d318d395fab7 |

Médias : les vingt-quatre fichiers (16:9, 9:16 et leurs deux vignettes) sont
déjà déposés dans la bibliothèque RapidoCMS, et `publier:cms` est passé pour
les six. Il ne manque à V09–V14 que l'URL YouTube.

## Ce qui reste, une fois chaque envoi effectué

1. Écrire `youtube.publish_video.publication.reponse.json` avec le
   `video_id` de l'envoi.
2. `npm run publier:youtube` puis `npm run publier:site` pour le tutoriel.
   Une page se remplit entièrement ou pas du tout : `publier-site` refuse de
   publier tant que l'URL YouTube ne répond pas.

## Réservé à Michael

- **Supprimer les posts LinkedIn programmés 669 à 676** : ce sont des doublons
  d'une session parallèle, et ils portent le domaine mort
  `tutoriel.rapidocrm.com`. Garder 677 à 684.
- Les habillages rendus affichent encore `academie.rapidosoftware.com/<slug>`
  à l'écran (ouverture et punchline). Le corriger demande un nouveau rendu de
  toute la série : arbitrage à rendre.
- V06 et V07 : blocs de voix synthétisés depuis du texte brut, à revoir.
- Recouvrement entre `27-creer-un-token` et `26-acheter-un-abonnement`.
