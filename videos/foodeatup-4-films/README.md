# FoodEatUp — 4 films (clip, présentation, commercial, démo)

Session du 2026-09-07. Tout est monté à partir de l'existant : les 150 plans de la
bibliothèque Higgsfield (analysés, jamais régénérés), les screencasts réels des tutoriels,
l'avatar HeyGen déjà produit, deux musiques originales et 22 voix off ElevenLabs.

## Livrables (`out/`)

| Film | Fichier | Durée | Format | Voix |
|---|---|---|---|---|
| Clip « Une journée. Une app. » | `foodeatup-clip.mp4` (+ `-16x9`) | 62 s | 1080×1920 | Paul K (4 lignes) |
| Présentation « Le même restaurant » | `foodeatup-presentation.mp4` (+ `-16x9`) | ~90 s | 1080×1920 | Anaïs (narratrice du film héros) |
| Commercial « Le contrôleur » | `foodeatup-commercial.mp4` (+ `-16x9`) | ~36 s | 1080×1920 | Paul K |
| Démo « Un tour du logiciel » | `foodeatup-demo.mp4` | ~1 min 45 | 1920×1080 | Enrick (tutoriel) |

Les versions `-16x9` posent le 9:16 sur son propre fond flouté (LinkedIn, site, YouTube).

## Matière

- **Higgsfield** : 150 plans relevés via l'API (2 pages), téléchargés dans `assets/higgsfield/`
  (lien symbolique vers le cache de session, non versionné), catalogue + prompts + analyse
  dans `assets/higgsfield-catalogue.json` et `HIGGSFIELD-BIBLIOTHEQUE.md`.
- **Musique** (ElevenLabs Music v2, instrumentales originales, `assets/music/`) :
  `musique-clip-123bpm.mp3` (62 s, electro-pop french touch, break au milieu) et
  `musique-underscore-99bpm.mp3` (2 min, piano/guitare/cordes sous voix), plus une variante `-alt` de chaque.
- **Voix off** (ElevenLabs `eleven_multilingual_v2`, `assets/vo/`) : scripts intégraux dans
  `scripts/VOIX-OFF.md`. Codes : C1-C4 clip, P1-P6 présentation, A1-A4 commercial (A3 = C3), D1-D9 démo.
  Flux ElevenLabs : https://elevenlabs.io/app/flows/P9XkZvN9YnnpIBmR2EF5
- **Screencasts** : `videos/foodeatup-*-tuto/assets/screen.mp4` (mcp, fiche-plat, reception-livraison,
  mouvements-stock, temperatures, tracabilite, haccp-export, planning-poste, qrcode-pointage,
  facture-ocr, boutique, jarvis, predibot).
- **HeyGen** : l'avatar chef FoodEatUp existant (`foodeatup-qrcode-tuto/assets/avatar.mp4`) ouvre la démo.
  Aucun nouveau rendu HeyGen n'était nécessaire (pas de clé API dans l'environnement de toute façon).

## Refaire un rendu

```bash
cd videos/foodeatup-4-films
python3 build.py clip            # ou presentation | commercial | demo | all
REMIX=1 python3 build.py clip    # ne refait que le mixage audio
```

`build.py` = moteur (découpe, mise à l'échelle, enchaînement, cartons Pillow, mixage avec
ducking sous la voix, loudnorm −14 LUFS). `films.py` = les quatre montages, plan par plan,
avec les timecodes d'entrée dans chaque source. Le ffmpeg utilisé est le binaire statique
d'`imageio-ffmpeg` (pas de `drawtext`, d'où les cartons PNG).

## À trancher avant diffusion

- L'URL affichée est `foodeatup.fr` (comme dans les voix off précédentes) ; l'app vit sur
  `foodeatup.com`. Modifier `url=` dans `end_card` si besoin, puis `REMIX` ne suffit pas :
  relancer le film.
- La durée d'essai n'est pas prononcée (7 jours dans le produit, 14 dans une ancienne VO).
- Les plans Higgsfield contiennent des dialogues lip-sync ; ils sont mixés très bas sous la
  musique et la voix. Vérifier à l'écoute qu'aucune réplique ne ressort.
