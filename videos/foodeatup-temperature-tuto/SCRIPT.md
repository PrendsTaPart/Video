# Tutoriel — Relever une température d'équipement (HACCP)

Module « Hygiène & HACCP ». Durée livrée : **44,36 s** — H.264 High/yuv420p 1920x828
25 fps, AAC LC 48 kHz stéréo, faststart. Audio : true peak **-7,3 dBFS** (sous la
marge cible du pipeline). Decode 0 erreur, moov avant mdat (faststart confirmé).

## Particularité du rush

Enregistrement d'écran **1920x1020**, à variable frame rate (~17 fps effectifs sur
20,73 s), qui embarque encore le chrome du navigateur (barre d'onglets + barre
d'URL + barre de favoris). Le contenu applicatif commence **exactement à y=191**
(mesuré par balayage colorimétrique, pas estimé) : un `crop=1920:828:0:192` retombe
donc pile sur le canevas natif de la série, sans mise à l'échelle et sans perdre un
pixel d'interface. Aucun letterbox, aucun recadrage créatif.

## Voix off (9 lignes)

Voix Adam FR (`TGAegA0zNRi8I6nUdq3i`), `eleven_multilingual_v2`.

| # | Texte | Durée | Segment |
|---|---|---:|---|
| N0 | Relever la température de vos équipements dans FoodEatUp ? C'est deux clics, et c'est tracé. | 4,86 s | carte intro (déborde sur A) |
| N1 | Chaque équipement est listé avec sa plage cible : Frigo 5, entre zéro et quatre degrés. | 5,04 s | B |
| N2 | Ajustez la température relevée avec les boutons plus et moins. | 3,11 s | C |
| N3 | Cliquez sur Enregistrer les relevés de température. | 2,69 s | clic D |
| N4 | Confirmez : un équipement modifié, on enregistre. | 2,95 s | E (modale de confirmation) |
| N5 | C'est enregistré, et daté. Neuf degrés pour un maximum de quatre : le relevé bascule aussitôt en non conforme. | 6,64 s | G |
| N6 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | 4,41 s | étages 1+2 (réutilisé) |
| N7 | Collez-le dans la conversation : votre relevé de température est enregistré en quelques secondes. | 5,02 s | étage 3 |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (CTA, réutilisé) |

N6/N8 réutilisés depuis `foodeatup-vitrine-tuto/vo/` (lignes génériques de la série).
N7 régénéré : il nomme l'objet créé, il n'est jamais réutilisable tel quel.

## Découpage

| Seg | Source | Départ | Sortie | Contenu |
|---|---|---:|---:|---|
| intro | carte | 0,00 | 3,40 s | RELEVER UNE TEMPÉRATURE D'ÉQUIPEMENT |
| A | 0,30 → 3,20 | 3,12 | 2,48 s | liste des équipements, compteurs du jour à zéro |
| B | 3,20 → 6,60 | 5,32 | 5,56 s | Frigo 5 à 6,0 °C et sa plage cible (min 0 °C, max 4 °C) |
| C | 6,60 → 10,45 | 10,60 | 3,80 s | steppers − / + : 6,0 → 7,5 → 8,0 → 9,0 °C |
| D | 10,60 → 10,95 | 14,12 | 1,16 s | **zoom-punch** sur Enregistrer les relevés de température (1570, 754) |
| E | 11,05 → 12,30 | 15,00 | 3,20 s | modale « Enregistrer les relevés ? 1 équipement(s) modifié(s) » |
| E2 | 12,30 → 12,50 | 17,92 | 0,92 s | **zoom-punch** sur Oui, enregistrer! (871, 607) |
| F | 13,35 → 15,25 | 18,56 | 3,24 s | modale « Enregistré ! Les relevés ont été sauvegardés avec succès. » |
| G | 15,40 → 20,60 | 21,52 | 6,84 s | compteurs à jour : 1 total aujourd'hui, 1 non conforme |
| claude1 | carte générée | 28,08 | 3,00 s | reveal — prompt en gros, fond crème |
| claude2 | carte générée | 30,80 | 1,72 s | confirmation « Copié dans le presse-papiers ! » |
| claude3 | carte générée | 32,24 | 4,20 s | mockup chatbot Claude |
| outro | carte | 36,16 | 8,20 s (auto-étendue) | CTA |

Coordonnées de clic mesurées par seuillage colorimétrique sur les frames réelles,
puis décalées dans l'espace recadré (y source − 192 px de chrome navigateur).

Rush court (20,4 s exploitables) pour ~40 s de narration : les segments de modale
(E, F) tournent autour de ×0,4-0,6, ce qui ne se voit pas — ce sont des boîtes de
dialogue fixes. Les segments avec du mouvement réel (A, B, C, G) restent entre
×0,76 et ×1,17.

## Séquence Claude — module partagé

Outil correspondant exactement à ce que montre le rush :
`add_temperature(establishment_id, equipment_id, temperature, measured_at)`.

> Enregistre une température de [température] degrés pour l'équipement
> [nom de l'équipement] dans mon établissement FoodEatUp (ID [ID établissement]).

Réponse assistant : « Bien sûr ! J'enregistre votre relevé de température… »
Même texte de prompt côté fiche Lovable (`claudePrompts`).

## Animations

Mêmes principes que toute la série : Ken Burns sur les cartes, xfade 0,28 s,
bandeaux d'étape, encadré orange pulsant sur les 2 clics.

## Bandeaux d'étape — rendus en PNG + overlay (écart avec le reste de la série)

Sur ce build, `drawbox` **n'évalue son expression `x` qu'une seule fois, à
l'initialisation** (ffmpeg 6.1.1). Avec l'expression de glissement de la série,
`t=0` place le bandeau à `x=-640`, entièrement hors champ : le panneau bleu et le
filet orange ne s'affichaient jamais, seul le texte apparaissait (`drawtext`, lui,
réévalue à chaque frame) — du blanc sur blanc, illisible. Le bandeau est donc
dessiné une fois en PNG RGBA (PIL) puis glissé avec `overlay`, qui réévalue bien
son `x` par frame. Rendu identique, animation comprise.

Deux conséquences à ne pas perdre :

- `fps=25` doit passer **avant** l'`overlay`. Le rush est en VFR, et le framesync
  d'`overlay` jette les dernières frames d'une entrée VFR : le segment E sortait à
  2,32 s au lieu de 3,20 s tant que le flux n'était pas remis en CFR en amont.
  PNG bouclé (`-loop 1`) + `shortest=1` : c'est la vidéo qui fixe la durée, comme
  dans le chemin `-vf` classique.
- Le PNG lève au passage l'interdiction d'apostrophe dans les libellés de bandeau
  (le piège `drawtext` documenté dans le workflow) — les accents, eux, n'ont
  jamais posé problème.

## Statut publication

Vidéo livrée à Michael. Fiche ajoutée au site Lovable
(workspace Contact.prendstapart, projet FoodEatUp Academy / `foodeatup-guide-star`).
Publication RapidoCMS + LinkedIn non demandée sur ce tutoriel.
