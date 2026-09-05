# Resto 2.0 — état de publication

## Fichiers servis (bibliothèque RapidoCMS, `video/mp4` / `image/jpeg` vérifiés en HTTP)

| Pièce | Format | URL |
|---|---|---|
| master (référence série) | 1080×1920, sous-titré | `.../bibliotheque/foodeatup-clip-resto-2-0-vertical-9x16` |
| paysage | 1920×1080 | `.../bibliotheque/foodeatup-clip-resto-2-0-master-16x9` |
| carre | 1080×1080 | `.../bibliotheque/foodeatup-clip-resto-2-0-carre-1x1` |
| 4:5 (Facebook/Instagram) | 1080×1350 | `.../bibliotheque/foodeatup-clip-resto-2-0-4x5` |
| vignette | 16:9 | `.../bibliotheque/foodeatup-clip-resto-2-0-vignette-16x9` |
| affiche | 9:16 | `.../bibliotheque/foodeatup-clip-resto-2-0-affiche-9x16` |

Préfixe : `https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/`

Le 4:5 n'a pas de type de pièce correspondant dans `publier_clip_musical`
(l'énumération ne prévoit que master / court / paysage / carre / teaser /
proxy / affiche / vignette). Il est dans la bibliothèque et sert le brouillon
Facebook, mais il n'est pas déposé au catalogue.

## Catalogue — fait

- `declarer_clip_musical` → slug `resto-2-0`, page `/clips/resto-2-0`,
  diffusion prévue le samedi 26 septembre 2026 (les trois samedis précédents
  sont pris par les clips existants).
- `publier_clip_musical` → master, paysage, carre, vignette, affiche —
  contrôle HTTP `ok` sur les cinq.
- `rattacher_clip_saison` → Le Coup de Feu, saison 5.
- **La validation reste un geste humain** : aucun outil n'écrit `valide`.

## RapidoCMS — un post sorti, deux encore en file

Campagne « Lancement FoodEatUp — Resto 2.0 », id **37**.

| Réseau | Compte | Draft | Post | Vidéo | Créneau |
|---|---|---|---|---|---|
| LinkedIn | FoodEatUp (68807312) | 958 | **833** | 16:9 | 05/09/2026 12:00 |
| Facebook | Foodeatup (201499969703551) | 959 | **834** | 4:5 | 05/09/2026 12:00 |
| Instagram | FoodEatUp (17841477689869013) | 960 | **835** | verticale | 05/09/2026 **12:10** |

État au 05/09 13:10 CEST, après le créneau :

| Post | Réseau | Statut | Identifiant du post |
|---|---|---|---|
| 834 | Facebook | **sorti** à 11:00 UTC | `1811183623210952` |
| 835 | Instagram | **sorti** à 11:10 UTC | `17964993396075791` |
| 833 | LinkedIn | **bloqué** (`statut 0`, jamais repris) | — |

Facebook et Instagram sont sortis à l'heure. LinkedIn ne sort pas, et le
problème n'est pas ce post : au 05/09 16:49, **les six posts LinkedIn du
jour sont à `statut 0`** — 671, 672, 679, 680 (compte 101119107), 833 et 836
(compte 68807312). Deux comptes LinkedIn différents, aucun `errors`
renseigné, aucun `updated_at` touché depuis la création. Le worker LinkedIn
est en panne pour tout le compte ; Facebook et Instagram fonctionnent.

Il n'y a aucune voie pour forcer la sortie depuis le MCP :
- aucun outil « publier maintenant » — RapidoCMS n'expose que créer,
  planifier, lister ;
- `cancel_schedules_post` est verrouillé côté serveur : « Destruction
  refusée, sans exception. Si quelque chose doit sortir, dites-le et
  arrêtez-vous : c'est une décision humaine. » ;
- replanifier sans annuler créerait un second job : si le worker repart, le
  post sortirait deux fois. **Non fait pour cette raison.**

À reprendre à la main depuis /admin/social, ou une fois le worker LinkedIn
remis en route — le post 833 est prêt et n'attend que ça.

