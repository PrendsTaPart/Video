# Script HeyGen — Tutoriel 00 « Créer son compte Plan'It »

Avatar féminin francophone qui **présente** la vidéo. Il n'accompagne pas la
démonstration écran de bout en bout : il ouvre (après l'animation de logo) et
laisse ensuite la main à la voix off ElevenLabs.

Fiche MCP de référence : `tutoriel_spec(numero: 0)` — slug `creer-son-compte`,
module `configuration-onboarding`, étape `ouvrir-la-porte`.

---

## 1. Réglages du projet HeyGen

| Réglage | Valeur |
|---|---|
| Format | **9:16 · 1080 × 1920** (même cadre que le screencast) |
| Avatar | Avatar féminin *Studio / Business casual*, cadrage **buste**, regard caméra |
| Fond | **Green screen / fond transparent** → incrusté ensuite sur `#EDEAFE` (`AppColors.backgroundPage`) |
| Voix | Voix féminine française, débit posé. Si vous voulez la **même voix** que la voix off : importer dans HeyGen la voix ElevenLabs *Perle* (`UaGvaD7NWzU5mJNoUqoY`) |
| Vitesse | 1.0 |
| Sous-titres | Désactivés dans HeyGen (ils sont brûlés au montage, police Manrope) |
| Durée cible | **10 à 12 s** |

> **Pourquoi fond transparent** : le montage place l'avatar en plein cadre sur le
> lavande de l'app, avec le logo Plan'It en filigrane en haut. Un fond de studio
> HeyGen jurerait avec la charte.

---

## 2. Texte à coller dans HeyGen

Un seul bloc, ponctuation comprise — c'est elle qui porte le rythme.

```
Bienvenue dans l'Académie Plan'It.
Aujourd'hui, on commence par le tout début : créer votre compte.
Une minute chrono, et votre espace de travail est ouvert.
Je vous montre les quatre écrans à passer — et le seul endroit où on se trompe souvent.
```

**Durée estimée** : ≈ 11 s à débit normal.

### Découpage en scènes (si vous préférez 4 scènes courtes)

| Scène | Texte | Geste / cadrage |
|---|---|---|
| S1 | « Bienvenue dans l'Académie Plan'It. » | Plan buste, sourire d'accueil, mains basses |
| S2 | « Aujourd'hui, on commence par le tout début : créer votre compte. » | Léger appui de la main ouverte |
| S3 | « Une minute chrono, et votre espace de travail est ouvert. » | Index levé sur « une minute » |
| S4 | « Je vous montre les quatre écrans à passer — et le seul endroit où on se trompe souvent. » | Main qui présente vers la droite (raccord vers le screencast) |

---

## 3. Prompt de direction d'acteur

À coller dans le champ *instructions / style* de HeyGen :

```
Ton : professionnel chaleureux, jamais commercial. Formatrice qui connaît son
produit et met l'utilisateur à l'aise. Débit posé, articulation nette, sourire
présent mais discret. Micro-pause après « Académie Plan'It » et après « le tout
début ». Accentuer « une minute chrono ». Terminer sur une intonation ouverte,
comme si l'on tournait la tête vers l'écran de démonstration.
```

---

## 4. Habillage du plan avatar au montage

- Fond : aplat `#EDEAFE`, halo radial `#FE64D5` à 18 % en bas à droite.
- Logo `black_logo.png` en haut à gauche, 96 px, marge 64 px.
- Bandeau bas : chip arrondi `#4F2DF9`, texte blanc Manrope 700 —
  `TUTORIEL 00 · CRÉER SON COMPTE`.
- Entrée : fondu depuis le blanc de fin d'intro (0,4 s).
- Sortie : coupe franche sur le premier écran du screencast.

---

## 5. Placement dans le montage

| # | Élément | Début | Durée |
|---|---|---:|---:|
| 1 | Animation d'ouverture (`out/intro.mp4`) | 0,00 s | 3,60 s |
| 2 | **Plan avatar HeyGen** | 3,60 s | ≈ 11 s |
| 3 | Démonstration écran + voix off ElevenLabs | ≈ 14,6 s | ≈ 47 s |
| 4 | Animation de fin + punchline (`out/outro.mp4`) | ≈ 61,6 s | 5,20 s |

Exportez le plan avatar en **`assets/avatar-heygen.mp4`**, puis relancez
`python3 build_video.py` : le script détecte le fichier et l'insère
automatiquement (sans lui, il produit la version courte sans avatar).

---

## 6. Réutilisation pour les 42 autres tutoriels

Seules trois lignes changent d'un tutoriel à l'autre. Le reste du prompt est
constant, ce qui permet de produire les plans avatar en lot :

```
Bienvenue dans l'Académie Plan'It.
Aujourd'hui : {TITRE DE LA FICHE}.
{PROMESSE DE LA FICHE}
Je vous montre comment faire.
```

Les trois variables sortent directement de `tutoriel_spec(numero: N)` —
respectivement `titre`, une reformulation courte, et `promesse`.
