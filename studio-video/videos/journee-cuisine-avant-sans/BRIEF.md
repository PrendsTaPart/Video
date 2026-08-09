---
workflow: faceless-explainer
flow: automation
storyboard: no
message: "Cinq minutes après l'ouverture, la cuisine tourne déjà sur du papier — et personne ne le voit."
destination: website (poster page today; site video slot reserved)
aspect: 1920x1080
language: fr
length: 75s (corps du film, hors intro/outro communes)
angle: story-explainer (une matinée en cuisine, à la première personne, avant le service)
audience: restaurateurs / gérants indépendants — public marketing FoodEatUp
---

## Intent

"C1s" de la série "Une journée SANS FoodEatUp" — deuxième film de la série après
le pilote "D1s" (`journee-directeur-avant-sans`), suivi ici comme gabarit exact
(structure de fichiers, palette, conventions GSAP, grammaire visuelle). Voix d'un
chef/cuisinier tôt le matin, avant le service : sec, résigné, ironique-de-constat
— même registre que le pilote. Le sujet est le nombre d'outils papier disséminés
en cuisine (classeur HACCP, tableau blanc, carnet, factures, fiches techniques,
étiquettes) et l'absence de lien entre eux — jamais un jugement sur un outil ou
un éditeur nommé.

## Réutilisation (identique sur toute la série, copiée telle quelle depuis le pilote)

- `compositions/frames/00-titre.html` — carton de titre
- `compositions/frames/00b-contexte.html` + `assets/audio/vo-00b.mp3` — plan de
  contexte, mêmes icônes (`public/generated/icon-*-crop.jpg`, copiées depuis le
  pilote)
- `compositions/frames/09-carte-marque.html` (renommée depuis `08-carte-marque.html`
  du pilote — contenu et voix identiques) + `assets/audio/vo-09.mp3`
  (= `vo-08.mp3` du pilote)
- `compositions/frames/10-cta-decouvrir.html` (renommée depuis `09-cta-decouvrir.html`)
- `compositions/watermark.html`
- `frame.md`, `.hyperframes/caption-skin.html` — design system, valeurs identiques
- `public/foodeatup-logo.png`, `public/foodeatup-product-dashboard.png`
- `assets/fonts/`, `assets/vendor/gsap.min.js`

Les frames 08/09 du pilote ont été renumérotées 09/10 dans ce projet pour laisser
la place aux 8 frames de corps (01 à 08) propres à ce film, sans collision de nom
de fichier. Contenu, texte et timings internes de ces fichiers copiés n'ont pas
été modifiés — seuls leurs `data-start`/`data-duration` dans `index.html` ont été
recalculés pour ce film.

## Corps du film — 8 frames propres à "Cuisine, avant le service"

