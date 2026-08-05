# Tutoriel — Vue publique Fidélité côté client

Module **Marketing, Fidélité & Iris** (`marketing-fidelite`, 0/24 publiés avant cette
vidéo) — catalogue `videos/CATALOGUE-157-TUTORIELS.md`, entrée « 20 Vue publique
Fidélité côté client ». Rush fourni par Michael : capture d'écran (19,28 s, 1920x828,
25 fps) de la page fidélité publique **GoSushi Démo**, côté client (pas d'administration
restaurateur dans cette vidéo).

Intrants : `assets/intro.jpg` (carte « VUE CLIENT FIDÉLITÉ », CTA « Rejoignez-nous »),
`assets/outro.jpg` (carte CTA générique, réutilisée telle quelle), `assets/screen.mp4`.

## Déroulé du rush

1. **0,4 → 7,6 s** — onglet **Fidélité** (actif par défaut) : carte « Bonjour »
   (solde 0 point), bandeau « Points doublés midi », progression vers la prochaine
   récompense (café offert, 0/2 pts), catalogue **Mes récompenses** (Tiramisu 80 pts,
   Bon 5€ 100 pts, café offert 2 pts), **Historique des points** (état vide).
2. **7,6 → 11,8 s** — clic sur l'onglet **Mes commandes** : état vide (« Aucune
   commande pour l'instant », bouton « Voir la carte »).
3. **11,8 → 16,85 s** — le rush revient sur l'onglet Fidélité (même contenu qu'en
   1., aucune information nouvelle) : **coupé au montage**, temps mort de redite.
4. **16,85 → 19,28 s** — clic sur l'onglet **Mes infos** → page **Mon compte** :
   connexion passwordless (email + bouton « Recevoir mon code »).

