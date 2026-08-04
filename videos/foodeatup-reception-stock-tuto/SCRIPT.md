# Tutoriel — Valider son entree stock : temperature & EAN (HACCP reception)

Rush source : "Creation des temperatures des livraisons, Validations du stock et
etiquettes code EAN" (52,28 s, 1920x828, 25 fps). Duree livree : **49,44 s** —
H.264 High/yuv420p, AAC 48 kHz stereo, faststart. Audio : true peak **-7,2 dBFS**.
Decode 0 erreur.

## Voix off (9 lignes)

| # | Texte | Duree | Ancrage |
|---|---|---:|---|
| N0 | Valider l'entree d'un stock chez FoodEatUp : temperature des produits et code-barres EAN, en quelques clics. | 6,77 s | carte d'intro |
| N1 | Depuis Gestion des livraisons, faites avancer le statut : expediee, puis confirmez la reception. | 5,25 s | clics Marquer comme expediee + Confirmer reception |
| N2 | Rendez-vous dans HACCP puis Reception pour retrouver vos livraisons du jour. | 4,91 s | navigation menu -> HACCP -> Reception |
| N3 | Ouvrez le controle d'un produit livre pour verifier sa conformite. | 3,37 s | recherche + ouverture du detail de commande |
| N4 | Renseignez la temperature mesuree a reception, et enregistrez. | 3,42 s | modal Temperature, 4.0 -> 6.5C, Enregistrer |
| N5 | Scannez aussi le code-barres EAN du produit pour tracer son origine. | 4,31 s | modal Scanner produit (camera EAN) |
| N6 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | 4,41 s | **reutilise tel quel** depuis foodeatup-fournisseurs-tuto (0 credit ElevenLabs) |
| N7 | Collez-le dans la conversation : votre controle de reception est enregistre en quelques secondes. | 4,86 s | etage 3 chatbot |
| N8 | Passez a la restauration intelligente avec FoodEatUp. Essayez gratuitement des aujourd'hui ! | 5,02 s | carte de fin (**reutilisee**) |

N6/N8 copies directement depuis `foodeatup-fournisseurs-tuto/vo/` (memes fichiers,
texte generique applicable a tout tutoriel). N0,N1,N2,N3,N4,N5,N7 generes via
ElevenLabs (voix Adam FR, `TGAegA0zNRi8I6nUdq3i`) — generation bloquee une premiere
fois par quota ElevenLabs epuise (35 credits restants), relancee apres recharge du
compte par Michael.

## Piege rencontre et corrige pendant ce build

**Erreur de lecture des timestamps sur les premieres passes d'analyse (contact
sheets redimensionnes).** En repérant les points de coupe a partir de planches-
contact (frames extraites toutes les 0,5-2s puis assemblees et redimensionnees a
30-40% pour tenir dans une seule image), deux plages ont ete mal datees de 1 a 2
secondes : le clic "Confirmer reception" et le clic sur "..." menu produit,
lus a des instants qui ne correspondaient pas exactement au contenu reel une fois
verifie frame par frame en taille native. Repere en QA visuel sur le premier
rendu : le segment K (26.80-27.20s) tombait en plein milieu du modal "Photo DLC"
(non montre dans le montage final, cf. plus bas) au lieu du tableau produit propre
attendu. Corrige en re-extrayant des frames a taille native (1920x828, pas de
redimensionnement) autour de chaque point de coupe suspect avant de figer les
timestamps de `build.py`. **Lecon : toujours verifier un point de coupe critique
sur une frame en taille native, jamais uniquement sur une planche-contact
redimensionnee.**

**Calibrage des segments sur la duree VO, pas l'inverse (bug deja documente,
reproduit puis corrige ici).** Premier rendu : jusqu'a 6,4s de derive entre
l'ancrage prevu et l'offset reel (ex. N4 "Renseignez la temperature..." se serait
retrouve a jouer pendant la sequence Scanner produit). Cause : segments visuels
trop courts pour porter des lignes VO de 3,4 a 6,8s. Corrige en allongeant les
segments concernes (carte d'intro 3.0 -> 4.6s, et la plupart des segments
intermediaires) jusqu'a ce que chaque groupe de segments associe a une ligne VO
dure au moins autant qu'elle. Deuxieme rendu : derive residuelle 0,35s sur N1
seulement (negligeable), toutes les autres lignes tombent pile sur leur ancrage.

