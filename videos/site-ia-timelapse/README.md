# Site IA Timelapse — boucle 20 s

Simulation accélérée de la génération d'un site de restaurant par l'IA (FoodEatUp).
1920×1080, **muet**, 20 s, boucle parfaite (dernière frame = première, vérifiée au pixel), ≤ 8 Mo.

## Livrables
- `output/site-ia-timelapse.mp4` (~674 Ko, H.264 crf 28, faststart, sans son)
- `output/site-ia-timelapse-poster.jpg` (frame de l'étape 3)

## Timeline
1. (0-4 s) Chat IA : « Décrivez votre restaurant… » → frappe « Pizzeria napolitaine à Lyon, four à bois »
2. (4-8 s) 3 propositions de design en cards (palette chaude + bleu FoodEatUp), sélection de la centrale (anneau bleu + ✓)
3. (8-14 s) Zoom + construction des sections une à une (hero, carte, horaires, bouton Commander)
4. (14-18 s) Barre d'URL qui tape « www.lanapoletana.fr » + cadenas SSL ✓
5. (18-20 s) Badge « En ligne en 10 minutes » + logo FoodEatUp, fondu retour début

## Méthode
`site.html` (page autonome, tout en HTML/CSS, typo Poppins locale) →
`capture.cjs` capture 600 frames à 30 fps via Playwright/Chromium (`render(t)` déterministe → boucle exacte) →
ffmpeg assemble le MP4.
```bash
GROOT=$(npm root -g) FRAMES=600 node capture.cjs
ffmpeg -y -framerate 30 -i work/frames/f%04d.png -c:v libx264 -preset slow -crf 28 \
  -pix_fmt yuv420p -movflags +faststart -an output/site-ia-timelapse.mp4
```
