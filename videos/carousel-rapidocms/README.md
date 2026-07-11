# Carousel RapidoCMS — Vidéo de présentation

Vidéo verticale (1080×1920, ~52 s) qui **présente le carrousel RapidoCMS**
« Une bibliothèque de posts, générée et 100 % modifiable » : on feuillette les
7 slides du carrousel, avec voix off, sous-titres incrustés, transitions *swipe*,
compteur `N/7` et pastilles de progression type Instagram.

## Livrable
- `deliverable/carousel-rapidocms.mp4`

## Sources & analyse
Le carrousel source (7 slides, PDF fourni) a été analysé et rebâti en assets :

| # | Slide | Message |
|---|-------|---------|
| 1 | Cover | Bibliothèque de posts, générée + 100 % modifiable (3 mockups Instagram) |
| 2 | Le problème | Créer du contenu, c'est chronophage |
| 3 | La solution RapidoCMS | L'IA génère et centralise vos posts (dashboards) |
| 4 | 100 % personnalisable | Texte, visuel, ton — contrôle total |
| 5 | Gain de temps réel | Piochez, ajustez en 2 clics, publiez |
| 6 | Toujours à jour | Bibliothèque qui s'enrichit en continu |
| 7 | CTA | Essayez RapidoCMS gratuitement — cms.rapidosoftware.com |

## Fichiers
- `SCRIPT.md` — script + voix off (8 segments)
- `STORYBOARD.md` — storyboard plan par plan
- `assets/slides/` — les 7 slides du carrousel (rendus haute résolution)
- `assets/logo/`, `assets/fonts/` — logo RapidoCMS + Poppins
- `audio/` — voix off ElevenLabs (Adam FR) `s0…s7.mp3` + `bgm.mp3`
- `frames/` — les 8 frames composées (intro + 7 slides)
- `build_frames.py` — compositeur PIL des frames
- `assemble.py` — montage ffmpeg (clips + xfade swipe + VO + BGM + loudnorm)

## Reproduire
```bash
python3 build_frames.py     # (re)génère frames/f0…f7.png
python3 assemble.py         # -> deliverable/carousel-rapidocms.mp4
```

## Specs
- Voix off : ElevenLabs Adam `TGAegA0zNRi8I6nUdq3i`, `eleven_multilingual_v2`, FR
- Transitions : `xfade=slideleft` 0,45 s (effet feuilletage)
- Audio : VO alignée sur la timeline xfade + BGM −18 dB en boucle, `loudnorm I=-14`
- Palette : accent `#29A9F2`, texte `#1B2A41`, fond blanc
