# Tutoriel — Pointer son service (pauses & photo), côté employé

Module Équipe, Planning & RH, item **15 "Pointer son Service (pauses & photo)"**
(`videos/CATALOGUE-157-TUTORIELS.md`). Slug Lovable : `pointer-son-service-cote-employe`.

## Historique du rush (important pour une future session)

Le premier envoi (`Gestion_des_pauses_pointage_entrée_et_sortie_et_Empreinte_photo_du_
pointage.mp4`, 41,52 s) était le même fichier Drive mal étiqueté déjà documenté sur
`creer-ses-roles-et-permissions` (Accueil/QR code/Rôles, pas le pointage). Une v1
carte-based avait été montée et publiée à partir de ça (voir git log) — voir plus bas.

**Michael a renvoyé le bon fichier** le même jour (23,88 s, même nom, taille différente :
7,07 Mo au lieu de 31 Mo). Vérifié image par image (`ffmpeg -ss t -frames:v 1` tous les
0,3 à 0,5 s) : c'est bien le flux "Pointage" côté employé — Entrée → Pause → Fin de pause
→ Sortie, chaque étape confirmée par une capture photo. **Cette version remplace la v1
carte-based.**

## Déroulé du rush (1920×828, 25 im/s, 23,88 s)

| t | Contenu |
|---|---|
| 0,00–1,85 | Dashboard employé "bonjour, alice !" — carte Shift "Pas encore pointé" |
| ~1,9 | Clic sur le badge "Pas encore pointé" (1598, 601) → ouvre la modale Pointage |
| 2,10–2,85 | Modale "Pointage", zone photo noire "Une photo sera prise au pointage", 3 boutons Entrée/Pause/Sortie (688/968/1248, y=672, ~275×60 chacun) |
| ~2,9 | Clic **Entrée** (688, 672) |
| 3,00–5,40 | Traitement en cours (photo + envoi) |
| 5,90–6,80 | Dashboard : badge "Au travail", ligne "Pointage d'entrée 17:51" |
| ~6,9 | Réouverture modale (même badge) |
| 7,00–7,90 | Ligne Entrée verte affichée, clic **Pause** (968, 672) |
| 8,00–9,90 | Traitement en cours (photo pause) |
| 11,00–11,90 | Dashboard : badge "En pause depuis 17:51", ligne "Pause déjeuner 17:51" (début seul) |
| ~11,9 | Réouverture modale |
| 12,00–13,00 | Lignes Entrée + Pause (début) affichées, clic **Fin pause** (968, 672, même bouton relabellisé) |
| 14,00–15,00 | Traitement en cours (photo fin de pause) |
| 16,00–16,90 | Dashboard : ligne "Pause déjeuner 17:51 - 17:51" (plage complète) |
| ~16,9 | Réouverture modale |
| 17,00–18,00 | Lignes Entrée + Pause affichées, clic **Sortie** (1248, 672, en rouge) |
| 18,00–19,90 | Traitement en cours (photo sortie) |
| 20,00–20,90 | Dashboard final : badge "Journée terminée", les 3 lignes remplies |

## Voix off (8 lignes, Adam FR `TGAegA0zNRi8I6nUdq3i`)

| # | Texte | Durée |
|---|---|---:|
| N0 | Pointer votre service dans FoodEatUp ? Entrée, pause, sortie : tout se fait en quelques secondes, avec une photo à chaque étape. | 7,71 s |
| N1 | Dès votre arrivée, un tap sur Pointage, une photo, et votre entrée est enregistrée à la seconde. | 5,51 s |
| N2 | Une pause déjeuner ? Le même geste : une photo, et l'heure de départ est pointée. | 4,68 s |
| N3 | De retour de pause, pointez à nouveau : FoodEatUp calcule automatiquement sa durée. | 4,55 s |
| N4 | En fin de service, un dernier pointage de sortie boucle votre journée. | 3,58 s |
| N5 | Chaque pointage est confirmé par une photo instantanée : impossible de pointer à la place d'un collègue absent. | 5,80 s |
| N6 | Vous pouvez aussi demander à Claude un résumé de vos heures ou de vos pauses de la semaine. | 4,83 s |
| N7 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 4,83 s |

N5/N6/N7 réutilisées telles quelles de la v1 carte-based (texte inchangé) — évite 3
aller-retours ElevenLabs inutiles.

## Découpage vidéo

Screen recording réel avec zoom-punch (crop fixe centré sur le bouton, jamais de
`zoompan` sur vidéo), `setpts` pour accélérer les "Traitement en cours" (~2× pour ne pas
faire traîner l'attente). Enchaîné : intro carte → dashboard/ouverture (badge) → Entrée
(clic + traitement) → dashboard entrée confirmée → Pause (clic + traitement) → dashboard
en pause → Fin pause (clic + traitement) → dashboard plage complète → Sortie (clic +
traitement) → dashboard journée terminée → graphique "photo anti-fraude" (déjà utilisé
en v1, toujours pertinent pour appuyer N5) → séquence "Utiliser avec Claude" (3 temps,
module partagé `_shared/claude_prompt_sequence.py`) → carte de fin CTA.

## Séquence "Utiliser avec Claude"

Pas d'outil MCP pour pointer soi-même (action employé self-service, comme
`se-connecter-cote-employe` / `creer-son-code-pin`), mais `list_attendances` couvre la
lecture de ses propres pointages/pauses. Prompt : "Fais-moi un résumé de mes heures et de
mes pauses pointées cette semaine pour [nom employé]." (même texte des deux côtés,
vidéo + fiche Lovable, cf. règle `FOODEATUP-TUTORIELS-WORKFLOW.md`).

## Statut

v2 construite sur le vrai rush, remplace la v1 carte-based (`out/
foodeatup-pointer-service-tuto-v1.mp4`, conservée dans l'historique git mais plus
référencée sur RapidoCMS/Lovable). Livrée directement sur demande explicite de Michael
("voici la vraie séquence vidéo tu peux remplacer").
