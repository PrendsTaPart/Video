# Identité sonore & bulle avatar — Académie Plan'It

Trois couches sonores et un composant visuel, tous **réutilisables tels quels sur
les 43 tutoriels**. C'est le poste qui fait baisser le coût de production : une
seule génération pour toute la série, contre un plan d'avatar facturé par vidéo.

---

## 1. Les trois couches sonores

Toutes générées via le MCP **ElevenLabs**, flow `sKOYDZDaS0015NSEy5C1`.

| Couche | Fichier | Modèle | Durée | Placement | Niveau |
|---|---|---|---:|---|---:|
| **Animation sonore d'ouverture** | `audio/sting-intro.mp3` | `eleven_text_to_sound_v2` | 1,04 s | 0,90 s — sur l'arrivée du logo | −7 dB |
| **Musique produit** | `audio/musique-produit.mp3` | `eleven_music_v2` | 70,03 s | tout le film, duckée | −21 dB |
| **Identité sonore de fin** | `audio/signature-outro.mp3` | `eleven_text_to_sound_v2` | 2,04 s | début de l'animation de fin (57,5 s) | −5 dB |

### Prompts utilisés

**Ouverture** — *Short branded logo sting, 3 seconds. A soft airy whoosh rises and
sweeps in, landing on a bright crystalline bell chime with a warm synth pad bloom
underneath. Clean, modern, premium tech product. Ends with a gentle shimmering
tail. No drums, no voice.*

**Musique** — *Instrumental background bed for a software tutorial, 70 seconds, no
vocals. Calm optimistic modern electronic: gentle plucked synth arpeggio, soft warm
pad, light muted kick and soft rim percussion, subtle bass pulse. Steady around
95 BPM, major key, forward-moving but unobtrusive — it must sit far under a female
narrator without competing. Clean, premium, friendly productivity-software feel.
Consistent throughout with no dramatic build, no drop, no big finish.*

**Signature de fin** — *Sonic logo for a tech brand, 4 seconds. A confident rising
three-note motif on a warm bell-like synth, resolving upward to a satisfying final
note, wrapped in a soft pad swell and a light shimmer tail that fades out.
Optimistic, premium, memorable, conclusive. No drums, no voice, no speech.*

> Les deux effets sont sortis plus courts que demandé (1 s et 2 s au lieu de 3 s
> et 4 s) : `eleven_text_to_sound_v2` n'a pas suivi la durée indiquée dans le texte.
> Ils fonctionnent comme **accents ponctuels**, ce qui est le bon usage ici, la
> musique portant la continuité. Pour des durées exactes il faudrait passer par le
> paramètre `duration_seconds` du nœud SFX plutôt que par le prompt.

### Le mixage

La musique n'est pas simplement baissée : elle est **duckée par la voix** via un
`sidechaincompress` piloté par la piste de parole.

```
[music][voix] sidechaincompress=threshold=0.03:ratio=9:attack=12:release=420
```

Elle se retire dès que la narratrice parle et remonte dans les respirations —
notamment sous l'ouverture, entre les plans, et sur la fin après la punchline.

**Master** : `loudnorm=I=-16:TP=-1.5:LRA=11` → mesuré à **−16,0 LUFS, crête vraie
−1,4 dBFS**. Niveau de diffusion standard, sans écrasement.

---

## 2. La bulle avatar de présentation

`build_presenter.py` — carte de présentation de **8,60 s** placée juste après
l'animation d'ouverture.

### Pourquoi elle remplace le plan HeyGen

Un plan d'avatar généré coûte à chaque vidéo. La bulle, elle, est **dessinée
localement** à partir de l'avatar 3D officiel de l'application
(`assets/images/avatars/avatar_brunette.png` du dépôt `planit-app`). Sur 43
tutoriels, le seul coût récurrent devient **une ligne de voix off** — quelques
centimes — au lieu d'un rendu d'avatar par épisode.

Bonus : l'avatar est celui de l'app. La présentatrice de l'Académie et l'assistant
que l'utilisateur voit dans Plan'It sont la même personne.

### Ce qui est animé

| Élément | Animation |
|---|---|
| Bulle | entrée en `easeOutBack`, puis **respiration pilotée par la voix** (échelle 0,96 → 0,99) |
| Anneau dégradé | rotation lente continue, **épaisseur pilotée par la voix** (16 → 28 px) |
| Halo | rayon et intensité suivant le niveau sonore |
| Barres de niveau | 13 barres lisant l'enveloppe réelle du MP3, avec décalage latéral — l'onde se propage du centre vers les bords |
| Titre · promesse · chip | apparitions décalées, glissement vers le haut |

**L'animation lit vraiment l'audio.** `voice_envelope()` décode la voix en PCM
16 kHz mono via ffmpeg et calcule le RMS par image, avec une compression douce
(`^0.55`) pour que les passages faibles restent visibles. La bulle ne fait pas
semblant de parler : elle suit la parole.

### Réutilisation sur un autre tutoriel

```bash
python3 build_presenter.py \
  --titre "Brancher un serveur MCP" \
  --promesse "Vous ajoutez n'importe quel logiciel compatible en collant une adresse." \
  --numero 13 \
  --vo vo/N0.mp3
```

Les trois valeurs sortent directement de `tutoriel_spec(numero: N)` —
`titre`, `promesse`, `numero`. Seul `vo/N0.mp3` doit être regénéré par tutoriel.

---

## 3. La vignette

`build_thumbnail.py` — **2560 × 1440**, conforme au gabarit du MCP (1280 × 720,
facteur 2).

Le MCP **ne stocke pas d'image** : `vignette_spec(numero: 0)` renvoie
`urlProduite: null` et une route de rendu côté Studio (`/rendu/vignette?numero=0`).
Il n'y avait donc rien à récupérer — la spécification, elle, est complète et le
script l'applique :

| Champ de la spec | Valeur | Traduction visuelle |
|---|---|---|
| `titreCourt` | « Ouvrir Plani't » | titre principal, Sora 800 |
| `module.nom` / `couleur` | Authentification / `#4F2DF9` | dégradé de fond + couleur du chip |
| `variante` | **A** — « l'avatar domine » | avatar sur 95 % de la hauteur, à droite |
| `avatar` | `accueil` | pose de face, regard caméra |
| `ecran` | `ecran-splash` | écran splash incliné, tiré de `out/intro.mp4` |

Pour un autre tutoriel, les mêmes champs se passent en arguments :

```bash
python3 build_thumbnail.py --titre-court "Brancher un MCP" \
  --sous-titre "Brancher un serveur MCP" \
  --module "Connexions API & MCP" --couleur "#8236F8" --numero 13
```

Une fois la vignette hébergée, elle se dépose sur la fiche avec
`enregistrer_vignette(numero, url)`.

---

## 4. Point à valider à l'oreille

Le nœud musique a tourné avec `instrumental: False` et `lyrics_type: auto` — le
prompt exigeait « no vocals » et le résultat semble instrumental, mais **je ne peux
pas l'écouter**. À confirmer à l'écoute : s'il y a la moindre voix chantée, il
faut regénérer en forçant le paramètre `instrumental: true` sur le nœud.
