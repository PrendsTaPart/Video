# Configurer sa caisse POS — TPE & ticket

**Fiche** `configurer-sa-caisse-pos` · module `caisse-pos` · identifiant de série `t01`

> Préparer la caisse avant le premier encaissement.

⚠️ **Film sans rush.** Ce tutoriel n'a pas de capture d'écran : il est en motion
design assumé. Aucun plan ne prétend montrer le produit — une planche
schématique dit « voici l'étape et ce qui compte », là où une fausse interface
prétendrait « voici l'écran ». Le jour où le rush existe, le film est remplacé ;
ce script, lui, reste.

## À quoi ça sert (texte de la fiche)

Une caisse mal déclarée se voit au premier service : le TPE ne répond pas, le ticket sort sans mentions légales, et personne ne sait quel terminal a encaissé quoi. Ce réglage se fait une fois, et il porte tout le reste.

## Marche à suivre (texte de la fiche)

1. Déclarez vos îlots d'encaissement : un comptoir, une terrasse, un bar sont trois points de vente distincts.
2. Appairez chaque terminal Smile&Pay à son îlot, et désignez celui qui sert par défaut.
3. Renseignez l'en-tête du ticket : raison sociale, adresse, numéro de TVA. Ce sont les mentions obligatoires.
4. Testez un encaissement à un euro, puis annulez-le : c'est le seul moyen de vérifier la chaîne complète avant le service.

## Astuce du chef

Nommez vos terminaux par leur place réelle — « Comptoir », « Terrasse » — jamais par leur numéro de série. Le jour où un écart apparaît, vous cherchez un endroit, pas un numéro.

## Voix off

Adam - Instructor (`TGAegA0zNRi8I6nUdq3i`), `eleven_multilingual_v2`, français.

| # | Texte |
|---|---|
| N0 | Avant le premier encaissement, la caisse se déclare une fois. Ce réglage porte tout le reste. |
| N1 | Commencez par vos îlots : un comptoir, une terrasse, un bar sont trois points de vente distincts. |
| N2 | Appairez chaque terminal Smile&Pay à son îlot, et désignez celui qui sert par défaut. |
| N3 | Renseignez l'en-tête du ticket : raison sociale, adresse, numéro de TVA. Ce sont les mentions obligatoires. |
| N4 | Puis testez un encaissement à un euro, et annulez-le. C'est le seul moyen de vérifier la chaîne complète avant le service. |
| N5 | Vous pouvez lister vos terminaux depuis Claude : leur îlot, lequel est actif, et quand chacun a servi pour la dernière fois. |
| CTA | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! |

## Frise des jalons

**îlots** → **terminaux** → **ticket** → **test à 1 €**

## Outils MCP correspondants

- `list_payment_terminals`

## Prompt Claude

> Liste mes terminaux de paiement pour l'établissement [ID] : libellé, îlot, lequel est actif par défaut, et la date de dernière utilisation.
