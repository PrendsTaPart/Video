# Tutoriel — Monter ses recettes / fiches techniques FoodEatUp

Tutoriel manquant du module `configuration` (Drive : dossier "MONTER SES RECETTES
FICHES TECHNIQUES"). Durée livrée : **46,2 s** — H.264 High/yuv420p, AAC 48 kHz
stéréo, faststart. Audio : true peak **-7,2 dBFS**. Decode 0 erreur, moov avant mdat.

## Ce que montre le rush (et ce qui n'est pas repris)

Le rush (93,1 s, 1920x828) montre : "Mes recettes (0)" → clic "Créer une recette" →
upload d'une photo de plat → clic "Générer avec l'IA" (nom "Kimbap Express au Thon
(Kimchi & Thon)", difficulté "Facile" et description se remplissent automatiquement
depuis la photo) → section "Ingrédients et Quantités" → ajout séquentiel de 4
ingrédients (Sushi riz 300g, Nori - feuilles d'algues grillées 2 pcs, Thon au
naturel 120g, Mayonnaise 30g) avec le coût total de la recette recalculé en direct
à chaque ajout (3,60€ → 31,60€ → 37,60€ → 38,35€).

Le rush s'arrête avant la saisie du prix de vente et le clic "Enregistrer la
recette" — jamais filmés. Le montage se termine donc sur le tableau d'ingrédients
avec le coût total en évidence, pas sur un écran de succès (pas d'invention à
l'écran de ce qui n'a pas été montré).

## Voix off (11 lignes, voix Adam FR `TGAegA0zNRi8I6nUdq3i`)

| # | Texte | Durée | Segment |
|---|---|---:|---|
| N0 | Créer une recette FoodEatUp, reliée à vos ingrédients et vos produits. | 3,76 s | intro |
| N1 | Cliquez sur Créer une recette. | 1,70 s | clic "Créer une recette" |
| N2 | Ajoutez une photo de votre plat. | 1,70 s | C — photo de la recette |
| N3 | Cliquez sur Générer avec l'IA. | 1,85 s | clic "Générer avec l'IA" |
| N4 | Le nom, la difficulté et la description se remplissent tout seuls depuis la photo. | 4,55 s | E — champs générés par l'IA |
| N5 | Ajoutez ensuite vos ingrédients, un par un. | 2,35 s | F — section ingrédients |
| N6 | Le coût de la recette se calcule en temps réel, ingrédient après ingrédient. | 4,41 s | G — ajout des 4 ingrédients |
| N7 | Cette recette alimente directement vos produits et votre carte. | 3,29 s | H — bénéfice (coût total) |
| N8 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | 4,41 s | étages 1+2 (réutilisé tel quel depuis `foodeatup-produits-tuto`) |
| N9 | Collez-le dans la conversation : votre recette, avec ses ingrédients, est créée en quelques secondes. | 5,15 s | étage 3 |
| N10 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (CTA, réutilisé tel quel depuis `foodeatup-produits-tuto`) |

N8/N10 réutilisés tels quels — zéro crédit ElevenLabs dépensé sur ces deux lignes.

**Retour d'expérience (bug évité) :** un premier montage du tuto PIN précédent avait
sous-dimensionné les segments visuels par rapport à la durée réelle de la VO
(dérive jusqu'à 11s). Ici, chaque segment a été dimensionné généreusement en marge
de la durée mesurée de sa ligne VO avant le premier rendu — dérive maximale
observée : 2,5s, aucune ligne ne déborde sur le mauvais segment.

## Découpage

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 3,20 s | MONTER SES RECETTES — FICHES TECHNIQUES |
| A | 0,20 → 2,00 | 2,00 s | "Mes recettes (0)", état vide |
| B | 2,00 → 2,30 | 0,80 s | **zoom-punch** sur "Créer une recette" (1682, 344) |
| C | 4,00 → 6,50 | 2,50 s | upload de la photo du plat |
| D | 7,00 → 7,30 | 0,80 s | **zoom-punch** sur "Générer avec l'IA" (535, 146) |
| E | 8,00 → 16,00 | 5,00 s | nom/difficulté/description auto-remplis |
| F | 20,00 → 28,00 | 3,00 s | section "Ingrédients et Quantités" |
| G | 28,00 → 68,00 | 7,00 s | ajout des 4 ingrédients, coût recalculé en direct |
| H | 88,00 → 93,00 | 4,00 s | tableau final, coût total 38,35€ |
| claude1 | carte générée | 6,00 s | reveal — prompt en gros, fond crème |
| claude2 | carte générée | 3,00 s | confirmation "Copié dans le presse-papiers !" |
| claude3 | carte générée | 6,00 s | mockup chatbot Claude |
| outro | carte | 6,20 s | CTA |

Coordonnées de clic mesurées directement sur les frames extraites du rush,
résolution source native 1920x828.

## Séquence Claude — module partagé

`mcp__FoodEatUp__create_recipe(establishment_id, name, ingredients[], steps[],
category_names?, dificulty?, how_many_people?, recommended_price?, tax_rate?)`
existe — schéma vérifié. Les ingrédients inconnus sont **créés automatiquement**
par l'outil (nom + quantité + unité + prix unitaire optionnel), donc un seul appel
crée à la fois la recette et ses ingrédients manquants :

> Crée la recette [nom de la recette], difficulté [facile / moyen / difficile],
> pour [nombre] personnes, avec les ingrédients [ingrédient 1] [quantité] [unité],
> [ingrédient 2] [quantité] [unité], et les étapes [étape 1], [étape 2], pour mon
> établissement FoodEatUp (ID [ID établissement]).

**3 exemples demandés côté fiche Lovable** (`claudePrompts[]`) : création directe
(vidéo), création depuis une photo d'un plat (chefTip de Michael : "prenez en photo
une recette et demandez à Claude de l'ajouter"), et création du produit vendable
associé à la recette (`create_product`) — pour boucler le lien recette → carte.

## Animations

Mêmes principes que toute la série : Ken Burns sur les cartes, xfade (0,28 s),
bandeaux d'étape, encadré orange pulsant sur les 2 clics ("Créer une recette",
"Générer avec l'IA"). Pas de zoom-punch sur l'ajout des ingrédients (saisie
continue, pas un bouton isolé) — même logique que le remplissage de formulaire
dans les tutos précédents. Pas de clip avatar dans ce dossier.

## Statut publication

Montage terminé et checklist de compatibilité passée (H.264 High/yuv420p, AAC 48 kHz
stéréo, faststart, peak -7,2 dBFS, 0 erreur de décodage). **En attente de validation
avant publication** (règle du 2026-08-02, `videos/LOVABLE-FOODEATUP-DOCS.md`) : pas
d'upload RapidoCMS/LinkedIn (RapidoCMS non authentifié dans cette session de toute
façon), pas d'envoi du prompt Lovable tant que la vidéo n'a pas été revue.
