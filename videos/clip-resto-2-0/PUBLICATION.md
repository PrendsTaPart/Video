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

## RapidoCMS — trois brouillons à relire, rien de planifié

Campagne « Lancement FoodEatUp — Resto 2.0 », id **37**.

| Réseau | Compte | Draft id | Vidéo |
|---|---|---|---|
| LinkedIn | FoodEatUp (68807312) | **958** | 16:9 |
| Facebook | Foodeatup (201499969703551) | **959** | 4:5 |
| Instagram | FoodEatUp (17841477689869013) | **960** | verticale |

Rien n'est planifié ni publié, comme demandé. Après relecture :
`schedule_draft_tool` sur les trois au même créneau, puis
`add_post_campagne` (campagne 37) — cet outil refuse un id de brouillon, il
attend un post déjà planifié, l'ordre du brief est donc à inverser sur ce
point.

## TikTok — relais manuel

`create_draft_tool` refuse le compte TikTok : la fiche connectée expose
`account_id: 5`, un identifiant de ligne interne et non un `open_id` TikTok,
et l'API rejette aussi bien `5` que le nom du compte. C'est cohérent avec ce
que documente le MCP Social : « WhatsApp et TikTok ne se publient par aucun
outil ». Vidéo à poster à la main : la verticale ci-dessus.

Légende (sans emoji, accroche dans les trois premiers mots) :

```
Ton stock ment. Le frigo dit oui, le carnet dit non, et personne ne sait qui a raison.

On en a fait une chanson. Tout ce qui coince en cuisine, puis ce que ça donne quand ça arrête de coincer.

Huit boucles logiciel. Quatre agents qui bossent pendant que tu cuisines.

Ton resto tourne, toi tu respires.

Devis : https://site.foodeatup.com/creer-mon-devis

#restaurant #restaurateur #cuisine #restauration #chef #logicielrestaurant #gestionrestaurant #coupdefeu
```

## YouTube — impossible dans cette session

Aucun serveur MCP YouTube Publisher n'est connecté : ni `get_channel_status`,
ni `publish_video`, ni `get_video_status` n'existent dans les outils
disponibles. Le MCP Social le confirme en creux — `dossier_publication_video`
dit que YouTube « ne passe pas par RapidoCMS » et qu'il faut donner sa fiche
« au serveur MCP YouTube Publisher », absent ici.

Métadonnées prêtes, à passer au serveur une fois connecté :

**Vidéo longue (16:9)** — `foodeatup-clip-resto-2-0-master-16x9`
- Titre : `FoodEatUp — Resto 2.0 (clip officiel)`
- Vignette : `foodeatup-clip-resto-2-0-vignette-16x9`
- Tags : `restaurant, gestion de restaurant, logiciel restaurant, logiciel de caisse, HACCP, restauration, restaurateur, chef de cuisine, stock restaurant, planning équipe, FoodEatUp, clip officiel`
- Description :

```
Resto 2.0 — le clip de lancement de FoodEatUp.

Le frigo dit oui, le carnet dit non. Le contrôle qui peut tomber n'importe
quand. Trois annonces, zéro réponse. Quarante-cinq minutes pour servir une
table. Les couplets alignent ce qui coince dans un restaurant ; les refrains
rejouent les mêmes scènes à l'endroit où le logiciel résout le problème.

Huit boucles logiciel qui parlent entre elles, et quatre agents qui
travaillent pendant que vous cuisinez : Caroline décroche, Jarvis répond à
l'équipe, PrediBot annonce ce qui va manquer, Iris parle pour votre
restaurant.

Ton resto tourne, toi tu respires.

Demander un devis : https://site.foodeatup.com/creer-mon-devis

Images tirées de la série « Le Coup de Feu » (33 épisodes).
```

**Short (9:16)** — `foodeatup-clip-resto-2-0-vertical-9x16`
- Titre : `Ton stock ment. Le frigo dit oui, le carnet dit non #Shorts`
- Description : accroche + `https://site.foodeatup.com/creer-mon-devis`

Une fois les deux vidéos en ligne, enregistrer les adresses avec
`publier_clip_musical` et son champ `lien_public`.
