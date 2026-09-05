# Reprendre la série « Michael remonte le temps »

Ce fichier est fait pour qu'un agent qui n'a rien vu de la conversation précédente puisse
monter l'épisode suivant sans rien casser, et surtout **sans que l'animation change d'un
épisode à l'autre**. C'est le seul document à lire avant de commencer.

**Dépôt** : `PrendsTaPart/Video` · **Branche** : `claude/gutenberg-episode-montage-r5cnjf`

---

## Deux règles qu'on ne discute pas

**1. On ne génère aucune vidéo.** Les plans existent déjà dans la bibliothèque Higgsfield ;
on les récupère par MCP (`show_generations`, type `video`) et on les télécharge. Si un plan
manque, on ne l'invente pas : on donne le prompt à l'utilisateur pour qu'il le génère
lui-même. C'est écrit dans le `CLAUDE.md` à la racine du dépôt, et c'est répété dans chaque
brief d'épisode.

**2. La règle des soixante secondes.** Elle s'applique à tous les épisodes, quoi qu'annonce
le brief — les briefs sont écrits en 45 s, ils datent d'avant la règle.

| Bloc | Durée | Timecode |
|---|---|---|
| Film Higgsfield | 30 s | 00:00 → 00:30 |
| Transition « COUPEZ » | 3 s | 00:30 → 00:33 |
| Méthode — les cinq étapes | 20 s | 00:33 → 00:53 |
| Hook de fin — la punchline | 7 s | 00:53 → 01:00 |

`npm run verifier` refuse un épisode dont un bloc a changé de durée.

---

## Ce qui existe

| Dossier | Quoi |
|---|---|
| `videos/module-methode-rapidocms/` | **le commun de la série** : gabarit animé, montage, contrôles, voix des étapes, SFX |
| `videos/s01e01-colomb/` | S01E01 « Il cherchait le poivre. » — Christophe Colomb |
| `videos/s01e02-gutenberg/` | S01E02 « Un livre, deux ans » — Gutenberg |
| `videos/s01e03-cleopatre/` | S01E03 « Le visage qu'elle a choisi » — Cléopâtre |

Les trois sont montés, vérifiés et poussés. **Prendre `s01e03-cleopatre` comme modèle** :
c'est le plus récent et le plus complet.

L'historique contient un commit « variante 50 s » (`352edb4`) : c'est un état intermédiaire,
abandonné quand la règle des 60 s est arrivée. Il n'en reste rien dans l'arbre, ne pas
chercher à le réactiver.

---

## Ce qui ne doit JAMAIS changer d'un épisode à l'autre

C'est le cœur de la question. L'animation est identique partout, et elle le reste parce que
tout le monde tape dans le même module.

- **Le gabarit** `module-methode-rapidocms/animation.html`. Ne pas le copier dans un épisode,
  ne pas le forker. Le modifier change la série entière — c'est voulu, mais il faut alors
  refaire tous les épisodes déjà montés.
- **Le montage** `module-methode-rapidocms/scripts/monter.mjs` et les contrôles
  `verifier.mjs`. Les scripts d'un épisode ne sont que des pilotes de quelques lignes.
- **Les six lignes de voix off des étapes** : `module-methode-rapidocms/audio/vo-etapes-2a7.wav`,
  déjà calées sur les trente secondes de la queue. **Ne jamais les regénérer** — ça coûte des
  crédits et, surtout, ça fait varier le timbre au milieu du film.
- **La voix.** Toute ligne générée pour un épisode doit l'être avec :
  - modèle `eleven_multilingual_v2`
  - voix `ecxPjiGTvAfpGEams6ec` — *Paul K — French Ad & Trailer Voice*

  Une autre voix s'entend immédiatement, au milieu du module.
- **Les logos** : `assets/logos/` se copie tel quel d'un épisode à l'autre, provenance dans
  `assets/LOGOS.md`. Jamais redessinés.
