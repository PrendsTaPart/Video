# Tutoriel 11 — Lancer une campagne : la page Campagne et sa fenêtre de création

**Module** : Communication · **Slug** : `lancer-une-campagne`
**Capture source** : `_sources/Affiliation_des_postes_a_une_campagne_marketing.mp4`
— 63,8 s. La voix d'origine est supprimée et remplacée par la voix off
ci-dessous.

**Promesse** : à la fin de cette vidéo, vous savez à quoi sert la page
Campagne, ce que comptent ses statistiques, et ce que demande la fenêtre de
création.

---

## Ce que montre réellement la capture

Le titre du fichier source annonce l'affiliation de posts à une campagne
marketing : **cette étape n'apparaît jamais**. La capture montre la page
« Campagne » d'un compte de démonstration vide — champ « Chercher »,
statistiques à zéro, « Liste des campagnes » vide — puis la fenêtre ouverte par
« Créer une campagne » : champs « Nom de la campagne » et « Description », trois
réseaux à cocher (Facebook, Instagram, LinkedIn) et le bouton « Ajouter ».

Rien n'est saisi, aucun réseau n'est coché, et le clic sur « Ajouter » ne
produit aucun effet : **la campagne n'est même pas créée**. Le script l'assume
— il décrit ce qui est à l'écran, puis annonce la suite au futur.

Le titre affiché en haut de la page ne correspond pas à la rubrique ouverte, et
le compteur de campagnes comporte une faute : ni l'un ni l'autre ne sont cités
tels quels, les mots sont prononcés correctement.

Temps morts écartés du montage : 4 s → 14 s et 20 s → 24 s partiellement (page
figée), 36 s → 52 s (fenêtre vide, souris qui erre), et la fin figée après
58 s. Les extraits sont pris dans 0–4 s, 14–36 s et 52–58 s.

---

## Voix off

Cadence 150 mots par minute. Une ligne = un plan ; chaque plan dure exactement
la durée de sa ligne.

| # | Chapitre | Source | Texte |
|---|---|---|---|
| N1 | **1 · Où vivent les campagnes** | 0,0 → 4,0 | Vos posts partent dans tous les sens et vous ne savez plus lesquels servent le même objectif. Une campagne les regroupe. |
| N2 | | 24,0 → 28,0 | Nous sommes dans RapidoCMS, rubrique Communication, page Campagne. Une recherche en haut, des statistiques au milieu, la liste de vos campagnes en dessous. |
| N3 | **2 · Les statistiques** | 14,0 → 18,0 | La première section compte deux choses : le nombre de campagnes créées, et le nombre de posts qui leur sont rattachés. |
| N4 | | 14,0 → 18,0 | Ici tout est à zéro, et les deux encarts de droite annoncent qu'aucune donnée n'est disponible. Ils se rempliront dès votre première campagne. |
| N5 | **3 · La liste des campagnes** | 20,0 → 24,0 | Plus bas, « Liste des campagnes » : vide elle aussi. C'est là qu'apparaîtront vos campagnes, chacune avec ses statistiques. |
| N6 | | 24,0 → 28,0 | Le champ « Chercher », en haut, servira quand la liste s'allongera : vous tapez le nom d'une campagne pour la retrouver sans faire défiler. |
| N7 | **4 · Créer une campagne** | 28,0 → 32,0 | Le bouton « Créer une campagne » est en haut à droite. Il devient bleu au survol, et ouvre une fenêtre par-dessus la page. |
| N8 | | 32,0 → 36,0 | Trois informations sont demandées : le nom de la campagne, une description qui précise l'objectif ou le public visé, et le réseau principal. |
| N9 | | 32,0 → 36,0 | Les réseaux proposés sont Facebook, Instagram et LinkedIn, à cocher. Le bouton « Ajouter », en bas, valide la création. |
| N10 | **5 · Ce que la capture ne montre pas** | 52,0 → 56,0 | Dans cette démonstration, les champs restent vides et rien n'est coché : la campagne n'est donc jamais créée, et la liste reste vide. |
| N11 | | 55,0 → 58,0 | Chez vous, remplissez le nom, la description, cochez un réseau, puis « Ajouter » : la campagne rejoindra la liste, et ses compteurs démarreront. |
| N12 | **6 · La Version Minute** | *carte* | Et si vous n'aviez pas à ouvrir cette page du tout ? Une campagne se crée en une phrase, depuis Claude. |
| N13 | | *carte* | L'outil `create_campagne` du MCP RapidoCMS la crée avec son nom, sa description et son réseau. Ensuite, `add_post_campagne` y rattache vos posts. |
| N14 | **7 · L'astuce** | 20,0 → 24,0 | L'astuce : créez la campagne avant les posts. Chaque post rattaché alimente les compteurs, et vous mesurez un ensemble au lieu de publications isolées. |
| FIN | *outro* | — | Retenez ceci : la campagne est le dossier qui regroupe vos posts et leurs résultats. Dans la prochaine vidéo, on découvre l'éditeur. |

## Chapitres prévisionnels

| Timecode | Chapitre |
|---|---|
| 00:00 | Ouverture |
| 00:08 | 1 · Où vivent les campagnes |
| 00:24 | 2 · Les statistiques |
| 00:44 | 3 · La liste des campagnes |
| 01:03 | 4 · Créer une campagne |
| 01:24 | 5 · Ce que la capture ne montre pas |
| 01:39 | 6 · La Version Minute |
| 01:54 | 7 · L'astuce |

*(Les timecodes définitifs sont recalculés par le montage, à partir de la durée
réelle de chaque ligne de voix off.)*

## Carte Version Minute

- **Prompt** : « Crée une campagne "Rentrée" sur Facebook pour ma société, et dis-moi combien j'en ai. »
- **Outil** : `create_campagne`
- **Suite citée** : `add_post_campagne` pour y rattacher les posts,
  `ingishts_campagne` pour en lire les résultats.

## Vignette

Timecode 32 s : la fenêtre de création ouverte, avec ses champs et les trois
réseaux — la seule image de la capture qui montre quelque chose de fonctionnel.

## Astuce retenue pour la fiche

Créer la campagne avant les posts : chaque post rattaché alimente les compteurs
de la campagne, ce qui permet de mesurer un ensemble plutôt que des
publications isolées.

## Cas d'usage

- Une entreprise prépare une opération de rentrée sur plusieurs semaines.
- Un gérant veut savoir combien de posts servent réellement un même objectif.
- Une équipe cherche où retrouver les résultats consolidés d'une opération.