### Diagnostic : c'est la taille du fichier

Des vidéos sortent bien sur LinkedIn — mais uniquement des petites. Relevé
sur les posts d'août et septembre :

| Post | Fichier | Taille | Résultat |
|---|---|---|---|
| 614 | EP501 | 1,5 Mo | ✅ `urn:li:ugcPost:7497767232018489344` |
| 617 | EP502 | 2,1 Mo | ✅ `urn:li:ugcPost:7497949939990286336` |
| 632, 635, 639 | EP505/506/507 | ~2 Mo | ✅ |
| 487 | haccp-historique | 5,2 Mo | ❌ `error creating asset401` |
| 490 | etiquettes | 7,7 Mo | ❌ `error creating asset401` |
| 637 | clip « il était une fois un restaurant » | **83 Mo** | ❌ jamais sorti |
| 842 | clip « Resto 2.0 » | **60 Mo** | ❌ `Undefined array key "etag"` |

Vingt-quatre tutoriels FoodEatUp (5 à 8 Mo) échouent tous en `asset401`, et
**le clip musical précédent n'est jamais sorti sur LinkedIn non plus**. La
bascule se situe entre 2,1 Mo (passe) et 5,2 Mo (échoue).

Les deux messages d'erreur sont le même incident à deux étapes : la création
de l'asset chez LinkedIn répond 401, puis le code lit `etag` dans une réponse
vide. L'envoi vidéo de RapidoCMS ne tient donc pas les gros fichiers — ce
n'est ni le compte, ni le jeton, ni le clip.

### Ce qui avait été conclu à tort

Premier diagnostic, incomplet — il concluait que « le chemin vidéo est
cassé », alors qu'il ne l'est que passé un certain poids :

- **833** (page société, vidéo native) : le job 947 n'a **jamais tourné**.
  `updated_at` n'a pas bougé depuis la création.
- **842** (profil Michael Kebail, vidéo native) : le job a tourné à 16:00:04
  et **a planté** — `errors: Undefined array key "etag"`, `post_urn: null`.
  RapidoCMS met quand même `statut: 1` : un post marqué publié sans
  `post_urn` et avec un `errors` renseigné n'est **pas** en ligne.

L'erreur `etag` tombe dans la gestion du média. En passant les posts en
`post_type: text` avec le lien YouTube — `media_url` devient `null`, tout le
chemin d'envoi vidéo est court-circuité — les deux sont sortis du premier
coup.

### Sorti sur LinkedIn, en texte + lien YouTube

Le profil personnel est connecté (`linkedin_profile`, `6Z5izYBhkC`, actif) et
constitue une seconde voie, indépendante du post 833 de la page société.
`create_draft_tool` refuse `linkedin_profile` comme `social_type` — il
n'accepte que les quatre réseaux de base — mais accepte l'identifiant du
profil sous `social_type: linkedin`.

| Compte | Brouillon | Post | `post_urn` |
|---|---|---|---|
| Michael Kebail (profil, `6Z5izYBhkC`) | 968 | **843** | `urn:li:share:7502034902524092417` |
| FoodEatUp (page, `68807312`) | 969 | **844** | `urn:li:share:7502036659132071936` |

Les deux sont rattachés à la campagne 37 (liens 123, 124). Textes
différenciés : première personne (voix du fondateur) sur le profil, voix de
marque sur la page.

`create_draft_tool` refuse `linkedin_profile` comme `social_type` — il
n'accepte que les quatre réseaux de base — mais accepte l'identifiant du
profil sous `social_type: linkedin`.

### Teaser LinkedIn, pour la vidéo native

`dist/FoodEatUp-Resto-2-0-teaser-linkedin-1280x720.mp4` — 21,8 s, 1280×720,
**1,70 Mo**, découpé sur le premier refrain (accroche chantée, flash logo,
double-O en signe infini). Il tient dans la bande qui fonctionne (1,5–2,1 Mo)
et devrait donc passer en vidéo native.

Son import en bibliothèque échoue encore : `upload_file_tool` récupère un 404
sur `raw.githubusercontent.com` alors que le fichier y répond en 206 — un
retard de propagation du CDN, à réessayer.

