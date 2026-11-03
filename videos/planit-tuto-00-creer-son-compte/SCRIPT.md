# Tutoriel 00 — Créer son compte Plan'It

Premier épisode de l'**Académie Plan'It** (43 tutoriels). Fiche MCP :
`tutoriel_spec(numero: 0)` — slug `creer-son-compte`, module
`configuration-onboarding`, étape `ouvrir-la-porte`, promesse *« À la fin de
cette minute, votre compte existe et votre espace de travail est ouvert. »*

**Livré** : `out/tuto-00-creer-son-compte.mp4` — **54,23 s**, 1080 × 1920,
H.264 High / yuv420p, AAC 48 kHz stéréo, faststart.

---

## 1. Analyse des écrans de la source

Source : `assets/screencast-inscription.mp4` — 78,0 s, 590 × 1280, 30 fps,
**muette**. Capture d'écran d'un téléphone Android, clavier français.
Bandes noires mesurées au `cropdetect` : image utile **590 × 1234 à l'offset (0, 23)**.

| Timecode source | Écran | Ce qu'on voit |
|---|---|---|
| 0,0 → 2,5 | **Se connecter** | Logo noir, titre Sora, « Connectez-vous à votre compte ». Champs *Email* et *Mot de passe* (œil barré), lien « Mot de passe oublié ? », bouton rose « Se connecter », pied « Vous n'avez pas de compte ? **Inscrivez-vous** » |
| 2,5 → 4,2 | Navigation | Appui sur « Inscrivez-vous » |
| 4,2 → 5,0 | **Créer un compte** | « Commencez à planifier intelligemment ». 4 champs : *Nom complet*, *Email*, *Mot de passe*, *Confirmer le mot de passe*. Bouton « S'inscrire », lien « Connectez-vous » |
| 5,0 → 12,0 | Saisie du nom | Clavier FR, suggestions. « Je » → « Jean Martin ». Le champ actif passe en bordure rose |
| 12,0 → 17,0 | Saisie de l'email | `demoutilisateur7@gmail.com`. La page défile, le titre sort du cadre |
| 17,0 → 27,0 | Mot de passe | 11 caractères masqués, clavier symboles |
| 27,0 → 34,0 | Confirmation | Second champ rempli à l'identique |
| 34,0 → 35,2 | Envoi | Bouton « S'inscrire » en état de chargement (spinner, fond grisé) |
| 35,2 → 39,2 | **Vérifier le code** | « Un code à 6 chiffres a été envoyé à demoutilisateur7@gmail.com. Veuillez le saisir ci-dessous. » 6 cases vides, « Vous n'avez pas reçu de code? **Renvoyer** », bouton « Vérifier » |
| 39,2 → 42,0 | *(hors app)* | Sortie vers l'écran d'accueil du téléphone, ouverture de Gmail |
| 42,0 → 47,0 | **Email Plan'It** | « Welcome to Plan'It! » — *Thanks for signing up! Please use the verification code below to activate your account* — code **815590** sur pastille verte — « © 2025 Plan'It » |
| 47,0 → 50,5 | *(hors app)* | Bascule multitâche, retour dans l'application |
| 50,5 → 58,5 | Saisie du code | Les 6 cases se remplissent (8-1-5-5-9-0), clavier numérique, appui sur « Vérifier » |
| 58,5 → 59,5 | Retour | L'app revient sur **Se connecter** — comportement conforme au code : `VerificationCodeScreen` fait `pushReplacementNamed('/signin')` sur `AuthSuccess` |
| 59,5 → 71,5 | Reconnexion | Saisie de l'email (bulle « Paste ») puis du mot de passe, appui sur « Se connecter » |
| 71,5 → 74,8 | Chargement | « Bonjour Utilisateur », cartes en squelette, clavier encore affiché |
| 74,8 → 78,0 | **Tableau de bord** | « Bonjour **Jean Martin** — Bienvenue dans votre espace Plan'it ». Bouton « Démarrer une conversation », filtres, cloche. Carte « Aujourd'hui — Aucune tâche prévue aujourd'hui ». KPI « Taux de réussite 0% », « En attente 0 ». Bloc « Activité ». Barre à 5 onglets |

### Ce que la source confirme du dépôt `planit-app`

| Observé à l'écran | Source dans le code |
|---|---|
| Fond lavande | `AppColors.backgroundPage` = `#EDEAFE` |
| Titres lourds arrondis | `AppTextStyles.soraDisplay1/2` (Google Fonts **Sora**) |
| Libellés et corps | **Manrope** |
| Bouton rose→violet | `AppColors.brandGradient` (`#FE64D5` → `#4F2DF9`) |
| Violet du tableau de bord | `AppColors.primary` = `#4F2DF9` |
| Les 4 champs, dans cet ordre | `signup.dart` — `Nom complet`, `Email`, `Mot de passe`, `Confirmer le mot de passe` |
| Retour au login après OTP | `verification_code.dart`, `BlocListener` sur `AuthSuccess` |
| « Renvoyer » | `_resendCode()` |

### Deux points relevés

1. **Le retour sur « Se connecter » après vérification** oblige l'utilisateur à
   ressaisir ses identifiants alors qu'il vient de les choisir. C'est le
   comportement du code, donc la vidéo l'assume et l'explique (ligne N8) plutôt
   que de le masquer — mais c'est un candidat naturel à une amélioration produit.
2. **L'email de vérification est en anglais** (« Welcome to Plan'It! ») alors que
   toute l'app est en français — Gmail propose d'ailleurs de le traduire. À
   signaler à l'équipe backend ; la voix off contourne en ne citant que le titre.

---

## 2. Structure du montage

