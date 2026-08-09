# Clôturer sa caisse — le Z de caisse

**Fiche** `cloturer-sa-caisse` · module `caisse-pos` · identifiant de série `t06`

> Fermer la journée et figer les chiffres.

⚠️ **Film sans rush.** Ce tutoriel n'a pas de capture d'écran : il est en motion
design assumé. Aucun plan ne prétend montrer le produit — une planche
schématique dit « voici l'étape et ce qui compte », là où une fausse interface
prétendrait « voici l'écran ». Le jour où le rush existe, le film est remplacé ;
ce script, lui, reste.

## À quoi ça sert (texte de la fiche)

La clôture n'est pas une formalité de fin de service : c'est elle qui fige le chiffre d'affaires du jour, sa ventilation de TVA et son écart. Une session qu'on oublie de fermer emporte le service du lendemain avec elle.

## Marche à suivre (texte de la fiche)

1. Lisez le rapport X avant de compter : c'est l'état de la session en cours, chiffre d'affaires, modes de paiement, TVA, remises.
2. Comptez les espèces en caisse et saisissez le montant compté.
3. Confirmez : l'écart se calcule entre le théorique et le compté.
4. Le rapport Z est alors figé. Il ne se recalcule plus, même si une correction arrive après.

## Astuce du chef

Lisez toujours le X avant de compter, jamais après. Connaître le montant théorique avant de compter, c'est se donner une chance de compter deux fois quand ça ne tombe pas juste.

## Voix off

Adam - Instructor (`TGAegA0zNRi8I6nUdq3i`), `eleven_multilingual_v2`, français.

| # | Texte |
|---|---|
| N0 | La clôture fige le chiffre du jour, sa TVA et son écart. Une session oubliée emporte le service du lendemain. |
| N1 | Lisez le rapport X avant de compter : la session en cours, son chiffre, ses modes de paiement, sa TVA, ses remises. |
| N2 | Comptez les espèces, et saisissez le montant compté. |
| N3 | Confirmez : l'écart se calcule entre le théorique et le compté. |
| N4 | Le rapport Z est figé. Il ne se recalcule plus, même si une correction arrive après. |
| CTA | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! |

## Frise des jalons

**rapport X** → **comptage** → **écart** → **Z figé**

## Outils MCP correspondants

- `get_pos_report`
- `close_pos_session`

## Prompt Claude

> Résume-moi le rapport X de la caisse de l'établissement [ID], puis clôture la session avec un comptage espèces de [MONTANT] euros, opérateur [ID EMPLOYÉ].
