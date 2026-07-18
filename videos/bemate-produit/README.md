# BeMaté — animation produit + avatar client

Client : **BeMaté** (energy drink au maté, 2 parfums — Mango Peach / Pomegranate Raspberry).

## Livrables

### 1. Animation produit (image → vidéo)
- `renders/bemate-anim-9x16-1080x1920.mp4` — **livrable final**, vertical 9:16, 8 s, sans audio.
  Les 2 canettes au centre, légère rotation ~15° qui révèle chaque face, condensation sur le
  métal, arrière-plan flou avec mangue+pêche (côté Mango Peach) et grenade+framboises en miroir
  (côté Pomegranate Raspberry). Fin sur les 2 canettes nettes et immobiles. Fond blanc, aucun
  texte incrusté (à ajouter au montage).
- `renders/bemate-anim-natif-768x1168.mp4` — sortie native du modèle (cadrage plus serré 2:3),
  avant recadrage 9:16.

**Pipeline :** Higgsfield `generate_video`, modèle **grok_video_v15** (image-to-video,
start_image = visuel produit), 720p, `generate_audio` off. Le modèle a rendu en 2:3 ; recadrage
en 9:16 par padding blanc (#FDFDFD, couleur de fond échantillonnée) via ffmpeg.

### 2. Avatar 3D « client type »
- `avatars/avatar-cliente-A.png` / `avatar-cliente-B.png` — 2 variantes d'une consommatrice type
  (jeune adulte, profil bien-être/sportif) qui présente la canette Mango Peach. Style 3D Pixar,
  fond off-white, format 9:16.

**Pipeline :** Higgsfield `generate_image`, modèle **nano_banana_pro** (nano_banana_2), image
produit passée en référence pour la fidélité de la canette.

## Source
- `source/bemate-2cans-source.png` — visuel produit fourni par le client (2 canettes, fond blanc).

## À itérer si besoin
- Choix de l'avatar (A/B), autre profil (homme, autre tranche d'âge, autre style).
- Version avatar avec la canette Pomegranate Raspberry.
- Animer l'avatar (mouvement / parole) via un modèle image-to-video.
- Version audio (les modèles Pro type Seedance/Kling nécessitent un upgrade de plan Higgsfield).
