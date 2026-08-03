# Catalogue cible — 157 tutoriels FoodEatUp (structure fournie par Michael, 2026-08-03)

Ce fichier est la référence brute de la structure catalogue transmise par Michael
pour réorganiser le site Lovable (FoodEatUp Academy) en 14 modules regroupés par
catégories, avec code couleur, et pour cadrer la production des tutoriels restants.
À relire avant de choisir la prochaine vidéo à produire ou avant de faire évoluer
l'architecture du site.

## ⚠️ Incohérence relevée dans le document source

Le résumé annonce **8 catégories**, mais le détail fourni liste **11 en-têtes
« CATÉGORIE N »** (3 d'entre elles regroupent 2 sous-modules : Caroline+Réservation,
Service+KDS, Comptabilité+PrediBot). C'est cette structure à **11 catégories /
14 modules** qui est utilisée ci-dessous et dans l'architecture Lovable : elle est
la seule dont la somme des vidéos tombe juste sur **157** (14+20+8+7+4+11+6+24+20+30+13).
Le chiffre « 8 » du résumé est probablement un reliquat d'une version antérieure du
document — à clarifier avec Michael si besoin, comme pour l'écart 107→94→92 déjà
rencontré sur le premier audit (`FAISABILITE-SERIE-TUTORIELS.md`).

## Vue d'ensemble (14 modules / 11 catégories réelles / 157 vidéos)

| Catégorie | Module(s) | Nb vidéos | Couleur | Slug module (site) |
|---|---|---:|---|---|
| 1. Configuration Boutique | — | 14 | `#0D6EFD` | `configuration` *(existant)* |
| 2. Équipe, Planning & RH | — | 20 | `#7C3AED` | `equipe-planning` *(existant)* |
| 3. Site Web & Vitrine | — | 8 | `#2563EB` | `site-web-vitrine` |
| 4. Caisse POS & Matériel | — | 7 | `#EA580C` | `caisse-pos` |
| 5. HubRise & Livraisons | — | 4 | `#06B6D4` | `hubrise-livraisons` |
| 6. Agent IA Caroline & Salle | Caroline (voix) | 6 | `#F59E0B` | `caroline-ia` |
| 6. Agent IA Caroline & Salle | Réservation & plan de salle | 5 | `#D97706` | `reservation-salle` |
| 7. Flux de Service & KDS | Service multi-canal | 3 | `#059669` | `service-commande` |
| 7. Flux de Service & KDS | KDS (écran cuisine) | 3 | `#16A34A` | `kds-cuisine` |
| 8. Marketing, Fidélité & Iris | — | 24 | `#EC4899` | `marketing-fidelite` |
| 9. StockVision AI | — | 20 | `#10B981` | `stockvision-ai` *(existant)* |
| 10. Hygiène & HACCP | — | 30 | `#DC2626` | `haccp` *(existant)* |
| 11. Comptabilité & PrediBot | Comptabilité & achats | 10 | `#475569` | `comptabilite` *(existant)* |
| 11. Comptabilité & PrediBot | PrediBot (agent IA directeur) | 3 | `#111827` | `predibot` |

Les 5 modules déjà existants sur le site (`configuration`, `equipe-planning`,
`comptabilite`, `haccp`, `stockvision-ai`) gardent leur slug pour ne pas casser
les tutoriels déjà publiés — seuls leur couleur/regroupement par catégorie et
leur `expectedCount` sont mis à jour pour matcher ce catalogue.

## Détail des 157 vignettes (intitulés vidéo, 3 lignes chacun)

### 1. Configuration Boutique (14) — `#0D6EFD`
00 Créer son **Compte** FoodEatUp · 01 Créer sa **Boutique** FoodEatUp · 02 Choisir
son **Abonnement** FoodEatUp · 03 Configurer son **Profil** Entreprise · 04
Paramétrer sa **TVA** FoodEatUp · 05 Ajouter ses **Fournisseurs** FoodEatUp · 06
Brancher son **MCP** sur Claude · 07 Créer ses **Catégories** FoodEatUp · 08 Régler
ses **Unités** de mesure · 09 Saisir ses **Ingrédients** FoodEatUp · 10 Créer ses
**Produits** FoodEatUp · 11 Monter ses **Recettes** (fiches techniques) · 12 Ouvrir
sa **Vitrine** en ligne · 13 Diffuser son **QR Code** FoodEatUp

