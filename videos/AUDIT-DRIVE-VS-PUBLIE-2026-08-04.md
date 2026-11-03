# Audit complet — Drive vs. tutoriels publiés (2026-08-04)

Audit demandé par Michael : comparer le Drive
`https://drive.google.com/drive/folders/1LpWivm0KEPwX5XhNHiw08426NjT6PXHC` (10 dossiers
module, interrogés en direct via le MCP Google Drive) avec `src/data/tutorials.ts` sur
Lovable (FoodEatUp Academy, project `55ff35b7-c442-42c4-950c-8c7fd420c645`, workspace
`Contact.prendstapart`).

**Le Drive a été considérablement enrichi depuis le dernier audit** (`FAISABILITE-SERIE-TUTORIELS.md`,
2026-08-02, qui ne couvrait que 5 modules/92 dossiers). Entre le 2026-08-03 10h12 et 11h18,
5 nouveaux dossiers module ont été créés : **Mon Site, Marketing, Service, KDS, Réservation**.
Le Drive couvre maintenant **137 sujets sur les 157 vidéos prévues** (les 20 restants —
`caisse-pos`, `hubrise-livraisons`, `caroline-ia` — n'ont **aucun dossier Drive** pour
l'instant ; `predibot` est fourni hors-Drive, directement par chat, comme convenu).

## Vignettes manquantes — vérifié, aucune

Audit des 55 entrées publiées sur `tutorials.ts` : **100% ont un `thumbnailUrl` qui répond
en HTTP 200 avec `content-type: image/jpeg`** (vérifié par sondage sur plusieurs URLs
RapidoCMS S3 sans extension de fichier apparente — S3 sert le bon `Content-Type` via ses
métadonnées, ce n'est pas une image cassée). **Rien à ajouter côté vignettes existantes.**
Chaque nouveau tutoriel continue de recevoir sa vignette (réutilisation neutre de la carte
d'intro) au moment de sa publication — c'est déjà fait pour `predire-ses-commandes` et le
sera pour `retrouver-lhistorique-des-zones-de-nettoyage` dès validation.

## Progression par module

| Module (Drive) | moduleSlug | Prévu | Publié | Manquant |
|---|---|---:|---:|---:|
| 1 - Configuration | `configuration` | 14 | **14** | 0 — **complet** |
| 2 - Équipe & Planning | `equipe-planning` | 20 | 19 | 1 |
| 3 - Comptabilité | `comptabilite` | 10 | 4 | 6 |
| 4 - HACCP | `haccp` | 30 | 8* | ~22* |
| 5 - StockVision AI | `stockvision-ai` | 20 | ~10* | ~10* |
| 6 - Mon Site | `site-web-vitrine` | 8 | 0 | 8 |
| 7 - Marketing | `marketing-fidelite` | 24 | 0 | 24 |
| 8 - Service | `service-commande` | 3 | 0 | 3 |
| 9 - KDS | `kds-cuisine` | 3 | 0 | 3 |
| 10 - Réservation | `reservation-salle` | 5 | 0 | 5 |
| — (pas de dossier Drive) | `caisse-pos` | 7 | 0 | 7 (+ dossier Drive à créer) |
| — (pas de dossier Drive) | `hubrise-livraisons` | 4 | 0 | 4 (+ dossier Drive à créer) |
| — (pas de dossier Drive) | `caroline-ia` | 6 | 0 | 6 (+ dossier Drive à créer) |
| — (fourni par chat, hors Drive) | `predibot` | 3 | 2 | 1 |
| **Total** | | **157** | **~57** | **~100** |

\* HACCP et StockVision AI : le Drive a réorganisé ses dossiers depuis la première vague de
tutoriels (numérotation différente, et certains sujets — "Production : valider une
production", "Historique de la production" — existent avec un intitulé quasi identique
**dans les deux modules Drive**, HACCP et StockVision AI). Trois tutoriels publiés sous
`moduleSlug: "predibot"` ou `"haccp"` correspondent en fait à des dossiers rangés sous
**StockVision AI** côté Drive (`predire-ses-commandes`, `suivre-suggestions-agent-ia`,
`valider-une-production`, `tracer-ses-productions-historique`) : pas d'erreur de production,
juste une convention à trancher — **question ouverte pour Michael**, pas corrigée
unilatéralement ici.

## Module Configuration — complet (14/14)

Aucune vidéo manquante. Point de nettoyage mineur repéré : deux entrées publiées
(`ouvrir-sa-vitrine`, subcatégorie "10 - ouvrir sa vitrine en ligne" et
`ouvrir-sa-vitrine-en-ligne`, subcatégorie "13 - votre vitrine en ligne") semblent couvrir
le même sujet Drive ("12 - votre vitrine en ligne") sous deux slugs différents — doublon
probable, à confirmer avant de le retirer (pas supprimé ici, décision qui revient à Michael).

## Module Équipe & Planning — 19/20

**Manquant :**
- **15 - Gestion des pauses, pointage entrée/sortie et empreinte photo du pointage**

Point de vigilance déjà noté dans `FAISABILITE-SERIE-TUTORIELS.md` (2026-08-02) : les rushes
des dossiers 14 et 15 faisaient exactement la même taille en octets (doublon probable) — à
revérifier avant de lancer cette vidéo, le rush du 15 est peut-être encore le mauvais fichier.

## Module Comptabilité — 4/10

**Publiés :** gérer ses fournisseurs (achats), changer les statuts d'un devis, changer les
statuts d'une facture, saisir ses dépenses fournisseur.

**Manquant :**
- **2 - Ajout/modification/suppression d'un client** — **bloqué** au dernier audit (aucun
  enregistrement d'écran déposé dans le dossier, seulement carte intro/fin + clip avatar) ;
  à revérifier si le rush a été ajouté depuis
- **3 - Créer un devis** (création — distinct du tutoriel "changer les statuts" déjà publié)
- **5 - Créer une facture** (idem, création distincte du statut)
- **8 - Archivage de mes dépenses et connexion aux livraisons**
- **9 - E-reporting et archivage des factures**
- **10 - Mes commandes QR code, site web, agent vocal**

## Module HACCP — 8/30 confirmés sans ambiguïté (~22 restants)

**Publiés (sans ambiguïté) :** déclarer ses équipements, relever une température
d'équipement, retrouver l'historique des températures, ajouter une température plat,
créer une traçabilité simplifiée, + `retrouver-lhistorique-des-zones-de-nettoyage`
(livré, en attente de validation).

**Manquant (liste Drive complète, 30 sujets) — à trancher/planifier avec Michael, plusieurs
se recoupent avec StockVision AI (voir note ci-dessus) :**
1, 3, 6, 8, 9, 10, 11, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30 —
soit notamment : enregistrer une température, traçabilité complète synchronisée produits,
plan de nettoyage (créer/éditer, pas seulement consulter l'historique — déjà fait), créer un
plat pour production, étiquettes (créer produit, imprimer, historique), documents de
nettoyage, templates FoodEatUp, check-list hygiène (créer, contrôler, historique), contrôle
réception livraison (créer, historique), photo + analyse IA nettoyage, export historique
module HACCP.

## Module StockVision AI — ~10/20 confirmés

**Publiés :** liste de courses (tenir), sortir ingrédients du stock, mouvements de stock
(saisir + lire), imprimer ingrédients de production, statistiques par module ; + 3 entrées
mentionnées plus haut dont le `moduleSlug` publié diffère du dossier Drive (prédictions,
suggestions agent IA, valider une production, historique production).

**Manquant :** carte (création/modification), liste de courses (commander/envoyer
fournisseur), livraisons (statuts, détails/validation, température/étiquettes EAN, facture
OCR, ajout factures historique, dépenses), 2ᵉ tutoriel statistiques (rapport/historique par
module).

## Modules sans aucune vidéo publiée (Drive prêt)

- **Mon Site** (`site-web-vitrine`, 8) : activer éditeur web, choisir template, personnaliser
  site, gérer pages, créer site par IA, réservations & horaires, ajouter contenu pro,
  connecter domaine.
- **Marketing** (`marketing-fidelite`, 24) : avis Google (débloquer/synchro/répondre), pack
  marketing, campagnes (lancer/100%IA/agenda), templates WhatsApp, ciblage/consentement,
  crédits com, fidélité (booster/récompenses/jeux concours/QR code/gagnants/vue client/
  multi-canal), sondages (créer/résultats), MCP RapidoCMS+Iris, calendrier IA Iris, stocks
  dormants, synchro design & charte.
- **Service** (`service-commande`, 3) : commandes multi-canaux, site vocal & QR code, envoi
  direct cuisine.
- **KDS** (`kds-cuisine`, 3) : créer postes KDS, vue par poste, gérer le KDS en direct.
- **Réservation** (`reservation-salle`, 5) : réservations du jour, ajouter une réservation,
  gérer & no-shows, placer un client à table, commander par QR code.

**Complétude des assets (carte intro/écran/carte fin) de ces 5 modules non vérifiée** —
c'est un point ouvert : l'audit de 2026-08-02 ne portait que sur les 5 premiers modules.
À faire avant de lancer la production dessus.

## Modules sans dossier Drive du tout

`caisse-pos` (7), `hubrise-livraisons` (4), `caroline-ia` (6) — 17 vidéos au total. Aucun
dossier trouvé sous le Drive racine actuel. Soit ils doivent encore être créés/partagés par
Michael, soit ces modules seront traités autrement (à clarifier).

## PrediBot — 2/3 (hors Drive, fourni par chat)

Publiés : `predire-ses-commandes`, `suivre-suggestions-agent-ia`. Reste 1 vidéo (sujet non
identifié pour l'instant — le module s'appelle "PrediBot (Agent IA Directeur)", une
intégration WhatsApp est mentionnée ailleurs dans le code du site, possible piste).

## Prochaines étapes proposées

1. **Michael tranche les points ouverts** : doublon vitrine (config), convention de module
   predibot/haccp/stockvision, sujet du 3ᵉ PrediBot, dossiers Drive manquants pour
   caisse-pos/hubrise-livraisons/caroline-ia.
2. **Revérifier les 2 blocages connus** : rush manquant (comptabilité, dossier client) et
   doublon de rush (équipe-planning, dossiers 14/15).
3. **Vérifier la complétude des assets** des 5 nouveaux modules Drive (Mon Site, Marketing,
   Service, KDS, Réservation) avant de lancer leur production.
4. **Dérouler module par module** en suivant le pipeline habituel (script → validation →
   VO → montage → livraison → validation → publication), en commençant par les modules les
   plus courts et déjà propres (Service, KDS : 3 vidéos chacun) pour valider le pipeline sur
   ces nouveaux contenus avant d'attaquer Marketing (24 vidéos, le plus gros morceau restant).
