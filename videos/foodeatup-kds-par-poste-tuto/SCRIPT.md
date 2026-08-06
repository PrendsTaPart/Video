# Tutoriel — Afficher le KDS par poste

**STATUT : BROUILLON — en attente de validation avant génération de la voix off.**

Module 7b « Écran Cuisine (KDS) » (`kds-cuisine`, catégorie `service-kds`), item **02/03**
du catalogue (`videos/CATALOGUE-157-TUTORIELS.md`) : « Afficher le KDS par poste ».
Une fiche placeholder existe déjà sur Lovable (`slug: "afficher-le-kds-par-poste"`,
`subcategory: "02 · Affichage KDS"`, `order: 2`) — sera mise à jour en place.

Rush fourni : `assets/screen.mp4` (21,3 s, 1920x828, 25 fps) — très court, pas de
compression de temps mort nécessaire cette fois.
Carte intro : `assets/intro.jpg` (« VUE KDS PAR POSTE »).
Carte outro : `assets/outro.jpg` (CTA générique, réutilisée telle quelle).

## Déroulé observé dans le rush

1. **0-3,7 s** — Back-office, page « Cuisine (kds) » : liste des postes (chaud,
   pass, froid), chacun avec badge type (Préparation/Pass), statut Actif, règles de
   routage (quelles catégories arrivent sur ce poste), boutons Ouvrir l'écran /
   Copier le lien / Nouveau lien / Supprimer. Curseur posé sur « Ouvrir l'écran »
   du poste **chaud** (clic ~3,5 s).
2. **3,7-6,3 s** — Transition d'onglet (écran noir, même pattern que le tuto
   précédent) → ouverture de l'écran KDS dédié.
3. **6,3-12,5 s** — Écran KDS, onglet **Chaud** actif : grille de tickets (n°,
   canal, client, plats, allergènes, timer), bouton **BUMP CHAUD** par ticket.
   En-tête : onglets Chaud/Pass/Froid, compteur Tickets, Production, Rappel,
   Pause, Retour.
4. **12,5-17 s** — Clic sur l'onglet **Pass** : tickets transférés depuis Chaud
   (badges « CHAUD ... » / « PASS ✓ »), bouton **FIRE SERVICE** (pas cliqué dans
   ce rush).
5. **17-21,3 s** — Clic sur l'onglet **Froid** : file vide, message « Aucun
   ticket — tout est à jour ».

**Message clé (correspond au titre du catalogue) :** chaque poste de cuisine a son
propre écran KDS, filtré sur ses seuls tickets — l'équipe chaud ne voit que le
chaud, l'équipe pass que le pass, etc.

## Voix off proposée (9 lignes, voix Adam FR `TGAegA0zNRi8I6nUdq3i`)

| # | Texte | Ancrage |
|---|---|---|
| N0 | Envie de voir votre cuisine s'organiser en temps réel, poste par poste ? Voici l'écran KDS de FoodEatUp. | carte d'intro |
| N1 | Depuis Cuisine, chaque poste — chaud, pass, froid — a son propre écran dédié. | liste des postes |
| N2 | Cliquez sur Ouvrir l'écran pour afficher les commandes de ce poste, en direct. | clic Ouvrir l'écran |
| N3 | Le poste Chaud affiche uniquement ses plats à préparer, prêts à être validés. | écran KDS Chaud |
| N4 | Passez à l'onglet Pass pour voir les tickets transférés, en attente d'envoi en salle. | onglet Pass |
| N5 | Et le poste Froid, à jour, sans ticket en attente : chaque équipe ne suit que ce qui la concerne. | onglet Froid (vide) |
| N6 | Vous pouvez aussi consulter la charge de vos postes depuis Claude : copiez ce prompt, remplacez les crochets. | séquence Claude étage 1+2 |
| N7 | Collez-le dans la conversation : la charge de chaque poste s'affiche en secondes. | séquence Claude étage 3 |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | carte de fin (CTA) — **réutilisée telle quelle** (`N8.mp3` déjà généré sur toute la série) |

## Séquence Claude (outil MCP correspondant)

`mcp__FoodEatUp__get_station_load(establishment_id)` existe (lecture seule : tickets
actifs par poste) et correspond exactement à l'action de consultation montrée à l'écran.

**Prompt proposé (identique côté vidéo et côté fiche Lovable `claudePrompt`) :**

> Affiche la charge de mes postes cuisine (KDS) pour mon établissement FoodEatUp
> (ID [ID établissement]).

## Astuce du chef (prévue pour la fiche Lovable)

> Gardez chaque écran KDS sur l'écran dédié de son poste plutôt que d'afficher tous
> les tickets en cuisine : votre équipe chaud ne voit que le chaud, votre équipe
> pass ne voit que ce qui doit partir en salle — moins de bruit visuel, moins
> d'erreurs de service en coup de feu.

## À faire une fois le script validé

1. Générer N0-N7 via ElevenLabs (voix Adam FR), réutiliser N8.mp3 existant.
2. Monter `build.py` — zoom-punch sur le clic « Ouvrir l'écran », coupure de
   scène (slideleft) au tab switch, retimer les segments sur les VO mesurées
   (ne pas répéter le bug de drift déjà rencontré sur `fidelite-multicanal-tuto`).
   Réutiliser directement le `banner()` corrigé (2 `drawtext`, pas `drawbox`+`t`).
3. Rendre le MP4 + vignette YouTube (= `assets/intro.jpg`, redimensionnée si besoin).
4. **STOP obligatoire** — livrer à Michael pour validation avant toute publication.
5. Après OK : upload RapidoCMS, mise à jour de la fiche Lovable
   `afficher-le-kds-par-poste` (déjà en placeholder), mise à jour de
   `PROGRESSION-157-TUTORIELS.md` / `LOVABLE-FOODEATUP-DOCS.md`, push GitHub.
