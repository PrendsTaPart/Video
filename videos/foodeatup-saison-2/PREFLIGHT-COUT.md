# Préflight coût — aucune dépense engagée ici

Décision à prendre **avant** production. Tarif Higgsfield publié en août 2026 pour Seedance 2.5 :
10 s en 480p = 30 crédits · 720p = 65 crédits (≈ 3,25 $) · 1080p = 90 crédits (≈ 4,50 $).

| Étape | Volume | Crédits |
|---|---|---|
| Validation des 60 prompts en 480p | 60 × 30 | 1 800 |
| Rendu final en 720p (1 prise) | 60 × 65 | 3 900 |
| Marge de sécurité (1 re-roll ou region edit sur 1 clip sur 2) | 30 × 65 | 1 950 |
| **Total réaliste saison complète (720p)** | | **≈ 7 650 crédits (≈ 380 $)** |
| Variante 1080p pour le rendu final | 60 × 90 | 5 400 au lieu de 3 900 |

Montage Remotion : **0 crédit**. Voix off ElevenLabs : négligeable.
Si le plan inclut « Unlimited Seedance 2.5 », le coût marginal est nul — **vérifier le solde avant
de lancer** (préflight gouvernance-credits).

## Règle du dépôt

Ce dépôt ne génère **aucune vidéo Higgsfield** (voir `CLAUDE.md` à la racine). Les prompts de
`prompts/` sont faits pour être collés dans l'interface Higgsfield par un humain, ou pour réutiliser
un plan déjà présent dans la bibliothèque du projet. Aucune commande de ce dossier n'appelle l'API.
