# Tutoriel — Créer ses catégories FoodEatUp

Dossier Drive « Création de ces catégories » (les catégories servent au menu, aux
produits de la carte et aux recettes — précision de Michael à la livraison des rushs).
Durée livrée : **41,3 s** — H.264 High/yuv420p, AAC 48 kHz stéréo, faststart.
Audio : true peak **-7,3 dBFS** (mesuré sur le MP4 final). Decode 0 erreur, moov avant
mdat (faststart confirmé).

## Voix off (9 lignes)

| # | Texte | Durée | Ancrage |
|---|---|---:|---|
| N0 | Créez vos catégories FoodEatUp : elles structurent votre menu, vos produits et vos recettes. | 4,86 s | carte d'intro (déborde sur A) |
| N1 | Cliquez sur Ajouter une catégorie pour commencer. | 2,64 s | clic Ajouter une catégorie |
| N2 | Choisissez le type concerné, puis donnez-lui un nom clair. | 3,16 s | modal type + nom |
| N3 | Ajoutez vos tags à la volée : les nouveaux seront créés automatiquement à l'enregistrement. | 4,49 s | saisie des tags |
| N4 | Choisissez une icône et une couleur pour la repérer d'un coup d'œil. | 3,34 s | icône + couleur |
| N5 | Validez avec Ajouter : votre catégorie apparaît aussitôt dans la liste. | 4,18 s | clic Ajouter → toast + liste |
| N6 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | 4,41 s | **étage 1+2** (réutilisé de la TVA, texte générique identique) |
| N7 | Collez-le dans la conversation : votre catégorie est créée en quelques secondes. | 4,55 s | **étage 3** (mockup chatbot) |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (CTA, réutilisé) |

N2 initialement générée en 6,09 s (énumération des 4 types) — régénérée en 3,16 s
avant de fixer les segments : l'énumération est déjà portée par N0, et une N2 longue
aurait recréé la dérive en chaîne corrigée sur la TVA. N6/N8 réutilisés depuis
`foodeatup-tva-tuto/vo/` (même voix, texte identique) — zéro crédit ElevenLabs dépensé
sur ces deux lignes.

## Découpage

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 3,00 s | CRÉER SES CATÉGORIES |
| A | 0,20 → 2,60 | 2,90 s | page Catégories, filtres Plat/Ingrédient/Produit/Recette |
| B | 4,30 → 4,55 | 0,90 s | **zoom-punch** sur Ajouter une catégorie (1570, 367) |
| C | 5,00 → 11,00 | 6,30 s | modal : type Plat → Produit, nom « Matériel et consommables » |
| D | 12,00 → 34,50 | 5,20 s | 4 tags à la volée (emballages, boîte à importer, serviettes, assiettes) — accéléré 4,3× |
| E | 44,50 → 53,50 | 4,00 s | icône (Vin) + couleur (gris) — accéléré 2,25× |
| F | 54,30 → 54,60 | 0,90 s | **zoom-punch** sur Ajouter / submit (1211, 737) |
| G | 55,30 → 60,30 | 4,20 s | toast « Catégorie créée » + retour liste + scroll vers la carte |
| claude1 | carte générée | 3,00 s | reveal — prompt en gros, fond crème |
| claude2 | carte générée | 2,30 s | confirmation « Copié dans le presse-papiers ! » |
| claude3 | carte générée | 5,30 s | mockup chatbot Claude (logo + bulles) |
| outro | carte | 6,20 s | CTA |

Transitions : `slideleft` sur chaque coupe qui saute du rush (B→C, C→D, D→E, G→claude)
et entre les 3 étages Claude ; `fade` sur l'action continue.

## Séquence Claude — module partagé

`mcp__FoodEatUp__create_category(establishment_id, name, type ∈ {ingredient, produit,
recette}, icon?, color?)` existe — schéma vérifié avant rédaction du prompt (les
catégories de PLAT se gèrent dans l'éditeur de carte, précision de la doc de l'outil).
Séquence rendue par `videos/_shared/claude_prompt_sequence.py`, seuls changent :

> Crée une catégorie [nom de la catégorie] de type [produit / ingrédient / recette]
> pour mon établissement FoodEatUp (ID [ID établissement]).

et la réplique assistant : « Bien sûr ! Je crée cette catégorie pour votre établissement… »

Même texte de prompt côté fiche Lovable (`claudePrompt`).

## Animations

Mêmes principes que toute la série : Ken Burns sur les cartes, xfade (0,28 s), bandeaux
d'étape, encadré orange pulsant sur les 2 clics. Pas de clip avatar dans ce dossier.

## Statut publication

Vidéo à livrer à Michael pour validation (règle du 2026-08-02) — pas de publication
RapidoCMS/LinkedIn/Lovable avant retour explicite.
