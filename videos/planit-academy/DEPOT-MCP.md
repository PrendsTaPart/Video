# Dépôt sur le MCP Plan'It Video — état et payloads

## ✅ Correctif serveur livré — les écritures persistent

**Relevé du 19/08/2026.** Les écritures du 18/08 ne persistaient pas (voir plus
bas). Ce n'est plus le cas : `tutoriel_spec(numero: 0)` rend un `contenuDepose`
complet — `videoUrl`, `vignetteUrl`, `transcription`, les douze chapitres, la
durée « 1 min 03 » et `statut: "en_ligne"`, horodaté `majLe`
`2026-08-18T14:39:12Z`. `tutoriel_lister` donne les fiches **0, 1 et 2** en
`en_ligne` avec vidéo et vignette, et `videos_manquantes` annonce
**3 déposées / 40 manquantes**.

Les payloads de la section « Payloads à rejouer » ont donc été rejoués avec
succès : ils ne sont conservés ci-dessous que comme trace du contenu déposé.

**Mise à jour du 19/08/2026, 09 h.** Dix épisodes de plus déposés — 07, 11, 12,
13, 14, 21, 22, 23, 25 et 27. `videos_manquantes` annonce **15 déposées /
28 manquantes**. Les quatre cartes de prompt déclarées par les fiches 07, 12,
13 et 21 ont été reportées dans `contenuDepose.cartes` via
`ajouter_carte_prompt`.

**Mise à jour du 26/08/2026, 21 h.** Quatre épisodes déposés — **07**, **10**,
**28** et **33**. `videos_manquantes` annonce **18 déposées / 25 manquantes**.

| Fiche | Vidéo (S3 RapidoCMS) | Vignette (S3 RapidoCMS) | Durée |
|---|---|---|---|
| 07 | `…/bibliotheque/planit-academie-tuto-07-enregistrer-sa-propre-carte-v2` | `…/bibliotheque/planit-academie-vignette-tuto-07-v2` | 1 min 07 |
| 10 | `…/bibliotheque/planit-academie-tuto-10-lancer-une-tache-longue` | `…/bibliotheque/planit-academie-vignette-tuto-10` | 32 s |
| 28 | `…/bibliotheque/planit-academie-tuto-28-installer-un-plugin` | `…/bibliotheque/planit-academie-vignette-tuto-28` | 48 s |
| 33 | `…/bibliotheque/planit-academie-tuto-33-choisir-son-avatar` | `…/bibliotheque/planit-academie-vignette-tuto-33` | 1 min 05 |

La **07 est un remplacement**, pas un ajout : elle était déjà `en_ligne` depuis
le 19/08. Le nouveau montage a été téléversé sous un nom distinct — suffixe
`-v2` — plutôt qu'en écrasant l'objet S3 existant : `upload_file_tool` ne
documente pas son comportement en cas de nom déjà pris, et un remplacement
silencieux aurait été invérifiable. **Les deux objets du 19/08 restent sur S3 et
ne sont plus référencés** ; ils peuvent être supprimés via `delete_file_tool`
une fois le nouveau montage validé.

Sa transcription a dû être réécrite en deux temps : `enregistrer_video` ne
touche pas au champ `transcription`, si bien que l'ancien texte — qui parlait
encore de laisser la visibilité sur « Privé » — a survécu au dépôt de la
nouvelle vidéo. Un appel explicite à `enregistrer_transcription` l'a corrigé.
**À retenir pour tout remontage : redéposer la transcription même quand seule
la vidéo change.**

Les fiches 10, 28 et 33 ne déclarent aucune carte de prompt (`fiche.cartes`
vide) : aucun `ajouter_carte_prompt` n'était à jouer. La carte de la 07 était
déjà en place et a été conservée telle quelle.

**Mise à jour du 27/08/2026.** Trois épisodes déposés — **15**, **26** et
**29**. `videos_manquantes` annonce **21 déposées / 22 manquantes**.

| Fiche | Vidéo (S3 RapidoCMS) | Vignette (S3 RapidoCMS) | Durée |
|---|---|---|---|
| 15 | `…/bibliotheque/planit-academie-tuto-15-premiere-conversation` | `…/bibliotheque/planit-academie-vignette-tuto-15` | 41 s |
| 26 | `…/bibliotheque/planit-academie-tuto-26-comprendre-les-skills` | `…/bibliotheque/planit-academie-vignette-tuto-26` | 51 s |
| 29 | `…/bibliotheque/planit-academie-tuto-29-desactiver-un-skill` | `…/bibliotheque/planit-academie-vignette-tuto-29` | 48 s |

