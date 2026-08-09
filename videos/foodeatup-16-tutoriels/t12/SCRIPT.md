# Gérer une commande en direct sur le KDS

**Fiche** `gerer-une-commande-en-direct-kds` · module `kds-cuisine` · identifiant de série `t12`

> Faire avancer un ticket plat par plat, pendant le service.

⚠️ **Film sans rush.** Ce tutoriel n'a pas de capture d'écran : il est en motion
design assumé. Aucun plan ne prétend montrer le produit — une planche
schématique dit « voici l'étape et ce qui compte », là où une fausse interface
prétendrait « voici l'écran ». Le jour où le rush existe, le film est remplacé ;
ce script, lui, reste.

## À quoi ça sert (texte de la fiche)

Le KDS ne suit pas des commandes, il suit des plats. C'est ce qui permet à une entrée de partir pendant qu'un plat chaud cuit encore, sans que le ticket entier attende le plus lent.

## Marche à suivre (texte de la fiche)

1. Le ticket arrive au poste concerné dès que la commande est confirmée.
2. Faites avancer chaque plat séparément : à faire, en cours, prêt, servi.
3. Passez un plat en « en cours » quand vous le commencez, pas quand vous le voyez : c'est ce qui rend le compteur d'attente juste.
4. « Prêt » l'envoie au pass. Le ticket ne disparaît qu'une fois tous ses plats servis.
5. La charge des postes se met à jour à chaque changement : elle dit où ça bloque, en direct.

## Astuce du chef

Le passage en « en cours » est le seul geste que personne ne fait spontanément — et c'est le seul qui rende le temps d'attente crédible. Sans lui, tout paraît prêt d'un coup.

## Voix off

Adam - Instructor (`TGAegA0zNRi8I6nUdq3i`), `eleven_multilingual_v2`, français.

| # | Texte |
|---|---|
| N0 | Le KDS ne suit pas des commandes, il suit des plats. L'entrée part pendant que le chaud cuit. |
| N1 | Le ticket arrive au poste dès que la commande est confirmée. |
| N2 | Faites avancer chaque plat séparément : à faire, en cours, prêt, servi. |
| N3 | Passez un plat en « en cours » quand vous le commencez, pas quand vous le voyez. C'est ce qui rend le compteur d'attente juste. |
| N4 | « Prêt » l'envoie au pass. Le ticket ne disparaît qu'une fois tous ses plats servis. |
| N5 | Et la charge des postes se met à jour à chaque changement : elle dit où ça bloque, en direct. |
| CTA | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! |

## Frise des jalons

**par plat** → **quatre statuts** → **en cours** → **charge des postes**

## Outils MCP correspondants

- `update_kds_item_status`
- `get_station_load`

## Prompt Claude

> Passe le plat [ID ITEM] de l'établissement [ID] en statut [pending / in_progress / ready / served], puis donne-moi la charge des postes.
