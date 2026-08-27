# Lot Configuration V06–V13 — état de publication

Chaîne YouTube : **RapidoCRM** (`UCXyptH13bJF7AVr2TZJWA-Q`).

## État

| Tutoriel | Durée | Bibliothèque | Page Académie | LinkedIn | YouTube | Short |
|---|---|---|---|---|---|---|
| V06 Configurer son IMAP | 80 s | ✅ 4 médias | ✅ en ligne | 29/08 16 h | HmVdbFSmvT0 | l3vHyg84IaY |
| V07 Configurer son IA | 82 s | ✅ 4 médias | ✅ en ligne | 30/08 07 h | xtGIQyk1-o4 | sDiZj1N3gQk |
| V09 Configurer Stripe | 80 s | ✅ 4 médias | ✅ en ligne | 30/08 16 h | OOEbjYD5KaY | q31o6n7iJO0 |
| V10 Configurer son IBAN | 86 s | à faire | à faire | à faire | 9oOiLfzPMIg | MBg02iH3BvM |
| V11 Choisir son abonnement | 106 s | à faire | à faire | à faire | QWs_RxI9cgE | b4epBUpjFus |
| V13 Récupérer sa clé api | 99 s | à faire | à faire | à faire | pmxUvYPaTig | Rd0lnCK8510 |

Les douze vidéos sont publiques. Les masters ont été déposés depuis leur URL
raw GitHub, la chaîne les téléchargeant elle-même.

## Ce qu'il reste à faire

### Les six liens YouTube ne sont pas encore sur les pages

`enregistrer_youtube` sur les six slugs — `01-configurer-son-imap`,
`01-configurer-son-ia`, `01-configurer-stripe`, `01-configurer-son-iban`,
`01-choisir-son-abonnement`, `01-recuperer-sa-cle-api`. Bloqué : la clé d'API
de l'Académie n'est plus en mémoire de session. Elle se génère dans
`/admin/parametres`, portée `ecriture`, et ne s'écrit jamais dans le dépôt.

### V10, V11, V13 — publication à faire

1. `npm run publier:cms` — les 4 médias de chaque tutoriel dans la
   bibliothèque RapidoCMS.
2. `creer_tutoriel` puis remplissage complet et `publier_tutoriel`, module
   `01-configuration`. Même clé d'API que ci-dessus.
3. LinkedIn, page RapidoSoftware, montage 9:16, un créneau par tutoriel à la
   suite des trois déjà programmés.

## Fait dans cette session

- Voix des trois tutoriels restants (V10 85 s, V11 105 s, V13 97 s), rendus,
  vignettes et QA verte sur les trois.
- Correction du contrôle de floutage de la QA : `sharp.stats()` ignorait
  l'`extract()`, le contrôle mesurait toute la frame. Métrique remplacée par
  l'énergie haute fréquence, seuil 4, calibré 14,5–15,8 (brut) contre
  0,6–1,5 (flouté). V06, V07, V09 et V10 repassés, toujours verts.
- Blocs de voix contenant « CRM » : ils avaient été envoyés en texte brut au
  lieu du texte de `pourLaVoix`. Corrigés sur V11 ; restent 3 blocs de V06 et
  1 de V07, déjà publiés, non repris.
