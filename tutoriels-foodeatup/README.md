# Tutoriels FoodEatUp — 171 vidéos à produire (audit du 03/11/2026)

Source de la liste : `mouna.md` du dépôt `PrendsTaPart/stockvisionai` (copie ici : `mouna.md`, générée — ne pas éditer).

| Fichier | Contenu |
|---|---|
| `liste.json` | les 171 vidéos : numéro, slug, module, titre de la fiche, titre de la vignette, où tourner, fiche à créer |
| `drive-dossiers.json` | identifiants Google Drive : dossier « 16 - À TOURNER », un dossier par module, un par vidéo, sous-dossiers `01-vignette (Zied)` et `02-rushes (Mouna)` |
| `scripts/NNN-slug.md` | accroche, **plan de tournage** pour Mouna, **voix off d'Adam**, appel à l'action, points à vérifier |

## Chaîne d'une vidéo

1. **Zied** dépose la vignette (PNG 1280×720, titre de la vignette) dans `01-vignette (Zied)`.
2. **Mouna** dépose l'enregistrement d'écran `slug.mp4` dans `02-rushes (Mouna)` en suivant le plan de tournage du script.
3. **Agent vidéo (Claude)** :
   - relit le script contre le rush (le « À vérifier » doit être levé) ;
   - voix off : ElevenLabs, voix **Adam `TGAegA0zNRi8I6nUdq3i`**, modèle **`eleven_v4`**, une seule prise (≈ 0,08 $ par voix de 25 s, estimer avant) ;
   - montage 1080p 40-90 s + sous-titres .srt (outils `academie-pipeline/`) ;
   - dépôt dans la bibliothèque **RapidoCMS** (adresse servie par la bibliothèque, jamais par le dépôt) ;
   - **YouTube** (après accord écrit de Michael, métadonnées relues) ;
   - lien vidéo + YouTube + vignette + transcription (= texte de la voix off) posés sur la fiche de l'**Académie** (MCP admin) ;
   - régénération du catalogue dans le **logiciel** : `python3 scripts/academie/generer_catalogue.py` (stockvisionai), puis `python3 scripts/academie/generer_mouna.py` → la vidéo sort de `mouna.md`.

## Règles

- Aucune génération Higgsfield (voir `CLAUDE.md`).
- Aucun prix, chiffre ou statistique inventé dans la voix off.
- 🎬 dans `mouna.md` = tournage sur le compte de démonstration, pas sur le restaurant école.
- ⛔ `previsions-rh` ne se tourne pas : l'écran n'est pas construit.
- Les 35 fiches marquées « fiche à créer » sont ajoutées à l'Académie par la PR `PrendsTaPart/foodeatup-guide-star-227b4772#3`.
