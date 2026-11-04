# Tutoriels vidéo — application FoodEatUp KDS (tablette de cuisine)

14 tutoriels (≈ 20 s, 1920×1080), montés avec HyperFrames 0.9.5 à partir des vrais écrans de l'application.
La voix est celle d'Adam sur ElevenLabs (`TGAegA0zNRi8I6nUdq3i`), modèle `eleven_v4`, en une seule prise.

## Fichiers

- `plan.json` : la série validée, la chaîne de production et le calendrier des créneaux. `statut.csv` donne l'avancement.
- `tutos.py` : pour chaque tutoriel, le titre, les écrans, les étapes, l'image du chef et le texte de la voix.
- `outils/enregistrer.js` : pilote l'application avec Playwright et un faux curseur.
  - Lancement : `node enregistrer.js scenario.json dossier`.
  - Le scénario prend des clics, des appuis longs, des captures, ou une vidéo `rush.webm`.
- `ecrans/` : les écrans réels (WebP 1920×1200). Ils viennent du build web de `braindcode1/foodeatup-kitchen-screen` en mode démo :
  - `flutter build web --dart-define=KDS_SIMULATED=true --no-web-resources-cdn`, puis serveur local sur le port 8123 ;
  - restaurant de démonstration « LUK », aucun restaurant réel contacté.
- `generer.py` : crée les projets HyperFrames dans `projets/` (dossier non versionné). Sans fichier `voix/<cle>.mp3`, il produit un brouillon muet.
- `rendre.sh` : rend les vidéos dans `brouillons/` (dossier non versionné).
- `fonds/` : les fonds de vignettes générés par Lovable (projet Académie, `public/tutos-kds/fonds`). Ils montrent le chef et ne contiennent aucun texte.
- `vignettes.py` : compose chaque vignette 16:9 à partir du fond, d'un vrai écran, de l'accroche, du badge et du logo officiel. Résultat : `sortie/<cle>-vignette.jpg`.
- `fiches-app-kds.ts` : les fiches de l'Académie. Elles sont versionnées dans `PrendsTaPart/foodeatup-guide-star-227b4772`.

## Publication

Une vidéo n'est publiée qu'une fois sa voix ajoutée et son contrôle qualité au vert. Elle va alors à trois endroits :

- la bibliothèque RapidoCMS ;
- l'Académie, par une PR sur le dépôt GitHub ;
- YouTube, sur la chaîne FoodEatUp.
