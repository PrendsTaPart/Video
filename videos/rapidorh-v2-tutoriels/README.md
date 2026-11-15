# Tutoriels RapidoRH V2 (RHV2-07 à RHV2-10)

Quatre tutoriels 1280×720 filmés sur le **produit réel** RapidoRH (branche `ccr-1f094534-m4xekn` de `PrendsTaPart/rapido-RH`, serveur local, entreprise de démonstration fictive « Studio Démo »). Aucune image générée par IA, aucun plan Higgsfield.

- Voix : ElevenLabs « Adam - Instructor » (`TGAegA0zNRi8I6nUdq3i`), modèle `eleven_v4`, une seule prise par épisode ; textes exacts dans `voix/*.txt`.
- `sources/episodes.js` : script (une phrase par segment) et gestes à l'écran ; `record.js` filme avec Playwright en se calant sur les silences de la voix ; `build.py` construit cartes, sous-titres et montage (H.264/AAC, faststart) et écrit le manifeste ; `qa.py` sort une planche de 8 images ; `reset.sh` recrée la démo ; `seed_v2_ui.cjs` crée poste, candidature et réunion par l'API du produit.
- Les scripts sont en CommonJS : les exécuter depuis une copie hors du dépôt RapidoRH (son `package.json` est en `"type": "module"`).

| Fichier | Sujet | Durée | Taille | SHA-256 (MP4) |
|---|---|---|---|---|
| `sortie/tutoriel-rapido-RHV2-07.mp4` | Des réunions qui deviennent des tâches | 1:15 | 3,9 Mo | voir manifeste |
| `sortie/tutoriel-rapido-RHV2-08.mp4` | Recruter avec RapidoRH | 0:56 | 2,3 Mo | voir manifeste |
| `sortie/tutoriel-rapido-RHV2-09.mp4` | Piloter l'équipe hybride | 0:38 | 1,7 Mo | voir manifeste |
| `sortie/tutoriel-rapido-RHV2-10.mp4` | Le journal d'audit | 0:37 | 1,5 Mo | voir manifeste |

Manifestes, sous-titres et fiches Académie : `PrendsTaPart/rapido-RH`, `docs/rapidorh-v2/tutoriels-v2/` (`episodes/RHV2-*/manifest.json`, `ACADEMIE_A_PUBLIER.json`).
Non publiés : ni bibliothèque RapidoCMS, ni Académie, ni réseaux.