| # | Élément | Durée | Voix |
|---|---|---:|---|
| 1 | Animation d'ouverture `out/intro.mp4` | 3,60 s | — (sound design) |
| 2 | *Plan avatar HeyGen* (optionnel) | ≈ 11 s | Avatar |
| 3 | Démonstration écran, 9 plans | 45,31 s | ElevenLabs N1→N9 |
| 4 | Animation de fin `out/outro.mp4` | 5,20 s | ElevenLabs N10 (punchline) |

**Sans avatar : 54,23 s.** Avec le plan avatar : ≈ 65 s.

### Règle de calage

**Chaque plan dure exactement la longueur de sa ligne de voix off.** Le script
lit la durée du MP3 et en déduit le facteur de vitesse du plan. Les saisies
clavier sont donc accélérées (jusqu'à ×3,6 sur les mots de passe) et les écrans
à lire sont tenus, voire ralentis.

C'est la correction directe de l'écueil rencontré sur `foodeatup-abonnement-tuto` :
des durées fixées au jugé, un dépassement qui s'accumule ligne après ligne, et
toute l'erreur qui atterrit sur la carte de fin.

### Découpage

| Plan | Source | Sortie | Vitesse | Bandeau |
|---|---|---:|---:|---|
| 1 | 0,0 → 4,2 | 5,62 s | ×0,75 | 1 · L'écran de connexion |
| 2 | 4,2 → 13,0 | 5,98 s | ×1,47 | 2 · Le formulaire d'inscription |
| 3 | 13,0 → 17,5 | 5,15 s | ×0,87 | 3 · L'adresse professionnelle |
| 4 | 17,5 → 35,0 | 4,86 s | ×3,60 | 4 · Mot de passe et confirmation |
| 5 | 35,2 → 39,2 | 4,08 s | ×0,98 | 5 · Le code à 6 chiffres |
| 6 | 42,0 → 47,0 | 4,36 s | ×1,15 | 6 · Le code reçu par email |
| 7 | 50,5 → 58,5 | 4,55 s | ×1,76 | 7 · Vérification du code |
| 8 | 58,8 → 71,5 | 5,15 s | ×2,47 | 8 · Première connexion |
| 9 | 74,8 → 78,0 | 5,56 s | ×0,58 | 9 · Votre espace est ouvert |

**Coupes volontaires** — 39,2 → 42,0 (sortie vers l'écran d'accueil du
téléphone), 47,0 → 50,5 (bascule multitâche) et 71,5 → 74,8 (squelettes de
chargement, clavier encore ouvert). Trois temps morts, 9,6 s retirés.

---

## 3. Habillage

- **Cadre** : téléphone recadré à 590 × 1234, mis à l'échelle sur 1860 px de
  haut, centré sur un fond `#EDEAFE` — le lavande de l'app elle-même, pour que
  le passage bumper → démo ne change pas de fond.
- **Bandeaux d'étape** : chip arrondi `#4F2DF9`, texte blanc Manrope 700, ombre
  portée douce, fondu de 0,35 s à l'entrée et à la sortie. Posé au-dessus de la
  barre d'onglets pour ne jamais masquer l'interface commentée.
- **Raccords** : l'ouverture se termine par un voile lavande et la fin démarre du
  même voile — les raccords se lisent comme des fondus sans décaler l'audio.

---

## 4. Animations d'ouverture et de fin

Générées par `build_bumpers.py` (Pillow + ffmpeg). **Aucun appel Higgsfield**,
conformément à la règle du dépôt.

**Ouverture (3,60 s)** — dégradé de marque `brandGradient` du rose au violet,
halos radiaux, bande lumineuse traversante. Le logo blanc monte de +190 px en
`easeOut` : c'est le geste exact du `SplashScreen` natif
(`Tween(begin: -200, end: 0)`, `Curves.easeOut`). Puis le nom « Plan'It » (Sora
800), un filet qui s'ouvre depuis le centre, le titre du tutoriel, et le chip
« ACADÉMIE PLAN'IT · TUTORIEL 00 ».

**Fin (5,20 s)** — même dégradé inversé. Logo, punchline en deux lignes, filet,
chip blanc « Commencez à planifier intelligemment » (la baseline réelle de
l'écran d'inscription) en `#4F2DF9`, et l'enchaînement vers le tutoriel suivant.

Les libellés qui varient d'un épisode à l'autre passent par `fitted_font()`, qui
réduit la police juste assez pour tenir dans le cadre — indispensable puisque les
titres viennent des fiches MCP et n'ont pas tous la même longueur.

---

## 5. Reproduire

```bash
python3 build_bumpers.py     # out/intro.mp4 + out/outro.mp4
python3 build_video.py       # out/tuto-00-creer-son-compte.mp4
```

Pour ajouter le plan avatar : exporter depuis HeyGen selon `HEYGEN.md`, déposer
le fichier en `assets/avatar-heygen.mp4`, relancer `build_video.py` — il le
détecte et l'insère entre l'ouverture et la démonstration.

## 6. Fichiers

```
planit-tuto-00-creer-son-compte/
├── SCRIPT.md          ce document — analyse des écrans et découpage
├── HEYGEN.md          script et réglages du plan avatar
├── ELEVENLABS.md      script de voix off, voix et punchline
├── build_bumpers.py   génère les animations d'ouverture et de fin
├── build_video.py     monte la vidéo complète
├── assets/
│   ├── screencast-inscription.mp4   source fournie
│   ├── white_logo.png · black_logo.png   logos officiels (planit-app)
│   └── avatar-heygen.mp4            ← à déposer
├── vo/                N1…N10.mp3 — voix off ElevenLabs
└── out/               intro.mp4 · outro.mp4 · tuto-00-creer-son-compte.mp4
```
