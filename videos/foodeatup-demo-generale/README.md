# FoodEatUp — Démo générale (16:9, ~1:51)

Vidéo de présentation générale de **FoodEatUp**, plateforme tout-en-un de gestion de restaurant.
1920×1080, H.264, voix off FR (ElevenLabs Adam) + musique légère, sous-titres incrustés.

## Livrables
- `output/demo-generale.mp4` — vidéo finale.
- `output/demo-generale-poster.jpg` — poster (frame à 0:05).

## Structure (8 séquences, xfade)
| # | Séquence | Visuel |
|---|----------|--------|
| S0 | **Logo FoodEatUp** (1re image) | carte logo bleue |
| S1 | Hook « et si tout tenait dans une seule plateforme ? » | scène resto + carte question |
| S2 | Stocks temps réel + PrédiBot | `screen-stocks-laptop` + mascotte Stock |
| S3 | Factures OCR — « 6 h gagnées » | `gen-ocr-facture` |
| S4 | Hygiène / HACCP | `hero-stockvision` + mascotte Chef |
| S5 | Salle + cuisine + **Jarvis** (onde vocale animée) | QR + KDS + écran Jarvis |
| S6 | Site de commande en ligne par IA | `gen-site-tablette` + mascotte Copilote |
| S7 | Outro CTA — 14 jours gratuits, foodeatup.fr | carte logo + slogan + URL |

## Reproduire
```bash
./build.sh          # VO + séquences + assemblage (nécessite ELEVENLABS_API_KEY)
```
Ou par étape : `python3 build_seqs.py` puis `python3 build_final.py`.

## Notes
- Charte : bleu `#147AFF`, orange `#FFA500`, typo **Poppins** (substitut arrondi à Baloo 2 — non installée).
- **Voix** : ElevenLabs Adam (`TGAegA0zNRi8I6nUdq3i`), FR, `eleven_multilingual_v2`.
- **Musique** : piste studio FoodEatUp (`stories-foodeatup-30j/audio/bgm.mp3`), −22 dB sous la voix, fade out.
- **Jarvis** : écran `#0F1A23` + 5 barres d'onde vocale animées (ffmpeg `drawbox` sinusoïdal) + dialogue.
- 3 visuels générés via RapidoCMS (`gen-ocr-facture`, `gen-kds-cuisine`, `gen-site-tablette`) — charte bleue,
  style 3D doux. Ils portent des noms d'UI génériques (b-roll) ; la voix FR + les cartes typo portent le message.
