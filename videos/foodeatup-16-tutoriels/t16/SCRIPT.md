# Retrouver la commande derrière une facture

**Fiche** `retrouver-toutes-mes-commandes` · module `comptabilite` · identifiant de série `t16`

> Rapprocher une écriture de la commande qui l'a produite.

⚠️ **Film sans rush.** Ce tutoriel n'a pas de capture d'écran : il est en motion
design assumé. Aucun plan ne prétend montrer le produit — une planche
schématique dit « voici l'étape et ce qui compte », là où une fausse interface
prétendrait « voici l'écran ». Le jour où le rush existe, le film est remplacé ;
ce script, lui, reste.

## À quoi ça sert (texte de la fiche)

Chaque commande crée sa facture et son devis. Le rapprochement compte au moment du contrôle : retrouver, derrière une ligne comptable, ce qui a été servi, à qui, par quel canal — et vérifier que le statut des deux concorde.

## Marche à suivre (texte de la fiche)

1. Partez de la facture, et remontez à la commande qui l'a générée.
2. Filtrez par canal, par statut ou par date pour retrouver une commande dont vous n'avez que l'à-peu-près.
3. Ouvrez le détail : les articles, le client, le total, et les liens vers la facture et le devis.
4. Vérifiez la concordance des statuts : changer celui de la commande se répercute sur la facture et le devis.
5. Une commande annulée dont la facture reste ouverte est l'écart que le contrôle trouvera à votre place.

## Astuce du chef

Rapprochez au fil de l'eau, pas en fin de mois. Un écart de statut vieux de trois semaines demande de se souvenir du service — ce que personne ne fait.

## Voix off

Adam - Instructor (`TGAegA0zNRi8I6nUdq3i`), `eleven_multilingual_v2`, français.

| # | Texte |
|---|---|
| N0 | Chaque commande crée sa facture et son devis. Le rapprochement, lui, compte au moment du contrôle. |
| N1 | Partez de la facture, et remontez à la commande qui l'a générée. |
| N2 | Filtrez par canal, par statut ou par date quand vous n'avez que l'à-peu-près. |
| N3 | Ouvrez le détail : les articles, le client, le total, et les liens vers la facture et le devis. |
| N4 | Vérifiez la concordance des statuts : changer celui de la commande se répercute sur les deux. |
| N5 | Une commande annulée dont la facture reste ouverte est l'écart que le contrôle trouvera à votre place. |
| CTA | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! |

## Frise des jalons

**depuis la facture** → **les filtres** → **le détail** → **concordance**

## Outils MCP correspondants

- `list_orders`
- `get_order`
- `get_invoice`
- `update_order_status`

## Prompt Claude

> Retrouve la commande liée à la facture [NUMÉRO] de l'établissement [ID], et dis-moi si le statut de la commande et celui de la facture concordent.
