# Tutoriel — Scanner sa facture (OCR & mise a jour des prix automatique) FoodEatUp

Tutoriel du module `stockvision-ai` / `comptabilite` (StockVision AI & Comptabilite).
Duree livree : **62,64 s** — H.264 High/yuv420p, AAC 48 kHz stereo, faststart.
Audio : true peak **-7,13 dBFS**. Decode 0 erreur, moov avant mdat.

## Ce que montre le rush

Le rush (48,7 s, 1920x828) montre, depuis "Gestion des livraisons" :
1. La liste des livraisons recues, avec fournisseur, prix et statut "Livree".
2. Clic "Voir le detail" sur une livraison -> page detail (statut, fournisseur,
   mode de livraison, dates, prix, produits livres).
3. Section "Facture" ("Aucune facture n'a ete ajoutee pour cette livraison") ->
   clic "+ Ajouter une facture" -> modale "Importer une facture" (glisser-
   deposer PDF/JPG/PNG, 10 Mo max, liee automatiquement a la livraison #2900).
4. Upload de `Facture_FAC-2026-00006.pdf` -> barre de progression "Analyse en
   cours" (15% -> 17% -> 39% "Extraction des donnees en cours" -> 100%
   "Analyse terminee !").
5. Page "Validation de la facture" : fournisseur detecte (FoodEatUp), numero
   de facture, date, produit detecte avec prix unitaire (13,00 €), case
   "MAJ PRIX" pre-cochee pour mettre a jour le catalogue.
6. Selection du Fournisseur ("La Comtesse #6") et de la Livraison associee
   ("DEL-D-42 — soulayma") dans deux menus deroulants, Totaux recalcules
   (13,00 € TTC).
7. Clic "Valider et enregistrer" -> modale "Facture validee ! 1 prix mis a
   jour." + "Depense enregistree dans votre comptabilite." -> clic
   "Voir la depense".
8. Fiche Depense `EXP-A5171F` : resume (13,00 € TTC), fournisseur lie,
   produits achetes, et note "Importe automatiquement depuis la facture :
   facture_FAC-2026-00006.pdf" — zero ressaisie manuelle.