Aucune des trois fiches ne déclare de carte de prompt : pas d'appel à
`ajouter_carte_prompt`. Les trois `vignette_spec` confirment une fois de plus la
réserve n° 2 ci-dessous — celle du numéro 28 décrit « Actualiser le catalogue »,
c'est-à-dire l'écran de la **capture** 28, pas celui de la fiche 28.

**Mise à jour du 27/08/2026, soir.** La fiche **3** est déposée (42 s), la
fiche **15** repassée hors ligne. `enregistrer_video` avec `enLigne: false`
bascule `contenuDepose.statut` de `en_ligne` à **`en_montage`** — c'est le
moyen de retirer un montage du site sans effacer ce qui a été déposé.

| Fiche | Vidéo (S3 RapidoCMS) | Vignette (S3 RapidoCMS) | Durée |
|---|---|---|---|
| 3 | `…/bibliotheque/planit-academie-tuto-03-premiers-reglages` | `…/bibliotheque/planit-academie-vignette-tuto-03` | 42 s |

La carte de prompt déclarée par la fiche 3 — « Décrire mon activité en trois
lignes » — a été reportée via `ajouter_carte_prompt`.

**Mise à jour du 27/08/2026, 18 h.** Le tutoriel 00 est redéposé sous
`…/bibliotheque/planit-academie-tuto-00-creer-son-compte-v2`, après masquage des
adresses e-mail de sa capture. Comme pour le 07, le nouveau fichier porte un
suffixe `-v2` plutôt que d'écraser l'objet S3 existant. Durée 1 min 03, douze
chapitres — le plan 5 ayant été raccourci, tous les repères suivants ont bougé.

Les publications YouTube du jour sont consignées dans `YOUTUBE.md` : le MCP
Plan'It Video n'a pas d'outil `enregistrer_youtube` pour les porter sur les
fiches.

### Deux réserves qui subsistent

1. **`fiche.statut` reste à `a_produire`** sur une fiche déposée, alors que
   `contenuDepose.statut` vaut `en_ligne`. Deux champs pour une seule notion —
   c'est `contenuDepose` (et `tutoriel_lister`) qui fait foi. À clarifier côté
   serveur.
2. **Les `vignette_spec` ne correspondent pas à leur fiche.** Constaté sur
   trois fiches : la 3 (`premiers-reglages`) reçoit `titreCourt` « Mot de passe
   oublié » et `ecran-otp` ; la 5 (`utiliser-une-carte-de-prompt`) reçoit
   « Retrouver ses tâches » ; la 6 (`chercher-une-carte-de-prompt`) reçoit
   « Créer une tâche ». Le décalage n'est pas un simple décalage d'indice. **Ne
   pas se fier à `vignette_spec` pour le titre, le module ni l'écran** — tous
   les épisodes prennent leur `titreVignette` et leur module dans `fiche`.
   Confirmé sur les dix épisodes du 19/08 : la fiche 07 (« Enregistrer sa
   propre carte ») reçoit `titreCourt` « Suivre une exécution » et le module
   *Tâches* au lieu de *Bibliothèque de prompts* ; la 27 (« Activer un skill »)
   reçoit « Activer ses plugins ». Dans `vignette`, le bloc décrit l'écran de
   la **capture n°** portant ce numéro, pas celui de la fiche.

### Une réserve de contenu, à voir avec l'équipe produit

Les fiches **21 · 22 · 23 · 25** parlent de « déposer des documents », de
« fichiers » et d'« indexation ». L'application ne propose rien de tel : la
base de connaissance se remplit par un **entretien en huit sections**, mené par
l'assistant ou rempli à la main. Les `commentCaMarche` de ces quatre fiches
(« Déposez vos fichiers », « Attendez la pastille indexé ») ne décrivent aucun
écran existant.

Les vidéos ont été montées **sur l'application réelle**, pas sur le texte des
fiches : la voix off parle de sections et d'entretien. Reste à corriger le
texte des fiches côté produit — promesse, `commentCaMarche`, et la carte de
prompt de la 21 qui dit « en te basant uniquement sur mes documents ».

### Ce qui n'a toujours pas d'outil d'écriture

`pointsCles` · `prerequis` · `ressources` · `promptsMarketplace` apparaissent
dans `contenuDepose` mais aucun des outils du MCP ne les remplit. Seul `cartes`
est adressable, via `ajouter_carte_prompt`.

---

## Trace du dépôt initial (18/08/2026) — écritures sans persistance

Ce qui suit décrit l'incident d'origine, conservé pour mémoire.

---

## Ce qui est bien en place

Les fichiers sont produits et **hébergés publiquement** — cette partie est
vérifiable immédiatement.

