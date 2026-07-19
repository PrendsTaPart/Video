# Boucle StockVisionAI — 60 s (voix off)

Vidéo narrée illustrant la boucle de gestion StockVisionAI dans FoodEatUp :
carte → courses → livraisons → production → stock, sans ressaisie.
1920×1080, voix off FR (ElevenLabs Adam, posé) + musique légère, sous-titres incrustés.

## Livrables
- `output/boucle-stockvision.mp4` (~4,7 Mo)
- `output/boucle-stockvision-poster.jpg`

## Méthode
`boucle.html` : timeline 60 s en HTML/CSS (diagramme de la boucle animé, 5 panneaux
recréés, Ken Burns sur `assets/screen-stocks-laptop.png`, cartons « 1 boucle »/« 0 ressaisie »,
sous-titres). `render(t)` déterministe → 1800 frames à 30 fps (Playwright/Chromium) →
`build_final.py` assemble + place la VO (6 blocs) + BGM −24 dB.
```bash
./build.sh   # VO + capture + assemblage (nécessite ELEVENLABS_API_KEY)
```
