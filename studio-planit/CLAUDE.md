# Studio Plani't — Mémoire du studio (LIRE EN PREMIER)

C'est le studio HyperFrames pour monter les épisodes vidéo Plani't (séries A/B/C/D du
catalogue « 186 épisodes »), sur le modèle de `studio-video/` (FoodEatUp) mais avec sa
propre charte, ses propres assets et son propre gabarit.

**Règle héritée de `CLAUDE.md` (racine du dépôt) : aucun agent ne génère jamais de plan
vidéo via Higgsfield.** On réutilise la bibliothèque existante, ou on donne le prompt à
l'utilisateur pour qu'il le génère lui-même dans l'interface Higgsfield.

## Format vidéo

- **1080×1920** (vertical, 9:16), **30 images/seconde**. Rendu avec `npx hyperframes render`.
- Vignettes (Série C notamment) exportées en **2160×3840**.

## Identité de marque — Plani't

### Charte graphique **officielle**, confirmée le 2026-08-22

Fournie directement par l'utilisateur (captures du PDF de marque). **C'est la source
prioritaire** — elle remplace toute couleur/typo déduite précédemment dans les documents
de stratégie du dossier zip fourni le même jour (`00-STRATEGIE-PLANIT.md` proposait
Poppins/Inter, fond off-white `#F7F9FC`, encre navy `#1B2A41` — **abandonné**, ces valeurs
étaient explicitement marquées « à confirmer avec le fichier de marque officiel » dans ce
document, et le fichier reçu les contredit).

- **Couleurs de marque** :
  - **Rose** `#FE64D5`
  - **Violet primaire** `#4F2DF9`
  - **Violet secondaire** `#8236F8`
  - **Encre / fond sombre** `#1F0D3E`
  - Traitement signature : **dégradé diagonal violet → rose** (`#4F2DF9` → `#FE64D5`,
    135°), utilisé en fond de titre/signature. Variables CSS posées dans
    `videos/_gabarit-planit/compositions/frames/01-placeholder.html`
    (`--planit-violet`, `--planit-violet-2`, `--planit-rose`, `--planit-ink`).
  - Ces valeurs sont la charte **marketing/marque** (titres, cartes-agent, habillage,
    signature). Voir plus bas la distinction avec les couleurs **fonctionnelles de l'app**.
- **Typographie de marque** : **Alte Haas Grotesk** (grotesque proche Helvetica, une seule
  famille pour titres et texte, vue en régulier + gras dans le PDF).
  - ⚠️ **Le fichier réel n'a pas pu être téléchargé** dans cet environnement (hébergeurs de
    police tiers — dafont/1001fonts/fontget — bloqués par la politique réseau de la
    session ; Alte Haas Grotesk n'est pas distribuée sur Google Fonts). **Archivo** (Google
    Fonts, grotesque de proportions proches, licence libre) sert de **remplaçant temporaire**,
    vendoré localement dans `assets/fonts/Archivo-{400,600,700,800}.woff2`, déclaré sous le
    nom `"PlanitDisplay"` dans un `@font-face` (donc aucun autre changement nécessaire
    ailleurs dans les compositions le jour où le vrai fichier arrive).
  - Dès que l'utilisateur fournit le vrai fichier Alte Haas Grotesk (`.woff2`/`.ttf`, deux
    graisses mini : régulier + gras), le déposer dans `assets/fonts/` et mettre à jour les
    `@font-face` de chaque composition (recherche `PlanitDisplay` dans le projet).
- **Logo** : marque-page en forme d'étoile/flamme (le glyphe "spark") + wordmark « Plani't »
  (apostrophe typographique). **Les fichiers réels du logo n'ont pas été fournis** — seules
  des captures d'écran existent. Ne jamais redessiner le glyphe à la main : tant que le
  fichier n'est pas fourni, n'utiliser que le **wordmark texte** « Plani't » en `PlanitDisplay`
  (voir le gabarit). Demander les fichiers PNG/SVG du logo avant tout habillage qui a besoin
  du glyphe (sting de signature, carte-agent, vignette).

### Couleurs **fonctionnelles de l'app réelle** (distinctes de la charte marque ci-dessus)

Auditées depuis le code source de l'app (`videos/planit-academy/CONNAISSANCE-PLANIT.md`,
`lib/core/theme/app_colors.dart`) — à utiliser **uniquement** quand on recrée un élément
d'interface réel (jamais pour l'habillage/motion design, qui suit la charte marque
ci-dessus) :

