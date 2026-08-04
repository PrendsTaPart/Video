# FoodEatUp — Pipeline tutoriels produit (série ~100 vidéos)

Méthode standard pour chaque tutoriel "screen recording -> vidéo pédagogique".
Chaque nouveau tutoriel = nouveau dossier `videos/foodeatup-<sujet>-tuto/`.

## Intrants attendus (fournis par Michael pour chaque tuto)

- 1 image d'ouverture ("carte intro") — ex: `CONFIGURER_SES_UNITES.jpg`
- 1 image de fin ("carte outro" / CTA) — généralement réutilisable telle quelle d'un tuto à l'autre
- 1 enregistrement d'écran `.mp4` de la fonctionnalité (1920x828 typiquement)

## Étapes (dans l'ordre, ne pas sauter)

1. **Analyse de la vidéo**
   Extraire des frames à intervalles réguliers (`ffmpeg -ss t -frames:v 1`) pour
   reconstituer le déroulé exact : quel écran, quel champ rempli, à quel timestamp
   a lieu chaque clic important (boutons d'action primaires : "Ajouter", "Créer",
   "Enregistrer", etc.). Noter les coordonnées pixel (espace source, ex 1920x828)
   de chaque bouton cliqué pour le zoom-punch.

2. **Création du script (voix off)**
   6-8 lignes courtes, voix Adam FR (`TGAegA0zNRi8I6nUdq3i`), ton simple et ludique.
   Structure type :
   - N0 intro : accroche ("Configurer X dans FoodEatUp ? ...")
   - N1..N(n-2) : les actions clés dans l'ordre du screen recording
   - N(n-1) bénéfice : à quoi ça sert / ce que ça débloque ensuite (souvent demandé
     en complément après validation du script — prévoir une ligne dédiée)
   - N(n) outro CTA : "Passez à la restauration intelligente avec FoodEatUp.
     Essayez gratuitement dès aujourd'hui !"

3. **Validation du script — STOP obligatoire**
   Présenter le script texte complet à Michael AVANT de générer l'audio ou de
   monter quoi que ce soit. Ne pas générer la VO tant que le script n'est pas
   confirmé (ou après ajustements demandés, re-présenter si changement de fond).

4. **Montage vidéo** (`build.py` par projet, même moteur à chaque fois)
   - Vitesse de lecture : `setpts=(PTS-STARTPTS)/factor` — **jamais `zoompan` sur
     une vidéo** (ça gèle l'image, bug déjà rencontré et corrigé plusieurs fois).
   - Zoom sur clic ("zoom-punch") : découper le segment en deux sous-clips au
     moment du clic ; le sous-clip après le clic reçoit un `crop=w:h:x:y` fixe
     centré sur le bouton (zoom ~1.20x) + `scale` retour à la taille cible.
     Pas d'`eval=frame` sur `crop` (option inexistante dans ce build ffmpeg).
   - **Calibrer la durée de chaque segment sur la durée de la ligne VO qui le
     commente**, pas l'inverse. Sinon la narration déborde et s'accumule dans
     une carte de sortie exagérément longue (bug rencontré sur le tuto unités :
     segments trop rapides -> outro tenue 15s en silence visuel). Voir le calcul
     factor = raw_duration / target_output_duration.
   - Voix off : placement séquentiel garanti sans chevauchement — chaque ligne
     démarre après `max(anchor, fin_ligne_précédente + GAP)` (GAP ~0.2-0.25s).
     Un doublon de voix (deux lignes qui se chevauchent) a déjà été signalé une
     fois — toujours vérifier qu'aucune ligne ne commence avant la fin de la
     précédente.
   - Carte intro / carte outro : fond flou (boxblur) + image nette overlay + fondus.
   - Audio final : appliquer `loudnorm=I=-16:TP=-1.5:LRA=11` **par ligne VO
     individuellement, avant `adelay`/`apad`** (pas sur le mix composite : le
     mix contient beaucoup de silence entre les lignes espacées, donc un
     `loudnorm` global sous-estime la loudness et sur-amplifie la parole —
     bug rencontré, pics à +1.9dB). Puis sur le mix final, un simple
     `alimiter=limit=0.6:level=disabled` en garde-fou.
     **Piège critique** : le paramètre `level` d'`alimiter` est activé par
     défaut et renormalise le signal à 0dB APRÈS limitation, annulant le
     plafond — toujours passer `level=disabled` explicitement, sinon `limit=`
     n'a aucun effet réel. Prévoir aussi ~4-5dB de marge sous 0dBFS avant
     l'encodage AAC (le codec peut réintroduire 1-2dB de dépassement par
     effet de reconstruction/ringing près du plafond) : viser un plafond
     effectif autour de `limit=0.6` (~-4.4dB) plutôt que 0.85-0.89.
     Vérifier avec `ffmpeg -i out.mp4 -af astats -f null /dev/null` (grep
     "Peak level dB") sur le fichier FINAL encodé — `volumedetect` seul est
     insuffisant, il arrondit et peut afficher "0.0dB" pour un clip réel.
   - Durée cible générale : éviter les blancs, viser le minimum nécessaire pour
     porter le script sans traîner (30-60s typiquement selon la complexité du
     flow ; suivre les instructions ponctuelles de Michael sur la durée).

