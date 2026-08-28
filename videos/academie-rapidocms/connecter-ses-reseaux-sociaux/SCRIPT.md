# Tutoriel 04 — Ses réseaux sociaux connectés, et quand les reconnecter

**Module** : Prise en main · **Slug** : `connecter-ses-reseaux-sociaux`
**Capture source** : `_sources/Configuration_et_connexion_social_media.mp4`
— 53,4 s. Le bandeau de marque d'origine et la bande de sous-titres incrustés
sont retirés au montage : la voix d'origine est supprimée et remplacée par la
voix off ci-dessous.

**Promesse** : à la fin de cette vidéo, vous savez lire l'écran des comptes
reliés à votre espace, repérer celui qui va expirer, et ce qui déclenche une
reconnexion.

---

## Ce que montre réellement la capture

L'onglet « Configuration compte » et sa section « Réseaux sociaux » : quatre
tuiles — Facebook, LinkedIn, Instagram, et une tuile « + ». Cliquer sur une
tuile affiche à droite les comptes **déjà** reliés, avec leur date
d'expiration.

**Aucune connexion n'est réellement effectuée** : le tunnel d'autorisation
(fenêtre du réseau social, écran de permissions, retour dans RapidoCMS) n'est
jamais montré. Les boutons « Se connecter » et « associer » ne sont pas
cliqués. La tuile « + » n'ouvre aucune fenêtre : elle affiche un panneau de
remplacement. Ni X, ni TikTok, ni YouTube n'apparaissent dans l'interface — le
script ne les mentionne donc pas. Le titre retenu décrit ce qui est réellement
filmé : la lecture des comptes reliés et de leurs échéances.

Valeurs relevées, reprises telles quelles : Facebook → « Cocuisinage By
Foodeatup », « Avatalk », « Plan'It », expiration « 2025-12-05 » ;
LinkedIn → « RapidoSoftware », « BraindCode », « FoodEatUp », expiration
« 2025-11-15 » ; Instagram → « BraindCode », « Cocuisinage », expiration
« 2025-12-05 ».

Temps morts écartés du montage : 4 s → 12 s, le plan 12 s (panneau droit encore
vide), 28 s → 32 s, et l'écran figé de 40 s à 48 s.

---

## Voix off

Cadence 150 mots par minute. Une ligne = un plan ; chaque plan dure exactement
la durée de sa ligne.

| # | Chapitre | Source | Texte |
|---|---|---|---|
| N1 | **1 · Vos comptes au même endroit** | 0,0 → 4,0 | Vous publiez encore réseau par réseau. Avant de changer ça, RapidoCMS a besoin de savoir quels comptes vous appartiennent. |
| N2 | | 0,0 → 4,0 | Page « Profil », onglet « Configuration compte ». La section « Réseaux sociaux » aligne quatre tuiles : Facebook, LinkedIn, Instagram, et un plus. |
| N3 | **2 · Facebook et LinkedIn** | 20,0 → 24,0 | Sélectionnez une tuile : le panneau de droite se remplit. Facebook liste trois pages reliées : « Cocuisinage By Foodeatup », « Avatalk » et « Plan'It ». |
| N4 | | 20,0 → 24,0 | Le bouton « Se connecter » lance l'autorisation côté Facebook. La capture ne l'ouvre pas : elle montre le résultat, une fois les pages autorisées. |
| N5 | | 24,0 → 28,0 | La tuile LinkedIn suit exactement le même principe, avec trois organisations : « RapidoSoftware », « BraindCode » et « FoodEatUp ». |
| N6 | | 24,5 → 28,0 | Son tableau n'a que deux colonnes, le nom et l'expiration : LinkedIn ne renvoie pas de vignette. Ce n'est pas une erreur. |
| N7 | **3 · Le cas Instagram** | 16,0 → 20,0 | Instagram pose une condition, rappelée par le bandeau bleu : votre compte doit d'abord être associé à une page Facebook. |
| N8 | | 16,0 → 20,0 | Le bouton « associer » prend le relais ensuite. Deux comptes figurent déjà dans la liste : « BraindCode » et « Cocuisinage ». |
| N9 | **4 · Les dates d'expiration** | 20,0 → 24,0 | La colonne « Expiration » est la plus importante de l'écran. Une autorisation a une fin de validité, ici le cinq décembre côté Facebook. |
| N10 | | 24,0 → 28,0 | Côté LinkedIn, c'est le quinze novembre. Passée la date, la publication échoue : il faut repasser par « Se connecter » pour prolonger. |
| N11 | | 20,0 → 24,0 | À droite de chaque ligne, la corbeille rouge retire le compte de votre espace RapidoCMS. Elle ne touche à rien sur le réseau lui-même. |
| N12 | **5 · La tuile plus** | 32,0 → 36,0 | La quatrième tuile sert à ajouter un autre réseau. Dans cette version, elle n'ouvre rien : elle affiche un panneau encore vide. |
| N13 | **6 · La Version Minute** | *carte* | Cet inventaire, vous n'avez pas besoin d'ouvrir la page pour l'obtenir. |
| N14 | | *carte* | Dans Claude, l'outil `list_connected_accounts` du MCP RapidoCMS vous rend la liste des comptes reliés et leurs échéances. |
| N15 | **7 · L'astuce** | 24,0 → 28,0 | L'astuce : notez la date la plus proche dans votre agenda, moins une semaine. Une autorisation expirée ne prévient pas, elle fait juste échouer la publication. |
| FIN | *outro* | — | Retenez ceci : un compte relié n'est pas relié pour toujours. Dans la prochaine vidéo, on lit votre tableau de bord. |

## Chapitres prévisionnels

| Timecode | Chapitre |
|---|---|
| 00:00 | Ouverture |
| 00:00 | 1 · Vos comptes au même endroit |
| 00:15 | 2 · Facebook et LinkedIn |
| 00:41 | 3 · Le cas Instagram |
| 00:54 | 4 · Les dates d'expiration |
| 01:15 | 5 · La tuile plus |
| 01:23 | 6 · La Version Minute |
| 01:35 | 7 · L'astuce |

*(Les timecodes définitifs sont recalculés par le montage, à partir de la durée
réelle de chaque ligne de voix off.)*

## Astuce retenue pour la fiche

Reporter dans son agenda la date d'expiration la plus proche, une semaine
avant : une autorisation périmée ne déclenche aucune alerte, elle fait
simplement échouer la publication.

## Cas d'usage

- Une publication programmée échoue sans message clair : vérifier les
  expirations.
- Un compte Instagram professionnel refuse de se relier faute de page Facebook.
- Un collaborateur part et son compte doit être retiré de l'espace.
