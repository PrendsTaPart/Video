# Lot Configuration V06–V13 — publication terminée

Chaîne YouTube : **RapidoCRM** (`UCXyptH13bJF7AVr2TZJWA-Q`).
Page LinkedIn : **RapidoSoftware** (compte RapidoCMS 32, `account_id 101119107`).

| Tutoriel | Durée | Bibliothèque | Page Académie | YouTube | Short | LinkedIn |
|---|---|---|---|---|---|---|
| V06 Configurer son IMAP | 80 s | ✅ | ✅ en ligne | HmVdbFSmvT0 | l3vHyg84IaY | 29/08 16 h |
| V07 Configurer son IA | 82 s | ✅ | ✅ en ligne | xtGIQyk1-o4 | sDiZj1N3gQk | 30/08 07 h |
| V09 Configurer Stripe | 80 s | ✅ | ✅ en ligne | OOEbjYD5KaY | q31o6n7iJO0 | 30/08 16 h |
| V10 Configurer son IBAN | 86 s | ✅ | ✅ en ligne | 9oOiLfzPMIg | MBg02iH3BvM | 31/08 07 h |
| V11 Choisir son abonnement | 106 s | ✅ | ✅ en ligne | QWs_RxI9cgE | b4epBUpjFus | 31/08 16 h |
| V13 Récupérer sa clé api | 99 s | ✅ | ✅ en ligne | pmxUvYPaTig | Rd0lnCK8510 | 01/09 07 h |

Les six pages sont complètes : `tutoriels_incomplets` n'en renvoie aucune.
Les douze vidéos sont publiques. Les masters ont été déposés depuis leur URL
raw GitHub, chaque service les téléchargeant lui-même.

## Deux défauts corrigés en cours de lot

**Le contrôle de floutage de la QA ne regardait pas la zone sensible.**
`sharp.stats()` lit l'image d'entrée et ignore les opérations en attente :
l'`extract()` du rectangle n'était jamais appliqué, et le contrôle mesurait
l'écart-type de la frame entière. Les quatre tutoriels validés avant la
correction l'avaient donc été par un contrôle qui ne contrôlait rien.
L'écart-type était de toute façon la mauvaise mesure : il capte le contraste,
pas ce qui reste lisible. Remplacé par l'énergie haute fréquence, seuil 4,
calibré 14,5–15,8 sur l'enregistrement brut contre 0,6–1,5 sur les segments
floutés, avec un test négatif. Tous les tutoriels du lot ont été repassés.

**Les blocs de voix contenant un sigle partaient en texte brut.** Ils
auraient dû passer par `pourLaVoix`, qui développe « CRM » en « C.R.M. ».
Corrigé sur V11. Restent trois blocs de V06 et un de V07, déjà publiés : les
reprendre suppose de refaire rendu et publication, non fait.

## Points ouverts

Deux fiches d'autres modules recoupent ce lot et restent à produire :
`27-creer-un-token` et `26-acheter-un-abonnement`. À arbitrer — soit les
produire à part, soit les rattacher aux tutoriels de Configuration existants.
