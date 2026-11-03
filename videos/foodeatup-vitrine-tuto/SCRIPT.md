# Tutoriel — Ouvrir sa vitrine en ligne FoodEatUp

Dossier Drive « Configuration de sa vitrine ». Durée livrée : **50,4 s** — H.264
High/yuv420p, AAC 48 kHz stéréo, faststart. Audio : true peak **-4,3 dBFS**
(dans la marge cible du pipeline). Decode 0 erreur, moov avant mdat (faststart
confirmé).

Première vidéo avec **avatar HeyGen** depuis `foodeatup-boutique-tuto` (voix native
conservée, aucune ligne ElevenLabs générée pour ce battement — extraction directe
`vo/N0.mp3`, 7,08 s).

## Voix off (9 lignes)

| # | Texte | Durée | Segment |
|---|---|---:|---|
| N0 | (avatar, voix native) | 7,08 s | avatar |
| N1 | Choisissez un template parmi ceux proposés, comme Brasserie Parisienne. | 3,89 s | A + clic B |
| N2 | Dans l'onglet Carte, organisez vos catégories, vos plats et vos formules. | 4,08 s | C + D |
| N3 | Personnalisez le nom, le logo et la charte graphique de votre vitrine. | 4,02 s | E |
| N4 | Cliquez sur Publier le site pour la mettre en ligne. | 2,64 s | clic F |
| N5 | Votre vitrine est en ligne, prête à recevoir vos premiers clients ! | 3,42 s | G |
| N6 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | 4,41 s | étages 1+2 (réutilisé) |
| N7 | Collez-le dans la conversation : votre vitrine est configurée en quelques secondes. | 4,31 s | étage 3 |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (CTA, réutilisé) |

N6/N8 réutilisés depuis `foodeatup-tva-tuto/vo/`.

## Découpage

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 2,60 s | OUVRIR SA VITRINE EN LIGNE |
| avatar | clip natif | 7,08 s | accroche du chef (voix native HeyGen) |
| A | 0,50 → 7,40 | 3,20 s | onglet Templates, galerie de 9 designs |
| B | 7,40 → 7,70 | 0,90 s | **zoom-punch** sur le template Brasserie Parisienne (660, 315) |
| C | 12,00 → 24,00 | 2,60 s | onglet Carte : catégories & plats, ajout « Desserts » |
| D | 24,00 → 76,00 | 7,00 s | Formules : Formule Déjeuner 18€, section « mini biroches », note |
| E | 76,00 → 120,00 | 7,50 s | onglet Personnaliser : nom, description, logo/bannière, charte graphique |
| F | 120,70 → 121,05 | 0,90 s | **zoom-punch** sur Publier le site (1680, 352) |
| G | 121,20 → 133,00 | 3,50 s (→ 5,24 s auto-étendu) | toast « Vitrine en ligne » + onglet Infos & Publication |
| claude1 | carte générée | 3,00 s | reveal — prompt en gros, fond crème |
| claude2 | carte générée | 2,30 s | confirmation « Copié dans le presse-papiers ! » |
| claude3 | carte générée | 5,30 s | mockup chatbot Claude |
| outro | carte | 7,94 s (auto-étendue) | CTA |

Coordonnées mesurées par seuillage colorimétrique. Rush très dense (133 s, 4 onglets :
Templates/Carte/Personnaliser/Infos & Publication) — accélération forte sur C/D/E
(jusqu'à ×7,4) pour tenir une durée raisonnable ; les bandeaux d'étape gardent le fil
pour le spectateur même à vitesse élevée.

## Séquence Claude — module partagé

Trois outils correspondent exactement à ce que montre le rush :
`apply_site_template(establishment_id, slug, confirm)` (choix du template),
`set_site_theme(establishment_id, tokens)` (couleurs/polices) et
`publish_site(establishment_id, confirm)` (mise en ligne). Prompt combiné couvrant
les trois actions dans l'ordre où elles apparaissent à l'écran :

> Applique le template [nom du template] à ma vitrine, personnalise les couleurs
> primaire [couleur] et secondaire [couleur], puis publie le site pour mon
> établissement FoodEatUp (ID [ID établissement]).

Même texte côté fiche Lovable (`claudePrompt`).

## Animations

Mêmes principes que toute la série : Ken Burns sur les cartes, xfade (0,28 s),
bandeaux d'étape, encadré orange pulsant sur les 2 clics. Avatar en plan fixe natif
(pas de setpts, pas de zoompan — c'est une personne qui parle), fond flou identique
au traitement des cartes.

## Statut publication

**Validée par Michael, publiée sur RapidoCMS et Lovable le 2026-08-03** (demande
explicite : "publi la vidéo sur lovable" — RapidoCMS fait au passage pour obtenir
les URLs stables S3 nécessaires à Lovable). Vidéo + vignette uploadées
(`foodeatup-vitrine-tuto-v1` / `-thumbnail`). Tutoriel `ouvrir-sa-vitrine` ajouté
dans `src/data/tutorials.ts`, module Configuration (sous-catégorie "10").
**LinkedIn non programmé cette fois** — la demande portait uniquement sur Lovable,
pas de draft créé ; à faire sur demande ultérieure si souhaité.
