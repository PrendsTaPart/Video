# Tutoriel — Ouvrir ses créneaux de réservation FoodEatUp

Module 6b « Réservations Salle » (catégorie Agent IA Caroline & Salle),
catalogue 157 tutoriels : « 05 Ouvrir ses Créneaux de réservation ». Rush
fourni par Michael (89 s, 1920×828, 25 fps) : sur la page Réservations, une
« Nouvelle réservation » est saisie pour **samedi 15/08/2026 18:58** et
refusée — « Restaurant fermé à cette heure (horaires Storefront). » (le
15/08/2026 tombe bien un samedi, jour non coché dans les horaires). Le
correctif se trouve dans **Configuration boutique > Ma Vitrine > Infos &
Publication > Horaires d'ouverture** : chaque jour a une case à cocher +
une plage horaire, Samedi est décoché (« Fermé »). Cocher Samedi (11:30 AM
– 10:00 PM) puis cliquer Enregistrer (« Vitrine enregistrée ») ouvre le
créneau. De retour sur Réservations, le même client/date/heure passe cette
fois : une table est assignée (T5, puis T7 pour une 2ᵉ réservation), la
liste finit à **Total 13** avec deux réservations « En attente » le samedi
15/08. Durée livrée : **52,08 s** — H.264 High/yuv420p, AAC 48 kHz stéréo,
faststart. Audio : peak **-7,2 dBFS**. Décode 0 erreur, moov avant mdat
(faststart confirmé). Pas de clip avatar.

## Voix off (9 lignes)

