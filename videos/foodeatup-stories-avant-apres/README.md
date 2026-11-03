# FoodEatUp — 9 stories Avant/Après + signature

Montage prêt à recevoir les clips au fur et à mesure que tu les génères sur
Higgsfield. **Je ne génère jamais de vidéo ici** (règle du dépôt, voir
`../../CLAUDE.md`) : `PROMPTS.md` contient les 19 prompts à coller toi-même
dans Higgsfield ; mon rôle se limite à récupérer les clips terminés et à les
monter avec ffmpeg.

## Workflow

1. Tu génères un clip sur Higgsfield, en le nommant **exactement** comme dans
   `PROMPTS.md` (ex. `story-04-cuisine-pendant-service-sans`).
2. Une fois qu'il est dans ta bibliothèque RapidoCMS, dis-le-moi (ou demande
   un état des lieux) — j'appelle `list_all_files` côté RapidoCMS, je
   télécharge ce qui est prêt dans `clips/`, et je te dis quelles stories
   sont désormais montables (les deux volets — `-sans` et `-avec` —
   doivent être présents).
3. Dès qu'une story a ses deux clips, je la monte et le fichier final
   apparaît dans `out/story-XX.mp4`. Une story incomplète est **reportée**,
   jamais bricolée avec un plan de remplacement.

## Structure

```
manifest.json     spec des 10 stories (textes, thème, moment, palette, sortie)
PROMPTS.md        les 10 prompts Higgsfield (bloc commun + moitié haute/basse) + nommage exact
clips/            clips sources téléchargés depuis RapidoCMS (jamais modifiés)
out/              stories finales : story-01.mp4 … story-10.mp4
work/             scratch ffmpeg (gitignored, régénérable)
assets/fonts/     Baloo 2 (converti en .ttf depuis studio-video, pour les bandeaux drawtext)
assets/endcard/   carton FoodEatUp conforme, une fois la source confirmée (voir ci-dessous)
scripts/
  common.py         constantes + helpers ffmpeg partagés
  inventory.py       état des lieux clips présents / manquants
  fetch_clips.py      télécharge les clips prêts sur RapidoCMS vers clips/
  build_story.py       monte une story split-screen (1 à 9)
  build_signature.py    monte la story 10 (plein cadre, pas de split)
  endcard.py            conforme le carton final (2s, 1080x1920, 24fps)
  build_all.py           monte tout ce qui est prêt + imprime le rapport de livraison
```

## Montage — ce que fait `build_story.py` pour chaque story 1-9

- Chaque clip source (carré 1:1) est mis à l'échelle puis recadré au centre
  en 1080×958 (jamais déformé). Si un clip n'est pas carré, un avertissement
  s'affiche au lieu d'un étirement silencieux.
- `-sans` en haut, `-avec` en bas, un liseré crème `#FCF9E6` de 4 px à la
  jonction (958 + 4 + 958 = 1920).
- Bandeau supérieur (texte "avant" de la story) : Baloo 2 bold, blanc sur
  voile marine `#0F1A23` à 70 %, dans les 250 premiers px (zone de sécurité
  Instagram).
- Bandeau inférieur (texte "avec") : même traitement, voile bleu `#007BFF`,
  dans les 250 derniers px.
- Audio : les deux pistes sources sont mixées et normalisées à -16 LUFS ; si
  aucune des deux n'a de son exploitable, la piste de sortie reste du
  silence (pas d'absence de piste, pour rester compatible avec le carton).
- 2 secondes de carton FoodEatUp ajoutées à la fin.

`build_signature.py` fait la même chose pour la story 10, mais sans split :
plein cadre 9:16, les deux textes ("Avant. Pendant. Après." puis "Un seul
outil pour les trois.") apparaissent l'un après l'autre plutôt qu'en deux
bandeaux simultanés, puis le même carton.

## Carton final — à confirmer avant le premier montage complet

`manifest.json` → `endcard.source` est **`null`** tant que tu ne m'as pas dit
quel fichier utiliser. Tant que c'est le cas, `build_story.py` /
`build_signature.py` construisent le corps de la story dans `work/` mais
**n'écrivent rien dans `out/`** — conformément à la consigne : je ne
fabrique jamais un carton, je m'arrête et je demande. Voir la question que
je t'ai posée en fin de session pour les candidats trouvés dans le dépôt.

Une fois la source choisie, mets à jour `manifest.json` :
```json
"endcard": { "seconds": 2, "source": "/home/user/Video/<chemin-vers-le-fichier>" }
```

## Lancer le montage

```bash
cd videos/foodeatup-stories-avant-apres/scripts
python3 inventory.py                 # état des lieux local
python3 fetch_clips.py dump.json     # après avoir sauvegardé un export list_all_files
python3 build_all.py                 # monte tout ce qui est prêt + rapport
```

Pipeline vérifié de bout en bout avec des clips de test synthétiques
(mire ffmpeg + carton factice) avant d'être livré : split-screen, liseré,
bandeaux Baloo 2 et concat du carton fonctionnent. Aucun clip réel n'a été
généré pour cette validation.
