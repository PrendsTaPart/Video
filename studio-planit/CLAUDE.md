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

**Source unique et prioritaire : l'outil MCP `mcp__planit-social__obtenir_charte`.**
À appeler avant tout travail de montage, de vignette ou de visuel — aucune couleur, police
ou règle de logo ne doit être recopiée de mémoire ou reprise d'un autre document (y compris
ce fichier : les valeurs ci-dessous sont un instantané au 2026-08-23, à revérifier via
l'outil si un écart est suspecté). Elle remplace la charte déduite du dossier de stratégie
zip (`00-STRATEGIE-PLANIT.md` proposait Poppins/Inter, fond off-white `#F7F9FC`, encre navy
`#1B2A41` — **abandonné**, valeurs que ce document marquait lui-même « à confirmer »), et
confirme/précise le PDF de marque envoyé par l'utilisateur le 2026-08-22.

- **Couleurs** (`obtenir_charte.couleurs`) :
  - `encre` `#1F0D3E` — fond dominant
  - `primaire` `#4F2DF9` — bleu-violet, aplats
  - `bouton` `#8236F8` — violet, boutons et surlignages
  - `rose` `#FE64D5` — accent unique, **jamais en fond de bloc**
  - `degrade_marque` : 135°, `#4F2DF9` → `#FE64D5`, **réservé au hook d'ouverture et à
    l'animation de fin uniquement** (pas un fond générique). Variables CSS posées dans
    `videos/_gabarit-planit/compositions/frames/01-placeholder.html`
    (`--planit-violet`, `--planit-violet-2`, `--planit-rose`, `--planit-ink`).
  - Ces valeurs sont la charte **marketing/marque** (titres, cartes-agent, habillage,
    signature). Voir plus bas la distinction avec les couleurs **fonctionnelles de l'app**.
- **Typographie** (`obtenir_charte.typographie`) : **Alte Haas Grotesk** en principale,
  **replis officiels : Sora, puis Inter** — chargement en `.woff2` locaux, jamais de CDN.
  Graisses : titres 700/800, texte 400.
  - ⚠️ **Le fichier Alte Haas Grotesk n'a pas pu être téléchargé** dans cet environnement
    (hébergeurs tiers — dafont/1001fonts/fontget — bloqués par la politique réseau de la
    session ; absente de Google Fonts). En attendant, on applique le repli **officiel de la
    charte** : **Sora** pour les titres (`assets/fonts/Sora-{700,800}.woff2`, famille
    `"PlanitTitle"`) et **Inter** pour le texte (`assets/fonts/Inter-400.woff2`, famille
    `"PlanitText"`) — vendorées localement dans `videos/_gabarit-planit/assets/fonts/`
    (Google Fonts, licence libre). Dès que l'utilisateur fournit le vrai fichier Alte Haas
    Grotesk, l'ajouter dans `assets/fonts/` et remplacer les `@font-face` `PlanitTitle`/
    `PlanitText` par la vraie police (recherche ces deux noms dans le projet).
- **Logo** (`obtenir_charte.logo`) : orthographe stricte **« Plani't »** — jamais « PlanIt »,
  « Plan'It », « Planit » ni « PLANIT ». Jamais redessiné, déformé ou recoloré. Trois
  variantes cataloguées (`blanc_sur_encre`, `encre_sur_rose`, `pictogramme_seul`), URLs
  hébergées sur `planit-social-ai.lovable.app` — **inaccessibles depuis cette session**
  (domaine hors de la politique réseau autorisée). **Statut au 2026-08-23 : en attente des
  fichiers, l'utilisateur les fournit via Google Drive** (a explicitement refusé de
  réutiliser les PNG `black_logo.png`/`white_logo.png` trouvés dans
  `videos/planit-academy/assets/`, même si visuellement conformes). Tant qu'ils ne sont pas
  déposés dans `assets/brand/`, n'utiliser que le **wordmark texte** « Plani't » en
  `PlanitTitle` (voir le gabarit) — jamais de glyphe redessiné à la main.
- **Format vidéo et zone de sécurité** (`obtenir_charte.format_video`) : 1080×1920, 30fps.
  **Aucun élément de marque au-dessus de y=120 ni en dessous de y=1600** — les 320px du bas
  sont réservés à l'UI des réseaux sociaux (like/commentaire/légende). Le bandeau de
  sous-titres du gabarit (`compositions/captions.html`) respecte cette zone
  (`--cap-band-top: 1380px`, `--cap-band-height: 200px`, finit à y=1580).
- **Signature** : « Ce n'est pas demain. C'est aujourd'hui. » — **Baseline** : « Vos
  logiciels ont enfin une équipe. »

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
`.ttf` dans `videos/_shared/fonts/`. Sora est aussi, par coïncidence, le repli titres de la
charte marque (voir ci-dessus) — mais le corps de texte diffère : **Inter** pour l'habillage
marque, **Manrope** uniquement si on reproduit un écran de l'app à la main (à éviter, voir
règle Shot 3 plus bas — toujours préférer une vraie capture d'écran).

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
`GROUPS` vide à régénérer depuis `caption_groups.json`), `assets/fonts/` (Sora/Inter, voir
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
