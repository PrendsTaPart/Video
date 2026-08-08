# FoodEatUp — « Le même jour, deux fois »

Film héros du site FoodEatUp. 3 min 45, 16:9, composition HyperFrames (pas Remotion —
le pipeline réel de ce dépôt est HyperFrames/GSAP, voir `studio-video/CLAUDE.md`).

## État de production

| Élément | État |
|---|---|
| Timeline (`data/hero.json`) | ✅ Complète, 8 séquences, ~30 beats, source de vérité unique |
| Composition (`index.html` + `hero-build.js`) | ✅ Construite dynamiquement depuis `hero.json`, validée (`npx hyperframes validate` → 0 erreur) |
| Balayage bleu / repli gris | ✅ Implémenté (`--wipe-progress` piloté par un seul tween GSAP, ligne + désaturation) |
| Personnages (chef, serveur, directeur) | ✅ Générés (Higgsfield, character sheets + Reference Elements pour la cohérence "sans"/"avec") |
| 17 plans vidéo | ✅ Générés (Higgsfield / Seedance 2.0), `assets/video/` |
| 10 images d'ambiance (HERO-01→10) | ✅ Générées (Higgsfield / Nano Banana Pro), `assets/image/ambiance/` |
| 4 voix (chef, serveur, directeur, narratrice) + commis | ✅ Générées (ElevenLabs TTS), `assets/voice/` — chaque personnage a une voix ElevenLabs fixe, cohérente entre ses répliques "sans" et "avec" |
| Cloche du passe ("clin") | ⚠️ **Placeholder IA** (ElevenLabs Sound Effects), PAS un vrai enregistrement. Voir `data/hero.json → clin.statusNote`. |
| Lexique SFX (scanner, imprimante, Jarvis, Iris...) | ⚠️ **Placeholder IA**, `assets/sfx/` — sons plausibles mais génériques, pas les vrais bips/mécaniques FoodEatUp |
| Musique (sans désaccordée / avec résolue) | ⚠️ **Placeholder IA** (ElevenLabs Music), `assets/music/` — à recomposer avec un vrai compositeur pour la sortie finale |
| Rendu final (mp4) | ❌ Pas rendu dans cette session : **ffmpeg indisponible** dans cet environnement. À rendre depuis `studio-video`'s environnement (qui a ffmpeg + Chrome headless opérationnels, voir son `CLAUDE.md`) |
| 14 séquences d'écran extraites des tutoriels | ❌ Non faites — le fichier catalogue avec les URLs S3 exactes (mentionné dans le brief) n'est pas dans ce dépôt. Nécessaire : le déposer dans `rapido-kb/` ou fournir les URLs. |
| Portraits/plans identiques day-of (cohérence lumière) | ⚠️ Générés par IA, donc cohérents par construction — mais ne remplacent pas un vrai tournage si l'objectif final reste un film 100% réel |

## Pourquoi des placeholders IA plutôt que les vrais assets

Cette session ne peut pas filmer de personnes réelles ni enregistrer de vrais sons.
Le brief original demande explicitement du réel (vraie cloche, vraies voix, vrai tournage)
pour que "les mêmes personnes" jouent les deux états — condition posée comme non négociable
en conclusion du brief. Les assets ici générés par IA (Higgsfield pour vidéo/image,
ElevenLabs pour voix/SFX/musique) permettent de **valider la structure, le rythme et le
montage du film dès maintenant**, mais la version diffusée publiquement devrait remplacer :

1. `assets/sfx/son-clin-passe-take{1,2,3}.mp3` → un vrai enregistrement de cloche de passe
2. `assets/sfx/son-*.mp3` (lexique) → les vrais sons d'action (bip scanner réel, etc.)
3. `assets/music/musique-*.mp3` → une composition originale calée sur le clin (tonique ré)
4. `assets/video/hero-*.mp4` → idéalement les vrais tournage avec le chef/serveur/directeur
   réels de l'établissement filmé (le concept du film repose sur "les mêmes personnes" —
   voir §10 du brief original)

Tout le reste (timeline, montage, balayage bleu, structure des beats, sous-titres générés
depuis le texte, QA) est directement réutilisable tel quel : il suffit de remplacer les
fichiers dans `assets/` sans toucher à `hero.json` ni à la composition.

## Lacunes de plans identifiées (voir `note` dans `hero.json`)

- `s1-serveur` : pas de plan "répondeur" dédié généré, réemploi temporaire
- `s3-chef` : image fixe seulement (pas de vidéo "bon tombé")
- `s3-directeur` : pas de plan "descend l'escalier" dédié
- `s4-beatA` / `s4-beatD` : motion design HTML/CSS/GSAP (convergence multi-canal, cascade
  Iris) plutôt que captation — cohérent avec le brief qui les décrit comme des effets
  graphiques, pas des plans filmés
- `s6-chef` : pas de plan "photo IA nettoyage" dédié, réemploi temporaire

## Commandes

```bash
npm run check          # lint + validate (fonctionne dans cet environnement)
node scripts/qa-hero.mjs   # QA mécanique (clin ×3, S4 intouchée, symétrie Jarvis, assets présents...)
npm run render:hero    # nécessite ffmpeg — à lancer depuis un environnement qui l'a
```

## Notes techniques

- Toute la timeline vit dans `data/hero.json` (typé, commenté) ; `index.html` inline ce
  JSON tel quel dans un `<script type="application/json">` et `hero-build.js` construit le
  DOM + le timeline GSAP à partir de là, au chargement. Aucun texte, timecode ou couleur
  n'est dupliqué à la main dans le HTML — modifier `hero.json` suffit.
- Les personnages Higgsfield (Reference Elements) sont documentés dans `hero.json →
  characters` avec leurs IDs pour régénérer d'autres plans cohérents plus tard.
- `assets/vendor/gsap.min.js` est vendoré localement (pas de CDN — Chrome headless de ce
  pipeline ne passe pas par le proxy réseau, voir `studio-video/CLAUDE.md`).