| Rôle | Hex |
|---|---|
| `backgroundPage` (fond des pages claires de l'app) | `#EDEAFE` |
| `textDark` (texte dans l'app) | `#0B0516` |
| `success` (validations dans l'app) | `#75AB00` |

Polices réelles de l'app : **Sora** (titres) + **Manrope** (corps) — déjà vendorées en
`.ttf` dans `videos/_shared/fonts/`. Distinctes de la police de marque `PlanitDisplay`
ci-dessus : Sora/Manrope ne servent que si on reproduit un écran de l'app à la main (à
éviter, voir règle Shot 3 plus bas — toujours préférer une vraie capture d'écran).

## Structure narrative — règle d'or du motion design

- Le visuel **AJOUTE** de l'info, il ne redit **jamais** ce que la voix dit déjà.
- **Un seul accent violet par plan Higgsfield**, comme objet physique dans le décor
  (chaise, tasse, câble, carnet), jamais comme étalonnage/filtre de toute l'image — sinon
  Seedance sur-violette le plan et casse le photoréalisme.
- Shot 3 des épisodes Série A (« le geste dans l'app ») ne montre **jamais** un écran
  généré ou recréé à la main : toujours une vraie capture d'écran incrustée au montage.

## Sous-titres

- Une seule ligne à la fois (jamais deux).
- Blocs de **2 à 6 mots**, coupés là où la phrase respire naturellement.
- Jamais de point final. Jamais de coupure qui laisse un groupe de sens en plan.
- Style : chip violet plein sur le mot en cours de lecture (karaoké), encre `#1F0D3E`
  pour le texte déjà lu, fond blanc/carte translucide — voir
  `videos/_gabarit-planit/compositions/captions.html` (skin déjà posé, tokens
  `--cap-accent`/`--cap-ink`/`--cap-canvas`).

## Catalogue, casting, nommage

Voir **`references/planit-brand.md`** : les 7 agents, les 5 personas humains (fiches
personnage Higgsfield), les 4 séries et leurs codes, la convention de nommage des dossiers
`planit-{serie}-s{saison}e{episode}-{slug}`. Voir **`references/planit-characters.md`**
pour l'inventaire des fiches personnage déjà générées (Reference Elements Higgsfield).

## Gabarit d'épisode

`videos/_gabarit-planit/` — projet HyperFrames vide mais valide (`npm run check` passe :
0 erreur, 0 avertissement, 0 problème de layout). Dupliquer ce dossier pour chaque nouvel
épisode, jamais le modifier pour un épisode réel. Contient : `index.html`, `meta.json`,
`package.json`, `hyperframes.json`, `compositions/frames/01-placeholder.html` (à remplacer
par les vraies frames de l'épisode), `compositions/captions.html` (skin de sous-titres prêt,
`GROUPS` vide à régénérer depuis `caption_groups.json`), `assets/fonts/` (Archivo, voir
ci-dessus), `assets/sfx/` (8 sons réutilisés depuis `videos/planit-product-launch/`),
`assets/vendor/gsap.min.js`, `assets/bgm/` (vide — pas de musique Plani't propre encore
identifiée, ne pas réutiliser une BGM d'une autre marque du groupe sans vérifier la licence
et la cohérence de ton).

## Prototypes existants Plani't dans ce dépôt (antérieurs à ce studio, styles différents)

- `videos/planit-product-launch/` — HyperFrames, 1920×1080 (paysage), palette sombre
  violet/Inter/Space Grotesk : un prototype d'avant cette charte, à ne pas copier tel quel.
- `videos/planit-academy/` et `videos/planit-tuto-*/` — pipeline **Python** (pas
  HyperFrames), habillage Académie avec avatar présentatrice. Studio séparé, pas concerné
  par ce studio HyperFrames sauf pour les fonds documentaires (`CONNAISSANCE-PLANIT.md`).

---

# HyperFrames Composition Project

## Skills — USE THESE FIRST

**Always invoke the relevant skill before writing or modifying compositions.** Skills
encode framework-specific patterns (`window.__timelines` registration, `data-*` attribute
semantics, shader-compatible CSS rules) that are NOT in generic web docs.

**Doing anything with HyperFrames?** Start at `/hyperframes` — it routes to the right
workflow (`/product-launch-video`, `/faceless-explainer`, `/embedded-captions`,
`/talking-head-recut`, `/motion-graphics`, `/general-video`, etc.) or the domain skills
(`/hyperframes-core`, `/hyperframes-animation`, `/hyperframes-creative`, `/hyperframes-cli`,
`/media-use`, `/hyperframes-registry`).

## Commands

```bash
npm run dev      # preview server — ALWAYS run_in_background: true (blocks otherwise)
npm run check    # lint + validate + inspect
npm run render   # render to MP4
npm run publish  # shareable link
```

## Key rules (points de vigilance connus, hérités de `studio-video/`)

1. Every timed element needs `data-start`, `data-duration`, `data-track-index`, and
   **`class="clip"`** — the framework uses the class for visibility control.
2. Timelines must be paused and registered on `window.__timelines["<composition-id>"]`.
3. Videos use `muted` + a separate `<audio>` element for the audio track.
4. Only deterministic logic — no `Date.now()`, no `Math.random()`, no network fetches.
5. GSAP and all fonts are **vendored locally** (`assets/vendor/`, `assets/fonts/`) — the
   Chrome headless used by `render`/`validate` does not go through the session's network
   proxy, so any CDN `<script src>` or `@import` times out.
6. `npm run dev` is long-running — never run it in the foreground.
