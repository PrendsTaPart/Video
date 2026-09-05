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
| 835 | Instagram | en file (`statut 0`, job relancé 949 → 954) | — |
| 833 | LinkedIn | en file (`statut 0`, jamais repris depuis sa création) | — |

Le retard n'est pas propre à ces posts : le post 836 (EPC05, LinkedIn,
créneau 08:00) est lui aussi encore à `statut 0` à 13:10, et le seul autre
post sorti aujourd'hui est un Facebook. Le planificateur passe donc sur
Facebook et traîne sur LinkedIn et Instagram, pour tout le compte.
**Ne pas replanifier** 833 et 835 : leur job existe, une seconde
programmation publierait deux fois.

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
