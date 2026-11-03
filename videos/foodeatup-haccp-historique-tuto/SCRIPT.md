# Tutoriel — Retrouver mes contrôles historique (HACCP, Checklist Hygiène) FoodEatUp

4e vidéo du module HACCP (après `valider-une-production`, `tracer-ses-productions-historique`,
`creer-une-tracabilite-simplifiee`). Rush fourni par Michael : `assets/screen.mp4`
(50,28 s, 1920x828, piste audio native silencieuse à -91 dB — VO entièrement
ElevenLabs). Pas de clip avatar.

## Ce que montre le rush (et ce qui est volontairement coupé au montage)

1. Page "Checklist hygiène" courante (0,0 → 2,0 s) : liste des points de contrôle
   ("Les employés portent des tenues propres", "Pas de bijoux, montres, ongles
   longs"), bouton "Ajouter une checklist".
2. Clic sur "Historique" (nav du haut) → page "historique haccp" : grille de
   modules (Températures, Traçabilité, Plan de nettoyage, Production, Contrôle à
   réception, **Checklist Hygiène** — "1 validations", Étiqueteuse).
3. Clic sur la carte "Checklist Hygiène" (4,4 → 4,7 s) → "Historique des
   validations" : stats (Total/Confirmées/Non confirmées/Score moyen = 100%),
   1 entrée "Aujourd'hui — Contrôle hygiène équipe — service du soir".
4. Clic sur l'entrée → modale "Modifier la validation" : date, zone de contrôle
   (Cuisine), point de contrôle, statut Conforme/Non conforme/Non évalué, score
   de conformité (barre verte), commentaires, photo existante.
5. **Non montré au montage** : entre 11,5 s et 32 s, le rush bascule le statut
   sur "Non conforme" (le score recalcule en direct à 0 %, barre rouge), scroll
   jusqu'aux commentaires/photo, tente d'enregistrer sans champ requis rempli et
   affiche une erreur de validation ("The reponse field is required"), puis
   revient à la liste sans avoir sauvegardé. Cette partie n'est pas un cas
   d'usage à montrer (message d'erreur mêlé anglais/français, pas une
   fonctionnalité) : le montage saute directement de la consultation du détail
   (étape 4) au retour sur la liste, propre.
6. Retour sur "Historique des validations" (32,5 → 34,0 s), clic sur "Exporter
   l'historique" (34,0 → 34,3 s).
7. Modale "Exporter l'Historique HACCP" : 3 formats (Standard / Détaillé /
   Statistiques), options avancées (photos, commentaires, groupement par date),
   clic sur "Générer le PDF" (41,0 → 41,3 s).
8. Toast "Génération de l'export en cours...", puis "Export standard généré
   avec succès". Le PDF s'ouvre : rapport "Historique Checklist Hygiène" (45,0
   → 50,28 s).

## Voix off (7 lignes)

| # | Texte | Durée | Segment |
|---|---|---:|---|
| N0 | Retrouvez en un instant l'historique de toutes vos checklists hygiène FoodEatUp. | 4,02 s | intro + A |
| N1 | Ouvrez Historique dans le menu, puis la carte Checklist Hygiène. | 3,53 s | B + clic C |
| N2 | Vous retrouvez toutes vos validations passées, avec leur score de conformité. | 4,13 s | D |
| N3 | Cliquez sur une validation pour revoir son détail : zone, date, commentaires et photos. | 5,25 s | E |
| N4 | Depuis cette page, exportez votre historique en un clic. | 3,11 s | F + clic G |
| N5 | Choisissez le format du rapport, puis générez le PDF : une preuve écrite prête pour vos contrôles sanitaires. | 6,69 s | H + clic I |
| N6 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (réutilisé de `foodeatup-produits-tuto/vo/N8.mp3`) |

Pas de N7/étage Claude : aucun outil MCP FoodEatUp ne couvre "lister l'historique
des validations" ni "exporter un rapport PDF" (`list_hygiene_checklists` ne
liste que les modèles de checklist, pas les validations passées — vérifié par
un appel réel). Conformément à la règle du pipeline, aucun prompt n'est
inventé : pas de séquence "Utilisez cette fonctionnalité avec Claude" dans
cette vidéo, pas de `claudePrompt` côté fiche Lovable.

## Découpage

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 2,60 s | RETROUVER MES CONTRÔLES HISTORIQUE |
| A | 0,00 → 2,00 | 3,00 s | Checklist hygiène (page courante) |
| B | 3,00 → 4,40 | 3,40 s | Grille "historique haccp", carte Checklist Hygiène |
| C | 4,40 → 4,70 | 0,70 s | **zoom-punch** sur la carte "Checklist Hygiène" (750, 562) |
| D | 5,00 → 8,50 | 4,60 s | "Historique des validations" : stats + entrée |
| E | 9,00 → 11,50 | 6,00 s | Détail d'une validation (modale) |
| F | 32,50 → 34,00 | 2,20 s | Retour sur "Historique des validations" |
| G | 34,00 → 34,30 | 0,70 s | **zoom-punch** sur "Exporter l'historique" (1462, 300) |
| H | 34,30 → 41,00 | 7,00 s | Modale export : Standard / Détaillé / Statistiques |
| I | 41,00 → 41,30 | 0,70 s | **zoom-punch** sur "Générer le PDF" (1023, 758) |
| J | 41,30 → 44,50 | 2,00 s | Génération + succès |
| K | 45,00 → 50,28 | 4,50 s | Le PDF "Historique Checklist Hygiène" s'ouvre |
| outro | carte | 6,20 s | CTA |

Coordonnées mesurées sur les frames réelles (`ffmpeg -ss t -frames:v 1`).

## Animations

Mêmes principes que la série : `setpts` pour la vitesse (jamais `zoompan` sur la
vidéo réelle), zoom-punch en crop fixe sur les 2 clics, xfade 0,28 s, cartes
intro/outro en fond flou + overlay net. Bandeaux et halo de clic en position
**statique** (pas d'animation de glissement/pulsation) : ce build ffmpeg évalue
les expressions `x`/`y` de `drawbox` une seule fois à t=0 (pas d'option `eval`
disponible sur ce build) — bug découvert et documenté sur
`foodeatup-predibot-suggestions-tuto`, même correctif appliqué ici dès le
premier montage.

## Statut publication

Vidéo montée suite à la demande explicite de Michael. Pas de séquence Claude
(aucun outil MCP ne correspond à "historique des validations hygiène" ni à
"export PDF" — vérifié). Publication Lovable uniquement (FoodEatUp Academy,
module HACCP), comme demandé.
