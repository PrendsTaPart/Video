# RapidoCRM Studio — règles de production

Ce projet produit les **172 tutoriels vidéo de RapidoCRM Académie**, de
l'enregistrement d'écran brut jusqu'à la page publiée sur le site.

## La chaîne, en 9 étapes

```
source.mp4
  1. analyse    → analyse.json      (frames, OCR, actions, étapes, zones sensibles)
  2. fiche      → fiche.json        (compréhension métier via MCP RapidoCRM)
  3. script     → script.json + script.md
  4. voix       → voix/*.mp3 + voix/alignement.json + transcription.txt
  5. rendu      → out/master-16x9.mp4, out/master-9x16.mp4, rendu.json
                  (la vignette du tutoriel ouvre la vidéo — voir plus bas)
  6. vignette   → out/thumb-16x9.jpg, out/thumb-9x16.jpg
  7. publier:cms      → lien AWS S3            (MCP RapidoCMS)
  8. publier:youtube  → lien YouTube           (MCP YouTube)
  9. publier:site     → page en ligne          (MCP « RapidoCMS tutoriels »)
```

`npm run tuto -- <module> <numero>` enchaîne le tout.

## Règles non négociables

1. **Ne jamais inventer une fonctionnalité de RapidoCRM.** Toute affirmation sur
   le logiciel vient soit d'une frame de l'enregistrement d'écran, soit d'un
   schéma d'outil du MCP RapidoCRM. Ce qui n'est pas vérifiable va dans
   `fiche.json → a_verifier`, jamais dans le script.
2. **Aucune écriture dans le CRM depuis ce pipeline.** Les appels au MCP
   RapidoCRM sont en lecture seule (schémas d'outils, listes de démonstration).
3. **La charte RapidoSoftware est une contrainte de build**, pas une
   recommandation. Voir « Charte » ci-dessous. Les composants échouent au build
   si elle est violée.
4. **La vidéo s'ouvre sur la vignette du tutoriel.** Elle est récupérée dans
   cet ordre : lien AWS de `publication.json`, puis la fiche en ligne via le MCP
   « RapidoCMS tutoriels » (`obtenir_tutoriel`), puis `out/thumb-16x9.jpg`. Le
   spectateur retrouve ainsi l'image sur laquelle il a cliqué.
5. **`script.json` est la seule source du rendu.** Aucun texte n'est écrit en dur
   dans le template.
6. **Deux points d'arrêt ne sont jamais contournés**, même en mode série :
   après l'écriture du script, et après le rendu de prévisualisation.
7. **Confidentialité** : toute donnée réelle visible à l'écran (email, téléphone,
   SIRET, IBAN, nom de client) est listée dans `analyse.json → zones_sensibles`
   et floutée au rendu.

## Ton

Français, vouvoiement. Phrases courtes, rythme vif. Ludique sans être puéril.
Compréhensible d'un débutant total, utile à un expert. Zéro jargon non expliqué
(un mot technique est défini en cinq mots à sa première occurrence). Jamais
« il suffit de », jamais « c'est très simple ». On dit ce que ça change pour
l'utilisateur avant de dire où cliquer.

## Charte RapidoSoftware

| Rôle | Couleur |
|---|---|
| Gris primaire (texte, titres) | `#383838` |
| Vert RapidoCRM (dominante) | `#4CAF50` |
| Violet RapidoRH (contrepoint) | `#7E57C2` |
| Bleu RapidoCMS (accent) | `#03A9F5` |
| Fond clair | `#F2F4F7` |
| Blanc | `#FFFFFF` |

- **Police unique : Arial** (Helvetica en repli). Aucune autre — sauf la carte
  prompt de la séquence 4, qui porte la charte Claude (voir plus bas).
- **Contraste** : sur un aplat de couleur, le texte est uniquement blanc ou
  `#383838`. Jamais de texte coloré sur fond coloré. Utiliser `textOn(bg)`.
- **Logo** : jamais déformé (scale uniforme seulement), **jamais tourné**,
  uniquement sur blanc / `#F2F4F7` / en défonce sur un aplat de la charte.
  Zone de protection = 2× la hauteur du logomark. Taille minimale = 8 % de la
  hauteur de frame.
- Le logomark est un trio d'oiseaux origami low-poly (vert, bleu, violet).

## MCP utilisés

