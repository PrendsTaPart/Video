# prompt.md — relance des vidéos tutoriels FoodEatUp

Prompt à donner à l'agent qui reprend la production des vidéos tutoriels. Mis à jour le 02/11/2026.

## Ta mission

Produire les vidéos manquantes des fiches de l'Académie FoodEatUp (https://tutoriel.foodeatup.com/), une à une,
puis les publier pour qu'elles apparaissent dans le logiciel FoodEatUp.

Source de vérité de la liste : `docs/academie/videos-a-produire.md` du dépôt `PrendsTaPart/stockvisionai`
(régénérée depuis le catalogue `resources/js/data/academieTutoriels.json`). La copie ci-dessous date du 02/11/2026.

## Chaîne de production (une vidéo = un dossier Google Drive)

Dossier Drive racine : https://drive.google.com/drive/folders/1LpWivm0KEPwX5XhNHiw08426NjT6PXHC
Arborescence : `{module}/{slug}/01-vignette`, `02-rushes`, `03-montage`, `04-publie`.

1. **Vignette** — Zied : PNG 1280×720, titre exact de la liste, charte FoodEatUp (bleu #0066FF, orange #FFA500, bleu nuit #0F1A23).
2. **Rushes** — Mouna : capture d'écran du logiciel, tournée sur le **restaurant école** (Configuration › Mode école),
   jamais sur les données d'un vrai client.
3. **Montage + voix** — Claude (toi) : MP4 1080p, 40 à 90 s, voix ElevenLabs du chef (même voix que l'Académie),
   sous-titres .srt, aucun prix ni chiffre inventé, outils de `academie-pipeline/`.
4. **Publication** — Claude : YouTube, puis lien YouTube posé sur la fiche de l'Académie (projet Lovable
   `55ff35b7-c442-42c4-950c-8c7fd420c645`). Ensuite, dans `stockvisionai`, régénérer le catalogue
   (`python3 scripts/academie/generer_catalogue.py` avec le dépôt `foodeatup-guide-star-227b4772` cloné à côté),
   PR vers `production`. La vidéo apparaît alors seule : bouton info (popup tutoriel) de l'écran, onglet Apprendre
   du Chef, « En savoir plus » des missions du mode école, guide « Cette page ».

## Règles

- Ne marque jamais une vidéo publiée tant que le lien YouTube ne répond pas.
- Une vidéo à la fois : vignette + rushes présents dans Drive avant le montage ; sinon, passe à la suivante et note le manque.
- Tiens à jour, à la fin de chaque séance, la colonne « état » dans `RAPPORT-VIDEOS.md` de ce dépôt.

## api-developpeurs (4)

| Slug | Titre de la vignette | Écran(s) du logiciel |
|---|---|---|
| `automatiser-avec-l-api-foodeatup` | Automatiser son restaurant avec n8n, Make ou un agent IA | — |
| `creer-sa-cle-api-foodeatup` | Créer sa clé API et obtenir un jeton | — |
| `documentation-api-foodeatup` | L'API FoodEatUp : les outils du catalogue courant derrière une seule porte | — |
| `premier-appel-api-foodeatup` | Son premier appel : lister et appeler un outil | — |

## assistant-foodeatup (3)

| Slug | Titre de la vignette | Écran(s) du logiciel |
|---|---|---|
| `chef-comprendre-apprendre-agir` | Le Chef — Comprendre / Apprendre / Agir | — |
| `mode-ecole-restaurant-fictif` | Le mode école : s'entraîner sur un restaurant fictif | `establishment.ecole.index` |
| `mon-profil-assistant` | Mon profil › Assistant | — |

## caisse-pos (38)

| Slug | Titre de la vignette | Écran(s) du logiciel |
|---|---|---|
| `acheter-son-materiel-de-caisse` | Acheter son matériel de caisse | — |
| `activer-les-garde-fous-de-caisse` | Activer les garde-fous de caisse | `establishment.service.integrations` |
| `affecter-un-role-et-un-pin-en-caisse` | Affecter un rôle et un code PIN à un employé | — |
| `ajouter-l-abonnement-caisse` | Ajouter l'abonnement caisse | — |
| `ajouter-smile-and-pay` | Ajouter Smile&Pay | — |
| `ajouter-son-tpe` | Ajouter son terminal de paiement (TPE) | — |
| `ajouter-une-promotion-en-caisse` | Ajouter une promotion en caisse | — |
| `appliquer-une-remise` | Appliquer une remise et des avoirs | `establishment.service.caisse.fullscreen` |
| `cloturer-sa-caisse` | Clôturer sa caisse — le Z de caisse | `establishment.service.caisse.fullscreen` |
| `configurer-sa-caisse-pos` | Configurer sa caisse POS — TPE & ticket | `establishment.service.caisse.fullscreen` |
| `configurer-ses-happy-hours` | Configurer ses happy hours | `establishment.service.caisse.fullscreen` |
| `configurer-ses-produits-en-caisse` | Configurer ses produits en caisse | — |
| `configurer-son-imprimante-de-caisse` | Configurer son imprimante de caisse | — |
| `configurer-supplements-et-cuissons` | Cuissons & suppléments | `establishment.carte.options.page` |
| `creer-un-lien-de-paiement` | Créer un lien de paiement | — |
| `creer-un-poste-de-caisse` | Créer un poste de caisse | `establishment.service.integrations` |
| `creer-une-note-sans-table` | Créer une note sans table — comptoir, à emporter, livraison | `establishment.service.caisse.fullscreen` |
| `declarer-une-perte` | Déclarer une perte | — |
| `encaisser-un-bon-ou-une-carte-cadeau` | Encaisser un bon ou une carte cadeau | `establishment.service.caisse.fullscreen` |
| `encaisser-une-commande` | Encaisser une commande — comptoir & table | `establishment.service.caisse.fullscreen`, `establishment.service.payment-links` |
| `envoyer-une-commande-en-cuisine` | Envoyer une commande en cuisine | `establishment.service.caisse.fullscreen` |
| `former-un-employe-mode-ecole` | Former un employé avec le mode école | `establishment.service.caisse.fullscreen` |
| `multi-caisse-z-consolide` | Multi-caisse et Z consolidé | — |
| `note-frais` | Note de frais | — |
| `ouvrir-son-fond-de-caisse` | Ouvrir son fond de caisse en début de service | `establishment.service.caisse.fullscreen` |
| `prendre-une-commande-en-caisse` | Prendre une commande à table | `establishment.service.caisse.fullscreen` |
| `rapprochement-bancaire-qonto` | Faire son rapprochement bancaire avec Qonto | — |
| `rapprochement-comptable-pennylane` | Faire son rapprochement comptable avec Pennylane | — |
| `rapprocher-paiement-tpe-sans-reponse` | Rapprochement d’un paiement TPE sans réponse | — |
| `realiser-un-avoir` | Réaliser un avoir | `establishment.service.caisse.fullscreen` |
| `realiser-un-paiement-en-caisse` | Réaliser un paiement — la fenêtre d'encaissement | `establishment.service.caisse.fullscreen` |
| `repas-personnel-pertes` | Repas du personnel et pertes | — |
| `retrouver-ses-documents-fiscaux` | Conformité fiscale | `establishment.service.fiscal` |
| `retrouver-ses-statistiques-de-caisse` | Statistiques caisse | `establishment.pos-analytics.index` |
| `separer-une-addition` | Séparer une addition — multi-paiement | `establishment.service.caisse.fullscreen` |
| `suivre-les-ecarts-de-caisse` | Suivre les écarts de caisse — historique | `establishment.service.caisse.fullscreen` |
| `telecharger-sa-compta` | Télécharger sa comptabilité | — |
| `voir-son-journal-de-caisse` | Journal de caisse | `establishment.cash-journal.index`, `establishment.service.caisse.fullscreen` |

## caroline-ia (1)

| Slug | Titre de la vignette | Écran(s) du logiciel |
|---|---|---|
| `caroline-transfert-humain` | Transfert vers un humain | — |

## client-restaurant (10)

| Slug | Titre de la vignette | Écran(s) du logiciel |
|---|---|---|
| `commander-a-table-avec-le-qr-code` | Commander à table avec le QR code | — |
| `commander-depuis-le-site-du-restaurant` | Commander depuis le site du restaurant | — |
| `cumuler-ses-points-a-chaque-passage` | Cumuler ses points à chaque passage | — |
| `laisser-un-avis-apres-son-passage` | Laisser un avis après son passage | — |
| `payer-sa-commande-et-recevoir-son-recu` | Payer sa commande et recevoir son reçu | — |
| `recevoir-les-offres-du-restaurant` | Recevoir les offres du restaurant sans être submergé | — |
| `rejoindre-le-programme-de-fidelite` | Rejoindre le programme de fidélité | — |
| `reserver-une-table` | Réserver une table | — |
| `trouver-le-restaurant-et-voir-la-carte` | Trouver le restaurant et voir la carte en ligne | — |
| `utiliser-une-recompense-ou-une-offre` | Utiliser une récompense ou une offre | — |

## comptabilite (6)

| Slug | Titre de la vignette | Écran(s) du logiciel |
|---|---|---|
| `doc-facturation-detaillee` | Facturation : la documentation détaillée | — |
| `gerer-ses-clients-cote-ventes` | Gérer ses clients côté ventes | `establishment.clients.index` |
| `modeles-apparence-factures-devis` | Modèles & apparence des factures et devis | `establishment.finance.modeles.page` |
| `paiement-relance-fiche-client` | Paiement en ligne et relance depuis la fiche client | — |
| `retrouver-toutes-mes-commandes` | Retrouver la commande derrière une facture | `establishment.commandes.index` |
| `tableau-bord-financier` | Tableau de bord financier | `establishment.finance.dashboard` |

## configuration (8)

| Slug | Titre de la vignette | Écran(s) du logiciel |
|---|---|---|
| `application-recettes-tablette` | Application Recettes — appairer une tablette | `establishment.recettes-app.index` |
| `dessiner-son-plan-de-salle` | Dessiner son plan de salle / QR code à table | `establishment.floor-plan` |
| `documents-pro` | Documents pro | `establishment.documents-pro.page` |
| `installer-son-restaurant-avec-le-configurateur` | L'Agent Configurateur : installez votre restaurant en une conversation | `establishment.onboarding.page` |
| `ma-marque` | Ma marque | `establishment.marque.page` |
| `premiers-pas-18-etapes` | Premiers pas — parcours en 18 étapes | — |
| `reprises-configuration` | Reprises de configuration | `establishment.duplications.index` |
| `securite-acces` | Sécurité & accès | `establishment.securite` |

## ecrans-bornes (5)

| Slug | Titre de la vignette | Écran(s) du logiciel |
|---|---|---|
| `bornes-tablettes` | Bornes & tablettes | `establishment.kiosks.index` |
| `ecrans-affichage` | Écrans d’affichage | `establishment.display.index` |
| `menu-digital-qr-table` | Menu digital & QR de table | `establishment.menu-digital.index` |
| `regie-publicitaire` | Régie publicitaire | `establishment.display.regie.index` |
| `supervision-ecrans` | Supervision des écrans | `establishment.display.supervision.index` |

## equipe-planning (4)

| Slug | Titre de la vignette | Écran(s) du logiciel |
|---|---|---|
| `consulter-ses-performances-employe` | Suivre ses performances FoodEatUp (côté employé) | `establishment.employees` |
| `retrouver-ses-documents-paie-et-contrat` | Retrouver ses documents, paie et contrat | `establishment.employees` |
| `suivre-ses-performances-cote-employe` | Suivre ses performances, côté employé | — |
| `variables-paie` | Variables de paie | `establishment.paie.index` |

## foodeatup-live (5)

| Slug | Titre de la vignette | Écran(s) du logiciel |
|---|---|---|
| `live-bracelets-nfc` | Bracelets NFC | `establishment.live.index` |
| `live-creer-un-evenement` | FoodEatUp Live : créer et ouvrir un événement | `establishment.live.index` |
| `live-portefeuille-cashless` | Portefeuille cashless | `establishment.live.index` |
| `live-qr-paiement` | QR de paiement | `establishment.live.index` |
| `live-recharges` | Recharges | `establishment.live.index` |

## haccp (5)

| Slug | Titre de la vignette | Écran(s) du logiciel |
|---|---|---|
| `cycles-thermiques` | Cycles thermiques — refroidissement et remise en température | `establishment.haccp.cellules.index` |
| `friteuses-huile` | Friteuses & huile — tests polaires | `establishment.haccp.friteuses.index` |
| `parametres-haccp` | Paramètres HACCP | `establishment.haccp.parametres` |
| `photo-ia-controle-nettoyage` | Une photo, l'IA contrôle votre nettoyage (Module Hygiène) | `establishment.haccp.plan-nettoyage.index` |
| `poser-une-dlc-sur-ses-productions` | Poser une DLC sur ses productions | `establishment.haccp.etiquettes.index` |

## hubrise-livraisons (4)

| Slug | Titre de la vignette | Écran(s) du logiciel |
|---|---|---|
| `centraliser-les-commandes-livraison` | Centraliser les commandes — flux livraison | `establishment.service.integrations` |
| `connecter-son-hubrise` | Connecter son HubRise à | `establishment.service.integrations` |
| `relier-uber-eats-et-deliveroo` | Relier Uber Eats & Deliveroo via HubRise | `establishment.service.integrations` |
| `synchroniser-sa-caisse-tierce` | Synchroniser sa caisse tierce via HubRise | `establishment.service.integrations` |

## laboratoire-livraison (10)

| Slug | Titre de la vignette | Écran(s) du logiciel |
|---|---|---|
| `commander-laboratoire` | Commander au laboratoire | `establishment.labo.index` |
| `commandes-boutiques-laboratoire` | Commandes des boutiques | `establishment.labo-reception.index` |
| `fabrication-jour` | Fabrication du jour | `establishment.fabrication.index` |
| `hub-laboratoire-siege` | Suivre ses laboratoires depuis le siège | `establishment.reseau.laboratoire` |
| `hub-livraison-siege` | Suivre les livraisons du réseau depuis le siège | `establishment.reseau.livraison` |
| `planning-atelier` | Planning d’atelier | `establishment.atelier.index` |
| `preparation-colis` | Préparation & colis | `establishment.picking.index` |
| `receptions-laboratoire` | Réceptions du laboratoire | `establishment.receptions.index` |
| `stock-finis-rappel-lot` | Stock produits finis & rappel de lot | `establishment.fabrication.stock` |
| `tournees-application-chauffeur` | Tournées de livraison — application chauffeur | `establishment.tournees.index` |

## les-8-boucles (8)

| Slug | Titre de la vignette | Écran(s) du logiciel |
|---|---|---|
| `boucle-01-configuration-boutique` | Boucle 01 — Configuration boutique : un prix change, toutes vos marges se recalculent | `establishment.onboarding.page` |
| `boucle-02-equipe` | Boucle 02 — Équipe : vos plannings tiennent compte de l'activité réelle | `establishment.leaves.index` |
| `boucle-03-stockvision` | Boucle 03 — StockVision AI : vos ventes deviennent vos achats et votre production | `establishment.dashboard` |
| `boucle-04-haccp` | Boucle 04 — HACCP : votre dossier de conformité se construit chaque jour | — |
| `boucle-05-ecommerce` | Boucle 05 — E-commerce : votre carte en ligne, sans commission | `establishment.service.payment-links`, `establishment.site.studio.index` |
| `boucle-06-communication` | Boucle 06 — Communication : ce que vous savez, vos clients le savent le matin même | `establishment.service.marketing` |
| `boucle-07-fidelite` | Boucle 07 — Fidélité et marketing : chaque client servi devient une relation réactivable | `establishment.service.engagement` |
| `boucle-08-comptabilite` | Boucle 08 — Comptabilité : le chiffre du jour, avant d'éteindre la lumière | `establishment.factures.archives.index` |

## marketing-fidelite (9)

| Slug | Titre de la vignette | Écran(s) du logiciel |
|---|---|---|
| `booster-les-stocks-dormants` | Booster les stocks dormants (opportunités IA) | `establishment.service.iris` |
| `integrer-le-mcp-rapidocms-iris` | Intégrer le MCP RapidoCMS & Iris | `establishment.service.iris` |
| `iris-creer-post` | Iris — créer un post | — |
| `iris-roi` | Iris — ROI | — |
| `menu-enfant-jeux` | Menu enfant & jeux | `establishment.menu-enfant.page` |
| `newsletters-emails` | Newsletters & e-mails | `establishment.emails.page` |
| `supports-imprimes-qr` | Supports imprimés & QR | `establishment.studio-print.page` |
| `supports-marketing-reseaux-sociaux` | Supports marketing : liens et réseaux sociaux | `establishment.marketing` |
| `voir-les-gagnants-historique` | Voir les gagnants — historique | `establishment.service.engagement` |

## partenaire-apporteur (2)

| Slug | Titre de la vignette | Écran(s) du logiciel |
|---|---|---|
| `organiser-sa-prospection-partenaire` | Organiser sa prospection de partenaire | — |
| `qualifier-un-etablissement-en-dix-questions` | Qualifier un établissement en dix questions | — |

## partenaire-formateur (2)

| Slug | Titre de la vignette | Écran(s) du logiciel |
|---|---|---|
| `former-une-brigade-a-l-haccp` | Former une brigade à l'HACCP en une heure | — |
| `passer-le-relais-academie` | Passer le relais : l'Académie comme support | — |

## partenaire-installateur (2)

| Slug | Titre de la vignette | Écran(s) du logiciel |
|---|---|---|
| `installer-un-poste-de-caisse-foodeatup` | Installer un poste de caisse | — |
| `raccorder-imprimante-tiroir-et-tpe` | Raccorder imprimante, tiroir et TPE | — |

## partenaire-revendeur (2)

| Slug | Titre de la vignette | Écran(s) du logiciel |
|---|---|---|
| `de-la-demonstration-a-la-signature` | Conclure : de la démonstration à la signature | — |
| `le-point-a-30-jours-avec-le-client` | Le point à 30 jours avec le client | — |

## predibot (9)

| Slug | Titre de la vignette | Écran(s) du logiciel |
|---|---|---|
| `agent-gestion-fournisseur-whatsapp` | Agent Gestion Fournisseur : validez vos réceptions depuis WhatsApp | `establishment.predibot.chat` |
| `agent-haccp-whatsapp` | Agent HACCP : relevez vos températures depuis WhatsApp | `establishment.predibot.chat` |
| `configurer-sa-boutique-avec-predibot` | Configurer sa boutique en discutant avec PrediBot | `establishment.predibot.chat` |
| `conformite-haccp-ia` | Conformité HACCP IA | `establishment.predibot.haccp-compliance` |
| `gerer-son-stock-par-whatsapp` | Gérer son stock par WhatsApp avec l'agent IA | `establishment.predibot.stock-predictions` |
| `lire-ses-previsions-predibot` | Lire ses prévisions PrediBot | `null`, `establishment.predibot.dashboard`, `establishment.predibot.order-forecasting` |
| `parler-a-predibot-avec-nos-prompts` | Parler à PrediBot avec nos prompts | `null`, `establishment.predibot.chat` |
| `piocher-dans-la-marketplace-de-prompts` | Piocher dans la marketplace de prompts | `establishment.predibot.chat` |
| `previsions-rh` | Prévisions RH | `establishment.predibot.hr-predictions` |

## reseau-franchise (12)

| Slug | Titre de la vignette | Écran(s) du logiciel |
|---|---|---|
| `accueil-siege` | Accueil siège | `establishment.reseau.index` |
| `achats-centralises` | Achats centralisés | `establishment.reseau.achats` |
| `boutiques-reseau` | Boutiques | `establishment.reseau.boutiques` |
| `catalogue-central` | Catalogue central | `establishment.reseau.catalogue` |
| `collecte-rh-paie-reseau` | Collecte RH & paie | `establishment.reseau.rh.collecte` |
| `comparatif-reseau` | Comparatif | `establishment.reseau.comparatif` |
| `comptabilite-banque-reseau` | Comptabilité & banque | `establishment.reseau.compta` |
| `configuration-reseau` | Configuration du réseau | `establishment.reseau.configuration` |
| `entites-topologie` | Entités & topologie | `establishment.reseau.topologie` |
| `kpi-reseau` | KPI du réseau | `establishment.reseau.kpi` |
| `prix-siege` | Prix du siège | `establishment.reseau.prix` |
| `rh-reseau` | RH du réseau | `establishment.reseau.rh` |

## reseau-partenaires (8)

| Slug | Titre de la vignette | Écran(s) du logiciel |
|---|---|---|
| `apres-la-mission-suivi-et-fidelisation` | Après la mission : suivi, commissions et fidélisation | — |
| `argumentaire-foodeatup-cinq-minutes` | L'argumentaire FoodEatUp en cinq minutes | — |
| `compte-rendu-de-mission-partenaire` | Rédiger son compte rendu de mission | — |
| `journee-type-partenaire-foodeatup` | Une journée de partenaire, sur le terrain | — |
| `remonter-les-retours-terrain` | Remonter les retours terrain à | — |
| `reseau-partenaires-foodeatup` | Le réseau de partenaires | — |
| `suivre-ses-ventes-et-commissions` | Suivre ses ventes et ses commissions | — |
| `vendre-le-passage-a-l-ia` | Vendre le passage à l'IA, pas un logiciel de plus | — |

## reservation-salle (11)

| Slug | Titre de la vignette | Écran(s) du logiciel |
|---|---|---|
| `acompte-empreinte-bancaire` | Acompte et empreinte bancaire — anti no-show | — |
| `billets-modeles` | Billets et modèles de billet | `establishment.evenements.index` |
| `billets-pdf-qr-scan` | Billets PDF à QR et scan à l’entrée | — |
| `bouton-reserver-google` | Bouton « Réserver » sur Google | — |
| `evenements-privatisations` | Événements & privatisations | — |
| `liste-attente-en-ligne` | Liste d’attente en ligne | — |
| `modeles-billet` | Modèles de billet | — |
| `offres-creneau` | Offres de créneau | — |
| `rappel-sms-veille` | Rappel SMS la veille | — |
| `reservation-sur-autre-site` | Module de réservation sur un autre site | — |
| `retrouver-ses-reservations-du-jour` | Retrouver ses réservations du jour | `establishment.service.reservations` |

## service-commande (3)

| Slug | Titre de la vignette | Écran(s) du logiciel |
|---|---|---|
| `commander-qr-code` | Commander par QR Code | `establishment.service.commandes` |
| `mes-commandes-tous-canaux` | Mes commandes : QR code, site web, agent vocal (toutes vos commandes) | `establishment.service.commandes` |
| `retrouver-ses-commandes-multi-canal` | Retrouver ses commandes multi-canal (recherche, filtres et fiche détail) | `establishment.commandes.index`, `establishment.service.commandes` |

## site-web-vitrine (5)

| Slug | Titre de la vignette | Écran(s) du logiciel |
|---|---|---|
| `blog-recettes` | Blog & recettes | `establishment.site.blog.page` |
| `commander-via-site-vocal-qrcode` | Commander : site, agent vocal & QR code à table | `establishment.storefront` |
| `configurer-horaires-et-reservations-site` | Configurer ses horaires et réservations | `establishment.site.studio.index` |
| `placement-carte-vitrine-site` | Placement de la carte — vitrine et site | — |
| `site-cinematique` | Site cinématique | `establishment.site.cinematique.page` |

## stockvision-ai (2)

| Slug | Titre de la vignette | Écran(s) du logiciel |
|---|---|---|
| `cadencier` | Cadencier | `establishment.carte.cadencier.page` |
| `portions-rupture-automatique` | Portions — compteur et rupture automatique | `establishment.carte.portions.page` |

## store-foodeatup (3)

| Slug | Titre de la vignette | Écran(s) du logiciel |
|---|---|---|
| `store-favoris` | Favoris | — |
| `store-installer-apk` | Installer un APK — hors Google Play | — |
| `store-trouver-application` | Trouver une application | — |
