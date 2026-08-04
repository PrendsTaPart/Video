# Tutoriel — Pointer ses actions de nettoyage FoodEatUp

Module « Hygiène & HACCP » (1er tutoriel de ce module, 0/30 publiés jusqu'ici).
Intrants reçus de Michael : `assets/intro.jpg` (carte "POINTER SES ACTIONS AU
QUOTIDIEN"), `assets/outro.jpg` (carte CTA standard, réutilisée telle quelle,
fichier identique à celui de `foodeatup-besoins-production-tuto`), `assets/screen.mp4`
(rush 1920x828, 97,58 s, H.264/AAC).

Durée livrée : **46,52 s** — H.264 High/yuv420p, AAC 48 kHz stéréo, faststart.
Audio : true peak **-6,9 dBFS** (mesuré sur le MP4 final, `astats`). Décodage
sans erreur, moov avant mdat (faststart confirmé).

## Ce que montre le rush (et ce qui en a été exclu)

Menu Hygiène > "Liste des zones à nettoyer" (zones A à E : Cuisine Quotidien, Cuisine
Hebdo, Zone de Stockage, Cuisine Mensuel, Zone de Préparation...). Ouverture de
"A - Cuisine Quotidien" : 5 postes (Électroménager, Inox, Matériel de cuisson, Plan de
travail, Sols), tous "Jamais nettoyé". Clic sur le crayon du poste "Électroménager" →
modal "Programmer le nettoyage" (date + heure, raccourcis "Maintenant" / "Dernière
action") → clic "Programmer" → toast "Action de nettoyage enregistrée avec succès !" —
le poste passe "Récent" avec "Dernière action : ... par Soulayma" (attribution
nominative). Le poste "Inox" affiche déjà "Urgent" à ce moment : statut calculé
automatiquement par l'app selon la fréquence attendue de la zone, pas une action
réalisée dans ce rush. Même flux répété sur "Matériel de cuisson" (2e succès propre).

**Exclu du montage** : le rush continue ensuite (~37s → 97,6s) sur le bouton "Valider"
en haut de la zone (validation groupée de tous les postes), qui tombe sur une erreur
"Zone non trouvée" affichée en rouge, sans se résoudre jusqu'à la fin du rush. Conforme
à la règle de la série (ne jamais mettre en avant un état cassé/non reproductible — voir
`FOODEATUP-TUTORIELS-WORKFLOW.md`, section pièges), le montage s'arrête donc au 2e
succès (56,2 s de rush utilisées sur 97,6 s).

## Voix off (9 lignes, voix Adam FR `TGAegA0zNRi8I6nUdq3i`, `eleven_multilingual_v2`)

| # | Texte | Durée | Ancrage |
|---|---|---:|---|
| N0 | Pointer les actions de nettoyage de votre équipe, jour après jour ? FoodEatUp s'en charge. | 5,09 s | carte d'intro |
| N1 | Depuis Hygiène, retrouvez la liste de vos zones à nettoyer. | 3,24 s | segment A |
| N2 | Ouvrez un poste et cliquez sur le crayon pour programmer son nettoyage. | 3,76 s | segments B+C (clic crayon) |
| N3 | Choisissez la date et l'heure, ou utilisez le bouton Maintenant pour l'instant présent. | 4,36 s | segment D |
| N4 | Cliquez sur Programmer pour valider l'action. | 2,27 s | segment E (clic Programmer) |
| N5 | L'action est enregistrée avec la date, l'heure et le nom de la personne : répétez l'opération sur chaque poste pour garder toute votre équipe à jour, et repérez d'un coup d'œil les postes urgents. | 10,58 s | segments F+G (résultat + 2e poste) |
| N6 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | 4,41 s | étage 1+2 (réutilisé) |
| N7 | Collez-le dans la conversation : l'action de nettoyage est enregistrée en quelques secondes. | 4,91 s | étage 3 |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (CTA, réutilisé) |

N6/N8 réutilisés tels quels depuis `foodeatup-produits-tuto/vo/` (texte générique
identique, zéro crédit ElevenLabs dépensé pour ces deux lignes).

## Découpage (build.py, coordonnées mesurées par seuillage colorimétrique)

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 5,40 s | POINTER SES ACTIONS AU QUOTIDIEN |
| A | 0,20 → 6,70 | 3,20 s | Liste des zones à nettoyer (A à E) |
| B | 6,70 → 9,50 | 2,30 s | Ouverture de la zone A, 5 postes "Jamais nettoyé" |
| C | 9,50 → 9,80 | 0,90 s | **zoom-punch** crayon, poste Électroménager (1596, 195) |
| D | 9,80 → 19,70 | 5,00 s | Modal "Programmer le nettoyage" — date/heure |
| E | 19,70 → 20,00 | 0,90 s | **zoom-punch** bouton "Programmer" (1025, 670) |
| F | 20,00 → 37,50 | 6,00 s | Toast succès, Électroménager "Récent" (par Soulayma), Inox "Urgent" ; le rush inclut aussi un bref survol/ouverture du poste Inox dans cette fenêtre (non soumis — Inox reste "Urgent" jusqu'à la fin), compressé au passage à ×2,9 |
| G | 37,50 → 56,20 | 6,50 s | Répétition sur "Matériel de cuisson" (2e succès propre) |
| claude1 | carte générée | 3,00 s | reveal — prompt en gros, fond crème |
| claude2 | carte générée | 2,30 s | confirmation « Copié dans le presse-papiers ! » |
| claude3 | carte générée | 5,30 s | mockup chatbot Claude |
| outro | carte | auto-étendue depuis 6,20 s pour porter N8 | CTA |

## Séquence Claude — module partagé

`record_cleaning_action(establishment_id, poste_nettoyage_id, statut?, commentaires?)`
correspond exactement au bouton "Programmer" du rush (enregistre une action de
nettoyage sur un poste). `list_cleaning_zones` permet de retrouver l'ID du poste.
Prompt :

> Enregistre le nettoyage du poste [nom du poste] (ID poste [ID poste]) pour mon
> établissement FoodEatUp (ID [ID établissement]).

Même texte prévu côté fiche Lovable (`claudePrompt`).

## Animations

Mêmes principes que toute la série : Ken Burns sur les cartes, xfade (0,28 s),
bandeaux d'étape (aucune apostrophe), encadré orange pulsant sur les 2 clics. Pas de
clip avatar dans ce dossier.

## Statut publication

Produite et publiée en autonomie le 2026-08-03, suite à l'accord donné par Michael le
même jour sur le tutoriel précédent (`deduire-ses-besoins-de-production`) pour ce même
enchaînement script → VO → montage → publication Lovable sans validation intermédiaire.
Voir tableau "Tutoriels publiés" dans `videos/LOVABLE-FOODEATUP-DOCS.md` (entrée #13).
