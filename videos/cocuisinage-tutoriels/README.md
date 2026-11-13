# Tutoriels vidéo de l'application Cocuisinage

Six tutoriels verticaux (1080 × 1920, 30 i/s, 17 à 25 s), filmés dans la **vraie application**
Cocuisinage by FoodEatUp (dépôt `PrendsTaPart/App-Demo-FoodEatUp-`), montés en HyperFrames 0.9.41.

| Sujet | Titre | Végé-fruité |
| --- | --- | --- |
| `premier-lancement` | Le premier lancement | le chef |
| `quartier` | Mon Quartier Gourmand | Capitaine Carotte |
| `autour-de-moi` | Autour de moi | Mango Queen |
| `recette` | La fiche recette (écoute et photo d'étape) | Don Tomate |
| `scanner` | Le scanner | Kevin Kiwi |
| `moi` | La page Moi | Le Sage Brocoli |

## Chaîne

1. **Tournage** (dépôt de l'application) : `cd app && flutter test tool/tutoriels_test.dart`.
   Chaque sujet est joué en mode démonstration (compte ouvert, 412 × 915 dp) et filmé image par
   image (10 i/s, 824 × 1830), animations comprises → `captures/tutoriels/<sujet>/` + `plan.json`
   (nombre d'images, position de chaque toucher). Ces images ne sont pas versionnées.
2. **Voix** : ElevenLabs, voix « Adam – Formation » (`TGAegA0zNRi8I6nUdq3i`), `eleven_v4`, connecteur
   ElevenLabs → `assets/voix/<sujet>.mp3`. Le texte de chaque voix est dans `build.py` (`SUJETS`) :
   il décrit ce que l'écran montre, rien de plus.
3. **Montage** : `python3 build.py --captures <app>/captures/tutoriels` écrit `<sujet>/index.html` :
   carte d'ouverture (Végé-fruité, titre), téléphone qui monte, écran filmé ralenti juste assez pour
   suivre la voix, doigt animé à chaque toucher, sous-titres, carte de fin (« À vous de jouer ! » + logo).
   Voix normalisée à -16 LUFS avant le mélange ; musique des stories FoodEatUp
   (`videos/stories-foodeatup-30j/audio/bgm.mp3`) à 12 %.
4. **Rendu** : `./rendre.sh` → `rendus/<sujet>.mp4` + `.jpg`, avec le plafond audio du guide
   (`alimiter=limit=0.6:level=disabled`, crêtes vers -4,3 dB).

Les images (logo, mascotte, Végé-fruités) sont celles embarquées dans l'application, non retouchées.
Aucun plan vidéo Higgsfield n'a été généré (règle du dépôt).

## Limites connues

- Mode démonstration : les lieux, les points et le produit scanné sont les données d'exemple de
  l'application (le bandeau « Démonstration » est visible quand l'écran l'affiche).
- La carte « Autour de moi » est filmée sans fond de carte (pas de tuiles hors ligne pendant le tournage).
- L'appareil photo de l'étape montre une photo de plat embarquée à la place de l'aperçu caméra.
- Les sous-titres sont placés au prorata du texte, pas mot à mot.
- Les scripts n'ont pas été validés avant la génération de la voix (étape 3 de
  `FOODEATUP-TUTORIELS-WORKFLOW.md`) : à relire avant toute publication.
