# Vidéo formation « L'Écosystème Rapido × Claude Code » — LIVRÉE

Format 16:9 1920×1080, 30 fps. Durée **3:45** (225 s). Voix Mika (HeyGen, avatar présentateur
bureau) pour l'intro/transition/module Startup/conclusion ; voix off Adam ElevenLabs FR
pour les 7 scènes narrateur. Sous-titres FR incrustés partout (karaoké de marque sur les scènes
graphiques, SRT propre sur les clips Mika). Musique corporate continue @ ~0.075, mix normalisé -16 LUFS.

## Livrable
- `deliverable/rapido-formation-ecosysteme-5min.mp4` (≈31 Mo, H.264, AAC 48 kHz).

## Structure (montage)
1. **S1** Mika — intro « et si vos outils se parlaient » (HeyGen, 14 s)
2. **S2** Le vrai problème — six outils cloisonnés (HyperFrames, 26 s)
3. **S3** L'écosystème Rapido — hub MCP + 4 logiciels (HyperFrames, 35 s)
4. **S4** Le plugin Claude Code — Skills 60+ / Agents / Garde-fous (HyperFrames, 33 s)
5. **S5** Mika — « assez de théorie, un lundi matin en vrai » (HeyGen, 4 s)
6. **S6a** Cas nº1 — briefing du dirigeant « Prépare ma journée » (HyperFrames, 14 s)
7. **S6b** Cas nº2 — pipeline de contenu « Crée les posts de la semaine » (HyperFrames, 15 s)
8. **S6c** Cas nº3 — restaurant « Fais le point du matin » + commande à valider (HyperFrames, 15 s)
9. **S7** Le Loop Engine — 4 routines à heure fixe + outils externes (HyperFrames, 32 s)
10. **S8** Mika — module Startup (coach IA + DAF virtuel → RapidoRH) (HeyGen, 17 s)
11. **S9** Mika — conclusion « installez le plugin, dites : prépare ma journée » (HeyGen, 13 s)
12. **Endcard** — logo RapidoSoftware + 4 logos + CTA (HyperFrames, 6,5 s)

## Pipeline de reproduction
- 6 images corporate : `public/img1..img6` (RapidoCMS generate_image, zéro texte).
- 11 VO : `assets/voice/01..11.wav` (01/05/10/11 = pistes Mika ; 02-04/06-09 = narrateur).
- `audio_meta.json` (durées + mots even-split) ; `audio_meta_nobgm.json` = variante sans BGM
  pour rendre les corps sans musique (musique ajoutée au montage final).
- Frames : `compositions/frames/02..07*.html` + `99-endcard.html`.
- Corps A (S2-S4) : `STORYBOARD-A.md` → captions.mjs → assemble-index.mjs → transitions.mjs →
  vendor gsap local → `npm run check` → `npm run render`.
- Corps B (S6a-S7) : idem avec `STORYBOARD-B.md`. Endcard : `STORYBOARD-C.md` (muet, sans captions/BGM).
- Clips Mika : SRT générés depuis les mots audio_meta (frames 1/5/10/11), incrustés via ffmpeg,
  normalisés 1920×1080/30 fps.
- Montage final : concat `mika-s1 + corpsA + mika-s5 + corpsB + mika-s8 + mika-s9 + endcard`,
  BGM continue (loop, fade in/out), loudnorm -16 LUFS.
- NB : `index.html` est régénéré par corps (A/B/C) ; ce n'est pas un montage unique.

## Notes QA
- 0 erreur lint/validate. WCAG AA : tous les textes de scène passent ; les alertes restantes
  ne concernent que des mots de sous-titres « déjà prononcés » (faux positifs du skin karaoké).
- `content_overlap` transitoire = sous-titres superposés à une scène en crossfade (intentionnel).
