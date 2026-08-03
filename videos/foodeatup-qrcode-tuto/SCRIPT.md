# Tutoriel — Diffuser son QR code FoodEatUp

Dossier Drive « 14 - votre QR code ». Durée livrée : **43,36 s** — H.264
High/yuv420p, AAC 48 kHz stéréo, faststart. Audio : true peak **-7,17 dBFS**
(marge confortable). Sans avatar HeyGen — retiré à la demande de Michael
(script déjà validé sans lui).

Écran couvert : « Supports marketing » (4 onglets) — QR Code (variantes
Tube/Prime/Sticker + téléchargement), Flyers (templates Classique/Moderne/
Photo + téléchargement), Cartes de visite (templates Minimal/Bold/Élégant +
téléchargement), Réseaux sociaux (Facebook/Instagram/TikTok/X/Site web/
Google Avis + bouton Enregistrer les liens).

## Voix off (8 lignes, sans N0 avatar)

| # | Texte | Durée | Segment |
|---|---|---:|---|
| N1 | Téléchargez votre QR code au format tube, prime ou sticker pour vos tables et votre vitrine. | 5,20 s | A |
| N2 | Dans l'onglet Flyers, choisissez un template et téléchargez-le prêt à imprimer. | 4,41 s | B |
| N3 | Faites de même pour vos cartes de visite, personnalisées à vos couleurs. | 3,47 s | C |
| N4 | Renseignez vos réseaux sociaux et votre lien Google Avis, puis enregistrez. | 4,68 s | D1 + clic D2 |
| N5 | Le QR code renvoie directement vers votre vitrine en ligne, avec vos horaires et vos réservations toujours à jour. | 6,40 s | E |
| N6 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | 4,41 s | étages 1+2 (réutilisée depuis vitrine/tva) |
| N7 | Collez-le dans la conversation : vos réseaux sociaux sont enregistrés en quelques secondes. | 4,49 s | étage 3 |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (réutilisée) |

N6/N8 réutilisés depuis `foodeatup-vitrine-tuto/vo/`.

## Découpage

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 2,50 s | DIFFUSER SON QR CODE |
| A | 0,00 → 7,30 | 5,70 s | QR Code : variantes Tube/Prime/Sticker, téléchargement |
| B | 7,30 → 11,80 | 4,95 s | Flyers : templates, téléchargement |
| C | 11,80 → 17,30 | 4,00 s | Cartes de visite : templates, téléchargement |
| D1 | 17,30 → 48,55 | 4,40 s | Réseaux sociaux : remplissage des champs (accéléré ×7,1) |
| D2 | 48,55 → 49,35 | 0,80 s | **zoom-punch** sur « Enregistrer les liens » (516, 680) |
| E | 49,35 → 55,40 | 6,90 s | Confirmation (page rechargée, footer avec icônes) — légèrement ralenti (×0,88) pour tenir la ligne bénéfice |
| claude1 | carte générée | 3,00 s | reveal — prompt en gros, fond crème |
| claude2 | carte générée | 2,30 s | confirmation « Copié dans le presse-papiers ! » |
| claude3 | carte générée | 5,30 s | mockup chatbot Claude |
| outro | carte | 6,20 s | CTA |

Coordonnées mesurées par extraction de frames pleine résolution (1920×828)
autour du clic. Rush dense (55 s, 4 onglets) mais sans plan-avatar : accéléré
fortement sur D1 (remplissage de champs, ×7,1) — inutile de montrer chaque
frappe clavier en temps réel.

## Séquence Claude — module partagé

Seule action du rush avec un équivalent MCP : `update_section(establishment_id,
section_id, props)` (fusion partielle des props d'une section — ici les liens
réseaux sociaux). QR code / flyers / cartes de visite sont des générations
client-side sans action serveur, donc sans outil MCP correspondant — pas de
prompt inventé pour ces 3 blocs (cohérent avec `creer-son-compte`,
`choisir-son-abonnement`, etc.).

> Mets à jour la section réseaux sociaux de mon site avec Facebook [URL
> Facebook], Instagram [URL Instagram], TikTok [URL TikTok] et Google Avis
> [URL Google Avis] pour mon établissement FoodEatUp (ID [ID établissement],
> section [ID section]).

Même texte côté fiche Lovable (`claudePrompt`).

## Bug rencontré et corrigé (2026-08-03) — banner() invisible

Le bandeau d'étape (`banner()`, filtre `drawbox` + `drawtext` partagé par
toute la série) ne s'affichait pas du tout sur cette vidéo : le texte
apparaissait mais jamais les rectangles orange/bleu derrière. Isolé après
tests systématiques : l'évaluateur d'expressions `drawbox` de cet ffmpeg
(6.1.1-3ubuntu5) échoue silencieusement (pas d'erreur, juste une position
hors-écran) quand l'expression `x` combine **un décalage constant en tête
(`-640+`) avec DEUX termes `min(1,max(0,...))` soustraits** (un pour le
slide-in, un pour le slide-out) — chaque moitié fonctionne isolément, la
combinaison des deux ne fonctionne pas. **Confirmé que ce même bug affecte
la vidéo déjà livrée `foodeatup-vitrine-tuto`** (bandeaux d'étape invisibles
là aussi, jamais remarqué avant faute de vérification pixel par pixel).

Corrigé ici en simplifiant `banner()` : un seul terme `min/max` pour le
slide-in, plus de slide-out animé (le fondu-enchaîné vers le segment suivant
masque déjà la sortie). Fonctionne de manière fiable. **À reporter dans
`FOODEATUP-TUTORIELS-WORKFLOW.md`** (piège ajouté) et à décider avec Michael
si `foodeatup-vitrine-tuto` doit être re-rendue avec le correctif.

## Animations

Mêmes principes que toute la série : Ken Burns sur les cartes, xfade
(0,28 s), bandeaux d'étape (corrigés, voir ci-dessus), encadré orange
pulsant sur le clic Enregistrer. Pas de plan avatar sur cette vidéo.

## Statut publication

Vidéo à livrer à Michael pour validation avant publication RapidoCMS/
LinkedIn/Lovable. RapidoCMS non autorisé dans cette session (connecteur non
connecté) — publication CMS/LinkedIn en attente dans tous les cas.
