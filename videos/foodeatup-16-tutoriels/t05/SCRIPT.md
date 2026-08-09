# Séparer une addition — multi-paiement

**Fiche** `separer-une-addition` · module `caisse-pos` · identifiant de série `t05`

> Faire payer une même note à plusieurs, sans recompter.

⚠️ **Film sans rush.** Ce tutoriel n'a pas de capture d'écran : il est en motion
design assumé. Aucun plan ne prétend montrer le produit — une planche
schématique dit « voici l'étape et ce qui compte », là où une fausse interface
prétendrait « voici l'écran ». Le jour où le rush existe, le film est remplacé ;
ce script, lui, reste.

## À quoi ça sert (texte de la fiche)

Une table de six qui paie en trois fois, c'est trois paiements sur une seule note — pas trois notes. La différence compte : une seule commande part en cuisine, une seule facture sort, et le reste dû se recalcule tout seul.

## Marche à suivre (texte de la fiche)

1. Gardez une seule note : c'est elle qui porte les plats et le total.
2. Encaissez un premier paiement partiel — le reste dû se recalcule immédiatement.
3. Changez de moyen entre deux paiements : carte pour l'un, espèces pour l'autre, titre-restaurant pour un troisième.
4. Répétez jusqu'à zéro : la note se solde à l'instant où le reste dû est couvert.
5. Relisez la liste des paiements : chaque part, son moyen, son rendu.

## Astuce du chef

Ne créez jamais plusieurs notes pour partager une addition. Vous doubleriez la commande en cuisine et vous perdriez le total réel de la table.

## Voix off

Adam - Instructor (`TGAegA0zNRi8I6nUdq3i`), `eleven_multilingual_v2`, français.

| # | Texte |
|---|---|
| N0 | Une table de six qui paie en trois fois, c'est trois paiements sur une seule note — pas trois notes. |
| N1 | Gardez une seule note : c'est elle qui porte les plats et le total. |
| N2 | Encaissez un premier paiement partiel. Le reste dû se recalcule immédiatement. |
| N3 | Changez de moyen entre deux paiements : carte pour l'un, espèces pour l'autre. |
| N4 | Répétez jusqu'à zéro. La note se solde à l'instant où le reste dû est couvert. |
| N5 | Et relisez la liste des paiements : chaque part, son moyen, son rendu. |
| CTA | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! |

## Frise des jalons

**une note** → **paiement partiel** → **modes** → **soldée**

## Outils MCP correspondants

- `record_pos_payment`
- `list_pos_payments`

## Prompt Claude

> Montre-moi les paiements de la commande [ID] pour l'établissement [ID] : les modes, les montants, le rendu et le reste dû.
