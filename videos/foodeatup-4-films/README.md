# FoodEatUp — 10 films montés à partir de la bibliothèque Higgsfield

Session du 2026-09-07. **Règle posée par Michael : uniquement des plans de la bibliothèque
Higgsfield.** Aucun screencast du logiciel, aucun plan du film héros, aucun avatar HeyGen
dans les livrables. La bibliothèque complète a été relevée (532 plans), téléchargée et
analysée ; s'y ajoutent deux musiques originales et 34 voix off ElevenLabs.

## Livrables (`out/`)

| Film | Fichier | Durée | Format | Voix |
|---|---|---|---|---|
| Clip « Une journée. Une app. » | `foodeatup-clip.mp4` (+ `-16x9`) | 62 s | 1080×1920 | Paul K (4 lignes) |
| Présentation « Le même restaurant » | `foodeatup-presentation.mp4` (+ `-16x9`) | ~90 s | 1080×1920 | Anaïs (narratrice du film héros) |
| Commercial « Le contrôleur » | `foodeatup-commercial.mp4` (+ `-16x9`) | ~36 s | 1080×1920 | Paul K |
| Démo « Un tour du restaurant » | `foodeatup-demo.mp4` | ~1 min 45 | 1920×1080 | Enrick (tutoriel) |
| Short « Le contrôle » (HACCP) | `foodeatup-short-haccp.mp4` (+ `-16x9`) | ~25 s | 1080×1920 | Paul K |
| Short « L'inventaire » (stock) | `foodeatup-short-stock.mp4` (+ `-16x9`) | ~25 s | 1080×1920 | Paul K |
| Short « Le planning » (équipe) | `foodeatup-short-equipe.mp4` (+ `-16x9`) | ~26 s | 1080×1920 | Paul K |
| Short « L'addition » (compta) | `foodeatup-short-compta.mp4` (+ `-16x9`) | ~25 s | 1080×1920 | Paul K |
| Short « La double réservation » | `foodeatup-short-reservations.mp4` (+ `-16x9`) | ~25 s | 1080×1920 | Paul K |
| Short « L'avis du soir » | `foodeatup-short-avis.mp4` (+ `-16x9`) | ~26 s | 1080×1920 | Paul K |

Les versions `-16x9` posent le 9:16 sur son propre fond flouté (LinkedIn, site, YouTube).

## Matière

- **Higgsfield** : **532 plans** relevés via l'API (6 pages d'historique, jusqu'à `next_cursor`
  nul), tous téléchargés dans `assets/higgsfield/` (lien symbolique vers le cache de session,
  non versionné) ; catalogue + prompts + analyse dans `assets/higgsfield-catalogue.json` et
  `HIGGSFIELD-BIBLIOTHEQUE.md`. Aucun plan n'a été régénéré.
- **Musique** (ElevenLabs Music v2, instrumentales originales, `assets/music/`) :
  `musique-clip-123bpm.mp3` (62 s, electro-pop french touch, break au milieu) et
  `musique-underscore-99bpm.mp3` (2 min, piano/guitare/cordes sous voix), plus une variante `-alt` de chaque.
- **Voix off** (ElevenLabs `eleven_multilingual_v2`, `assets/vo/`) : scripts intégraux dans
  `scripts/VOIX-OFF.md`. Codes : C1-C4 clip, P1-P6 présentation, A1-A4 commercial (A3 = C3), D1-D9 démo.
  Flux ElevenLabs : https://elevenlabs.io/app/flows/P9XkZvN9YnnpIBmR2EF5
- **Pas de screencast, pas de HeyGen** : la première version de la démo et de la présentation
  utilisait les captures d'écran des tutoriels et l'avatar HeyGen existant ; elles ont été
  remontées en plans Higgsfield seuls, sur consigne. La démo devient « un tour du restaurant » :
  la voix off nomme les modules, l'image montre la scène de restaurant correspondante, en
  privilégiant les versions 16:9 natives de la bibliothèque.

## Refaire un rendu

```bash
cd videos/foodeatup-4-films
python3 build.py clip            # ou presentation | commercial | demo | all
python3 shorts.py                # les six shorts ; ou shorts.py haccp stock ...
REMIX=1 python3 build.py clip    # ne refait que le mixage audio
```

`build.py` = moteur (découpe, mise à l'échelle, enchaînement, cartons Pillow, mixage avec
ducking sous la voix, loudnorm −14 LUFS). `films.py` = les quatre films longs et `shorts.py` les six
shorts, plan par plan, avec les timecodes d'entrée dans chaque source. Le ffmpeg utilisé est le binaire statique
d'`imageio-ffmpeg` (pas de `drawtext`, d'où les cartons PNG).

## À trancher avant diffusion

- L'URL affichée est `foodeatup.fr` (comme dans les voix off précédentes) ; l'app vit sur
  `foodeatup.com`. Modifier `url=` dans `end_card` si besoin, puis `REMIX` ne suffit pas :
  relancer le film.
- La durée d'essai n'est pas prononcée (7 jours dans le produit, 14 dans une ancienne VO).
- Les plans Higgsfield contiennent des dialogues lip-sync ; ils sont mixés très bas sous la
  musique et la voix. Vérifier à l'écoute qu'aucune réplique ne ressort.
