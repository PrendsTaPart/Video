# RAPPORT — vidéo « Chaînes »

---

## ⚠️ EN TÊTE : les quatre chiffres `[À CONFIRMER]` sont TOUJOURS OUVERTS

C0 : *« Si un seul chiffre est encore ouvert, écris-le en tête du rapport : la vidéo
ne part pas en prospection avec un trou. »* Les quatre le sont.

| # | Chiffre attendu | Statut |
|---|---|---|
| 1 | Taux d'invendus moyen d'une chaîne de boulangerie | **non fourni** |
| 2 | Écart de food cost constaté entre sites d'une même enseigne | **non fourni** |
| 3 | Délai moyen de remontée d'un consolidé en restauration multi-sites | **non fourni** |
| 4 | Toute économie chiffrée attribuée à FoodEatUp | **non fourni** |

**Conséquence, et elle est assumée :** la vidéo est montée en **version sans chiffres**.
Aucun pourcentage, aucun montant, aucune quantité à l'écran ni dans la voix off —
l'écart est *montré*, jamais quantifié, et « plusieurs semaines » remplace partout
« six semaines ». C'est la clause C0 : poser la question plutôt qu'affirmer la réponse.

Elle est donc **diffusable telle quelle** sans risque de se faire retourner un chiffre
en rendez-vous. Elle est simplement moins tranchante qu'avec des chiffres réels.

### Second point ouvert, de nature différente

**La vue consolidée multi-établissements n'existe pas dans le MCP FoodEatUp.** Les
~250 outils prennent tous un `establishment_id` singulier et obligatoire ; aucun
n'accepte plusieurs sites, aucun ne liste les établissements, aucun rôle « siège ».
Les **séquences 5, 6 et 8** montreraient un écran non vérifié : **elles ne sont pas
produites**. Réserve : ce constat porte sur la surface MCP, pas forcément sur
l'application web — à trancher par Michael.

---

## Ce qui est livré

| Livrable | Durée | Fichier |
|---|---|---|
| Master boulangerie | **77,00 s** | `boulangerie/out/foodeatup-chaines-boulangerie-master-v1.mp4` |
| Master restauration | **77,00 s** | `restauration/out/foodeatup-chaines-restauration-master-v1.mp4` |
| Bloc variante seul (boulangerie) | 55,00 s | `…-boulangerie-seq1-4-v1.mp4` |
| Bloc variante seul (restauration) | 55,00 s | `…-restauration-seq1-4-v1.mp4` |
| Bloc de fin (séq. 7 + 9) | 22,00 s | `fin/out/foodeatup-chaines-fin-v1.mp4` |
| Vignettes (×2 par variante) | — | `…-thumbnail.jpg` et `…-thumbnail-mot.jpg` |

Tous : 1920×1080, H.264, 25 fps, audio AAC 48 kHz stéréo, crête ≈ −4,3 à −4,8 dBFS.

**Écart au plan C4 :** le master devait faire ~120 s (séquences 1 à 9). Il fait 77 s
parce que les séquences 5, 6 et 8 sont bloquées. Les séquences 7 et 9 ont pu être
produites : elles ne contiennent aucun écran produit.

---

## Coût réellement dépensé

| Outil | Appels | Consommation |
|---|---|---|
| ElevenLabs `text-to-speech` | 13 (3 essais de voix + 10 lignes retenues) | — |
| ElevenLabs `music` | 2 (nappe 55 s + nappe 77 s) | — |
| ElevenLabs `sound-generation` | 5 bruitages | — |
| **Total ElevenLabs** | **20 appels** | **6 299 caractères** (13 016 / 122 330 sur le cycle) |
| RapidoCMS `generate_image` | 4 (carnet, fournée, plat, carte de France) | — |
| HyperFrames `render_video` | **0** | **0 crédit** |

**Le rendu HyperFrames n'a jamais été facturé** : le MCP refuse l'import
(`Import URL host is not an allowed Claude Design origin`), aussi bien depuis
`raw.githubusercontent.com` que depuis une URL d'artifact Claude. La voie d'import
passe par le bouton « Send to HyperFrames » côté Claude Design. Les MP4 livrés ont
donc été produits par capture temps réel dans Chromium puis encodage H.264.

Pour mémoire, si vous passez par le rendu cloud : l'import est gratuit, le rendu est
facturé **20 crédits par minute rendue** — soit ≈ 26 crédits par master de 77 s.

### Deux écarts entre ces MP4 et un futur rendu cloud

1. La transition shader `cinematic-zoom` (s2 → s3, à 27,75 s) est remplacée par un
   **fondu croisé de 0,5 s** au même instant : les shaders WebGL plantent le renderer
   headless. Les `index.html` gardent bien le shader.
