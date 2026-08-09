# Connecter son HubRise à FoodEatUp

**Fiche** `connecter-son-hubrise` · module `hubrise-livraisons` · identifiant de série `t08`

> Brancher le connecteur qui relie les plateformes à la carte.

⚠️ **Film sans rush.** Ce tutoriel n'a pas de capture d'écran : il est en motion
design assumé. Aucun plan ne prétend montrer le produit — une planche
schématique dit « voici l'étape et ce qui compte », là où une fausse interface
prétendrait « voici l'écran ». Le jour où le rush existe, le film est remplacé ;
ce script, lui, reste.

## À quoi ça sert (texte de la fiche)

HubRise est le point de passage : c'est lui qui parle aux plateformes de livraison, et FoodEatUp qui parle à HubRise. Une seule connexion à tenir, au lieu d'une par plateforme.

## Marche à suivre (texte de la fiche)

1. Créez ou reliez votre compte HubRise depuis FoodEatUp.
2. Choisissez la location : c'est le point de vente précis, pas l'enseigne. Une erreur ici envoie les commandes au mauvais établissement.
3. Autorisez le connecteur, puis vérifiez son état : connecté, location reconnue.
4. Contrôlez enfin les commandes du jour restées en attente côté plateformes — elles disent si le flux passe vraiment.

## Astuce du chef

Vérifiez la location avant tout le reste. Une enseigne à deux adresses a deux locations, et rien dans l'interface ne vous dira que vous avez choisi la mauvaise.

## Voix off

Adam - Instructor (`TGAegA0zNRi8I6nUdq3i`), `eleven_multilingual_v2`, français.

| # | Texte |
|---|---|
| N0 | HubRise est le point de passage : il parle aux plateformes, et FoodEatUp lui parle. Une seule connexion à tenir. |
| N1 | Créez ou reliez votre compte HubRise depuis FoodEatUp. |
| N2 | Choisissez la location : le point de vente précis, pas l'enseigne. Une erreur ici envoie les commandes au mauvais établissement. |
| N3 | Autorisez le connecteur, puis vérifiez son état : connecté, location reconnue. |
| N4 | Et contrôlez les commandes du jour restées en attente côté plateformes. C'est elles qui disent si le flux passe. |
| CTA | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! |

## Frise des jalons

**compte** → **location** → **autorisation** → **contrôle**

## Outils MCP correspondants

- `get_hubrise_status`

## Prompt Claude

> Donne-moi l'état du connecteur HubRise de l'établissement [ID] : connexion, location, plats bloqués au push, commandes du jour en attente côté plateformes.