⚠️ **Point de vigilance rencontré — mauvais repérage du clic "Mes infos"** : un
premier passage au montage avait placé la bascule vers "Mon compte" à 16,0 s
(lecture d'une frame mal indexée). Vérification image par image après un premier
rendu incohérent (bandeau et contenu ne correspondaient plus au bon segment) :
la vraie bascule a lieu entre **17,10 et 17,14 s**, pas 16,0 s. Toujours vérifier
un point de coupure au **md5sum d'une frame extraite du MP4 final**, pas seulement
d'un montage mental des durées de segments.

## Voix off (8 lignes, Adam FR `TGAegA0zNRi8I6nUdq3i`)

| # | Texte | Durée | Segment |
|---|---|---:|---|
| N0 | Voici la page fidélité que vos clients retrouvent, sans rien installer. | 3,66 s | carte intro + A |
| N1 | Ils voient leur solde de points, et ce qu'il reste avant leur prochaine récompense. | 3,79 s | B1 — solde et progression |
| N2 | Toutes les récompenses du programme s'affichent, avec leur coût en points et l'historique des gains. | 5,09 s | B2 — récompenses et historique |
| N3 | Un onglet Mes commandes centralise aussi leur suivi, juste à côté. | 4,00 s | D — onglet Mes commandes |
| N4 | Et pour se connecter, un simple email suffit : un code reçu, aucun mot de passe à retenir. | 5,46 s | F — Mon compte (passwordless) |
| N5 | Vous pouvez aussi consulter ce programme depuis Claude : copiez ce prompt, remplacez les crochets. | 5,15 s | étages 1+2 (reveal + copié) |
| N6 | Collez-le dans la conversation : solde de points et récompenses de votre client, en quelques secondes. | 5,33 s | étage 3 (chatbot mockup) |
| N7 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (CTA, **réutilisé** octet-identique depuis `foodeatup-fiche-plat-tuto/vo/N8.mp3`, zéro crédit ElevenLabs) |

## Découpage (segments source → sortie)

| Seg | Source | Sortie | Contenu | Bandeau |
|---|---|---:|---|---|
| intro | carte | 2,60 s | VUE CLIENT FIDÉLITÉ | — |
| A | 0,40 → 1,90 | 1,50 s | établissement (carte + onglets) | — |
| B1 | 1,90 → 3,60 | 3,85 s | solde + progression récompense | 1 - Solde et prochaine recompense |
| B2 | 3,60 → 7,60 | 5,25 s | récompenses + historique | 2 - Vos recompenses disponibles |
| C | 7,60 → 7,95 | 0,90 s | **zoom-punch** onglet Mes commandes (801, 338) | — |
| D | 7,95 → 11,80 | 4,15 s | Mes commandes (état vide) | 3 - Onglet Mes commandes |
| E | 16,85 → 17,12 | 0,90 s | **zoom-punch** onglet Mes infos (1065, 338) | — |
| F | 17,12 → 19,28 | 5,65 s | Mon compte (passwordless) | 4 - Connexion sans mot de passe |
| claude1 | générée | 2,60 s | reveal — prompt en gros, fond crème | — |
| claude2 | générée | 2,40 s | confirmation « Copié dans le presse-papiers ! » | — |
| claude3 | générée | 6,00 s | mockup chatbot Claude | — |
| outro | carte | 7,57 s (auto-étendue) | CTA | — |

**Coupe volontaire** : 11,80 → 16,85 s (retour sur l'onglet Fidélité, redite sans
information nouvelle) — même logique que les coupes de spinner/chargement déjà
documentées sur d'autres tutos de la série.

## Séquence Claude — lecture seule (vue client, pas de création)

Cette vidéo montre une page **publique côté client** : aucune action de création
n'y a lieu, uniquement de la consultation (solde de points, récompenses). Les deux
outils MCP FoodEatUp qui correspondent exactement à ce qui est affiché à l'écran :

- `mcp__FoodEatUp__get_loyalty_account(establishment_id, email)` — solde de points
  et prochaine récompense (carte du haut).
- `mcp__FoodEatUp__list_loyalty_rewards(establishment_id)` — catalogue de
  récompenses échangeables (section « Mes récompenses »).

Prompt combiné utilisé dans la vidéo et sur la fiche Lovable (`claudePrompt`) :

> Vérifie le solde de points, la prochaine récompense et le catalogue de
> récompenses fidélité de [email du client] pour mon établissement FoodEatUp
> (ID [ID établissement]).

## Bug rencontré et corrigé — bandeaux d'étape invisibles (`drawbox`/`t`)

Premier rendu : bandeaux d'étape réduits à du texte blanc fantôme, sans plaque
bleue ni filet orange visibles (bug déjà documenté dans
`FOODEATUP-TUTORIELS-WORKFLOW.md` — `drawbox` sur cet ffmpeg 6.1.1 n'évalue
`x`/`y`/`w`/`h` qu'une fois, à la configuration du filtre, donc l'expression de
glissement en `t` reste figée hors-écran). Corrigé en reprenant le patron de
référence de `videos/foodeatup-production-ingredients-tuto/build.py` : bandeau
rendu une fois en PNG RGBA (PIL), glissé avec `overlay` (qui honore `eval=frame`),
`shortest=1` obligatoire (le PNG est une entrée `-loop 1` infinie).

## Statut publication

Vidéo montée, vérifiée (bandeaux, zoom-punch, séquence Claude, peak audio
-7,19 dBFS), livrée pour validation puis **publiée le 2026-08-05 sur instruction
explicite** : upload RapidoCMS (vidéo + vignette) et mise à jour de la fiche
Lovable préexistante `vue-publique-fidelite-cote-client` dans `src/data/
tutorials.ts` (commit `5679dd3a`, module `marketing-fidelite`). LinkedIn non
demandé pour cette vidéo. Voir `videos/LOVABLE-FOODEATUP-DOCS.md` (tableau
« Tutoriels publiés ») et `videos/PROGRESSION-157-TUTORIELS.md`.