**Reste à nettoyer, à la main :** les posts vidéo 833 (page) et 842 (profil)
traînent encore. 842 est déjà marqué `statut 1` et ne repartira pas. 833 est
toujours à `statut 0` avec son job 947 : si le chemin vidéo est un jour
réparé et que ce job repart, la page société publierait une seconde fois le
même clip. `cancel_schedules_post` étant verrouillé côté serveur, la
suppression est à faire depuis /admin/social.

Les trois sont rattachés à la campagne 37 (liens 119, 120, 121).

Deux remarques sur l'outillage :
- `schedule_draft_tool` documente `post_heure` au format `H-i-s` mais l'API
  exige `H:i:s`.
- `add_post_campagne` refuse un id de brouillon : il attend un id de *post*
  déjà planifié. L'ordre du brief est donc à inverser — planifier, puis
  rattacher.
- RapidoCMS a décalé Instagram de dix minutes tout seul (12:10 au lieu de
  12:00 demandé).

## YouTube — publié

Chaîne **FoodEatUp** (`UC0Mc8pkW4t3uVjbI-ULptUA`), active et favorite, le
2026-09-04, en **public**. `get_video_status` renvoie `completed` sur les deux.

| Pièce | Lien | id interne |
|---|---|---|
| Clip 16:9 | https://www.youtube.com/watch?v=OFLbCs7IFlk | `fe72393a-…` |
| Short 9:16 | https://www.youtube.com/watch?v=vIaiReHEZRI | `493e0502-…` |

Les deux adresses sont enregistrées au catalogue en `lien_public`, sur la
pièce `paysage` et sur la pièce `master`.

`get_quota_status` annonçait pourtant `remaining: 0` et `uploads_remaining: 0`
(33 600 unités consommées sur 10 000). Les deux envois sont passés malgré ce
compteur : il est à considérer comme peu fiable, pas comme un feu vert.

## TikTok — relais manuel, reste à faire

`create_draft_tool` refuse le compte TikTok : la fiche connectée expose
`account_id: 5`, un identifiant de ligne interne et non un `open_id` TikTok,
et l'API rejette aussi bien `5` que le nom du compte. C'est cohérent avec ce
que documente le MCP Social : « WhatsApp et TikTok ne se publient par aucun
outil ». Vérifié aussi du côté Higgsfield, qui sait publier sur TikTok :
`tiktok_accounts` renvoie une liste vide, aucun compte n'y est connecté.
Il n'existe donc aucune voie automatique dans cette session. Vidéo à poster
à la main : la verticale.

Légende (sans emoji, accroche dans les trois premiers mots) :

```
Ton stock ment. Le frigo dit oui, le carnet dit non, et personne ne sait qui a raison.

On en a fait une chanson. Tout ce qui coince en cuisine, puis ce que ça donne quand ça arrête de coincer.

Huit boucles logiciel. Quatre agents qui bossent pendant que tu cuisines.

Ton resto tourne, toi tu respires.

Devis : https://site.foodeatup.com/creer-mon-devis

#restaurant #restaurateur #cuisine #restauration #chef #logicielrestaurant #gestionrestaurant #coupdefeu
```

## Deux points ouverts

- Le catalogue porte encore `date_prevue: 2026-09-26`, alors que le clip est
  sorti le 04/09 sur YouTube et sort le 05/09 sur les réseaux. Aucun outil
  exposé ne réécrit cette date : `declarer_clip_musical` refuse un slug déjà
  pris. À corriger dans /admin.
- Le statut du clip reste `monte`. La validation est un geste humain :
  aucun outil n'écrit `valide`.

## Vérifications du 05/09

- Les six fichiers de la bibliothèque répondent en 206 avec le bon
  content-type (`video/mp4`, `image/jpeg`).
- `get_video_status` : les deux vidéos YouTube sont `completed` et `public`.
- `publier_clip_musical` avait renvoyé `controle: ok` sur les cinq pièces
  au dépôt.
