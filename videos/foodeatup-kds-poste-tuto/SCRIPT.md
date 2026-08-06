# Tutoriel — Créer un poste de travail (module KDS)

Module « Flux de Service & KDS » (catégorie `service-kds`), sous-module **Écran Cuisine
(KDS)** (`kds-cuisine`, 1re vidéo du module, 0/3 avant celle-ci — voir
`videos/PROGRESSION-157-TUTORIELS.md`). Catalogue : 7b. Écran Cuisine KDS — 01 Créer un
poste de travail (module KDS) (`videos/CATALOGUE-157-TUTORIELS.md`).

Rush unique et continu (26,88 s, 1920x828, 25 fps) fourni par Michael : page « Cuisine
(kds) » avec un poste existant (« chaud », type Préparation) → clic sur « + Nouveau poste »
→ formulaire inline (nom, type, couleur) → saisie du nom « Froid » → bascule du type entre
Préparation et Pass (envois) pour montrer les deux options, réglé sur Préparation →
sélection de couleur → clic sur « Créer le poste » → toast « Poste « Froid » créé. » → la
liste défile et affiche les trois postes (« chaud » Préparation, « pass » Pass, « froid »
Préparation, chacun avec son propre lien d'écran).

## Recherche de l'outil MCP FoodEatUp correspondant

Aucun outil de création de poste KDS n'existe côté MCP FoodEatUp — seuls
`mcp__FoodEatUp__get_station_load` (lecture, charge des postes) et
`mcp__FoodEatUp__update_kds_item_status` (changer le statut cuisine d'un item de commande)
existent pour ce module. Aucun des deux ne crée un poste. **Donc pas de `claudePrompt`** sur
cette vidéo, conformément à la règle de `FOODEATUP-TUTORIELS-WORKFLOW.md` (« si non : ne pas
fabriquer de prompt, laisser `claudePrompt` absent — la section reste masquée sur le site »).

## Voix off (8 lignes) — ElevenLabs Adam Instructor (`TGAegA0zNRi8I6nUdq3i`)

| # | Texte | Durée | Placement |
|---|---|---:|---|
| N0 | Créer un poste de travail sur votre écran cuisine, ça prend quelques secondes. | 4,18 s | carte d'intro |
| N1 | Direction l'écran Cuisine, puis Nouveau poste. | 2,35 s | A/B — page + clic Nouveau poste |
| N2 | Donnez-lui un nom, comme Froid. | 1,62 s | C — saisie du nom |
| N3 | Choisissez son type : Préparation pour la production, ou Pass pour l'envoi des plats. | 4,44 s | D — bascule du type |
| N4 | Choisissez sa couleur, puis cliquez sur Créer le poste. | 2,95 s | E/F — couleur + clic |
| N5 | Votre poste est créé et rejoint la liste, prêt à recevoir ses commandes en temps réel. | 4,68 s | G — toast + résultat |
| N6 | Chaque poste dispose de son propre écran, tablette ou télé, pour un flux de commandes toujours limpide en cuisine. | 6,16 s | G (suite) — bénéfice, déborde sur la carte de fin |
| N7 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (CTA) |

N7 réutilisé tel quel (octet-identique, copié depuis `foodeatup-fiche-plat-tuto/vo/N8.mp3`)
— texte générique, zéro crédit ElevenLabs dépensé. N0-N6 générés fraîchement, voix Adam
Instructor FR.

## Découpage

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 4,50 s | CRÉER TES POSTES KDS |
| A | 0,30 → 4,00 | 2,50 s | page « Cuisine (kds) », poste « chaud » existant |
| B | 4,00 → 4,35 | 0,90 s | **zoom-punch** sur « + Nouveau poste » (1675, 363) |
| C | 7,50 → 14,00 | 3,00 s | formulaire : nom « Froid » |
| D | 14,00 → 18,00 | 4,00 s | bascule type Préparation ↔ Pass (envois), réglé sur Préparation |
| E | 18,00 → 19,00 | 1,40 s | sélection couleur |
| F | 19,00 → 19,35 | 0,90 s | **zoom-punch** sur « Créer le poste » (1668, 600) |
| G | 19,35 → 26,88 | 6,00 s | toast « Poste « Froid » créé. », défilement, 3 postes affichés |
| outro | carte | 6,00 s (auto-étendue si besoin) | CTA |

Coupe volontaire : **4,35 → 7,50 s** (temps mort/transition entre le clic sur « + Nouveau
poste » et l'apparition du formulaire, rien à montrer). Coordonnées des boutons mesurées
visuellement sur les frames réelles (`ffmpeg -ss t -frames:v 1`), cross-vérifiées sur
plusieurs frames voisines (tolérance ±15 px, sans impact sur un zoom-punch à ×1,20), même
méthode que le reste de la série.

## Séquence Claude

Absente — voir « Recherche de l'outil MCP » ci-dessus. Vidéo terminée sur la carte de fin
juste après le résultat (poste créé + bénéfice), pas de bloc « Utilisez cette fonctionnalité
avec Claude ».

## Animations

Mêmes principes que toute la série : Ken Burns sur les cartes (intro zoom-in, outro
zoom-out), xfade (0,28 s) à chaque raccord, bandeaux d'étape glissants (accents, pas
d'apostrophe dans les captions), encadré orange pulsant sur les 2 clics (+ Nouveau poste,
Créer le poste). Pas de clip avatar dans ce dossier (voix ElevenLabs de bout en bout).

## Cas d'usage / astuce du chef (pour la fiche Lovable, `howItWorks` / `whatItsFor` / `chefTip`)

**Mise à jour du 2026-08-06** — texte enrichi sur demande explicite (définition du KDS,
temps réel, exemples concrets de postes pour le dispatch des bons de commande). Publié sur
Lovable (`src/data/tutorials.ts`, commit `e37791e`) et déployé en production.

- **Qu'est-ce que le KDS** : Kitchen Display System, ou écran d'affichage cuisine — remplace
  les tickets papier par un écran par poste (tablette ou télé) installé directement sur
  chaque zone de préparation.
- **Comment ça marche** : Cuisine (kds) → + Nouveau poste → nommer le poste selon sa zone
  réelle (ex. Entrée, Chaud, Grillade, Bar) → choisir son type (Préparation ou Pass/envois)
  → choisir une couleur de repérage → Créer le poste. Chaque poste obtient son propre lien
  d'écran (bouton « Ouvrir l'écran ») et peut être régénéré (« Nouveau lien ») ou supprimé.
  Ensuite, associer ses catégories de plats dans le routage du poste (section « Routage —
  quelles catégories arrivent sur ce poste ? » visible sur chaque carte poste).
- **Temps réel** : dès qu'une commande est confirmée (comptoir, table, QR code ou
  livraison), elle s'affiche instantanément sur le ou les postes concernés — sans
  impression, sans allers-retours.
- **Personnalisation par poste / dispatch des bons de commande** : chaque poste peut être
  dédié à une zone de préparation précise — Entrée, Chaud, Grillade, Bar... — et FoodEatUp
  route automatiquement chaque ligne de commande vers le bon poste selon la catégorie du
  plat : les entrées atterrissent chez le chef entrée, les grillades chez le grillardin, les
  boissons/desserts au bar, chacun ne voyant que ce qui le concerne.
- **Astuce du chef** : un poste marqué « Poste par défaut (tout le reste) » récupère toutes
  les catégories de plats non explicitement routées vers un poste précis — toujours garder
  un poste par défaut actif pour ne perdre aucune commande. Le poste type « Pass » sert de
  dernière étape avant l'envoi en salle : idéal pour un contrôle qualité juste avant le
  service.

## Statut publication

Vidéo montée et publiée directement sur instruction explicite reçue de publier la vidéo une
fois le montage terminé, en gardant la structure comment-ça-marche / astuce du chef / cas
d'usage (même dérogation documentée que sur `foodeatup-fiche-plat-tuto` et
`foodeatup-liste-courses-tuto`) — livrée à l'utilisateur via `SendUserFile` en parallèle de
la publication.
