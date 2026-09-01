# Prompt Lovable — le clip de saison : au catalogue, à l'agenda, sur la page et sur la carte

Projet **FoodEatUp Social Hub** (`food-series-hub`), workspace **Braind's Lovable**
(`78f6380983eca2a8298e`), projet `05bb6b0d-8c57-4347-b29b-d850b916ddde`.

## Ce qui existe déjà, et qui sert de modèle

Vérifié le 31 août 2026. `lister_series` porte désormais, **pour chaque saison**,
un objet `bandeAnnonce` :

```json
{ "numero": 1, "titre": "Michael fait son cinéma", "episodes": 30,
  "premierEpisode": "EPC01", "dernierEpisode": "EPC30",
  "affiche": "https://food-series-hub.lovable.app/thumbnails/saison-michael-fait-son-cinema-1-instagram.jpg",
  "bandeAnnonce": {
    "url": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/michael-fait-son-cinema-saison-2-bande-annonce",
    "vignette": "https://food-series-hub.lovable.app/bandes-annonces/michael-fait-son-cinema-S1.jpg",
    "duree_secondes": 28, "statut": "pret" } }
```

**C'est exactement la forme qu'il faut reprendre pour le clip.** Ce prompt ne
demande rien de nouveau sur le plan de la conception : il demande de refaire,
pour le clip musical, ce qui a déjà été fait pour la bande-annonce.

## Ce qui manque

Un clip musical est une entité du catalogue, avec son propre `slug` — et rien
ne permet d'en créer un ni de le rattacher à une saison :

```
declarer_clip_musical                      →  n'existe pas
publier_clip_musical("c-est-ma-maison", …) →  Clip inconnu : c-est-ma-maison.
                                              Clips connus : le-clash,
                                              il-etait-une-fois-un-restaurant.
```

`publier_clip_musical` **dépose une pièce sur un clip qui existe déjà** — sa
propre description dit d'appeler `lister_clips_musicaux` d'abord, « il donne les
identifiants (`slug`) exacts ». Aucun outil ne **crée** un clip, et aucune saison
ne peut en porter un.

Conséquence concrète : le clip de la saison 2 de « Michael fait son cinéma » est
monté, habillé, déposé en bibliothèque — et il n'apparaît ni à l'agenda, ni sur
la page de la saison, ni sur sa carte.

---

## Le prompt à envoyer

