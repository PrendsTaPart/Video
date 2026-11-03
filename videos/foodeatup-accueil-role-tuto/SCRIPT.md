# Tutoriel — Découvrir son accueil selon son rôle (module Équipe & Planning)

Dixième vidéo du module `equipe-planning` (catalogue #14 — voir
`CATALOGUE-157-TUTORIELS.md`). Durée livrée : **67,64 s** — H.264 High/yuv420p,
AAC LC 48 kHz stéréo, faststart (moov avant mdat confirmé). Audio : max
**-7,2 dBFS** / mean -22,3 dBFS. Decode 0 erreur.

## Ce que montre le rush

Le rush (41,52 s, capture 1920x828 @25fps, pas de chrome navigateur à rogner)
montre : l'espace personnel d'un manager (tableau de bord, modules de gestion
accessibles) → navigation Équipe > Rôles → liste des rôles (Admin, Manager)
avec le nombre de permissions actives par rôle → clic sur "Modifier" la carte
Manager → modale de permissions par module, défilement jusqu'à la ligne
**HACCP (0/41)** — un manager n'a par défaut aucun accès à ce module → retour
à l'espace personnel, dont l'affichage se recalcule selon les permissions du
rôle.

## Voix off (9 lignes, voix Adam FR `TGAegA0zNRi8I6nUdq3i`)

| # | Texte | Durée | Segment |
|---|---|---:|---|
| N0 | Chaque employé a son propre accueil dans FoodEatUp, selon son rôle et ses permissions. Voici comment ça marche. | 6,35 s | intro |
| N1 | Le manager voit tous les modules de gestion : stocks, production, finances, ressources humaines, et plus encore. | 6,71 s | A — tour de "Mon espace" (manager) |
| N2 | Direction Équipe puis Rôles, pour gérer les accès de toute votre équipe. | 3,76 s | C — nav Équipe > Rôles |
| N3 | Chaque rôle, Admin, Manager, ou un rôle que vous créez vous-même, a son propre nombre de permissions. | 6,03 s | E — liste des rôles, compteurs |
| N4 | Cliquez sur Modifier pour ajuster précisément les modules accessibles, un par un. | 4,44 s | G — modale de permissions par module |
| N5 | Un manager n'a par exemple aucun accès HACCP par défaut, à vous de l'activer si besoin. Et l'accueil de chaque employé se met à jour automatiquement dès que ses permissions changent. | 11,70 s | H — ligne HACCP (0/41) |
| N6 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | 4,41 s | claude1 — reveal + copied (réutilisé tel quel depuis `foodeatup-contrat-tuto`) |
| N7 | Collez-le dans la conversation : le rôle est appliqué à l'employé en quelques secondes. | 4,44 s | claude3 — résultat chatbot |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (CTA, réutilisé tel quel depuis `foodeatup-borne-tuto`) |

N6 et N8 réutilisés tels quels (texte générique identique aux tutos
précédents) — zéro crédit ElevenLabs dépensé sur ces deux lignes.

## Découpage

Segments largement dimensionnés dès le départ après la leçon des tutos
précédents (mesurer chaque ligne VO réelle avant de fixer la durée du
segment) — première tentative avec `INTRO_D=4.00s` trop courte pour les
6,35 s de N0, provoquant une dérive en cascade de 2,85 s à 4,28 s sur
N1–N6. Corrigé en élargissant l'intro (4,00→7,00 s) et les segments
B/C/E/H/I ; seconde tentative : **dérive nulle, toutes les lignes sur leur
ancre**.

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 7,00 s | DÉCOUVRIR SON ACCUEIL SELON SON RÔLE |
| A | 0,20 → 2,00 | 3,00 s | tour de "Mon espace" (manager) |
| B | 2,00 → 9,00 | 6,00 s | grille de modules de gestion |
| C | 17,40 → 18,30 | 4,00 s | navigation Équipe > Rôles |
| D | 18,30 → 18,60 | 0,90 s | **zoom-punch** sur l'item "Rôles" du menu |
| E | 20,00 → 23,50 | 7,00 s | liste des rôles (Admin, Manager) |
| F | 24,00 → 24,30 | 0,90 s | **zoom-punch** sur "Modifier" (carte Manager) |
| G | 25,00 → 33,00 | 5,50 s | modale de permissions par module |
| H | 33,50 → 34,50 | 8,00 s | ligne HACCP (0/41) |
| I | 36,60 → 41,52 | 7,50 s | retour "Mon espace", accueil recalculé |
| claude1-3 | PNG générés | 6+3+6 s | séquence "Utiliser avec Claude" (reveal / copied / chatbot) |
| outro | carte | 6,20 s | CTA |