Le montage saute la demonstration du filtre "Toutes les livraisons -> Livree"
(t=4-7s dans le rush, hors-sujet pour ce tuto centre sur l'OCR) et le retour
en haut de page apres la selection fournisseur/livraison (scroll non montre,
enchainement direct sur le clic "Valider et enregistrer").

## claudePrompts — cas d'usage (sequence "Utilisez cette fonctionnalite avec Claude")

Aucun outil `mcp__FoodEatUp__*` ne fait l'OCR a lui seul : le cas d'usage
correspond a l'envoi de la photo de la facture a Claude, qui combine ensuite
`update_product` (prix) et `create_expense` (depense), sur le meme modele que
le prompt "facture fournisseur (image)" deja utilise sur le tutoriel
fournisseurs. Un seul `claudePrompt` (pas de liste `claudePrompts`) :

> Voici la photo de ma facture fournisseur [numero de facture]. Mets a jour
> les prix de mes produits et enregistre la depense correspondante, pour mon
> etablissement FoodEatUp (ID [ID etablissement]).

## Voix off (12 lignes, voix Adam FR `TGAegA0zNRi8I6nUdq3i`)

| # | Texte | Duree | Segment |
|---|---|---:|---|
| N0 | Scanner une facture fournisseur et mettre les prix a jour a la main ? FoodEatUp s'en charge pour vous. | 5,43 s | intro |
| N1 | Chaque livraison recue attend sa facture, pour garder vos couts a jour. | 4,02 s | A — liste des livraisons |
| N2 | Ouvrez le detail de la livraison, puis ajoutez la facture du fournisseur. | 3,71 s | D — detail + clic "+ Ajouter une facture" |
| N3 | Deposez le PDF ou la photo de la facture, en quelques secondes. | 3,29 s | F — modale d'import |
| N4 | L'OCR lit le document et extrait fournisseur, numero de facture et prix, automatiquement. | 5,46 s | G — progression OCR |
| N5 | Verifiez les prix detectes, et cochez ceux a mettre a jour dans votre catalogue. | 4,26 s | H — page Validation de la facture |
| N6 | Reliez la facture au bon fournisseur et a la livraison correspondante. | 3,79 s | I — selection fournisseur/livraison |
| N7 | D'un clic, les prix sont mis a jour et la depense enregistree dans votre comptabilite. | 4,55 s | K — modale "Facture validee !" |
| N8 | La depense est aussitot visible, reliee a sa facture d'origine, zero ressaisie. | 4,78 s | M — fiche Depense |
| N9 | Vous pouvez aussi le faire depuis Claude : envoyez la photo de la facture, et donnez l'instruction. | 5,15 s | Claude — etage 1 (reveal) |
| N10 | Claude met a jour vos prix et enregistre la depense a votre place. | 3,71 s | Claude — etage 3 (chatbot mockup) |
| N11 | Passez a la restauration intelligente avec FoodEatUp. Essayez gratuitement des aujourd'hui ! | 5,02 s | carte de fin (CTA, reutilisee telle quelle depuis `foodeatup-devis-statuts-tuto`) |

N11 reutilisee telle quelle — zero credit ElevenLabs depense sur cette ligne
(texte identique, CTA generique). Drift mesure a l'execution de `build.py` :
N1/N4/N5 decalees de 0,13-0,19 s (marge de securite consommee, sans
chevauchement) ; N10 et N11 decalees de ~1,5 s car N9 (5,15 s) deborde des
etages Claude 1+2 (3,00+1,40 s) — poussee automatique en cascade, sans
chevauchement, et carte de fin auto-etendue de 6,00 a 7,60 s pour absorber le
CTA. Comportement attendu du moteur (voir `FOODEATUP-TUTORIELS-WORKFLOW.md`).

## Decoupage

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 5,80 s | SCANNER SA FACTURE — OCR & PRIX AUTO |
| A | 0,20 → 3,70 | 4,40 s | "1 - Vos livraisons recues" |
| B | 7,00 → 8,55 | 1,50 s | survol de "Voir le detail" |
| C | 8,55 → 8,85 | 0,80 s | **zoom-punch** sur "Voir le detail" (372, 608) |
| D | 8,90 → 11,70 | 4,00 s | "2 - Ouvrez le detail et ajoutez la facture" |
| E | 11,70 → 12,00 | 0,80 s | **zoom-punch** sur "+ Ajouter une facture" (1586, 497) |
| F | 12,00 → 13,00 | 3,60 s | "3 - Deposez le PDF ou la photo" (modale d'import) |
| G | 15,80 → 21,90 | 6,00 s | "4 - Analyse OCR et extraction des donnees" (15% → 100%) |
| H | 22,50 → 26,80 | 5,60 s | "5 - Fournisseur, facture et prix detectes" |
| I | 27,00 → 33,60 | 6,00 s | "6 - Fournisseur et livraison lies" |
| J | 36,60 → 36,90 | 0,80 s | **zoom-punch** sur "Valider et enregistrer" (1537, 492) |
| K | 37,50 → 40,60 | 5,20 s | modale "Facture validee !" |
| L | 40,60 → 40,90 | 0,80 s | **zoom-punch** sur "Voir la depense" (830, 579) |
| M | 41,50 → 48,70 | 5,60 s | "7 - La depense est creee automatiquement" (fiche Depense) |
| claude 1-3 | cartes generees | 3,00 + 1,40 + 4,20 s | sequence "Utilisez cette fonctionnalite avec Claude" |
| outro | carte | 7,60 s (auto-etendue) | CTA |

Coordonnees de clic estimees visuellement sur les frames extraites du rush
(resolution source native 1920x828) ; le crop zoom-punch (~1600x690, marge
~x±160/y±70) absorbe l'imprecision de mesure. Transitions `fade` partout sauf
`slideleft` entre les 3 etages Claude (scenes distinctes) et vers la carte de
fin.

## Animations

Memes principes que toute la serie : Ken Burns sur les cartes intro/outro
(zoom avant en ouverture, zoom arriere en fin), xfade 0,28 s, bandeaux
d'etape en bas d'ecran, encadre orange pulsant sur les 4 clics-cles (Voir le
detail, + Ajouter une facture, Valider et enregistrer, Voir la depense). La
demonstration du filtre de statut (debut du rush) et le retour en haut de
page (avant validation) sont coupes au montage — hors-sujet / repetitifs.
Sequence Claude en 3 temps (reveal / copie / chatbot mockup) ajoutee juste
avant la carte de fin, module partage `videos/_shared/claude_prompt_sequence.py`
(pas de code duplique).

## Statut publication

Montage termine et checklist de compatibilite passee (H.264 High/yuv420p, AAC
48 kHz stereo, faststart, peak -7,13 dBFS, 0 erreur de decodage). **En attente
de validation** avant publication (regle du 2026-08-02) : ni upload/schedule
RapidoCMS+LinkedIn, ni mise a jour du site Lovable tant que Michael n'a pas
donne son accord sur le montage livre.
