# FoodEatUp — vidéo prospect « 4 IA » (9:16)

Vidéo de prospection verticale, 1080×1920 / 30 fps, **2 min 15**.
Objectif : obtenir un RDV démo.

## État

| Élément | État |
|---|---|
| Script minuté (`script/script.json`) | ✅ V2 — corrections de texte appliquées, **à valider avant la voix off** |
| Maquettes d'interface (S2→S7) | ✅ Générées (`build_mockups.py`) — données inventées, cf. `NOTES-CAPTURES.md` |
| B-roll (S1, S7) | 🟡 Recadrage vertical des plans 16:9 existants — à remplacer par les plans natifs de `PROMPTS-HIGGSFIELD.md` |
| Sous-titres incrustés | ✅ Style Reels, minutage estimé (2,6 mots/s) |
| Musique | ✅ Piste studio `stories-foodeatup-30j/audio/bgm.mp3`, −10 dB |
| Voix off | ❌ **Non générée** — attend la validation du script (règle étape 3 du workflow tutoriels) |
| Rendu | ✅ `out/foodeatup-prospect-9x16-animatique-v0.mp4` (animatique, sans voix) |

## Fabriquer

```bash
python3 build_mockups.py          # maquettes d'interface -> work/seq-s2..s7.mp4
python3 build_broll.py            # b-roll vertical      -> work/seq-s1.mp4, seq-s7a.mp4
python3 build_final.py            # assemblage + sous-titres + musique -> out/
```

`work/` est ignoré par git (frames intermédiaires) : tout se régénère avec ces trois commandes.

## Montage

| # | Durée | Contenu |
|---|---|---|
| S1 | 14 s | B-roll chaos + pastilles de notification + post-it « TOMATES J-3 » |
| S2 | 13 s | Logo + les 4 IA qui se posent |
| S3 | 20 s | Téléphone / borne / en ligne → écran cuisine |
| S4 | 23 s | Alerte rupture → commande fournisseur → planning |
| S5 | 22 s | Conversation WhatsApp (2 questions, 2 réponses chiffrées) |
| S6 | 26 s | Alerte tomates → recette promo → carte → campagne publiée |
| S7 | 5 + 12 s | Retour en salle + carte CTA |

## À faire ensuite

1. Valider le script (`script/script.json`) → je génère la voix off ElevenLabs et je recale
   le minutage des sous-titres sur les durées réelles.
2. Générer les plans verticaux de `PROMPTS-HIGGSFIELD.md` et les déposer dans `assets/hf/`.
3. Fournir le vrai lien de prise de RDV (la carte finale affiche un placeholder).