5. **Intégration de l'image d'ouverture en tant que vignette YouTube**
   **Ne jamais recréer/redesigner une vignette.** Utiliser directement l'image
   d'ouverture fournie par Michael (`assets/intro.jpg`), simplement redimensionnée
   si besoin au format YouTube (1280x720, JPG, <2 Mo) sans recadrage créatif —
   uniquement un `scale`+`crop` neutre si le ratio source diffère légèrement.
   Livrable : `out/thumbnail-youtube.jpg`.

6. **Livraison pour validation — STOP obligatoire (règle ajoutée le 2026-08-02)**
   Une fois le montage terminé et la checklist de compatibilité passée (voir plus
   bas), commit + push du dossier projet (`assets/`, `vo/`, `build.py`, `out/`) sur
   la branche désignée (`work/` reste dans `.gitignore`, c'est du scratch), puis
   livrer le fichier vidéo à Michael (`SendUserFile`). **Ne pas publier tant que
   la vidéo n'est pas validée** : ni upload/schedule RapidoCMS+LinkedIn, ni mise à
   jour du site Lovable. Attendre un retour explicite (OK, ou demande de
   correction — dans ce cas corriger puis relivrer avant de reproposer).

7. **Publication (après validation confirmée)**
   - Upload de la vidéo finale ET de la vignette sur RapidoCMS
     (`mcp__RapidoCMS__upload_file_tool`, en pointant l'URL GitHub raw du fichier
     poussé).
   - `create_draft_tool` + `schedule_draft_tool` sur le compte LinkedIn FoodEatUp
     (2 vidéos/jour, 7h et 16h, prochain créneau libre de la rotation).
   - Ajout du tutoriel sur le site Lovable (`LOVABLE-FOODEATUP-DOCS.md`) + entrée
     dans le tableau "Tutoriels publiés" du même fichier.

## Séquence de fin « cas d'utilisation + prompt Claude » (règle ajoutée le 2026-08-02,
## design revu le 2026-08-02 — animation chatbot en 3 temps)

**Quand un tutoriel correspond à une action exposée par un outil MCP FoodEatUp**
(`mcp__FoodEatUp__*` — voir liste dans `videos/LOVABLE-FOODEATUP-DOCS.md`), ajouter en fin
de vidéo (juste avant la carte de fin/CTA) une séquence animée en 3 temps montrant le cas
d'utilisation (template validé sur `foodeatup-tva-tuto`, à réutiliser tel quel) :

1. **Reveal** — fond crème FoodEatUp (`#FCF9E6`, **pas de boîte noire**), titre "Utilisez
   cette fonctionnalité avec Claude", le prompt affiché en gros dans une carte blanche à
   filet bleu + liseré corail (police Liberation Sans Bold, pas de monospace), avec ses
   `[placeholders]` entre crochets.
2. **Copié** — même carte, filet vert + badge "check" dessiné (pas un glyphe emoji — non
   fiable selon la police), légende "Copié dans le presse-papiers !".
3. **Chatbot Claude** — mockup d'interface Claude : logo réel
   (`studio-video/assets/brand/third-party-logos/claude-logo.png`) + "claude.ai" dans une
   barre du haut, fond `#F0EEE6` (le cream propre à l'UI Claude, pas celui de FoodEatUp),
   bulle utilisateur alignée à droite en corail `#D97757` (couleur de marque Claude, extraite
   du logo lui-même) contenant le prompt collé, bulle assistant à gauche (avatar rond corail
   + astérisque dessiné) qui commence sa réponse — pour montrer l'action prise en charge.

**Implémentation — module partagé, ne pas dupliquer le code d'une vidéo à l'autre.** Tout
vit dans `videos/_shared/claude_prompt_sequence.py` (`render_claude_stage1_png` /
`_stage2_png` / `_stage3_png`, + `CLAUDE_STAGE_D` par défaut). Chaque projet l'importe
(`sys.path.insert(0, ".../_shared")`) et ne fournit que ce qui change : le texte du prompt
(`CLAUDE_PROMPT`) et, optionnellement, la réplique de l'assistant (`response=...`, sinon
texte générique par défaut). **Même univers visuel sur toute la série — gagner du temps
en ne touchant jamais au rendu, seulement au contenu.** Étapes pour un nouveau tutoriel :

```python
import sys; sys.path.insert(0, "/home/user/Video/videos/_shared")
from claude_prompt_sequence import render_claude_stage1_png, render_claude_stage2_png, render_claude_stage3_png
CLAUDE_PROMPT = "..."  # propre à ce tutoriel, avec ses [placeholders]
# puis dans build_silent(), comme pour tva : rendre les 3 PNG, les passer
# dans card(..., fade=False), enchaîner en "slideleft".
```

Chaque étage est rendu en PNG via PIL (contrôle total du texte/formes/logo, évite le bug
`drawtext`/`%` — voir plus bas) puis passé dans `card()` **avec `fade=False`** (les cartes
intro/outro gardent `fade=True` car elles sont en tout début/fin de vidéo ; un stage court
au milieu du montage qui a son propre fondu-au-noir ET un xfade des deux côtés se retrouve
à moitié dans le noir tout le temps qu'il est censé être visible — bug rencontré et corrigé
sur `foodeatup-tva-tuto`). Transitions `slideleft` entre les 3 étages (scènes distinctes),
`fade` partout ailleurs. Si aucun outil MCP ne correspond, ne pas ajouter cette séquence —
pas de prompt inventé. Cette règle vaut aussi bien pour la vidéo que pour la fiche du
tutoriel sur le site Lovable (voir `LOVABLE-FOODEATUP-DOCS.md`, champ `claudePrompt`) :
rester cohérent, même texte de prompt des deux côtés.

**Prévoir 2 lignes VO dédiées à la séquence**, pas une seule : une qui explique le prompt
(ancrée sur l'étage 1 "reveal", éventuellement audible jusqu'à l'étage 2 "copié"), une qui
présente l'envoi dans Claude et le résultat (ancrée sur l'étage 3 "chatbot mockup"). Une
ligne unique qui doit couvrir les 3 étages déborde presque toujours sur le mauvais étage
(bug rencontré sur `foodeatup-tva-tuto` v2 — corrigé en v3, voir son `SCRIPT.md`).
**Mesurer chaque ligne VO avant de fixer les durées de segment/étage** (règle déjà en
place, voir plus bas) : sur `tva`, ignorer cette règle sur l'ensemble de la chaîne (pas
seulement la ligne suivante) avait fait dériver la narration de 4-6 s en fin de vidéo,
au point qu'une ligne décrivant un clic se retrouvait à jouer sur un tout autre segment.
Toujours vérifier après coup que chaque offset réel (`offsets:` imprimé par `build.py`)
correspond à son ancrage `S[...]`, pas seulement que le total tient dans la durée.