| MCP | À quoi il sert |
|---|---|
| `RapidoCRM` | Comprendre le logiciel : outils réels, schémas de paramètres, données de démo en lecture |
| `RapidoCMS` | Déposer les médias dans la bibliothèque, obtenir les liens AWS S3 |
| `YouTube` | Publier sur la chaîne, vignette, playlist, SEO |
| `RapidoCMS tutoriels` | Remplir et publier la page du tutoriel sur le site Lovable (publication immédiate, sans validation) |

Le pipeline Node **n'appelle pas les MCP directement** : ce sont des outils de
Claude Code. Le pont est le protocole de `src/mcp/pont.ts` — le pipeline écrit
une demande dans `content/<module>/<Vxx>/mcp/<nom>.demande.json`, Claude Code
exécute l'appel MCP et dépose la réponse dans `<nom>.reponse.json`, validée par
zod. Voir `src/mcp/README.md`.

## Images du présentateur

`assets/presentateur/` contient les **16 photos détourées du présentateur
RapidoCRM**, partagées par les 172 tutoriels. On ne les régénère jamais : on
pioche dedans.

- `src/brand/presentateur.ts` décrit chaque pose (intention, direction du
  regard) et sépare les poses de **hook** (le problème : surpris, réflexion,
  stop, présentation…) de celles d'**image de fin** (le résultat : victoire,
  deux pouces, OK, casque…).
- Le choix est **déterministe** : `poseHook(module, numero)` et
  `poseFin(module, numero, titre)` donnent toujours la même pose pour un
  tutoriel donné. La pose de fin suit d'abord le contenu (voir « La fin de
  vidéo »), l'empreinte ne servant qu'en dernier recours.
- Les fichiers sont en WebP avec canal alpha : le présentateur se pose
  directement sur les aplats de la charte, sans cadre. Il est calé sur le bord
  bas de la frame — la photo source est coupée au buste.

## Le présentateur en bulle, et l'avatar

Méthode reprise du projet **Plan'It** (`videos/planit-tuto-00-creer-son-compte/AVATAR.md`
et `videos/planit-academy/habillage/presentatrice.py`), qui a fait ses preuves sur
43 épisodes.

**Le principe.** La synchronisation labiale part d'un **rendu image fixe**, pas
du modèle 3D : le `.glb` sert à produire les images, ce sont elles qui alimentent
le modèle. Portrait + piste voix → `creatify-aurora` (ElevenLabs) → plan parlant.

**L'avatar RapidoCRM.** `assets/avatar/manager.glb` est le modèle fourni ;
`assets/avatar/rendus/` en conserve les trois rendus (buste, mi-corps,
plein-pied). C'est le **buste** qui sert de portrait : tête et épaules, 768 × 840,
fond studio uni — le cadrage que `creatify-aurora` attend.

**La voix passe par-dessus.** Le plan est monté **muet** : il n'apporte que les
yeux et la bouche. La voix off du tutoriel, elle, vient de la piste `voix/` et
joue par-dessus. Les lèvres ne prononcent donc pas les mots entendus — c'est le
compromis assumé du plan unique réutilisé, celui que Plan'It a retenu pour ses
43 épisodes.

**La boucle est en aller-retour.** Bout à bout, un plan de huit secondes rebouclé
saute visiblement à chaque tour. `preparerBoucleAvatar` monte donc le clip suivi
de lui-même à l'envers, puis répète l'ensemble : le mouvement se retourne sans
rupture. Cette étape ne coûte rien, le plan payant reste unique.

**Un seul plan pour toute la série.** Le plan est rendu **une fois**, sur un texte
générique, puis réutilisé par les 172 tutoriels et bouclé en aller-retour pour
éviter le saut du raccord. C'est le seul poste facturé à la seconde : un plan de
8,6 s coûtait 1,39 $ chez Plan'It. Un plan par épisode multiplierait ce coût par
172 sans rien apporter, puisque le titre est déjà affiché à l'écran.

**Le repli, gratuit.** Sans `assets/avatar/parle.mp4`, la bulle affiche
`assets/avatar/portrait.webp` : l'habillage reste animé, seule la bouche ne bouge
plus. C'est le mode d'itération — on ne relance une génération payante que
lorsque la mise en page est arrêtée.

**L'habillage** (`src/brand/Avatar.tsx`) est calculé localement, sans rien
facturer : bulle en `easeOutBack`, anneau dégradé en rotation lente dont
l'épaisseur suit la voix, halo dont le rayon suit la voix, et treize barres de
niveau où l'onde se propage du centre vers les bords. **C'est la voix qui pilote
l'animation, jamais l'inverse** — `src/template/niveauVoix.tsx` lit l'enveloppe
de la piste avec `visualizeAudio`.

