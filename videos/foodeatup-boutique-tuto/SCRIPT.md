# Tutoriel — Monter sa boutique FoodEatUp

Module 1 « CONFIGURATION », dossier Drive `2 - monte votre boutique`.
Durée livrée : **36,7 s** — H.264 High/yuv420p, AAC 48 kHz stéréo, faststart.
Audio : **-16,9 LUFS**, true peak **-4,3 dBFS** (mesurés sur le MP4 final).

## Nouveau dans ce projet — avatar HeyGen avec voix intégrée

Le dossier fournissait `Script 2 - monte votre boutique_1080p.mp4` : un chef
(avatar HeyGen) qui parle à la caméra pendant 6,64 s, voix déjà incrustée dans le
fichier (piste AAC continue, aucun silence détecté). Consigne : ne pas superposer
une ligne ElevenLabs par-dessus.

Traitement retenu : la piste audio native du clip est **extraite telle quelle**
(`ffmpeg -vn` → `vo/N0.mp3`) et injectée dans le mix final exactement comme les
lignes ElevenLabs — même `loudnorm`, même `adelay`, mais ancrée strictement au
début de son propre segment vidéo. Aucune ligne N0 n'est générée par ElevenLabs :
le chef reste la seule voix de l'accroche, et les lignes N1+ ne démarrent qu'après
la fin de son intervention (poussées séquentiellement comme toutes les autres VO).

Le clip est en 1920×1080 (portrait studio) alors que le canevas du tuto est en
1920×828 (format écran). Traitement : fond flou agrandi (`split` + `scale/crop`
+ `boxblur`) et clip net redimensionné en « contain » par-dessus, centré — même
principe que les cartes intro/outro, mais **sans `zoompan`** : ce filtre gèle
l'image sur de la vraie vidéo (bug déjà rencontré), il ne sert qu'aux photos fixes.
Vitesse native conservée (pas de `setpts`) — on n'accélère pas la voix d'une personne.

## Voix off

| # | Texte | Durée | Placement |
|---|---|---:|---|
| N0 | *(voix native de l'avatar, non générée)* | 6,70 s | clip chef HeyGen |
| N1 | Depuis votre espace, cliquez sur Ajouter une boutique et glissez la photo de votre établissement. | 5,51 s | ouverture modal + upload photo |
| N2 | Renseignez le nom de votre boutique, son email et le nom de domaine souhaité. | 4,21 s | nom / email / domaine |
| N3 | Choisissez le pays et la ville de votre établissement. | 2,87 s | pays / ville |
| N4 | Complétez l'adresse, votre numéro de SIRET et votre téléphone, puis validez avec Ajouter. | 5,02 s | adresse / SIRET / tél. + clic Ajouter |
| N5 | Votre boutique est en ligne, prête à recevoir ses premières commandes ! | 3,53 s | retour espace, carte boutique visible |
| N6 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 4,91 s | carte de fin (CTA) |

## Découpage

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 1,7 s | CRÉER SA BOUTIQUE FOODEATUP (pas de VO, juste un repère visuel) |
| avatar | clip HeyGen | 6,64 s | chef, voix native (N0) |
| A1 | 0,30 → 6,00 | 3,20 s | modal « Ajout d'un boutique » vide |
| A2 | 6,00 → 6,55 | 0,90 s | **zoom-punch** sur Choisir un fichier (967, 353) |
| A3 | 7,00 → 9,00 | 1,60 s | photo uploadée |
| B | 9,00 → 24,00 | 5,00 s | nom / email / domaine |
| C | 24,00 → 33,50 | 4,00 s | pays / ville |
| D | 33,50 → 58,00 | 5,50 s | code postal / adresse / SIRET / téléphone |
| E | 58,00 → 58,60 | 1,00 s | **zoom-punch** sur Ajouter (1035, 735) |
| F | 59,00 → 63,48 | 3,00 s | retour espace, boutique créée |
| outro | carte | 6,9 s | CTA |

Vérifié à l'image : le clic sur Ajouter reste bien affiché jusqu'à 58,6 s ;
la page ne bascule sur « Bienvenue dans votre espace » qu'entre 58,5 et 59,0 s.

## Animations

Mêmes principes que `foodeatup-inscription-tuto` : Ken Burns sur les cartes fixes
uniquement, xfade (0,28 s) à chaque raccord, bandeaux d'étape glissants, encadré
orange pulsant sur chaque clic. Voir ce projet pour le détail des trois pièges de
compatibilité (yuv444p, 96 kHz, faststart) — corrigés d'office ici dès la première
passe.

## Reste à faire

Rien dans ce dossier n'est resté inutilisé.
