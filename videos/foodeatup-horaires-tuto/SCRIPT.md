# Tutoriel — Régler ses horaires par employé (module Équipe & Planning)

Douzième vidéo du module `equipe-planning` (catalogue #4). Durée livrée :
**64,72 s** — H.264 High/yuv420p, AAC LC 48 kHz stéréo, faststart (moov avant
mdat confirmé). Audio : max **-7,2 dBFS** / mean -22,0 dBFS. Decode 0 erreur.

## Ce que montre le rush

Le rush (30,44 s, capture 1920x828 @25fps, pas de chrome navigateur à
rogner) montre : liste des employées, carte "Alice Charbit" (Chef) → clic
"Voir" → panneau détail (onglet Personnel, section "Horaires de travail" :
Lundi 08:00-17:00, 1h de pause) → clic "Modifier" → modale "Modifier
l'employé" (étape 2, Horaires de travail) → "+ Ajouter une plage horaire"
crée un second créneau → le jour du second créneau est basculé sur Mardi,
puis ses heures sont ajustées pour rejoindre celles du lundi (08:00-17:00) →
clic "Sauvegarder" → retour à la liste, planning mis à jour.

## Voix off (10 lignes, voix Adam FR `TGAegA0zNRi8I6nUdq3i`)

| # | Texte | Durée | Segment |
|---|---|---:|---|
| N0 | Chaque employé a ses propres horaires selon les jours. Voici comment les régler dans FoodEatUp. | 5,20 s | intro |
| N1 | Depuis la fiche d'un employé, retrouvez d'un coup d'oeil ses horaires de travail, jour par jour. | 4,96 s | A — carte employé |
| N2 | Ici, Alice travaille le lundi de huit heures à dix-sept heures, avec une heure de pause. | 4,68 s | C — panneau détail, horaires actuels |
| N3 | Un clic sur Modifier, et vous ajustez directement l'heure de début, l'heure de fin, et la pause, jour par jour. | 6,50 s | E — modale "Horaires de travail" |
| N4 | Ajoutez une plage horaire pour un autre jour, par exemple pour renforcer l'équipe un soir de forte affluence. | 5,75 s | G — nouveau créneau (Mardi) |
| N5 | Modifiez les heures à tout moment, pour coller aux besoins réels du service. | 4,00 s | H — ajustement des heures |
| N6 | Un clic sur Sauvegarder, et le nouveau planning s'applique aussitôt à l'employé. | 4,21 s | J — retour à la liste |
| N7 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | 6,87 s | claude1 — reveal + copied (réutilisé tel quel depuis `foodeatup-conge-employe-tuto`) |
| N8 | Collez-le dans la conversation : les horaires sont configurés en quelques secondes, à partir de la photo. | 5,28 s | claude3 — résultat chatbot |
| N9 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (CTA, réutilisé tel quel depuis `foodeatup-borne-tuto`) |

N7 et N9 réutilisés tels quels (texte générique identique aux tutos
précédents) — zéro crédit ElevenLabs dépensé sur ces deux lignes.

## Découpage

Segments dimensionnés dès le départ à partir des durées VO réellement
mesurées (leçon appliquée d'entrée de jeu après les dérives rencontrées sur
`foodeatup-borne-tuto` et `foodeatup-accueil-role-tuto`) — **dérive nulle dès
le premier montage**.

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 6,00 s | RÉGLER SES HORAIRES PAR EMPLOYÉ |
| A | 0,20 → 2,00 | 6,50 s | carte employée "Alice Charbit" |
| B | 3,30 → 3,60 | 0,90 s | **zoom-punch** sur "Voir" |
| C | 4,00 → 6,00 | 6,00 s | panneau détail, horaires actuels |
| D | 6,80 → 7,10 | 0,90 s | **zoom-punch** sur "Modifier" (Horaires de travail) |
| E | 8,00 → 9,30 | 7,50 s | modale "Modifier l'employé", étape Horaires |
| F | 9,30 → 9,60 | 0,90 s | **zoom-punch** sur "+ Ajouter une plage horaire" |
| G | 11,00 → 14,00 | 7,00 s | nouveau créneau, jour basculé sur Mardi |
| H | 16,00 → 22,00 | 5,00 s | ajustement des heures (Mardi aligné sur Lundi) |
| I | 25,50 → 25,80 | 0,90 s | **zoom-punch** sur "Sauvegarder" |
| J | 26,50 → 30,44 | 5,50 s | retour à la liste, planning sauvegardé |
| claude1-3 | PNG générés | 6+3+6 s | séquence "Utiliser avec Claude" (reveal / copied / chatbot) |
| outro | carte | 6,20 s | CTA |

Transitions : `fade` sur les enchaînements continus (intro→A, A→B, C→D, E→F,
G→H, H→I, claude3→outro), `slideleft` sur les coupures de contexte (B→C,
D→E, F→G, I→J, J→claude1→claude2→claude3).

## Séquence "Utiliser avec Claude"

`mcp__FoodEatUp__update_employee_schedule` remplace entièrement le planning
hebdomadaire d'un employé (tableau de créneaux jour/début/fin/pause) — un
outil MCP existe donc bel et bien pour cette action, à la différence des
tutos précédents côté borne/PIN/congés. Le prompt de la vidéo exploite en
plus la capacité multimodale native de Claude (lecture d'image) pour partir
d'une photo d'un planning papier plutôt que de ressaisir chaque horaire à la
main :

```
Voici en photo le planning papier de [prénom] [nom] pour la semaine :
configure ses horaires de travail dans FoodEatUp exactement selon cette
photo, pour mon établissement FoodEatUp (ID [ID établissement]).
```

## Animations

Mêmes principes que toute la série : Ken Burns sur les cartes, xfade
(0,28 s), bandeaux d'étape, encadré orange pulsant sur les 3 clics (Voir,
Modifier, Sauvegarder). Séquence "Utiliser avec Claude" en 3 étages
(reveal/copied/chatbot) via `claude_prompt_sequence.py`, réutilisée telle
quelle. Pas de mini-animation dédiée supplémentaire.

## Astuce du chef — cas d'usage horaires

L'astuce du chef publiée sur Lovable couvre deux cas d'usage concrets
demandés explicitement par Michael : (1) configurer les horaires d'un
employé directement à partir d'une photo d'un planning papier existant, et
(2) ajuster les horaires d'un jour précis selon l'affluence prévue (réduire
un service creux, renforcer un soir chargé), sans reconstruire tout le
planning à la main.

## Statut publication

Montage terminé et checklist de compatibilité passée (H.264 High/yuv420p,
AAC 48 kHz stéréo, faststart, peak -7,2 dBFS, 0 erreur de décodage). Demande
explicite de Michael d'ajouter un prompt sur l'envoi en photo d'un planning
et l'ajustement selon l'affluence (message du 2026-08-03). Vidéo et vignette
hébergées via URL GitHub raw sur la branche
`claude/foodeatup-tutorial-video-vn7udf`. Lovable : tutoriel
`regler-ses-horaires-par-employe` ajouté dans `src/data/tutorials.ts` (module
`equipe-planning`), avec `chefTip` et `claudePrompt`.