Transitions : `fade` sur les enchaînements continus (intro→A, A→B, C→D,
E→F, G→H, claude3→outro), `slideleft` sur les coupures de contexte
(B→C, D→E, F→G, H→I, I→claude1→claude2→claude3).

## Séquence "Utiliser avec Claude"

`mcp__FoodEatUp__create_employee` accepte un champ `role` (string, valeurs
courantes documentées : `employee, manager, chef, cuisinier, serveur`, sans
enum stricte). Le prompt de la vidéo se limite donc, honnêtement, à
l'affectation d'un rôle **déjà existant** à un nouvel employé — aucun outil
MCP ne permet de créer un rôle personnalisé avec ses propres permissions
(action UI uniquement, via Équipe > Rôles > Créer un rôle) :

```
Crée l'employé [prénom] [nom], email [email], téléphone [téléphone], avec
le rôle [rôle], pour qu'il ait exactement les permissions déjà définies
pour ce rôle, pour mon établissement FoodEatUp (ID [ID établissement]).
```

## Animations

Mêmes principes que toute la série : Ken Burns sur les cartes, xfade
(0,28 s), bandeaux d'étape, encadré orange pulsant sur les 2 clics (item
"Rôles", bouton "Modifier"). Séquence "Utiliser avec Claude" en 3 étages
(reveal/copied/chatbot) via `claude_prompt_sequence.py`, réutilisée telle
quelle. Pas de mini-animation dédiée supplémentaire : le rush illustre déjà
nativement le concept "accueil selon le rôle" (deux rôles, deux univers de
modules).

## Astuce du chef — cas d'usage par métier

Chaque métier de l'établissement a son propre accès : le **chef de partie**
et le **second de cuisine** n'ont besoin que des modules Production, Recettes,
Stocks et HACCP ; le **serveur** n'a besoin que du Plan de salle, des
Commandes et du Planning ; le **directeur** a accès à tout, y compris
Finances et Ressources Humaines. Trois cas concrets :

1. **Un stagiaire arrive** : donnez-lui directement un rôle déjà existant
   (ex. `serveur`) pour hériter instantanément de toutes ses permissions,
   sans tout reconfigurer à la main.
2. **Un rôle métier n'existe pas encore** (ex. "Second de cuisine") : créez-le
   dans Équipe > Rôles > Créer un rôle, cochez uniquement Production,
   Recettes, Stocks et HACCP, puis créez l'employé avec ce rôle — il hérite
   aussitôt de ce périmètre exact.
3. **Un employé change de poste** (ex. serveur promu directeur adjoint) :
   modifiez son rôle sur sa fiche employé, son accueil et ses accès se
   recalculent automatiquement, aucune reconfiguration manuelle nécessaire.

## Statut publication

Montage terminé et checklist de compatibilité passée (H.264 High/yuv420p,
AAC 48 kHz stéréo, faststart, peak -7,2 dBFS, 0 erreur de décodage). Demande
explicite de Michael de traiter plusieurs cas d'usage par métier (chef de
partie, second de cuisine, serveur, directeur) avec plusieurs prompts Claude
en astuce du chef (message du 2026-08-03) : vidéo et vignette à héberger via
URL GitHub raw sur la branche `claude/foodeatup-tutorial-video-vn7udf`.
Lovable : tutoriel `decouvrir-son-accueil-selon-son-role` à ajouter dans
`src/data/tutorials.ts` (module `equipe-planning`), avec `chefTip` enrichi
(cas d'usage par métier) et 2 `claudePrompts[]` (affecter un rôle existant à
un stagiaire ; promouvoir un employé via un rôle personnalisé déjà créé côté
UI).
