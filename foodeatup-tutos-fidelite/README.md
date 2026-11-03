# Tutoriels vidéo — application FoodEatUp Fidélité (tablette comptoir)

7 tutoriels (≈ 18 s, 1920×1080) montés avec HyperFrames 0.9.5 à partir des vrais écrans de l'application.
Voix : ElevenLabs Adam (`TGAegA0zNRi8I6nUdq3i`), modèle `eleven_v4`, une seule prise (≈ 0,06 $ par voix, 03/11/2026).

- `tutos.py` : titres, écrans, étapes, image du chef et texte de la voix.
- `generer.py` : construit un projet HyperFrames par tutoriel (`projets/`, non versionné). Galerie : variable `GALERIE`.
- `rendre.sh` : rend chaque projet puis ré-encode (`sortie/<cle>.mp4` + vignette `.jpg`).
- `ecrans/` : les écrans de l'application (WebP 1920×1200), rendus par le dépôt `PrendsTaPart/foodeatup-fid-lit`
  (`CAPTURES=1 CAPTURES_DPR=1.5 flutter test --update-goldens test/captures`), données de démonstration,
  aucun client réel, aucune image générée par une IA. Ils servent aussi aux vidéos de communication (Journal).
- `commun/` : GSAP 3.12.5 (licence GreenSock standard), Inter (OFL), logo officiel FoodEatUp.

Les vidéos sont publiées sur l'Académie (tutoriel.foodeatup.com, module « Marketing, Fidélité & Iris »,
section « Application tablette fidélité ») et dans l'application (Réglages gérant › Tutoriels vidéo).