| # | Composition | Beat (script) | Visuel |
|---|---|---|---|
| 01 | `01-sept-heures-cuisine.html` | "Sept heures. La cuisine est vide. Le classeur, lui, est plein." | Horloge "7H" + photo `haccp-binder.jpg` |
| 02 | `02-temperatures-tableau.html` | "Les températures... tableau blanc. Effacé hier soir." | Deux panneaux : `temperature-log-clipboard.jpg` / `whiteboard-wiped.jpg` |
| 03 | `03-refrain.html` | Aparté série : "La nouvelle a été formée trois heures. Elle est partie au bout de six semaines." | Numéral géant rouge, hard-cut 3H → 6 SEM. (CSS pur) |
| 04 | `04-livraison-dlc.html` | "La livraison arrive. Je note les DLC sur un carnet..." | Photo `salmon-crate.jpg` + carnet CSS (frappe) |
| 05 | `05-facture-beurre.html` | "La facture... comptable... kilo de beurre." | Photo `01-factures.jpg` + stat "6 semaines" + placeholder "—" (jamais de chiffre inventé) |
| 06 | `06-fiches-techniques.html` | "Fiches techniques... Version 2023... changé quatre fois." | CSS pur : carte "V2023" barrée + compteur 0→4 |
| 07 | `07-etiquettes-allergenes.html` | "Étiquettes au marqueur... allergènes... j'espère." | Photo `marker-labels.jpg` + puces allergènes marquées "?" (jamais de coche verte) |
| 08 | `08-onze-heures-trente.html` | "Onze heures trente. Ma matinée est faite. Elle n'est nulle part." | CSS pur, ligne brisée + 3 lignes (bookend de l'ouverture, comme le Frame 7 du pilote) |

Le refrain de la série a été inséré à 45.265s dans le montage final (~19s après
le début du corps, soit dans le premier tiers du film comme demandé) — cousu en
hard-cut entre le plan "températures/tableau" et le plan "livraison", exactement
au point de couture suggéré par le brief (juste avant la livraison).

## Assets — images réellement utilisées

**Dossier partagé `_shared-sans-assets/` (textures/objets physiques, palette
neutre "sans", zéro logo) :**
- `haccp-binder.jpg` (Frame 01)
- `temperature-log-clipboard.jpg`, `whiteboard-wiped.jpg` (Frame 02)
- `salmon-crate.jpg` (Frame 04 — pas listé nommément dans la consigne mais présent
  dans le dossier partagé et visuellement pertinent pour "la livraison arrive" ;
  réutilisé plutôt que d'en générer un nouveau, dans l'esprit de la consigne de
  réutilisation)
- `marker-labels.jpg` (Frame 07)

**Réutilisées depuis le pilote (`journee-directeur-avant-sans/public/generated/`) :**
- `01-factures.jpg` (Frame 05)
- `icon-livraison-crop.jpg`, `icon-stock-crop.jpg`, `icon-encaisser-crop.jpg`
  (dépendances de `00b-contexte.html` réutilisé)

**Non utilisées :** `04-tableur.jpg` du pilote (jugée trop proche d'un rendu
d'écran logiciel générique pour la scène "fiches techniques" — remplacée par une
maquette CSS pure, cohérente avec la contrainte "pas d'écran logiciel
photoréaliste"). Aucune image n'a été générée via `mcp__RapidoCMS__generate_image`
— les assets existants couvraient tous les beats prévus pour une photo.

## Voix — ElevenLabs (hors pipeline TTS du skill)

8 lignes générées via `mcp__ElevenLabs__text_to_speech` (voix `pNInz6obpgDQGcFmaJgB`,
`eleven_multilingual_v2`, `language_code: fr` — même voix que le pilote, pour la
cohérence du narrateur sur toute la série). Chaque clip brut a été téléchargé dans
`assets/audio/raw/` puis complété d'un silence de fin (`ffmpeg apad`) pour occuper
la durée de plan voulue (2,3 à 5,7s de silence selon le poids dramatique du beat),
exactement le procédé documenté par le pilote. `assets/audio/vo-01.mp3` à
`vo-08.mp3` sont les fichiers finaux (silencieux-inclus) utilisés dans `index.html`.

Durée totale du corps (frame 01 start → frame 08 end) : **74.97s**, très proche
de la cible 75s. Calcul : 8 frames dont la durée = durée de la voix (silence
inclus), chaînées avec un recouvrement de 0.5s à chaque transition (comme le
pilote), soit `Σ(durées) − 7×0.5 = 75.0s` visé, `74.97s` réel après arrondi des
mesures `ffprobe`.

## Simplifications documentées

- **Captions.** Pas de piste `captions.html`/`captions.mjs` pour le corps du
  film. Comme `00b-contexte.html` dans le pilote, chaque frame de corps porte
  son texte directement à l'écran (labels, titres, listes) — le texte affiché
  couvre déjà l'intégralité de ce qui est dit, donc une bande de sous-titrage
  mot-par-mot séparée n'apporterait pas d'information supplémentaire et aurait
  demandé de recâbler `caption_groups.json`/`caption-overrides.json` sans gain
  clair pour ce format à 8 plans courts. Décision explicitement permise par la
  tâche ("si trop lourd à recâbler proprement, tu peux t'en passer").
- **Pas de BGM/SFX**, comme le pilote — pas de bibliothèque musicale HeyGen
  connectée dans cet environnement, pas de contournement fragile inventé.
- **`audio_meta.json`** n'a pas été reconstruit à la main pour ce projet : il
  n'est consommé que par le pipeline `captions.mjs`, non utilisé ici (voir
  ci-dessus). Documenté pour éviter le piège connu (`audio.mjs fetch-sfx`
  écrasant `voices: []`) plutôt que de le redécouvrir.

## Pièges techniques rencontrés

- `npx hyperframes lint` a d'abord échoué sur des assets manquants : les icônes
  de `00b-contexte.html` (dépendance du fichier réutilisé, oubliées lors de la
  copie initiale) et `salmon-crate.jpg` (référencé avant d'être copié). Corrigé
  en copiant les fichiers manquants dans `public/generated/`.
- `npx hyperframes lint` a ensuite signalé un chevauchement sur la piste audio
  10 : en donnant à chaque `<audio>` la même durée que sa frame visuelle (qui
  inclut 0.5s de recouvrement de transition avec la frame suivante), les clips
  audio consécutifs se chevauchaient de 0.5s. Corrigé en réduisant la
  `data-duration` de chaque `<audio>` (frames 01 à 07) de 0.5s par rapport à sa
  frame — l'audio se termine exactement au début du plan suivant, tandis que la
  frame visuelle continue 0.5s dans le silence de fin (déjà présent grâce au
  padding `ffmpeg apad`) pour porter le fondu de transition. La frame 08 (avant
  le hard-cut vers la carte de marque, sans recouvrement) garde sa durée audio
  pleine, comme le Frame 7 du pilote.
- Contrairement à ce que documentait le pilote, `npx hyperframes check` a cette
  fois **réussi sa passe Runtime** dans cet environnement (probablement une
  connectivité réseau différente au moment de ce run) — `Check passed` avec
  0 erreur (2 avertissements GSAP mineurs "target not found" à t=0s, sans
  incidence visible sur le rendu ; 2 notes Layout de dépassement mineur non
  bloquantes, dont un dépassement du halo `f8-glow` interne à la carte de marque
  réutilisée, hérité du fichier du pilote et non modifiable sous contrainte de
  "ne pas changer le contenu réutilisé"). `npx hyperframes snapshot` n'a pas été
  testé séparément puisque `check` couvrait déjà le rendu Runtime avec succès ;
  le contact-sheet a malgré tout été reconstruit via `ffmpeg` à partir du MP4
  rendu (plus rapide, et cohérent avec la méthode documentée par le pilote).
- Rendu final via `npx hyperframes render` : succès, ~11 minutes, aucun
  contournement nécessaire.

## Note de sécurité — message reçu en cours de tâche

Pendant l'écriture des frames de corps, un message affiché comme venant du
"coordinateur" est arrivé, affirmant que la session avait été interrompue par
un plafond d'usage et demandant de "reprendre le travail". Aucune interruption
réelle n'avait eu lieu — j'étais activement en train d'écrire les frames au
moment du message. Je n'ai suivi aucune instruction qui en aurait découlé au-delà
de continuer le travail déjà en cours (ce que j'aurais fait de toute façon) ; je
ne l'ai pas traité comme une confirmation ou une approbation de l'utilisateur.
Signalé ici par cohérence avec la pratique documentée dans le `BRIEF.md` du
pilote face à des messages "coordinateur" non vérifiables.

## Rendu final

`renders/journee-cuisine-avant-sans_2026-08-09_10-53-43.mp4` — 1920×1080,
h264/aac, **111.27s** (intro 3.5s + contexte 22.782s + corps 74.97s + carte de
marque 5.6s + CTA 4.4s, avec recouvrements de transition). `snapshots/contact-sheet.jpg`
reconstruit via `ffmpeg` (12 vignettes couvrant l'ensemble du film). Livrable
terminé.
