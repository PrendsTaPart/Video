# Centraliser les commandes — flux livraison

**Fiche** `centraliser-les-commandes-livraison` · module `hubrise-livraisons` · identifiant de série `t11`

> Tenir un seul flux, quelle que soit la provenance.

⚠️ **Film sans rush.** Ce tutoriel n'a pas de capture d'écran : il est en motion
design assumé. Aucun plan ne prétend montrer le produit — une planche
schématique dit « voici l'étape et ce qui compte », là où une fausse interface
prétendrait « voici l'écran ». Le jour où le rush existe, le film est remplacé ;
ce script, lui, reste.

## À quoi ça sert (texte de la fiche)

Une commande de plateforme n'est pas une commande à part : elle entre dans la même liste, avec les mêmes statuts, et part en cuisine par le même chemin. Ce qui change, c'est son canal — et c'est la seule chose à savoir.

## Marche à suivre (texte de la fiche)

1. Ouvrez vos commandes : toutes y sont, tous canaux confondus.
2. Filtrez par canal pour isoler la livraison — sur place, vitrine, téléphone, agent vocal, plateformes.
3. Suivez le statut comme pour n'importe quelle commande : en attente, confirmée, en préparation, prête, livrée.
4. Surveillez les commandes du jour restées en attente côté plateformes : ce sont celles qui n'ont pas franchi le connecteur.

## Astuce du chef

Ne traitez pas les commandes de livraison sur un écran séparé. Un service qui regarde deux listes en oublie une, toujours la même, toujours au coup de feu.

## Voix off

Adam - Instructor (`TGAegA0zNRi8I6nUdq3i`), `eleven_multilingual_v2`, français.

| # | Texte |
|---|---|
| N0 | Une commande de plateforme n'est pas une commande à part. Même liste, mêmes statuts, même cuisine. |
| N1 | Ouvrez vos commandes : toutes y sont, tous canaux confondus. |
| N2 | Filtrez par canal pour isoler la livraison. |
| N3 | Suivez le statut comme pour n'importe quelle commande : en attente, confirmée, en préparation, prête, livrée. |
| N4 | Et surveillez celles restées en attente côté plateformes : ce sont celles qui n'ont pas franchi le connecteur. |
| CTA | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! |

## Frise des jalons

**une liste** → **filtre canal** → **les statuts** → **en attente**

## Outils MCP correspondants

- `list_orders`
- `get_hubrise_status`
- `update_order_status`

## Prompt Claude

> Liste les commandes du jour de l'établissement [ID], canal par canal, et signale celles encore en attente côté plateformes.