**Où se place la bulle**

| Format | Place | Répartition |
|---|---|---|
| 16:9 | en bas à droite, par-dessus le mockup | bulle à 20 % de la hauteur |
| 9:16 | en haut, au-dessus du logiciel | **1,5 pour l'avatar · 2,5 pour le logiciel**, sur 4 parts |

**Le logiciel est toujours dans un mockup** (`src/brand/Mockup.tsx`) : fenêtre de
navigateur avec barre de titre, pastilles et adresse. Sans ce cadre, un
enregistrement large se retrouve rogné par les bords en 9:16 et on ne comprend
plus qu'on regarde un logiciel.

## La carte prompt porte la charte Claude

Exception assumée à la règle « Arial et palette RapidoSoftware partout » : la
carte de la séquence 4 représente **Claude**, comme une capture d'écran porterait
l'interface qu'elle montre. Elle utilise donc la charte d'Anthropic
(`src/brand/claude.ts`) :

| Rôle | Valeur |
|---|---|
| Fond de carte | `#faf9f5` |
| Texte | `#141413` |
| Accent (bouton, surlignage des variables) | `#d97757` |
| Gris de libellé | `#b0aea5` |
| Titres | Poppins, Arial en repli |
| Corps du prompt | Lora, Georgia en repli |

Le logo Claude (`assets/ia/claude.png`) ouvre l'en-tête, suivi du nom de l'outil
MCP visé. **Le reste de la frame reste à la charte RapidoSoftware.**

## La fin de vidéo

- **Le logo officiel** `assets/logos/rapidocrm-complet.png` est monté **tel
  quel** : jamais redessiné, jamais tourné, scale uniforme.
- Il se pose en deux temps : un halo s'ouvre une seule fois derrière lui, un
  trait vert se trace dessous, puis le slogan et l'adresse suivent.
- **Le présentateur reste d'un bout à l'autre** de la séquence : il porte la
  punchline, puis accompagne la carte de fin.
- **La pose vient du contenu**, pas d'un tirage : `poseFin(module, numero, titre)`
  applique des règles — compte et accès → accueil, équipe → bras ouverts, support
  → casque, facture et contrat → OK, campagne et workflow → victoire. L'empreinte
  ne sert qu'en dernier recours, pour répartir les poses restantes.

## Autres assets partagés

- `assets/ia/` — logos des assistants. **Seul `claude.png` est monté**, dans
  l'en-tête de la carte prompt (séquence 4) : c'est une décision prise, la
  séquence dit « collez-le dans Claude » et reste sur un seul assistant.
  `openai.png` et `mistral.png` restent en réserve, non montés — ne les ajouter
  au template que sur demande explicite.
- `assets/ecrans/` — la **banque d'écrans RapidoCRM** (17 maquettes fournies
  par l'équipe produit), décrite par `src/brand/ecrans.ts` : titre, module,
  mots-clés, et `cadrage` (`capture` = l'écran remplit le cadre, utilisable
  comme plan de démonstration ; `mockup` = ordinateur en situation, illustration
  seulement). `ecranPour(module, titre, cadrage)` choisit le meilleur écran, ou
  **rien** si aucun ne correspond vraiment — mieux vaut pas d'écran qu'un écran
  hors sujet. `npm run ecrans` liste la banque, `--pour "<titre>"` montre le
  choix retenu.

  Ces maquettes ne remplacent jamais l'enregistrement réel d'un tutoriel publié.
  Quand `source.mp4` manque, le rendu retombe dessus **avec un avertissement** :
  la vidéo se monte, mais la démonstration n'est pas une vraie capture.

Tous ces dossiers (`presentateur/`, `ia/`, `ecrans/`, `avatar/`) sont recopiés dans
`public/` par `copierAssetsPartages`, appelé au rendu et par
`npm run prepare:assets`.

## Le montage de référence — V01 « Créer un compte »

`content/Configuration/V01-creer-un-compte` est le **montage étalon**. Les
170 tutoriels suivants s'en déduisent : mêmes séquences, mêmes proportions,
mêmes règles. On ne réinvente pas une mise en page par vidéo — on rejoue
celle-ci et on ne change que le contenu.

Enchaînement, identique pour tous :
ouverture (vignette dans un mockup) → hook → titre → démonstration →
carte prompt Claude → punchline → carte de fin.

**16:9** — l'écran du logiciel occupe le cadre, la bulle avatar se pose en bas
à droite, les sous-titres sont **superposés** en bas de l'image, la barre de
chapitre court en pied d'écran.