- **La charte** : fond `#F2F4F7`, bleu `#03A9F5`, violet `#7E57C2`, texte `#383838`.
  Réseaux : Facebook `#1877F2`, Instagram `#E1306C`, TikTok `#000000`, LinkedIn `#0A66C2`,
  YouTube `#FF0000`.

## Ce qui change à chaque épisode

Quatre choses, pas une de plus :

1. **Le numéro de séquence sur l'ardoise** (`queue.blocs.transition.sequence`) et le titre,
   qui vient de `titre`.
2. **La ligne d'ouverture** — 2 s, créneau 33 → 35.
3. **La punchline du hook** — 5 s, créneau 53,8 → 58,8. Patron de série :
   « Lui/Elle, [le fait du film]. Vous, vous avez RapidoCMS. »
4. **Tout le bloc film** : plans, accroche, sous-titres, accent, incrustation produit.

Soit **deux lignes ElevenLabs par épisode**, une dizaine de centimes.

---

## Monter l'épisode suivant, pas à pas

```bash
# 1. partir du plus récent
cp -r videos/s01e03-cleopatre videos/s01eNN-slug   # puis vider source/ audio/ deliverable/ work/
cd videos/s01eNN-slug && npm install
```

2. **Trouver les plans.** `mcp__Higgsfield__show_generations` avec `type: "video"`. Les plans
   de la série se reconnaissent au préfixe commun du prompt (« Prise de vue à la perche »,
   « @michael ») et à la ligne `2. @<produit>` qui nomme le produit de l'épisode.
   Télécharger les trois `results.rawUrl` dans `source/`.
   **Vérifier qu'ils font bien 720×1280** : le champ `aspect_ratio` des paramètres ment
   parfois (il dit 16:9 sur des fichiers verticaux), c'est le fichier qui fait foi.

3. **Écrire `episode.json`.** Copier celui de l'épisode 3 et remplacer : `id`, `slug`,
   `titre`, les trois `clips`, `accroche`, `sous_titres`, `accent`, `incrustation_produit`,
   `faits`, `exports`, `vignette`, et dans `queue` : la `sequence` et les deux `vo`.

4. **Générer les deux lignes** avec la voix ci-dessus, les déposer en
   `audio/vo-ouverture.mp3` et `audio/vo-hook.mp3`.

5. **Relever le suivi du produit** (voir plus bas), puis :

```bash
npm run queue      # les deux lignes + 900 images de queue  (~1 min 30)
npm run monter     # film + queue, niveaux, exports, vignette  (~4 min)
npm run verifier   # structure, format, durée, niveau, coupes, sous-titres
npm run build      # les trois à la suite
npm run queue -- --apercu 31,34,44,55    # juste des images, pour juger sans tout rendre
```

6. **README de l'épisode** sur le modèle des trois autres, puis commit et push sur la branche.

---

## Les pièges, tous rencontrés pour de vrai

**ffmpeg n'est pas installé sur la machine.** Celui livré avec Playwright est amputé (pas de
libx264, pas d'AAC, pas de muxer mp4). Le paquet npm `ffmpeg-static`, déjà dans le
`package.json` de chaque épisode, en fournit un complet. `ffprobe` n'existe pas : `sonder()`
dans `scripts/outils.mjs` lit ce que ffmpeg écrit sur sa sortie d'erreur.

**Ne pas faire confiance aux timecodes du brief : les mesurer.** Sur trois épisodes, deux
étaient faux.
- E02 : l'accent annoncé à 16,4 s tombait bien sur un transitoire — gardé.
- E03 : l'accent annoncé à 12,6 s tombait dans le vide, les coups de marteau étant à 11,5 et
  11,9 s. Recalé sur 11,9.
- E03 : la fenêtre du produit s'ouvrait à 24 s alors que l'objet entre dans le cadre à 27 s.

  Comment mesurer un transitoire : découper le plan en tranches de 0,1 s et lire
  `volumedetect` sur chacune, puis prendre le maximum dans la fenêtre visée.

