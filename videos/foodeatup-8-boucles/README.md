# Les 8 boucles FoodEatUp — série de 9 vidéos pour l'Academy

Vidéo 0 (« Le principe », 45 s) + 8 vidéos de boucle (80-90 s), chacune rendue en
**master 1920×1080** pour l'Academy et en **reel 1080×1920**.

## Pourquoi ce pipeline et pas HyperFrames

Le brief visait le contrat « Send to HyperFrames ». Trois raisons l'écartent :

1. `compose` et `render_video` du MCP HyperFrames sont **désactivés depuis un
   client CLI** (Claude Code) — le serveur le dit lui-même et renvoie vers les
   skills locaux.
2. Le contrat Send-to vise des compositions **silencieuses de 8 à 25 s**, plafond
   5 s par scène. Ici il faut 85 s narrées.
3. Sa liste de polices bannies contient Inter, Nunito et Poppins — le corps de
   texte de la charte Academy.

On reprend donc le pipeline maison déjà éprouvé sur `videos/boucle-stockvision/` :
composition HTML avec `window.render(t)` déterministe → capture Playwright frame
par frame → assemblage ffmpeg avec la VO. Il produit un MP4 réel, VO incluse, et
évite au passage tous les pièges `drawbox` documentés dans
`videos/FOODEATUP-TUTORIELS-WORKFLOW.md` (aucun filtre ffmpeg n'anime quoi que ce
soit ici : tout le mouvement est calculé dans le navigateur).

## Arborescence

```
boucles.json          manifeste : slug, VO mot à mot, durées, statut, voix figée
visuels.json          ce qui s'affiche à l'écran, plan par plan
mcp-tool-counts.json  comptage réel des outils MCP par boucle
engine/scene.css      la charte Academy, une seule fois pour les 9 vidéos
engine/scene.js       le moteur : 7 gabarits de plan, window.render(t)
assets/fonts/         Fredoka + Inter, inlinées en base64
assets/img/           personnages détourés depuis videos/shared-images/
NN-<slug>/
  index.html          composition master 16:9, auto-portée
  index-reel.html     composition reel 9:16, même timeline
  assets/vo/pNN.mp3   voix off, une piste par plan
capture.cjs           capture Playwright (frames, ou instants de contrôle)
tools/                fetch_fonts · prepare_assets · build_html · check_palette
                      count_mcp_tools
```

## Chaîne de production

```bash
python3 tools/fetch_fonts.py        # une fois — polices inlinées
python3 tools/prepare_assets.py     # une fois — détourage des personnages
python3 tools/count_mcp_tools.py    # une fois — compteurs affichés au plan 3

# 1. VO d'abord : c'est elle qui fixe la durée des plans, jamais l'inverse.
#    Générée via le MCP ElevenLabs, puis récupérée par :
python3 tools/fetch_vo.py <<< '{"01-configuration-boutique": {"p01": "<url>"}}'

# 2. Compositions, calées sur la durée réelle des mp3
python3 tools/build_html.py --exiger-vo
python3 tools/check_palette.py

# 3. Contrôle visuel avant de rendre 2 500 frames
node capture.cjs --html 01-.../index.html --out work/qa --at 4,30,52,72

# 4. Rendu (capture + assemblage + nettoyage des frames)
./render_all.sh boucle-01-configuration-boutique
FORMAT=reel ./render_all.sh boucle-01-configuration-boutique

# 5. Livrables Academy
python3 tools/make_deliverables.py --vignettes
```

`--exiger-vo` fait échouer le build si un mp3 manque : sans lui, `build_html.py`
retombe sur une **estimation** de durée (17,1 caractères/seconde, débit d'Adam
mesuré sur la série) — pratique pour maquetter, jamais acceptable pour un rendu
final.

Les liens rendus par le MCP ElevenLabs sont **signés et valables 15 minutes**.
`fetch_vo.py` les passe tels quels : recomposer la query string, ne serait-ce
que pour réordonner les paramètres, casse la signature et fait télécharger une
erreur XML de 860 octets à la place du mp3.

## Décisions prises, et pourquoi

- **Voix figée** : Adam-Instructor `TGAegA0zNRi8I6nUdq3i`, `eleven_multilingual_v2`.
  C'est déjà la voix du catalogue FoodEatUp (boucle-stockvision, les tutoriels).
  Elle ne change plus d'une vidéo à l'autre.
