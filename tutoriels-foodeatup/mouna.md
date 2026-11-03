# mouna.md — vidéos tutoriels à tourner

Relevé du 03/11/2026 : catalogue en ligne de l'Académie (https://tutoriel.foodeatup.com, 310 fiches) comparé aux écrans et aux fonctions du logiciel. Fichier GÉNÉRÉ par `scripts/academie/generer_mouna.py` — ne pas l'éditer à la main, modifier `scripts/academie/vignettes.py`.

## En bref

- **171 vidéos à tourner** : 136 fiches existent sur l'Académie sans vidéo, 35 fonctions du logiciel n'ont pas encore de fiche (marquées « fiche à créer »).
- **1 vidéo à retourner** (l'écran a changé), voir plus bas.
- **44 vidéos déjà montées** n'ont pas de lien YouTube : rien à tourner, Claude les publie.
- Doublon à fusionner avant de tourner : `modeles-billet` → `billets-modeles`.

## Qui fait quoi

| Étape | Qui | Dossier Drive de la vidéo | Livrable |
|---|---|---|---|
| 1. Vignette | Zied | `NNN-slug/01-vignette` | PNG 1280×720, **titre de la vignette** ci-dessous, charte FoodEatUp (bleu #0066FF, orange #FFA500, bleu nuit #0F1A23), photo du chef |
| 2. Enregistrement d'écran | **Mouna** | `NNN-slug/02-rushes` | MP4 1080p brut, souris visible, sans voix, 1 à 2 min, sur le **restaurant école** |
| 3. Script + voix off | Claude | `NNN-slug/03-script-voix` | texte de la voix off + MP3 voix Adam (ElevenLabs `eleven_v4`, une prise). Script et **plan de tournage** de chaque vidéo : dépôt `PrendsTaPart/Video`, `tutoriels-foodeatup/scripts/NNN-slug.md` |
| 4. Montage | Claude | `NNN-slug/04-montage` | MP4 1080p 40 à 90 s, sous-titres .srt |
| 5. Publication | Claude | `NNN-slug/05-publie` | RapidoCMS (bibliothèque) → YouTube → fiche de l'Académie → logiciel (catalogue régénéré) |

Dossier Drive : **[16 - À TOURNER](https://drive.google.com/drive/folders/1OJUwIp4Fgsm-h-dDUwU8pbUWmfkrFmf1)** dans [FoodEatUp — Tutoriels vidéo](https://drive.google.com/drive/folders/1LpWivm0KEPwX5XhNHiw08426NjT6PXHC). Un dossier par module, puis un dossier par vidéo `NNN - Titre de la vignette (slug)` avec `01-vignette (Zied)` et `02-rushes (Mouna)`. Les dossiers 1 à 15 déjà présents (vidéos tournées avant le 03/11) ne sont pas touchés.

## Règles de tournage (Mouna)

1. Toujours sur le **restaurant école** (Configuration › Mode école) ou le compte de démonstration : jamais un vrai client, jamais un vrai nom ni un vrai téléphone à l'écran.
2. Navigateur en plein écran, zoom 100 %, 1920×1080, notifications du système coupées, onglets fermés.
3. Un geste par vidéo : partir du menu, faire le geste lentement, montrer le résultat, s'arrêter 2 s sur l'écran final.
4. Pas de voix : Adam est ajouté au montage. Pas de musique.
5. Lire le plan de tournage du script (dépôt Video, `tutoriels-foodeatup/scripts/NNN-slug.md`) avant de filmer.
6. Déposer le fichier dans `02-rushes` sous le nom `slug.mp4` et cocher la colonne « Rush » dans ce fichier (ou prévenir Claude).
7. 🎬 = à tourner sur le compte de démonstration : le restaurant école bloque volontairement paiements, impressions, appairages et envois.
8. Si l'écran ne correspond pas à la fiche (bouton absent, erreur), ne pas tourner : noter le problème dans `02-rushes/probleme.txt`.

Lieu de tournage hors écran du logiciel :

- `client-restaurant` : téléphone, côté client (site public, QR de table, page fidélité)
- `reseau-partenaires` : face caméra + diapositives
- `partenaire-formateur` : face caméra + diapositives
- `partenaire-revendeur` : face caméra + diapositives
- `partenaire-installateur` : sur site, matériel réel (caisse, imprimante, TPE)
- `partenaire-apporteur` : face caméra + diapositives
- `foodeatup-live` : back-office + application Live (téléphone)
- `store-foodeatup` : Store du logiciel (menu profil › Boutiques)

## Ordre conseillé

1. Caisse POS (le plus demandé par les clients), 2. Fiches à créer de la caisse et du KDS, 3. Réservations, 4. Écrans & bornes, 5. Marketing & Iris, 6. Configuration et assistant, 7. Réseau, laboratoire, Live, Store, 8. Côté client, 9. Partenaires.

## Liste de tournage

### caisse-pos (38) — [dossier Drive](https://drive.google.com/drive/folders/1kUQmQgvuxf7L5Y6O7z_zaHl_Qu2WXEta)

| N° | Titre de la vignette (Zied) | Fiche / slug | Où tourner (Mouna) | Rush | Vignette |
|---|---|---|---|---|---|
| 001 [📁](https://drive.google.com/drive/folders/1kK579ABS02mEOcsygzLC7ByPH6L8PqBv) | **Active ta caisse** | Ajouter l'abonnement caisse<br>`ajouter-l-abonnement-caisse` | Abonnement › choisir le Pack caisse | ☐ | ☐ |
| 002 [📁](https://drive.google.com/drive/folders/1ghI_E3B8vP4YUeOloQykPwbOUmru1hJO) | **Ta caisse livrée prête** | Acheter son matériel de caisse<br>`acheter-son-materiel-de-caisse` | Menu profil › Boutiques › Matériel (/materiel) | ☐ | ☐ |
| 003 [📁](https://drive.google.com/drive/folders/1pq_STcLJO52F3bAaTSB9p_mJRy7MEBzu) | **Imprimante branchée** | Configurer son imprimante de caisse<br>`configurer-son-imprimante-de-caisse` | Service › Intégrations › Imprimantes<br>🎬 Compte de démonstration (pas l'école). | ☐ | ☐ |
| 004 [📁](https://drive.google.com/drive/folders/1WEWJmfjY52wWnauvx4YeVKCsLUa2AN1Z) | **Bar + salle = 2 caisses** | Créer un poste de caisse<br>`creer-un-poste-de-caisse` | Configuration boutique › Intégration | ☐ | ☐ |
| 005 [📁](https://drive.google.com/drive/folders/1W_WlXhHMDwZ1rmUsihQUa83a4DTrXkyi) | **Branche Smile&Pay** | Ajouter Smile&Pay<br>`ajouter-smile-and-pay` | Service › Intégrations › Smile&Pay<br>🎬 Compte de démonstration (pas l'école). | ☐ | ☐ |
| 006 [📁](https://drive.google.com/drive/folders/1vXBxQxwzlikZLuujdkp5WNPEm3uLsx0s) | **Ton TPE relié à la caisse** | Ajouter son terminal de paiement (TPE)<br>`ajouter-son-tpe` | Service › Intégrations › Terminaux de paiement<br>🎬 Compte de démonstration (pas l'école). | ☐ | ☐ |
| 007 [📁](https://drive.google.com/drive/folders/1CRJKLACrjsZouf73Zo8WatRWR8ADTJ-6) | **Plus de remise sauvage** | Activer les garde-fous de caisse<br>`activer-les-garde-fous-de-caisse` | Configuration boutique › Intégration | ☐ | ☐ |
| 008 [📁](https://drive.google.com/drive/folders/1UC2QVkJURhqPlWu_kjNftXDuxdtyCgl_) | **Ta carte dans la caisse** | Configurer ses produits en caisse<br>`configurer-ses-produits-en-caisse` | Ma carte › plats, puis Caisse › grille | ☐ | ☐ |
| 009 [📁](https://drive.google.com/drive/folders/1rUF98h__t0fe49dN5Mfi-xUU-d42ThaO) | **Cuissons sans erreur** | Cuissons & suppléments<br>`configurer-supplements-et-cuissons` | StockVisionAI › Cuissons & suppléments | ☐ | ☐ |
| 010 [📁](https://drive.google.com/drive/folders/1qanKE4llJLUZ1e0zh5BalxE7bpzyc1o0) | **Happy hour automatique** | Configurer ses happy hours<br>`configurer-ses-happy-hours` | Service › Caisse | ☐ | ☐ |
| 011 [📁](https://drive.google.com/drive/folders/18CW9Mt0Me2hn1Ciy1TyRQkCn8WCvrCve) | **Une promo en 3 clics** | Ajouter une promotion en caisse<br>`ajouter-une-promotion-en-caisse` | Caisse › ligne › % Remise / Offert | ☐ | ☐ |
| 012 [📁](https://drive.google.com/drive/folders/1B05sgF52tgDk5NShN2V5V-8hBbGI4_ce) | **Un code par serveur** | Affecter un rôle et un code PIN à un employé<br>`affecter-un-role-et-un-pin-en-caisse` | Équipe › Employés › fiche › rôle + code personnel | ☐ | ☐ |
| 013 [📁](https://drive.google.com/drive/folders/19ph4JSP0Lvs8s64zYOocnXlqS6EwrEGk) | **Forme ton serveur** | Former un employé avec le mode école<br>`former-un-employe-mode-ecole` | Service › Caisse | ☐ | ☐ |
| 014 [📁](https://drive.google.com/drive/folders/1nJ1mvZh4n2IqSJRQiIJQ_ci-JtAFb_YS) | **Prends la commande à table** | Prendre une commande à table<br>`prendre-une-commande-en-caisse` | Service › Caisse | ☐ | ☐ |
| 015 [📁](https://drive.google.com/drive/folders/1GIrz02JLxESh_IeNNGbY22xjbnh72HkZ) | **Comptoir, emporter, livraison** | Créer une note sans table — comptoir, à emporter, livraison<br>`creer-une-note-sans-table` | Service › Caisse | ☐ | ☐ |
| 016 [📁](https://drive.google.com/drive/folders/1DLEUU6mPD3geO2mG29IjvbZySHveD10c) | **Envoie en cuisine** | Envoyer une commande en cuisine<br>`envoyer-une-commande-en-cuisine` | Service › Caisse | ☐ | ☐ |
| 017 [📁](https://drive.google.com/drive/folders/14RooWz8WAxyOSNdqOPWUaPI4g4xhyYu5) | **Encaisse en 2 gestes** | Réaliser un paiement — la fenêtre d'encaissement<br>`realiser-un-paiement-en-caisse` | Service › Caisse | ☐ | ☐ |
| 018 [📁](https://drive.google.com/drive/folders/1Zj5HdCVbn_Q0yPSL24B96eKVNyiMYpoS) | **Carte cadeau encaissée** | Encaisser un bon ou une carte cadeau<br>`encaisser-un-bon-ou-une-carte-cadeau` | Service › Caisse | ☐ | ☐ |
| 019 [📁](https://drive.google.com/drive/folders/1uVHz9VNxZ-g8PpQWXJp9ZD5PJwPvuKZg) | **Fais-toi payer par lien** | Créer un lien de paiement<br>`creer-un-lien-de-paiement` | Service › Liens de paiement<br>🎬 Compte de démonstration (pas l'école). | ☐ | ☐ |
| 020 [📁](https://drive.google.com/drive/folders/1p4dyaGYbYgV33YyDlDdZca76JxHVrDxY) | **Un avoir propre** | Réaliser un avoir<br>`realiser-un-avoir` | Service › Caisse | ☐ | ☐ |
| 021 [📁](https://drive.google.com/drive/folders/17aF_Fe1yiMLuWsEGkGQsuOLNJXCIDiox) | **Déclare ta perte** | Déclarer une perte<br>`declarer-une-perte` | Caisse › Personnel / Perte | ☐ | ☐ |
| 022 [📁](https://drive.google.com/drive/folders/1gKYCsGbzn2CDvwIpYRIrQInJZLxam8Ok) | **Le journal de caisse** | Journal de caisse<br>`voir-son-journal-de-caisse` | Finance › Journal de caisse; Service › Caisse | ☐ | ☐ |
| 023 [📁](https://drive.google.com/drive/folders/1zhHiZM5sDu-9DfvluBQWyBpF3kV_IHcl) | **NF525 : tout est là** | Conformité fiscale<br>`retrouver-ses-documents-fiscaux` | Service › Conformité fiscale<br>🎬 Compte de démonstration (pas l'école). | ☐ | ☐ |
| 024 [📁](https://drive.google.com/drive/folders/1HjKZDgpRisZtn67TreMk2yXyC5F3F3gk) | **Ta caisse en chiffres** | Statistiques caisse<br>`retrouver-ses-statistiques-de-caisse` | Finance › Statistiques caisse<br>🎬 Compte de démonstration (pas l'école). | ☐ | ☐ |
| 025 [📁](https://drive.google.com/drive/folders/13Rx-umBfAjKzFSesBdcPK7KM5jD4pK-y) | **Ta compta part seule** | Faire son rapprochement comptable avec Pennylane<br>`rapprochement-comptable-pennylane` | Finance › Comptabilité › Pennylane<br>🎬 Compte de démonstration (pas l'école). | ☐ | ☐ |
| 026 [📁](https://drive.google.com/drive/folders/1vT3GpxHOWVw9EN5rQqAKsJcd_11q-bBs) | **Caisse = banque ?** | Faire son rapprochement bancaire avec Qonto<br>`rapprochement-bancaire-qonto` | Finance › Comptabilité › Qonto<br>🎬 Compte de démonstration (pas l'école). | ☐ | ☐ |
| 027 [📁](https://drive.google.com/drive/folders/1J7Dx8tzea2-4MxsQPyGEtG-sLb9H9Vq7) | **Ta compta en 1 fichier** | Télécharger sa comptabilité<br>`telecharger-sa-compta` | Finance › Comptabilité › Exports (FEC) | ☐ | ☐ |
| 028 [📁](https://drive.google.com/drive/folders/16EEHaKzEZ6vSb1Sq36ntts-rup9ESuRd) | **Un Z pour toute la journée** | Multi-caisse et Z consolidé<br>`multi-caisse-z-consolide` | Caisse › menu Caisse › Z consolidé du jour | ☐ | ☐ |
| 029 [📁](https://drive.google.com/drive/folders/1cFBXvXnR3bxawFerTwOm9QOkhqbdosAt) | **Repas staff : tracé** | Repas du personnel et pertes<br>`repas-personnel-pertes` | Caisse › Personnel / Perte | ☐ | ☐ |
| 030 [📁](https://drive.google.com/drive/folders/128TWBXTBPWcCGfqfHB18gYvK9WoxeT1-) | **Note de frais en 1 clic** | Note de frais<br>`note-frais` | Caisse › note réglée › Note de frais<br>⚠ La fiche de l'Académie décrit une note de frais d'employé ; le logiciel fait un justificatif client sans détail : corriger la fiche avant de tourner. | ☐ | ☐ |
| 031 [📁](https://drive.google.com/drive/folders/1bTS4bC5oKnM5AdEbJnLprqmP0nNTttoB) | **TPE sans réponse ? Calme** | Rapprochement d’un paiement TPE sans réponse<br>`rapprocher-paiement-tpe-sans-reponse` | Caisse › Notes ouvertes › Le client paie autrement<br>🎬 Compte de démonstration (pas l'école). | ☐ | ☐ |
| 032 [📁](https://drive.google.com/drive/folders/1kSrs3iBFSCimkScrrTI4aimZqwH-GCl_) | **Aucune commande ratée** | Voir les commandes qui arrivent en caisse<br>`caisse-pastille-arrivees` | Caisse › cloche « Arrivées » **(fiche à créer)**<br>🎬 Compte de démonstration (pas l'école). | ☐ | ☐ |
| 033 [📁](https://drive.google.com/drive/folders/1te1tSb4oZx0RZb5IxXYKC26MqPZB19HZ) | **Formules en 1 geste** | Vendre une formule et mettre une note en attente<br>`caisse-formules-et-note-en-attente` | Caisse › tuiles Formules, rail « En attente » **(fiche à créer)** | ☐ | ☐ |
| 034 [📁](https://drive.google.com/drive/folders/1mi3aHKkPiPSV-tM0-Xxpog_kv5rLK3Ry) | **Le pourboire bien rangé** | Pourboire, convive et « Et avec ça ? »<br>`caisse-pourboire-convive-et-avec-ca` | Caisse › Encaisser / ticket « Pour : C1 » **(fiche à créer)** | ☐ | ☐ |
| 035 [📁](https://drive.google.com/drive/folders/1K9kx1cThynP9VPDMYxDtcDdcTTTTgjnf) | **Ta caisse, ton mode** | Choisir le mode par défaut : salle, comptoir ou emporter<br>`caisse-mode-par-defaut` | Caisse › menu Caisse › Mode par défaut **(fiche à créer)** | ☐ | ☐ |
| 036 [📁](https://drive.google.com/drive/folders/1Tr5T_F6TR6PgNh4C0bexvkzug-kHI1v9) | **Borne : encaisse en 2 s** | Encaisser au comptoir une commande de la borne<br>`caisse-a-encaisser-borne` | Caisse › badge « À encaisser » (F6) **(fiche à créer)**<br>🎬 Compte de démonstration (pas l'école). | ☐ | ☐ |
| 037 [📁](https://drive.google.com/drive/folders/1GOTKF-RErqckZnMKq3x7NBPzJAMb16dE) | **Débloque ton Z** | Mettre une note de côté « à rapprocher »<br>`caisse-notes-a-rapprocher` | Caisse › Notes ouvertes › Mettre à rapprocher **(fiche à créer)**<br>🎬 Compte de démonstration (pas l'école). | ☐ | ☐ |
| 038 [📁](https://drive.google.com/drive/folders/1OSHR4Nn4Gl6u78nyaKD7d6pZMXqYvMuo) | **La caisse dans ta poche** | L'application Caisse Mobile sur téléphone<br>`application-caisse-mobile` | Application FoodEatUp Caisse Mobile (téléphone) **(fiche à créer)** | ☐ | ☐ |

### kds-cuisine (2) — [dossier Drive](https://drive.google.com/drive/folders/1lZ4POWHo2ye4x-aJZ0mPwRUnHaVgo6XA)

| N° | Titre de la vignette (Zied) | Fiche / slug | Où tourner (Mouna) | Rush | Vignette |
|---|---|---|---|---|---|
| 039 [📁](https://drive.google.com/drive/folders/1I4e-Ubg2JDgUmg03J7fc0aO-xUWiH2aJ) | **Ton KDS sur tablette** | L'application KDS sur tablette : appairer et régler<br>`application-kds-tablette` | Cuisine (KDS) › Application tablette + appli KDS **(fiche à créer)**<br>🎬 Compte de démonstration (pas l'école). | ☐ | ☐ |
| 040 [📁](https://drive.google.com/drive/folders/1NB6aBQfAeA881Ag6OKxMdd2XKS1Lw8YG) | **La cuisine respire** | Rythme du service : envois en attente et saturation<br>`rythme-du-service-kds` | Cuisine (KDS) › Application tablette › Rythme du service **(fiche à créer)**<br>🎬 Compte de démonstration (pas l'école). | ☐ | ☐ |

### reservation-salle (10) — [dossier Drive](https://drive.google.com/drive/folders/1qpAYYbfzqfoh5WyNdD1gqmziqTDI8j7S)

| N° | Titre de la vignette (Zied) | Fiche / slug | Où tourner (Mouna) | Rush | Vignette |
|---|---|---|---|---|---|
| 041 [📁](https://drive.google.com/drive/folders/1bTz5ouVJbORPEcTaR6IpgJswM-yzLZYX) | **Stop aux no-shows** | Acompte et empreinte bancaire — anti no-show<br>`acompte-empreinte-bancaire` | Réservations › Acompte / Anti no-show | ☐ | ☐ |
| 042 [📁](https://drive.google.com/drive/folders/1KgfuFbPRjqRE9L962oMXJdS_eWjV0csh) | **Le SMS qui évite le lapin** | Rappel SMS la veille<br>`rappel-sms-veille` | Réservations › Anti no-show › Rappel SMS<br>🎬 Compte de démonstration (pas l'école). | ☐ | ☐ |
| 043 [📁](https://drive.google.com/drive/folders/1kSD9ThFvTaDCxAeZE7VrpSsFOY1fhKXi) | **Complet ? Liste d'attente** | Liste d’attente en ligne<br>`liste-attente-en-ligne` | Réservations › Salle › Liste d'attente en ligne<br>🎬 Compte de démonstration (pas l'école). | ☐ | ☐ |
| 044 [📁](https://drive.google.com/drive/folders/16ao4g0rI5raqNvbB0dVzzT_QTTiG8rPb) | **Réserve sur ton site** | Module de réservation sur un autre site<br>`reservation-sur-autre-site` | Réservations › Intégration & Google | ☐ | ☐ |
| 045 [📁](https://drive.google.com/drive/folders/1ih4ZVTlOGWGlI9AVEHE3ubtfb7gtMbjO) | **Réserver depuis Google** | Bouton « Réserver » sur Google<br>`bouton-reserver-google` | Réservations › Intégration & Google › Google<br>🎬 Compte de démonstration (pas l'école). | ☐ | ☐ |
| 046 [📁](https://drive.google.com/drive/folders/1C_TdG1XUYm-1KHmFIy-yprEkYV5mmFEh) | **Remplis les heures creuses** | Offres de créneau<br>`offres-creneau` | Réservations › Promos par créneau (?tab=promos)<br>Accès : Réservations › onglet promos (retiré du menu). | ☐ | ☐ |
| 047 [📁](https://drive.google.com/drive/folders/1fYCNWi0UjGKq3xSmEthBNiEowGpwTtif) | **Privatise, encaisse** | Événements & privatisations<br>`evenements-privatisations` | Service › Événements & privatisations | ☐ | ☐ |
| 048 [📁](https://drive.google.com/drive/folders/1f34PszBF41NtJO-XF6tU10n5-2ZHQR1Z) | **Billet scanné à l'entrée** | Billets PDF à QR et scan à l’entrée<br>`billets-pdf-qr-scan` | Événements › Ventes + Service › Validation salle<br>🎬 Compte de démonstration (pas l'école). | ☐ | ☐ |
| 049 [📁](https://drive.google.com/drive/folders/1nO2oqSZuamnzpj0QL0LG56bGbdE_OaXI) | **Tes billets à ton image** | Billets et modèles de billet<br>`billets-modeles` | Mon Site › Billets & modèles | ☐ | ☐ |
| 050 [📁](https://drive.google.com/drive/folders/1pmHcSaoZdw-kHzhgEpyN5axUkBi054zR) | **Ton widget de résa** | Le module de réservation : modèles et plusieurs restaurants<br>`module-reservation-modeles` | Réservations › Intégration & Google **(fiche à créer)**<br>🎬 Compte de démonstration (pas l'école). | ☐ | ☐ |

### ecrans-bornes (7) — [dossier Drive](https://drive.google.com/drive/folders/1AwCRJMz-6NVxEm38JV6ho5wjKtOCK5ib)

| N° | Titre de la vignette (Zied) | Fiche / slug | Où tourner (Mouna) | Rush | Vignette |
|---|---|---|---|---|---|
| 051 [📁](https://drive.google.com/drive/folders/1sBfP6EtSwD8ntkXSB02upUAJkjQKfuKo) | **Tes écrans prennent vie** | Écrans d’affichage<br>`ecrans-affichage` | Display › Écrans d'affichage<br>🎬 Compte de démonstration (pas l'école). | ☐ | ☐ |
| 052 [📁](https://drive.google.com/drive/folders/1zK0ZkPkjz9RuU1V59YHyfdWIVeS3gaZk) | **Tes écrans rapportent** | Régie publicitaire<br>`regie-publicitaire` | Display › Régie publicitaire | ☐ | ☐ |
| 053 [📁](https://drive.google.com/drive/folders/1KhpsxhaB51S1WR7dQVhe73-q9D5nUsB6) | **Aucun écran éteint** | Supervision des écrans<br>`supervision-ecrans` | Display › Supervision des écrans | ☐ | ☐ |
| 054 [📁](https://drive.google.com/drive/folders/1EUEWajvuVAO4bgM61gOdSCZBT5xrFs-p) | **Ta borne de commande** | Bornes & tablettes<br>`bornes-tablettes` | Display › Bornes & tablettes<br>🎬 Compte de démonstration (pas l'école). | ☐ | ☐ |
| 055 [📁](https://drive.google.com/drive/folders/1dU_bADfu0owfxuzsWcIQF3kxWRzGt7fW) | **Le menu sur la table** | Menu digital & QR de table<br>`menu-digital-qr-table` | Display › Menu digital & QR de table | ☐ | ☐ |
| 056 [📁](https://drive.google.com/drive/folders/12HCvLrZLcntlN0pRa6zq4v2DHSfZDwQr) | **Le menu sur tablette** | L'application Menu digital sur la table<br>`application-menu-digital-tablette` | Application Menu digital + Menu digital & QR **(fiche à créer)**<br>🎬 Compte de démonstration (pas l'école). | ☐ | ☐ |
| 057 [📁](https://drive.google.com/drive/folders/17VgrkcTu_hwlZ2IKj_2u3OM4ujy7sDPa) | **Jouez en attendant** | Jeux de table entre tablettes et cadeaux fidélité<br>`jeux-de-table-tablette` | Marketing › Fidélité & Jeux › Jeux de table **(fiche à créer)** | ☐ | ☐ |

### marketing-fidelite (20) — [dossier Drive](https://drive.google.com/drive/folders/1gG_osjJJpAMeM-20wSPEj4TG41OovE6k)

| N° | Titre de la vignette (Zied) | Fiche / slug | Où tourner (Mouna) | Rush | Vignette |
|---|---|---|---|---|---|
| 058 [📁](https://drive.google.com/drive/folders/1-1di4rgV45bggq2DA6i_EJxjDYlCvCAj) | **Newsletters qui remplissent** | Newsletters & e-mails<br>`newsletters-emails` | Marketing et communication › Email & Newsletters | ☐ | ☐ |
| 059 [📁](https://drive.google.com/drive/folders/1FI3PXMX9pdAlK16UbO_CGoCTgXUM_2j9) | **Flyers et QR pros** | Supports imprimés & QR<br>`supports-imprimes-qr` | Marketing et communication › Supports imprimés & QR | ☐ | ☐ |
| 060 [📁](https://drive.google.com/drive/folders/1MWofJn8zfB_veEcRwgKBgXujLtwudoaz) | **Les enfants adorent** | Menu enfant & jeux<br>`menu-enfant-jeux` | Marketing et communication › Menu enfant & jeux | ☐ | ☐ |
| 061 [📁](https://drive.google.com/drive/folders/1hvRukrgtOqJtAtotVCYK9gYqkSf51t9m) | **Ton post pro en 2 min** | Iris — créer un post<br>`iris-creer-post` | Service › Iris › Créer | ☐ | ☐ |
| 062 [📁](https://drive.google.com/drive/folders/16r-bsc7VgcK6r2_legT0_kj5wUOHK_xe) | **Ton post a rapporté ?** | Iris — ROI<br>`iris-roi` | Service › Iris › Publications (ROI) | ☐ | ☐ |
| 063 [📁](https://drive.google.com/drive/folders/18o5u_YlKfPvJuCkffKpm2nxSqN3xYMDg) | **Tes réseaux reliés** | Supports marketing : liens et réseaux sociaux<br>`supports-marketing-reseaux-sociaux` | Configuration boutique › Supports marketing | ☐ | ☐ |
| 064 [📁](https://drive.google.com/drive/folders/18I4e-mSzEO04Ndw65HR-xzzOfPAmBhYr) | **Fidélité au comptoir** | La tablette fidélité au comptoir<br>`application-fidelite-comptoir` | Service › Bornes & tablettes (mode fidélité) **(fiche à créer)** | ☐ | ☐ |
| 065 [📁](https://drive.google.com/drive/folders/1Pitho17-np8H_8U7b8tYaUnz9G5vey8Q) | **6 jeux, 1 tirage honnête** | Six jeux : roue, grattage, dé, machine à sous, pile ou face, boîtes<br>`jeux-fidelite-six-jeux` | Marketing › Fidélité & Jeux › Créer un jeu **(fiche à créer)** | ☐ | ☐ |
| 066 [📁](https://drive.google.com/drive/folders/1t9b00FbZ_2TgYdZEh9VUk7CImdniStHO) | **Ton code promo maison** | Créer ses codes promo<br>`codes-promo-du-restaurant` | Newsletters & e-mails › Codes promo **(fiche à créer)** | ☐ | ☐ |
| 067 [📁](https://drive.google.com/drive/folders/1a4PigyaMull2eWazKfHJ_RhV9EJcM-tT) | **Les e-mails partent seuls** | Automatisations e-mail : panier, anniversaire, avis<br>`emails-automatisations-par-etapes` | Newsletters & e-mails › Automatisations **(fiche à créer)** | ☐ | ☐ |
| 068 [📁](https://drive.google.com/drive/folders/1qA8OuADcJgRltfDFeQ16KToIUqS0Q5aI) | **Tout sur ton client** | La fiche client 360 : achats, messages, consentements<br>`fiche-client-360` | Clients › fiche client **(fiche à créer)** | ☐ | ☐ |
| 069 [📁](https://drive.google.com/drive/folders/1Esc9gRHd2Uu991Mr0GuIZggfIVSPpGNi) | **Ta pub vidéo, montée seule** | Iris — monter une vidéo avec voix off<br>`iris-monter-une-video` | Service › Iris › étape 5 › Monter la vidéo **(fiche à créer)** | ☐ | ☐ |
| 070 [📁](https://drive.google.com/drive/folders/1KhIH0R7_Rjra2AzzFiFwMubMsnPdxc2G) | **Ta vidéo IA Google** | Iris — préparer sa vidéo avec Google Flow<br>`iris-kit-video-google` | Service › Iris › Kit vidéo **(fiche à créer)** | ☐ | ☐ |
| 071 [📁](https://drive.google.com/drive/folders/1YteOjJT7MM_VCOoF7g88C-nRAhw4rf9F) | **Remplis ton mardi** | Iris — packs « remplir le creux » et anti-gaspi<br>`iris-packs-creux-anti-gaspi` | Service › Iris › Opportunités **(fiche à créer)** | ☐ | ☐ |
| 072 [📁](https://drive.google.com/drive/folders/1cxWKaB0232foOLzWE9E1d9iT6ltOOjiy) | **1 visuel, 5 canaux** | Iris — diffuser un visuel partout<br>`iris-diffuser-partout` | Service › Iris › Mes visuels › Diffuser **(fiche à créer)** | ☐ | ☐ |
| 073 [📁](https://drive.google.com/drive/folders/1byTZTr0jcNne9UjoZnip3wuAq7LYMoXZ) | **Ton mois de posts prêt** | Iris — le mois de publications proposé<br>`iris-mois-propose` | Service › Iris › Calendrier **(fiche à créer)** | ☐ | ☐ |
| 074 [📁](https://drive.google.com/drive/folders/1AiK6rGBiTFhD-LEpJfRBoQBzhKL23Gag) | **Une BD à ton nom** | Menu enfant — créer une bande dessinée<br>`menu-enfant-bande-dessinee` | Marketing › Menu enfant & jeux › Bande dessinée **(fiche à créer)** | ☐ | ☐ |
| 075 [📁](https://drive.google.com/drive/folders/1R3-tKJQ2NsWcxRHp_lsZN4qkbsJeA-nq) | **Qui est-ce ? à table** | Menu enfant — le jeu « Qui est-ce ? » à deux téléphones<br>`menu-enfant-qui-est-ce` | Menu enfant & jeux › chevalet Qui est-ce ? **(fiche à créer)** | ☐ | ☐ |
| 076 [📁](https://drive.google.com/drive/folders/1MTYk0dAaIvSSNfxrAoyKAv2Ap7NnGEES) | **Emballages livrés** | Commander ses emballages à emporter<br>`commander-ses-emballages` | Supports imprimés & QR › Emballages **(fiche à créer)** | ☐ | ☐ |
| 077 [📁](https://drive.google.com/drive/folders/1UFsam2b4YtXq1FsqfPsR4Zgv7nQWZlVP) | **Ta boîte pizza déguisée** | Le couvercle costume de boîte à pizza<br>`couvercle-costume-pizza` | Supports imprimés › Couvercle costume **(fiche à créer)** | ☐ | ☐ |

### configuration (7) — [dossier Drive](https://drive.google.com/drive/folders/17C2VbHPKtzIeSpPnMxRDnvksZwSfIni5)

| N° | Titre de la vignette (Zied) | Fiche / slug | Où tourner (Mouna) | Rush | Vignette |
|---|---|---|---|---|---|
| 078 [📁](https://drive.google.com/drive/folders/1oQnBrmwAexismkr1Mrr8a5F_Wb7r5RMX) | **Une marque partout** | Ma marque<br>`ma-marque` | Configuration boutique › Ma marque | ☐ | ☐ |
| 079 [📁](https://drive.google.com/drive/folders/1Tr4V2U7De-Fb3ZlNxw1w8IdSlJYGufJ7) | **Docs pro en 1 clic** | Documents pro<br>`documents-pro` | Configuration boutique › Documents pro | ☐ | ☐ |
| 080 [📁](https://drive.google.com/drive/folders/1l1yPzS2okiYXLHvNoXQj8ngfcsNjtTP3) | **Tes recettes sur tablette** | Application Recettes — appairer une tablette<br>`application-recettes-tablette` | Configuration boutique › Application Recettes | ☐ | ☐ |
| 081 [📁](https://drive.google.com/drive/folders/1mN32qgD1nz6otoDLuynq5GxA7BFe9NUY) | **Ton logiciel verrouillé** | Sécurité & accès<br>`securite-acces` | Configuration boutique › Sécurité & accès | ☐ | ☐ |
| 082 [📁](https://drive.google.com/drive/folders/1e5Ie2fs4-Yxy7zVLZY68Z_9TchSmsh59) | **2e resto sans ressaisir** | Reprises de configuration<br>`reprises-configuration` | Configuration boutique › Reprises de configuration | ☐ | ☐ |
| 083 [📁](https://drive.google.com/drive/folders/106GKldvkIgD_oF5zsqpgVtBx7wthujyV) | **Ton resto prêt en 41 étapes** | Premiers pas — parcours en 18 étapes<br>`premiers-pas-18-etapes` | Configuration › Premiers pas (41 étapes)<br>⚠ Le parcours compte 41 étapes : corriger le titre de la fiche avant de tourner. | ☐ | ☐ |
| 084 [📁](https://drive.google.com/drive/folders/1aiYRpHv9D5sU57-X_vT0GHTE1qsrOq7S) | **Tes factures FoodEatUp** | Ses factures FoodEatUp et son adresse de facturation<br>`facturation-abonnement` | Abonnement › Facturation **(fiche à créer)** | ☐ | ☐ |

### assistant-foodeatup (6) — [dossier Drive](https://drive.google.com/drive/folders/1K9BjyEwzlzF2uQQIC_qTqX5C3gIrHSWF)

| N° | Titre de la vignette (Zied) | Fiche / slug | Où tourner (Mouna) | Rush | Vignette |
|---|---|---|---|---|---|
| 085 [📁](https://drive.google.com/drive/folders/1abv4RrdH8B37EB9f4ByizBEYkq6b2cuz) | **Le Chef t'explique tout** | Le Chef — Comprendre / Apprendre / Agir<br>`chef-comprendre-apprendre-agir` | Bouton du Chef (bas à droite) | ☐ | ☐ |
| 086 [📁](https://drive.google.com/drive/folders/13ovuG6gdvGggVVjOtMThypgkGQecmmHm) | **Règle ton assistant** | Mon profil › Assistant<br>`mon-profil-assistant` | Mon profil › Assistant | ☐ | ☐ |
| 087 [📁](https://drive.google.com/drive/folders/1rDLNjuU4vOMxs2i6Nspl5N3ZoKN7nSfO) | **Entraîne-toi sans risque** | Le mode école : s'entraîner sur un restaurant fictif<br>`mode-ecole-restaurant-fictif` | Configuration boutique › Mode école | ☐ | ☐ |
| 088 [📁](https://drive.google.com/drive/folders/1F_mEAF5dFlWdQf9aSZf3XQywKvugvaw1) | **Jarvis te suit partout** | Jarvis — appairer par QR et le garder sur tous les écrans<br>`jarvis-qr-et-compagnon` | Service › Jarvis — sièges & appairage + Mon espace › Jarvis **(fiche à créer)**<br>⚠ Tourner sur le compte de démonstration : un appairage crée un siège Jarvis facturé (interdit dans l'école). | ☐ | ☐ |
| 089 [📁](https://drive.google.com/drive/folders/1Wb1HiDjEjTfdeC2PxjchZSkenZfibyaw) | **Le Chef répond pour de vrai** | Le Chef — la réponse de l'IA et les crédits<br>`chef-reponse-ia-credits` | Chef › bouton « Réponse de l'IA » **(fiche à créer)** | ☐ | ☐ |
| 090 [📁](https://drive.google.com/drive/folders/1CJRWFaejyodjPjl0vIvKbrkzLUEVR2DP) | **Gagne tes missions** | Mode école — les missions et le quiz<br>`mode-ecole-missions` | Configuration › Mode école **(fiche à créer)** | ☐ | ☐ |

### comptabilite (4) — [dossier Drive](https://drive.google.com/drive/folders/1RIAGadpTAWOrQJwes-ZuLw5r4UGZ9E7z)

| N° | Titre de la vignette (Zied) | Fiche / slug | Où tourner (Mouna) | Rush | Vignette |
|---|---|---|---|---|---|
| 091 [📁](https://drive.google.com/drive/folders/1gV2Z9Izh0Q8NR1LedcFEBlACNDE4KIj6) | **Ton resto en 4 chiffres** | Tableau de bord financier<br>`tableau-bord-financier` | Finance › Tableau de bord financier | ☐ | ☐ |
| 092 [📁](https://drive.google.com/drive/folders/1HEQuaixuZ4cJWUe44roXurz0QMq_Gu_i) | **50 factures à ton image** | Modèles & apparence des factures et devis<br>`modeles-apparence-factures-devis` | Finance › Modèles & apparence | ☐ | ☐ |
| 093 [📁](https://drive.google.com/drive/folders/1ALDugohCbflCEfxKxHopmd09ar1vlq-w) | **Relance = payé** | Paiement en ligne et relance depuis la fiche client<br>`paiement-relance-fiche-client` | Clients › fiche › Factures & devis | ☐ | ☐ |
| 094 [📁](https://drive.google.com/drive/folders/1Ntus7m7p0lX4rSclIUbXLTyGXNhDg_V9) | **La facturation de A à Z** | Facturation : la documentation détaillée<br>`doc-facturation-detaillee` | Finance › Factures et Devis | ☐ | ☐ |

### haccp (4) — [dossier Drive](https://drive.google.com/drive/folders/1A1rwuOK_sySi4u1pHhQcov0zEilu3ld4)

| N° | Titre de la vignette (Zied) | Fiche / slug | Où tourner (Mouna) | Rush | Vignette |
|---|---|---|---|---|---|
| 095 [📁](https://drive.google.com/drive/folders/1ZCC1E8V3c6akzKnSDa_IiYh_fgwd3S-v) | **Refroidir sans risque** | Cycles thermiques — refroidissement et remise en température<br>`cycles-thermiques` | Haccp › Cycles thermiques | ☐ | ☐ |
| 096 [📁](https://drive.google.com/drive/folders/16zpJerIvFL27FuDlx1UaQpSAv5BJZqa-) | **Ton huile sous contrôle** | Friteuses & huile — tests polaires<br>`friteuses-huile` | Haccp › Friteuses & huile | ☐ | ☐ |
| 097 [📁](https://drive.google.com/drive/folders/1Lb4yg7NHq2AahvZ-J0x1GWTkRHHk-pg6) | **Ton HACCP réglé** | Paramètres HACCP<br>`parametres-haccp` | Haccp › Paramètres HACCP<br>Cet écran active/désactive les modules HACCP (pas les seuils). | ☐ | ☐ |
| 098 [📁](https://drive.google.com/drive/folders/1YKtzACFXcUVq7sy2QxpriIRzavSvYr69) | **HACCP dans la poche** | L'application HACCP sur téléphone<br>`application-haccp-mobile` | Application FoodEatUp HACCP (téléphone) **(fiche à créer)** | ☐ | ☐ |

### stockvision-ai (2) — [dossier Drive](https://drive.google.com/drive/folders/1tlNRsETDZChRJBB8_rwPAwdbrnMovRKH)

| N° | Titre de la vignette (Zied) | Fiche / slug | Où tourner (Mouna) | Rush | Vignette |
|---|---|---|---|---|---|
| 099 [📁](https://drive.google.com/drive/folders/1_gkVQ4aEi0oAU9QF32PuurMH0dc-Uasj) | **Épuisé tout seul** | Portions — compteur et rupture automatique<br>`portions-rupture-automatique` | StockVisionAI › Portions | ☐ | ☐ |
| 100 [📁](https://drive.google.com/drive/folders/1qp8pc7gvREEKE3Ra6afQMK0jAPx7vxW7) | **Commande fournisseur en 2 min** | Cadencier<br>`cadencier` | StockVisionAI › Cadencier | ☐ | ☐ |

### equipe-planning (1) — [dossier Drive](https://drive.google.com/drive/folders/1XUzSHxLkYPnBQu9QTqiggjIdFpKDaug0)

| N° | Titre de la vignette (Zied) | Fiche / slug | Où tourner (Mouna) | Rush | Vignette |
|---|---|---|---|---|---|
| 101 [📁](https://drive.google.com/drive/folders/1kAYxoNzKY0fzCJGvVwLsSs4B1EZnI3cO) | **Paie sans erreur** | Variables de paie<br>`variables-paie` | Equipe › Variables de paie | ☐ | ☐ |

### site-web-vitrine (4) — [dossier Drive](https://drive.google.com/drive/folders/1cJGglEFLUoPXTYKvO2-uLYQDZvjqkiHf)

| N° | Titre de la vignette (Zied) | Fiche / slug | Où tourner (Mouna) | Rush | Vignette |
|---|---|---|---|---|---|
| 102 [📁](https://drive.google.com/drive/folders/1xv62mRpasVv_Roopkzlt0sUDibNHxlLK) | **Ton blog qui attire** | Blog & recettes<br>`blog-recettes` | Mon Site › Blog & recettes | ☐ | ☐ |
| 103 [📁](https://drive.google.com/drive/folders/1b3bLhhN5Ff8LZP8JnyZd9JQbBKfdSTkv) | **Un site comme un film** | Site cinématique<br>`site-cinematique` | Mon Site › Site cinématique | ☐ | ☐ |
| 104 [📁](https://drive.google.com/drive/folders/1mN7kPdlZzd8inEVb2HVyB_tyjmR6YinF) | **Mets tes stars en avant** | Placement de la carte — vitrine et site<br>`placement-carte-vitrine-site` | Ma vitrine › Carte & placement | ☐ | ☐ |
| 105 [📁](https://drive.google.com/drive/folders/1nT6fomgBgSKRihM5-pyKmHc84BfDcXdL) | **Ton thème en 1 phrase** | Créer un thème de site avec l'IA<br>`site-themes-ia` | Mon Site › Templates & IA › Mon thème **(fiche à créer)** | ☐ | ☐ |

### caroline-ia (1) — [dossier Drive](https://drive.google.com/drive/folders/1GOVA5IzT-pEpcTyJkAK8iAumW4F3fdBN)

| N° | Titre de la vignette (Zied) | Fiche / slug | Où tourner (Mouna) | Rush | Vignette |
|---|---|---|---|---|---|
| 106 [📁](https://drive.google.com/drive/folders/1Nv-3oPlYzde4MBnOlM7FTgQWwv3B6Rzj) | **Caroline te passe l'appel** | Transfert vers un humain<br>`caroline-transfert-humain` | Agent IA › Configuration Voix › Transfert | ☐ | ☐ |

### predibot (2) — [dossier Drive](https://drive.google.com/drive/folders/1J5dHdbQfcFwGThPTa8QSXRk_EG6VupPG)

| N° | Titre de la vignette (Zied) | Fiche / slug | Où tourner (Mouna) | Rush | Vignette |
|---|---|---|---|---|---|
| 107 [📁](https://drive.google.com/drive/folders/1ffoZ0yvD1IzuAE977FGt5TwTGx9Gg8VL) | **Le bon staff au bon jour** | Prévisions RH<br>`previsions-rh` | PrediBot › Prévisions RH<br>⛔ NE PAS TOURNER : l'écran PrediBot › Prévisions RH affiche « bientôt disponible ». | ☐ | ☐ |
| 108 [📁](https://drive.google.com/drive/folders/1GQ5iL82nm-vtYnTh3TXGpE1Qf77n-EAu) | **L'IA veille ton HACCP** | Conformité HACCP IA<br>`conformite-haccp-ia` | PrediBot › Conformité HACCP IA<br>⚠ Certains badges de la page sont écrits en dur : ne pas les présenter comme de vraies données. | ☐ | ☐ |

### api-developpeurs (7) — [dossier Drive](https://drive.google.com/drive/folders/1a9G0Yo44lrTEtgGVVAjXjQGMxJbgMVOE)

| N° | Titre de la vignette (Zied) | Fiche / slug | Où tourner (Mouna) | Rush | Vignette |
|---|---|---|---|---|---|
| 109 [📁](https://drive.google.com/drive/folders/10c9KoldwQpGjTWasfvjVEqiJSuagZ025) | **Une seule porte, tous les outils** | L'API FoodEatUp : les outils du catalogue courant derrière une seule porte<br>`documentation-api-foodeatup` | Page publique /tutoriels (doc API) | ☐ | ☐ |
| 110 [📁](https://drive.google.com/drive/folders/1titmMXqSd87l0ClcTtJg_Ts1iKOPP9Eo) | **Ta clé API en 1 minute** | Créer sa clé API et obtenir un jeton<br>`creer-sa-cle-api-foodeatup` | Mon profil › API Clients | ☐ | ☐ |
| 111 [📁](https://drive.google.com/drive/folders/1c2Pji03eIHdwfP44F6ScigfQC8B2W9gd) | **Ton premier appel API** | Son premier appel : lister et appeler un outil<br>`premier-appel-api-foodeatup` | /tutoriels › Tester ma clé | ☐ | ☐ |
| 112 [📁](https://drive.google.com/drive/folders/1bVKm05NaZgY8jd3mDPUd6TLNe81G7pxP) | **Ton resto en pilote auto** | Automatiser son restaurant avec n8n, Make ou un agent IA<br>`automatiser-avec-l-api-foodeatup` | n8n ou Claude + clé API | ☐ | ☐ |
| 113 [📁](https://drive.google.com/drive/folders/1ktsRC9bWavCgjiMabMen1thZ27Tn5Jnx) | **Ton IA préférée branchée** | Connecter ChatGPT, Le Chat ou Grok à son restaurant<br>`connecter-chatgpt-le-chat-grok` | Marketplace de prompts › Connecter un assistant **(fiche à créer)** | ☐ | ☐ |
| 114 [📁](https://drive.google.com/drive/folders/1LHxy8Yk9hCpYh1i6RugOEGuJaJOj7ClX) | **Le plugin Claude** | Installer le plugin FoodEatUp pour Claude<br>`plugin-claude-foodeatup` | Page publique /plugin-claude **(fiche à créer)** | ☐ | ☐ |
| 115 [📁](https://drive.google.com/drive/folders/1G5orkPG7A361G9Usq3417XCNRV5RPHdV) | **Ton IA, tes droits** | Brancher son assistant IA côté employé<br>`assistant-ia-employe` | Réglages › Intégrations › Assistant IA (adresse employé) **(fiche à créer)** | ☐ | ☐ |

### reseau-franchise (12) — [dossier Drive](https://drive.google.com/drive/folders/1k1RLgqkR0vXU1ojJBI0YLivFQElgwjpE)

| N° | Titre de la vignette (Zied) | Fiche / slug | Où tourner (Mouna) | Rush | Vignette |
|---|---|---|---|---|---|
| 116 [📁](https://drive.google.com/drive/folders/1Cp71HyyNTECfHR98iURNyuPzkUNHTlw7) | **Tout ton réseau, 1 écran** | Accueil siège<br>`accueil-siege` | Siège › Accueil siège<br>🎬 Démo réseau (`php artisan reseau:demo`, modules réseau allumés). | ☐ | ☐ |
| 117 [📁](https://drive.google.com/drive/folders/1h4OuFEzyi7Ot50UGNemN2lEsaDTbNz0D) | **Tes boutiques notées** | Boutiques<br>`boutiques-reseau` | Siège › Boutiques<br>🎬 Démo réseau (`php artisan reseau:demo`, modules réseau allumés). | ☐ | ☐ |
| 118 [📁](https://drive.google.com/drive/folders/1KQWELQZ7oLkCxGvqCNTMth8fvQG9XdtT) | **Qui fait mieux ?** | Comparatif<br>`comparatif-reseau` | Siège › Comparatif des boutiques<br>🎬 Démo réseau (`php artisan reseau:demo`, modules réseau allumés). | ☐ | ☐ |
| 119 [📁](https://drive.google.com/drive/folders/1bLXuWfc2qoma-AJNZZOKcbN1ChW9GSm-) | **Le staff de tout le réseau** | RH du réseau<br>`rh-reseau` | Siège › RH du réseau<br>🎬 Démo réseau (`php artisan reseau:demo`, modules réseau allumés). | ☐ | ☐ |
| 120 [📁](https://drive.google.com/drive/folders/10YH6YUGF456xgu7AAqH-NuObR6UWsayS) | **La paie du réseau** | Collecte RH & paie<br>`collecte-rh-paie-reseau` | Siège › Collecte RH & paie<br>🎬 Démo réseau (`php artisan reseau:demo`, modules réseau allumés). | ☐ | ☐ |
| 121 [📁](https://drive.google.com/drive/folders/1uQ1ct2yaXZwDmVTn8fjMXvehRL7ct0K_) | **Compta réseau en ordre** | Comptabilité & banque<br>`comptabilite-banque-reseau` | Siège › Comptabilité & banque<br>🎬 Démo réseau (`php artisan reseau:demo`, modules réseau allumés). | ☐ | ☐ |
| 122 [📁](https://drive.google.com/drive/folders/165tumlGH0FbLIk312aTJG3pb8V7PpAcR) | **Les vrais KPI du réseau** | KPI du réseau<br>`kpi-reseau` | Siège › KPI du réseau<br>🎬 Démo réseau (`php artisan reseau:demo`, modules réseau allumés). | ☐ | ☐ |
| 123 [📁](https://drive.google.com/drive/folders/1Ik1nxEUTq9KqTpGZMBUU4jPE04rmeKpX) | **Une carte pour tout le réseau** | Catalogue central<br>`catalogue-central` | Siège › Catalogue central<br>🎬 Démo réseau (`php artisan reseau:demo`, modules réseau allumés). | ☐ | ☐ |
| 124 [📁](https://drive.google.com/drive/folders/1TFP_vVNCiF5HDf_fw5j_vJqFSw675nBJ) | **Les prix du siège** | Prix du siège<br>`prix-siege` | StockVisionAI › Prix du siège<br>🎬 Démo réseau (`php artisan reseau:demo`, modules réseau allumés). | ☐ | ☐ |
| 125 [📁](https://drive.google.com/drive/folders/1pGmitcTpVzCZoS3_9EyATUg_2H2HsAo9) | **Achète groupé, paie moins** | Achats centralisés<br>`achats-centralises` | Siège › Achats centralisés<br>🎬 Démo réseau (`php artisan reseau:demo`, modules réseau allumés). | ☐ | ☐ |
| 126 [📁](https://drive.google.com/drive/folders/1GWxFFOH6EeMc696W8RqIXgsK1VVtH731) | **Règle ton réseau** | Configuration du réseau<br>`configuration-reseau` | Siège › Configuration du réseau<br>🎬 Démo réseau (`php artisan reseau:demo`, modules réseau allumés). | ☐ | ☐ |
| 127 [📁](https://drive.google.com/drive/folders/1oV_gF3PRAq4h_EC32Wjh0xOy6NjwAg0x) | **Siège, labo, boutiques** | Entités & topologie<br>`entites-topologie` | Siège › Entités & topologie<br>🎬 Démo réseau (`php artisan reseau:demo`, modules réseau allumés). | ☐ | ☐ |

### laboratoire-livraison (10) — [dossier Drive](https://drive.google.com/drive/folders/1GVRMzz4TIuJUDox19ijEJM4BePuprFTg)

| N° | Titre de la vignette (Zied) | Fiche / slug | Où tourner (Mouna) | Rush | Vignette |
|---|---|---|---|---|---|
| 128 [📁](https://drive.google.com/drive/folders/1PqjirRn0GhD--EuRuq876vXAKZzvx_HP) | **Commande au labo** | Commander au laboratoire<br>`commander-laboratoire` | StockVisionAI › Commander au laboratoire<br>🎬 Démo réseau (`php artisan reseau:demo`, modules réseau allumés). | ☐ | ☐ |
| 129 [📁](https://drive.google.com/drive/folders/1pTUuPaaYDQ0fulqiG1VsG5oDht3gGr77) | **Toutes les commandes boutiques** | Commandes des boutiques<br>`commandes-boutiques-laboratoire` | StockVisionAI › Commandes des boutiques<br>🎬 Démo réseau (`php artisan reseau:demo`, modules réseau allumés). | ☐ | ☐ |
| 130 [📁](https://drive.google.com/drive/folders/1AiBPolHLReajVwLhIa-8Wzf_0ifKInL9) | **Atelier jamais saturé** | Planning d’atelier<br>`planning-atelier` | StockVisionAI › Planning d'atelier<br>🎬 Démo réseau (`php artisan reseau:demo`, modules réseau allumés). | ☐ | ☐ |
| 131 [📁](https://drive.google.com/drive/folders/1S5Ys7UW2xfe339KQkn-mMXfwVNLG5zYS) | **La fabrication du jour** | Fabrication du jour<br>`fabrication-jour` | StockVisionAI › Fabrication du jour<br>🎬 Démo réseau (`php artisan reseau:demo`, modules réseau allumés). | ☐ | ☐ |
| 132 [📁](https://drive.google.com/drive/folders/1X-ZHfXsVcTuVsWC5ylv0YurQoQI37GlG) | **Rappel de lot en 60 s** | Stock produits finis & rappel de lot<br>`stock-finis-rappel-lot` | StockVisionAI › Stock produits finis & rappel<br>🎬 Démo réseau (`php artisan reseau:demo`, modules réseau allumés). | ☐ | ☐ |
| 133 [📁](https://drive.google.com/drive/folders/1eyIOX3dqh9-XvntoOFq_gyhHx0spB9pH) | **Colis sans oubli** | Préparation & colis<br>`preparation-colis` | StockVisionAI › Préparation & colis<br>🎬 Démo réseau (`php artisan reseau:demo`, modules réseau allumés). | ☐ | ☐ |
| 134 [📁](https://drive.google.com/drive/folders/1G_LEiVNOal9bJ3Yk_3t9oQVTmLppB90e) | **L'appli du chauffeur** | Tournées de livraison — application chauffeur<br>`tournees-application-chauffeur` | StockVisionAI › Tournées de livraison<br>🎬 Démo réseau (`php artisan reseau:demo`, modules réseau allumés). | ☐ | ☐ |
| 135 [📁](https://drive.google.com/drive/folders/1VwatABWNXyOhctXAUBIgZgjkD1OOJnVN) | **Réception en 1 minute** | Réceptions du laboratoire<br>`receptions-laboratoire` | StockVisionAI › Réceptions du laboratoire<br>🎬 Démo réseau (`php artisan reseau:demo`, modules réseau allumés). | ☐ | ☐ |
| 136 [📁](https://drive.google.com/drive/folders/1q57LAPrNv4dYn00uDwGUe1ahTRepdg-M) | **Ton labo vu du siège** | Suivre ses laboratoires depuis le siège<br>`hub-laboratoire-siege` | Siège › Laboratoires<br>🎬 Démo réseau (`php artisan reseau:demo`, modules réseau allumés). | ☐ | ☐ |
| 137 [📁](https://drive.google.com/drive/folders/1nghIX80rsXmLiNY-fCmOHwTVN1NLzN4M) | **Tes livraisons en direct** | Suivre les livraisons du réseau depuis le siège<br>`hub-livraison-siege` | Siège › Livraison<br>🎬 Démo réseau (`php artisan reseau:demo`, modules réseau allumés). | ☐ | ☐ |

### foodeatup-live (5) — [dossier Drive](https://drive.google.com/drive/folders/1tbNho13GK9NjYXkNiAysTaVw6svKbmvb)

| N° | Titre de la vignette (Zied) | Fiche / slug | Où tourner (Mouna) | Rush | Vignette |
|---|---|---|---|---|---|
| 138 [📁](https://drive.google.com/drive/folders/1pAy5DllBdmhhG43HFZLi_JVkPZHHRhoA) | **Zéro cash au bar** | Portefeuille cashless<br>`live-portefeuille-cashless` | Display › FoodEatUp Live<br>🎬 Live allumé ; ne jamais filmer le NFC comme fonctionnel. | ☐ | ☐ |
| 139 [📁](https://drive.google.com/drive/folders/1sgxAbQNzeTXTfenjpF1RCiDlCOkxUf9D) | **Paie en montrant un QR** | QR de paiement<br>`live-qr-paiement` | Display › FoodEatUp Live<br>🎬 Live allumé ; ne jamais filmer le NFC comme fonctionnel. | ☐ | ☐ |
| 140 [📁](https://drive.google.com/drive/folders/1d_IPge-KDWl2jf-EE5CI2vpfOkrg7Aqm) | **Recharge en 10 s** | Recharges<br>`live-recharges` | Display › FoodEatUp Live<br>🎬 Live allumé ; ne jamais filmer le NFC comme fonctionnel. | ☐ | ☐ |
| 141 [📁](https://drive.google.com/drive/folders/1Ez0STw2cfBa_g6lB19iGLVXGeORcqBjK) | **Bracelet = portefeuille** | Bracelets NFC<br>`live-bracelets-nfc` | Display › FoodEatUp Live<br>🎬 Live allumé ; ne jamais filmer le NFC comme fonctionnel. | ☐ | ☐ |
| 142 [📁](https://drive.google.com/drive/folders/1uYjfSOJXZ_jWp2cnnp_SvNXHv-uc1ypQ) | **Ton festival en ligne** | FoodEatUp Live : créer et ouvrir un événement<br>`live-creer-un-evenement` | Display › FoodEatUp Live<br>🎬 Live allumé ; ne jamais filmer le NFC comme fonctionnel. | ☐ | ☐ |

### store-foodeatup (3) — [dossier Drive](https://drive.google.com/drive/folders/1OR-eUclAvpVthmibkGaq5t_OmZsogFKL)

| N° | Titre de la vignette (Zied) | Fiche / slug | Où tourner (Mouna) | Rush | Vignette |
|---|---|---|---|---|---|
| 143 [📁](https://drive.google.com/drive/folders/1Ibi-C18jElN0aFTH5VSCWKav36ubsJVt) | **Le Store FoodEatUp** | Trouver une application<br>`store-trouver-application` | Menu profil › Boutiques › Store | ☐ | ☐ |
| 144 [📁](https://drive.google.com/drive/folders/1rKjcUZfTTys_Eg8NH1WNRK0gZO2G1Nv8) | **Tes applis favorites** | Favoris<br>`store-favoris` | Store › cœur sur une fiche › Mes favoris | ☐ | ☐ |
| 145 [📁](https://drive.google.com/drive/folders/1bnNpEmPrzMkcX1b7b-Amvbg1OJAgCGVB) | **Installer un APK** | Installer un APK — hors Google Play<br>`store-installer-apk` | Store › fiche Recettes › Télécharger l'APK (téléphone Android) | ☐ | ☐ |

### client-restaurant (10) — [dossier Drive](https://drive.google.com/drive/folders/1XuwjdEFOINcsJQXmT9GKnGR87sDR3R4K)

| N° | Titre de la vignette (Zied) | Fiche / slug | Où tourner (Mouna) | Rush | Vignette |
|---|---|---|---|---|---|
| 146 [📁](https://drive.google.com/drive/folders/17_a3hqF73Ormq2prPDuLh8nh52YsinbC) | **La carte avant d'y aller** | Trouver le restaurant et voir la carte en ligne<br>`trouver-le-restaurant-et-voir-la-carte` | téléphone, côté client (site public, QR de table, page fidélité) | ☐ | ☐ |
| 147 [📁](https://drive.google.com/drive/folders/1LRegeHRlaBZjtU0Uxo1Qz1zW4wtm1tDh) | **Commande en ligne** | Commander depuis le site du restaurant<br>`commander-depuis-le-site-du-restaurant` | téléphone, côté client (site public, QR de table, page fidélité) | ☐ | ☐ |
| 148 [📁](https://drive.google.com/drive/folders/1tglK0_HkwAbmcqKo4w7C2kgb65A_40jo) | **Commande depuis ta table** | Commander à table avec le QR code<br>`commander-a-table-avec-le-qr-code` | téléphone, côté client (site public, QR de table, page fidélité) | ☐ | ☐ |
| 149 [📁](https://drive.google.com/drive/folders/1iIkm9tkAkVABYFYa6NxHF15ksWh3tPYV) | **Paie, reçu par mail** | Payer sa commande et recevoir son reçu<br>`payer-sa-commande-et-recevoir-son-recu` | téléphone, côté client (site public, QR de table, page fidélité) | ☐ | ☐ |
| 150 [📁](https://drive.google.com/drive/folders/1yJ6wPTSEK6SJ1iw_mTDyygyhuq_YES_q) | **Réserve ta table** | Réserver une table<br>`reserver-une-table` | téléphone, côté client (site public, QR de table, page fidélité) | ☐ | ☐ |
| 151 [📁](https://drive.google.com/drive/folders/1vR189fZ4gIhGNJw22FGk-R9ADIJojQOV) | **Rejoins le club** | Rejoindre le programme de fidélité<br>`rejoindre-le-programme-de-fidelite` | téléphone, côté client (site public, QR de table, page fidélité) | ☐ | ☐ |
| 152 [📁](https://drive.google.com/drive/folders/1LJvlqT-d4GahXgGaYg_XffCl1aP30L-A) | **Chaque repas rapporte** | Cumuler ses points à chaque passage<br>`cumuler-ses-points-a-chaque-passage` | téléphone, côté client (site public, QR de table, page fidélité) | ☐ | ☐ |
| 153 [📁](https://drive.google.com/drive/folders/1E4XApsN1-OYAw0nEe-SXLqAoYrGPm_Rl) | **Utilise ta récompense** | Utiliser une récompense ou une offre<br>`utiliser-une-recompense-ou-une-offre` | téléphone, côté client (site public, QR de table, page fidélité) | ☐ | ☐ |
| 154 [📁](https://drive.google.com/drive/folders/1BkoX2ICOiwXdvH9Gm4SPw2RhHLXU3DcI) | **Les offres, sans spam** | Recevoir les offres du restaurant sans être submergé<br>`recevoir-les-offres-du-restaurant` | téléphone, côté client (site public, QR de table, page fidélité) | ☐ | ☐ |
| 155 [📁](https://drive.google.com/drive/folders/1UU45pLkyppOKuvuhkN8YQeuFCgqOWCGC) | **Ton avis en 20 s** | Laisser un avis après son passage<br>`laisser-un-avis-apres-son-passage` | téléphone, côté client (site public, QR de table, page fidélité) | ☐ | ☐ |

### reseau-partenaires (8) — [dossier Drive](https://drive.google.com/drive/folders/11AXrf6jQiFaQ3MdHuL6QzBSUa8SxWrb1)

| N° | Titre de la vignette (Zied) | Fiche / slug | Où tourner (Mouna) | Rush | Vignette |
|---|---|---|---|---|---|
| 156 [📁](https://drive.google.com/drive/folders/1Qq1h6Cjd5Qn64vuIceTbfVdCS4II4Sr7) | **Deviens partenaire** | Le réseau de partenaires<br>`reseau-partenaires-foodeatup` | face caméra + diapositives | ☐ | ☐ |
| 157 [📁](https://drive.google.com/drive/folders/1WQLfX_MUlyDsMOGX6NVLaykm7CRV_15m) | **Une journée de partenaire** | Une journée de partenaire, sur le terrain<br>`journee-type-partenaire-foodeatup` | face caméra + diapositives | ☐ | ☐ |
| 158 [📁](https://drive.google.com/drive/folders/1JB81gPtuxEcx83sS_Gm9eo9kf7Y9taTj) | **FoodEatUp en 5 minutes** | L'argumentaire FoodEatUp en cinq minutes<br>`argumentaire-foodeatup-cinq-minutes` | face caméra + diapositives | ☐ | ☐ |
| 159 [📁](https://drive.google.com/drive/folders/1sTZVMvqLlnVP64hDHKvobQP-rcDyem5b) | **Vends l'IA, pas un logiciel** | Vendre le passage à l'IA, pas un logiciel de plus<br>`vendre-le-passage-a-l-ia` | face caméra + diapositives | ☐ | ☐ |
| 160 [📁](https://drive.google.com/drive/folders/1fx0U8COtOPDiXxNOwAyDrVdXH5HRD-X4) | **Ton compte rendu** | Rédiger son compte rendu de mission<br>`compte-rendu-de-mission-partenaire` | face caméra + diapositives | ☐ | ☐ |
| 161 [📁](https://drive.google.com/drive/folders/1f9kt42s9hbdISBcKrywQvO8DuhTgxe9N) | **Tes commissions en direct** | Suivre ses ventes et ses commissions<br>`suivre-ses-ventes-et-commissions` | face caméra + diapositives | ☐ | ☐ |
| 162 [📁](https://drive.google.com/drive/folders/1Wzi8Ti2-cfYwfQ0LrLzt8mnIgcWgtAyE) | **Remonte le terrain** | Remonter les retours terrain à<br>`remonter-les-retours-terrain` | face caméra + diapositives | ☐ | ☐ |
| 163 [📁](https://drive.google.com/drive/folders/11FG44jeR3KYam2ULQbHU0orP_8nO3fWd) | **Après la mission** | Après la mission : suivi, commissions et fidélisation<br>`apres-la-mission-suivi-et-fidelisation` | face caméra + diapositives | ☐ | ☐ |

### partenaire-formateur (2) — [dossier Drive](https://drive.google.com/drive/folders/1jA6ULh9YxtBFnGeNOXaFvjGjTFHrGAF_)

| N° | Titre de la vignette (Zied) | Fiche / slug | Où tourner (Mouna) | Rush | Vignette |
|---|---|---|---|---|---|
| 164 [📁](https://drive.google.com/drive/folders/11cmnbYVePZ-AgpjL6hlsvYD63f8sSj3a) | **HACCP en 1 heure** | Former une brigade à l'HACCP en une heure<br>`former-une-brigade-a-l-haccp` | face caméra + diapositives | ☐ | ☐ |
| 165 [📁](https://drive.google.com/drive/folders/1SEpSF7Vrb8-8H1_9mCBzwTq_udVYcwK4) | **L'Académie prend le relais** | Passer le relais : l'Académie comme support<br>`passer-le-relais-academie` | face caméra + diapositives | ☐ | ☐ |

### partenaire-revendeur (2) — [dossier Drive](https://drive.google.com/drive/folders/1u3UY37lk9E3UfXn1XX0i41y8LSEvW5ip)

| N° | Titre de la vignette (Zied) | Fiche / slug | Où tourner (Mouna) | Rush | Vignette |
|---|---|---|---|---|---|
| 166 [📁](https://drive.google.com/drive/folders/1BJN-XmPl6Mo9KmnWdn-snYfl-cngX-E1) | **De la démo à la signature** | Conclure : de la démonstration à la signature<br>`de-la-demonstration-a-la-signature` | face caméra + diapositives | ☐ | ☐ |
| 167 [📁](https://drive.google.com/drive/folders/1XvcN2rU6IJgUw2ie8vI2CRTRSSR7uJAe) | **Le point à 30 jours** | Le point à 30 jours avec le client<br>`le-point-a-30-jours-avec-le-client` | face caméra + diapositives | ☐ | ☐ |

### partenaire-installateur (2) — [dossier Drive](https://drive.google.com/drive/folders/1BnkXGw-W--G2UmeY-ULXr1BEsZUveXi7)

| N° | Titre de la vignette (Zied) | Fiche / slug | Où tourner (Mouna) | Rush | Vignette |
|---|---|---|---|---|---|
| 168 [📁](https://drive.google.com/drive/folders/1WY85g-8VfKde1goEQloftQnL4WCCQry7) | **Installe une caisse** | Installer un poste de caisse<br>`installer-un-poste-de-caisse-foodeatup` | sur site, matériel réel (caisse, imprimante, TPE) | ☐ | ☐ |
| 169 [📁](https://drive.google.com/drive/folders/1Vo8KPYLujZtrjDU5ECYeGoNwekpnKKTW) | **Tout branché, tout marche** | Raccorder imprimante, tiroir et TPE<br>`raccorder-imprimante-tiroir-et-tpe` | sur site, matériel réel (caisse, imprimante, TPE) | ☐ | ☐ |

### partenaire-apporteur (2) — [dossier Drive](https://drive.google.com/drive/folders/1juEDEprp67ca4wrhJo76PvsVxdkvOeF6)

| N° | Titre de la vignette (Zied) | Fiche / slug | Où tourner (Mouna) | Rush | Vignette |
|---|---|---|---|---|---|
| 170 [📁](https://drive.google.com/drive/folders/1dI-XV2YK5K1rV5KvRSAGrbx4AvtVLBQ2) | **Prospecte malin** | Organiser sa prospection de partenaire<br>`organiser-sa-prospection-partenaire` | face caméra + diapositives | ☐ | ☐ |
| 171 [📁](https://drive.google.com/drive/folders/1piDNmvWnV5Z5Nkn0gBHji5rJc8xmFtGM) | **10 questions, 1 client** | Qualifier un établissement en dix questions<br>`qualifier-un-etablissement-en-dix-questions` | face caméra + diapositives | ☐ | ☐ |

## Vidéo à retourner

| Fiche | Raison |
|---|---|
| `brancher-jarvis-et-son-jeton` | le jeton affiché a disparu : appairage par QR de connexion depuis le 28/10 |

## Vidéos montées sans lien YouTube (44) — rien à tourner

`agent-gestion-fournisseur-whatsapp`, `agent-haccp-whatsapp`, `appliquer-une-remise`, `booster-les-stocks-dormants`, `boucle-01-configuration-boutique`, `boucle-02-equipe`, `boucle-03-stockvision`, `boucle-04-haccp`, `boucle-05-ecommerce`, `boucle-06-communication`, `boucle-07-fidelite`, `boucle-08-comptabilite`, `centraliser-les-commandes-livraison`, `cloturer-sa-caisse`, `commander-qr-code`, `commander-via-site-vocal-qrcode`, `configurer-horaires-et-reservations-site`, `configurer-sa-boutique-avec-predibot`, `configurer-sa-caisse-pos`, `connecter-son-hubrise`, `consulter-ses-performances-employe`, `dessiner-son-plan-de-salle`, `encaisser-une-commande`, `gerer-ses-clients-cote-ventes`, `gerer-son-stock-par-whatsapp`, `installer-son-restaurant-avec-le-configurateur`, `integrer-le-mcp-rapidocms-iris`, `lire-ses-previsions-predibot`, `mes-commandes-tous-canaux`, `ouvrir-son-fond-de-caisse`, `parler-a-predibot-avec-nos-prompts`, `photo-ia-controle-nettoyage`, `piocher-dans-la-marketplace-de-prompts`, `poser-une-dlc-sur-ses-productions`, `relier-uber-eats-et-deliveroo`, `retrouver-ses-commandes-multi-canal`, `retrouver-ses-documents-paie-et-contrat`, `retrouver-ses-reservations-du-jour`, `retrouver-toutes-mes-commandes`, `separer-une-addition`, `suivre-les-ecarts-de-caisse`, `suivre-ses-performances-cote-employe`, `synchroniser-sa-caisse-tierce`, `voir-les-gagnants-historique`
