# Synchroniser sa caisse tierce via HubRise

**Fiche** `synchroniser-sa-caisse-tierce` · module `hubrise-livraisons` · identifiant de série `t10`

> Faire correspondre les plats de part et d'autre.

⚠️ **Film sans rush.** Ce tutoriel n'a pas de capture d'écran : il est en motion
design assumé. Aucun plan ne prétend montrer le produit — une planche
schématique dit « voici l'étape et ce qui compte », là où une fausse interface
prétendrait « voici l'écran ». Le jour où le rush existe, le film est remplacé ;
ce script, lui, reste.

## À quoi ça sert (texte de la fiche)

La synchronisation ne tient qu'à une chose : la référence de chaque plat. Sans elle, le plat existe des deux côtés sans que rien ne les relie, et il est purement et simplement bloqué au push.

## Marche à suivre (texte de la fiche)

1. Renseignez la référence — le sku_ref — de chaque plat de votre carte.
2. Reprenez exactement la référence de la caisse tierce : une majuscule d'écart suffit à casser le lien.
3. Relancez la synchronisation.
4. Relisez l'état du connecteur : il liste nommément les plats sans référence, donc bloqués.

## Astuce du chef

Traitez la liste des plats sans référence comme une liste de courses : tant qu'elle n'est pas vide, la carte est incomplète chez le client, et personne ne vous le signalera.

## Voix off

Adam - Instructor (`TGAegA0zNRi8I6nUdq3i`), `eleven_multilingual_v2`, français.

| # | Texte |
|---|---|
| N0 | La synchronisation ne tient qu'à une chose : la référence de chaque plat. |
| N1 | Renseignez le sku_ref de chaque plat de votre carte. |
| N2 | Reprenez exactement la référence de la caisse tierce. Une majuscule d'écart suffit à casser le lien. |
| N3 | Relancez la synchronisation. |
| N4 | Et relisez l'état du connecteur : il liste nommément les plats sans référence, donc bloqués au push. |
| CTA | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! |

## Frise des jalons

**sku_ref** → **à la lettre** → **synchro** → **plats bloqués**

## Outils MCP correspondants

- `get_hubrise_status`
- `list_dishes`

## Prompt Claude

> Liste les plats de l'établissement [ID] qui n'ont pas de sku_ref et sont donc bloqués au push HubRise.
