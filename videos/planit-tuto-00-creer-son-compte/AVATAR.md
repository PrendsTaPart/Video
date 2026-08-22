# La présentatrice de l'Académie Plan'It

Qui elle est, ce qu'elle dit, et comment sa bouche s'anime.

Elle ouvre chaque tutoriel : elle annonce l'épisode, pose la promesse, puis passe
la main à la démonstration écran commentée en voix off.

---

## 1. Le modèle

Choisie dans **« Les avatars par défaut »** (Drive), parmi les quatre personas
fournis :

| Persona | Genre | Retenu |
|---|---|---|
| **Commercial** | femme — chignon, col roulé blanc, jupe noire | ✅ **la présentatrice** |
| RH | homme — costume marine, cravate rouge | — |
| Community manager | homme — chemise bleue, lunettes, casque | — |
| Chef Cuisinier | — | — (univers FoodEatUp) |

**Commercial** est la seule persona féminine du lot, ce qui la rend cohérente
avec la voix off féminine (*Perle*) déjà retenue pour la série. Sa tenue neutre
— blanc et noir — ne concurrence pas le violet et le rose de la charte Plan'It.

Chaque persona du Drive fournit un `.glb` (3D) et un dossier `images` de rendus.
Ce sont les rendus qui servent ici : la synchronisation labiale part d'une image
fixe, pas du modèle 3D.

**Fichiers**
- `assets/avatar-presentatrice.png` — portrait source, 1024 × 1280
- cadrage envoyé au modèle : tête et épaules, 768 × 840

---

## 2. Ce qu'elle dit

### Tutoriel 00

> « Bienvenue dans l'Académie Plan'It. Aujourd'hui, on commence par le tout
> début : créer votre compte. Une minute, et votre espace de travail est
> ouvert. »

**8,62 s** · voix ElevenLabs *Perle* (`UaGvaD7NWzU5mJNoUqoY`) · `vo/N0.mp3`

### Le gabarit, pour les 43 épisodes

Trois phrases, toujours la même structure :

```
Bienvenue dans l'Académie Plan'It.
Aujourd'hui : {TITRE DE LA FICHE}.
{PROMESSE DE LA FICHE, raccourcie}
```

Les deux variables sortent de `tutoriel_spec(numero: N)` — champs `titre` et
`promesse`. Exemple pour la fiche 13 :

> « Bienvenue dans l'Académie Plan'It. Aujourd'hui : brancher un serveur MCP.
> Vous ajoutez n'importe quel logiciel compatible en collant une adresse. »

**Contrainte** : rester **sous 10 secondes**. Au-delà, l'ouverture pèse trop lourd
devant une démonstration de 45 s, et le coût de synchronisation labiale monte
avec la durée.

### Ce qu'elle ne dit pas

Elle **n'explique pas les étapes** — c'est le travail de la voix off pendant la
démonstration. Elle annonce, elle situe, elle passe la main. Sa dernière phrase
se termine sur une intonation ouverte, qui appelle l'écran suivant.

---

## 3. L'animation de la bouche

### Le principe

Portrait fixe + fichier voix → **`creatify-aurora`** (ElevenLabs) → plan de
synchronisation labiale. Le modèle anime la bouche, la mâchoire, les clignements
et un léger mouvement de tête, calés sur l'audio réel.

```
assets/avatar-presentatrice.png ─┐
                                  ├─→ creatify-aurora ─→ out/avatar-talking.mp4
vo/N0.mp3 ───────────────────────┘
```

**Prompt de direction transmis au modèle :**

```
Talking-head presenter. The woman speaks the provided French audio directly to
camera, with accurate lip synchronisation, natural jaw and mouth movement, soft
blinking and subtle head motion. Warm, professional, welcoming expression — a
corporate trainer opening a tutorial. Camera static, framing unchanged, plain
grey studio background preserved.
```

### Le coût, mesuré

| | Valeur |
|---|---|
| Un plan de 8,6 s | **7 635 crédits ≈ 1,39 $** |
| Temps de rendu | ≈ 5 min |
| **Les 43 épisodes** | **≈ 60 $** |

C'est le seul poste facturé à la seconde de toute la chaîne. Deux façons de le
réduire, à trancher :

1. **Un plan par épisode** (≈ 60 $) — la présentatrice nomme le tutoriel, ce qui
   est plus vivant et plus utile au spectateur.
2. **Un seul plan générique réutilisé** (1,39 $ une fois) — texte neutre du type
   « Bienvenue dans l'Académie Plan'It. Je vous montre, pas à pas, comment tirer
   le meilleur de votre espace. » Le titre de l'épisode reste affiché à l'écran
   sous la bulle, mais n'est plus prononcé.

L'option 2 divise le coût par 43. L'option 1 est meilleure à regarder. Le reste
de la chaîne — habillage, bulle, barres, montage — ne coûte rien dans les deux
cas.

---

## 4. La bulle qui l'entoure

`build_presenter.py` place le plan parlant dans une bulle circulaire et dessine
tout l'habillage autour, **localement**, sans rien facturer.

| Élément | Comportement |
|---|---|
| Bulle | entrée en `easeOutBack`, puis respiration pilotée par la voix |
| Anneau dégradé | rotation lente ; épaisseur pilotée par la voix (16 → 28 px) |
| Halo | rayon et intensité suivant le niveau sonore |
| 13 barres de niveau | lisent l'enveloppe RMS du MP3, avec décalage latéral — l'onde se propage du centre vers les bords |
| Titre · promesse · chip | apparitions décalées, glissement vers le haut |

Le cadrage circulaire est **identique** pour le portrait fixe et pour chaque image
du plan parlant (`circular()`, même `top_ratio`) : la bulle ne saute pas au
changement de mode.

**Repli automatique** — sans `out/avatar-talking.mp4`, le script retombe sur le
portrait fixe. L'habillage reste animé, seule la bouche ne bouge plus. Utile pour
itérer sur la mise en page sans relancer une génération payante.

### Commandes

```bash
# avec synchronisation labiale
python3 build_presenter.py --talking out/avatar-talking.mp4

# portrait fixe (gratuit, pour itérer)
python3 build_presenter.py --talking /dev/null

# autre épisode
python3 build_presenter.py \
  --titre "Brancher un serveur MCP" \
  --promesse "Vous ajoutez n'importe quel logiciel compatible en collant une adresse." \
  --numero 13 --vo vo/N0.mp3 --talking out/avatar-talking.mp4
```

---

## 5. Refaire la synchronisation labiale

1. Générer la ligne de présentation (`creative_generate_speech`, voix *Perle*).
2. Téléverser le portrait et l'audio :
   `creative_create_asset_upload` → `PUT` des octets → `creative_finalize_asset_upload(flow_id)`.
   Chacun rend un `node_id`.
3. Lancer la génération :

```
creative_generate_in_flow(
  flow_id      = "sKOYDZDaS0015NSEy5C1",
  node_type    = "video-generation",
  model_id     = "creatify-aurora",
  connect_from = [<node image>, <node audio>],
  generations_count = 1,
  prompt       = "<le prompt de direction ci-dessus>")
```

4. `creative_get_flow_run_status` jusqu'à `all_completed`, puis télécharger le MP4
   vers `out/avatar-talking.mp4`.
5. `python3 build_presenter.py --talking out/avatar-talking.mp4`
6. `python3 build_video.py`

> Passer d'abord `estimate_only: true` pour connaître le coût avant de valider —
> c'est la seule étape payante à la seconde.
