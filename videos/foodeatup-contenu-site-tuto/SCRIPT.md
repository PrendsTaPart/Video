# Tutoriel — Ajouter du contenu sur son site FoodEatUp

Durée livrée : **50,00 s** — H.264 High/yuv420p 1920x828, AAC 48kHz stéréo,
faststart. Audio : true peak **-7,2 dBFS** (large marge sous le plafond cible).
Decode 0 erreur. Vignette YouTube = `assets/intro.jpg` redimensionnée en 1280x720
sans recadrage créatif (`out/thumbnail-youtube.jpg`).

Module Lovable : `site-web-vitrine` (Site Web & Vitrine, 8 vidéos attendues), tutoriel
n°07 « Ajouter du **Contenu** sur son site » (`CATALOGUE-157-TUTORIELS.md` ligne 72).
Slug déjà réservé côté site (`ajouter-du-contenu-sur-son-site`, stub "en cours de
tournage" dans `src/data/tutorials.ts`) — cette vidéo remplit ce stub.

Rush fourni : `assets/screen.mp4` (1920x828, 25fps, 132.84s) — parcourt les 5 sous-onglets
de la page **Contenu du site** : Recrutement, Producteurs, Boissons, Privatisations
(vue), Agenda. Cartes intro/outro fournies telles quelles par Michael
(`assets/intro.jpg` = "AJOUTER DU CONTENU PRO", `assets/outro.jpg` = carte CTA
générique déjà utilisée sur d'autres tutos).

## Voix off (9 lignes, voix Adam FR `TGAegA0zNRi8I6nUdq3i`)

| # | Texte | Segment |
|---|---|---|
| N0 | Ajouter du contenu sur votre site FoodEatUp ? On vous montre comment, en quelques clics ! | intro/carte |
| N1 | Dans Recrutement, publiez une offre : poste, salaire, avantages, puis cliquez sur Enregistrer. | A (+ punch B + confirm C) |
| N2 | Dans Producteurs, mettez en avant vos fournisseurs locaux et leurs spécialités. | D |
| N3 | Dans Boissons, composez votre carte des vins par catégorie, prix au verre et à la bouteille. | F |
| N4 | L'onglet Privatisations regroupe vos demandes de privatisation et vos cartes cadeaux vendues. | G |
| N5 | Et dans Agenda, créez vos événements : la soirée est publiée en quelques secondes sur votre site. | H (+ punch I + confirm J) |
| N6 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | claude1+2 (réutilisé de `foodeatup-vitrine-tuto`) |
| N7 | Collez-le dans la conversation : votre offre d'emploi est publiée en quelques secondes. | claude3 |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | carte de fin (CTA, réutilisé de `foodeatup-vitrine-tuto`) |

N6/N8 copiés depuis `foodeatup-vitrine-tuto/vo/` (texte identique, voix identique).

## Découpage (mesuré par extraction de frames, `work/sheets/` + `work/detail/`)

| Seg | Source | Cible | Contenu |
|---|---|---:|---|
| intro | carte | 2,60 s | AJOUTER DU CONTENU PRO |
| A | 0,20 → 29,30 | 4,60 s | Recrutement : formulaire Nouvelle offre (intitulé, contrat, horaires, salaires, statut, description, avantages) |
| B | 30,00 → 30,35 | 0,80 s | **zoom-punch** clic Enregistrer (496, 644) |
| C | 30,35 → 35,00 | 2,00 s | toast "Offre enregistrée", bascule onglet Producteurs |
| D | 35,00 → 52,50 | 4,60 s | Producteurs : formulaire Nos producteurs (nom, région, bio) |
| E | 52,50 → 57,00 | 1,20 s | confirmation + bascule onglet Boissons |
| F | 57,00 → 89,50 | 4,60 s | Boissons : Carte des vins & boissons, catégorie Rouge, cépage/AOP/millésime/prix |
| G | 89,50 → 95,00 | 2,00 s | Privatisations : demandes de privatisation + cartes cadeaux vendues (vue), bascule Agenda |
| H | 95,00 → 127,30 | 4,60 s | Agenda : formulaire Nouvel évènement (titre, date/heure, lieu, description, publié) |
| I | 127,30 → 127,70 | 0,80 s | **zoom-punch** clic Enregistrer (496, 712) |
| J | 127,70 → 132,84 | 2,20 s | toast "Événement enregistré", liste Événements du site |
| claude1 | carte générée | 3,00 s | reveal — prompt en gros, fond crème |
| claude2 | carte générée | 2,30 s | confirmation "Copié dans le presse-papiers !" |
| claude3 | carte générée | 5,30 s | mockup chatbot Claude |
| outro | carte | 6,20 s (auto-étendue) | CTA |

Coordonnées mesurées par extraction de frames autour des clics (`work/detail/jo_*.jpg`,
`work/detail/ag2_*.jpg`), pas de seuillage colorimétrique automatisé cette fois (bouton
bleu net sur fond blanc, lecture directe suffisante).

## Séquence Claude — module partagé

Outil correspondant le plus directement à ce que montre le rush :
`create_job_offer(establishment_id, title, contract, description, salary_min, salary_max,
status)` — action vedette de l'onglet Recrutement, premier sous-onglet visité et thème
principal du fichier fourni par Michael (nom de fichier : "...recrutement producteur
etc"). Prompt :

> Crée une offre d'emploi pour mon établissement FoodEatUp (ID [ID établissement]) :
> poste [intitulé du poste], contrat [type de contrat], salaire de [salaire min]€ à
> [salaire max]€, avec la description : [description du poste].

Un second outil correspond à l'onglet Boissons — `upsert_beverage_item(establishment_id,
category, name, appellation, vintage, glass_price, bottle_price)` — ajouté côté site
Lovable comme second exemple (`claudePrompts`, pas d'animation vidéo dédiée, une seule
séquence chatbot par vidéo comme sur le reste de la série) :

> Ajoute une boisson à la carte de mon établissement FoodEatUp (ID [ID établissement]) :
> [nom de la boisson], catégorie [rouge/blanc/rosé/bulles/bière/soft/café/saké],
> appellation [appellation AOP/IGP], millésime [année], prix au verre [prix]€, prix à la
> bouteille [prix]€.

Producteurs, Privatisations et Agenda n'ont pas d'outil MCP FoodEatUp équivalent exposé
dans cette session (pas de `create_producer` / `create_site_event` / privatisation) —
pas de prompt inventé pour ces trois sous-onglets, conformément à la règle du pipeline.
