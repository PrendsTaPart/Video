# FoodEatUp — vidéo prospect « 4 IA » (9:16)

Vidéo de prospection verticale, 1080×1920 / 30 fps, **1 min 59**. Cible : franchises
(snack, boulangerie, vente à emporter).
Objectif : obtenir un RDV démo.

## État

| Élément | État |
|---|---|
| Script minuté (`script/script.json`) | ✅ V2 — corrections de texte appliquées, **à valider avant la voix off** |
| Maquettes d'interface (S2→S7) | ✅ Générées (`build_mockups.py`) — données inventées, cf. `NOTES-CAPTURES.md` |
| B-roll (S1, S7) | ✅ Photos verticales snack / boulangerie / borne générées via RapidoCMS (`assets/rapidocms/`), animées en Ken Burns |
| Sous-titres incrustés | ✅ Style Reels, calés sur les durées réelles de la voix · export `.vtt` |
| Musique | ✅ Piste studio `stories-foodeatup-30j/audio/bgm.mp3`, −10 dB |
| Voix off | ✅ 16 lignes — **Rémy** (`APbYQosMxYlAnCCBzydW`, FR natif chaleureux), 75,1 s, loudnorm par ligne (`vo/`) · comparatif de 5 voix dans `vo/essais/` |
| Rendu | ✅ `out/foodeatup-prospect-9x16.mp4` — 1:58, crête −4,4 dB, RMS −18,5 dB, stéréo |

## Fabriquer

```bash
python3 build_mockups.py          # maquettes d'interface -> work/seq-s2..s7.mp4
python3 build_broll.py            # b-roll vertical      -> work/seq-s1.mp4, seq-s7a.mp4
export ELEVENLABS_API_KEY=...     # ou: set -a; . ../../studio-video/.env; set +a
python3 build_vo.py               # voix off ligne par ligne -> vo/L*.mp3 + vo/vo_meta.json
python3 build_final.py            # assemblage + sous-titres + musique -> out/
```

`build_final.py` détecte `vo/vo_meta.json` : présent, il monte la version complète et cale
les sous-titres sur la durée réelle de chaque ligne ; absent, il sort l'animatique muette.

`work/` est ignoré par git (frames intermédiaires) : tout se régénère avec ces trois commandes.

## Montage

| # | Durée | Contenu |
|---|---|---|
| S0 | 2,6 s | Sting logo d'ouverture |
| S1 | 16 s | Snack en rush, tacos, boulangerie, borne + pastilles de notification + post-it « TOMATES J-3 » |
| S2 | 13 s | Logo + les 4 IA qui se posent |
| S3 | 15 s | Téléphone / borne / en ligne → écran cuisine |
| S4 | 19 s | Alerte rupture → commande fournisseur → planning |
| S5 | 15 s | Conversation WhatsApp (2 questions, 2 réponses chiffrées) |
| S6 | 22 s | Alerte tomates → recette promo → carte → campagne publiée |
| S7 | 5 + 11 s | Retour en salle + carte CTA |

Durées calées sur la voix off réelle : chaque scène tient la voix plus la respiration,
sans temps mort une fois l'animation arrivée au bout de sa chorégraphie.

## À faire ensuite

1. ~~Valider le script~~ ✅ · ~~voix off~~ ✅ générée avec Lucas.
2. Générer les plans verticaux de `PROMPTS-HIGGSFIELD.md` et les déposer dans `assets/hf/`.
3. Fournir le vrai lien de prise de RDV (la carte finale affiche un placeholder).
4. Retours de Moody suivis dans `RETOURS.md`.
