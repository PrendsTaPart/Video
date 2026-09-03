# Tutoriel 08 — Créer un post : la page Réseaux sociaux et son formulaire

**Module** : Communication · **Slug** : `creer-un-post-reseaux-sociaux`
**Capture source** : `_sources/comunication_resaux_socieaux.mp4` — 63,4 s. La
voix d'origine est supprimée et remplacée par la voix off ci-dessous.

**Promesse** : à la fin de cette vidéo, vous savez où se crée un post dans
RapidoCMS et ce que demande le formulaire, champ par champ.

---

## Ce que montre réellement la capture

La page « Réseaux sociaux » d'un compte de démonstration vide : trois onglets
(Facebook, LinkedIn, Instagram) et, sous chacun, le message « Il n'y a
actuellement aucune donnée à afficher ». Puis le formulaire ouvert par
« Créer un poste », rempli **à moitié** : nom « Test », réseau « Facebook »,
compte « Cocuisinage By Foodeatup », type « Texte ». Le champ de rédaction
reste vide et le clic sur « Créer » n'aboutit sur rien : **aucun post n'est
créé dans cette capture**. Le script le dit et annonce la suite comme une
suite.

Aucune liste déroulante n'est montrée ouverte : on voit la valeur avant, puis
après. Les types « image », « vidéo » et « lien » ne sont jamais affichés — ils
ne sont donc pas décrits. L'étiquette « Aide du bot » apparaît sans jamais être
ouverte : la voix off le signale sans lui prêter de comportement.

Temps morts écartés du montage : 0 s → 8 s (écran vide immobile), 28 s (temps
mort avant la première saisie), 48 s → 63 s (souris qui erre, puis fin figée
sur un bouton inactif). Les extraits sont pris entre 8 s et 48 s.

Fautes d'interface (« Paramètrage », « Apperçu », « Choisissez un réseaux »,
« Ecrire un texte ») : les mots sont prononcés correctement, sans être
soulignés.

---

## Voix off

Cadence 150 mots par minute. Une ligne = un plan ; chaque plan dure exactement
la durée de sa ligne.

| # | Chapitre | Source | Texte |
|---|---|---|---|
| N1 | **1 · La page Réseaux sociaux** | 8,0 → 12,0 | Publier sur Facebook, LinkedIn et Instagram sans jongler entre trois applications : tout part d'une seule page, et d'un seul bouton. |
| N2 | | 8,0 → 12,0 | Nous sommes dans RapidoCMS, rubrique Communication, page Réseaux sociaux. Trois onglets séparent vos publications par réseau : Facebook, LinkedIn, Instagram. |
| N3 | | 12,0 → 16,0 | Sur ce compte de démonstration, chaque onglet est vide : « Il n'y a actuellement aucune donnée à afficher ». Vos posts viendront s'y ranger, réseau par réseau. |
| N4 | | 16,0 → 20,0 | L'onglet actif est souligné en bleu. Vous changez d'onglet pour vérifier ce qui est prévu sur un réseau précis, sans quitter la page. |
| N5 | **2 · Créer un poste** | 20,0 → 24,0 | Le bouton « Créer un poste » est en haut à droite. C'est le seul point d'entrée : il ouvre le formulaire à la place de la liste. |
| N6 | | 24,0 → 28,0 | Deux colonnes. À gauche le paramétrage, à droite l'aperçu : une maquette de post avec « J'aime », « Commenter » et « Partager ». |
| N7 | **3 · Nommer et choisir le réseau** | 30,0 → 34,0 | Premier champ, le nom du poste. Ici, « Test ». Ce nom est interne : il sert à retrouver le post dans la liste, il n'est jamais publié. |
| N8 | | 34,0 → 38,0 | Deuxième champ, « Choisir un réseau social ». La liste propose vos réseaux connectés ; on retient Facebook. |
| N9 | **4 · Le compte et le type** | 38,0 → 42,0 | Troisième champ, « Choisir un compte » : ici « Cocuisinage By Foodeatup ». L'aperçu se met à jour en direct, avec le nom de la page et la mention « Maintenant ». |
| N10 | | 42,0 → 46,0 | Quatrième champ, « Type de poste » : « Texte ». Le cadre image disparaît de l'aperçu, et un champ de rédaction s'ouvre plus bas. |
| N11 | | 44,0 → 48,0 | Ce champ accueille votre message. À côté apparaît « Aide du bot », que cette démonstration n'ouvre pas. Le bouton « Créer » attend sous le champ. |
| N12 | | 44,0 → 48,0 | Dans la capture, le texte reste vide et le post n'est pas créé. Chez vous : rédigez, cliquez sur « Créer », et le post rejoindra la liste de l'onglet. |
| N13 | **5 · La Version Minute** | *carte* | Ce formulaire, vous pouvez aussi ne jamais l'ouvrir : la même chose se demande en une phrase, depuis Claude. |
| N14 | | *carte* | L'outil `create_draft_tool` du MCP RapidoCMS crée le brouillon avec son réseau, son compte et son texte. Vous le retrouvez ensuite dans la liste. |
| N15 | **6 · L'astuce** | 38,0 → 42,0 | L'astuce : donnez au poste un nom qui commence par la date et le réseau. Quand la liste se remplit, vous retrouvez n'importe quel post en un coup d'œil. |
| FIN | *outro* | — | Retenez ceci : un nom, un réseau, un compte, un type — et le post est prêt à écrire. Dans la prochaine vidéo, on pilote le calendrier éditorial. |

## Chapitres prévisionnels

| Timecode | Chapitre |
|---|---|
| 00:00 | Ouverture |
| 00:08 | 1 · La page Réseaux sociaux |
| 00:36 | 2 · Créer un poste |
| 00:53 | 3 · Nommer et choisir le réseau |
| 01:11 | 4 · Le compte et le type |
| 01:36 | 5 · La Version Minute |
| 01:52 | 6 · L'astuce |

*(Les timecodes définitifs sont recalculés par le montage, à partir de la durée
réelle de chaque ligne de voix off.)*

## Carte Version Minute

- **Prompt** : « Prépare un brouillon de post Facebook pour le compte Cocuisinage By Foodeatup, sur le thème de la rentrée. »
- **Outil** : `create_draft_tool`
- **Suite citée** : `list_drafts_tool` pour retrouver le brouillon.

## Vignette

Timecode 40 s : le formulaire renseigné (« Test », « Facebook », « Cocuisinage
By Foodeatup ») avec l'aperçu à droite — l'image la plus parlante de la capture.

## Astuce retenue pour la fiche

Nommer chaque poste avec sa date et son réseau : le nom du poste est interne,
il n'est jamais publié, mais c'est lui qui rend la liste lisible quand elle se
remplit.

## Cas d'usage

- Un gérant prépare sa première publication Facebook depuis RapidoCMS.
- Une équipe veut séparer clairement ce qui part sur Facebook, LinkedIn et Instagram.
- Un community manager cherche où l'aperçu du post se vérifie avant publication.
