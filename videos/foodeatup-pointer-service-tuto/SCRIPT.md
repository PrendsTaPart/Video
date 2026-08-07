# Tutoriel — Pointer son service (pauses & photo), côté employé

Module Équipe, Planning & RH, item **15 "Pointer son Service (pauses & photo)"**
(`videos/CATALOGUE-157-TUTORIELS.md`). Le slot existe déjà sur Lovable en placeholder
"à venir" : slug `pointer-son-service-cote-employe`, `videoUrl: ""`, `durationSeconds: 0`.

## ⚠️ Constat sur le rush fourni (à relire avant de refaire cette vidéo)

Le fichier envoyé pour cette vidéo (`Gestion_des_pauses_pointage_entrée_et_sortie_et_
Empreinte_photo_du_pointage.mp4`, 41,52 s, 1920×828) a été vérifié image par image
(`ffmpeg -ss t -frames:v 1` toutes les 1-2 s, planche-contact incluse). **Il ne montre
pas l'écran de pointage (entrée/sortie/pause/photo)** : il montre en réalité, dans
l'ordre, **Accueil "mon espace"** (grille de modules selon le rôle, item 14) →
**QR code de pointage actif** (item 8, déjà couvert par `generer-qr-code-pointage`) →
**Rôles & Permissions, modale "Modifier le rôle"** (item 1, déjà couvert par
`creer-ses-roles-et-permissions`, qui a d'ailleurs été construite avec un `claudePrompts`
sur les pauses — voir plus bas).

C'est **exactement le même bug d'étiquetage Google Drive déjà documenté** dans
`videos/LOVABLE-FOODEATUP-DOCS.md` (tableau "Tutoriels publiés", ligne #17,
`creer-ses-roles-et-permissions`) : le fichier du dossier Drive 15 contient en réalité
l'enregistrement du dossier 1. Le problème n'a donc pas été corrigé côté Drive entre les
deux sessions — un nouvel envoi du même fichier mal étiqueté a été fait.

**Décision prise ici (pas de validation Michael obtenue avant, faute de rush exploitable
à lui soumettre en l'état)** : ne pas refaire un troisième tutoriel quasi identique à
partir du même écran Rôles/Permissions (déjà utilisé une fois). À la place :
- Utiliser la **vraie capture d'écran produit** déjà présente dans le dépôt,
  `studio-video/assets/brand/product-screenshots/pointage.png` — un vrai popup
  "Pointage" FoodEatUp montrant Pointage d'entrée / Pointage déjeuner (pause, avec
  heure de début-fin) / Pointage de sortie. C'est un asset réel, pas une invention.
  Zoom/Ken Burns successifs sur ses 3 lignes pour rythmer la vidéo malgré l'absence de
  screen recording.
- **Ne pas montrer d'écran de capture photo inventé** : aucun asset ne le documente.
  La confirmation par photo à chaque pointage est mentionnée **en voix off uniquement**
  (fait réel, déjà documenté comme mécanisme anti-fraude dans
  `videos/foodeatup-qrcode-pointage-tuto/SCRIPT.md` — "pointage fiable et anti-fraude" —
  et cohérent avec le titre "Empreinte photo du pointage" du dossier Drive), sans habillage
  d'interface fabriqué.
- Vidéo volontairement courte et construite sur cartes + un visuel réel (même traitement
  que `brancher-son-mcp-sur-claude` / `diffuser-son-qrcode`, tutoriels déjà publiés sans
  rush screen recording exploitable).

**À rattraper si/quand un vrai screen recording du flux employé (pointer entrée → pause →
sortie → capture photo) est fourni** : reprendre ce dossier avec un montage type
zoom-punch complet comme le reste de la série, remplacer ce montage carte-based.

## Voix off (7 lignes, Adam FR `TGAegA0zNRi8I6nUdq3i`)

| # | Texte |
|---|---|
| N0 | Pointer votre service dans FoodEatUp ? Entrée, pause, sortie : tout se passe en quelques secondes, directement depuis votre espace employé. |
| N1 | Dès votre arrivée, un seul geste enregistre votre pointage d'entrée, horodaté à la seconde. |
| N2 | Une pause déjeuner ? Pointez-la aussi : FoodEatUp calcule automatiquement sa durée. |
| N3 | En fin de service, un dernier pointage de sortie, et votre journée est bouclée. |
| N4 | Chaque pointage est confirmé par une photo instantanée : impossible de pointer à la place d'un collègue absent. |
| N5 | Vous pouvez aussi demander à Claude un résumé de vos heures ou de vos pauses de la semaine. |
| N6 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! |

(N6 réutilisée telle quelle d'un tuto à l'autre, cf. règle N6/N8 de
`FOODEATUP-TUTORIELS-WORKFLOW.md`.)

## Séquence "Utiliser avec Claude"

Pas d'outil MCP pour pointer soi-même (action employé self-service, comme
`se-connecter-cote-employe` / `creer-son-code-pin`) mais `list_attendances` couvre la
lecture de ses propres pointages/pauses — même outil que `retrouver-les-pointages-historique`
et le `claudePrompts` pauses de `creer-ses-roles-et-permissions`, réutilisé ici sous l'angle
employé (voir aussi `voir-son-planning-cote-employe`, même tolérance de chevauchement
documentée dans `LOVABLE-FOODEATUP-DOCS.md` quand l'angle diffère) :
prompt "Résumé de mes heures et pauses de la semaine".

## Statut

Montage carte-based construit malgré le rush inexploitable (voir constat ci-dessus).
**À livrer à Michael pour validation avant publication RapidoCMS/LinkedIn/Lovable**, comme
le veut la règle standing de `LOVABLE-FOODEATUP-DOCS.md` — d'autant plus ici vu l'écart
avec le rush attendu.
