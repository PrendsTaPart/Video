# Tutoriel — Gérer ses fournisseurs côté achats FoodEatUp

Première vidéo du module `comptabilite` (Comptabilité & Achats), Drive : "GÉRER
SES FOURNISSEURS CÔTÉ ACHATS". Durée livrée : **35,4 s** — H.264 High/yuv420p,
AAC 48 kHz stéréo, faststart. Audio : true peak **-7,3 dBFS**. Decode 0 erreur,
moov avant mdat.

## Ce que montre le rush

Le rush (79,2 s, 1920x828) montre le cycle complet de gestion d'un fournisseur,
depuis la page "Liste des fournisseurs" :
1. Clic "Ajouter un fournisseur" → formulaire complet : nom (Carrefour), adresse
   (Paris, France), email, téléphone, catégorie (Légumes), case "Livraison"
   cochée, note de fiabilité (4 étoiles) → "Enregistrer" → le fournisseur
   apparaît aussitôt dans la liste (4,0/5).
2. Clic "Modifier" sur la carte Carrefour → la note de fiabilité est remontée à
   5 étoiles → "Mettre à jour" → toast "Fournisseur mis à jour avec succès !" →
   la carte affiche désormais 5,0/5.
3. Clic "Supprimer" sur la carte Carrefour → modale de confirmation "Êtes-vous
   sûr ? Voulez-vous vraiment supprimer carrefour ?" → clic **"Annuler"** — la
   suppression n'est **pas** confirmée dans le rush, le fournisseur Carrefour
   reste dans la liste jusqu'à la fin.

Les deux longues phases de saisie (création ~44s, ajustement de la fiabilité en
mode édition ~15s) sont accélérées en montage (facteur `setpts` élevé, jamais de
`zoompan` sur les rushs réels) plutôt que coupées, pour montrer que tous les
champs sont bien renseignés sans étirer inutilement le tuto.

## claudePrompts — cas d'usage (à la demande du demandeur)

`mcp__FoodEatUp__create_supplier` (avec `reliability` et `livraison`) couvre la
création directe. Pas d'outil `update_supplier`/`delete_supplier` exposé — cohérent
avec le rush qui ne montre d'ailleurs jamais de suppression confirmée. En
revanche, `mcp__FoodEatUp__create_supplier_order` est spécifique à l'angle
achats de ce module : passer une commande à un fournisseur existant. Et
`mcp__FoodEatUp__list_suppliers`/`get_supplier` couvrent la consultation avant
de commander. 3 `claudePrompts` proposés :
1. Créer un fournisseur directement (`create_supplier`).
2. Passer une commande à un fournisseur (`create_supplier_order`) — cas d'usage
   achats.
3. Vérifier les infos d'un fournisseur avant de commander (`list_suppliers`).

## Voix off (9 lignes, voix Adam FR `TGAegA0zNRi8I6nUdq3i`)

| # | Texte | Durée | Segment |
|---|---|---:|---|
| N0 | Gérer ses fournisseurs, aussi vu côté achats et comptabilité. | 3,19 s | intro |
| N1 | Retrouvez la liste de vos fournisseurs, prête à commander. | 3,00 s | A — liste |
| N2 | Ajoutez un fournisseur : coordonnées, catégorie, livraison et fiabilité. | 4,83 s | C — montage saisie |
| N3 | Il apparaît aussitôt dans la liste. | 1,75 s | E — ajouté |
| N4 | Modifiez-le à tout moment, par exemple sa note de fiabilité. | 3,29 s | G — montage édition |
| N5 | La mise à jour est immédiate. | 1,57 s | I — mis à jour |
| N6 | Avant toute suppression, FoodEatUp vous demande confirmation. | 3,19 s | K — modale confirmation |
| N7 | De quoi éviter une erreur qui casserait vos commandes en cours. | 3,11 s | M — annulé |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (CTA, réutilisé tel quel depuis `foodeatup-produits-tuto`) |

N8 réutilisé tel quel — zéro crédit ElevenLabs dépensé sur cette ligne. Drift
maximal ≤0,53s sur toutes les lignes sauf la carte de fin (auto-étendue de 6,20
à 8,15s pour caler le CTA, comportement normal).

## Découpage

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 3,20 s | GÉRER SES FOURNISSEURS CÔTÉ ACHATS |
| A | 0,20 → 3,00 | 3,20 s | "Liste des fournisseurs" |
| B | 3,85 → 4,15 | 0,80 s | **zoom-punch** sur "Ajouter un fournisseur" (1670, 345) |
| C | 4,30 → 48,00 | 5,50 s | montage accéléré : saisie complète du formulaire |
| D | 49,70 → 50,10 | 0,80 s | **zoom-punch** sur "Enregistrer" (1055, 745) |
| E | 50,30 → 53,00 | 2,60 s | Carrefour ajouté à la liste (4,0/5) |
| F | 53,45 → 53,75 | 0,80 s | **zoom-punch** sur "Modifier" (390, 515) |
| G | 53,80 → 68,60 | 4,20 s | montage accéléré : fiabilité 4→5 étoiles |
| H | 68,65 → 68,95 | 0,80 s | **zoom-punch** sur "Mettre à jour" (1050, 745) |
| I | 69,00 → 72,30 | 2,80 s | toast succès, note à 5,0/5 |
| J | 73,45 → 73,75 | 0,80 s | **zoom-punch** sur "Supprimer" (210, 657) |
| K | 73,80 → 77,20 | 2,60 s | modale "Êtes-vous sûr ?" |
| L | 76,90 → 77,20 | 0,80 s | **zoom-punch** sur "Annuler" (1082, 587) |
| M | 77,60 → 79,20 | 2,00 s | retour à la liste, Carrefour toujours présent |
| outro | carte | 8,15 s (auto-étendue) | CTA |

Coordonnées de clic mesurées directement sur les frames extraites du rush,
résolution source native 1920x828.

## Animations

Mêmes principes que toute la série : Ken Burns sur les cartes, xfade (0,28 s,
uniquement `fade` — aucune vraie coupure de scène, tout se passe sur le même
écran), bandeaux d'étape, encadré orange pulsant sur les 6 clics (Ajouter,
Enregistrer, Modifier, Mettre à jour, Supprimer, Annuler). Un bug de cadrage sur
le zoom-punch "Annuler" (fenêtre source trop tardive, la modale s'était déjà
refermée) a été corrigé en avançant la fenêtre à 76,90-77,20s. Pas de séquence
Claude animée — 3 `claudePrompts` texte suffisent ici. Pas de clip avatar.

## Statut publication

Montage terminé et checklist de compatibilité passée (H.264 High/yuv420p, AAC 48 kHz
stéréo, faststart, peak -7,3 dBFS, 0 erreur de décodage). **En attente de validation
avant publication** (règle du 2026-08-02, `videos/LOVABLE-FOODEATUP-DOCS.md`) : pas
d'upload RapidoCMS/LinkedIn (RapidoCMS non authentifié dans cette session de toute
façon), pas d'envoi du prompt Lovable tant que la vidéo n'a pas été revue.
