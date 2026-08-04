# Tutoriel — Voir son planning côté employé FoodEatUp

Sixième vidéo du module `equipe-planning` (Drive : "VOIR SON PLANNING CÔTÉ
EMPLOYÉ"). Durée livrée : **29,2 s** — H.264 High/yuv420p, AAC 48 kHz stéréo,
faststart. Audio : true peak **-7,2 dBFS**. Decode 0 erreur, moov avant mdat.

## Ce que montre le rush

Le rush (26,2 s, 1920x1020) montre la page "Mon planning" côté employé
(`foodeatup.com/employee/26/planning`) : stats de la semaine (heures planifiées,
shifts, tâches) → défilement jour par jour (repos, puis tâches "Prendre les
commandes", "Nettoyage de bar", "Gestion de commandes en ligne") → clic sur la
case de la tâche du jour → tâche cochée, toast "Tâche faite" → retour en haut :
le compteur passe de 0/3 à 1/3 → clic "Ajouter à mon agenda" (export du planning
en ICS vers l'agenda personnel de l'employé).

Un second onglet "Planning Équipe - Laravel" reste ouvert en arrière-plan tout du
long mais n'est jamais utilisé dans le rush — non repris dans le montage.

**Bruit d'enregistrement non repris :** un toast de l'extension antivirus McAfee
WebAdvisor apparaît en bas à droite après le clic sur "Ajouter à mon agenda"
(propre à la machine d'enregistrement, aucun rapport avec FoodEatUp) — le
montage recadre serré sur le bouton pour ne jamais le montrer à l'écran.

## Un seul claudePrompt (outil en lecture seule)

Aucun outil MCP FoodEatUp ne permet de cocher une tâche comme faite ni d'exporter
un planning en ICS (actions client-side / self-service). En revanche,
`mcp__FoodEatUp__list_plannings(establishment_id, week)` liste les shifts de la
semaine — un employé peut donc demander à Claude de lui afficher son planning.
Un seul `claudePrompt` proposé côté Lovable, pas de `claudePrompts[]` (un seul cas
d'usage réellement couvert par un outil MCP existant).

## Voix off (7 lignes, voix Adam FR `TGAegA0zNRi8I6nUdq3i`)

| # | Texte | Durée | Segment |
|---|---|---:|---|
| N0 | Chaque employé retrouve son planning et ses tâches, personnellement. | 3,53 s | intro |
| N1 | Ici, ses heures planifiées, ses shifts et ses tâches de la semaine. | 4,08 s | A — stats de la semaine |
| N2 | Jour par jour : repos, horaires et tâches à faire. | 3,34 s | B — défilement de la semaine |
| N3 | Il coche une tâche terminée, elle passe faite instantanément. | 3,29 s | C/D — clic case + tâche faite |
| N4 | Le compteur de tâches se met à jour en direct. | 2,35 s | E — stats 1/3 |
| N5 | Il peut aussi ajouter son planning à son propre agenda. | 3,11 s | F — clic Ajouter à mon agenda |
| N6 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (CTA, réutilisé tel quel depuis `foodeatup-produits-tuto`) |

N6 réutilisé tel quel — zéro crédit ElevenLabs dépensé sur cette ligne. Premier
rendu avec intro/segment A trop courts (drift jusqu'à 1,68s en cascade) : corrigé
en élargissant `INTRO_D` (3,2→3,9) et le segment A (3,6→4,5) pour absorber les
lignes N0/N1 sans déborder — drift final ≤0,11s sur tout sauf la carte de fin
(qui s'étend automatiquement pour caler le CTA, comportement normal).

## Découpage

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 3,90 s | VOIR SON PLANNING CÔTÉ EMPLOYÉ |
| A | 0,20 → 3,00 | 4,50 s | "Mon planning", stats 0h/0/0-3 |
| B | 3,00 → 6,50 | 5,00 s | défilement semaine (repos + tâches) |
| C | 13,00 → 13,50 | 1,00 s | **zoom-punch** sur la case "Prendre les commandes" (150, 500) |
| D | 13,60 → 16,50 | 3,60 s | tâche cochée, toast "Tâche faite" |
| E | 18,00 → 19,60 | 2,60 s | retour en haut, compteur "1/3" |
| F | 20,70 → 21,15 | 1,00 s | **zoom-punch** sur "Ajouter à mon agenda" (1640, 527) |
| outro | carte | 8,48 s (auto-étendue) | CTA |

Coordonnées de clic mesurées directement sur les frames extraites du rush,
résolution source native 1920x1020 (différente des tutos précédents, 1920x828).

## Transitions

`slideleft` sur les 2 coupures (B→C retour en haut de page + clic checkbox,
D→E retour en haut + stats) ; `fade` partout ailleurs (continuité de scroll/clic
sur le même écran).

## Animations

Mêmes principes que toute la série : Ken Burns sur les cartes, xfade (0,28 s),
bandeaux d'étape, encadré orange pulsant sur les 2 clics (case à cocher, bouton
agenda). Pas de séquence Claude animée (3 temps) — un seul `claudePrompt` texte
suffit ici vu qu'il n'y a qu'un seul outil MCP pertinent. Pas de clip avatar dans
ce dossier.

## Statut publication

Montage terminé et checklist de compatibilité passée (H.264 High/yuv420p, AAC 48 kHz
stéréo, faststart, peak -7,2 dBFS, 0 erreur de décodage). Validée le 2026-08-03 et
publiée sur Lovable (`voir-son-planning-cote-employe`, module `equipe-planning`,
17e entrée de `videos/LOVABLE-FOODEATUP-DOCS.md`), avec 3 `claudePrompts` (semaine
en cours, semaine prochaine, comparaison planning prévu / heures pointées via
`list_plannings` + `list_attendances`) et un `chefTip` détaillant ces 3 cas
d'usage, à la demande explicite du demandeur. Pas d'upload RapidoCMS/LinkedIn
(RapidoCMS non authentifié dans cette session).
