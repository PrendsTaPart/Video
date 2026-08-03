# Tutoriel — Changer les statuts d'un devis FoodEatUp

Deuxième vidéo du module `comptabilite` (Comptabilité & Achats), Drive :
"CHANGER LES STATUTS D'UN DEVIS". Durée livrée : **41,3 s** — H.264 High/yuv420p,
AAC 48 kHz stéréo, faststart. Audio : true peak **-7,3 dBFS**. Decode 0 erreur,
moov avant mdat.

## Ce que montre le rush

Le rush (38,1 s, 1920x828) montre, depuis l'onglet "Devis" de Facturation :
1. La liste des devis avec leurs statuts (Brouillon, En attente, Signé) — clic
   sur le menu d'actions (⋮) du devis #D20260004 (En attente, 1 327,00 €) →
   "Visualiser".
2. La page détail du devis : informations, articles, historique ("Devis créé"
   → "Envoyé au client"), actions rapides (Dupliquer, Nouveau devis).
3. Clic sur "Téléchargements et options" → menu déroulant : Télécharger PDF,
   Renvoyer, Modifier, **Marquer comme accepté**, Marquer comme refusé,
   Supprimer.
4. Clic "Marquer comme accepté" → modale de confirmation "Marquer ce devis
   comme accepté ?" → OK → toast "Devis marqué comme accepté !" → le statut
   passe à "Signé" et le menu d'actions change (Télécharger PDF / Convertir en
   facture).
5. Retour à la liste via le fil d'Ariane "Facturation" → le devis apparaît
   bien "Signé" et le compteur "En attente de paiement" passe de 8 à 7.

Entre le retour à la liste et son affichage définitif, le rush contient un
rechargement de page (flash blanc, ~10 s) pendant lequel un toast sans rapport
("Devis créé avec succès et envoyé par email") reste affiché — reliquat d'une
notification précédente, non lié au changement de statut. Ce passage est
sauté au montage : les segments N (clic sur le fil d'Ariane) et O (liste
finale) ne sont pas contigus dans la source, pour ne montrer que l'état
correct et persistant.

## claudePrompts — cas d'usage (à la demande du demandeur)

`mcp__FoodEatUp__update_quote_status` est une correspondance directe avec le
sujet du tuto (statuts `brouillon`/`envoye`/`accepte`/`refuse`/`expire`).
`mcp__FoodEatUp__list_quotes` (filtre par statut) permet de retrouver les
devis à traiter avant de changer leur statut. 3 `claudePrompts` proposés :
1. Marquer un devis comme accepté (`update_quote_status`, statut `accepte`).
2. Marquer un devis comme refusé (`update_quote_status`, statut `refuse`).
3. Lister tous les devis en attente de paiement pour savoir lesquels traiter
   (`list_quotes`, filtre `envoye`).

## Voix off (10 lignes, voix Adam FR `TGAegA0zNRi8I6nUdq3i`)

| # | Texte | Durée | Segment |
|---|---|---:|---|
| N0 | Faites évoluer le statut de vos devis, de l'envoi jusqu'à la signature. | 4,02 s | intro |
| N1 | Chaque devis affiche son statut : brouillon, en attente ou signé. | 4,60 s | A — liste |
| N2 | Ouvrez le menu d'actions puis visualisez le devis à traiter. | 3,06 s | C/D — menu + visualiser |
| N3 | Vérifiez les informations, les articles et l'historique avant de trancher. | 3,94 s | E — détail du devis |
| N4 | Le menu Téléchargements et options permet de changer son statut. | 3,34 s | F/G — ouverture du menu statuts |
| N5 | Marquez-le comme accepté, ou refusé si besoin, en un clic. | 3,19 s | H/I/J — accepté + confirmation + OK |
| N6 | FoodEatUp confirme aussitôt la mise à jour. | 2,12 s | K/L — toast succès |
| N7 | Une fois signé, convertissez-le directement en facture. | 2,95 s | M — statut Signé, nouvelles actions |
| N8 | Le nouveau statut apparaît immédiatement dans la liste des devis. | 3,16 s | N/O — retour liste, statut enregistré |
| N9 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (CTA, réutilisé tel quel depuis `foodeatup-produits-tuto`) |

