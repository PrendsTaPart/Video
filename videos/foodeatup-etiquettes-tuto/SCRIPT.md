# Tutoriel — Imprimer ses étiquettes (vente / stockage) FoodEatUp

Tutoriel du module `haccp` (Hygiène & HACCP). Durée livrée : **61,68 s** —
H.264 High/yuv420p, AAC 48 kHz stéréo, faststart. Audio : true peak
**-7,31 dBFS**. Decode 0 erreur, moov avant mdat.

## Ce que montre le rush

Le rush (46,6 s, 1920x828) montre, depuis le module "Traçabilité > Étiqueteuse" :
1. La liste des produits (Farine, Abricot, Pizza margaritta) — sélection de
   "Pizza margaritta" (case à cocher) : un compteur "1" et les boutons
   "Retirer de la liste" / "Imprimer 1 étiquette(s)" apparaissent.
2. Clic "Imprimer 1 étiquette(s)" -> modale "Etiqueteuse" : Date, Type
   ("Fait/ouvert" -> "Surgelé"), Produit (1) pré-rempli avec la Pizza margaritta.
3. DLC, numéro de lot ("LOT-PIZZA-20260728") et code-barres de vente,
   ajustables mais calculés/proposés automatiquement.
4. NB étiquettes (1 -> 3) et Équipement de stockage ("frigo (Frigo) - 0°C à
   4°C") -> le bouton "Créer les étiquettes" ne s'active qu'une fois
   l'équipement choisi.
5. "3 étiquette(s) créée(s) avec succès !" -> aperçu des 3 étiquettes
   générées (produit, lot, DLC, équipement), badge "Prêt pour impression".
6. Clic "Valider -> Historique" -> "Étiquettes validées ! 3 étiquette(s) ont
   été ajoutée(s) à l'historique. Voulez-vous consulter l'historique ?" ->
   "Rester ici" -> retour à la liste, sélection remise à zéro.

## claudePrompts — cas d'usage

`mcp__FoodEatUp__create_haccp_label` correspond directement au sujet du
tuto (le numéro de lot est auto-généré si absent, comme dans l'UI). Un seul
`claudePrompt` :

> Crée une étiquette HACCP pour [quantité] [nom du produit], DLC le [date],
> stockée au [équipement de stockage], pour mon établissement FoodEatUp
> (ID [ID établissement]).

## Voix off (10 lignes, voix Adam FR `TGAegA0zNRi8I6nUdq3i`)

| # | Texte | Durée | Segment |
|---|---|---:|---|
| N0 | Imprimer une étiquette de vente ou de stockage à la main ? FoodEatUp génère tout pour vous, en quelques clics. | 6,40 s | intro |
| N1 | Depuis l'Étiqueteuse, sélectionnez le ou les produits à étiqueter. | 3,76 s | A — liste des produits |
| N2 | Renseignez la date, le type d'étiquette, et retrouvez votre produit pré-rempli. | 4,44 s | E — modale Etiqueteuse |
| N3 | La DLC, le numéro de lot et le code-barres de vente sont calculés automatiquement. | 4,36 s | F — DLC/lot/code-barres |
| N4 | Choisissez le nombre d'étiquettes et l'équipement de stockage associé. | 3,42 s | G — quantité + équipement |
| N5 | Vos étiquettes sont générées, prêtes à imprimer, avec toute la traçabilité HACCP. | 5,33 s | J — aperçu des étiquettes |
| N6 | Validez : elles sont ajoutées à votre historique de traçabilité, en un clic. | 4,31 s | L — modale "Étiquettes validées" |
| N7 | Vous pouvez aussi créer une étiquette HACCP directement depuis Claude, en donnant le produit et la DLC. | 7,29 s | Claude — étage 1 (reveal) |
| N8 | Claude crée l'étiquette avec le lot et le stockage, prête à imprimer. | 3,89 s | Claude — étage 3 (chatbot mockup) |
| N9 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (CTA, réutilisée telle quelle depuis `foodeatup-facture-ocr-tuto`) |

N9 réutilisée telle quelle — zéro crédit ElevenLabs dépensé sur cette ligne.
Drift mesuré à l'exécution de `build.py` : N1 décalée de 0,18 s (marge
consommée, sans chevauchement) ; N8/N9 décalées de ~2,2 s car N7 (7,29 s, la
ligne la plus longue de la série à ce jour) déborde largement des étages
Claude 1+2 (4,50+1,40 s) — poussée automatique en cascade, sans
chevauchement, carte de fin auto-étendue de 6,00 à 8,41 s pour absorber le
CTA. Comportement attendu du moteur (voir `FOODEATUP-TUTORIELS-WORKFLOW.md`).

## Découpage

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 6,70 s | IMPRIMER SES ÉTIQUETTES VENTE & STOCKAGE |
| A | 0,20 → 3,80 | 4,20 s | "1 - Sélectionnez vos produits à étiqueter" |
| B | 3,80 → 4,10 | 0,80 s | **zoom-punch** sur la case à cocher (1324, 187) |
| C | 4,10 → 6,90 | 2,40 s | état sélectionné (compteur, boutons) |
| D | 6,90 → 7,20 | 0,80 s | **zoom-punch** sur "Imprimer 1 étiquette(s)" (1681, 748) |
| E | 7,30 → 12,00 | 5,00 s | "2 - Date, type et produit pré-remplis" |
| F | 13,50 → 22,50 | 5,00 s | "3 - DLC, lot et code-barres calculés automatiquement" |
| G | 24,00 → 28,80 | 4,00 s | "4 - Quantité et équipement de stockage" |
| H | 28,80 → 29,10 | 0,80 s | **zoom-punch** sur "Créer les étiquettes" (1028, 719) |
| I | 29,20 → 32,20 | 3,00 s | modale succès (3 étiquette(s) créée(s)) |
| J | 33,00 → 40,20 | 6,00 s | "5 - Étiquettes prêtes, traçabilité HACCP incluse" |
| K | 40,20 → 40,50 | 0,80 s | **zoom-punch** sur "Valider → Historique" (1253, 358) |
| L | 40,60 → 44,50 | 5,00 s | modale "Étiquettes validées !" |
| M | 44,50 → 46,56 | 3,20 s | retour à la liste, sélection réinitialisée |
| claude 1-3 | cartes générées | 4,50 + 1,40 + 4,20 s | séquence "Utilisez cette fonctionnalité avec Claude" |
| outro | carte | 8,41 s (auto-étendue) | CTA |

Coordonnées de clic estimées visuellement sur les frames extraites du rush
(résolution source native 1920x828) ; le crop zoom-punch (~1600x690, marge
~x±160/y±70) absorbe l'imprécision de mesure. Transitions `fade` partout sauf
`slideleft` entre les 3 étages Claude et vers la carte de fin. Le retour à la
liste en fin de rush (segment M) est gardé tel quel — pas de coupe artificielle
— pour boucler proprement sur l'état initial avant l'appel à l'action.

## Animations

Mêmes principes que toute la série : Ken Burns sur les cartes intro/outro,
xfade 0,28 s, bandeaux d'étape en bas d'écran, encadré orange pulsant sur les
4 clics-clés (case à cocher, Imprimer, Créer les étiquettes, Valider ->
Historique). Séquence Claude en 3 temps (reveal / copié / chatbot mockup)
ajoutée juste avant la carte de fin, module partagé
`videos/_shared/claude_prompt_sequence.py` (pas de code dupliqué).

## Statut publication

Montage terminé et checklist de compatibilité passée (H.264 High/yuv420p, AAC
48 kHz stéréo, faststart, peak -7,31 dBFS, 0 erreur de décodage). Publié sur
Lovable (module `haccp`, slug `imprimer-ses-etiquettes`), vidéo hébergée en
raw GitHub sur `videos/foodeatup-etiquettes-tuto/out/`, branche
`claude/foodeatup-tutorial-video-qtwswo`.
