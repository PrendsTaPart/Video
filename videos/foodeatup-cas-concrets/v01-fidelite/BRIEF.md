# Vidéo 1 — 250 couverts, 10 fidèles

**✅ Montage assemblé** — `renders/video-01-fidelite.mp4` (29s, 1080×1920, prêt à publier
sous réserve de validation de Michael). Voir "Montage final" en bas de fichier.

**Restructuration 2026-08-09** : SOLUTION et RÉSULTAT fusionnés en un seul segment (11–25s)
suite à la demande de Michael ("il manque la voix off qui présente le logiciel") — l'avatar
HeyGen apparaît maintenant **par-dessus** le logiciel (en haut de l'écran) et le présente à
la voix pendant 7.3s, puis disparaît en fondu pour laisser le logiciel seul jusqu'à la fin
du segment. Le bloc RÉSULTAT autonome (25–32.3s) n'existe plus — durée totale de la vidéo
ramenée de 36.3s à **29s**.

**Bug corrigé (2026-08-09)** : le premier rendu masquait HOOK et PROBLÈME derrière un fond
crème vide pendant 11s (Michael : "on ne voit pas la séquence Higgsfield", "il manque la
voix off"). Cause : `#solution-crop` était un `<div>` conteneur SANS `data-start`/`data-duration`
— un élément non minuté est peint sur **toute** la durée de la composition (0–36.3s), pas
seulement pendant la fenêtre où son contenu minuté à l'intérieur est actif. Étant plus loin
dans le DOM que HOOK et PROBLÈME, il se peignait par-dessus eux tout du long, mais restait
en dessous de RÉSULTAT/PUNCHLINE (plus tard dans le DOM) — d'où un bug qui touchait
uniquement les deux premiers segments. Fix : fond, logiciel, trait accent et logo du
segment SOLUTION sont maintenant 4 clips SIBLINGS correctement minutés (`data-start="11"
data-duration="14"`), plus de wrapper non minuté. Ajouté au passage : une animation
(logo "8" qui respire + trait orange) dans l'espace sous le logiciel, suite à la demande
"il manque l'animation en bas de la vidéo du logiciel". Vérifié image par image sur
l'ensemble des 36.3s (24 échantillons) + niveaux audio (`ffmpeg volumedetect`) avant
renvoi — voir `snapshots/fix2-sheet-*.jpg`.

Statut des 4 segments (2026-08-09, après fusion SOLUTION+RÉSULTAT) :

| Segment | Durée réelle | Statut | Détail |
|---|---|---|---|
| HOOK | 0–3s | ✅ | `assets/hook/hook-intro.mp4` |
| PROBLÈME (Higgsfield) | 3–11s | ✅ | `assets/higgsfield/probleme.mp4` — chef de dos, salle qui se vide, clients qui partent. 720×1280, 24fps ; fenêtre 0–8s utilisée. Palette plus chaude que demandé (grise/désaturée dans le prompt) mais cadrage et action conformes. |
| SOLUTION + RÉSULTAT (fusionnés) | 11–25s | ✅ | `assets/solution/programme-fidelite.mp4` en fond (pleine largeur, sans recadrage, centré en bas d'écran, fenêtre source 14–28s) + `assets/heygen/resultat.mp4` par-dessus en haut (11.3–18.598s, sa durée réelle de 7.298s) qui présente le logiciel à la voix, puis disparaît en fondu pour laisser le logiciel seul jusqu'à 25s. Trait accent orange entre les deux. |
| PUNCHLINE | 25–29s | ✅ | `assets/punchline/punchline-outro.mp4` |

## Prompt Higgsfield à générer manuellement

Référence image 1 : `studio-video/assets/brand/profile/michael-chef-mascot.jpg`

```
Plan unique continu de 8 secondes, vertical 9:16, 4K, 24 images/seconde, style
documentaire, grain fin. Palette froide et désaturée : gris #8A9099, surfaces #EDEEF0,
encre #3A3F45. Lumière plate de néon, sans chaleur. Référence image 1 = photo du chef :
visage, morphologie et tenue à conserver strictement à l'identique. Son d'ambiance seul,
aucune voix, aucune musique. Aucune coupe, aucun personnage dupliqué, aucun texte à
l'écran, aucun logo, aucune marque ni application identifiable, aucun sous-titre.

Action : fin de service, le chef debout au comptoir regarde une salle qui se vide, les
tables se libèrent une à une, les clients sortent sans un mot ni un regard vers lui. Il
reste seul devant l'entrée.
Caméra : plan fixe depuis le fond de la salle, très légère avancée.
Son : chaises, porte, brouhaha qui s'éteint.
Fin de plan : la salle vide, lui de dos.
```

## Script HeyGen (avatar Mika)

```
Vidéo avatar de 8 secondes, format vertical 9:16, 1080 × 1920. Avatar : homme, la
quarantaine, veste de cuisine blanche col ouvert, cadrage buste, regard caméra. Décor :
cuisine professionnelle floutée en arrière-plan, tons chauds. Voix française masculine,
ton posé et direct, débit naturel, pas de ton commercial. Sous-titres désactivés — ils
sont ajoutés au montage. Aucun logo, aucun texte incrusté.

Script exact : « Tu ne perds pas des clients. Tu ne les reconnais pas. Le programme se
déclenche à la première visite, et le deuxième passage arrive tout seul. »
```

## Problème sur le clip HeyGen reçu (2026-08-09)

`assets/heygen/resultat-v1-a-refaire.mp4` (1080×1920, 25fps, 7.56s) — le chef Mika dit bien
le bon texte, la voix est bonne. Mais ce n'est pas un avatar "propre" comme demandé dans le
plan :

- Il ne parle que **~3 secondes** (« Tu ne perds pas des clients. Tu ne les reconnais
  pas. »), puis le clip **coupe sur un template graphique générique** HeyGen pendant les
  ~4,5s restantes : fond bleu, titre « FIDÉLITÉ AUTOMATIQUE », sous-titre « L'expérience
  client réinventée », photo stock d'une femme avec une tablette (pas un vrai visuel
  FoodEatUp), fin du texte incrustée dedans.
- **Logo FoodEatUp et sous-titres brûlés à l'image** sur toute la durée — le plan les veut
  ajoutés au montage, pas incrustés par HeyGen (pour rester dans notre propre habillage,
  cohérent avec le carton HOOK/PUNCHLINE déjà fait).

→ Ça vient du **type de génération choisi dans HeyGen Studio** : un mode "template/scene"
plutôt qu'un export "avatar seul". Pour la vidéo 1 (et pareil pour les 9 suivantes), il
faut régénérer en choisissant l'option **avatar seul / plan unique**, sans template de
scène ni sous-titres/logo intégrés — juste Mika qui parle les 8 secondes pleines, cadrage
buste, fond de cuisine flouté, comme décrit dans le script ci-dessus. C'est ce clip-là que
je monterai avec nos propres sous-titres et notre propre logo (déjà faits dans
`../motion/`).

## Montage final

`index.html` (projet HyperFrames autonome, 1080×1920, `npx hyperframes render . -q high -o
renders/video-01-fidelite.mp4`) concatène les 4 segments en coupes franches (pas de
crossfade, cohérent avec le rythme TikTok voulu) :

- HOOK et PUNCHLINE : mp4 déjà rendus dans `../motion/`, copiés tels quels.
- PROBLÈME : `assets/higgsfield/probleme.mp4`, fenêtre 0–8s, son d'ambiance à 0.6.
- SOLUTION+RÉSULTAT fusionnés (11–25s, 14s) :
  - `assets/solution/programme-fidelite.mp4` en fond, affiché pleine largeur (1080px = la
    largeur source complète, échelle 0.5625, donc **aucun recadrage, rien n'est coupé**),
    centré en bas d'écran, fenêtre source 14–28s (configuration des règles, clic sur
    "Enregistrer le programme", confirmation). Trois itérations avant cette version : d'abord
    un recadrage/pan serré (refait car "ne le coupe pas"), puis logiciel plein cadre ancré en
    haut avec juste le logo (refait car "il manque la voix off qui présente le logiciel").
  - `assets/heygen/resultat.mp4` par-dessus, en haut de l'écran (recadré à la hauteur de sa
    boîte, buste + visage, aucune déformation), actif 11.3–18.598s (sa durée réelle), fondu
    entrée/sortie ; le logiciel reste seul le temps restant du segment.
  - Trait accent orange entre les deux zones.
- Vidéo muette + `<audio>` séparé pour les segments avec son (règle HyperFrames : la
  `<video>` reste `muted`, le son passe par un `<audio>` distinct même sur la même source).

## Historique du clip HeyGen (2026-08-09)

Deux clips reçus avant le bon :
1. `resultat-v1-a-refaire.mp4` — seulement ~3s d'avatar puis coupe sur un template
   générique HeyGen (fond bleu "Fidélité automatique", photo stock, logo+sous-titres brûlés).
   Venait d'un mode "template/scène" dans HeyGen Studio plutôt qu'un export avatar seul.
2. Le même fichier redéposé (hash identique) — pas une nouvelle génération.

Le clip final (`assets/heygen/resultat.mp4`) vient d'un export avatar seul, plan unique,
sans template : 8s pleines de Mika qui parle, aucun élément incrusté.
