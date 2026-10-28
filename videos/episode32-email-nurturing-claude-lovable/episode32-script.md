# Épisode 32/365 : « J'ai appris à mon site à écrire à mes contacts »

89 s (+ short 46 s) · 9:16 · 1080 × 1920 · 30 i/s · voix Noé (ElevenLabs `7pDdnNI6PhXmAp0pXFZm`, eleven_multilingual_v2, une prise de 56,7 s, ralentie à 0,9 → 63 s) · narration à la première personne · musique `videos/planit-academy/assets/audio/musique-produit.mp3` à 30 % avec ducking, -14 LUFS visé.

La voix fait 56,7 s : la vidéo a été montée en 83 s (2,8 s de respiration par scène) plutôt qu'en 120 s, pour éviter de longs passages sans voix.

Le texte d'origine était dans une session qui n'est plus lisible : le script a été réécrit à partir des sources réelles (formation 32, dépôt `michael-au-quotidien`, migration `0011_episode32_nurturing.sql`, outils MCP).

## Narration

Aujourd'hui, je me suis rendu compte d'un problème : des personnes laissent leur email sur mon site pour débloquer une formation… et ensuite, je ne leur écris jamais.

Alors j'ai décidé de mettre en place l'email nurturing, avec Claude, Lovable et le MCP de mon site.

Première règle : séparer les consentements. Débloquer une formation, ce n'est pas s'abonner à mon actualité. Il y a une case à part, jamais cochée d'office.

Ensuite, j'ai demandé à Lovable de dessiner mes emails en HTML et en CSS, puis de les exporter en images. Quarante-six visuels, aux couleurs de chacun de mes logiciels.

Chaque email a un seul objectif et un seul bouton : commencer l'étape un, découvrir une ressource, tester un logiciel, ou prendre rendez-vous.

Et j'ai donné des outils à Claude, par MCP : préparer la campagne d'un nouvel épisode, choisir les images, préparer les publications. Mais aucun outil n'envoie, ni ne publie. Claude prépare, je valide.

Désormais, chaque vidéo déclenche une chaîne : sa formation, son PDF, son lead magnet, sa campagne et ses publications. Et un outil me dit ce qui manque, dans l'ordre.

Pour l'instant, rien n'est encore parti : il me reste à brancher l'envoi. Mais chaque formulaire de mon site peut maintenant devenir une vraie relation.

## Storyboard

| Temps | Image | Mention à l'écran |
|---|---|---|
| 0–9,5 s | Portrait, logos Claude / Lovable / MCP, « ET JE NE LEUR ÉCRIS JAMAIS. », capture réelle de la page Formations | — |
| 9,5–17,4 s | « L'IDÉE » · L'email nurturing, logos, couverture réelle du PDF formation 32 | — |
| 17,4–27,1 s | « RÈGLE N°1 » · deux cases (formation / actualité), extrait réel de la migration SQL | « Illustration du principe » · « Extrait réel du code du site » |
| 27,1–39,2 s | « LE DESIGN » · email reconstitué avec les vrais visuels qui défile, « 46 », les 6 héros par logiciel | — |
| 39,2–48,7 s | « LA SÉQUENCE » · vrais boutons J+1 / J+2 / J+3 et visuel rendez-vous | « Séquence en brouillon · rien n'est encore envoyé » |
| 48,7–61,2 s | « LES OUTILS DE CLAUDE » · `creer_campagne_email`, `lister_medias`, `preparer_publication`, `tester_campagne_email` ; envoi à la base et publication : n'existent pas | « Noms réels des outils du MCP du site » |
| 61,2–71,8 s | « LA CHAÎNE D'UN ÉPISODE » · vidéo → formation → PDF → lead magnet → campagne → publications, outil `etat_episode` | — |
| 71,8–82,8 s | « OÙ J'EN SUIS » · 8 modèles, 46 visuels, 53 outils MCP dont 16 emails, 112 images ; ÉPISODE 32/365 · CLAUDE × LOVABLE × MCP | « Envoi pas encore branché · 0 email de nurturing envoyé » |

Short 46 s : accroche (0–9,5) · règle n°1 (17,4–27,1) · outils de Claude (48,7–61,2) · où j'en suis (71,8–82,7).

## Points de vérité

- Chiffres repris de la formation 32 (« Ce qui est réellement en place, au 27/10 au soir ») : 8 modèles en brouillon, 46 visuels, 53 outils MCP dont 16 pour les emails, la médiathèque, les épisodes et les statistiques, 112 images.
- Noms d'outils de `src/lib/mcp/tools/` ; `tester_campagne_email` n'envoie qu'à l'adresse du compte connecté. Aucun outil d'envoi à la base ni de publication.
- La page publique de la formation 32 répondait « Cette formation n'existe pas » le 27/10 (pas encore publiée) : la vidéo montre le PDF. **Publier la formation 32 avant de diffuser la vidéo.**
- Le visuel des deux cases est une illustration du principe, signalé à l'écran.

## Fichiers

`episode32-final-89s.mp4`, `episode32-short-46s.mp4`, `episode32-miniature.png`, `episode32-sous-titres.srt`, `episode32-short-46s.srt`, `episode32-voix.mp3` (voix seule), `episode32-voix-mix.mp3` (mix), `composition/` (page HTML rendue image par image, `engine.js` commun, scripts `align.py`, `build_cfg.py`, `render.js`, `finish.py`).

## Réglage du son (28/10)

Voix ralentie à 0,9 (atempo, timbre conservé) et coupée au milieu des silences entre paragraphes : plus aucun mot tronqué. Musique à 20 %. Les minutages du storyboard ci-dessus datent de la version précédente ; les minutages exacts sont dans `composition/config.json`.
