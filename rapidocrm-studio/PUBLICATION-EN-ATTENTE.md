# Pages Académie en attente

Le jeton du MCP « RapidoCRM Académie » a expiré en cours de session
(`requires re-authorization`), et il ne peut pas être renouvelé depuis une
session non interactive. Les pages du site sont donc les seules pièces
manquantes : **tout le reste est publié**.

## Ce qui est déjà en ligne

| Tutoriel | Bibliothèque RapidoCMS | YouTube | Short | LinkedIn |
|---|---|---|---|---|
| V02 Mot de passe oublié | ✅ 16:9 + 9:16 | CThuBhcp4MY | oGx-2mmzQf8 | 27/08 16 h |
| V03 Créer son entreprise | ✅ 16:9 + 9:16 | MMOlUjJyqvw | _DQJGhlTgYI | 28/08 07 h |
| V04 Configurer son profil | ✅ 16:9 + 9:16 | lw5o48sIWDM | We8GOS3QRKw | 28/08 16 h |
| V05 Configurer sa TVA | ✅ 16:9 + 9:16 | fXxLbCkZ2rk | QAoMYtLHsXk | 29/08 07 h |

V01 est déjà entièrement publiée, page du site comprise.

## Ce qu'il reste à faire, une fois le MCP réautorisé

Pour chacun des quatre tutoriels, dans cet ordre :

1. `creer_tutoriel` — titre, titre court, accroche, `a_quoi_ca_sert`,
   `explication` (le « comment ça marche »), prérequis, étapes ;
2. `ajouter_astuces`, `ajouter_cas_usage`, `ajouter_prompts` (mode `remplacer`) ;
3. `enregistrer_transcription` avec les chapitres de
   `transcription-chapitres.json` ;
4. `enregistrer_seo` (bloc `seo` de `script.json`) ;
5. `configurer_agent_tutoriel` ;
6. `enregistrer_video` (lien AWS 16:9 + durée) et `enregistrer_video_avatar`
   (lien AWS 9:16) ;
7. `enregistrer_youtube` (lien de la vidéo normale, pas du Short) ;
8. `publier_tutoriel`.

Tout le contenu à saisir est déjà dans `fiche.json` et `script.json` de chaque
dossier — rien à réécrire.

## Slugs

| Dossier | Slug Académie |
|---|---|
| V02-oublie-de-mot-de-passe | `01-oublie-de-mot-de-passe` |
| V03-creer-son-entreprise | `01-creer-son-entreprise` |
| V04-configurer-son-profil | `01-configurer-son-profil` |
| V05-configurer-sa-tva | `01-configurer-sa-tva` |

## V06

`V06-configurer-son-imap` a sa source et sa vignette en place, rien d'autre.