> Le catalogue sait rattacher une **bande-annonce** à une saison. Il ne sait pas
> en faire autant d'un **clip musical**, et il ne sait pas non plus créer
> l'entrée d'un clip. Ajoute ce qui manque : dans la donnée, dans les pages, à
> l'agenda, et dans le serveur MCP. Prends `bandeAnnonce` comme modèle partout où
> la question se pose — ce qui a été tranché pour elle vaut pour le clip.
>
> ### 1. Créer un clip : `declarer_clip_musical`
>
> Un outil MCP qui crée l'entrée d'un clip musical. Paramètres : `slug`, `titre`,
> `accroche`, `serie` (slug de série), `saison` (numéro), `date_prevue`, et un
> volet `chanson` : `style`, `bpm_demande`, `bpm_mesure`, `tonalite`,
> `duree_secondes`, `outil`.
>
> Il **refuse un `slug` déjà pris** plutôt que d'écraser. Le clip naît sans
> aucune pièce : `publier_clip_musical` les dépose ensuite, une par une, avec le
> contrôle HTTP qu'il fait déjà. Il **ne valide jamais** — `valide` reste un
> geste humain dans `/admin/production`, aucun outil ne l'expose et aucun
> n'existera.
>
> `bpm_mesure` n'est pas décoratif et **ne doit pas être facultatif**. Sur les
> trois clips produits à ce jour, le tempo demandé n'a jamais été le tempo
> obtenu : 142 demandés pour 144 mesurés, 92 pour 90,7, et 92 pour 92,29. Une
> grille de montage bâtie sur le tempo demandé dérive d'une demi-seconde en fin
> de morceau. Le catalogue doit garder celui qu'on a mesuré, pas celui qu'on a
> écrit dans le prompt.
>
> Prévois aussi le volet `montage` (`plans_sources`, `coupes`, `partis_pris[]`)
> que `lister_clips_musicaux` rend déjà pour les deux clips existants : soit en
> paramètre facultatif ici, soit dans un `enregistrer_montage_clip` séparé.
>
> ### 2. Une affiche est une image, pas une vidéo
>
> `publier_clip_musical` accepte les pièces `master | court | paysage | carre |
> teaser | proxy` et **vérifie un content-type vidéo**. Une affiche n'entre donc
> nulle part.
>
> Ajoute deux pièces d'image — `affiche` (9:16, la verticale) et `vignette`
> (16:9, celle des listes) — et fais porter au contrôle HTTP le **bon** type :
> `image/*` pour ces deux-là, `video/*` pour les autres. Un contrôle qui exige
> une vidéo là où on attend une image est pire que pas de contrôle : il refuse
> les fichiers justes.
>
> ### 3. Une saison porte son clip
>
> Dans `src/data/series.ts`, ajoute à `Saison` un champ **optionnel**, calqué sur
> `bandeAnnonce` :
>
> ```ts
> type ClipDeSaison = {
>   slug: string;              // l'entrée du catalogue, pour faire le lien
>   titre: string;
>   url: string;               // le master, servi par la bibliothèque RapidoCMS
>   affiche: string | null;    // 9:16, l'image d'attente du lecteur
>   vignette: string | null;   // 16:9, pour les listes et la carte
>   dureeSecondes: number | null;
>   datePrevue: string | null;
>   statut: Statut;
>   reseaux: Record<Reseau, Diffusion>;
> };
>
> type Saison = {
>   numero: number;
>   titre: string;
>   episodes: Episode[];
>   affiche: string;
>   bandeAnnonce?: BandeAnnonce;
>   clip?: ClipDeSaison;        // ← nouveau, facultatif
> };
> ```
>
> **Optionnel, et c'est important** : la plupart des saisons n'en auront jamais.
> Toute page doit se rendre correctement quand le champ est absent — pas de cadre
> vide, pas de « clip à venir », rien du tout. C'est la règle déjà appliquée à
> `bandeAnnonce`, et la saison 2 du « Coup de Feu » (`bandeAnnonce: null`) prouve
> qu'elle tient.
>
> Réutilise `Statut`, `Reseau` et `Diffusion` tels quels. Ne crée pas de types
> parallèles : le jour où l'on ajoute un réseau, il doit s'ajouter à un seul
> endroit.
>
> Un outil **`rattacher_clip_saison`** (`serie`, `saison`, `clip`) écrit ce lien,
> et refuse un `clip` que `lister_clips_musicaux` ne connaît pas — le lien ne
> doit jamais pouvoir désigner un clip qui n'existe pas.
>
> `lister_series` gagne alors un `clip` par saison : `null` quand il n'y en a
> pas, sinon `{ slug, titre, url, affiche, vignette, duree_secondes, date_prevue,
> statut }`. **Ne change rien d'autre à sa sortie** — d'autres outils la lisent.
>
> ### 4. L'agenda
>
> C'est le point qui manque le plus : un clip monté n'apparaît dans aucune des
> vues de production, alors qu'il a une date de diffusion comme un épisode.
>
> - **`agenda_production`** croise aujourd'hui « chaque épisode × réseau ». Fais-y
>   entrer les clips et les bandes-annonces, avec un champ `type`
>   (`episode | clip | bande_annonce`) sur chaque ligne, pour qu'un appelant
>   puisse filtrer sans deviner à la forme de l'identifiant. Garde `heberge`
>   (`bibliotheque` / `depot` / `externe` / `absent`) et `non_livrable` : ils
>   valent pour un clip exactement comme pour un épisode.
> - **`prochaines_publications`** et **`file_du_jour`** : mêmes ajouts. Les clips
>   sortent le **samedi**, les épisodes en semaine — la file du jour doit le
>   savoir, pas l'appelant.
> - **`visuels_a_planifier`** ne prend qu'un `episode`. Rends le paramètre
>   polymorphe (`episode` **ou** `clip`), ou ajoute son équivalent pour un clip.
>   Il doit rendre, réseau par réseau : l'URL du média, l'affiche, le texte à
>   coller, les hashtags, le créneau, l'état de la pièce et `planifiable`.
> - **`planifier_publication`** ne prend qu'un `episode`. Même traitement. Il doit
>   garder son verrou : il **refuse `planifie` sur une pièce non validée**.
> - **`lister_a_produire`** doit faire apparaître un clip dont une pièce manque,
>   trié par date de diffusion comme le reste.
>
> ### 5. Les pages
>
> **Page saison** — sous la bande-annonce et avant la grille d'épisodes, si la
> saison a un clip : un lecteur vidéo 9:16, largeur maximale 420 px, centré,
> `controls playsinline preload="metadata"`, l'**affiche** en `poster`. Une
> légende sous le lecteur : « Clip de la saison · *titre* · 2 min 55 ». Aucune
> lecture automatique, aucun son au chargement.
>
> Réutilise le composant du lecteur de bande-annonce plutôt que d'en écrire un
> second — un seul lecteur, deux usages.
>
> **Carte de la saison** (page série et page d'accueil) — quand la saison a un
> clip, l'affiche du clip devient disponible en second visuel, et une pastille
> « Clip » en accent orange `#FFA500`, texte blanc, apparaît à côté de la
> pastille « Bande-annonce » existante. Elle mène à la page de la saison, à
> l'ancre du lecteur ; elle ne lance aucune lecture.
>
> **Page du clip** (`/clips/:slug`) — elle existe déjà pour `le-clash` et
> `il-etait-une-fois-un-restaurant`. Un clip déclaré par `declarer_clip_musical`
> doit y arriver sans travail supplémentaire : c'est le contrôle que la
> déclaration écrit bien au même endroit que les deux clips historiques.
>
> ### 6. `verifier_pieces`
>
> Étends-le aux pièces de clip et aux bandes-annonces : interrogation HTTP
> réelle, `heberge` et `repond`. C'est le contrôle qui compte — un fichier servi
> depuis `raw.githubusercontent.com` a déjà été refusé en 403 par YouTube, et les
> deux clips historiques sont **tous les deux** servis depuis le dépôt.
>
> ### 7. Ce qu'il ne faut pas faire
>
> - Ne touche pas au modèle `Episode` ni aux outils par épisode.
> - Ne fais pas du clip un attribut privé de la saison : il garde son `slug`, sa
>   page et son entrée au catalogue. La saison le **référence**, elle ne le
>   contient pas. (C'est l'inverse de la bande-annonce, qui n'a pas d'existence
>   propre — et c'est voulu : un clip a une page, une bande-annonce non.)
> - N'expose aucun outil qui écrirait `valide`.
> - Ne code en dur aucun slug de série, aucun numéro de saison, aucun slug de
>   clip, nulle part.
>
> ### 8. Critères de recette
>
> 1. `declarer_clip_musical` sur un `slug` déjà pris refuse, sans rien écrire.
> 2. `lister_clips_musicaux(clip: "c-est-ma-maison")` rend le clip, avec
>    `bpm_mesure` à 92.29.
> 3. `publier_clip_musical(…, piece: "affiche", url: <un PNG>)` accepte ; le même
>    appel avec `piece: "master"` et ce PNG refuse, en disant que le type est
>    faux.
> 4. `publier_clip_musical(…, url: <une URL qui répond 404>)` n'écrit rien et le
>    dit.
> 5. `rattacher_clip_saison` sur un clip inconnu refuse.
> 6. Une saison sans `clip` se rend **exactement** comme avant, sans espace
>    réservé ni libellé.
> 7. `agenda_production` fait apparaître le clip à sa date, avec `type: "clip"` et
>    son `heberge`.
> 8. `planifier_publication` refuse `planifie` sur une pièce de clip non validée.
> 9. `lister_series` reste lisible par ses appelants actuels.

---

## Le clip à déclarer, prêt

| Champ | Valeur |
|---|---|
| `slug` | `c-est-ma-maison` |
| `titre` | C'est ma maison |
| `accroche` | Une année, un restaurant, un homme qui recommence. |
| `serie` | `michael-fait-son-cinema` |
| `saison` | voir l'anomalie ci-dessous |
| `date_prevue` | 2026-09-19 (un samedi, comme les deux autres clips) |
| `style` | Rap français narratif, boom-bap et piano |
| `bpm_demande` | 92 |
| `bpm_mesure` | 92.29 |
| `tonalite` | *non relevée* |
| `duree_secondes` | 183.57 |
| `outil` | Suno |
| `plans_sources` | 60 |
| `coupes` | 131 |

Les pièces, servies par la bibliothèque RapidoCMS
(base : `https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/`) :

| Pièce | Fichier | Format |
|---|---|---|
| `master` | `michael-fait-son-cinema-clip-c-est-ma-maison-master` | 1080×1920, 183,58 s |
| `proxy` | `michael-fait-son-cinema-clip-c-est-ma-maison-proxy` | 720×1280, léger |
| `affiche` | `michael-fait-son-cinema-clip-c-est-ma-maison-vignette` | 1080×1920 |

Partis pris du montage, pour le volet `montage` :

- Les neuf sections sont relevées sur le profil d'énergie de la chanson, pas sur
  des durées visées : chaque borne tombe sur un début de mesure de la grille
  mesurée à 92,29 BPM.
- Aucune fenêtre n'est consommée deux fois : chaque plan garde un curseur, et une
  fenêtre déjà servie ne ressort pas. Les soixante plans passent tous, aucun ne
  se répète à l'identique.
- Le couplet 2 resserre les coupes de deux temps à un temps, ligne après ligne.
- Le pont tient sur un seul plan ralenti, sans une seule coupe, pendant 20,8 s :
  la batterie tombe, l'image tombe avec elle.
- Le refrain final donne trente coupes pour trente épisodes, dans l'ordre du
  catalogue.
- Carton d'ouverture « un film réalisé par FoodEatUp et Michael », carton de fin,
  et la marque en haut à droite pendant tout le clip.
- La ligne de temps est quantifiée en images sur l'horloge absolue, pas coupe par
  coupe.

---

## L'anomalie à trancher avant de rattacher quoi que ce soit

`lister_series` annonce **une seule** saison pour `michael-fait-son-cinema` :
`numero: 1`, EPC01 → EPC30. Mais `lister_episodes` répond aux **deux** filtres,
avec les mêmes identifiants et deux calendriers :

| Appel | Résultat |
|---|---|
| `saison: 1` | 30 épisodes, EPC01 → EPC30, dates de septembre 2026 |
| `saison: 2` | 30 épisodes, EPC01 → EPC30, dates d'août 2027 |

Et la preuve que ça mord déjà : la **bande-annonce de la saison 2** est
aujourd'hui rattachée à la saison **`numero: 1`** — son URL le dit
(`…-saison-2-bande-annonce`), sa vignette dit l'inverse
(`…-michael-fait-son-cinema-S1.jpg`).

Un clip s'adresse par `serie` + `saison`, comme une bande-annonce. Tant que ce
couple ne désigne pas une chose unique, `rattacher_clip_saison` écrira au mauvais
endroit sans que rien ne le signale. **À vérifier côté données avant de se fier
au rattachement**, et à dire explicitement dans la réponse : soit la série n'a
qu'une saison et il faut corriger le libellé de la bande-annonce, soit elle en a
deux et `lister_series` en oublie une.