| Fiche | Vidéo (S3 RapidoCMS) | Vignette (S3 RapidoCMS) |
|---|---|---|
| 0 | `…/bibliotheque/planit-academie-tuto-00-creer-son-compte` | `…/bibliotheque/planit-academie-vignette-tuto-00` |
| 1 | `…/bibliotheque/planit-academie-tuto-01-se-connecter` | `…/bibliotheque/planit-academie-vignette-tuto-01` |
| 2 | `…/bibliotheque/planit-academie-tuto-02-retrouver-son-mot-de-passe` | `…/bibliotheque/planit-academie-vignette-tuto-02` |

Racine S3 : `https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/`

---

## Payloads à rejouer

### Fiche 0 — Créer son compte Plan'It · 1 min 03

```
enregistrer_video(
  numero: 0,
  videoUrl: "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/planit-academie-tuto-00-creer-son-compte",
  duree: "1 min 03",
  chapitres: [
    {0,  "Ouverture"},                    {4,  "Présentation"},
    {12, "L'écran de connexion"},         {18, "Le formulaire d'inscription"},
    {24, "L'adresse professionnelle"},    {29, "Mot de passe et confirmation"},
    {34, "Le code à 6 chiffres"},         {38, "Le code reçu par email"},
    {42, "Vérification du code"},         {47, "Première connexion"},
    {52, "Votre espace est ouvert"},      {58, "Punchline"}])

enregistrer_vignette(numero: 0,
  url: ".../bibliotheque/planit-academie-vignette-tuto-00")

enregistrer_transcription(numero: 0, texte: <voir SCRIPT.md de l'épisode>)
definir_statut(numero: 0, statut: "en_ligne")
```

### Fiche 1 — Se connecter à son espace · 50 s

```
enregistrer_video(
  numero: 1,
  videoUrl: ".../bibliotheque/planit-academie-tuto-01-se-connecter",
  duree: "50 s",
  chapitres: [
    {0,  "Ouverture"},                    {4,  "Présentation"},
    {13, "L'écran de connexion"},         {17, "Votre adresse professionnelle"},
    {20, "Le mot de passe"},              {24, "Votre espace s'ouvre"},
    {31, "Paramètres · Déconnexion"},     {35, "Confirmer la déconnexion"},
    {41, "Compte fermé"},                 {45, "Punchline"}])

enregistrer_vignette(numero: 1,
  url: ".../bibliotheque/planit-academie-vignette-tuto-01")

enregistrer_transcription(numero: 1, texte: <voir SCRIPT.md de l'épisode>)
definir_statut(numero: 1, statut: "en_ligne")
```

### Fiche 2 — Retrouver son mot de passe · 49 s

```
enregistrer_video(
  numero: 2,
  videoUrl: ".../bibliotheque/planit-academie-tuto-02-retrouver-son-mot-de-passe",
  duree: "49 s",
  chapitres: [
    {0,  "Ouverture"},                    {4,  "Présentation"},
    {11, "« Mot de passe oublié ? »"},    {15, "L'adresse de votre compte"},
    {20, "Envoyer le code"},              {23, "L'écran de vérification"},
    {26, "Le code reçu par email"},       {32, "Saisir les six chiffres"},
    {35, "Le nouveau mot de passe"},      {40, "Mot de passe actif"},
    {44, "Punchline"}])

enregistrer_vignette(numero: 2,
  url: ".../bibliotheque/planit-academie-vignette-tuto-02")

enregistrer_transcription(numero: 2, texte: <voir SCRIPT.md de l'épisode>)
definir_statut(numero: 2, statut: "en_ligne")
```

---

## Champs de fiche sans outil d'écriture

Le MCP n'expose que **8 outils**. Quatre champs apparaissent dans
`contenuDepose` mais **aucun outil ne permet de les remplir** :

`pointsCles` · `prerequis` · `ressources` · `promptsMarketplace`

Seul `cartes` est adressable, via `ajouter_carte_prompt`. Les fiches 0, 1 et 2
ne définissent aucune carte de prompt dans leur spécification — il n'y a donc
rien à y déposer, et en inventer irait contre la fiche.

**À demander à l'équipe MCP** : des outils d'écriture pour ces quatre champs, ou
confirmation qu'ils sont alimentés ailleurs.

---

## Procédure standard, à appliquer à chaque épisode

1. `python3 episode.py` — rend le master et la vignette.
2. `git commit && git push` — le dépôt est public, ce qui donne des URL `raw`.
3. `upload_file_tool` (RapidoCMS) × 2 — la vidéo puis la vignette, depuis l'URL
   `raw` figée sur le SHA du commit.
4. `enregistrer_video` · `enregistrer_vignette` · `enregistrer_transcription` ·
   `definir_statut` sur la fiche du MCP.
5. **Relire `tutoriel_spec(numero)`** pour confirmer que `contenuDepose` est bien
   rempli — l'accusé de succès ne suffit pas, comme l'a montré ce dépôt.
