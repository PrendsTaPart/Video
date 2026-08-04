# Tutoriel — Lire ses notifications et tâches du jour FoodEatUp

Septième vidéo du module `equipe-planning` (Drive : "LIRE SES NOTIFICATIONS ET
TÂCHES DU JOUR"). Durée livrée : **29,2 s** — H.264 High/yuv420p, AAC 48 kHz
stéréo, faststart. Audio : true peak **-7,3 dBFS**. Decode 0 erreur, moov avant
mdat.

## Ce que montre le rush

Le rush (18,6 s, 1920x1020) montre la page "mon espace" (hub employé) → clic sur
la cloche de notifications (badge "3") → panneau "Mes notifications" (5
notifications au total) → filtres "Tout" / "Congés" / "Planning" / "Tâches",
cliqués un à un :
- **Tout** : Congé approuvé, Nouveau shift, Tâche à faire (HACCP), Modification
  planning, Rappel solde congés.
- **Congés** : Congé approuvé + Rappel solde congés.
- **Planning** : Nouveau shift + Modification planning.
- **Tâches** : Tâche à faire — "Compléter le contrôle température frigo n°2
  avant 18h" (badge "Attention").

## Pas de séquence Claude

Aucun outil MCP FoodEatUp ne couvre la lecture des notifications employé (flux
self-service côté client, rien à créer ni consulter via un outil serveur) —
même raison que `creer-son-code-pin` et `se-connecter-cote-employe`. Pas de
`claudePrompt`/`claudePrompts` sur cette fiche.

## Voix off (6 lignes, voix Adam FR `TGAegA0zNRi8I6nUdq3i`)

| # | Texte | Durée | Segment |
|---|---|---:|---|
| N0 | Chaque notification importante remonte directement dans son espace. | 3,76 s | intro |
| N1 | La cloche indique combien sont encore à lire. | 2,35 s | A — mon espace, badge cloche |
| N2 | Congé approuvé, nouveau shift, tâche urgente : tout au même endroit. | 4,08 s | B/C — clic cloche, panneau Tout |
| N3 | Il peut aussi filtrer par congés, planning ou tâches. | 2,87 s | D/E/F/G — clics filtres |
| N4 | Une tâche HACCP urgente ? Il la voit tout de suite. | 3,94 s | H/I — filtre Tâches |
| N5 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (CTA, réutilisé tel quel depuis `foodeatup-produits-tuto`) |

N5 réutilisé tel quel — zéro crédit ElevenLabs dépensé sur cette ligne. Drift
maximal au premier rendu : 0,66 s (aucune cascade), outro auto-étendue de 6,20 à
6,76 s pour caler le CTA.

## Découpage

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 3,60 s | LIRE SES NOTIFICATIONS ET TÂCHES DU JOUR |
| A | 0,20 → 3,00 | 3,60 s | "mon espace", badge cloche "3" |
| B | 5,40 → 5,70 | 1,00 s | **zoom-punch** sur la cloche (1670, 325) |
| C | 5,80 → 9,60 | 4,80 s | panneau "Mes notifications", filtre Tout |
| D | 10,00 → 10,30 | 1,00 s | **zoom-punch** sur le filtre "Congés" (1295, 533) |
| E | 10,35 → 13,10 | 3,20 s | vue filtrée Congés |
| F | 13,30 → 13,60 | 1,00 s | **zoom-punch** sur le filtre "Planning" (1445, 533) |
| G | 13,65 → 15,30 | 2,20 s | vue filtrée Planning |
| H | 15,40 → 15,70 | 1,00 s | **zoom-punch** sur le filtre "Tâches" (1590, 533) |
| I | 15,75 → 18,60 | 3,80 s | vue filtrée Tâches (HACCP) |
| outro | carte | 6,76 s (auto-étendue) | CTA |

Coordonnées de clic mesurées directement sur les frames extraites du rush,
résolution source native 1920x1020.

## Animations

Mêmes principes que toute la série : Ken Burns sur les cartes, xfade (0,28 s,
uniquement `fade` — aucune vraie coupure de scène ici, tout se passe sur le même
écran/panneau), bandeaux d'étape, encadré orange pulsant sur les 4 clics (cloche
+ 3 filtres). Pas de séquence Claude animée. Pas de clip avatar dans ce dossier.

## Statut publication

Montage terminé et checklist de compatibilité passée (H.264 High/yuv420p, AAC 48 kHz
stéréo, faststart, peak -7,3 dBFS, 0 erreur de décodage). Validée le 2026-08-03 et
publiée sur Lovable (`lire-ses-notifications`, module `equipe-planning`, 18e
entrée de `videos/LOVABLE-FOODEATUP-DOCS.md`), avec un `chefTip` sur les alertes
HACCP à échéance serrée. Pas de `claudePrompt` (aucun outil MCP ne couvre la
lecture des notifications employé). Pas d'upload RapidoCMS/LinkedIn (RapidoCMS
non authentifié dans cette session).
