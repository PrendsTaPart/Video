# Tutoriel — Créer son compte FoodEatUp + confirmation email

Module 1 « CONFIGURATION », dossier Drive `1 - Inscription, e-mail de confirmation`.
Voix Adam FR (`TGAegA0zNRi8I6nUdq3i`, `eleven_multilingual_v2`).
Durée livrée : **37,5 s** — pic audio **-3,6 dBFS** (mesuré sur le MP4 final).

## Voix off

| # | Texte | Durée | Placement |
|---|---|---:|---|
| N0 | Créer votre compte FoodEatUp ? C'est deux minutes, montre en main. | 3,47 s | carte d'intro |
| N1 | Sur la page d'inscription, renseignez votre nom, votre prénom et votre adresse email. | 4,49 s | saisie du formulaire |
| N2 | Choisissez votre mot de passe, confirmez-le, puis validez avec S'inscrire. | 4,44 s | mot de passe + clic S'inscrire |
| N3 | FoodEatUp vous envoie aussitôt un email de vérification. | 3,06 s | page « Vérification de l'email » |
| N4 | Ouvrez votre boîte mail : le message vous attend déjà. | 3,06 s | boîte Gmail |
| N5 | Un clic sur Vérifier mon adresse email, et votre compte est activé. | 3,60 s | email + clic Vérifier |
| N6 | Bienvenue dans votre espace ! Vous pouvez maintenant ajouter votre boutique. | 4,08 s | espace connecté |
| N7 | Un compte confirmé, c'est votre restaurant prêt à être piloté. | 3,34 s | espace connecté (bénéfice) |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,09 s | carte de fin (CTA) |

## Découpage

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 3,9 s | CRÉER SON COMPTE FOODEATUP |
| A | 0,50 → 6,00 | 4,90 s | nom, prénom, email |
| B | 6,00 → 9,60 | 3,20 s | mot de passe + confirmation |
| C | 9,60 → 10,90 | 1,70 s | **zoom-punch** sur S'inscrire (1422, 644) |
| D | 10,90 → 13,80 | 3,50 s | page de vérification |
| E | 14,00 → 17,80 | 3,50 s | boîte Gmail |
| F | 25,50 → 27,10 | 2,20 s | email de vérification |
| G | 27,10 → 27,68 | 1,80 s | **zoom-punch** sur Vérifier mon adresse email (1149, 398) |
| H | 39,30 → 44,25 | 8,00 s | Bienvenue dans votre espace |
| outro | carte | 7,1 s | CTA |

Coupes volontaires dans le rush : **19,5 → 25,5 s** (détour par le site vitrine) et
**27,7 → 39,3 s** (11 s d'écran de chargement vide).

## Animations

- Cartes intro/outro : **Ken Burns** (zoom avant sur l'intro, arrière sur l'outro) + fondus.
  `zoompan` n'est utilisé **que** sur les images fixes — jamais sur le rush.
- **Transitions xfade** (0,28 s) à chaque raccord : fondu sur l'action continue,
  `slideleft` aux trois endroits où du métrage est coupé, pour que le saut se lise
  comme une navigation.
- **Bandeaux d'étape animés** en bas à gauche, qui glissent depuis la gauche puis
  ressortent (« 1 · Vos informations » … « Votre espace est prêt »).
- **Encadré orange pulsant** autour du bouton pendant chaque zoom-punch.

## Points de vigilance rencontrés

- Les deux rushes du dossier Drive sont **inversés** : `oublie de mot de passe.mp4`
  contient la création de compte, et `Création d'un compte...mp4` contient la
  réinitialisation du mot de passe. Renommés ici en `screen-inscription.mp4` et
  `screen-motdepasse.mp4`.
- Le zoom-punch sur « Vérifier mon adresse email » doit rester **avant 27,70 s** :
  la page bascule sur un écran de chargement vide juste après, et l'encadré se
  retrouvait posé sur du vide.
- Sortie encodée avec `-t` plutôt que `-shortest` : le mix audio se termine
  légèrement avant la vidéo et tronquait le fondu final au noir.

## Reste à faire

Le rush `screen-motdepasse.mp4` (réinitialisation du mot de passe) n'est pas utilisé
dans cette vidéo — il peut alimenter un tutoriel dédié « mot de passe oublié ».