**Le niveau sonore se cale bloc par bloc, jamais sur l'assemblage.** Le film sort de
Higgsfield entre −24 et −26 LUFS, la queue est mixée vers −15. `monter.mjs` mesure chaque
bloc en EBU R128 et le cale à −14 **avant** de les coller. `loudnorm`, même en deux passes,
ratait la cible de 3 dB : ne pas y revenir.

**Le suivi de l'incrustation produit.** Deux méthodes, selon ce que montre le plan :
- *à la couleur*, avec `module/scripts/suivre-couleur.mjs`, quand l'objet porte un repère
  franc (la bouteille de sauce de l'épisode 1). Le garde-fou de taille écarte une boîte qui
  a avalé le décor.
- *à l'œil*, quand il n'y a rien à suivre : le cuir sombre du livre (E02), le sceau de cire
  noyé dans la lumière du brasero (E03). On relève sur trois images, on écrit les points
  dans `episode.json`, et le script de l'épisode les **redessine** pour qu'on puisse juger.

  Dans les deux cas : vérifier que le plan est vraiment fixe sur la fenêtre. Sur E02 il ne
  l'était pas — le livre descend de 90 px.

**La hauteur des sous-titres dépend du produit.** `incrustation_produit.y_soustitre` : 1440
sur E01, 1250 sur E02, 1110 sur E03. Le produit occupe le bas du cadre et l'incrustation de
l'annonceur s'y pose : un sous-titre trop bas tombe dessus. **Le vérifier en montant un
emblème d'essai**, c'est comme ça que le défaut a été trouvé sur E03.

**Aucune marque annonceur n'a jamais été fournie.** Les trois épisodes livrent donc le
produit vierge, et c'est ce que demandent les briefs. Le mécanisme attend son image :
déposer une PNG à fond transparent au chemin qu'indique `incrustation_produit.fichier`.
Avec `relief: true` elle est posée comme pressée dans la matière — copie sombre floutée
décalée de 5 px, emblème à 82 %.

---

## Points ouverts, à ne pas trancher seul

- **Le catalogue.** Les briefs demandent de déclarer l'épisode « monté dans RapidoCMS, les
  cinq réseaux en `a_venir` ». Ce vocabulaire est celui du catalogue Social, pas de
  RapidoCMS qui gère campagnes et posts ; et la série n'existe dans aucun des deux. La
  question a été posée à l'utilisateur, la réponse est « on verra plus tard ». **Ne rien
  écrire dans l'un ni dans l'autre sans le lui redemander.**
- **Les punchlines de fin sont écrites par l'agent**, sur le patron de série, faute de texte
  fourni. Idem le CTA « FAITES LA VÔTRE » sous le logo (pas d'URL, faute d'en connaître une).
  À faire valider.
- **Les réglages de voix du brief** (stability 0,45 · similarity 0,80 · style 0,25 · speaker
  boost) ne sont pas applicables : l'outil MCP ElevenLabs n'expose ni stabilité, ni
  similarité, ni style. Ils restent écrits dans les `episode.json` pour une prise refaite
  depuis l'interface.
- **La nappe** `s01e01-colomb/assets/musique/nappe-methode.mp3` est empruntée à
  `videos/planit-product-launch`, faute d'une nappe propre à la série.
- **Arial n'est pas installée** : c'est Liberation Sans qui rend, mêmes métriques.

---

## L'épisode 4 semble amorcé

La bibliothèque Higgsfield contient un plan `6ce269c1` — « Michael, peintre d'écriteaux,
seul dans un atelier ouvert sur une cour romaine », référence produit `@amphore`, 720×1280.
C'est le clip 1 d'un épisode romain qui n'a pas encore de brief. Les clips 2 et 3
n'existaient pas au moment d'écrire ces lignes : les rechercher avant de conclure quoi que
ce soit.
