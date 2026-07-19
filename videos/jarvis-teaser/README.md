# Jarvis Teaser — boucle 15 s

Teaser en boucle de la conversation Jarvis (commis vocal FoodEatUp).
1920×1080, **sans son**, 15 s, boucle parfaite (dernière frame = première, vérifiée au pixel).

## Livrables
- `output/jarvis-teaser.mp4` (≈201 Ko, H.264 crf 28, faststart)
- `output/jarvis-teaser-poster.jpg` (frame de l'étape 3)

## Méthode
`teaser.html` (page autonome, fond #0F1A23, typo Poppins locale en @font-face —
substitut arrondi à Baloo 2/Nunito non installées) → `capture.cjs` capture 450 frames
à 30 fps via Playwright/Chromium (`render(t)` déterministe) → ffmpeg assemble le MP4.

```bash
GROOT=$(npm root -g) node capture.cjs
ffmpeg -y -framerate 30 -i work/frames/f%04d.png -c:v libx264 -preset slow -crf 28 \
  -pix_fmt yuv420p -movflags +faststart -an output/jarvis-teaser.mp4
```

## Timeline (15 s)
1. Bulle Vous « Jarvis, sors 2 kg de tomates » (0–2 s)
2. Onde vocale bleue (2–4 s)
3. Bulle Jarvis « Je retire 2 kg de tomates du stock. Je confirme ? » (4–7 s)
4. Bulle Vous « Vas-y » (7–8,5 s)
5. Badge vert ✓ « Stock mis à jour · tracé dans le journal » (8,5–11,5 s)
6. Fondu → logo « Jarvis by FoodEatUp » (11,5–13,5 s), fondu retour début (13,5–15 s)