- **Fredoka** pour les titres, pas Baloo 2 : Fredoka est la police maison du
  studio (remplaçante de Goodly, la vraie police de marque, pas encore fournie)
  et elle est déjà vendorée dans le dépôt. P0 autorisait les deux.
- **Personnages** : repris de `videos/shared-images/characters/`, la librairie
  maison, conformément à sa règle « réutiliser avant de générer ». Ils arrivent
  en RGB sur fond blanc et sont détourés par `tools/prepare_assets.py` — posés
  tels quels sur le crème, ils afficheraient un rectangle blanc.
- **177 outils MCP**, recomptés. Les compteurs par boucle du brief
  (21/18/14/17/22/14/23/17) sommaient à 146 et n'étaient pas vérifiables ; le
  total 177 annoncé côté Lovable, lui, est exact. La répartition réelle est dans
  `mcp-tool-counts.json`, avec le détail outil par outil.
- **ffmpeg** n'est pas installé dans l'image : la chaîne prend le binaire static
  livré par le wheel `imageio-ffmpeg` (7.0.2).

## Publication

Les 9 masters et leurs 9 vignettes sont dans la bibliothèque RapidoCMS, sous les
noms imposés par P9 (`boucle-NN-<slug>-v1` en `video`, `-thumbnail` en `image`).
`manifest-academy.json` porte leurs URLs S3 et les durées mesurées sur les MP4.

**Ne pas se fier au champ `taille` de `list_all_files`** : il vaut `0` pour tout
fichier versé par URL, y compris des uploads antérieurs parfaitement intacts.
Pour vérifier un upload, interroger S3 directement et comparer le
`Content-Length` au fichier local — c'est ce que fait le contrôle de livraison.

Les reels 1080×1920 ne sont pas publiés : P9 ne les demande pas et l'Academy
consomme le master. Ils restent dans le dépôt pour un usage réseaux.

## Écarts au script, à valider

Les VO des boucles 01 à 08 sont **mot à mot** celles des prompts P1-P8, à trois
phrases près, ajoutées parce que le squelette impose 7 plans là où le script en
fournissait 6 :

| Vidéo | Plan | Phrase ajoutée |
|---|---|---|
| 05-ecommerce | 5 | « Fidélité, communication, comptabilité : le même client, la même donnée, d'un bout à l'autre. » |
| 06-communication | 6 | « Trois cent quarante clients prévenus le matin même, et des commandes qu'on sait rattacher à la campagne. » |
| 07-fidelite | 7 | « Sans elle, on rachète chaque client à chaque fois. » |

La VO de **la vidéo 0** est entièrement rédigée ici : le brief en donnait
l'intention (45 s, présenter le principe), pas le texte.

### Durées

Les vidéos font 44 à 76 s, là où le brief visait 45 à 90 s. Adam lit à
**17,1 caractères par seconde**, plus vite que l'estimation initiale. Trois plans
reçoivent de la respiration parce que l'image en a besoin (cascade, chiffres,
CTA — voir `RESPIRATION`) ; le reste n'est pas rembourré. Atteindre les durées
cibles demanderait d'écrire plus de texte, pas d'étirer les blancs.

### Chiffres inventés

Les montants d'ajustement du plan 4 de la boucle 01 (`18,50 € → 19,40 €` et les
deux autres lignes) **ne viennent pas du brief** : le script disait « il vous
propose l'ajustement » sans chiffrer. Ils sont plausibles mais non vérifiés — à
remplacer par de vraies valeurs, ou à basculer en « donnée à confirmer » comme
partout ailleurs où le brief était muet.

## Données manquantes

Les valeurs marquées « donnée à confirmer » dans `visuels.json` ne sont pas des
oublis : ce sont les chiffres que le brief n'a pas fournis et qu'on refuse
d'inventer (coût d'un shift, écarts de caisse, bons émis/utilisés, nombre de
livraisons sans contrôle). Elles s'affichent telles quelles tant que Michael ne
les a pas données.

Deux personnages manquent à la librairie et restent à générer via RapidoCMS :
le « problème » de la boucle 06 (surstock que les clients ignorent) et celui de
la boucle 07 (clients qui ne reviennent pas).
