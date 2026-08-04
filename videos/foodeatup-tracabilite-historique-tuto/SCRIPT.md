# Tutoriel — Retrouver ma traçabilité (historique) FoodEatUp

**STATUT : PUBLIÉE (2026-08-04).** Validée, uploadée sur RapidoCMS (vidéo + vignette), et
ajoutée à `src/data/tutorials.ts` sur le site Lovable FoodEatUp Academy (module `haccp`,
slug `retrouver-lhistorique-de-la-tracabilite`). Pas de post LinkedIn programmé (non demandé
pour cette vidéo).

Durée livrée : **42,84 s** — H.264 High/yuv420p 1920×828, AAC 48 kHz stéréo, faststart.
Audio : max_volume **-7,2 dBFS** (identique au réglage de référence `foodeatup-tva-tuto`).
Fichiers : `out/foodeatup-tracabilite-historique-tuto-v1.mp4`, `out/thumbnail-youtube.jpg`
(1280×720, recadré depuis la carte d'intro, même méthode que les tutos précédents).

Module 4 « HACCP » (30 vidéos prévues). Rush fourni : `Historique_de_la_traçabilité.mp4`
(1920×828, 22,28 s, aucun avatar — cohérent avec le constat de `FAISABILITE-SERIE-TUTORIELS.md`
§3.1 : le module HACCP n'a pas de clip avatar, format carte intro + écran commenté).
Carte d'intro fournie : `RETROUVER MA TRAÇABILITÉ HISTORIQUE.jpg`. Carte de fin : asset
générique déjà en dépôt (174 269 octets, identique à celui utilisé sur les autres tutos).

## Déroulé reconstitué à partir du rush (frames extraites toutes les 0,5 s)

1. 0,0–4,0 s : la page « Traçabilité complète » est déjà ouverte, le curseur glisse vers
   l'onglet **Historique** dans la barre du haut.
2. ~4,0–6,0 s : clic sur **Historique** → tableau de bord « historique haccp » (cartes
   Températures / Traçabilité / Plan de nettoyage / Production / …).
3. ~6,0–8,0 s : clic sur la carte **Traçabilité** → page « Historique traçabilité »
   (recherche produit, filtres Tous/Simplifiée/Complète, filtre Toutes les dates), liste
   des produits tracés (ex. Abricot — Complète, 1 traçage, dernier 28/07/2026).
4. ~8,0–10,0 s : clic sur la ligne **Abricot** → dépliage du détail : tableau
   Date/heure, Qté, Lot, DLC, Photos, Remarques, Utilisateur, Actions.
5. ~10,0–14,0 s : survol puis clic sur **Modifier** → modal d'édition complet (Date de la
   traçabilité, Heure, Quantité, Date limite de consommation, N° de lot, Ajouter des
   photos, Remarques).
6. ~14,0–18,0 s : fermeture du modal, clic sur **Supprimer** → boîte de confirmation
   « Êtes-vous sûr de vouloir supprimer cette traçabilité ? » (OK/Annuler).
7. ~18,0–22,3 s : **Annuler** (rien n'est supprimé dans la démo) → retour à la page,
   onglet Historique actif (surligné bleu).

Coordonnées pixel précises des clics et facteurs de vitesse par segment : à relever au
moment du montage (`build.py`), une fois le script validé — pas avant, pour ne pas perdre
ce travail si le texte change.

## Voix off proposée (9 lignes, voix Adam FR `TGAegA0zNRi8I6nUdq3i`)

| # | Texte | Ancrage |
|---|---|---|
| N0 | Besoin de retrouver une traçabilité passée ? FoodEatUp garde tout en mémoire. | carte d'intro |
| N1 | Direction l'onglet Historique, en haut à droite. | clic Historique |
| N2 | Cliquez sur la carte Traçabilité, parmi les historiques HACCP. | clic carte Traçabilité |
| N3 | Chaque produit tracé apparaît ici, avec sa dernière date. | liste (Abricot) |
| N4 | Ouvrez une ligne : date, heure, quantité, lot, DLC, photos, tout y est. | dépliage du détail |
| N5 | Une erreur ? Le bouton Modifier corrige la fiche en quelques secondes. | clic Modifier / modal |
| N6 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | **réutilisée telle quelle** (mp3 déjà copié depuis `foodeatup-tva-tuto`) — étage 1+2 |
| N7 | Collez-le dans la conversation : tout votre historique de traçabilité s'affiche aussitôt. | étage 3 (mockup chatbot) |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | carte de fin (CTA) — **réutilisée telle quelle** |

N6.mp3 et N8.mp3 sont déjà copiés dans `vo/` (identiques à `foodeatup-tva-tuto`, texte
inchangé). **Seules N0 à N5 et N7 restent à générer via ElevenLabs** une fois ce script
validé (7 lignes, pas 9).

## Séquence de fin « cas d'usage + prompt Claude »

Outil MCP FoodEatUp correspondant à l'action de la vidéo : **`list_haccp_tracabilite`**
(liste les enregistrements de traçabilité HACCP d'un établissement, avec filtre de statut
optionnel « complété »/« non complété »). Correspondance directe avec le tutoriel
(consultation de l'historique) → séquence à ajouter, module partagé
`videos/_shared/claude_prompt_sequence.py` (reveal → copié → mockup chatbot), template
`foodeatup-tva-tuto`.

Prompt proposé (identique côté vidéo et côté fiche Lovable `claudePrompt`) :

> Montre-moi l'historique de traçabilité HACCP de mon établissement FoodEatUp
> (ID [ID établissement]).

## Fiche Lovable (préparée, à envoyer après validation + publication)

- `slug` : `retrouver-ma-tracabilite-historique`
- `moduleSlug` : `haccp`
- `title` : « Retrouver ma traçabilité (historique) »
- `howItWorks` : Ouvrez l'onglet Historique → cliquez sur la carte Traçabilité → ouvrez une
  ligne pour voir le détail complet (date, quantité, lot, DLC, photos, remarques) →
  corrigez avec Modifier si besoin.
- `whatItsFor` : Retrouver en quelques secondes l'historique complet de vos traçabilités
  HACCP pour un contrôle, un audit ou une simple vérification — sans ressaisir quoi que
  ce soit.
- `claudePrompt` : voir ci-dessus.

## Prochaines étapes (bloquées tant que le script n'est pas validé)

1. Validation du script par Michael (ce document).
2. Génération ElevenLabs des 7 lignes manquantes (N0-N5, N7).
3. Montage (`build.py`, relevé précis des clics/timestamps sur le rush, zoom-punch,
   séquence Claude, cartes intro/outro).
4. Livraison du MP4 pour validation (STOP obligatoire, étape 6 du workflow) — **aucune
   publication RapidoCMS/LinkedIn/Lovable avant retour explicite de Michael**.
5. Une fois validé : publication + mise à jour de `LOVABLE-FOODEATUP-DOCS.md` (tableau des
   tutoriels publiés) et du suivi du dépôt.
