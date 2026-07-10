# Bibliothèque Mika — manifeste des clips HeyGen (réutilisables)

Objectif : **ne jamais régénérer un clip existant** → réduire les frais HeyGen.
Avant toute génération HeyGen, **chercher ici** un clip dont le texte correspond ; sinon générer,
puis **ajouter la ligne au manifeste** et déposer le fichier dans `raw/` (+ `audio/`).

Config HeyGen (constante série) : avatar_id `bd56633302aa4790a8d526fe2ee6b63f` · avatar_style `normal`
· voix = audio ElevenLabs Adam `TGAegA0zNRi8I6nUdq3i` (lip-sync) · fond `#00B140` · dimension `1080×1920`.
Le clip brut a des bandes vertes haut/bas (letterbox 16:9) → au montage, **crop de la bande centrale**
`crop=1080:608:0:656` posée sur fond de marque + sous-titres incrustés (pas de chroma-key : trop agressif).

## Clips disponibles

| Fichier (raw/) | Type | Texte exact | video_id HeyGen | audio_asset_id | Réutilisable |
|---|---|---|---|---|---|
| e01-hook.mp4 | hook E1 | « Et si ta boîte travaillait pour toi à 7h du matin, avant même ton premier café ? » | 10a4ce741cf243cbbbf7399f9b9ea928 | 05527e8fa7d14a6f8e053e77307d9f9d | non (hook propre à E1) |
| e01-cta-A.mp4 | outro CTA-A (E1) | « Demain, je te montre comment brancher cette IA sur les vraies données de ta boîte. Abonne-toi pour ne pas la rater. » | d4b3d03f5ac44800a972ea9f88f039e2 | 5afc1b01c50442de8bde59330fd75549 | non (teaser E2 intégré) |

## À générer une seule fois (réutilisables sur les 30) — voir REUSE-POLICY.md
- `cta-A-generique.mp4` · « Abonne-toi pour ne pas rater le prochain épisode. »
- `cta-B-generique.mp4` · « La routine complète est dans notre plugin — le lien est en bio. »
- `cta-C-generique.mp4` · « Envoie ça à un entrepreneur qui se noie dans ses outils. »
(Le teaser « Demain : … » de chaque épisode est incrusté en **texte à l'écran**, pas dans la voix de Mika.)