N9 réutilisé tel quel — zéro crédit ElevenLabs dépensé sur cette ligne. Drift :
**aucun** — chaque segment de contenu a été dimensionné (marge ≥0,35 s) au-delà
de la durée mesurée de sa voix off, donc chaque ligne tombe exactement sur son
ancrage. Outro auto-étendue de 6,20 à 8,44 s pour caler le CTA (comportement
normal).

## Découpage

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 4,70 s | CHANGER LES STATUTS D'UN DEVIS |
| A | 0,20 → 5,00 | 5,30 s | "1 - Vos devis et leur statut" |
| B | 4,85 → 5,15 | 0,80 s | **zoom-punch** sur le menu d'actions ⋮ (1655, 165) |
| C | 5,15 → 6,55 | 3,30 s | "Ouvrez le menu Actions" (menu déroulant visible) |
| D | 6,60 → 6,90 | 0,80 s | **zoom-punch** sur "Visualiser" (1510, 210) |
| E | 7,05 → 11,15 | 4,70 s | "2 - Consultez le devis" (infos, articles, historique) |
| F | 11,70 → 12,00 | 0,80 s | **zoom-punch** sur "Téléchargements et options" (1620, 290) |
| G | 12,05 → 13,35 | 3,60 s | "3 - Choisissez le nouveau statut" (menu déroulant) |
| H | 14,25 → 14,55 | 0,80 s | **zoom-punch** sur "Marquer comme accepté" (1520, 160) |
| I | 14,60 → 15,50 | 2,60 s | "Confirmez le changement" (modale) |
| J | 15,55 → 15,85 | 0,80 s | **zoom-punch** sur OK de la modale (1095, 105) |
| K | 16,30 → 17,75 | 2,00 s | "Statut mis à jour" (toast succès) |
| L | 17,85 → 18,15 | 0,80 s | **zoom-punch** sur OK du toast (1225, 100) |
| M | 18,40 → 22,10 | 3,70 s | "4 - Nouvelles actions disponibles" (statut Signé) |
| N | 22,20 → 22,50 | 0,80 s | **zoom-punch** sur le fil d'Ariane "Facturation" (160, 268) |
| O | 34,00 → 37,90 | 3,60 s | "Statut enregistré dans la liste" (Signé, compteur 7) |
| outro | carte | 8,44 s (auto-étendue) | CTA |

Coordonnées de clic mesurées directement sur les frames extraites du rush,
résolution source native 1920x828. Segments N et O non contigus dans la
source (rechargement de page sauté, voir plus haut).

## Animations

Mêmes principes que toute la série : Ken Burns sur les cartes, xfade (0,28 s,
uniquement `fade` — aucune vraie coupure de scène, tout se passe sur le même
écran/panneau), bandeaux d'étape, encadré orange pulsant sur les 7 clics (menu
actions, Visualiser, Téléchargements et options, Marquer comme accepté, OK
modale, OK toast, fil d'Ariane Facturation). Pas de séquence Claude animée — 3
`claudePrompts` texte suffisent ici. Pas de clip avatar.

## Statut publication

Montage terminé et checklist de compatibilité passée (H.264 High/yuv420p, AAC 48 kHz
stéréo, faststart, peak -7,3 dBFS, 0 erreur de décodage). **En attente de validation
avant publication** (règle du 2026-08-02, `videos/LOVABLE-FOODEATUP-DOCS.md`) : pas
d'upload RapidoCMS/LinkedIn (RapidoCMS non authentifié dans cette session de toute
façon), pas d'envoi du prompt Lovable tant que la vidéo n'a pas été revue.
