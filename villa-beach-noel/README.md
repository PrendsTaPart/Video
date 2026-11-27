# Villa Beach · Noël le 23 décembre 2026 — campagne vidéo et Instagram

Campagne du réveillon de Noël du **mercredi 23 décembre 2026** au Domaine Villa Beach (Lisses).
Fil conducteur : *« Vous ne pouvez pas fêter Noël le 24 ? Invitez vos proches le 23. »*

> ✅ **VERSION FINALE sans voix off** (validée par le client le 27/11/2026, faute de crédits ElevenLabs) : musique seule, textes et sous-titres incrustés.
> Une version avec voix reste possible plus tard : déposer `audio/vo/vo01…vo09.mp3` et relancer le rendu.

## Livrables

| Fichier | Contenu |
|---|---|
| `renders/villa-beach-noel-23-decembre.mp4` | Film principal 9:16, 1080×1920, 30 fps, 55 s |
| `renders/*.srt` | Sous-titres de chaque vidéo (texte intégral de la voix off) |
| `renders/reels/reel-1…5.mp4` | 5 Reels courts (15 à 20 s) : accroche, dîner, enfants, ambiance, émotion |
| `posts/post-01…10.png` | 10 publications Instagram 4:5 (1080×1350) |
| `posts/legendes-instagram.md` | Légendes et hashtags des 10 posts et des 5 Reels |
| `audio/music/music.mp3` | Musique de Noël originale (synthèse de mélodies du domaine public) |
| `audio/vo/` | Emplacement des voix ElevenLabs `vo01.mp3` à `vo09.mp3` (vide pour l'instant) |

## Sources éditables

- `composition/timelines.js` : textes, voix off et minutage du film et des 5 Reels (scènes en secondes)
- `composition/index.html` : mise en page et animations (charte du site Lovable : Cormorant Garamond + Manrope, bordeaux, sapin et or)
- `composition/posts.html` : les 10 publications
- `composition/img/` : logo et photos du domaine récupérés depuis le projet Lovable (recadrés)
- `scripts/render.mjs` : rendu (Playwright + FFmpeg), mixage voix et musique avec ducking, normalisation à −14 LUFS, export SRT
- `scripts/posts.mjs` : export des posts
- `scripts/music.py` : génération de la musique

```bash
export NODE_PATH=/opt/node22/lib/node_modules   # Playwright global
node scripts/render.mjs --tl main --out renders/villa-beach-noel-23-decembre.mp4          # version finale (sans --wip)
for i in 1 2 3 4 5; do node scripts/render.mjs --tl reel$i --out renders/reels/reel-$i.mp4; done
node scripts/posts.mjs
python3 scripts/music.py audio/music/music.wav && ffmpeg -y -i audio/music/music.wav -b:a 256k audio/music/music.mp3
```
`--wip` ajoute le bandeau « version de travail ». `--stills 2,10,20` produit des captures de contrôle.

## Points ouverts

1. **Voix off (optionnelle) : ElevenLabs sans crédits.** Les 9 voix ont été refusées avec « Your subscription has a failed or incomplete payment », et la musique avec « Insufficient funds ». Une fois la facture réglée :
   - générer les 9 répliques (voix **Atma**, `vq479zipNPD44hpCdbIh`, modèle `eleven_v4`) avec le texte de `audio/vo/script-voix-off.md`, dans le flow ElevenLabs « Villa Beach – Noël 23 décembre 2026 » ;
   - les enregistrer sous `audio/vo/vo01.mp3` … `vo09.mp3` ;
   - relancer les commandes de rendu. Le script mesure les vraies durées, recale les sous-titres et signale tout chevauchement.
2. **Lien de réservation non vérifié.** Le projet Lovable « Villa Beach NYE Gathering » n'est **pas publié**. Son adresse `id-preview` est privée (401), on ne peut donc pas renvoyer vers une page de réservation vérifiée. La vidéo et les posts n'affichent **ni URL ni QR code**, seulement le téléphone. À fournir : l'URL publiée de la page Noël (et une URL courte), à ajouter ensuite à l'écran final.
3. **Points du site à faire valider** :
   - la description du projet Lovable parle de « quatre salles », alors que le code n'en présente que **2** (Généraliste / Caribbean Vibes) ; la vidéo en montre 2, comme demandé ;
   - le site présente une « Semaine spéciale Noël du 22 au 25 décembre » ; la campagne ne parle que du 23 ;
   - le compte à rebours du code pointe encore vers le 31/12 (`EVENT_TARGET`), sans impact sur la vidéo.

## Choix artistiques et conformité

- Toutes les photos sont de **vraies photos du domaine** tirées du site Lovable. Aucune image d'illustration n'est présentée comme une photo du domaine. La photo « danse-latino » a été écartée : c'est une capture Instagram avec le filigrane d'un tiers.
- La mention « L'abus d'alcool est dangereux pour la santé » (loi Évin) figure sur les écrans et posts qui parlent de champagne.
- Zones de sécurité Reels/TikTok respectées : contenu entre 230 et 1360 px de haut, sous-titres vers 1400 px, marge à droite.
- Écran final de 7,6 s dans le film (≥ 6 s dans chaque Reel), téléphone en très grand.
- Higgsfield n'est pas utilisé (règle du dépôt) : aucun plan vidéo généré.
