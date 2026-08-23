# Pourquoi les interfaces sont des maquettes et pas les vraies captures

En analysant les ~70 enregistrements d'écran du dépôt (`videos/foodeatup-*-tuto/assets/screen.mp4`)
pour les recadrer en vertical, j'ai trouvé trois choses qui interdisent de les diffuser
telles quelles dans une vidéo commerciale publique.

### 1. Des données personnelles réelles à l'écran

`foodeatup-jarvis-tuto` (et d'autres captures de la liste des employés) affichent en clair
des **noms, adresses e-mail et numéros de téléphone d'employés**. Publier ça dans une
vidéo de prospection serait une fuite de données personnelles — et le RGPD s'applique même
si ce sont des comptes de test qui portent de vraies coordonnées.

### 2. La barre de favoris du navigateur

Plusieurs captures (ex. `foodeatup-predibot-tuto`) montrent la **barre de favoris
personnelle** : Gmail, YouTube, et un favori vers un site de téléchargement illégal. Ça
apparaît en haut de l'image, donc dans tout recadrage vertical qui garde le haut du cadre.

### 3. Des données de test peu vendeuses

Des plats nommés « Uuuu », des champs vides, des indicateurs à « 30 % / Faible ». Sur une
vidéo prospect, ça travaille contre le produit.

## Ce que j'ai fait

Toutes les interfaces de la vidéo sont des **maquettes animées** (`build_mockups.py`),
dessinées aux couleurs de la charte, avec des données inventées et cohérentes. C'est
d'ailleurs ce que demandaient tes notes de production : « interfaces IA en mockups épurés ».
Aucune donnée réelle ne peut fuir.

## Ce qu'il faudrait pour passer aux vraies captures

Un **jeu d'enregistrements sur un compte de démonstration propre** :

- un établissement de démo avec une carte crédible (vrais noms de plats, vrais prix) ;
- des employés fictifs (pas d'e-mail ni de téléphone réels) ;
- navigateur en **fenêtre privée, sans barre de favoris**, ou en mode plein écran (F11) ;
- résolution 1920×1080, et si possible un enregistrement cadré serré sur le module montré.

Avec ça, je remplace les maquettes par les vraies captures sans toucher au reste du montage.

---

## Pourquoi la voix off n'est pas encore dans le montage

Le script a été validé, mais je ne peux pas produire les fichiers audio depuis cette session :

- Le **connecteur ElevenLabs** disponible ici génère bien la voix (testé sur la première
  ligne, voix Adam `TGAegA0zNRi8I6nUdq3i`, flow `KcQxLe13OnO3BBrewdnY`), mais il rend le
  résultat dans une vue de lecture côté client. Aucun de ses outils ne renvoie l'URL du
  fichier généré, donc je ne peux pas le rapatrier dans le dépôt pour le monter.
- L'**API REST ElevenLabs** est joignable depuis cette session (`api.elevenlabs.io`), mais
  `ELEVENLABS_API_KEY` n'est pas dans l'environnement : le dépôt la range dans
  `studio-video/.env`, qui est gitignoré et donc absent d'un clone frais.

`build_vo.py` est écrit et prêt : dès que la clé est fournie, une commande génère les 16
lignes, les normalise une par une, et `build_final.py` recale automatiquement les
sous-titres sur les durées réelles.
