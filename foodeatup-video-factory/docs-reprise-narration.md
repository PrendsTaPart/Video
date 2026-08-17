# Prompt de reprise — poser la narration sur le film UpEatFood

À coller tel quel au démarrage d'une session Claude Code neuve.

---

Termine la narration du film UpEatFood et intègre-la au montage.

## Le worktree

`/tmp/claude-0/-home-user/e0e434d2-ea78-5570-94a6-9f2649fd6572/scratchpad/factory-wt`,
branche `claude/foodeatup-video-factory-wtb7gs`. S'il a disparu, le recréer
depuis `/home/user/Video` sur cette branche. **Commence par `git pull`** : une
autre session travaille sur la même branche et a déjà poussé sept commits
pendant la précédente.

Lis `foodeatup-video-factory/VEILLE.md` avant d'agir.

## Ce qui est déjà fait

Le film est monté : `dist/film/upeatfood.mp4`, 375,141 s, 1920 × 1080,
35 chapitres sur 35, cinq saisons. Logo animé, carton de titre, un carton par
saison, générique de fin. Il ne lui manque que la voix.

La voix est choisie et validée par l'utilisateur : **Bass — Warm, Deep
Storytelling**, `voice_id` = `wQjKP9DkO6pDLKdaqFn6`, modèle
`eleven_multilingual_v2`. Ne la remets pas en question, elle a été comparée à
deux autres sur la première réplique du film.

Deux fichiers d'état portent tout le reste :

- `state/narration-film.json` — les **66 répliques**, chacune avec sa clé
  (`EP501-conteur`, `EP501-personnage`, …), son **minutage absolu dans le film**
  (`t`, en secondes) et son texte.
- `state/narration-sessions.json` — le `flow_id` ElevenLabs
  (`TpOBoQbfuLKgs07pdYrR`) et les **16 répliques déjà lancées**, par clé.

## Le piège à ne pas reproduire

`assets/voix/conteur-film.mp3` **n'est pas la narration du film**. C'est
l'échantillon de casting de Bass — une seule phrase, 5,98 s — qu'une session
précédente a pris pour la piste finale et posée sur 375 s de film. Vérifié par
somme de contrôle : il est identique au fichier de démonstration.

`build-habillage.py` lit ce fichier. Tant qu'il n'est pas remplacé par la vraie
piste, tout habillage régénéré reproduira l'erreur. **Remplace-le, ne le
contourne pas.**

## Ce qu'il reste à faire

**1. Générer les 50 répliques manquantes.**

Une par appel `creative_generate_speech`, `generations_count: 1`, en passant le
`flow_id` existant. Après **chaque bloc**, écris les `session_id` dans
`state/narration-sessions.json` : le serveur ElevenLabs s'est déconnecté trois
fois pendant la session précédente, et un lot perdu est un lot à repayer.

**2. Récupérer les 66 fichiers.**

`creative_get_flow_run_status` avec le `flow_id` et les `session_ids` renvoie
les URL. Télécharge dans `assets/vo/film/<clé>.mp3`.

**3. Assembler la piste.**

Écris `scripts/build-narration-film.py`. Il lit `state/narration-film.json`,
pose chaque mp3 à son `t` sur un lit silencieux de la durée du film, et écrit
`assets/voix/conteur-film.mp3`. En ffmpeg : un `adelay` par réplique puis un
`amix`, ou `aresample` + `apad`. Sortie 48 kHz stéréo.

**Contrôle indispensable avant de mixer** : les 66 minutages ont été calculés à
partir des constantes de `build-film.py` — `T_LOGO` 4 s, `T_TITRE` 3,5 s,
`T_SAISON` 2 s, 10 s par chapitre. Si le film livré vient d'un autre script,
ces repères sont faux et chaque réplique tombera sur le mauvais plan. Vérifie
d'abord que la durée totale attendue par le calcul correspond bien à 375,141 s,
et contrôle à l'œil qu'une réplique connue tombe au bon endroit — par exemple
`EP501-conteur` à 10,0 s, la première du film.

**4. Mixer.**

`python3 scripts/build-film.py --narration assets/voix/conteur-film.mp3`

Le script gère déjà les trois pistes : ambiance à 0,42, musique à 0,30, voix à
1,0, puis `loudnorm` à −16 LUFS et limiteur. Les gains d'entrée sont bas
volontairement pour que la somme ne dépasse pas la pleine échelle — ne les
remonte pas.

**5. Vérifier l'audio plutôt que l'affirmer.**

```
ffmpeg -hide_banner -nostats -i dist/film/upeatfood.mp4 -af astats=metadata=1 -f null -
```

Le **facteur de platitude doit rester à 0,000000**. Un écrêtage laisse des
suites d'échantillons figés en butée ; c'est le seul indicateur fiable, le pic
seul ne dit rien parce que l'encodeur AAC dépasse la consigne du limiteur d'un
décibel environ.

**6. Envoyer pour validation.**

Le master fait 86 Mo, au-dessus de la limite d'envoi de 30 Mo. Fabrique une
épreuve : `-vf scale=1280:720 -crf 30 -b:a 96k` donne environ 14 Mo.

## Les règles du dépôt

- **Ne génère RIEN sur Higgsfield.** Seuls `show_generations` et
  `show_generation_by_ids` sont autorisés. S'il manque un plan, donne le prompt
  à l'utilisateur.
- **Brouillons seulement** sur les réseaux, jamais de planification sans accord
  explicite.
- **RapidoCMS d'abord** pour l'hébergement.
- N'assouplis jamais l'appariement de la veille pour ramener plus de prises.

## Deux pièges de terrain

**Le disque.** La machine précédente finissait à 3,2 Go libres sur un dépôt de
34 Go. Si `git gc` s'interrompt faute de place, il laisse des
`.git/objects/pack/tmp_pack_*` de plusieurs gigaoctets, référencés par rien et
supprimables sans risque.

**Les fichiers générés.** `src/data/series.ts` et `src/data/contenu.ts` du
projet Lovable sont produits par `gen-site-data.py`. Tout ce que Lovable y
ajoute à la main disparaît à la régénération suivante — c'est arrivé quatre
fois : l'en-tête de types, `texteDe`, la liste des réseaux avec WhatsApp, et le
typage de `publications`. Avant toute régénération, repars de l'en-tête de
`origin/main` et corrige dans **le gabarit du générateur**, jamais dans le
fichier produit.

## Ce qui reste après ça

- La voix de punchline d'EP524 — `assets/vo/punchlines/EP524.mp3` manque, son
  générique de fin est muet là où les 34 autres parlent.
- Le film en hero sur l'accueil et sur la page de la série : `film.url` et
  `film.duree` sont posés côté donnée, il reste le code Lovable.
- Le générique de 5 s : le prompt Higgsfield est chez l'utilisateur.
- La reconstruction des Shorts, Facebook et TikTok sur les stories corrigées —
  hors les 24 de la semaine du 19 au 31 août, déjà refaites. Environ cinq heures
  de rendu et 3,4 Go d'objets git.