**9:16** — répartition **1,5/4 pour l'avatar, 2,5/4 pour le logiciel** :

- bulle avatar en haut (`bulle(0.115, 4)`) ;
- puis le mockup du logiciel, **pleine largeur et jamais recadré** : marges
  latérales réduites à `height * 0.012`, le mockup adopte le `demoRatio` de la
  source. On n'ampute jamais l'interface pour gagner en lisibilité — ni bande
  horizontale, ni « colonne utile » ;
- **interdiction absolue de superposer du texte à la vidéo du logiciel.**
  Sous-titres et libellé d'étape passent **sous** la vidéo, dans leur propre
  zone (`SousTitres placement="dans-le-flux"`). Sur l'écran, seul le cercle
  vert pulsé reste, pour désigner la zone active ;
- barre de chapitre en bas.

Le reste du dispositif est déjà décrit plus haut et ne bouge pas d'une vidéo à
l'autre : une **seule** animation d'avatar générée avec ElevenLabs, muette et
bouclée en ping-pong, avec la voix off posée par-dessus ; la carte prompt à la
charte Claude ; la fin au logo officiel avec la pose du présentateur choisie
par le contenu.

## Publication — l'ordre imposé

Toujours dans cet ordre, pour chaque tutoriel, sans en sauter aucune :

1. `npm run qa` — **rouge = on ne publie pas**. `fiche.a_verifier` doit être
   vide : un point non tranché est un point qu'on ne raconte pas.
2. `npm run publier:cms` — dépôt des 4 médias (master 16:9, master 9:16,
   les deux vignettes) dans la bibliothèque RapidoCMS, liens AWS S3 en retour.
   L'upload est idempotent : même empreinte de fichier, pas de réupload.
3. `npm run publier:youtube` — la vidéo normale (16:9) **et** le Short (9:16),
   à partir des liens AWS de l'étape 2.
4. `npm run publier:site` — remplissage complet puis mise en ligne sur
   RapidoCRM Académie. **La page part en ligne sans validation admin** : tout
   ce qui est écrit ici est publié tel quel.

La page du site se remplit **entièrement**, jamais à moitié : titre et titre
court, accroche, « comment ça marche » (l'intro puis les étapes numérotées,
puis le segment Claude), à quoi ça sert, prérequis, étapes, vignette
récupérée via le MCP RapidoCRM Académie, vidéo, vidéo verticale, lien YouTube,
transcription et chapitres, astuces, cas d'usage, prompt Claude à copier-coller
avec ses variables et son outil MCP, SEO (titre, description, mots-clés,
image), et les instructions de l'agent IA de la page.

Deux dépendances externes, sans lesquelles rien ne part :

- `RAPIDO_ACADEMIE_API_KEY` dans `.env` — le `cle_api` qu'exige **chaque**
  outil du MCP RapidoCRM Académie. Il se génère dans `/admin/parametres`.
- une **chaîne YouTube connectée** au MCP YouTube.

Le paramètre `module` de `creer_tutoriel` attend le **slug** du module, pas son
nom : `01-configuration`, pas `configuration`. `lister_modules` donne la liste
exacte. Un slug inconnu fait échouer l'appel avec « Module introuvable ».

Le MCP RapidoCMS n'avale un fichier que depuis une **URL publique**
(`upload_file_tool(file_url)`) : un master qui n'est que local ne peut pas être
déposé. Ne jamais contourner en écrivant directement dans le bucket S3.

## LinkedIn — une publication par tutoriel

Chaque tutoriel part aussi sur **LinkedIn**, sur la page **RapidoSoftware**
(compte RapidoCMS `id 32`, `account_id 101119107`) — jamais sur FoodEatUp,
BraindCode ou un profil personnel. Le montage publié est le **9:16**, plus lisible
dans le fil.

Le post se tient à trois choses, dans cet ordre :

1. **le problème concret** que le tutoriel règle, en une ou deux phrases, dans les
   mots du métier — pas « découvrez notre fonctionnalité » ;
2. **ce que le logiciel fait**, montré et non promis : ce que l'on voit à l'écran,
   en combien de temps ;
3. **l'invitation à une démo**, avec le numéro WhatsApp **06.14.18.92.25**.

Ton : professionnel, sobre, à la première personne du pluriel. On vouvoie. On
donne envie d'essayer le logiciel en montrant qu'il fait gagner du temps, jamais
en survendant. Pas d'emoji en rafale (deux au maximum, jamais dans la première
ligne), pas de superlatif, pas de « révolutionnaire », pas de « il suffit de ».
Trois à cinq hashtags en fin de post, sobres : #CRM #RapidoCRM et le domaine
métier du tutoriel.