2. Le son est ajouté par `_shared/mixaudio.py` ; dans le pipeline HyperFrames il
   s'ajouterait à l'étape « enhance ».

---

## Contrôles passés

- `_shared/check.py` : **41/41** sur chaque variante, **34/34** sur le bloc de fin
  (contrat d'import, déterminisme, assets auto-portés, palette, absence de chiffre).
- **Balayage image par image (4 img/s) des trois blocs et des deux masters : aucune
  image vide.** Ce contrôle a révélé un défaut réel — voir ci-dessous.
- Voix off : présente sur chaque séquence porteuse ; **la séquence 2b est vierge de
  voix** (le brief impose trois secondes sans VO), mesuré à −30,3 dB, nappe seule.
- Jonction variante → fin (55 s) : −34,9 dB sur 1 s, aucun mot coupé.
- Bruitages : chacun émerge de 7 à 14 dB au-dessus de la nappe, mesuré à sa crête.

### Le défaut trouvé, et pourquoi il avait échappé aux premiers contrôles

Un **flash d'image entièrement vide à chaque coupe de scène**. Cause : GSAP applique
l'état de départ des `tl.from()` dès la construction (`immediateRender`) ; la scène
entrante était donc visible alors que tout son contenu était encore invisible, jusqu'à
son premier tween calé 0,2 s plus tard.

Il avait échappé à deux vérifications successives, pour deux raisons cumulées :

- **un mauvais critère** — je comptais les « pixels sombres », ce qui rate le contenu
  clair (carnets estompés, texte fin) et faisait passer des images pleines pour vides
  et l'inverse. Le bon critère est « pixels différents du fond crème » ;
- **un décalage de trim** — le point de départ de la capture était estimé à la main
  (5,28 s au lieu de 4,96 s réels), donc les sondages tombaient à côté des coupes.

`_shared/render.py` **détecte** désormais ce point de départ au lieu de l'estimer, et
balaie tout le fichier à la recherche d'images vides.

---

## Publié sur RapidoCMS — 2026-08-08

Michael a validé explicitement (« tu peux publier sur RapidoCMS »). Les quatre
fichiers sont déposés dans la bibliothèque et vérifiés : taille identique à l'octet
près à la source, type MIME correct.

| Nom dans la bibliothèque | Type | id | Taille |
|---|---|---|---|
| `foodeatup-chaines-boulangerie-v1` | video | 1235 | 6 738 248 o |
| `foodeatup-chaines-restauration-v1` | video | 1236 | 5 314 039 o |
| `foodeatup-chaines-boulangerie-thumbnail` | image | 1237 | 75 254 o |
| `foodeatup-chaines-restauration-thumbnail` | image | 1238 | 69 498 o |

Les deux `-short-v1` prévus par C4 ne sont pas déposés : la version courte n'est pas
produite (voir plus bas).

**Aucune publication sociale n'a été programmée.** L'accord portait sur le dépôt dans
RapidoCMS ; `create_draft_tool` / `schedule_draft_tool` vers LinkedIn est une étape
distincte, qui n'a pas été demandée.

## Non fait, et pourquoi

- **Séquences 5, 6 et 8** — bloquées sur la vue groupe (voir plus haut).
- **Version courte 45 s** — C4 la définit comme séquence 2 + séquence 6 + séquence 9.
  La séquence 6 étant bloquée, elle se réduirait à séquence 2 + séquence 9, soit ≈ 28 s.
  Et C4 impose de **proposer la voix off réduite AVANT de la générer** : la proposition
  est ci-dessous, rien n'a été généré.
- **Pull request** — non ouverte : `videos/FOODEATUP-TUTORIELS-WORKFLOW.md` note que le
  dépôt n'a pas de branche `main` distincte, la branche désignée EST la branche par
  défaut. Tout est poussé sur `claude/foodeatup-chaines-video-1vij8y`.
- **Higgsfield** — le serveur MCP n'était pas connecté quand les assets ont été
  produits ; il l'est depuis. Rien n'en a été utilisé.

### Proposition de voix off pour la version courte (à valider avant génération)

> « Vos douze sites vendent la même chose, au même prix. Ils ne la produisent pas au
> même coût. L'écart entre le meilleur et le dernier, personne dans l'entreprise ne
> saurait le donner. Trois sites, soixante jours, vos chiffres. »

Une seule ligne, ~13 s, montée sur séquence 2 puis séquence 9.

---

## Reproduire

```bash
cd videos/foodeatup-chaines
python3 boulangerie/build.py && python3 _shared/check.py boulangerie/index.html
python3 _shared/render.py boulangerie          # capture + détourage + H.264
python3 _shared/mixaudio.py master-boulangerie # voix + nappe + bruitages
```

La voix off se régénère avec `ELEVENLABS_API_KEY=… python3 _shared/vo.py`.
La clé n'est jamais écrite dans le dépôt.
