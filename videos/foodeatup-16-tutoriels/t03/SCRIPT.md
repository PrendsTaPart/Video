# Encaisser une commande — comptoir & table

**Fiche** `encaisser-une-commande` · module `caisse-pos` · identifiant de série `t03`

> Solder une note, quel que soit le moyen de paiement.

⚠️ **Film sans rush.** Ce tutoriel n'a pas de capture d'écran : il est en motion
design assumé. Aucun plan ne prétend montrer le produit — une planche
schématique dit « voici l'étape et ce qui compte », là où une fausse interface
prétendrait « voici l'écran ». Le jour où le rush existe, le film est remplacé ;
ce script, lui, reste.

## À quoi ça sert (texte de la fiche)

Encaisser, ce n'est pas enregistrer un total : c'est faire tomber le reste dû à zéro. Tant qu'il ne l'est pas, la note reste ouverte — et c'est cette règle qui rend possibles les paiements partagés et les acomptes.

## Marche à suivre (texte de la fiche)

1. Ouvrez la note, au comptoir ou à la table : le reste dû s'affiche.
2. Choisissez le moyen : espèces, carte, titre-restaurant ou chèque.
3. En espèces, saisissez le montant remis — le rendu se calcule tout seul.
4. Le titre-restaurant ne rend jamais la monnaie : le surplus est perdu pour le client, jamais rendu en pièces.
5. La note se solde d'elle-même quand le reste dû atteint zéro.

## Astuce du chef

Saisissez toujours le montant réellement remis, même quand il est rond. C'est ce chiffre qui alimente le rendu, et c'est lui qu'on relit quand un écart apparaît le soir.

## Voix off

Adam - Instructor (`TGAegA0zNRi8I6nUdq3i`), `eleven_multilingual_v2`, français.

| # | Texte |
|---|---|
| N0 | Encaisser, ce n'est pas enregistrer un total. C'est faire tomber le reste dû à zéro. |
| N1 | Ouvrez la note, au comptoir ou à la table : le reste dû s'affiche. |
| N2 | Choisissez le moyen : espèces, carte, titre-restaurant ou chèque. |
| N3 | En espèces, saisissez le montant remis. Le rendu se calcule tout seul. |
| N4 | Attention au titre-restaurant : il ne rend jamais la monnaie. Le surplus est perdu, jamais rendu en pièces. |
| N5 | Et la note se solde d'elle-même dès que le reste dû atteint zéro. |
| CTA | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! |

## Frise des jalons

**la note** → **le mode** → **le rendu** → **soldée**

## Outils MCP correspondants

- `record_pos_payment`
- `list_pos_payments`

## Prompt Claude

> Encaisse la commande [ID] de l'établissement [ID] : [MONTANT] euros en [especes / carte / titre_restaurant / cheque], opérateur [ID EMPLOYÉ]. Pour des espèces, indique aussi le montant remis par le client.
