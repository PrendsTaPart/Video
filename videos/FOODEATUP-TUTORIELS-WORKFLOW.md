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
   - Audio final : `loudnorm=I=-16:TP=-1.5:LRA=11` + `alimiter=limit=0.89` pour
     éviter tout clip. Vérifier au `volumedetect` (`mean` ~-16dB, `max` < 0dB).
   - Durée cible générale : éviter les blancs, viser le minimum nécessaire pour
     porter le script sans traîner (30-60s typiquement selon la complexité du
     flow ; suivre les instructions ponctuelles de Michael sur la durée).

5. **Intégration de l'image d'ouverture en tant que vignette YouTube**
   **Ne jamais recréer/redesigner une vignette.** Utiliser directement l'image
   d'ouverture fournie par Michael (`assets/intro.jpg`), simplement redimensionnée
   si besoin au format YouTube (1280x720, JPG, <2 Mo) sans recadrage créatif —
   uniquement un `scale`+`crop` neutre si le ratio source diffère légèrement.
   Livrable : `out/thumbnail-youtube.jpg`.

6. **Publication sur le CMS**
   - Commit + push du dossier projet (`assets/`, `vo/`, `build.py`, `out/`) sur
     la branche désignée (`work/` reste dans `.gitignore`, c'est du scratch).
   - Upload de la vidéo finale ET de la vignette sur RapidoCMS
     (`mcp__RapidoCMS__upload_file_tool`, en pointant l'URL GitHub raw du fichier
     poussé).
   - Livrer le fichier vidéo à Michael (SendUserFile).

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
