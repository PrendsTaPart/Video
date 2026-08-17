# La veille — monter et publier sans jamais générer

Cette procédure est faite pour tourner seule, à intervalle régulier, dans une
session Claude Code neuve. Elle ramasse les plans que **vous** avez générés à la
main dans l'interface Higgsfield, les monte et les publie.

Elle ne génère rien. C'est la règle du dépôt, et c'est aussi ce qui rend
l'automate sûr à laisser tourner : le pire qu'il puisse faire est de ne rien
trouver.

## Le tour complet

### 1. Lire l'historique Higgsfield

```
show_generations(type="video", size=50)
```

Rappeler avec le `next_cursor` renvoyé jusqu'à ce qu'il soit `null`, ou jusqu'à
dépasser la date du dernier passage (`state/veille.json`, champ `jobs_lus`).
Chaque réponse est trop grosse pour le fil : le harnais l'écrit dans un fichier,
c'est ce chemin qu'on garde.

**Outils autorisés ici : `show_generations` et `show_generation_by_ids`, rien
d'autre.** Tout `generate_*` est interdit — voir `CLAUDE.md`.

### 2. Rapprocher

```bash
python3 scripts/veille-higgsfield.py <page1.json> <page2.json> …
```

Écrit `state/veille.json` : ce qui est nouveau, ce qui est déjà servi, ce qui
reste attendu.

L'appariement se fait sur les répliques entre accolades du prompt, et il est
strict — toutes les répliques attendues doivent être là, et un plan de
bande-annonce ne peut pas servir d'épisode. Cette sévérité vient d'un accident :
un appariement laxiste a publié la bande-annonce d'UpEatFood à la place de
l'épisode EP535, les deux partageant la phrase « Il était une fois un
restaurant. ». **Ne pas assouplir ce test pour faire remonter davantage de
prises.** Une prise non reconnue attend ; une prise mal rapprochée se publie.

### 3. Récupérer

Pour les épisodes :

```bash
./scripts/fetch-hooks.sh EP503 EP504 …
```

Pour les bandes-annonces, les URL sont dans `state/veille.json` — les déposer
dans `assets/bandes-annonces/<serie>-S<n>.mp4`.

Les URL de CDN Higgsfield **expirent**. Ce qui est récupéré est donc commité :
`dist/hooks/`, `dist/bandes-annonces/`. Un fichier commité ne disparaît pas.

### 4. Retirer la voix du plan

Seedance prononce les répliques écrites dans le prompt : chaque plan arrive avec
une voix française incrustée. Partout où le montage pose ensuite une voix
ElevenLabs — la réplique d'une bande-annonce, la punchline d'un chapitre du film
— on en entendrait deux.

```bash
python3 scripts/enlever-voix.py bandes-annonces
python3 scripts/enlever-voix.py hooks EP5xx …
```

Ne le faire **que** pour ces deux familles. Les stories de la série comique
n'ont pas de voix off : leur hook et leur punchline sont incrustés en texte, la
voix du plan est le seul contenu parlé et la retirer les viderait.

Compter une vingtaine de secondes par plan. Le résultat est commité
(`assets/*-sans-voix/`, ~200 ko pièce) pour ne pas refaire tourner Demucs.

### 5. Monter

| Ce qu'on monte | Commande |
|---|---|
| Story d'un épisode de la série comique | `python3 scripts/build-stories.py EPxxx` |
| Story d'un chapitre du film UpEatFood | `python3 scripts/build-film-stories.py EPxxx` |
| Master 37,5 s | `./scripts/build-episode.sh EPxxx` |
| Bande-annonce de saison + affiche | `python3 scripts/build-bandes-annonces.py <serie>-S<n>` |
| Short YouTube d'un épisode | `python3 scripts/build-youtube.py EPxxx` |
| Vidéo YouTube paysage | `python3 scripts/build-youtube-paysage.py EPxxx` |
| Story Facebook | `python3 scripts/build-facebook.py EPxxx` |
| Vidéo TikTok | `python3 scripts/build-tiktok.py EPxxx` |

Ne pas se tromper de script entre les deux premiers : un chapitre du film porte
`story.motion` et n'a ni badge permanent ni punchline incrustée. `build-stories.py`
le détecte et refuse, en indiquant le bon script — le suivre.

Le Short YouTube se monte **après** la story, dont il est la suite : la même
image, plus un carton de fin de deux secondes et demie qui pose le titre, la
série et la chaîne. YouTube est le seul réseau où la vidéo se cherche au lieu
d'être croisée dans un fil ; s'y arrêter sur la punchline, sans rien dire de la
série, laisse le spectateur sans suite. Relancer `build-youtube.py` après avoir
remonté une story : le Short ne se met pas à jour tout seul, il faut supprimer
le fichier de `dist/youtube/` pour qu'il soit refait.

