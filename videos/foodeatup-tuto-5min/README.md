# Tutoriel FoodEatUp en 5 minutes — vidéo Académie

Vidéo verticale (1080×1920, ~4–5 min) qui présente **l'intégralité des tutoriels
FoodEatUp** : 18 étapes réparties en 7 phases, « de la création de votre boutique
à la maîtrise de l'IA ». Le présentateur (avatar) apparaît à **chaque changement
de phase**, et les fonctionnalités sont montrées via les **captures d'écran produit**.

## Livrable
- `deliverable/foodeatup-tuto-5min.mp4`

## Contenu (7 phases · 18 étapes)
1. **Compte & boutique** — créer son compte, créer l'établissement
2. **Fondations** — TVA, catégories
3. **Connecter l'IA** — MCP StockVisionAI (Claude/Mistral/ChatGPT/WhatsApp)
4. **Remplir avec l'IA** — carte→produits, ingrédients, recettes, Ma carte, fournisseurs
5. **Équipe (RH)** — employés/rôles/QR, plannings/pointages/congés
6. **HACCP** — équipements/températures, DLC/traçabilité, nettoyage/checklists
7. **Exploitation** — stocks/production, clients/devis/factures, PrediBot & bilan

## Assets
- `assets/gen/` — **8 illustrations 3D générées via RapidoCMS** (intro, 7 phases, CTA)
- `assets/screens/` — 20 captures d'écran produit FoodEatUp mappées aux étapes
- `assets/avatar/` — clip présentateur (Mika/HeyGen) + masque médaillon
- `assets/logo/`, `assets/fonts/` — logo FoodEatUp + Poppins
- `audio/` — voix off ElevenLabs (Adam FR) `s00…s99.mp3` + `bgm.mp3`

## Fichiers
- `SCRIPT.md` — script + voix off (27 segments)
- `STORYBOARD.md` — storyboard plan par plan
- `build_fe.py` — compositeur PIL (intro, 18 cartes étapes, 7 bases de phase, outro)
- `gen_vo.py` — génération voix off
- `assemble_fe.py` — montage ffmpeg (clips + avatar en médaillon sur les phases + BGM + loudnorm)

## Reproduire
```bash
python3 gen_vo.py       # voix off -> audio/
python3 build_fe.py     # frames -> frames/
python3 assemble_fe.py  # -> deliverable/foodeatup-tuto-5min.mp4
```

## Specs
- Charte FoodEatUp : bleu `#1E86FF`, orange `#F7941E`, fond clair, police ronde
- Avatar en médaillon (440×560, coins arrondis) sur les 7 bumpers de phase
- Voix off : ElevenLabs Adam `TGAegA0zNRi8I6nUdq3i`, `eleven_multilingual_v2`, FR
- Audio : VO + BGM en boucle (−24 dB), `loudnorm I=-14`
