# Tutoriel — Afficher le KDS par poste

**STATUT : PUBLIÉ (2026-08-06)** — validé par Michael, monté (v1, 49,2s), archivé sur
RapidoCMS et ajouté sur Lovable FoodEatUp Academy (mise à jour de la fiche placeholder
`afficher-le-kds-par-poste` déjà présente, module `kds-cuisine`). Fiche enrichie sur
demande explicite (explication du bump, du temps réel, et de la synchronisation des
postes sur le Pass — voir `howItWorks`/`chefTip` ci-dessous). LinkedIn non demandé.

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

## Réalisé

1. VO ElevenLabs (Adam FR), N8 réutilisée depuis `foodeatup-qrcode-tuto/vo/N8.mp3`.
2. `build.py` : le même bug de drift voix/image que `fidelite-multicanal-tuto`
   est réapparu au premier rendu (segments trop courts par rapport aux VO
   mesurées — N5/N6 tombaient dans la séquence Claude au lieu de Froid/du
   reveal). Corrigé en calculant précisément les cibles de segment à partir des
   offsets voix "purs" (chaîne séquentielle GAP=0,22s), pas en devinant :
   `INTRO=7.18, A=5.78, B=0.90 (punch), C=8.90 (absorbe la fin de N2 + tout N3),
   D=5.28, E=6.25, CLAUDE_STAGE_D=[3.40,2.77,4.61]`. Vérifié image par image
   après coup sur chaque ancrage — zéro dérive. `banner()` réutilisait déjà le
   pattern corrigé (2 `drawtext`) dès la première passe.
3. Rendu final : `out/foodeatup-kds-par-poste-tuto-v1.mp4` (49,2s, peak audio
   -7,3dBFS). Vignette = `assets/intro.jpg` redimensionnée 1280x720.
4. Livré à Michael (STOP respecté) → validé, publication autorisée, avec demande
   explicite d'enrichir la fiche : expliquer le bump, le temps réel, et la
   synchronisation des postes sur le Pass.
5. Publication : RapidoCMS (vidéo + vignette), fiche Lovable
   `afficher-le-kds-par-poste` mise à jour en place avec un `howItWorks` étendu
   (6 étapes, dont le mécanisme bump/Fire Service) et un `chefTip` dédié
   (bump = "prêt et transmis" au poste amont, pas "servi" ; Fire Service = envoi
   réel en salle ; un ticket reste bloqué au Pass tant qu'un poste n'a pas
   bumpé son plat — anti-commande-incomplète). `PROGRESSION-157-TUTORIELS.md` /
   `LOVABLE-FOODEATUP-DOCS.md` mis à jour, tout poussé sur GitHub.