### 2. Équipe, Planning & RH (20) — `#7C3AED`
01 Créer ses **Rôles** et permissions · 02 Ajouter ses **Employés** (module Équipe)
· 03 Établir un **Contrat** et son salaire · 04 Régler ses **Horaires** par employé
· 05 Brancher **Jarvis** et son jeton · 06 Imprimer son **Planning** par poste · 07
Assigner les **Tâches** sur le planning · 08 Générer le **QR Code** de sa boutique
· 09 Créer son **Code PIN** (accès & Jarvis) · 10 Commander ses **Cartes NFC** pour
le badge · 11 Installer la **Borne** d'accueil · 12 Retrouver les **Pointages**
(historique) · 13 Se connecter **côté employé** (URL & code PIN) · 14 Découvrir son
**Accueil** selon son rôle · 15 Pointer son **Service** (pauses & photo) · 16 Voir
son **Planning** côté employé · 17 Poser un **Congé** côté employé · 18 Suivre ses
**Performances** côté employé · 19 Retrouver ses **Documents** (paie & contrat) ·
20 Lire ses **Notifications** et tâches du jour

### 3. Site Web & Vitrine (8) — `#2563EB`
01 Activer l'**Abonnement** éditeur web · 02 Choisir son **Template** (mon site) ·
03 Personnaliser **son site** (éditeur web) · 04 Gérer les **Pages** de son site ·
05 Créer un site **par IA** FoodEatUp · 06 Configurer ses **Horaires** &
réservations · 07 Ajouter du **Contenu** sur son site · 08 Connecter son
**Domaine** (mon site)

### 4. Caisse POS & Matériel (7) — `#EA580C`
01 Configurer sa **Caisse POS** (TPE & ticket) · 02 Ouvrir son **Fond de caisse**
(début de service) · 03 Encaisser une **Commande** (comptoir & table) · 04
Appliquer une **Remise** et avoirs · 05 Séparer une **Addition** (multi-paiement) ·
06 Clôturer sa **Caisse** (le Z de caisse) · 07 Suivre les **Écarts caisse**
(historique)

### 5. HubRise & Livraisons (4) — `#06B6D4`
01 Connecter son **HubRise** FoodEatUp · 02 Relier **Uber Eats & Deliveroo** via
HubRise · 03 Synchro votre **Caisse tierce** via HubRise · 04 Centraliser les
**Commandes** (flux livraison)

### 6a. Agent IA Caroline (6) — `#F59E0B`
01 Configurer **Caroline** (voix & prompts) · 02 Réécouter ses **Appels** et
réservations · 03 Dessiner son **Plan de salle** (QR code à table) · 04 Gérer ses
**Tables** (ajout & blocage) · 05 Ouvrir ses **Créneaux** de réservation · 06 Tenir
ses **Réservations** au quotidien

### 6b. Réservations Salle (5) — `#D97706`
01 Retrouver ses **Réservations** du jour · 02 Ajouter une **Réservation** (module
table) · 03 Gérer ses **No-shows** & modifications · 04 Placer un **Client** à
table · 05 Scanner le **QR Code** de la table

### 7a. Service Multi-Canal (3) — `#059669`
01 Retrouver ses **Commandes** multi-canal · 02 Commander sur **Site & QR** (ou
agent vocal) · 03 Envoyer en **Cuisine** en direct

### 7b. Écran Cuisine KDS (3) — `#16A34A`
01 Créer un poste de travail (module KDS) · 02 Afficher le **KDS** par poste · 03
Gérer une **Commande** en direct (KDS)

