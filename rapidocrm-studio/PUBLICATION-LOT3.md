# Lot Utilisateur V01–V04 et Produits V01–V04 — LinkedIn programmé

Page LinkedIn : **RapidoSoftware** (compte RapidoCMS 32, `account_id 101119107`).
Cadence reprise du lot précédent : deux publications par jour, 07 h et 16 h.

| Tutoriel | Slug de la page | Brouillon | Publication | Créneau |
|---|---|---|---|---|
| Utilisateur V01 Ajouter un commercial | `02-ajouter-modifier-un-commercial` | 860 | 677 | 04/09 07 h |
| Utilisateur V02 Modifier son mot de passe | `02-modifier-mot-de-passe-utilisateur` | 861 | 678 | 04/09 16 h |
| Utilisateur V03 Modifier un objectif | `02-ajouter-modifier-un-objectif` | 862 | 679 | 05/09 07 h |
| Utilisateur V04 Consulter le portefeuille | `02-consulter-le-portefeuille-du-commercial` | 863 | 680 | 05/09 16 h |
| Produit V01 Ajouter un produit | `03-ajouter-modifier-un-produit` | 864 | 681 | 06/09 07 h |
| Produit V02 Ajouter une stratégie | `03-ajouter-modifier-une-strategie-a-un-produit` | 865 | 682 | 06/09 16 h |
| Produit V03 Attacher des documents | `03-ajouter-modifier-des-documents-a-un-produit` | 866 | 683 | 07/09 07 h |
| Produit V04 Programme de fidélité | `03-ajouter-le-produit-a-un-programme-fidelite` | 867 | 684 | 07/09 16 h |

Chaque post monte le master 9:16 déposé dans la bibliothèque RapidoCMS, et se
tient aux trois temps de la charte : le problème dans les mots du métier, ce que
le logiciel fait à l'écran, l'invitation à une démo au 06.14.18.92.25. Aucun
emoji, quatre hashtags, le lien de la page en fin de post.

## Deux défauts trouvés en préparant ce lot

**Le domaine `tutoriel.rapidocrm.com` n'existe pas.** Il n'a aucun
enregistrement DNS — ce n'est pas une limite du proxy de l'environnement, la
résolution échoue partout. Le domaine servi est **`tutoriel.rapido-crm.com`**,
avec un trait d'union, vers lequel `academie-rapidocrm.lovable.app` redirige en
302 et qui répond 200 sur les huit pages de ce lot.

Conséquences, aucune corrigée ici :

- `publication.json → site.url` porte le domaine mort sur les 19 tutoriels
  publiés. La valeur vient du MCP « RapidoCMS tutoriels » (`publier_tutoriel`
  renvoie `url`), pas d'une construction du pipeline : c'est donc côté serveur
  qu'il faut la corriger, sinon la prochaine publication réécrira la mauvaise.
- **Les 11 posts LinkedIn du lot précédent pointent tous vers ce domaine mort.**
  Leur lien de fin de post ne mène nulle part.
- `publier:site` appelle pourtant `repond(url)` avant d'écrire `publication.json`,
  et `repond()` renvoie `false` sur un échec DNS. Le contrôle aurait dû arrêter
  la publication : à comprendre avant de relancer un lot.

Les huit posts de ce lot utilisent `tutoriel.rapido-crm.com`, vérifié en 200.

**La file LinkedIn de RapidoSoftware n'a jamais tourné.** Les 11 publications du
lot précédent (27/08 → 01/09) sont toutes à `statut = 0`, sans `post_urn`, avec
`updated_at` égal à `created_at` : le job ne les a pas prises, et leurs créneaux
sont maintenant passés. Sur la même période, la file de FoodEatUp
(`account_id 68807312`) tourne — sept posts publiés avec leur URN, vingt en échec
`error creating asset401`. Le problème est donc propre à ce compte, pas au
planificateur.

À trancher par Michael : reprogrammer les 11 posts du lot précédent à des dates
futures une fois la file réparée, et corriger leur lien avant de les renvoyer.

## Instructions d'agent des quatre pages Produits — toujours en attente

Le connecteur **« RapidoCRM tuto »** n'est pas activé dans la session
(`enabledInChat: false`) : `configurer_agent_tutoriel` n'est pas appelable du
tout, indépendamment de l'erreur « Cannot coerce the result to a single JSON
object » observée le 28/08. Rien ne permet de dire, depuis ici, si cette panne
serveur est encore là.

Les quatre charges utiles sont prêtes, générées par le même code que le pipeline
(`instructionsAgent` de `src/pipeline/publier-site.ts`), dans
`content/Produits/<Vxx>/mcp/rapidocms-tutoriels.configurer_agent_tutoriel.configurer_agent_tutoriel.demande.json`.
Le pont MCP les reprendra telles quelles ; `cle_api` s'ajoute à l'appel, jamais
dans le fichier.

## Module Comptabilité — arrêté au point de contrôle

`content/Comptabilite/V01..V04` ont analyse, fiche et script (122 s, 91 s, 90 s,
118 s). Le premier point d'arrêt de la chaîne — validation du script — n'est pas
levé : ni voix ni rendu n'ont été lancés, conformément à la règle 6 du
`CLAUDE.md` du studio.
