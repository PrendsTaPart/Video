# Série tutoriels — état de production

Suivi des 30 vidéos décrites dans `SCRIPTS-HEYGEN-30.md`. Chaque vidéo suit la structure
validée sur `v01-fidelite/` : hook → problème → démo (logiciel + avatar par-dessus) →
punchline.

## Le son (revu le 2026-08-10)

Michael : « il manque la voix off au début de chaque vidéo et pendant la séquence
Higgsfield », « les vidéos Higgsfield en mute », « toute la vidéo doit avoir du son ».
Trois couches audio, donc plus aucun silence :

| Piste | Contenu | Niveau |
|---|---|---|
| 8 | lit d'ambiance continu (`planit-ambient-pad.mp3`), fondu de sortie sur la dernière seconde | ~20 dB sous la voix |
| 10 | voix off du hook | −16 LUFS |
| 11 | voix off du bloc problème | −16 LUFS |
| 12 | voix de l'avatar, puis voix off de la punchline | −16 LUFS |

Les plans Higgsfield sont montés **sans aucune piste audio**.

Toutes les voix sont passées au `loudnorm` **−16 LUFS** avant montage : les sorties
ElevenLabs arrivaient ~8 dB sous la voix des clips HeyGen, ce qui obligeait à monter le son
au début puis à le baisser à l'arrivée de l'avatar. Les fichiers normalisés sont dans
`motion/assets/audio/norm/`, les originaux à côté.

Le bloc démo est aussi resserré : il dure maintenant la réplique de l'avatar + 2 s, au lieu
de 14 s fixes. Le logiciel ne tourne plus 4 s en silence après la fin de la voix.

## Montées (6 / 30)

| # | Projet | Durée | Avatar HeyGen | Vidéo logiciel (fenêtre) |
|---|---|---|---|---|
| 01 | `t01-ingredients/` | 28,4 s | `gen-1` (10,22 s) | `foodeatup-ingredients-tuto` · 85→97 s |
| 02 | `t02-recettes/` | 28,3 s | `gen-2` (12,14 s) | `foodeatup-recettes-tuto` · 74→88 s |
| 03 | `t03-fournisseurs/` | 27,4 s | `gen-3` (9,24 s) | `foodeatup-fournisseurs-tuto` · 44→55 s |
| 04 | `t04-mes-commandes/` | 25,4 s | `gen-4` (9,24 s) | `foodeatup-mes-commandes-tuto` · 20→31 s |
| 05 | `t05-mcp-claude/` | 27,6 s | `gen-5` (9,35 s) | `foodeatup-mcp-tuto` · 30→41 s |
| 06 | `t06-employes/` | 27,7 s | `gen-6` (9,47 s) | `foodeatup-employes-tuto` · 38→49 s |

Les fenêtres du logiciel ont été choisies en échantillonnant chaque rush : elles couvrent le
geste utile **et** sa confirmation à l'écran (« Succès ! Ingrédient ajouté », tableau des
ingrédients avec coût total, fiche fournisseur créée, commande créée + liste multicanal).

Les durées diffèrent d'une vidéo à l'autre parce que chaque bloc est calé sur la durée réelle
de son contenu (voix off, réplique de l'avatar, plan disponible). C'est voulu, pas un oubli.

## Réserve restante sur les plans problème

Deux écarts par rapport à la vidéo 1 validée. (Le silence du bloc problème, qui en était un
troisième, est réglé : la voix off le couvre désormais.)

1. **Format** — les plans `hero-video/` sont en 1280 × 720 paysage. Ils sont montés en
   pillarbox (plan centré sur un fond flouté tiré de lui-même) : regardable, mais en
   dessous d'un plan nativement vertical.
2. **Visage** — c'est le personnage IA « Karim » du film héros, pas la photo de Michael
   utilisée dans la vidéo 1.

Même correctif pour les deux : générer les plans problème en **9:16 natif, 8 s, référence =
photo de Michael**, avec les prompts du plan principal. Les montages se mettent alors à jour
par simple remplacement de `assets/higgsfield/probleme.mp4` et re-rendu — rien d'autre à
refaire.

## Rendre à nouveau une vidéo

```bash
cd videos/foodeatup-cas-concrets/t01-ingredients
npx hyperframes check .
npx hyperframes render . -q high -o renders/video-t01-ingredients.mp4
```

## Produire les suivantes

Le carton hook est paramétrable — plus besoin d'une composition par vidéo :

```bash
cd videos/foodeatup-cas-concrets/motion
npx hyperframes render . -c compositions/hook-card.html -q high \
  -o renders/hook-t05.mp4 \
  --variables '{"num1":"…","rest1":"…","num2":"…","rest2":"…"}'
```

Puis le générateur d'assemblage :
`build_videos.py` (une entrée par vidéo dans la liste `VIDEOS`, puis
`npx hyperframes render`). Il calcule seul la hauteur d'affichage du logiciel à partir des
dimensions réelles du rush, et cale l'avatar sur sa durée réelle.

## Clips HeyGen restants

24 sur 30. Ils arrivent par lots dans `_heygen-inbox/` — voir son README pour la convention
de nommage et le contrôle qualité appliqué à chaque clip.

**Attention aux doublons** : sur les 8 fichiers reçus jusqu'ici, 2 étaient des renvois d'un
clip déjà fourni (vérifié par hash md5). Le lot du 2026-08-10 annonçait 3 clips mais n'en
contenait que 2 nouveaux — le troisième était le clip 03 re-téléchargé, ce qui laisse penser
que le **script 07 (Contrat & salaire) n'a pas encore été généré**.

## Ce qu'il reste à faire pour chaque nouvelle vidéo

Le seul travail manuel restant par vidéo est d'écrire deux phrases (voix off du hook, voix
off du problème) puis de les générer. Tout le reste est automatisé :

1. Ajouter une ligne dans `VIDEOS` (`build_videos.py`) : plan problème, projet tuto, fenêtre,
   clip avatar, durée.
2. Rendre le carton hook avec `--variables`.
3. Générer les 2 voix off (ElevenLabs, voix Adam `TGAegA0zNRi8I6nUdq3i`), les normaliser à
   −16 LUFS dans `motion/assets/audio/norm/`.
4. `python3 build_videos.py` puis `npx hyperframes render`.

## Fenêtres logiciel déjà repérées pour les prochaines vidéos

Repérées en échantillonnant les rushes, pour que le montage suive dès l'arrivée du clip
avatar. Chaque fenêtre couvre le geste **et** sa confirmation à l'écran.

| # | Projet tuto | `media_start` | Ce qu'on voit |
|---|---|---|---|
| 07 | `foodeatup-contrat-tuto` (66 s) | 52 | fin du formulaire → « Créer le contrat » → fiche salaire enregistrée (brut, transport, congés) |
| 08 | `foodeatup-planning-poste-tuto` (83 s) | 48 | grille hebdo colorée par poste → « Enregistré » → export PDF du planning |
| 09 | `foodeatup-taches-tuto` (85 s) | 58 | tâche assignée à un créneau → « Enregistré » → ligne dans « Tâches de la semaine » |