### 8. Marketing, Fidélité & Iris (24) — `#EC4899`
01 Débloquer les **Avis** clients · 02 Synchro Google **Avis** clients · 03
Répondre aux **Avis** clients · 04 Activer le pack **Marketing** FoodEatUp · 05
Lancer une **Campagne** marketing · 06 Créer une campagne **par IA** (agent
FoodEatUp) · 07 Retrouver son **Agenda** marketing · 08 Créer ses templates
**WhatsApp** marketing · 09 Ciblage et **Consentement** clients · 10 Suivre ses
**Crédits** SMS & WhatsApp · 11 Recharger ses **Crédits** (pack Com') · 12 Booster
la **Fidélité** (programme) · 13 Gérer les **Récompenses** fidélité · 14 Lancer un
**Jeu concours** fidélité · 15 Retrouver son **QR Code** jeu concours · 16 Voir les
**Gagnants** (historique) · 17 Créer un **Sondage** fidélité · 18 Résultats des
**Sondages** (historique) · 19 Fidélité **Multi-canal** (canaux de vente) · 20 Vue
publique **Fidélité** côté client · 21 Intégrer le **MCP** RapidoCMS & Iris · 22
Synchroniser la **Charte** graphique Iris · 23 Booster les **Stocks**
(opportunités IA) · 24 Calendrier **de Com'** (agent Iris)

### 9. StockVision AI (20) — `#10B981`
01 Construire sa **Carte** StockVision AI · 02 Déduire ses **Besoins** de la
production · 03 Prédire ses **Commandes** (ventes & production) · 04 Tenir sa
**Liste** de courses · 05 Envoyer sa **Commande** au fournisseur · 06 Suivre ses
**Livraisons** (statuts & dates) · 07 Valider son **BL** en détail · 08 Valider son
**Entrée stock** (température & EAN) · 09 Scanner sa **Facture** (OCR & prix auto)
· 10 Classer ses **Factures** dans les dépenses · 11 Tenir ses **Dépenses**
StockVision AI · 12 Valider sa **Production** (quantité & temp.) · 13 Imprimer ses
**Ingrédients** de production · 14 Tracer ses **Productions** (historique) · 15
Sortir ses **Ingrédients** du stock · 16 Lire ses **Mouvements** de stock · 17
Saisir un **Mouvement** de stock · 18 Lire ses **Statistiques** par module · 19
Sortir un **Rapport** et son historique · 20 Suivre les **Suggestions** de l'agent
IA

### 10. Hygiène & HACCP (30) — `#DC2626`
01 Ouvrir son **Classeur** (module HACCP) · 02 Déclarer ses **Équipements**
(module HACCP) · 03 Relever une **Température** d'équipement · 04 Retrouver mes
**Relevés** (historique) · 05 Sonder ses **Plats** à cœur · 06 Retrouver mes
**Plats sondés** (historique) · 07 Tracer en mode **Simplifié** (traçabilité) · 08
Tracer en mode **Complet** (traçabilité) · 09 Retrouver ma **Traçabilité**
(historique) · 10 Paramétrer son **Nettoyage** (plan & zones) · 11 Pointer ses
**Actions** au quotidien · 12 Retrouver mes **Zones** (historique) · 13 Créer sa
**Fiche plat** pour production · 14 Consulter ses **Productions** en cours · 15
Poser une **DLC** sur ses productions · 16 Retrouver ses **Productions**
(historique) · 17 Créer un **Produit** pour étiquetage · 18 Imprimer ses
**Étiquettes** (vente & stockage) · 19 Retrouver mes **Étiquettes** (historique) ·
20 Archiver ses **Documents** de nettoyage · 21 Utiliser nos **Modèles**
FoodEatUp · 22 Créer sa **Check-list** hygiène · 23 Faire son **Contrôle** de
conformité · 24 Retrouver mes **Contrôles** (historique) · 25 Contrôler à
**Réception** de livraison · 26 Valider une **Livraison** (module HACCP) · 27
Scanner le **Code EAN** et la DLC · 28 Retrouver mes **Livraisons** (historique) ·
29 Une photo, **l'IA contrôle** votre nettoyage · 30 Exporter tout son **Classeur**
(module HACCP)

### 11a. Comptabilité & Achats (10) — `#475569`
01 Gérer ses **Fournisseurs** côté achats · 02 Gérer ses **Clients** côté ventes ·
03 Créer un **Devis** (comptabilité) · 04 Changer les **Statuts** d'un devis · 05
Créer une **Facture** (comptabilité) · 06 Changer les **Statuts** d'une facture ·
07 Saisir ses **Dépenses** fournisseur · 08 Relier ses achats **aux livraisons**
(comptabilité) · 09 Déclarer son **e-reporting** (comptabilité) · 10 Retrouver
toutes mes **commandes** (QR, web, vocal)

### 11b. PrediBot — Agent IA Directeur (3) — `#111827`
01 Lire ses **Prévisions** PrediBot · 02 Piocher dans la **Marketplace** de
prompts · 03 Parler à **PrediBot** avec nos prompts

## Suivi de production

Voir le tableau « Tutoriels publiés » dans `LOVABLE-FOODEATUP-DOCS.md` pour l'état
réel (vidéos déjà tournées/publiées) — ce fichier-ci est la cible catalogue, pas
l'état d'avancement.

**2026-08-03 — Architecture implémentée.** Les 11 catégories / 14 modules et couleurs
de ce catalogue sont désormais en place sur le site Lovable (`src/data/tutorials.ts`,
commit `12fb06d2510edcdda4116f886a3d259f638559a8`), avec regroupement par catégorie sur
l'accueil, fil d'Ariane catégorie sur les pages module, et SEO complet (canonical,
og/twitter, JSON-LD `VideoObject`) sur chaque page tutoriel. Vérifié par lecture
complète des fichiers modifiés : les 16 tutoriels déjà publiés n'ont pas été touchés.
Reste à faire au fil de la production : ajouter les tutoriels des 9 modules encore
vides (`site-web-vitrine`, `caisse-pos`, `hubrise-livraisons`, `caroline-ia`,
`reservation-salle`, `service-commande`, `kds-cuisine`, `marketing-fidelite`,
`predibot`) au fur et à mesure des rushes reçus — l'architecture n'a plus besoin
d'être retouchée pour ça.
