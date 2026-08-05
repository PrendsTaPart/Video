# Tutoriel — Synchroniser la Charte graphique Iris

Module `marketing-fidelite` (catégorie « Marketing, Fidélité & Iris »), item **#22** du
catalogue 157 tutoriels (`videos/CATALOGUE-157-TUTORIELS.md`, ligne 118 : « Synchroniser la
**Charte** graphique Iris »).

Durée livrée : **36,92 s** — H.264 High/yuv420p, AAC 48 kHz stéréo, faststart.
Audio : true peak **-7,24 dBFS**. Sans avatar HeyGen. **Sans séquence « cas d'usage + prompt
Claude »** : aucun outil `mcp__Foodeatup__*` n'expose le pairage marque/Iris (uniquement des
outils métier — dishes, employés, HACCP, réservations, etc.), donc pas de prompt fabriqué,
conformément à la règle du repo (`FOODEATUP-TUTORIELS-WORKFLOW.md`, section « Séquence de
fin »).

## Rush

`assets/screen.mp4` (1920×828, 49,26 s, audio quasi silencieux -91 dB → pas de voix native) :
page **Intégrations** de FoodEatUp, carte « Iris — Marque & Charte ». Déroulé :
1. Champ « ID de la marque CMS » (vide = marque du compte), bouton **Appairer la marque**.
2. Clic (~t=33-34s) → état **Synchronisation...** (t≈37-40s).
3. Résultat (dès t≈41s) : marque **Braindcode** liée, « Charte synchronisée », palette de
   couleurs + police (Trebuchet MS) + tous les comptes sociaux connectés (Facebook, LinkedIn,
   Instagram, TikTok) + 728 assets de marque, boutons Resynchroniser / Désappairer.

La colonne de gauche (« RapidoCMS — Réseaux sociaux », jetons MCP, journal d'appels) est hors
sujet pour ce tutoriel — masquée par un crop fixe sur la colonne de droite (`RIGHT_CROP`,
`crop=956:828:964:0` puis `scale=1920:828`) sur tous les segments sauf le zoom-punch du clic.

## Voix off (7 lignes, voix Adam FR `TGAegA0zNRi8I6nUdq3i`)

Script validé par l'utilisateur avant génération.

| # | Texte | Durée | Ancrage |
|---|---|---:|---|
| N0 | Synchroniser la charte graphique de votre restaurant avec Iris ? Ça prend quinze secondes. | 4,73 s | carte d'intro |
| N1 | Rendez-vous dans Intégrations, sur la carte Iris — Marque et Charte. | 3,94 s | vue d'ensemble (seg A) |
| N2 | Cliquez sur Appairer la marque pour lancer la synchronisation. | 2,93 s | clic — zoom-punch (seg B) |
| N3 | Iris récupère aussitôt vos couleurs, votre police et votre logo depuis RapidoCMS. | 4,96 s | résultat — couleurs/police (seg D) |
| N4 | Vos comptes sociaux connectés — Facebook, Instagram, LinkedIn, TikTok — sont listés au même endroit. | 6,30 s | résultat — comptes sociaux (seg E) |
| N5 | Résultat : chaque contenu généré par Iris respecte automatiquement votre identité de marque, sans ressaisie. | 6,16 s | résultat — bénéfice (seg F) |
| N6 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 4,86 s | carte de fin (CTA, réutilisée telle quelle — même hash que `foodeatup-tva-tuto`/`foodeatup-mcp-tuto`) |

## Découpage

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 5,33 s | SYNCHRO DESIGN & CHARTE (image fournie par Michael) |
| A | 0,00 → 2,50 | 4,30 s | Vue d'ensemble carte Iris — Marque & Charte |
| B | 32,00 → 33,50 | 3,20 s | **zoom-punch** sur « Appairer la marque » (1133, 339), taille (279, 61) |
| C | 37,00 → 39,00 | 1,30 s | État « Synchronisation... » (beat de transition, pas de VO dédiée) |
| D | 41,00 → 42,50 | 5,26 s | Résultat — palette de couleurs + police Trebuchet MS |
| E | 44,00 → 45,50 | 6,60 s | Résultat — comptes sociaux connectés |
| F | 46,00 → 49,20 | 6,46 s (étendu à 6,51 s) | Résultat — 728 assets de marque, boutons Resynchroniser/Désappairer |
| outro | carte | 6,25 s | CTA (carte fournie par Michael, identique à celle déjà utilisée sur la série) |

Coordonnée du bouton mesurée par extraction de frames plein-format (1920×828) autour du clic
et détection de la bbox bleue par seuillage couleur (PIL) : bbox `(994,309)-(1273,370)`,
centre `(1133,339)`.

## Pièges rencontrés sur cette vidéo

- **`drawtext` absent du binaire ffmpeg fourni par `imageio_ffmpeg` (build statique
  johnvansickle 7.0.2)** — la liste `ffmpeg -filters` ne l'expose pas malgré
  `--enable-libfreetype` dans la configuration. Contournement : `apt-get install ffmpeg`
  (après un `apt-get update` — le premier essai avait échoué sur des paquets `libva2`/
  `libcaca0` 404, résolu par un simple retry) a fourni le vrai ffmpeg 6.1.1-3ubuntu5 système,
  avec `drawtext` disponible. C'est exactement la version 6.1.1 documentée dans
  `FOODEATUP-TUTORIELS-WORKFLOW.md` (bugs `drawbox`/`t`), donc le `banner()` déjà écrit avec
  le contournement documenté (un seul clamp de glissement, pas de slide-out animé) fonctionne
  sans modification.
- **`ffprobe` absent du binaire `imageio_ffmpeg`** (seul `ffmpeg` est empaqueté) — contourné
  temporairement par un shim Python (`/usr/local/bin/ffprobe`) le temps de récupérer le vrai
  binaire via `apt-get install ffmpeg`, qui l'installe aussi.
- Pas de scroll dans la carte résultat contrairement à l'hypothèse initiale (vérifiée sur les
  captures) : c'est le même cadrage du début à la fin du rush après le clic, seul le curseur
  se déplace. D/E/F utilisent donc le même `RIGHT_CROP` fixe (pas de zoom-punch), juste des
  fenêtres source différentes du même plan large.

## Statut publication

**Script validé par l'utilisateur le 2026-08-05.** Vidéo montée, vignette générée
(`out/thumbnail-youtube.jpg`, 1280×720, recadrage neutre depuis `assets/intro.jpg`).
Conformément à la règle du repo (STOP obligatoire), **livrée pour validation avant toute
publication** — pas d'upload RapidoCMS/LinkedIn, pas de mise à jour Lovable tant que
l'utilisateur n'a pas donné son accord sur le rendu final.
