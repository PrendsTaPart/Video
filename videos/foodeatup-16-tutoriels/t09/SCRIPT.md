# Relier Uber Eats & Deliveroo via HubRise

**Fiche** `relier-uber-eats-et-deliveroo` · module `hubrise-livraisons` · identifiant de série `t09`

> Faire arriver les commandes des plateformes dans la même liste.

⚠️ **Film sans rush.** Ce tutoriel n'a pas de capture d'écran : il est en motion
design assumé. Aucun plan ne prétend montrer le produit — une planche
schématique dit « voici l'étape et ce qui compte », là où une fausse interface
prétendrait « voici l'écran ». Le jour où le rush existe, le film est remplacé ;
ce script, lui, reste.

## À quoi ça sert (texte de la fiche)

Chaque plateforme se relie une fois, à HubRise, pas à FoodEatUp. Les commandes descendent ensuite dans la liste unique — mêmes statuts, même cuisine, même comptabilité que les commandes sur place.

## Marche à suivre (texte de la fiche)

1. Reliez chaque plateforme depuis votre compte HubRise, l'une après l'autre.
2. Rattachez-les à la même location que celle choisie pour FoodEatUp.
3. Attendez une première commande réelle : c'est le seul test qui vaille.
4. Vérifiez qu'elle apparaît bien dans vos commandes, avec son canal d'origine.

## Astuce du chef

Ne testez pas avec une commande fictive passée depuis votre propre téléphone hors zone de livraison : elle est refusée par la plateforme avant d'atteindre HubRise, et vous conclurez à tort que le lien ne marche pas.

## Voix off

Adam - Instructor (`TGAegA0zNRi8I6nUdq3i`), `eleven_multilingual_v2`, français.

| # | Texte |
|---|---|
| N0 | Chaque plateforme se relie une fois, à HubRise, pas à FoodEatUp. |
| N1 | Reliez-les l'une après l'autre depuis votre compte HubRise. |
| N2 | Rattachez-les à la même location que celle choisie pour FoodEatUp. |
| N3 | Puis attendez une première commande réelle. C'est le seul test qui vaille. |
| N4 | Vérifiez qu'elle apparaît dans vos commandes, avec son canal d'origine. |
| CTA | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! |

## Frise des jalons

**par plateforme** → **même location** → **commande réelle** → **canal**

## Outils MCP correspondants

- `get_hubrise_status`
- `list_orders`

## Prompt Claude

> Vérifie l'état HubRise de l'établissement [ID], puis liste les commandes du jour pour voir celles qui viennent des plateformes.
