# Tutoriel — Traçabilité complète FoodEatUp (synchroniser avec vos produits)

Module « HACCP », sous-catégorie proposée : **Traçabilité complète**.
Slug proposé : `tracabilite-complete`.
Rush source : `assets/screen.mp4` (1920x828, 55,68 s), carte d'intro fournie
(`assets/intro.jpg` — « TRACER EN MODE COMPLET TRAÇABILITÉ »), carte de fin réutilisée
telle quelle (`assets/outro.jpg`, identique au reste de la série).

## Déroulé reconstitué (extraction de frames, `ffmpeg -ss t -frames:v 1`)

| t | Écran | Action |
|---:|---|---|
| 0,0 – 6,5 s | Traçabilité (accueil du module) | Deux cartes : « Traçabilité simplifiée » / « Traçabilité complète ». Le curseur se déplace vers la carte orange puis clique la flèche (≈836, 538 en 1920x828 source, coin haut-droit de la carte). |
| 6,5 – 8,0 s | Traçabilité complète (vide) | État vide « Aucun élément de traçabilité — Les traçabilités se génèrent automatiquement depuis vos productions ». Bouton **Ajouter des produits à la traçabilité** (haut droit) et **Synchroniser avec les productions** (centre). |
| 8,0 – 12,5 s | Sélectionner des produits | Clic sur **Ajouter des produits à la traçabilité** → liste filtrable (Tous / Aliments bio / Animation culinaire / Boissons / Boissons énergétiques / Autres) + recherche. Clic sur le **+** de la ligne « Abricot » (#505) → coche bleue, bouton **Valider** s'active (vert). |
| 12,5 – 16,0 s | Traçabilité complète | Retour à la liste : carte « Abricot », statut rouge **non complété** (+ icônes supprimer / dupliquer). |
| 16,0 – 22,0 s | Modal fiche produit | Clic sur **non complété** → formulaire « Abricot » : bloc **Photo de la DLC*** (Ouvrir la caméra pour DLC / Ou importer depuis les fichiers) ; une photo de l'étiquette est ajoutée. |
| 22,0 – 38,0 s | Modal (suite) | Champs **Quantité*** (`2`), **DLC*** (`02/07/2026`), **N° de lot** (`LOT-ABRICOT-20260728`), **Remarques** (`frigo - 2`). |
| 38,0 – 40,0 s | Modal → validation | Clic **Valider la traçabilité** (bouton bleu) → état « Validation... » puis fermeture. |
| 40,0 – 44,0 s | Traçabilité complète | La carte « Abricot » passe au statut vert **Complété**. Boutons **Enregistrer et imprimer** / **Enregistrer** apparaissent en bas. |
| 44,0 – 48,0 s | Modal « Date de la traçabilité » | Clic **Enregistrer** → modal Date/Heure (`28/07/2026`, `12:00 AM`) → clic **Valider**. |
| 48,0 – 50,0 s | Accueil | Retour bref à l'accueil (« bonjour, soulayma ! ») montrant les modules (Températures, Traçabilité, Plan de nettoyage, Production...). |
| 50,0 – 55,7 s | Traçabilité complète | Retour final sur la liste, carte « Abricot » toujours **Complété**. |

**Note** : le rush ne montre pas de clic sur le bouton « Synchroniser avec les
productions » (génération auto depuis les productions) — seul le flux manuel
« Ajouter des produits → fiche détaillée → valider » est démontré. Le script ci-dessous
reste donc fidèle à ce qui est réellement à l'écran, sans inventer une action non
montrée (règle du pipeline).

## Voix off proposée (Adam FR, `TGAegA0zNRi8I6nUdq3i`) — 9 lignes

| # | Texte | Ancrage |
|---|---|---|
| N0 | Traçabilité complète sur FoodEatUp : un suivi précis, produit par produit. | carte d'intro |
| N1 | Depuis l'onglet Traçabilité, ouvrez la Traçabilité complète pour un suivi détaillé. | clic carte orange (0-6,5s) |
| N2 | Ajoutez vos produits en un clic, ils rejoignent aussitôt votre liste de traçabilité. | sélection Abricot + Valider (8-12,5s) |
| N3 | Prenez en photo la DLC directement depuis l'application. | bloc Photo DLC (16-22s) |
| N4 | Complétez la quantité, la date et le numéro de lot pour un enregistrement structuré. | remplissage formulaire (22-38s) |
| N5 | Validez : votre fiche passe aussitôt au statut Complété. | Valider la traçabilité → badge vert (38-44s) |
| N6 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | séquence Claude — étage 1+2 (reveal + copié) |
| N7 | Collez-le dans la conversation : votre traçabilité est enregistrée en quelques secondes. | séquence Claude — étage 3 (mockup chatbot) |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | carte de fin (CTA) |

## Séquence de fin « cas d'usage + prompt Claude »

Outil MCP correspondant : `mcp__FoodEatUp__create_haccp_tracabilite`
(`establishment_id`, `type="complete"`, `reference_type="product"`, `quantite`, `dlc`,
`lot`, `remarques`). Template partagé `videos/_shared/claude_prompt_sequence.py`
(reveal → copié → mockup chatbot), même règles que `foodeatup-tva-tuto`.

Prompt (identique vidéo + fiche Lovable `claudePrompt`) :

> Crée une fiche de traçabilité complète pour [nom du produit] : lot [numéro de lot],
> DLC [jj/mm/aaaa], quantité [quantité], dans mon établissement FoodEatUp (ID [ID
> établissement]).

## Découpage réel (v1, corrigé après vérification image-par-image)

Un premier passage de minutage (clics/coordonnées) avait été bâti sur un scan grossier
toutes les 2 s et s'est révélé faux sur plusieurs clics une fois vérifié précisément
(échantillonnage toutes les 0,2-0,3 s + seuillage couleur des vrais pixels de bouton,
voir historique de session) : le clic sur la carte « Traçabilité complète » a vraiment
lieu à ~4,75 s (pas 6,3 s), le « + » sur Abricot à ~8,15 s (pas 9,9 s), le badge « non
complété » à ~12,8 s (pas 15,9 s), et **« Valider la traçabilité » à ~34,3 s (pas
38,2 s)** — écart de près de 4 s. Toutes les coordonnées et bornes source ont été
recalées sur les vraies transitions ; la fenêtre 46-52 s (aller-retour non pertinent
vers le tableau de bord Accueil) a été coupée au montage.

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 4,60 s | TRACER EN MODE COMPLET TRAÇABILITÉ |
| A | 0,20 → 4,60 | 2,30 s | deux cartes traçabilité |
| B | 4,65 → 4,90 | 0,90 s | **zoom-punch** carte « Traçabilité complète » (1702,384) |
| C | 4,95 → 8,00 | 4,40 s | état vide → liste produits |
| D | 8,05 → 8,30 | 0,90 s | **zoom-punch** « + » Abricot (1703,650) |
| E | 8,35 → 11,10 | 2,40 s | produit coché, Valider actif |
| F | 11,15 → 11,35 | 0,85 s | **zoom-punch** Valider sélection (1735,193) |
| G | 11,40 → 12,65 | 2,60 s | retour liste, Abricot « non complété » |
| H | 12,70 → 12,90 | 0,85 s | **zoom-punch** badge non complété (1552,496) |
| I | 12,95 → 22,00 | 5,40 s | modal, photo de la DLC |
| J | 22,10 → 34,15 | 6,10 s | quantité, DLC, n° de lot, remarques |
| K | 34,20 → 34,45 | 0,90 s | **zoom-punch** Valider la traçabilité (1032,694) |
| L | 34,50 → 39,50 | 1,80 s | validation en cours |
| M | 39,55 → 40,95 | 1,80 s | statut Complété |
| N | 41,00 → 41,20 | 0,85 s | **zoom-punch** Enregistrer (1673,606) |
| O | 41,25 → 43,45 | 1,40 s | modal date/heure |
| P | 43,50 → 43,75 | 0,85 s | **zoom-punch** Valider date (1273,577) |
| Q | 52,00 → 55,68 | 1,80 s | retour liste, Complété (final) |
| claude1/2/3 | cartes générées | 3,00 / 2,30 / 5,30 s | reveal → copié → mockup chatbot |
| outro | carte | 6,20 s | CTA |

Offsets voix off finaux (zéro dérive, `voice_end` 51,3 s) :
N0 0,30 · N1 6,46 · N2 11,34 · N3 17,80 · N4 22,92 · N5 28,66 · N6 36,40 · N7 41,16 ·
N8 46,35.

## Livrable

`out/foodeatup-tracabilite-tuto-v1.mp4` — 52,20 s, 1920×828, H.264 High/yuv420p,
AAC-LC 48 kHz stéréo, faststart, true peak mesuré **-7,3 dBFS** (conforme au reste de
la série).

## Statut

**v1 montée et vérifiée (contact sheet + relecture image par image) — en attente de
validation avant publication** (règle « STOP obligatoire » de
`FOODEATUP-TUTORIELS-WORKFLOW.md`, §6). Aucune publication RapidoCMS/LinkedIn/Lovable
ni mise à jour du dépôt de suivi n'a été effectuée à ce stade.
