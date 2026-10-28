# Épisode 36/365 : mon app HACCP sur Google Play, publiée par un agent IA

Tourné le 28/10. Style repris de la vidéo de référence fournie par Michael : fond noir, accent orange, mascotte étoile, gros chiffres qui claquent, sous-titres mot à mot avec les mots clés en orange, pseudo en haut à gauche et compte à rebours en haut à droite.

63 s (+ short 32 s) · 9:16 · 1080 × 1920 · 30 i/s · voix Noé (ElevenLabs `7pDdnNI6PhXmAp0pXFZm`, eleven_multilingual_v2, une prise, ralentie à 0,9) · musique `videos/planit-academy/assets/audio/musique-produit.mp3` à 20 % avec ducking.
Projets : site de l'app HACCP (Lovable `56f5e836-87ed-49d9-a58e-3c5d3a2777c1`) et ReleaseSync, MCP Google Play (Lovable `40be640d-20b0-4cf3-86fe-3af95d03765c`, https://play-track-release-control.lovable.app/mcp).

## Narration

Aujourd'hui, mon application HACCP est arrivée sur Google Play. Et ce n'est pas moi qui ai cliqué sur « publier ».

C'est un agent IA. Je lui ai construit un MCP avec Lovable : ReleaseSync. Seize outils, branchés sur l'API officielle de Google Play.

Je lui écris une seule phrase : « Publie FoodEatUp HACCP en test fermé. »

L'agent récupère le fichier de l'appli, choisit la piste, écrit les nouveautés… et fait d'abord une simulation. Google valide tout, rien n'est publié.

Je relis. Je dis oui. Version 1.6.2 : publiée.

Il a aussi rempli la fiche du store : le texte, l'icône, la bannière, et huit captures d'écran.

Et chaque action est écrite dans un journal : qui, quand, sur quelle appli.

L'appli, elle, fait vos relevés HACCP à la voix : températures, DLC, réceptions, nettoyage. En dix secondes.

Ma caisse et ma carte de fidélité sont déjà enregistrées dans ReleaseSync. Ce sont les prochaines.

Tu veux le même agent pour publier tes applis ? Écris « STORE » en commentaire. Épisode 36.

## Storyboard

| Temps | Image |
|---|---|
| 0–6,6 s | Fiche « FoodEatUp HACCP », version 1.6.2 · test fermé, puis « 0 clic de ma part » |
| 6,6–15,1 s | Mascotte « un agent IA », carte ReleaseSync (MCP construit avec Lovable), « 16 outils MCP » entouré des 16 noms réels, puce Android Publisher API |
| 15,1–20,7 s | Boîte de discussion : « Publie FoodEatUp HACCP en test fermé », appel `google_play_publish_release`, `dryRun: true`, `track: "alpha"` |
| 20,7–28,4 s | Les 4 étapes de l'agent, puis « Google Play : versionCode 12 validé · rien n'est publié » |
| 28,4–32,3 s | « OUI » puis « 1.6.2 », « PUBLIÉE · test fermé · 100 % », 28/10 · 13:59 |
| 32,3–37,8 s | Fiche du store fr-FR : texte, icône, bannière, 8 captures, « 8 » |
| 37,8–41,8 s | Journal `audit_logs` : 5 vraies lignes (13:59, 13:56, 11:17, 11:16, 09:55) |
| 41,8–50 s | Écran réel de l'app (site HACCP), températures, DLC, réceptions, nettoyage, « 10 s » |
| 50–55,2 s | Apps ReleaseSync : HACCP publiée, Caisse et Fidélité enregistrées, « les prochaines » |
| 55,2–63,3 s | Commentaire « STORE », ÉPISODE 36/365 · LOVABLE × CLAUDE × GOOGLE PLAY |

Short 32 s : accroche (0–6,6) · la phrase et la simulation (15,1–28,4) · oui, publiée (28,4–32,3) · appel à l'action (55,2–63,2).

## Points de vérité

- Relevé dans la base ReleaseSync le 28/10 : `google_play_publish_release` réussi à 12:59 UTC (13:59 à Paris) pour `com.foodeatup.haccp`, versionCode 12, nom « 1.6.2 (12) », piste `alpha` (test fermé), 100 %, déclenché par « Claude AI Agent », précédé d'une simulation réussie à 12:56 UTC.
- Fiche du store : `google_play_update_listing` fr-FR (08:55 UTC), icône, bannière et 8 captures d'écran envoyées (10:16–10:17 UTC).
- 16 outils déclarés dans `src/lib/mcp/index.ts` ; chaque écriture fait d'abord une simulation, puis attend l'accord.
- Caisse (`com.foodeatup.caisse`) et Fidélité (`com.foodeatup.fidelite`) sont enregistrées dans ReleaseSync, pas encore publiées.
- L'app est en **test fermé**, pas encore en production : Google impose 12 testeurs pendant 14 jours aux comptes développeurs personnels récents. La vidéo dit « test fermé » à l'écran et à la voix.
- La fiche Google Play de la première scène est une reconstitution (même nom, même package, même version), pas une capture de la Play Console. L'écran de l'app vient du site HACCP publié.
