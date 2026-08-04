# Générateur d'avatars parlants HeyGen (API REST v3)

Débloque la génération d'avatars RÉELS côté CLI. Les outils MCP `compose`/`render_video`
sont désactivés pour ce type de client, mais l'API REST v3 (`api.heygen.com/v3`, header
`x-api-key`) fonctionne directement.

## Clé
`HEYGEN_API_KEY=` dans `studio-video/.env` (gitignoré).

## ⚠️ Crédits
La génération vidéo consomme les crédits **API** (`details.api`), PAS les crédits **plan**
(app web). Vérifier : `python3 heygen_avatar.py check`.
- **Avatar III / 720p** = économe (défaut du script).
- **Avatar IV / 1080p** = premium, plusieurs crédits API par clip.

## Commandes
```
python3 heygen_avatar.py check                                  # crédits + voix FR
python3 heygen_avatar.py upload <fichier>                       # -> asset_id
python3 heygen_avatar.py video <avatar_id> <voice_id> "<texte>" out.mp4 16:9
python3 heygen_avatar.py lipsync <video_url|asset_id> <audio.mp3> out.mp4   # relip sur NOTRE voix ElevenLabs
```

## Assets utiles (compte actuel)
- Avatar « Michael » costume navy + téléphone : `364644aadd6247e2aa64388bd7ceaa4f`
- Avatars restaurant/chef : `40ae2c8f92d845048e39984d92bd3f88` (gentleman restaurant),
  `02655c23494c4cf08a2f8b8224747885` (chef cuisine), `a964e5add80d40a6bcf5ac834a33290e`
- Voix FR homme : `68c7001d8ff34d168d287e1bd7653041` (Etienne Lefebvre), `e11f0b51e57541f4abebd5f5d76defb8` (Mathieu)

## Intégration vidéo
Ces clips remplacent les avatars statiques (intro Michael + 6 bumpers + hook de fin).
Pour garder NOTRE voix ElevenLabs : générer une base `video` puis `lipsync` sur le mp3 ElevenLabs.
