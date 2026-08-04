# Tutoriel — Ajouter ses employés FoodEatUp (module Équipe & Planning)

Première vidéo du module `equipe-planning` (Drive : dossier "AJOUTER SES EMPLOYÉS —
MODULE ÉQUIPE"). Durée livrée : **46,0 s** — H.264 High/yuv420p, AAC 48 kHz stéréo,
faststart. Audio : true peak **-7,3 dBFS**. Decode 0 erreur, moov avant mdat (faststart
confirmé).

## Ce que montre le rush

Le rush (56,1 s, 1920x828) montre : la liste Employées vide → clic "Ajouter un
employé" → formulaire en 2 étapes (1. Informations générales : prénom, nom, email,
téléphone, rôle ; 2. Horaires de travail : jour, heure de début/fin, repos) → clic
"Ajouter" → la carte "Alice charbit / Chef / Permission : HACCP" apparaît dans la
liste → clic "Voir" → fiche complète (coordonnées, rôle, horaires). La fin du rush
(édition "Modifier" puis "Annuler", ~49,5→56,1s) n'est pas reprise dans le montage :
hors sujet pour ce tutoriel (ajout, pas modification).

## Voix off (9 lignes, voix Adam FR `TGAegA0zNRi8I6nUdq3i`)

| # | Texte | Durée | Segment |
|---|---|---:|---|
| N0 | Ajouter un employé à votre équipe FoodEatUp, en quelques clics. | 3,53 s | intro |
| N1 | Cliquez sur Ajouter un employé pour commencer. | 2,59 s | clic "Ajouter un employé" |
| N2 | Renseignez son prénom, son nom, son email, son téléphone et son rôle. | 4,49 s | C — informations générales |
| N3 | Définissez ensuite ses horaires de travail. | 2,22 s | E — horaires de travail |
| N4 | Cliquez sur Ajouter : votre employé apparaît aussitôt dans l'équipe. | 3,60 s | clic Ajouter → succès |
| N5 | Ouvrez sa fiche pour retrouver toutes ses informations et ses permissions. | 4,00 s | I — fiche complète (clic Voir) |
| N6 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | 4,41 s | étages 1+2 (réutilisé tel quel depuis `foodeatup-produits-tuto`) |
| N7 | Collez-le dans la conversation : votre employé est ajouté en quelques secondes. | 4,18 s | étage 3 |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (CTA, réutilisé tel quel depuis `foodeatup-produits-tuto`) |

N6/N8 réutilisés tels quels (texte générique identique) — zéro crédit ElevenLabs
dépensé sur ces deux lignes.

## Découpage

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 3,00 s | AJOUTER SES EMPLOYÉS — MODULE ÉQUIPE |
| A | 0,20 → 2,60 | 2,60 s | liste "Employées" vide, bouton "Ajouter un employé" |
| B | 2,60 → 2,90 | 0,90 s | **zoom-punch** sur "Ajouter un employé" (1695, 344) |
| C | 3,00 → 26,90 | 6,00 s | prénom "alice", nom "charbit", email, téléphone, rôle "Chef" |
| D | 27,00 → 27,30 | 0,90 s | **zoom-punch** sur "Suivant" (1202, 759) |
| E | 27,40 → 41,00 | 6,00 s | jour "Lundi", 08:00→17:00, repos 1H |
| F | 41,10 → 41,40 | 0,90 s | **zoom-punch** sur "Ajouter" (1205, 674) |
| G | 41,50 → 45,40 | 3,00 s | carte "Alice charbit / Chef / Permission : HACCP" |
| H | 45,40 → 45,70 | 0,90 s | **zoom-punch** sur "Voir" (389, 682) |
| I | 45,80 → 49,20 | 4,00 s | fiche complète (tél/email, rôle, horaires) |
| claude1 | carte générée | 6,00 s | reveal — prompt en gros, fond crème |
| claude2 | carte générée | 3,00 s | confirmation "Copié dans le presse-papiers !" |
| claude3 | carte générée | 6,00 s | mockup chatbot Claude |
| outro | carte | 6,20 s | CTA |

Coordonnées de clic mesurées directement sur les frames extraites du rush
(`ffmpeg -ss t -frames:v 1`), résolution source native 1920x828 — pas de seuillage
colorimétrique nécessaire ici, boutons identifiés visuellement à chaque clic.

## Séquence Claude — module partagé

`mcp__FoodEatUp__create_employee(establishment_id, first_name, last_name, email,
phone_number, role?, schedule?)` existe — schéma vérifié, `role` accepte
`employee/manager/chef/cuisinier/serveur` (le rush utilise "Chef", valeur valide) :

> Crée l'employé [prénom] [nom], email [email], téléphone [téléphone], rôle [rôle],
> pour mon établissement FoodEatUp (ID [ID établissement]).

Même texte côté fiche Lovable (`claudePrompt`).

## Animations

Mêmes principes que toute la série : Ken Burns sur les cartes, xfade (0,28 s),
bandeaux d'étape, encadré orange pulsant sur les 3 clics (nouveauté vs. les tutos à 2
clics : "Ajouter un employé" → "Suivant" → "Ajouter", plus un 4e clic zoom-punché sur
"Voir" pour montrer la fiche complète). Pas de clip avatar dans ce dossier.

## Statut publication

Montage terminé et checklist de compatibilité passée (H.264 High/yuv420p, AAC 48 kHz
stéréo, faststart, peak -7,3 dBFS, 0 erreur de décodage). **En attente de validation
avant publication** (règle du 2026-08-02, `videos/LOVABLE-FOODEATUP-DOCS.md`) : pas
d'upload RapidoCMS/LinkedIn (RapidoCMS non authentifié dans cette session de toute
façon), pas d'envoi du prompt Lovable tant que la vidéo n'a pas été revue.
