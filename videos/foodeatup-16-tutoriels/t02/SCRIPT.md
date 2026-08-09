# Ouvrir son fond de caisse en début de service

**Fiche** `ouvrir-son-fond-de-caisse` · module `caisse-pos` · identifiant de série `t02`

> Ouvrir la session avant le premier client.

⚠️ **Film sans rush.** Ce tutoriel n'a pas de capture d'écran : il est en motion
design assumé. Aucun plan ne prétend montrer le produit — une planche
schématique dit « voici l'étape et ce qui compte », là où une fausse interface
prétendrait « voici l'écran ». Le jour où le rush existe, le film est remplacé ;
ce script, lui, reste.

## À quoi ça sert (texte de la fiche)

Tant que la session n'est pas ouverte, aucun encaissement ne se rattache à personne ni à un fond de départ. L'écart de fin de service devient alors inexplicable — non pas grand, mais impossible à attribuer.

## Marche à suivre (texte de la fiche)

1. Choisissez l'opérateur : seul un employé disposant de la permission caisse peut ouvrir une session.
2. Comptez le fond de caisse réel et saisissez-le, au centime. C'est la référence de tout l'écart de ce soir.
3. Validez : la session s'ouvre, et chaque encaissement s'y rattache automatiquement.
4. Une seule session à la fois par établissement : si elle est déjà ouverte, c'est la précédente qu'il faut clôturer.

## Astuce du chef

Saisissez le fond compté, pas le fond théorique. Reporter le montant d'hier parce que « ça n'a pas bougé » revient à effacer l'écart d'hier dans celui d'aujourd'hui.

## Voix off

Adam - Instructor (`TGAegA0zNRi8I6nUdq3i`), `eleven_multilingual_v2`, français.

| # | Texte |
|---|---|
| N0 | Le fond de caisse s'ouvre avant le premier client. Sans session ouverte, aucun encaissement ne se rattache à personne. |
| N1 | Choisissez l'opérateur : seul un employé avec la permission caisse peut ouvrir une session. |
| N2 | Comptez le fond réel, et saisissez-le au centime. C'est la référence de tout l'écart de ce soir. |
| N3 | Validez : la session s'ouvre, et chaque encaissement s'y rattache tout seul. |
| N4 | Une seule session à la fois. Si elle est déjà ouverte, c'est la précédente qu'il faut clôturer. |
| N5 | Depuis Claude, l'ouverture tient en une phrase : l'établissement, l'opérateur, le montant du fond. |
| CTA | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! |

## Frise des jalons

**opérateur** → **comptage** → **ouverture** → **une seule**

## Outils MCP correspondants

- `open_pos_session`
- `get_pos_session`

## Prompt Claude

> Ouvre la caisse de l'établissement [ID] avec un fond de [MONTANT] euros, opérateur [ID EMPLOYÉ].