YouTube veut les deux formats. Le Short vertical va dans l'onglet Shorts ; la
page de la chaîne, la recherche et la lecture sur téléviseur sont en paysage,
où un plan vertical arrive entre deux bandes noires. `build-youtube-paysage.py`
part de la même story, pose le plan en pleine hauteur au centre d'un cadre
1920 × 1080 et comble les côtés d'une copie floutée — le traitement des
vignettes `EPxxx-16x9.jpg`. Ces vignettes sont d'ailleurs la miniature de la
vidéo : le site les sert par `vignetteEpisode(id, "youtube")`, il n'y a rien à
poser dans la donnée. Même règle de reprise que le Short : supprimer le fichier
de `dist/youtube-paysage/` pour le refaire.

Facebook et TikTok sont le même moule encore. Même image et même cadre que le
Short ; seul le carton change, parce que seul change ce que le spectateur peut
faire à la fin. YouTube donne le nom de la chaîne et TikTok celui du compte —
tous deux cliquables depuis leur lecteur. Facebook donne l'appel à l'action et
l'adresse du site en toutes lettres : une vidéo native y est repartagée sans sa
légende, et le lecteur ne propose aucun lien.

⚠️ La sortie TikTok est `dist/tiktok-story/`, pas `dist/tiktok/` — ce dernier
porte les masters de 37,5 s servis par `videoUrl`, et cinquante et un épisodes
en dépendent. Le nom est trompeur, il vient du premier réseau visé ; on ne le
renomme pas, ces adresses sont publiées.

Les quatre partagent `montage_carton.py` — l'empilement du bloc de texte, les
fondus, le fondu du son à la fin de la source. Chaque script n'y ajoute qu'un
gabarit : la taille du cadre, les lignes de pied, et le `queue` qui règle le
talon du bloc. **Ne pas toucher au `queue` d'un gabarit existant** : il est là
pour que le carton retombe exactement où il était sur les fichiers déjà
publiés, ce qui a été vérifié par comparaison de sommes de contrôle.

Compter une vingtaine de secondes par vidéo, et **surveiller le disque** — deux
cent huit fichiers de 2 Mo tiennent, mais l'espace libre se compte en gigaoctets
sur cette machine. Si `git gc` s'interrompt faute de place, il laisse des
`.git/objects/pack/tmp_pack_*` de plusieurs gigaoctets : ils ne sont référencés
par rien et se suppriment sans risque.

Une voix off de punchline manquante ne bloque pas : le montage se fait sans, et
le script le dit. Elle peut être ajoutée ensuite (`assets/vo/punchlines/`), en
supprimant le fichier monté avant de relancer.

### 6. Relier et régénérer

```bash
python3 scripts/lier-clips-et-stories.py
python3 scripts/gen-site-data.py
```

Le premier pose les adresses sur l'inventaire, le second réécrit les données du
site. **Vérifier le diff avant de committer** : il doit se limiter aux épisodes
traités. Un diff qui déborde signale une régénération qui a rattrapé une dérive
sans rapport — l'isoler dans son propre commit plutôt que de la noyer.

### 7. Publier

**RapidoCMS d'abord**, c'est l'hébergement de production :

```
upload_file_tool(type="video", name=…, file_url=<URL brute du dépôt>)
```

puis reporter l'adresse S3 dans `data/clips-du-site.json`, où elle prime sur le
dépôt. Si le téléversement répond « vous n'avez plus de stockage », s'arrêter là
et le signaler : le site reste servi depuis `raw.githubusercontent`, ce qui
fonctionne mais n'est pas un CDN vidéo.

**Rien ne part en publication sans validation humaine.** `create_draft_tool` pose
un brouillon ; `schedule_draft_tool` exige un accord explicite. Ne jamais
planifier de sa propre initiative.

### 8. Déposer

Commit sur la branche d'intégration, puis report des données du site vers le
projet Lovable (`food-series-hub-cdb6e3bf`), PR, et fusion une fois la CI verte.

Le lint de ce projet échoue parfois sur des fichiers sans rapport. Vérifier avec
`prettier --check .` sur tout le dépôt plutôt qu'en lisant le log de la CI : il
est tronqué et ne montre pas tous les fichiers fautifs.

## Ce que l'automate ne fait pas

- **Générer.** Ni Higgsfield, ni HeyGen, ni image. S'il manque un plan, il le
  signale dans `toujours_attendus` et s'arrête là.
- **Publier sur les réseaux.** Il dépose des brouillons.
- **Assouplir l'appariement** pour ramener davantage de prises.

## Cadence

Les Routines de Claude Code ne descendent pas sous l'heure. Pour un tour plus
fréquent, en poser plusieurs décalées — par exemple aux minutes 5, 25 et 45,
soit un passage toutes les vingt minutes.

Rien n'oblige à serrer : l'automate ne crée pas le travail, il le ramasse. Un
tour par heure suffit tant que les plans sont générés à la main.