**N6 et N8 sont réutilisables tels quels d'une vidéo à l'autre (copier le .mp3), N7 ne
l'est jamais.** N6 ("vous pouvez aussi le faire depuis Claude...") et N8 (CTA de fin) sont
assez génériques pour s'appliquer à n'importe quel tutoriel — les copier fait gagner un
aller-retour ElevenLabs. N7 nomme l'objet qui vient d'être créé ("...votre X est créé en
quelques secondes") : il est donc *toujours* spécifique au tutoriel. Bug rencontré sur
`foodeatup-fournisseurs-tuto` : N7 copié par réflexe depuis `foodeatup-tva-tuto` disait
encore "...votre taux de TVA est créé...", contenu faux pour cette vidéo — repéré avant
livraison en relisant le SCRIPT.md, corrigé par une régénération ciblée. Toujours relire
le texte de chaque ligne VO copiée avant de l'utiliser, pas seulement sa durée.

Ce même gabarit est aussi la base demandée par Michael pour un usage possible hors vidéo
(pages produit du site web) — les 3 fonctions de rendu du module sont autonomes et
réutilisables telles quelles pour générer des visuels statiques (pas seulement intégrées
à un montage).

## Pièges déjà rencontrés (ne pas reproduire)

- `zoompan` sur vidéo = gel de l'image. Utiliser `setpts` + crop fixe.
- `crop` n'a pas d'option `eval` dans cet ffmpeg — zoom-punch = crop fixe sur
  sous-clip, pas de crop animé par frame.
- Chevauchement de VO (deux lignes en même temps) si les offsets ne sont pas
  poussés séquentiellement.
- Segments vidéo trop rapides par rapport à la VO -> narration qui déborde et
  gonfle artificiellement la carte de sortie. Toujours dimensionner les
  segments sur la durée de la VO correspondante.
- Une branche de travail (`videos/predibot-presentation-6min/`) réapparaît
  parfois de façon intempestive après reset d'environnement — la déplacer vers
  le scratchpad plutôt que la commiter, ce n'est pas lié à cette série.
- Le dépôt n'a pas de branche `main` distincte : la branche désignée EST la
  branche par défaut. Pousser directement dessus, pas de PR à ouvrir contre
  elle-même.
- **`drawbox` ne sait PAS s'animer : sa variable `t` est l'épaisseur du trait,
  pas le timestamp** (contrairement à `drawtext` et `overlay`, où `t` est bien
  le temps). Découvert le 2026-08-03 sur `foodeatup-tracabilite-tuto`. Le
  bandeau d'étape historique (`banner()`) glissait son `x` avec une expression
  en `t` : avec `t=fill`, `t` valait une constante énorme, l'expression se
  figeait hors champ et **les deux `drawbox` (barre orange + boîte bleue)
  n'étaient jamais dessinés**. Seul le `drawtext` du libellé s'affichait — du
  texte blanc sur une UI claire, quasi illisible. Vérifiable sur les vidéos
  déjà publiées de la série (`foodeatup-produits-tuto` t≈4 s) : le bandeau y
  est un fantôme blanc. **Correctif à reprendre pour toute nouvelle vidéo** :
  rendre le bandeau en PNG (PIL, largeur calculée sur le texte) et le faire
  glisser avec `overlay=x='<expr en t>'`, dont le `x` est réévalué à chaque
  frame — voir `banner_png()` / `banner_overlay()` dans
  `videos/foodeatup-tracabilite-tuto/build.py`. Même piège pour l'encadré de
  zoom-punch : la « pulsation » `sin(2*PI*t*2.2)` n'a jamais pulsé, elle se
  résolvait en décalage constant (le rendu restait correct, c'est pourquoi ça
  n'avait pas été repéré) — l'écrire en statique plutôt que de laisser croire
  à une animation.
- **Apostrophe dans un texte de bandeau (`banner()`) = même bug que le `%`
  dans les prompts Claude.** Le texte est injecté entre guillemets simples
  dans l'argument `-vf` (`text='{text}'`) ; une apostrophe dedans (ex. "seuil
  d'alerte") ferme la chaîne prématurément et fait planter tout le filtre
  (`ffmpeg` rapporte une erreur `drawtext` cryptique en fin de chaîne, pas un
  message clair sur l'apostrophe). Rencontré sur `foodeatup-ingredients-tuto`.
  Corrigé en reformulant le bandeau sans apostrophe ("seuil minimum" plutôt
  que "seuil d'alerte") — plus simple que d'échapper le caractère. Vérifier
  chaque texte de bandeau avant build, pas seulement les prompts Claude.
- **`banner()` peut échouer silencieusement : texte affiché, boîte
  orange/bleu invisible, aucune erreur ffmpeg.** Trouvé sur
  `foodeatup-qrcode-tuto` (2026-08-03), confirmé aussi présent sur
  `foodeatup-vitrine-tuto` déjà livrée. Cause : l'évaluateur d'expression de
  `drawbox` (ffmpeg 6.1.1) plante silencieusement (position hors-écran) quand
  le `x` combine un décalage constant en tête (`-640+`) avec DEUX termes
  `min(1,max(0,...))` soustraits (un slide-in, un slide-out) — chaque moitié
  marche isolément, la combinaison non. Fix appliqué : un seul clamp
  `min/max` pour le slide-in, pas de slide-out animé (le fondu-enchaîné vers
  le segment suivant masque déjà la sortie). **Toujours vérifier
  visuellement** (extraire une frame pendant le bandeau, pas juste écouter le
  rendu) plutôt que de faire confiance à l'absence d'erreur ffmpeg — un
  filtre peut « réussir » tout en ne dessinant rien.

- **`drawbox` n'évalue pas `t` dans cet ffmpeg (6.1.1) — le bandeau d'étape ne
  s'affichait pas du tout.** Découvert le 2026-08-03 sur
  `foodeatup-mouvement-stock-tuto`. Un `drawbox` dont le `x` dépend de `t` est
  **silencieusement ignoré** : pas d'erreur, pas de boîte. `drawtext`, lui,
  évalue bien `t` à chaque frame. Le `banner()` historique (2 `drawbox` pour le
  filet orange et la plaque bleue + 1 `drawtext` pour le libellé) ne rendait
  donc **que le texte blanc** glissant sur la capture — vérifié aussi sur le
  MP4 livré de `foodeatup-produits-tuto` : même plaque manquante. Sur une UI
  claire, c'est du blanc sur quasi-blanc, illisible.
  `overlay` est une impasse (même comportement sur son `x`, et il faut boucler
  l'entrée image sinon il ne dure qu'une frame). **Correctif retenu** : le
  bandeau est fait de deux `drawtext` partageant la même expression de
  glissement — la plaque est la `box` de `drawtext` (`boxborderw=16` autour
  d'une ligne de 31 px = exactement la plaque de 62 px de la charte), et le
  filet orange est cette même plaque redessinée 10 px plus à gauche en orange,
  que la plaque bleue recouvre sauf ses 10 px de gauche. Code de référence :
  `videos/foodeatup-mouvement-stock-tuto/build.py`, fonction `banner()`.
  Les 10 vidéos déjà publiées gardent l'ancien rendu — à re-livrer si Michael
  veut rattraper la série.
- **Ne pas supposer un bouton immobile d'un bout à l'autre du rush.** Sur
  `foodeatup-mouvement-stock-tuto`, la page défile de ~158 px dès que le
  tableau se remplit : « Ajouter un mouvement » passe de y=344 à y=186. Mesurer
  les coordonnées sur la frame du clic concerné, pas sur une frame voisine.
