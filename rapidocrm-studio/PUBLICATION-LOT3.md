# Lot Utilisateur V01–V04 et Produits V01–V04 — état au 03/09

Chaîne YouTube : **RapidoCRM** (`UCXyptH13bJF7AVr2TZJWA-Q`).
Page LinkedIn : **RapidoSoftware** (compte RapidoCMS 32, `account_id 101119107`).

| Tutoriel | Durée | Page Académie | YouTube | Short | LinkedIn |
|---|---|---|---|---|---|
| U V01 Ajouter un commercial | 112 s | ✅ en ligne | xiUlRID_ejY | gY2Sx73KnZY | 04/09 07 h |
| U V02 Modifier son mot de passe | 96 s | ✅ en ligne | 4m4qEMgHtd4 | -bnbYA7DE9I | 04/09 16 h |
| U V03 Modifier un objectif | 94 s | ✅ en ligne | yyHOYL0CHJI | Dg3-znnzUYY | 05/09 07 h |
| U V04 Voir un portefeuille | 93 s | ✅ en ligne | xasAVxJNTGc | Gi5uAz6szhM | 05/09 16 h |
| P V01 Ajouter un produit | 111 s | ✅ en ligne | wzw2o5xaCwU | R6TdgkjHq8U | 06/09 07 h |
| P V02 Ajouter une stratégie | 95 s | ✅ en ligne | HJ-kOZO36Zg | 4bT2n15z_RY | 06/09 16 h |
| P V03 Attacher des documents | 84 s | ✅ en ligne | sZKuyYfuWrU | zoBK8JqAqRA | 07/09 07 h |
| P V04 Produit et fidélité | 90 s | ✅ en ligne | QVt4pDOBB2k | TmjySZcVU0E | 07/09 16 h |

Les huit posts LinkedIn portent le montage 9:16 déposé dans la bibliothèque
RapidoCMS. Ils reprennent la cadence du lot précédent — 07 h et 16 h, un
tutoriel par créneau — et prennent la suite du dernier post programmé
(01/09 07 h). Brouillons RapidoCMS `852` à `859`, publications `669` à `676`.

## Pourquoi `configurer_agent_tutoriel` n'écrivait rien

L'appel partait avec `instructions` et `outils_autorises`. Le schéma de
l'Académie nomme ces deux champs **`agent_instructions`** et
**`agent_outils_mcp`**. Les clés envoyées n'étant reconnues par aucune colonne,
la mise à jour ne portait sur rien : le serveur échouait ensuite sur son propre
résultat vide — « Cannot coerce the result to a single JSON object » — et
`updated_at` ne bougeait pas. Ce n'était donc pas une panne serveur, et aucune
tentative supplémentaire n'aurait pu passer.

Les deux noms sont corrigés dans `src/pipeline/publier-site.ts`. Le passage de
révision du 28/08, qui avait aligné `etapes[].texte`, `chapitres[].debut`,
`astuces[].texte`, `cas_usage[].action` / `.resultat` et
`enregistrer_video_avatar`, avait laissé celui-ci de côté.

La correction n'a pas pu être vérifiée contre le serveur : le MCP
« RapidoCMS tutoriels » n'est pas connecté à la session, et la clé
`RAPIDO_ACADEMIE_API_KEY` n'est pas disponible.

## Les quatre appels à passer

Les instructions des quatre pages Produits sont rédigées et déposées, prêtes à
exécuter, dans le protocole du pont MCP :

```
content/Produits/V0*/mcp/rapidocms-tutoriels.configurer_agent_tutoriel.configurer_agent_tutoriel.demande.json
```

Chaque fichier porte `slug`, `agent_instructions` et `agent_outils_mcp`.
Il manque la clé d'API — à ajouter à l'exécution en `cle_api`, ou en en-tête
`X-Academie-Cle`, jamais dans un fichier du dépôt. Déposer ensuite le résultat
brut dans le `.reponse.json` de même nom.

Le texte des instructions sort de `fiche.json` (`a_quoi_ca_sert`, `pour_qui`,
`erreurs_frequentes`) et de `script.json` (les étapes) ; les outils autorisés
sont les `fiche.outils_mcp[].nom`, tous en lecture seule.

## Points ouverts, à arbitrer par Michael

- Les quatre blocs de voix de Configuration V06 et V07 synthétisés depuis le
  texte brut au lieu de `pourLaVoix`, sigle « CRM » non développé. Les reprendre
  suppose de refaire rendu et publication.
- Le recouvrement entre `27-creer-un-token` / V13 et `26-acheter-un-abonnement`
  / V11 — produire à part, ou rattacher aux tutoriels existants.
- Module Comptabilité : `content/Comptabilite/V01..V04` ont analyse, fiche et
  script (122 s, 91 s, 90 s, 118 s). Les scripts attendent la validation au
  premier point d'arrêt ; ni voix ni rendu avant.
