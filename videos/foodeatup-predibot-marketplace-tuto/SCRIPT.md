# Tutoriel — Piocher dans la marketplace de prompts (PrediBot) FoodEatUp

Module `predibot` (Agent IA Directeur, catégorie Comptabilité & PrediBot), tutoriel 02/3
du catalogue (`videos/CATALOGUE-157-TUTORIELS.md` ligne « 02 Piocher dans la **Marketplace**
de prompts »). Les deux autres vidéos du module existent déjà : `foodeatup-predibot-tuto`
(01, Prévisions) et `foodeatup-predibot-suggestions-tuto` (03, Chat PrediBot).

Rush fourni par Michael : `assets/screen.mp4` (142,66 s, 1920x828, aucune piste audio
utile — VO entièrement ElevenLabs). `assets/intro.jpg` et `assets/outro.jpg` fournis
également (1281x721, outro = carte CTA générique déjà réutilisée sur toute la série).

## Particularité de cette vidéo

Contrairement aux autres tutos, le rush **montre déjà en direct** le round-trip complet
« marketplace → Tester en live → Claude → retour FoodEatUp » — c'est littéralement le
sujet de la vidéo. La séquence synthétique 3-temps du module partagé
(`videos/_shared/claude_prompt_sequence.py`, reveal/copié/chatbot) n'a donc **pas** été
ajoutée en fin de vidéo : elle serait redondante avec ce que la vidéo montre déjà en
entier. Le champ `claudePrompt` de la fiche Lovable reste néanmoins renseigné (voir plus
bas), pour cohérence avec le reste du site.

## Ce que montre le rush

1. Page marketplace de prompts FoodEatUp (`https://foodeatup.com/api/mcp`, connexion
   OAuth 2.0 revocable), filtres par catégorie (Tous 182, Stock & Appro 16, Carte &
   Recettes 20, Commandes 4, Réservations 18, Finance 19, RH 16, Production 6, HACCP 14,
   Système 64, Orchestration 5) — catégorie **Stock & Appro** sélectionnée (0,3 → 12,0 s).
2. Carte de prompt « Crée un nouveau fournisseur » (niveau Intermédiaire), avec le texte
   du prompt affiché tel quel et un bouton **Tester en live** — clic à 15,1 s (14,6 →
   15,9 s).
3. Nouvel onglet Claude, le prompt est déjà collé et envoyé automatiquement
   (15,9 → 25,5 s) : Claude réfléchit, appelle ses outils, puis demande le nom du
   fournisseur et une liste de champs optionnels (type de produits, email/téléphone,
   adresse, site web, livraison, fiabilité, statut).
