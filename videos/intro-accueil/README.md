# Intro cinématographique de l'accueil (HyperFrames, esprit 3D)

20 s, muette. Histoire : « Un soir. Un téléphone. » → l'écran s'allume → les projets (écrans réels) s'envolent du téléphone et forment un anneau en 3D → « 46 projets. 130+ vidéos. » → la caméra plonge dans le téléphone qui affiche l'accueil → l'accueil réel prend tout l'écran : le site s'affiche.

- `gen.py` génère `index.html` (1920x1080) et `mobile/index.html` (1080x1920). Après une refonte de l'accueil, recapturer `assets/accueil-desktop.jpg` et `assets/accueil-mobile.jpg` pour que la dernière image corresponde au site.
- Rendu : `npx hyperframes render -o intro-accueil-1920x1080.mp4` (et dans `mobile/`).
