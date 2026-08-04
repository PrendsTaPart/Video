# Tutoriel — Une photo, l'IA contrôle votre nettoyage (Module Hygiène)

Module « Hygiène » > « Contrôle de conformité ». Rush fourni :
`Prendre_une_photo_et_faite_analyser_l'ia_pour_avoir_un_rapport_de_nettoyage.mp4`
(1920x828, 25fps, 35,72 s). Intro fournie : `UNE PHOTO IA CONTRÔLE VOTRE NETTOYAGE.jpg`.
Outro CTA générique (réutilisée telle quelle).

Pas d'avatar sur ce rush — VO ElevenLabs (Adam FR, `TGAegA0zNRi8I6nUdq3i`) sur toute la vidéo.

## Déroulé observé dans le rush

| t≈ | Écran |
|---|---|
| 0-3s | Accueil (« bonjour, soulayma ! »), tuiles du module Hygiène (Températures, Traçabilité, Plan de nettoyage, Production, Étiqueteuse, Documents, Checklist Hygiène, Contrôle à réception, Conformité) |
| 3-9s | Page **« Contrôle de conformité — hygiène cuisine »** : cartes « Zone à contrôler » (A - Cuisine Quotidien, B - Cuisine Hebdo), chacune avec Note (optionnel) et un encadré explicatif : *« Vous pouvez uploader l'image de la zone de cuisine ici : l'IA analyse l'hygiène et la conformité (propreté, rangement, équipements) et vous renvoie le résultat par notification. »* |
| 9-9,35s | Clic sur **« Prendre une photo »** (ou « Choisir un fichier ») dans la zone de dépôt |
| 9,35-22,5s | Sélection du fichier, aperçu de l'image uploadée (vignette + nom de fichier, coche verte) |
| 22,5-22,85s | Clic sur **« Envoyer pour analyse »** |
| 22,85-26s | Bandeau vert de succès : *« Image envoyée avec succès. L'analyse de conformité a été déclenchée automatiquement. »* |

Rush avec une deuxième boucle de démonstration (~26-35,7s, retour à la page vide) non
reprise dans le montage — un seul passage complet suffit à illustrer le flux.

**Aucune séquence Claude sur ce tuto.** L'action montrée (upload d'une photo → analyse IA
automatique → notification) n'a pas d'outil `mcp__FoodEatUp__*` équivalent : le candidat le
plus proche, `create_hygiene_checklist_validation`, est une soumission manuelle de réponses
clé/valeur à une checklist, pas un upload photo + analyse IA. Conformément à la règle du
pipeline (« si aucun outil MCP ne correspond, ne pas ajouter cette séquence — pas de prompt
inventé »), ni la vidéo ni la fiche Lovable n'ont de `claudePrompt`.

## Voix off (6 lignes)

| # | Texte | Segment |
|---|---|---|
| N0 | Contrôler l'hygiène d'une zone cuisine ? Prenez-la simplement en photo. | intro + A |
| N1 | Depuis Hygiène, ouvrez Contrôle de conformité et choisissez la zone à contrôler. | B |
| N2 | Ajoutez une note si besoin, puis importez ou prenez une photo de la zone. | C(clic)+D |
| N3 | Cliquez sur « Envoyer pour analyse ». | E(clic) |
| N4 | L'IA analyse la propreté, le rangement et les équipements, et vous envoie le résultat par notification. | F (bandeau succès) |
| N5 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | carte de fin (CTA) — **réutilisée telle quelle** |

## Statut build (2026-08-04)

Durée livrée : **28,00 s** (tuto plus court que la moyenne — contenu source volontairement
resserré : une seule action, pas de séquence Claude). Checklist de compatibilité passée :
H.264 High/yuv420p, AAC LC 48 kHz stéréo, faststart, 0 erreur de décodage, true peak
**-6,93 dBFS**.

## Fiche Lovable

- **slug** : `photo-ia-controle-nettoyage`
- **title** : Une photo, l'IA contrôle votre nettoyage (Module Hygiène)
- **moduleSlug** : `haccp`
- **subcategory** : Contrôle de conformité par photo (analyse IA)
- **whatItsFor** : Contrôler la conformité d'une zone de cuisine sans grille papier : une
  photo suffit, l'IA analyse la propreté, le rangement et les équipements et vous envoie le
  résultat par notification.
- **chefTip** : La Note (optionnel) est le bon endroit pour préciser le contexte du contrôle
  (« après nettoyage du soir », par exemple) — elle aide à interpréter le résultat de l'IA a
  posteriori, surtout si vous comparez plusieurs photos de la même zone dans le temps.
  L'analyse se déclenche automatiquement dès l'envoi : pas besoin de revenir sur l'écran,
  le résultat arrive par notification.
- **chefTipAvatar** : `michael-chef-mascot.jpg`
- **claudePrompt** : absent (pas d'outil MCP équivalent — voir plus haut)

## Statut

Vidéo montée et publiée à la demande de Michael (workflow complet demandé dans le même
message : montage, VO, publication Lovable, mise à jour du dépôt).
