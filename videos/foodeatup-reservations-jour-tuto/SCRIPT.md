# Tutoriel — Retrouver ses réservations du jour

**STATUT : BROUILLON — en attente de validation avant génération de la voix off.**

Module 6b « Réservations & Plan de salle » (`reservation-salle`, catégorie
`caroline-reservation`), item **01/05** du catalogue : « Retrouver ses réservations
du jour ». Premier tutoriel du module (0/5 publiés à ce jour). Fiche placeholder
déjà présente sur Lovable (`slug: "retrouver-ses-reservations-du-jour"`,
`subcategory: "01 · Réservations du jour"`, `order: 1`) — sera mise à jour en place.

Rush fourni : `assets/screen.mp4` (24,7 s, 1920x828, 25 fps) — pas de clic, un simple
scroll continu sur le tableau de bord (pas de coupure de scène nécessaire).
Carte intro : `assets/intro.jpg` (« RÉSERVATIONS DU JOUR »).
Carte outro : `assets/outro.jpg` (CTA générique, réutilisée telle quelle).

## Déroulé observé dans le rush

Page « Réservations » (« Planning et arrivées du jour », service du jeudi 6 août),
scroll continu, sans clic :
1. **Plan de salle** — chaque table avec sa capacité, sa zone (Salle
   principale/Terrasse) et son statut coloré (Libre/Réservée/Occupée/À nettoyer),
   légende en haut à droite.
2. **File d'attente** — clients sans réservation en attente d'une table (vide
   dans ce rush : « File vide »).
3. **Réservations du jour** — liste chronologique : heure, nom du client, nombre
   de couverts, n° de réservation, salle/zone, table assignée, statut
   (« Installée »). Bouton « Ouvrir la gestion complète (planning, création,
   zones) » en bas.

**Message clé (correspond au titre du catalogue) :** un seul écran centralise le
plan de salle en temps réel, la file d'attente, et la liste des réservations du
jour — de quoi savoir qui arrive, où l'installer, et ce qui reste disponible.

## Voix off proposée (9 lignes, voix Adam FR `TGAegA0zNRi8I6nUdq3i`)

| # | Texte | Ancrage |
|---|---|---|
| N0 | Envie de voir vos réservations du jour d'un coup d'œil ? FoodEatUp centralise tout sur un seul écran. | carte d'intro |
| N1 | Le plan de salle affiche chaque table en temps réel : libre, réservée, occupée, ou à nettoyer. | plan de salle |
| N2 | La file d'attente regroupe les clients sans réservation, prêts à être placés dès qu'une table se libère. | file d'attente |
| N3 | Plus bas, la liste Réservations du jour détaille chaque arrivée : heure, client, nombre de couverts. | réservations du jour (haut) |
| N4 | Et pour chacune, la table déjà assignée, avec son statut d'installation en direct. | réservations du jour (détail) |
| N5 | D'un coup d'œil, vous savez qui arrive, où l'installer, et ce qui reste disponible pour le service. | vue d'ensemble |
| N6 | Vous pouvez aussi consulter vos réservations du jour depuis Claude : copiez ce prompt, remplacez les crochets. | séquence Claude étage 1+2 |
| N7 | Collez-le dans la conversation : la liste de vos réservations s'affiche en secondes. | séquence Claude étage 3 |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | carte de fin (CTA) — **réutilisée telle quelle** (`N8.mp3` déjà généré sur toute la série) |

## Séquence Claude (outil MCP correspondant)

`mcp__FoodEatUp__list_reservations(establishment_id, date, status, limit)` existe
et correspond exactement au contenu de la liste "Réservations du jour" montrée.

**Prompt proposé (identique côté vidéo et côté fiche Lovable `claudePrompt`) :**

> Affiche mes réservations du jour ([date]) pour mon établissement FoodEatUp
> (ID [ID établissement]).

## Astuce du chef (prévue pour la fiche Lovable)

> Gardez un œil sur la file d'attente autant que sur les réservations : un client
> sans réservation peut souvent être casé sur une table libérée entre deux
> arrivées prévues — le plan de salle en temps réel vous montre cette fenêtre
> avant qu'elle ne se referme.

## À faire une fois le script validé

1. Générer N0-N7 via ElevenLabs (voix Adam FR), réutiliser N8.mp3 existant.
2. Monter `build.py` — pas de clic/zoom-punch cette fois (rush = scroll continu,
   sans coupure de scène), segments dimensionnés directement sur les VO
   mesurées dès le premier passage (leçon des deux vidéos précédentes : calculer
   les cibles depuis la chaîne d'offsets séquentielle, pas deviner).
3. Rendre le MP4 + vignette YouTube (= `assets/intro.jpg`, redimensionnée si besoin).
4. **STOP obligatoire** — livrer à Michael pour validation avant toute publication.
5. Après OK : upload RapidoCMS, mise à jour de la fiche Lovable
   `retrouver-ses-reservations-du-jour` (déjà en placeholder), mise à jour de
   `PROGRESSION-157-TUTORIELS.md` / `LOVABLE-FOODEATUP-DOCS.md`, push GitHub.