Le lien vers la page du tutoriel sur l'Académie va **en fin de post**.

## La voix off — une seule, pour les 172 tutoriels

**« Enrick - Calm French Narrator » — `voice_id: 0xHziZolI8Tp6rLtUqh2`.**
Voix masculine française, âge moyen, calme et rassurante, diction précise,
accent standard, décrite pour la narration, les vidéos tutorielles et
l'e-learning. Validée sur V01, elle est la voix de toute la série.

Elle est **écrite en dur** dans `src/pipeline/voix.ts` (`VOIX_SERIE`) : le
`voice_id` ne se déduit jamais d'un autre projet du dépôt — les voix maison de
`studio-video/` ou de FoodEatUp ne sont **pas** celle de RapidoCRM Académie.
`ELEVENLABS_VOICE_ID` ne sert qu'à un essai ponctuel. Modèle :
`eleven_multilingual_v2`.

Sans `ELEVENLABS_API_KEY`, les blocs peuvent être produits par le MCP
ElevenLabs (`creative_generate_speech`, `generations_count: 1`) puis déposés
dans `voix/<bloc>.mp3` : le pipeline reprend une piste déjà présente au lieu
d'échouer.

### Le cache mutualisé

`assets/voix-cache/` garde une piste par couple (voix, texte). Une phrase
identique d'un tutoriel à l'autre — l'invitation à copier le prompt, une
punchline reprise, une étape formulée pareil — **n'est synthétisée qu'une
fois**, puis recopiée. Le cache se remplit quelle que soit l'origine de la
piste : synthèse par l'API, reprise, ou fichier déposé à la main. Sur 172
tutoriels dont les segments Claude se ressemblent beaucoup, c'est le poste
d'économie principal.

Corollaire à la rédaction : quand une formulation identique convient à
plusieurs tutoriels, **la reprendre au mot près** plutôt que la paraphraser.

### L'ouverture montre la vignette du tutoriel

La vidéo s'ouvre sur la vignette **dans un mockup de navigateur**. Elle vient en
priorité de `vignette.jpg`, déposée dans le dossier du tutoriel : c'est la
vignette de l'Académie, récupérée une fois sur
`https://academie-rapidocrm.lovable.app/api/public/vignettes/<slug>.jpg` et
versionnée avec le tutoriel. Aucune clé d'API, aucun appel réseau au rendu,
aucune ouverture sur un mockup vide. Les autres sources (lien AWS de
`publication.json`, fiche en ligne via le MCP, `out/thumb-16x9.jpg`) ne servent
que de repli.

### Le pitch d'ouverture

L'intro dit **ce qu'on va voir à l'écran**, pas seulement ce qu'on va faire.
Elle nomme la page de départ et la page d'arrivée, et annonce en une phrase le
bénéfice concret. Elle ne récite pas la liste des étapes — la démonstration
s'en charge — et elle ne commente jamais l'habillage (« voici une maquette »,
« sur cette capture »). Le spectateur doit comprendre où il est et pourquoi ça
vaut le coup de rester, en deux phrases.

### Ne pas marteler « C.R.M. »

**Au plus une occurrence de « C.R.M. » par bloc de voix**, et jamais deux fois
dans la même phrase. Ailleurs, on désigne le logiciel autrement : « votre
espace », « le logiciel », « RapidoCRM », « votre tableau de bord », ou tout
simplement rien du tout — « vos clients », « vos factures » suffisent souvent.
La répétition s'entend beaucoup plus à l'oral qu'elle ne se voit à l'écrit.

## Nommage des sorties

```
content/<module>/<Vxx-slug>/
  source.mp4  analyse.json  fiche.json  script.json  script.md
  voix/{hook,intro,etape-01…,claude,punchline}.mp3
  voix/{alignement.json,complete.mp3,manifest.json}
  transcription.txt  transcription-chapitres.json
  out/master-16x9.mp4  out/master-9x16.mp4
  out/thumb-16x9.jpg   out/thumb-9x16.jpg
  rendu.json  qa.json  publication.json  pipeline.log
```

Fichiers déposés dans la bibliothèque RapidoCMS :
`rapidocrm-tuto-<module>-<Vxx>-<slug>.mp4` (`-vertical`, `-thumb`,
`-thumb-vertical` pour les autres).
