# Académie RapidoCMS — studio de production

Espace de travail des tutoriels vidéo RapidoCMS (16 modules, 112 tutoriels),
jumeaux des tutoriels de l'univers Académie du dépôt, avec le **bleu #03A9F5**
à la place du vert.

Un dossier par tutoriel, créé au démarrage de sa production :

```
videos/academie-rapidocms/<slug-du-tutoriel>/
├── script/        # SCRIPT.md validé + plan de captures
├── audio/         # 01-hook.wav, 02-contexte.wav… + timings de visèmes
├── captures/      # Playwright 1920×1080 sur cms.rapidosoftware.com (compte démo)
├── avatar/        # rendus three.js (pastilles 16:9 + version 9:16)
├── composition/   # montage intermédiaire
└── exports/       # master 16:9 1080p + Short 9:16 1080×1920 + vignette
```

Références :

- Avatar et lipsync : `assets/avatar/` (GLB + stack copiée de academie-rapido-spark).
- Poses présentateur : `assets/avatar/poses/`.
- Pipeline de montage de référence : `videos/planit-academy/academie.py` + `habillage/`.
- Charte : bleu primaire `#03A9F5`, gris texte `#383838`, fond `#F2F4F7`,
  vert `#4CAF50` réservé aux confirmations, Arial.
- Logo : `assets/rapidocms/logo-rapidocms.png` (et l'URL S3 de la charte).
- Mockup hero : `assets/rapidocms/mockup-laptop-calendrier-stats.jpg`.

Trois points de validation humaine par vidéo : script, montage final,
publication (site + YouTube + planification sociale). Journal de session dans
`logs/AAAA-MM-JJ.md`.