| # | Texte | Durée | Ancrage |
|---|---|---:|---|
| N0 | Ouvrir vos créneaux de réservation dans FoodEatUp ? Une case à cocher suffit. | 4,41 s | carte d'intro |
| N1 | Créez une réservation : client, puis date, heure et couverts souhaités. | 4,68 s | segments A+B+C (saisie client) |
| N2 | Hors de vos horaires Storefront, FoodEatUp refuse la réservation et vous prévient. | 4,49 s | segment D+E (l'erreur, **zoom-punch** sur le message) |
| N3 | Direction Configuration boutique, Ma Vitrine, Infos et Publication : réglez vos horaires d'ouverture. | 6,87 s | segment F+G (**zoom-punch** sur « Ma Vitrine » dans le menu) |
| N4 | Cochez le jour concerné, ajustez les heures, puis enregistrez votre vitrine. | 4,26 s | segments H+I+J+K (**zoom-punch** sur la case Samedi, puis sur Enregistrer) |
| N5 | Retournez sur Réservations : le créneau est accepté, choisissez une table et validez, vos disponibilités sont ouvertes. | 6,77 s | segments L+M (nouvelle tentative + liste à jour) |
| N6 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | 4,41 s | **étage 1+2** — réutilisé tel quel depuis `foodeatup-dlc-tuto/vo/N6.mp3`, texte identique |
| N7 | Collez-le dans la conversation : Claude vérifie en quelques secondes si le créneau est disponible avant de réserver. | 5,69 s | **étage 3** (mockup chatbot) |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (CTA) — réutilisé tel quel depuis `foodeatup-dlc-tuto/vo/N8.mp3` |

N6/N8 copiés depuis `foodeatup-dlc-tuto` (texte identique, même voix Adam
FR `TGAegA0zNRi8I6nUdq3i`) — zéro crédit ElevenLabs dépensé sur ces deux
lignes. N0/N1/N2/N3/N4/N5/N7 générés neufs pour cette vidéo.

## Découpage

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 3,00 s | OUVRIR SES CRÉNEAUX DE RÉSERVATION (image fournie par Michael, non retouchée) |
| A | 0,20 → 0,80 | 2,60 s | Réservations — vue d'ensemble (Total 12) |
| B | 0,80 → 1,10 | 0,90 s | **zoom-punch** sur « + Nouvelle réservation » (1650, 310) |
| C | 3,00 → 9,00 | 4,60 s | Modal : coordonnées client (nom, téléphone, email) |
| D | 20,00 → 29,40 | 5,60 s | Créneau saisi (15/08/2026, 18:58, 4 couverts) → erreur horaires |
| E | 29,20 → 29,50 | 1,00 s | **zoom-punch** sur le message d'erreur (948, 497) |
| F | 36,50 → 39,20 | 3,40 s | Menu > Configuration boutique (sous-menu déroulé) |
| G | 39,20 → 39,50 | 0,90 s | **zoom-punch** sur « Ma Vitrine » (150, 545) |
| H | 44,80 → 47,90 | 3,60 s | Onglet Infos & Publication — Horaires d'ouverture (Samedi décoché) |
| I | 47,90 → 48,20 | 0,90 s | **zoom-punch** sur la case Samedi (190, 290) |
| J | 49,80 → 50,10 | 0,90 s | **zoom-punch** sur Enregistrer (1100, 699) |
| K | 53,80 → 55,30 | 2,60 s | Confirmation « Vitrine enregistrée » |
| L | 59,50 → 80,00 | 5,60 s | Nouvelle tentative : client, créneau, sélection de table (T7) |
| M | 85,00 → 89,00 | 3,80 s | Réservations à jour — Total 13, 2 réservations « En attente » samedi 15/08 |
| claude1 | carte générée | 3,00 s | reveal — prompt en gros, fond crème |
| claude2 | carte générée | 2,30 s | confirmation « Copié dans le presse-papiers ! » |
| claude3 | carte générée | 6,00 s | mockup chatbot Claude |
| outro | carte | 6,21 s | CTA (auto-étendu depuis 6,20 s pour absorber le reliquat de voix) |

Transitions : `slideleft` sur les coupes (E→F ouverture du menu, K→L retour
Réservations, M→claude1→claude2→claude3), `fade` partout ailleurs (action
continue à l'écran).

## Piège rencontré : mauvaise fenêtre source pour le zoom sur « Ma Vitrine »

Premier passage : le segment G ciblait `40.50 → 40.80`, une fenêtre où le
menu déroulant est **déjà refermé** (retour à la page Réservations nue) —
le zoom-punch encadrait donc l'en-tête du tableau, pas le lien « Ma
Vitrine ». Cause : à `t=39` le menu est bien ouvert avec le curseur sur
« Ma Vitrine » (confirmé par extraction d'image), mais il se referme
avant `t=40` (la page Réservations réapparaît nue dès `t=40-41`), et le
site vitrine ne charge qu'à partir de `t≈42`. Corrigé en resserrant F sur
`36.50 → 39.20` et G sur `39.20 → 39.50`, pendant que le menu est encore
ouvert — vérifié frame par frame après correction : l'encadré orange tombe
bien sur « Ma Vitrine ». Même leçon que le « Bug corrigé » de
`foodeatup-dlc-tuto` : toujours vérifier le zoom-punch sur une frame
extraite du rendu final, pas seulement sur l'aperçu du rush.

## Séquence Claude — module partagé

`mcp__FoodEatUp__reservation_availability(establishment_id, date, time,
party_size)` vérifie exactement ce que cette vidéo montre : restaurant
ouvert (horaires Storefront) + tables libres pour un créneau donné, avant
même de tenter une réservation. Séquence rendue par
`videos/_shared/claude_prompt_sequence.py`, seuls changent le texte du
prompt et la réplique assistant :

> Vérifie la disponibilité d'un créneau le [date] à [heure] pour [nombre
> de couverts] couverts, pour mon établissement FoodEatUp (ID [ID
> établissement]).

Réplique assistant : « Bien sûr ! Je vérifie la disponibilité de ce
créneau… ». Même texte de prompt côté fiche Lovable (`claudePrompt`).

## Animations

Mêmes principes que toute la série : Ken Burns sur les cartes, xfade
(0,28 s), bandeaux d'étape rendus en PNG (PIL) + `overlay` (le `drawbox`
de cet ffmpeg 6.1.1 n'anime pas son `x`), encadré orange statique sur les
clics/champs (`punch_highlight`, pas de pulsation animée — `drawbox`
n'évalue ses coordonnées qu'une fois sur ce build). Pas de clip avatar.

## Statut publication

Montage terminé, checklist de compatibilité passée, 5 zoom-punchs vérifiés
frame par frame sur le rendu final. Livré via `SendUserFile`. Prochaines
étapes une fois l'accord confirmé : upload RapidoCMS + vignette, ajout sur
Lovable (`src/data/tutorials.ts`, module `reservation-salle`,
`claudePrompt` ci-dessus), et entrée dans le tableau "Tutoriels publiés"
de `LOVABLE-FOODEATUP-DOCS.md` + mise à jour de
`videos/PROGRESSION-157-TUTORIELS.md`.
