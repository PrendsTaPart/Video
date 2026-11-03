# Épisode 32/365 : « J'ai appris à mon site à écrire à mes contacts »

89 s (+ short 46 s) · 9:16 · 1080 × 1920 · 30 i/s · voix Noé (ElevenLabs `7pDdnNI6PhXmAp0pXFZm`, eleven_v4, une prise de 56,7 s, ralentie à 0,9 → 63 s) · narration à la première personne · musique `videos/planit-academy/assets/audio/musique-produit.mp3` à 30 % avec ducking, -14 LUFS visé.

La voix fait 56,7 s : la vidéo a été montée en 83 s (2,8 s de respiration par scène) plutôt qu'en 120 s, pour éviter de longs passages sans voix.

Le texte d'origine était dans une session qui n'est plus lisible : le script a été réécrit à partir des sources réelles (formation 32, dépôt `michael-au-quotidien`, migration `0011_episode32_nurturing.sql`, outils MCP).

## Narration

> **Refait le 28/10** à la demande de Michael : même voix et même modèle que les épisodes 1 à 30 (Noé, `eleven_v4`, débit naturel), langage simple sans terme technique ni chiffre, textes techniques retirés de l'écran. Nouvelle durée : 69s. Les temps du storyboard ci-dessous sont ceux de la version précédente ; l'ordre des scènes est inchangé.

Aujourd'hui, je me suis rendu compte d'un problème : des gens laissent leur email sur mon site pour recevoir une formation… et ensuite, je ne leur écris jamais.

Alors j'ai décidé de garder le lien avec eux, par email, avec l'aide de Claude et de Lovable.

Première règle : demander la permission. Recevoir une formation, ce n'est pas accepter de recevoir mes nouvelles. Il y a une case à part, que la personne coche elle-même.

Ensuite, Lovable a dessiné mes emails, aux couleurs de chacun de mes logiciels.

Chaque email a un seul but et un seul bouton : commencer la formation, découvrir une ressource, tester un logiciel, ou prendre rendez-vous.

Et Claude peut préparer mes emails et mes publications à ma place. Mais il n'envoie rien, et il ne publie rien. Il prépare, je valide.

Désormais, chaque vidéo a sa suite : sa formation, son guide à télécharger, son email et ses publications. Et je vois tout de suite ce qu'il manque.

Pour l'instant, aucun email n'est encore parti : il me reste à brancher l'envoi. Mais chaque personne qui laisse son email peut maintenant devenir une vraie relation.

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
