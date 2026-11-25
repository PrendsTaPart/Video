# Réveillon du Nouvel An — Domaine Villa Beach (Reels / TikTok / Stories)

Teaser vertical **1080 × 1920, 30 i/s, 54 s** + 5 Reels/TikTok du plan de campagne, monté avec HyperFrames + GSAP (pipeline du dépôt).
Source unique : `data/timeline.json` (scènes, textes à l'écran, voix off, sous-titres).

> Versions finales des Reels et stories : `renders/reels/` et `renders/stories/` (suffixe `_final`).
> Le teaser 54 s (`renders/reveillon-villa-beach_9x16_version-de-travail.mp4`) reste une version de travail.

## Livrables

| Fichier | Contenu |
|---|---|
| `renders/reveillon-villa-beach_9x16_version-de-travail.mp4` | Aperçu H.264/AAC, 54 s, musique de travail, **sans voix off** |
| `renders/sous-titres.srt` | Sous-titres (aussi incrustés dans la vidéo) |
| `index.html` + `assets/style.css` | Composition éditable (générée par `scripts/build.mjs`) |
| `scripts/music.py` | Musique de travail originale (synthèse par code, aucun droit tiers) |
| `scripts/mix.sh` | Mixage voix + musique (sidechain, -14 LUFS) et mux |

## Versions finales (25/11/2026)

Sans bandeau, édition **jeudi 31 décembre 2026 → 2027**. Sans voix off (ElevenLabs bloqué) ;
musique originale générée par `scripts/music.py`.

- **Date toujours visible** : badge « Jeudi 31 décembre 2026 » en haut des Reels, pied de page
  « Jeudi 31 décembre 2026 · Réservations 01 84 60 20 46 » sur les stories, date encadrée sur
  chaque carton final.
- **Menu exclusif** : « Servi uniquement le 31 décembre », tampon « Exclusif · 31.12 uniquement »
  sur la carte du menu, mention « Menu exclusif · uniquement le 31.12 » sur le carton final.
- **Formats** : carton d'invitation qui se retourne, grille 2×2 des 4 salles, horloge 23:59,
  carte du menu tamponnée, décompte, texte animé mot à mot, transitions (balayage, zoom, flash doré,
  montée), grain pellicule.
- **Vidéos réelles** : `assets/video/` — travelling vers la pergola (site Villa Beach, 9:16) et
  panoramique jardin/pergola (site Villa Beach, 16:9 recadré en deux plans verticaux). Utilisées en
  ouverture, en plans de lieu et en fond animé de tous les cartons finaux.

### Reels / TikTok — `renders/reels/*_9x16_final.mp4`

| Reel | Durée | Déroulé |
|---|---|---|
| 01 Grand lancement | 25,6 s | invitation → « 2027 approche… » (vidéo) → grille 4 salles → DJs invités → blind test → jusqu'à 05 h → horloge 23:59 → 2027 ! → carton |
| 02 4 univers | 20,6 s | Team Généraliste / Latino / 80-90-2000 / Caraïbéenne ? → grille « Et vous, team quoi ? » → carton |
| 03 Dîner du réveillon | 24 s | vidéo → « Servi uniquement le 31 décembre » + tampon → tartare → carte du menu exclusif → 120 € / 180 € / dès 19 h → carton |
| 04 Expérience VIP | 19 s | vidéo → packs 200 / 280 / 500 / 1 200 € → carton |
| 05 Countdown minuit | 21 s | horloge 23:59 → Prêts ? → 10…1 → Happy New Year 2027 ! → carton |

### Stories Instagram — `renders/stories/*_9x16_final.mp4`

| Story | Sticker à poser dans l'app |
|---|---|
| 01 Teaser (vidéo) — Une nuit exceptionnelle se prépare… | Compte à rebours 31/12/2026 19:00 |
| 02 Annonce — invitation « Le plus grand réveillon du Nouvel An · 31.12.2026 » | Appel / lien |
| 03 4 salles — grille + « Quelle sera la vôtre ? » | Sondage |
| 04 Dîner — menu exclusif du 31.12, 120 € / 180 € | Réserver |
| 05 VIP — packs dès 200 € | Appel |
| 06 Compte à rebours — 23:59 → 10…1 → 2027 ! | Partager / taguer |
| 07 Clubbing — 20 / 30 / 40 / 100 € | Réserver |
| 08 Anniversaire — 1 bouteille offerte pour 5 entrées | Partager |
| 09 Dress code — Chic & élégant | Question |
| 10 Dernier CTA — carton sur fond vidéo | Appel / prévente |

Rendu : `bash scripts/render-reels.sh` et `bash scripts/render-stories.sh`
(`DRAFT=1` pour une version avec bandeau). Données : `scripts/reels-data.py`, `scripts/stories-data.py`.

### Plans vidéo manquants — prompts Higgsfield (à générer dans l'interface, règle du dépôt)

Aucun plan de soirée filmé n'existe dans le dépôt ni sur les sites. Plans d'ambiance à générer
(à présenter comme ambiance, pas comme images du domaine), 9:16, 4-5 s, sans texte ni logo :
1. « Close-up of champagne flutes clinking in slow motion, golden bokeh lights, black and gold New Year's Eve party, cinematic, shallow depth of field »
2. « Gold confetti and streamers falling in slow motion over a dancing crowd at midnight, club lights, festive, cinematic 9:16 »
3. « Waiter carrying a champagne bottle with a sparkler fountain through a dark VIP lounge, gold and black, cinematic tracking shot »
4. « Elegant plated foie gras starter being finished with tweezers, warm candlelight, fine dining, macro, slow motion »
Idéalement, remplacer par de vrais rushs filmés au domaine (soirées précédentes) : déposer les
fichiers dans `assets/video/` et les référencer dans les scripts de données.

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
