# Tutoriel — Ajouter une température de production (Plats) FoodEatUp

Module **HACCP** (1ère vidéo publiée du module, voir `videos/LOVABLE-FOODEATUP-DOCS.md`).

**STATUT : script validé par Michael (2026-08-03) → v1 montée, en attente de validation
de la vidéo avant publication** (règle `FOODEATUP-TUTORIELS-WORKFLOW.md`, étape 6 : STOP
obligatoire avant tout upload RapidoCMS/LinkedIn/Lovable).

Durée livrée (v1) : **37,84 s** — H.264 High/yuv420p, AAC 48 kHz stéréo, faststart (moov
avant mdat confirmé). Audio : true peak **-6,97 dBFS** (mesuré sur le MP4 final).
Livrable : `out/foodeatup-temperatures-tuto-v1.mp4` + `out/thumbnail-youtube.jpg`
(1280×720, recadrage neutre de `assets/intro.jpg`, non redessinée).

## Pas de séquence Claude sur cette vidéo

`add_temperature` (MCP) ne couvre que l'onglet Équipements (température frigo/four…),
pas l'onglet Plats montré ici. `create_recipe`/`create_dish` n'ont pas les champs vus à
l'écran (allergènes, durée de vie, pièce jointe, seuil recommandé). Aucun outil MCP ne
correspond exactement à l'action filmée → pas de prompt inventé, pas de séquence chatbot
en fin de vidéo (voir détail dans STORYBOARD.md).

## Voix off (brouillon, 8 lignes, voix Adam FR)

| # | Texte | Ancrage |
|---|---|---|
| N0 | Contrôler la température de vos plats sur FoodEatUp ? Quelques secondes suffisent. | carte d'intro |
| N1 | Dans Production, ouvrez Températures puis cliquez sur Ajouter un relevé. | clic "+ Ajouter un relevé" |
| N2 | Choisissez un plat déjà enregistré dans la liste... | sélection dropdown ("suchi - haccp_recipe") |
| N3 | ...ou créez-en un nouveau à la volée avec Ajouter une recette : nom, allergènes, durée de conservation. | modale "Nouvelle recette" |
| N4 | Saisissez la température mesurée : FoodEatUp la compare aussitôt au seuil recommandé. | champ "Saisie température" + "Recommandé : +63°C minimum" |
| N5 | Ajoutez une photo si besoin, puis validez avec Enregistrer. | pièce jointe + clic "Enregistrer" |
| N6 | Votre relevé apparaît dans la liste, conforme ou non conforme en un coup d'œil. | résultat : carte "Pizza" 63.0°C, stats mises à jour |
| N7 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | carte de fin (CTA) |

N7 est la ligne CTA standard, réutilisable telle quelle (déjà en stock dans plusieurs
`vo/N*.mp3` d'autres tutoriels si on veut éviter un aller-retour ElevenLabs).

## Découpage (v1)

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 4,95 s | SONDER SES PLATS À CŒUR |
| A | 0,30 → 3,60 | 4,05 s | liste vide (« Aucun plats ») |
| B | 4,30 → 4,60 | 0,90 s | **zoom-punch** sur + Ajouter un relevé (1668, 304) |
| C | 5,00 → 10,80 | 3,15 s | modale, sélection « suchi - haccp_recipe » |
| D | 24,50 → 24,80 | 0,90 s | **zoom-punch** sur + Ajouter une recette (1382, 334) |
| E | 26,00 → 45,00 | 6,30 s | Nouvelle recette : nom, allergènes, durée de vie (accéléré ~3×) |
| F | 57,90 → 58,20 | 0,90 s | **zoom-punch** sur Enregistrer, sous-modale (1018, 648) |
| G | 58,90 → 59,60 | 4,60 s | retour modale principale : température + seuil recommandé |
| H | 60,00 → 60,30 | 0,90 s | **zoom-punch** sur Enregistrer, modale principale (1024, 648) |
| I | 60,30 → 60,60 | 2,85 s | « Enregistrement… » |
| J | 61,50 → 65,50 | 4,60 s | résultat : carte « Pizza » 63.0°C, stats à jour |
| outro | carte | 6,20 s | CTA |

Offsets voix off réels (`build.py`, sans extension d'outro nécessaire) : N0=0.30 N1=4.88
N2=9.36 N3=12.24 N4=18.96 N5=24.08 N6=27.52 N7=31.99, fin de voix 37.01s pour un total
vidéo de 37.84s — chaque offset tombe après (ou quasi à) l'ancrage visuel de son segment,
pas de chevauchement.

## Points encore ouverts (non bloquants pour la livraison de la v1)

1. **Nom exact à donner au tutoriel / slug Lovable** — proposition : `ajouter-temperature-plat`
   (module `haccp`, sous-catégorie à préciser — quel est le nom du sous-dossier Drive
   correspondant, pour rester cohérent avec `LOVABLE-FOODEATUP-DOCS.md` ?).
2. Le rush montre une recette « suchi » existante et une nouvelle recette « pizza » créée
   en démo — noms conservés tels quels dans le montage.

Vidéo livrée pour validation (`SendUserFile`) — pas de publication RapidoCMS/LinkedIn/
Lovable tant que Michael n'a pas donné son accord explicite sur cette v1.
