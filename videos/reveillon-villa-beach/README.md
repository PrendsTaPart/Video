# Réveillon du Nouvel An — Domaine Villa Beach (Reels / TikTok / Stories)

Teaser vertical **1080 × 1920, 30 i/s, 54 s** + 5 Reels/TikTok du plan de campagne, monté avec HyperFrames + GSAP (pipeline du dépôt).
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

## Reels / TikTok — plan de campagne Excel (onglet « TikTok Reels »)

Édition confirmée : **31 décembre 2026 → 1er janvier 2027**. Timelines générées par
`scripts/reels-data.py` → `data/reels/*.json`, rendus par `bash scripts/render-reels.sh`.

| Reel | Fichier | Durée | Contenu |
|---|---|---|---|
| 1 Grand lancement | `renders/reels/reel-01-lancement_9x16_version-de-travail.mp4` | 25,6 s | 2027 approche… → domaine → 4 salles → DJ/foule → 3-2-1 → jusqu'à 05 h → carton |
| 2 4 univers | `renders/reels/reel-02-quatre-univers_9x16_version-de-travail.mp4` | 20 s | Team Généraliste / Latino / 80-90-2000 / Caraïbéenne ? (musique propre à chaque salle) → carton |
| 3 Dîner de fête | `renders/reels/reel-03-diner_9x16_version-de-travail.mp4` | 22 s | table dressée → tartare → plats → bûches → 120 € / 180 € / dès 19 h → carton |
| 4 Expérience VIP | `renders/reels/reel-04-vip_9x16_version-de-travail.mp4` | 19 s | packs 200 / 280 / 500 / 1 200 € avec inclusions → carton |
| 5 Countdown minuit | `renders/reels/reel-05-countdown_9x16_version-de-travail.mp4` | 21 s | 23:59 → Prêts ? → 10…1 → Happy New Year 2027 ! → carton |

Carton final commun (6 s) : monogramme, 31 décembre 2026, préventes conseillées, adresse,
**01 84 60 20 46**. Pas d'URL ni de QR tant que le site réveillon n'est pas publié
(renseigner `url` dans `END()` de `scripts/reels-data.py` le moment venu).
Photos : uniquement les photos réelles fournies (`assets/photos/`), aucune image IA.
Les photos de plats ne sont pas légendées comme des plats du menu, sauf le tartare (entrée du menu).
Le service bouteilles/tables VIP n'a pas de photo dédiée : le Reel 4 utilise bar, flamme,
plateau de cocktails et bouteille au seau.

## Stories Instagram — plan de campagne Excel (onglet « Stories Instagram »)

10 stories 1080 × 1920, 7 à 8 s chacune, musique seule (pas de voix off : les stories se
regardent souvent sans le son). Pied de page constant : monogramme · 31.12.2026 · 01 84 60 20 46.
Timelines : `scripts/stories-data.py` → `data/stories/*.json` ; rendu : `bash scripts/render-stories.sh`.
Fichiers : `renders/stories/story-NN-*_9x16_version-de-travail.mp4`.

| Story | Sticker à ajouter dans l'app Instagram |
|---|---|
| 01 Teaser — « Une nuit exceptionnelle se prépare… » | Compte à rebours (31/12/2026 19:00) |
| 02 Annonce — Le plus grand réveillon du Nouvel An · 31.12.2026 | Lien (après publication du site) ou appel |
| 03 4 salles — « Quelle sera la vôtre ? » | Sondage Généraliste / Latino / 80-2000 / Caraïbes |
| 04 Dîner — 120 € / 180 € / dès 19 h | Réserver le dîner |
| 05 VIP — Packs à partir de 200 € | Appel / réservation |
| 06 Compte à rebours — 10…1 → 2027 ! | Partager / taguer |
| 07 Clubbing — 20 / 30 / 40 / 100 € | Réserver |
| 08 Anniversaire — né en décembre, 1 bouteille offerte pour 5 entrées | Partager à un ami |
| 09 Dress code — Chic & élégant | Question « Ta tenue du 31 ? » |
| 10 Dernier CTA — Réservez votre soirée + téléphone | Lien de prévente / appel |

Les stickers se posent à la publication, dans la zone libre centrale (≈ 1080–1400 px).

## Points à valider avant diffusion

1. **Voix off — manquante** (Reels 1, 3, 4 et teaser ; Reel 2 optionnelle, Reel 5 sans voix).
   ElevenLabs a refusé la génération (facture d'abonnement impayée). Textes prêts dans
   `voiceover.lines` de chaque JSON. Déposer `assets/voice/<reel>.wav` puis relancer
   `FINAL=1 bash scripts/render-reels.sh <reel>` : le mix baisse la musique sous la voix.
   Coût estimé ElevenLabs : ~600 crédits par voix off, ~900 par musique — à valider avant génération.
2. **Musique — placeholder** : composition originale générée par `scripts/music.py` (aucun droit
   tiers), à remplacer par une musique sous licence promotionnelle.
3. **Lien de réservation** : à ajouter à la publication du site.
4. **Tarifs** (site + Excel, identiques) : dîners 120 / 180 €, clubbing dès 20 €, packs 200 / 280 / 500 / 1 200 €.

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