## Decoupage (montage final, apres compression du rush)

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 4,60 s | VALIDER SON ENTREE STOCK TEMPERATURE & EAN |
| A | 0,30 -> 2,30 | 2,80 s | Gestion des livraisons, etat initial |
| B | 3,30 -> 3,60 | 0,90 s | **zoom-punch** clic "Marquer comme expediee" (1525,393) |
| C | 3,60 -> 5,30 | 1,80 s | dialog "Confirmer le changement de statut ?" + Confirmer |
| D | 6,00 -> 7,20 | 1,30 s | toast "Statut mis a jour" |
| E | 8,00 -> 8,30 | 0,90 s | **zoom-punch** bouton "Confirmer reception" (1526,763) |
| F | 12,25 -> 14,20 | 2,00 s | dialog "Confirmer la reception de la livraison ?" + Confirmer |
| G | 14,50 -> 16,00 | 1,40 s | toast "Livraison confirmee" |
| H | 17,30 -> 19,30 | 2,80 s | menu -> HACCP -> Controle a reception |
| I | 19,40 -> 22,20 | 3,00 s | page Reception du jour + recherche tapee |
| J | 22,30 -> 25,10 | 3,60 s | resultat filtre -> clic -> detail commande (Livree) |
| K | 25,20 -> 25,70 | 1,00 s | menu "..." ouvert (Photo DLC / DLC manuelle / Temperature / Scanner produit) |
| L | 37,60 -> 37,90 | 0,90 s | menu reouvert, "Temperature" survole |
| M | 38,00 -> 42,70 | 3,60 s | modal Temperature : 4.0 -> 5.0 -> 6.5C, clic Enregistrer |
| N | 43,00 -> 45,50 | 2,00 s | tableau mis a jour (6.5C) + toast "Temperature enregistree" |
| O | 46,00 -> 46,30 | 1,00 s | menu reouvert, "Scanner produit" survole |
| P | 46,50 -> 48,80 | 2,80 s | modal Scanner produit, camera EAN active |
| Q | 48,80 -> 50,30 | 1,70 s | fermeture scanner -> retour tableau |
| claude1 | carte generee | 3,00 s | reveal — prompt en gros, fond creme |
| claude2 | carte generee | 2,30 s | confirmation "Copie dans le presse-papiers !" |
| claude3 | carte generee | 5,30 s | mockup chatbot Claude |
| outro | carte | 6,20 s | CTA |

**Detours volontairement coupes du montage final** : entre K (25,70s source) et L
(37,60s source), le rush explore aussi "Photo DLC" (~26,6-31s) et "DLC manuelle"
(~32-36,6s) — deux options du meme menu, mais pas le sujet du tutoriel (temperature
+ EAN, per les cartes intro/outro fournies). Coupees via un `slideleft` (cut
assume), pas montrees a l'ecran ni dans le script VO.

## Sequence Claude — module partage

`mcp__FoodEatUp__create_haccp_reception(establishment_id, date_controle,
heure_controle, etat_livraison, fournisseur_nom/fournisseur_id, reference_bl,
temperature_produits_frais)` existe — schema verifie avant redaction du prompt,
les champs correspondent a ce que montre le rush (fournisseur, reception
confirmee, temperature saisie a 6,5C) :

> Enregistre un controle de reception HACCP pour [nom du fournisseur], le [date]
> a [heure], etat [conforme/non_conforme], avec une temperature produits frais de
> [temperature]C, pour mon etablissement FoodEatUp (ID [ID etablissement]).

Meme texte cote fiche Lovable (`claudePrompt`). Un second outil correspond aussi
au volet EAN/etiquette (`mcp__FoodEatUp__create_haccp_label`, DLC/lot/temperature)
— documente comme deuxieme `claudePrompts[]` sur la fiche Lovable, pas anime dans
la video (une seule sequence chatbot par video, comme sur les tutos precedents).

## Astuce du chef (Lovable)

Le scan du code-barres EAN peut directement alimenter la creation d'une etiquette
HACCP (numero de lot auto-genere), exploitable en cuisine sans ressaisie.

## Animations

Memes principes que toute la serie : Ken Burns sur les cartes, xfade (0,28 s),
bandeaux d'etape (3), encadre orange pulsant sur les 2 clics logistique
(expediee / confirmer reception). Pas de clip avatar dans ce dossier.

## Statut publication

**Script et rendu final valides.** Video + vignette uploadees sur RapidoCMS
(`foodeatup-reception-stock-tuto-v1` / `-thumbnail`). Tutoriel
`controler-sa-reception-stock` ajoute sur Lovable (`src/data/tutorials.ts`,
module HACCP — premiere video du module) le 2026-08-04. LinkedIn : pas encore
programme (publication Lovable demandee explicitement dans ce tour, pas la
diffusion reseaux sociaux).
