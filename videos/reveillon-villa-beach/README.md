# Réveillon du Nouvel An — Domaine Villa Beach (Reels / TikTok / Stories)

Teaser vertical **1080 × 1920, 30 i/s, 54 s**, monté avec HyperFrames + GSAP (pipeline du dépôt).
Source unique : `data/timeline.json` (scènes, textes à l'écran, voix off, sous-titres).

> ⚠️ **VERSION DE TRAVAIL — ne pas diffuser en l'état.** Le bandeau jaune en haut de l'image
> le rappelle ; il disparaît avec `npm run build:final`.

## Livrables

| Fichier | Contenu |
|---|---|
| `renders/reveillon-villa-beach_9x16_version-de-travail.mp4` | Aperçu H.264/AAC, 54 s, musique de travail, **sans voix off** |
| `renders/sous-titres.srt` | Sous-titres (aussi incrustés dans la vidéo) |
| `index.html` + `assets/style.css` | Composition éditable (générée par `scripts/build.mjs`) |
| `scripts/music.py` | Musique de travail originale (synthèse par code, aucun droit tiers) |
| `scripts/mix.sh` | Mixage voix + musique (sidechain, -14 LUFS) et mux |

## Points à valider avant l'export diffusion

1. **Édition / année** — le site Lovable « Réveillon Villa Beach » annonce la nuit du
   **31 décembre 2026 au 1er janvier 2027** (titre « Nouvel An 2026 », programme « pour 2027 »,
   roadmap « Conserver la nuit du 31 décembre 2026 au 1er janvier 2027 »). Le brief parle du
   passage **2025 → 2026**. Aucune année n'est affichée à l'écran (accroche, minuit « Bonne année ! »).
2. **Lien / QR de réservation** — le site réveillon **n'est pas publié** : aucune URL vérifiée,
   donc ni URL ni QR code à l'écran. Le carton final affiche le téléphone du site
   (01 84 60 20 46) et l'adresse. Si une URL est publiée et vérifiée, la renseigner dans
   `scenes[s14-reservation].url` (elle s'affiche sous le téléphone).
3. **Tarifs** (lus dans `src/lib/offers.ts` du site, identiques au brief) : Dîner de fête 120 €/pers.,
   Dîner Champagne 180 €/pers., entrée clubbing dès 20 €. Restaurant dès 19 h, clubbing jusqu'à 05 h.
4. **Voix off — manquante.** ElevenLabs a refusé la génération le 24/11/2026 :
   « Your subscription has a failed or incomplete payment ». Régler la facture, puis générer :
   - voix **Simon - Voix Radio** (`mvhJVdVoTWVUtL4keT7W`), modèle `eleven_v4`, 1 prise ;
   - texte : `voiceover.lines` dans `data/timeline.json` (le texte du brief, avec « dix-neuf heures »,
     « vingt euros », « cinq heures » écrits en toutes lettres pour la prononciation) ;
   - flow ElevenLabs déjà créé : « Réveillon Villa Beach – voix off & musique ».
5. **Musique — placeholder.** ElevenLabs Music a échoué (« Insufficient funds »). La musique actuelle
   est une composition originale générée par `scripts/music.py` (droits : aucun tiers), suffisante
   pour valider le rythme, pas pour la diffusion. Remplacer `assets/music/musique-travail.wav` par une
   musique sous licence promotionnelle (ElevenLabs Music une fois le compte réglé) en gardant le
   découpage (dîner lounge 5-14 s, house 14-18, latino 18-22, disco 22-26, caribéen 26-30,
   montée 30-34,4, décompte 34,5 / 35,35 / 36,2, drop 37 s, outro 47-54).
6. **Images** — toutes réelles (site réveillon : « Intégrer les photos réelles » ; site Villa Beach :
   vidéo terrasse, pergola, monogramme VB). Aucune image IA. Manquent : table dressée du réveillon,
   service à table, cotillons/bulles réels (remplacés par des effets graphiques), photo propre à la
   salle Caraïbéenne (photo d'ambiance du club recadrée et étalonnée). Les deux photos de plats
   ne sont pas légendées comme les plats du menu ; le menu est cité à part (« Au menu : … »).

## Finaliser (une fois les points validés)

```bash
# 1. déposer la voix : assets/voice/voix-off.wav (54 s max, calée sur voiceover.lines.start)
#    et ajuster les temps de data/timeline.json → subtitles si la diction diffère
npm run build:final   # sans bandeau « version de travail »
npm run render        # → renders/video-muette.mp4
bash scripts/mix.sh renders/video-muette.mp4 renders/reveillon-villa-beach_9x16_final.mp4
npm run srt
```

Contrôles faits sur l'aperçu : 1080×1920, 30 i/s, 54,0 s ; 4 salles nommées et étalonnées
différemment (magenta/cyan, rouge/ambre, néon violet + grille rétro, vert/jaune) ; textes dans la
zone sûre (x 80–930, y 260–1480) ; carton final 47–54 s, téléphone lisible 6,4 s ; mix de travail
-15 LUFS intégré (sans voix).
