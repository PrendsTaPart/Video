# Script ElevenLabs — Tutoriel 00 « Créer son compte Plan'It »

Toutes les lignes parlées de l'épisode, dans une seule voix féminine.

La ligne **N0** est prononcée par l'avatar à l'image (bulle de présentation,
synchronisation labiale — voir `AVATAR.md`). Les lignes **N1 à N9** sont de la
voix off pure, qui **commente la démonstration écran**. **N10** ferme sur la
punchline, posée sur l'animation de fin.

## Réglages

| Réglage | Valeur |
|---|---|
| Voix | **Perle — Premium French Corporate Voice** |
| `voice_id` | `UaGvaD7NWzU5mJNoUqoY` |
| Modèle | `eleven_multilingual_v2` |
| Profil | Féminine, français standard, pensée pour l'e-learning, l'onboarding et les tutoriels |
| Sortie | MP3, un fichier par ligne, dans `vo/` |
| Flow ElevenLabs | `sKOYDZDaS0015NSEy5C1` |

> **Pourquoi cette voix** : elle est décrite pour « corporate content, e-learning,
> tutorials, onboarding, explainers ». C'est exactement le registre de l'Académie
> — chaleureuse sans être commerciale, et assez neutre pour tenir 43 épisodes.

---

## Lignes de voix off

Les durées sont **mesurées sur les fichiers rendus**, pas estimées. C'est cette
colonne qui pilote la durée de chaque plan au montage.

| # | Fichier | Texte | Durée | Écran commenté |
|---|---|---|---:|---|
| **N0** | `vo/N0.mp3` | *Bienvenue dans l'Académie Plan'It. Aujourd'hui, on commence par le tout début : créer votre compte. Une minute, et votre espace de travail est ouvert.* | 8,62 s | **Bulle avatar** — voir `AVATAR.md` |
| N1 | `vo/N1.mp3` | Voici l'écran d'accueil de Plan'It. Vous n'avez pas encore de compte : touchez « Inscrivez-vous », tout en bas. | 5,62 s | Écran **Se connecter** |
| N2 | `vo/N2.mp3` | Le formulaire tient en quatre champs : votre nom complet, votre adresse email, puis un mot de passe que vous confirmez. | 5,98 s | Écran **Créer un compte**, saisie du nom |
| N3 | `vo/N3.mp3` | Un conseil : prenez votre adresse professionnelle. Vos collègues pourront rejoindre le même espace de travail. | 5,15 s | Saisie de l'email |
| N4 | `vo/N4.mp3` | Touchez « S'inscrire ». Plan'It crée votre compte et vous envoie un code à six chiffres. | 4,86 s | Mots de passe + appui sur **S'inscrire** |
| N5 | `vo/N5.mp3` | L'écran de vérification s'affiche. Le code, lui, vous attend dans votre boîte mail. | 4,08 s | Écran **Vérifier le code** (6 cases) |
| N6 | `vo/N6.mp3` | Ouvrez le message « Welcome to Plan'It » : le code est là, bien en évidence. | 4,36 s | Gmail, code **815590** |
| N7 | `vo/N7.mp3` | Revenez dans l'application, saisissez les six chiffres, puis touchez « Vérifier ». | 4,55 s | Saisie OTP + **Vérifier** |
| N8 | `vo/N8.mp3` | Votre email est validé. Reconnectez-vous avec l'adresse et le mot de passe que vous venez de choisir. | 5,15 s | Retour **Se connecter**, saisie |
| N9 | `vo/N9.mp3` | Et voilà votre espace Plan'It. Le tableau de bord est encore vide : c'est normal, tout reste à construire. | 5,56 s | **Dashboard** « Bonjour Jean Martin » |
| **N10** | `vo/N10.mp3` | **Vous planifiez une fois. Vos agents s'occupent du reste. Plan'It.** | 3,39 s | **Animation de fin** |

**Total voix off** : 57,3 s · **présentation (N0)** : 8,6 s · **démonstration (N1→N9)** : 45,3 s · **punchline (N10)** : 3,4 s.

> **N0 est à part** : c'est la seule ligne prononcée *par l'avatar à l'image*, et
> c'est elle qui alimente la synchronisation labiale (`creatify-aurora`). Les
> autres lignes sont de la voix off pure, posées sur la démonstration écran.

---

## La punchline

> ### « Vous planifiez une fois. Vos agents s'occupent du reste. »

Elle ferme chaque épisode de l'Académie. Elle dit la promesse réelle du produit —
des tâches planifiées (`once`, `daily`, `weekly`, `monthly`) exécutées par des
agents connectés à des serveurs MCP — sans promettre de magie. Les deux membres
de phrase sont aussi les deux moitiés de l'animation de fin, l'un sous l'autre.

**Ne pas la modifier d'un épisode à l'autre** : c'est la signature sonore de la
série. Seule la ligne d'enchaînement (« Tutoriel suivant · … ») change.

---

## Choix d'écriture

- **Vouvoiement.** L'app tutoie dans l'onboarding (« Planifie en un clic »), mais
  un tutoriel qui vouvoie vieillit mieux et passe en contexte professionnel.
- **Les libellés sont cités au mot près** — « Inscrivez-vous », « S'inscrire »,
  « Vérifier » — pour que le spectateur retrouve exactement ce qu'il voit.
- **N3 reprend l'astuce de la fiche MCP** (`astuce.texte`, agent *nina*) plutôt
  que d'inventer un conseil : la fiche et la vidéo racontent la même chose.
- **N9 désamorce** le tableau de bord vide, qui est le premier moment de doute
  d'un nouvel utilisateur.
- **Aucune ligne ne dépasse 6 s.** Au-delà, la ligne déborde de son plan et le
  décalage s'accumule jusqu'à la fin.

---

## Régénérer la voix off

Via le MCP ElevenLabs, une ligne à la fois, en réutilisant le flow :

```
creative_generate_speech(
  flow_id = "sKOYDZDaS0015NSEy5C1",
  voice_id = "UaGvaD7NWzU5mJNoUqoY",
  model_id = "eleven_multilingual_v2",
  generations_count = 1,
  prompt = "<le texte de la ligne>"
)
```

Puis `creative_get_flow_run_status` pour récupérer l'URL du MP3.

> ⚠️ **Après toute regénération, relancer `python3 build_video.py`.** Les durées
> de plan sont dérivées des fichiers audio : une ligne plus longue étire son plan
> automatiquement, mais seulement au prochain rendu.
