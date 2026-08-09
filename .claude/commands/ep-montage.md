---
description: Assemble le master 40s + les 8 déclinaisons + thumbnails
---

# /ep-montage

Étape 5 du pipeline.

## Garde-fou (bloquant)

Refuse de s'exécuter si `manifest.json.pipeline.ep-ingest.status != "done"`.

## Étapes

1. Rendre `remotion/OutroEp01.tsx` (Bloc C, 25→40 s) en injectant les variables résolues de
   `manifest.json.pipeline.ep-data.variables` — tout carton `"__SUPPRIMER__"` n'est
   simplement **pas rendu**.
2. Lancer `scripts/build_master.sh` : concat `A_hook.mp4` + `B_corps.mp4` + outro Remotion,
   mix de la VO (`episodes/ep01-la-rentree/voix/`), loudnorm à **-14 LUFS**, sous-titres
   brûlés (lisibles son coupé).
3. Lancer `scripts/build_variants.sh` pour produire les 8 déclinaisons du
   `episodes/ep01-la-rentree/05-DECLINAISONS.md` (teaser 10 s, 3 extraits, 9:16/1:1/16:9,
   etc.).
4. Générer les thumbnails 1080×1350 et 1080×1920 via RapidoCMS `generate_image`
   — titre composé en Remotion, jamais généré par IA.
5. Écrire tous les livrables dans `episodes/ep01-la-rentree/exports/`.
6. Mettre à jour `manifest.json.pipeline.ep-montage.status = "done"`.
