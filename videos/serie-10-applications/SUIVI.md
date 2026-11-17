# Série « Les 10 applis FoodEatUp » : suivi (17/11/2026)

30 épisodes verticaux 1080 × 1920 (≈ 17–22 s), 3 par application : **TOFU** (le problème), **MOFU** (comment ça marche, vrais écrans), **BOFU** (passer à l'action). Un épisode par jour à 18 h, du 17/11 au 16/12/2026, sur **TikTok Michael** et **LinkedIn Michael**. Calendrier et textes : `POSTS.md`.

Page de vente (Lovable, publiée) : https://foodeatup-10-applications.lovable.app (projet `84bf4ecc-60b6-47fc-9fef-760f53e21bca`, images d'ambiance générées par Lovable + vrais écrans, formulaire « Être rappelé » dans la table `callback_requests`).

## Fabrication

- `episodes.py` → `episodes.json` : les 30 scripts, une phrase = une scène (`B:` mots qui claquent, `P:`/`D:` vrais écrans, `C:` mot-clé à commenter).
- Voix : ElevenLabs Noé `7pDdnNI6PhXmAp0pXFZm`, `eleven_v4`, flow `3XmTJZUQg6LPpYxNrFzE` → `episodes/<slug>/vo.mp3`.
- `python3 moteur/construire.py <slug>…` : transcription faster-whisper, calage des scènes, `cfg.js`, `index.html` (copie de `moteur/modele.html`).
- `bash moteur/rendre.sh <slug>…` : images (`../_moteur/render.js`), mixage voix + musique à 20 % (`../_moteur/fin.py`), SRT, miniature.
- `python3 posts.py` : légendes TikTok / LinkedIn et calendrier.
- Écrans : `ecrans/<app>/` (Store FoodEatUp, journal-assets, captures Cocuisinage, jeux FoodEatUp Game). **Production** : maquettes du site, signalées « Aperçu · application en préparation » dans la vidéo.

## État (17/11/2026, fin de journée)

Les 30 épisodes sont montés, déposés dans la bibliothèque RapidoCMS, planifiés à 18 h (LinkedIn + TikTok Michael) et **publiés** dans le Journal (série « Mes projets », épisodes 105 à 134).

| # | Date | Brouillon LI | Brouillon TT | Journal |
|---|---|---|---|---|
| 1 | 2026-11-17 | 2204 | 2205 | 105 · publie |
| 2 | 2026-11-18 | 2206 | 2207 | 106 · publie |
| 3 | 2026-11-19 | 2212 | 2213 | 107 · publie |
| 4 | 2026-11-20 | 2208 | 2209 | 108 · publie |
| 5 | 2026-11-21 | 2210 | 2211 | 109 · publie |
| 6 | 2026-11-22 | 2214 | 2215 | 110 · publie |
| 7 | 2026-11-23 | 2216 | 2217 | 111 · publie |
| 8 | 2026-11-24 | 2218 | 2219 | 112 · publie |
| 9 | 2026-11-25 | 2220 | 2221 | 113 · publie |
| 10 | 2026-11-26 | 2222 | 2223 | 114 · publie |
| 11 | 2026-11-27 | 2224 | 2225 | 115 · publie |
| 12 | 2026-11-28 | 2226 | 2227 | 116 · publie |
| 13 | 2026-11-29 | 2228 | 2229 | 117 · publie |
| 14 | 2026-11-30 | 2230 | 2231 | 118 · publie |
| 15 | 2026-12-01 | 2232 | 2233 | 119 · publie |
| 16 | 2026-12-02 | 2234 | 2235 | 120 · publie |
| 17 | 2026-12-03 | 2236 | 2237 | 121 · publie |
| 18 | 2026-12-04 | 2238 | 2239 | 122 · publie |
| 19 | 2026-12-05 | 2240 | 2241 | 123 · publie |
| 20 | 2026-12-06 | 2242 | 2243 | 124 · publie |
| 21 | 2026-12-07 | 2244 | 2245 | 125 · publie |
| 22 | 2026-12-08 | 2246 | 2247 | 126 · publie |
| 23 | 2026-12-09 | 2248 | 2249 | 127 · publie |
| 24 | 2026-12-10 | 2250 | 2251 | 128 · publie |
| 25 | 2026-12-11 | 2252 | 2253 | 129 · publie |
| 26 | 2026-12-12 | 2254 | 2255 | 130 · publie |
| 27 | 2026-12-13 | 2256 | 2257 | 131 · publie |
| 28 | 2026-12-14 | 2258 | 2259 | 132 · publie |
| 29 | 2026-12-15 | 2260 | 2261 | 133 · publie |
| 30 | 2026-12-16 | 2262 | 2263 | 134 · publie |

## Restant

1. **TikTok Michael** est marqué expiré dans RapidoCMS : les posts TikTok ne partiront qu'après reconnexion.
2. **Page Lovable** : l'ajout des 30 vidéos est refusé faute de crédits Lovable ; la demande est prête dans `LOVABLE-VIDEOS.md`.

## YouTube

Les 30 Shorts sont planifiés sur la chaîne FoodEatUp (`UC0Mc8pkW4t3uVjbI-ULptUA`) via Rapido YouTube, à 18 h du 17/11 au 16/12, en mode « envoi à l’heure prévue » (une vidéo par jour, dans le quota). Identifiants : `youtube-planif.json`, métadonnées : `youtube.json`.
