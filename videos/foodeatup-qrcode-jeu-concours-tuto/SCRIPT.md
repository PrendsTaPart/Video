# Tutoriel — Retrouver son QR Code jeu concours

Catalogue #15, module `marketing-fidelite` (« Marketing, Fidélité & Iris »),
voir `videos/CATALOGUE-157-TUTORIELS.md` ligne 114. Fourni par Michael :
`QR_CODE_JEU_CONCOURS.jpg` (carte intro), `page_fin_vid..jpg` (carte outro,
réutilisée telle quelle depuis le reste de la série),
`Retrouver_votre_lien_et_qrcode_du_jeux_concours.mp4` (rush, 25,08 s,
1920×828, 25 fps).

Durée livrée : **45,92 s** — H.264 High/yuv420p, AAC 48 kHz stéréo,
faststart. Audio : true peak **-7,18 dBFS** (cohérent avec le reste de la
série).

Écran couvert : **Fidélité & jeux → onglet Roue cadeaux**. Bouton « QR
imprimable » survolé, clic sur « Copier le lien » (toast « Lien copié ✓ »),
nouvel onglet avec l'URL collée (`.../shop/gosushi-demo/roue/whl_...`), page
publique de la roue (« GoSushi Démo », jeu hors ligne donc message « Ce jeu
est terminé — revenez bientôt ! »).

## Voix off (8 lignes, voix Adam FR `TGAegA0zNRi8I6nUdq3i`)

L'ordre des lignes 2-4 a été réagencé par rapport au script initialement
présenté à Michael pour coller à la chronologie réelle du rush (le survol de
« QR imprimable » précède le clic sur « Copier le lien » dans
l'enregistrement) — même contenu, juste réordonné.

| # | Texte | Durée | Segment |
|---|---|---:|---|
| N1 | Retrouver le lien et le QR code de votre jeu concours FoodEatUp ? Voici comment faire. | 4,96 s | idle |
| N2 | Cliquez sur QR imprimable pour télécharger un QR code prêt à afficher en salle ou sur votre vitrine. | 5,93 s | QR (zoom-punch) |
| N3 | Ou cliquez sur Copier le lien pour récupérer directement l'URL de votre roue. | 4,55 s | COPY (zoom-punch + toast) |
| N4 | Le lien copié ouvre aussitôt la roue cadeaux, prête à être jouée par vos clients. | 4,44 s | TAB (nouvel onglet, URL collée) |
| N5 | Vos clients scannent ou cliquent, tentent leur chance, et rejoignent votre programme de fidélité en un instant. | 5,69 s | WHEEL (page publique) |
| N6 | Vous pouvez aussi retrouver ce lien depuis Claude : copiez ce prompt, remplacez les crochets. | 4,83 s | claude étages 1+2 |
| N7 | Collez-le dans la conversation : le lien et les statistiques de votre roue s'affichent aussitôt. | 5,25 s | claude étage 3 |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin |

N8 réutilisée telle quelle depuis `foodeatup-qrcode-tuto/vo/N8.mp3` (CTA
générique de toute la série, texte identique).

## Découpage

| Seg | Source | Cible | Contenu |
|---|---|---:|---|
| intro | carte | 3,00 s | QR CODE JEU CONCOURS |
| idle | 0,00 → 12,00 | 5,00 s | Page Fidélité & jeux, onglet Roue cadeaux (accéléré, contenu statique) |
| QR | 12,00 → 13,50 | 6,00 s | **zoom-punch** sur « QR imprimable » (1500, 695) |
| COPY | 13,50 → 16,00 | 5,00 s | **zoom-punch** sur « Copier le lien » (1300, 695) + toast « Lien copié ✓ » |
| TAB | 16,00 → 19,50 | 4,80 s | Nouvel onglet, URL collée dans la barre d'adresse, chargement |
| WHEEL | 19,50 → 25,08 | 6,00 s | Page publique « GoSushi Démo », roue cadeaux affichée |
| claude1 | carte générée | 3,20 s | reveal — prompt en gros, fond crème |
| claude2 | carte générée | 2,20 s | confirmation « Copié dans le presse-papiers ! » |
| claude3 | carte générée | 5,50 s | mockup chatbot Claude |
| outro | carte | 7,61 s (auto-étendue pour tenir N8) | CTA |

Coordonnées mesurées par extraction de frames pleine résolution (1920×828)
autour de chaque interaction (`ffmpeg -vf fps=2` sur la fenêtre 8-19 s pour
localiser précisément le clic et l'ouverture du nouvel onglet).

**Segments dimensionnés sur la durée de leur ligne VO, pas sur la durée
brute du rush** (leçon relearned ici : un premier rendu avec des segments
calés sur le minutage réel de l'enregistrement — mouvement de souris compris
— a produit un dérapage de 4 à 7 s entre chaque ligne et son ancrage visuel,
voir `drift vs anchors` dans le log de build). Le rush étant très statique
(pas de saisie de champs, juste survol + clic), le ralenti important
appliqué aux segments QR/COPY (jusqu'à ×5) ne crée aucun artefact visible.

## Séquence Claude — module partagé

Action du rush avec un équivalent MCP direct : `list_wheel_games
(establishment_id)` + `get_wheel_stats(establishment_id, wheel_id)` —
retrouver le lien de partage et les statistiques (lancers, leads) d'une
roue cadeaux. Correspondance particulièrement directe puisque le tutoriel
porte lui-même sur la *récupération* de cette information.

> Montre-moi le lien de partage et les statistiques (lancers, leads) de ma
> roue cadeaux jeu concours pour mon établissement FoodEatUp (ID [ID
> établissement]).

Même texte côté fiche Lovable (`claudePrompt`).

## Astuce du chef (`chefTip`)

> Affichez le QR code sur vos tables et votre vitrine, et réservez le lien
> pour vos campagnes SMS/e-mail : vous doublez vos points d'entrée dans le
> jeu sans dupliquer d'effort.

## Animations

Mêmes principes que toute la série : Ken Burns sur les cartes, xfade
(0,28 s), bandeaux d'étape (`banner()`), encadré orange pulsant sur les
zoom-punch. `fade` pour les cuts continus sur la même page (idle→QR→COPY,
TAB→WHEEL), `slideleft` pour les changements de contexte (COPY→TAB nouvel
onglet, WHEEL→claude1, entre les 3 étages Claude).

## Statut publication

Vidéo à livrer à Michael pour validation avant publication RapidoCMS /
LinkedIn / Lovable, conformément à la règle du 2026-08-02
(`videos/LOVABLE-FOODEATUP-DOCS.md`).
