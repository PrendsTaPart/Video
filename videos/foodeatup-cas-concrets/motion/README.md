# FoodEatUp — Cas concrets : cartons HOOK et PUNCHLINE

Compositions HyperFrames réutilisables pour les blocs fixes de la série TikTok « Cas
concrets » (voir `../../FOODEATUP-CAS-CONCRETS-PLAN.md`) : le carton HOOK (0–3 s) qui ouvre
chacune des 10 vidéos, et le carton PUNCHLINE (33–36 s) qui les ferme toutes de la même
façon. Projet HyperFrames autonome (`npx hyperframes init . --example blank`), format
1080×1920, 30 fps.

## Rendus

| Fichier | Rôle | Durée |
|---|---|---|
| `renders/hook-intro.mp4` | Carton HOOK, instancié avec le chiffre de la **vidéo 1** (« 250 couverts aujourd'hui. 10 clients fidèles. ») | 3.0 s |
| `renders/punchline-outro.mp4` | Carton PUNCHLINE fixe, identique sur les 10 vidéos (« FoodEatUp. Ton restaurant, en entier. ») | 3.0 s |
| `thumbnail/cover-hook-v1.png` | Thumbnail/cover TikTok — frame extraite du hook vidéo 1, texte posé | — |
| `thumbnail/cover-punchline.png` | Frame de secours (logo + tagline posés), si un thumbnail neutre est préféré | — |

## Assets de marque utilisés (déjà commités, réutilisés — pas de nouvel asset créé)

- `assets/brand/foodeatup-mark-eight.png` ← `studio-video/assets/brand/logo/foodeatup-mark-eight.png`
- `assets/brand/foodeatup-logo-mascot.png` ← `studio-video/assets/brand/logo/foodeatup-logo-mascot.png`
- `assets/brand/foodeatup-logo-on-blue-card.png` ← `studio-video/assets/brand/logo-v2/foodeatup-logo-on-blue-card.png`
- `assets/brand/michael-chef-mascot.jpg` ← `studio-video/assets/brand/profile/michael-chef-mascot.jpg` (photo
  réelle du chef, pas encore utilisée dans ces deux cartons — voir "Pour continuer")
- `assets/vendor/gsap.min.js`, `assets/vendor/fonts/fredoka-{400,700}.woff2` — vendorés en
  local (Chrome headless ne passe pas par le proxy réseau de cet environnement, voir
  `studio-video/CLAUDE.md`).

Les 4 images fournies par Michael dans le chat (logo mascotte, mark "8", logo carte bleue,
photo chef) sont **déjà présentes dans le dépôt** aux emplacements ci-dessus — comparaison
par hash confirmée le 2026-08-09, rien de nouveau à committer côté sources.

## Réutiliser le HOOK pour les 9 autres vidéos

`index.html` est écrit comme un patron : le chiffre (`#num1`/`#rest1`) et le sous-chiffre
(`#num2`/`#rest2`) sont les deux seuls éléments à changer par vidéo. Pour la vidéo N,
remplacer le texte de ces 4 éléments par le hook correspondant dans
`../../FOODEATUP-CAS-CONCRETS-PLAN.md`, puis :

```bash
cd videos/foodeatup-cas-concrets/motion
npx hyperframes check .
npx hyperframes render . -q high -o renders/hook-intro-v<N>.mp4
```

Le PUNCHLINE (`compositions/punchline-outro.html`) ne change pas — c'est le même rendu sur
les 10 vidéos, à concaténer tel quel en fin de montage.

## Pour continuer

Ce que je n'ai **pas** tranché et qui a un impact sur la suite :

1. **La photo réelle du chef (`michael-chef-mascot.jpg`)** — fournie mais pas encore
   utilisée ici. Le plan `FOODEATUP-CAS-CONCRETS-PLAN.md` prévoit un avatar **HeyGen** pour
   le bloc RÉSULTAT (25–33 s, "il parle") — pas ce chef-là par défaut (voir
   `studio-video/CLAUDE.md` : l'avatar retenu est **Mika**, pas un avatar "Michael"). Cette
   vraie photo peut servir de **Reference Element Higgsfield** pour les 8 plans "problème"
   encore à générer manuellement (remplacerait le personnage IA générique "Karim" utilisé
   dans `hero-video`) — dis-moi si c'est ce que tu veux, je mets à jour le plan en
   conséquence.
2. **Le montage final par vidéo** (hook + Higgsfield + capture écran + HeyGen + punchline)
   n'est pas fait — ces deux cartons ne sont que les segments 1 et 4 du montage en 4 blocs.
   Il manque encore, par vidéo : le plan Higgsfield (8 à générer manuellement, 2
   réutilisables depuis `hero-video/`, voir le plan), la capture écran recadrée en 9:16, et
   le clip HeyGen.
3. **Police de marque** : toujours Fredoka en remplacement de Goodly (fichier réel jamais
   fourni) — si Michael a le vrai fichier `.woff2`/`.ttf` Goodly, le déposer dans
   `assets/vendor/fonts/` et je réajuste le `@font-face`.
4. **Le sous-titre karaoké** n'est pas ajouté sur ces cartons (le plan le prévoit "brûlé sur
   toute la durée, y compris HeyGen" — sur le hook/punchline le texte EST déjà le sous-titre,
   donc rien à dupliquer ; à confirmer que c'est le comportement voulu).
