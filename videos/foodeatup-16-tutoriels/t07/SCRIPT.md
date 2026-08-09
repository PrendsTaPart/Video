# Suivre les écarts de caisse — historique

**Fiche** `suivre-les-ecarts-de-caisse` · module `caisse-pos` · identifiant de série `t07`

> Lire les écarts sur la durée plutôt qu'au jour le jour.

⚠️ **Film sans rush.** Ce tutoriel n'a pas de capture d'écran : il est en motion
design assumé. Aucun plan ne prétend montrer le produit — une planche
schématique dit « voici l'étape et ce qui compte », là où une fausse interface
prétendrait « voici l'écran ». Le jour où le rush existe, le film est remplacé ;
ce script, lui, reste.

## À quoi ça sert (texte de la fiche)

Un écart isolé ne dit rien : on rend mal la monnaie, ça arrive. C'est la répétition qui parle — toujours le même opérateur, toujours le même service, toujours le même sens.

## Marche à suivre (texte de la fiche)

1. Ouvrez l'historique des sessions clôturées : chacune porte son rapport Z.
2. Comparez l'écart par session, pas seulement son montant : son signe compte autant.
3. Ventilez par opérateur : un écart qui suit une personne n'a pas la même cause qu'un écart qui suit un service.
4. Ventilez par moyen de paiement : un écart qui ne touche que les espèces désigne le rendu de monnaie.

## Astuce du chef

Un écart toujours négatif du même montant n'est presque jamais un vol : c'est un fond de caisse mal saisi à l'ouverture, qui se reproduit chaque jour.

## Voix off

Adam - Instructor (`TGAegA0zNRi8I6nUdq3i`), `eleven_multilingual_v2`, français.

| # | Texte |
|---|---|
| N0 | Un écart isolé ne dit rien. C'est la répétition qui parle. |
| N1 | Ouvrez l'historique des sessions clôturées : chacune porte son rapport Z. |
| N2 | Comparez les écarts, et regardez leur signe autant que leur montant. |
| N3 | Ventilez par opérateur : un écart qui suit une personne n'a pas la même cause qu'un écart qui suit un service. |
| N4 | Puis par moyen de paiement : un écart qui ne touche que les espèces désigne le rendu de monnaie. |
| CTA | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! |

## Frise des jalons

**historique** → **signe** → **opérateur** → **moyen**

## Outils MCP correspondants

- `get_pos_report`

## Prompt Claude

> Donne-moi le rapport Z de la session [ID SESSION] de l'établissement [ID] : chiffre d'affaires, ticket moyen, ventilation par mode et par opérateur, TVA, remises.