4. L'utilisateur répond en une phrase dans le chat, en langage naturel (pas de formulaire) :
   « patesserie monaliza, des gateaux, patesseriemonaliza@contact.fr +21625362514, rue de
   fleurs tunis tunisie 4000, livraison disponible oui, actif » — saisie progressive,
   42,0 → 113,3 s (timelapse dans le montage, bien plus rapide qu'en réel).
5. Envoi du message à 113,8 s (113,3 → 114,3 s), puis Claude traite et confirme :
   « C'est fait ! Le fournisseur **Pâtisserie Monaliza** (ID #126) est créé pour votre
   établissement 38 (...) » (114,3 → 122,6 s).
6. Retour sur FoodEatUp, ouverture du menu latéral jusqu'à « Liste des fournisseurs »
   (127,0 → 141,5 s) : la fiche **Pâtisserie Monaliza** apparaît bien dans la liste, aux
   côtés des fournisseurs existants.

## Voix off (9 lignes, voix Adam FR `TGAegA0zNRi8I6nUdq3i`, ElevenLabs `eleven_multilingual_v2`)

| # | Texte | Durée mesurée | Ancrage |
|---|---|---:|---|
| N0 | Piocher dans la marketplace de prompts FoodEatUp ? Toute une bibliothèque de prompts Claude, prête à l'emploi. | 5,69 s | carte d'intro |
| N1 | Cent quatre-vingt-deux prompts triés par catégorie : stock, carte, réservations, finance, RH... | 6,53 s | segment A — vue marketplace |
| N2 | Trouvez le prompt qu'il vous faut, et cliquez sur Tester en live. | 3,00 s | segment B — **zoom-punch** sur Tester en live |
| N3 | Il s'ouvre directement dans Claude, déjà rempli avec votre établissement. | 4,02 s | segment C — bascule + formulaire Claude |
| N4 | Répondez en une phrase avec les infos du fournisseur, Claude s'occupe du reste. | 4,02 s | segment D — timelapse de la saisie |
| N5 | Envoyez, et c'est parti. | 1,44 s | segment E — **zoom-punch** sur le bouton d'envoi |
| N6 | Votre nouveau fournisseur est créé en quelques secondes. | 2,82 s | segment F — confirmation Claude |
| N7 | Retournez sur FoodEatUp : Pâtisserie Monaliza apparaît aussitôt dans votre liste. | 4,18 s | segment G — retour + liste des fournisseurs |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,09 s | carte de fin (CTA) |

## Découpage (targets, avant retiming automatique de l'outro)

| Seg | Source | Sortie cible | Contenu |
|---|---|---:|---|
| intro | carte | 5,90 s | PIOCHER DANS LA MARKETPLACE DE PROMPTS |
| A | 0,30 → 12,00 | 5,80 s | vue marketplace + filtres catégorie |
| B | 14,60 → 15,90 | 0,90 s | **zoom-punch** sur "Tester en live" (1420, 533) |
| C | 15,90 → 25,50 | 4,60 s | bascule Claude + formulaire (nom + champs optionnels) |
| D | 42,00 → 113,30 | 6,00 s | **timelapse** de la saisie en langage naturel (facteur ×11,9) |
| E | 113,30 → 114,30 | 0,90 s | **zoom-punch** sur le bouton d'envoi (1740, 731) |
| F | 114,30 → 122,60 | 3,60 s | Claude traite et confirme la création |
| G | 127,00 → 141,50 | 4,60 s | retour FoodEatUp, navigation, liste des fournisseurs |
| outro | carte | 9,55 s (auto-étendu) | CTA |

Boutons zoom-punch repérés par extraction de frames (`ffmpeg -ss t -frames:v 1`) à 2 Hz
autour de chaque clic, coordonnées en espace source 1920x828 :
- **Tester en live** (carte "Crée un nouveau fournisseur") : centre (1420, 533), taille
  (325, 51). Clic identifié entre 15,5 s (encore sur la marketplace) et 16,0 s (déjà sur
  l'onglet Claude, page d'accueil vide) → posé à 15,1 s (juste avant, pour anticiper le
  zoom).
- **Bouton d'envoi Claude** (flèche orange) : centre (1740, 731), taille (46, 46). Message
  complet visible dans le textarea à 113,3 s, bulle envoyée + "Mulling" à 114,0 s.

Durée totale livrée : **39,68 s** — H.264 High/yuv420p, AAC LC 48 kHz stéréo, faststart.
Audio : true peak **-7,15 dBFS** (mesuré avec `astats` sur le MP4 final, conforme à la
marge de sécurité documentée dans `FOODEATUP-TUTORIELS-WORKFLOW.md`).

## Séquence Claude — pas de module partagé sur cette vidéo

Voir "Particularité de cette vidéo" plus haut : le rush montre déjà tout le cycle avec
Claude, donc pas de séquence de fin ajoutée. Le prompt (identique côté carte marketplace
et côté fiche Lovable `claudePrompt`) :

> Pour mon établissement (ID [ID établissement]), crée un nouveau fournisseur pour un
> établissement. Demande-moi les informations nécessaires.

`mcp__FoodEatUp__create_supplier` (nom exact à vérifier côté outils FoodEatUp — action
« créer un fournisseur ») correspond à cette action.

## Statut publication

Montage terminé et vérifié (checklist de compatibilité passée). **En attente de
validation de Michael avant publication** (Lovable / RapidoCMS / LinkedIn), conformément
à la règle du 2026-08-02 dans `videos/LOVABLE-FOODEATUP-DOCS.md`.
