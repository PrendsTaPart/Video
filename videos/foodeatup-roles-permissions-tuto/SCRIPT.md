# Tutoriel — Rôles et permissions : contrôler le pointage (pauses & photo)

Module Équipe & Planning, dossier Drive **« 15-Gestion des pauses, pointage
entrée et sortie et Empreinte photo du pointage »** — mais le rush fourni
(`78feb708-...mp4`, 41,52 s) enregistre en réalité l'écran **Équipe > Rôles >
Modifier le rôle** (rôles/permissions), qui est le contenu du dossier Drive
**« 1-Configuration des rôles et permissions »**. Vérifié via
`mcp__Google_Drive__search_files` : le fichier vidéo présent dans le dossier
15 a exactement la même taille (31 001 599 octets) que celui envoyé, donc
c'est bien un mauvais enregistrement déposé dans le dossier 15, pas une
erreur d'upload — **à signaler à Michael** pour qu'il vérifie si le dossier 1
a besoin d'un rush séparé.

Suivant l'instruction explicite de Michael ("pense que c'est le patron qui
regarde et contrôle le pointage... grâce à ces permissions"), la vidéo est
construite à partir de ce contenu réel (rôles/permissions) mais racontée du
point de vue du patron/chef de cuisine/directeur qui pilote le pointage
(entrée/sortie, pauses, photo) via le système de rôles. Durée livrée :
**62,44 s** — H.264 High/yuv420p, AAC 48 kHz stéréo, faststart. Sans avatar
HeyGen, **sans claudePrompt pour l'action affichée à l'écran** (éditer un
rôle n'a pas d'équivalent MCP, même classe que `creer-son-compte` /
`regler-ses-unites`) mais **avec une séquence Claude** pour un cas d'usage
directeur réel (`list_attendances`).

## Voix off (8 lignes)

| # | Texte | Durée | Segment |
|---|---|---:|---|
| N1 | Chaque membre de l'équipe accède à FoodEatUp selon son rôle : voici l'espace d'un manager. | 5,25 s | A |
| N2 | Vos employés pointent leur service, leurs pauses, et confirment leur identité par photo, en scannant simplement ce QR code. | 6,95 s | B |
| N3 | Depuis Équipe puis Rôles, retrouvez les rôles déjà configurés : Admin avec deux cent quarante-cinq permissions, Manager avec deux cent dix. | 7,71 s | C1 |
| N4 | Modifiez un rôle pour ajuster précisément ce que chaque niveau — manager, chef de cuisine ou directeur — peut voir et faire dans FoodEatUp. | 8,25 s | C2 |
| N5 | Le module Pointages est ouvert à sept permissions sur sept pour le Manager : il peut pointer son service, gérer ses pauses et valider sa photo. HACCP, lui, reste fermé à zéro sur quarante-et-un — les modules sensibles restent réservés aux rôles supérieurs. | 14,65 s | D1 + D2 (zoom-punch) |
| N6 | Vous pouvez aussi demander ça à Claude : copiez ce prompt, remplacez les crochets. | 4,21 s | étages 1+2 |
| N7 | Collez-le dans la conversation : les pauses de votre équipe s'affichent en quelques secondes. | 4,60 s | étage 3 |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (réutilisée) |

## Découpage

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 2,50 s | POINTER SON SERVICE, PAUSES & PHOTO (visuel fourni par Michael) |
| A | 0,00 → 5,00 | 6,00 s | « mon espace » — vue Manager, grille de modules |
| B | 15,00 → 18,00 | 7,50 s | QR code permanent de pointage + 3 étapes d'usage |
| C1 | 19,00 → 21,30 | 8,30 s | Page Rôles : cartes Admin (245 permissions) / Manager (210 permissions) |
| C2 | 22,00 → 26,00 | 8,90 s | Modale « Modifier le rôle » — défilement des modules |
| D1 | 32,50 → 33,10 | 7,60 s | **zoom-punch** sur « Pointages (7/7) » |
| D2 | 32,50 → 33,10 | 7,60 s | **zoom-punch** sur « HACCP (0/41) » — contraste rôle limité |
| claude1 | carte générée | 2,60 s | reveal — prompt en gros, fond crème |
| claude2 | carte générée | 2,50 s | confirmation « Copié dans le presse-papiers ! » |
| claude3 | carte générée | 5,40 s | mockup chatbot Claude |
| outro | carte | 6,20 s | CTA |

## Séquence Claude — module partagé

Aucun outil MCP ne couvre l'édition d'un rôle/permission elle-même (action de
sécurité/admin, comme `creer-son-compte`). En revanche, le directeur peut
demander directement à Claude le détail des pauses d'un employé via
`list_attendances(establishment_id, date_from, date_to)` — même outil que
`retrouver-les-pointages-historique`, réutilisé ici sous un angle « pauses »
demandé explicitement par Michael.

> Donne-moi le détail des pauses de [prénom] [nom] du [date début] au [date
> fin], pour mon établissement FoodEatUp (ID [ID établissement]).

Côté fiche Lovable, deux prompts de cas d'usage supplémentaires pour le
directeur (mêmes données, angles d'analyse différents) :
- Repérer les pauses anormalement longues sur une période.
- Comparer les pointages réels aux horaires prévus au planning.

## Animations

Mêmes principes que toute la série : Ken Burns sur les cartes, xfade
(0,28 s), bandeaux d'étape (module `banner()` corrigé — slide-in seul),
encadré orange pulsant en zoom-punch sur les lignes de permission
« Pointages » puis « HACCP » (coordonnées mesurées sur une fenêtre stable du
rush, 32,5-33,1 s — le défilement de la modale dérive légèrement avant ce
point, d'où la fenêtre resserrée).

## Statut publication

Vidéo à livrer à Michael pour validation avant publication RapidoCMS/
LinkedIn/Lovable — **et à faire confirmer explicitement le sujet** (rôles et
permissions, dossier Drive 1) avant publication, vu le mélange avec le
dossier 15. RapidoCMS non autorisé dans cette session — publication CMS/
LinkedIn en attente dans tous les cas.
