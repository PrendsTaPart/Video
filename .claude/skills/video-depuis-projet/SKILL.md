---
name: video-depuis-projet
description: Créer une vidéo tendance (TikTok, Reels Instagram, YouTube Shorts ou long, LinkedIn) à partir d'un projet du Journal, en récupérant tout son contexte, ses assets et son thème par le MCP. Utiliser quand on demande « fais une vidéo sur le projet X », « une vidéo tendance pour RapidoMeet », « un short LinkedIn sur … ».
---

# Vidéo tendance à partir d'un projet

Le projet est la source unique : contexte, visuels et thème viennent du MCP
Journal. Rien n'est inventé (ni chiffre, ni prix, ni avis, ni écran).

## 1. Récupérer le contexte (MCP Journal, lecture seule)

| Besoin | Outil | Ce qu'on en tire |
|---|---|---|
| Identité | `obtenir_projet(slug)` | nom, hook, punchline, description, URL, logo, charte (couleurs, polices, ton, clé de thème), assets (écrans réels, logo, 4 couvertures), vidéos déjà faites |
| Argumentaire | `obtenir_page_projet(slug)` | bénéfices, étapes, FAQ, tarifs réels, CTA n°1, ressources liées (lead magnet, formation, webinaire) |
| Historique | `lister_videos(serie, projet_slug)` | ne pas refaire un angle déjà traité ; faire une suite |
| Format narratif | `lister_formats_video` → `obtenir_format_video` | 17 formats éprouvés (duel écran partagé, tuto écran sombre, hologramme…) |
| Méthode et garde-fous | `preparer_episode`, `obtenir_methode_video` | voix eleven_v4, langage simple, sans terme technique ni chiffre |
| Visuels | `lister_assets(projet_slug)`, `lister_medias` | réutiliser avant de créer (règle bibliothèque) |
| Thème local | `videos/_journal-63-72/themes.json` (clé = `charte.theme`) | palette exacte du rendu |

Si un champ manque (bénéfices vides, pas d'écran), on le complète d'abord à
partir du vrai site (capture réelle), on l'enregistre (`modifier_page_projet`,
`ajouter_asset_projet` catégorie ecran) — jamais de remplissage inventé.

## 2. Choisir l'angle et le réseau

Une seule vidéo master 9:16 sert TikTok, Reels, Shorts et LinkedIn (règle de
`episode-multicanal`). On adapte le texte du post, pas la vidéo.

- **Hook dans les 2 premières secondes** : partir du `hook` du projet ou d'une
  douleur concrète ; texte à l'écran dès la 1re image.
- **Durée** : 20–35 s (TikTok/Reels/Shorts), 30–60 s si tuto ; YouTube long
  seulement si on a assez de vrai contenu (étapes de la page projet).
- **Tendances qui marchent ici** : avant/après en écran partagé, « POV : … »,
  tuto en 3 étapes numérotées, « ce que personne ne te dit sur … », démo réelle
  de l'écran en accéléré, réponse à une question de la FAQ.
- **LinkedIn** : même vidéo, post plus posé (problème → ce que fait le projet →
  CTA), sous-titres obligatoires.
- **CTA** : le CTA n°1 de la page projet ; mot-clé à commenter si un lead
  magnet est lié.

## 3. Produire

1. Script court (6–8 phrases), validé par `preparer_episode`.
2. Voix ElevenLabs en **une seule prise** (`generations_count=1`), voix de Michael.
3. Plans : vidéo réelle du site (enregistrement du défilement) ou écran réel du
   projet ; jamais de nouvelle génération Higgsfield (donner le prompt à Michael
   si un plan manque).
4. Rendu avec le moteur du dépôt (`mes-projets/_engine`, thème = `charte.theme`),
   logo officiel du projet, photo d'entrepreneur de Michael.
5. Miniature : design couverture (règle CLAUDE.md) ou la couverture 1080x1920
   active du projet.

## 4. Déposer et préparer la sortie

- Fichiers sur RapidoCMS (`upload_file_tool`), `creer_video` avec `projet_slug`,
  `ajouter_media` pour chaque nouvelle image.
- Puis la skill **episode-multicanal** : un seul lien, six textes de post,
  rien ne part sans validation de Michael.

## Garde-fous

- Modifier un projet (`modifier_projet`) recompose ses couvertures en
  brouillon : relancer `activer_couverture_projet(slug)` juste après.
- Pas de chiffres, prix, résultats ou témoignages qui ne figurent pas sur la
  page projet ou le site.
- Publier demande l'accord explicite de Michael.
