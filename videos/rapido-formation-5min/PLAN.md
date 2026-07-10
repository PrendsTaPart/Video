# Vidéo formation « L'Écosystème Rapido × Claude Code » — état de production

Format 16:9 1920×1080. Voix Adam ElevenLabs FR (~3:39 de VO → vidéo ~4 min).
11 scènes = S1, S2, S3, S4, S5, S6a, S6b, S6c, S7, S8, S9 (audio 01..11).

## FAIT
- 6 images corporate (public/img1..img6) générées via RapidoCMS (zéro texte, palette Rapido).
- 11 segments VO (assets/voice/01..11.wav) — texte exact du script.
- audio_meta.json (durées + sous-titres even-split) + BGM.
- Logos : RapidoCRM/CMS/RH/Software (public/), FoodEatUp (public/foodeatup-logo.png), mockups CMS/CRM.

## EN ATTENTE (bloque la finalisation)
- **Clips avatar Mika (S1, S5, S8, S9)** : nécessitent la clé API HeyGen + avatar_id Mika + voice_id.
  Compositing : **WebM alpha préféré** (HTML composite l'alpha nativement) ; sinon **MP4 fond vert #00B140**
  que je détoure en local via ffmpeg (colorkey → WebM alpha). MP4 vert accepté.
- À réception : génération des 4 clips (/v2/video/generate), compositing aux positions du storyboard
  (S1/S9 plein écran, S5 coin bas droit 28%, S8 coin bas gauche 25%), puis rendu final.

## À FAIRE (dès déblocage Mika, ou sur accord pour une version placeholder)
- Authoring des 11 scènes HTML (storyboard fourni), sous-titres FR incrustés, animations, SFX.
- Assemble 1920×1080 → render → livraison → archive RapidoCMS → 3 brouillons sociaux (proposés, non publiés).
