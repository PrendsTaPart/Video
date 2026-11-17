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

## État

| # | Épisode | Voix | Vidéo | Bibliothèque RapidoCMS | Planifié 18 h | Journal (brouillon) |
|---|---|---|---|---|---|---|
| 1 | ep01-haccp-tofu | ✅ | ✅ 21 s | ✅ `10-applis-ep01-haccp-tofu` | 17/11 · LI brouillon 2204 · TT 2205 | ✅ ép. 105 |
| 2 | ep02-haccp-mofu | ✅ | ✅ 21 s | ✅ | 18/11 · LI 2206 · TT 2207 | ✅ ép. 106 |
| 3 | ep03-haccp-bofu | ❌ crédits ElevenLabs | — | — | 19/11 à faire | — |
| 4 | ep04-caisse-tofu | ✅ | ✅ 18 s | ✅ | 20/11 · LI 2208 · TT 2209 | ✅ ép. 108 |
| 5 | ep05-caisse-mofu | ✅ | ✅ 17 s | ✅ | 21/11 · LI 2210 · TT 2211 | ✅ ép. 109 |
| 6–30 | voir `POSTS.md` | ❌ crédits ElevenLabs | — | — | — | — (numéros 110 à 134 réservés) |

## Bloqueurs

1. **ElevenLabs** : quota mensuel atteint après 4 voix (« exceeds your quota »). Recharger ou attendre la remise à zéro, puis générer les 26 voix restantes (textes = `phrases` de `episodes.json`), et relancer `construire.py` + `rendre.sh`. Le Journal ne peut pas prendre le relais tant qu'ElevenLabs n'y est pas connecté (Communauté → Connexions).
2. **TikTok Michael** : le compte est marqué **expiré** dans RapidoCMS. Les posts TikTok sont planifiés mais ne partiront pas tant que le compte n'est pas reconnecté.
3. **Lovable** : crédits épuisés après la création de la page ; la page est publiée, mais les retouches demanderont des crédits. Points à valider : texte de consentement du formulaire et lien des mentions légales (foodeatup.com/mentions-legales supposé).
