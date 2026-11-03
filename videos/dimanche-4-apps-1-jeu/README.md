# « Mon dimanche à la maison : 4 applications et un jeu vidéo »

Vidéo verticale 1080 × 1920 pour LinkedIn, Instagram, TikTok et Facebook.
**Rien n'a été publié** : tout attend ta validation.

## Livrables

| # | Livrable | Fichier |
|---|---|---|
| 1 | Storyboard minuté | ce document, § Storyboard |
| 2 | Voix off définitive | ce document, § Voix off + `audio/voix-off-noe.mp3` |
| 3 | Captures utilisées et provenance | ce document, § Captures |
| 4 | Vidéo finale MP4 (82 s, sous-titres incrustés) | `renders/dimanche-4-apps-1-jeu_1080x1920.mp4` |
| 5 | Miniature de couverture | `renders/miniature-1080x1920.jpg` |
| 6 | Légendes LinkedIn et Instagram | ce document, § Légendes |
| 7 | Version courte (29,8 s) | `renders/dimanche-4-apps-1-jeu_30s_1080x1920.mp4` |
| — | Sous-titres séparés (SRT + ASS) | `sous-titres/` |
| — | Mixage, musique seule, voix seule | `audio/` |

Caractéristiques : H.264 High, 30 i/s, AAC 192 kb/s, environ −15 LUFS intégrés, sous-titres français synchronisés mot à mot (horodatage par transcription de la voix).

## Ce qui a changé par rapport au brief, et pourquoi

Le contrôle des sources a imposé trois corrections au texte :

1. **Caisse : « paiement NFC » retiré.** Dans le code, `Tap to Pay` est marqué « Bientôt » et désactivé (`foodeatup-caisse-mobile/app/lib/features/payment/presentation/payment_screen.dart`, `available: false`). caisse.foodeatup.fr écrit aussi : « Tap to Pay : intégration en cours ». Le badge NFC d'employé n'est pas encore construit (`login_screen.dart`, `nfc_manager` en commentaire dans `pubspec.yaml`). La voix dit donc : « Le paiement sans contact, c'est la prochaine étape », et une pastille « bientôt » s'affiche à l'écran.
2. **Tablette : « sondages » déplacé vers la borne de fidélité.** Rien dans le code du menu digital ne concerne les sondages. L'app Fidélité, elle, a l'écran « Sondage express » (capture `08_survey`).
3. **Minutage : 82 s au lieu de 90 s.** La voix générée dure 56 s. Les sections sont placées sur les blocs du brief avec des respirations musicales, et FoodEatUp Rush garde 5 s d'images sans voix.

Également : les APK n'ont pas pu être installés, car le conteneur n'a pas de KVM, donc pas d'émulateur Android. Toutes les images viennent des captures réelles déjà produites (fiches Play, rendus des tests Flutter, sites). L'avatar 3D est la vraie scène WebGL embarquée dans l'APK HACCP (`app/assets/avatar/`), filmée dans Chromium. Le jeu est filmé en direct depuis son URL.

## Voix off définitive

Voix ElevenLabs « Noé – Content Creator », modèle `eleven_v4`, take A (la take B reste dans le flow ElevenLabs). Ce n'est pas ta voix : aucun clone n'existe dans l'espace ElevenLabs. Voir § À faire.

> Mon dimanche à la maison ? J'ai décidé de développer quatre applications mobiles… et un jeu vidéo, pour FoodEatUp.
>
> Première application : une borne de fidélité à installer directement au comptoir, pour récompenser les clients. Ils cumulent des points, tournent la roue et répondent à des sondages.
>
> Deuxième application : un assistant HACCP vocal, avec un avatar 3D. Avec des oreillettes, les équipes accèdent aux fonctionnalités HACCP, impriment sur une imprimante compatible, et apprennent grâce au mode école.
>
> *(Jarvis, clip réel de l'app : « C'est enregistré, merci ! »)*
>
> Troisième application : une caisse mobile pour les serveurs, avec scanner de QR code, et un mode école accompagné par un avatar 3D. Le paiement sans contact, c'est la prochaine étape.
>
> Quatrième application : une tablette interactive pour les clients, avec menu digital, commandes, jeux-concours et fidélité.
>
> Et chaque restaurant peut personnaliser le thème et la charte graphique de ses applications.
>
> Et pour terminer, FoodEatUp Rush : un jeu vidéo 3D qui transforme l'univers de la restauration en expérience interactive.
>
> Tout ça, depuis la maison, avec Flutter, l'IA et les outils MCP FoodEatUp. Maintenant, prochaine étape : Google Play et l'App Store.

## Storyboard (version 82 s)

| Temps | Scène | Voix | Images |
|---|---|---|---|
| 0,0–6,8 | Accroche | « Mon dimanche à la maison ? … pour FoodEatUp. » | Titre « Mon dimanche à la maison ? », fenêtre « Google Drive › APK FoodEatUp ». Les 4 vrais APK et leurs vraies tailles s'affichent un par un (24,0 / 133,7 / 86,2 / 28,6 Mo), puis la pastille « + un jeu vidéo 3D » et le logo FoodEatUp |
| 6,8–16,6 | App 1 · Fidélité | « Première application … sondages. » | Tablette : attract → n° de téléphone → accueil client → récompenses → roue cadeaux → sondage. Pastilles Points / Roue cadeaux / Sondages au mot près |
| 16,6–30,6 | App 2 · HACCP vocal | « Deuxième application … mode école. » + Jarvis | Téléphone : accueil → température 3,2 °C → étiquette DLC → mode école → historique. Carte de l'avatar 3D Jarvis animé. Pastilles Oreillettes / Imprimante / Mode école, puis bulle « C'est enregistré, merci ! » (vrai clip audio de l'app) |
| 30,6–41,4 | App 3 · Caisse mobile | « Troisième application … prochaine étape. » | Deux téléphones : plan de salle + commande table 12. Pastilles Scanner QR code / Mode école + chef 3D (écran Formation avec Jarvis). Écran Paiement + pastille « Paiement sans contact : bientôt » |
| 41,4–50,2 | App 4 · Tablette client | « Quatrième application … fidélité. » | Tablette : accueil table T7 → carte → panier → jeux concours → Club fidélité. Pastilles Menu / Commande / Jeux / Fidélité |
| 50,2–56,6 | Personnalisation | « Et chaque restaurant … applications. » | Six styles réels de la caisse (Braise, Brasserie, Comptoir, Épure, Indigo, Prairie), puis l'éditeur « Votre thème » du menu digital qui monte par-dessus |
| 56,6–68,6 | FoodEatUp Rush | « Et pour terminer … interactive. » (puis 5 s de musique) | Écran titre du jeu sur téléphone, puis écran paysage : façade 3D → salle → chef Marco → service en vue de dessus avec l'écran cuisine |
| 68,6–76,6 | Conclusion | « Tout ça, depuis la maison … App Store. » | « Tout ça, depuis la maison. » + pastilles Flutter / IA / MCP FoodEatUp, carte « Prochaine étape : Google Play & App Store », avec la mention « Publication sur les stores : pas encore faite. » |
| 76,6–82,0 | Carton final | musique | FoodEatUp × BraindCode (logos officiels dans des pastilles blanches), « Comment je m'y suis pris ? Posez la question en commentaire. » |

### Version courte (29,8 s)

Accroche (0–6,3) → montage rapide sans voix des 4 apps, 1,8 s chacune (Fidélité, HACCP + avatar, Caisse, Tablette) → FoodEatUp Rush avec voix (13,5–20,1) → conclusion avec voix (20,1–27,4) → carton FoodEatUp × BraindCode. Musique continue, sous-titres de la voix seulement.

## Captures utilisées et provenance

Chaque scène porte à l'écran une mention « Captures réelles · source ».

| Scène | Images | Provenance |
|---|---|---|
| Accroche | Noms et tailles des 4 APK | Dossier Google Drive fourni (métadonnées lues le 26/10/2026) |
| Fidélité | `01_attract`, `02_phone`, `04_home`, `05_rewards`, `07_wheel`, `08_survey` | Rendus des tests Flutter de l'app (`foodeatup-fid-lit/mobile/test/golden/goldens/`) |
| HACCP | `1-accueil`, `2-temperature`, `3-etiquette`, `6-historique` | Captures de la fiche Google Play (`foodeatup-haccp/app/play/listing/fr-FR/images/phoneScreenshots/`), générées par les tests de l'app |
| HACCP | Mode école `ecole-missions.webp` | Image publiée sur haccp.foodeatup.fr |
| HACCP | Avatar 3D Jarvis (vidéo) | Scène WebGL réelle de l'APK (`foodeatup-haccp/app/assets/avatar/` : `avatar.js` + `chef.glb` CC0), filmée dans Chromium, humeurs pilotées par son API `window.avatar` |
| HACCP | Voix « C'est enregistré, merci ! » | Clip réel de l'app (`app/assets/voice/jarvis_enregistre.mp3`) |
| Caisse | `03-accueil`, `04-plan-de-salle`, `06-commande`, `07-paiement`, `21-formation` | Captures publiées sur caisse.foodeatup.fr (`/screens/…`) |
| Tablette | `Accueil_fr`, `C02_fr`, `C05_fr`, `C08_jeux_fr`, `C08_points_fr` | Rendus des tests Flutter de l'app (`foodeatup-menu-digital/app/test/goldens/`). Les vignettes produits y sont vides : c'est le rendu de test, pas un défaut du montage |
| Personnalisation | `*-accueil.png` (6 styles) + `R03_fr` | `foodeatup-caisse-mobile/app/docs/captures/` + golden « Votre thème » du menu digital |
| Rush | Écran titre + 4 plans en jeu | Filmé en direct sur https://formation.foodeatup.fr/jeux/restaurant-3d/index.html (rendu logiciel sans GPU, d'où une caméra parfois lente) |
| Carton | Logos FoodEatUp (toque) et BraindCode | `foodeatup-haccp/design/brand/`, `growth-loop-academy/public/brand/chartes/braindcode.png` |
| Audio | Voix off, musique électro | ElevenLabs (voix Noé, `eleven_v4` ; musique `eleven_music_v2_5`, instrumentale, vérifiée sans paroles) |

Aucune capture n'a été inventée. Aucun avis, chiffre de téléchargement, statistique ou publication store n'apparaît.

## Légendes

### LinkedIn

> Mon dimanche à la maison ? 4 applications mobiles et un jeu vidéo pour FoodEatUp.
>
> Pendant que certains profitent de leur dimanche, moi je construis l'avenir de la restauration avec mes agents IA.
>
> Ce qui est sorti :
> 1️⃣ Une borne de fidélité au comptoir : points, roue cadeaux, sondages express.
> 2️⃣ Un assistant HACCP vocal avec un avatar 3D : relevés à la voix avec des oreillettes, impression d'étiquettes, mode école pour former les équipes.
> 3️⃣ Une caisse mobile pour les serveurs : commande à table, scanner de QR code, mode école avec un chef 3D. Le paiement sans contact sur le téléphone est la prochaine étape.
> 4️⃣ Une tablette client : menu digital, commande, jeux-concours, fidélité.
> 🎮 Et FoodEatUp Rush, un jeu 3D jouable dans le navigateur qui fait vivre le service de l'intérieur.
>
> Chaque restaurant peut adapter le thème et la charte graphique de ses applications.
>
> La stack : Flutter, l'IA et les outils MCP FoodEatUp.
> Prochaine étape : la publication sur Google Play et l'App Store (pas encore faite).
>
> Vous vous demandez comment c'est possible ? Posez la question en commentaire, je réponds à tout.
>
> #FoodEatUp #BraindCode #Restauration #IA #Flutter #MCP #Entrepreneuriat #FoodTech

### Instagram

> Mon dimanche à la maison 🏠 → 4 applis + 1 jeu vidéo pour FoodEatUp 🍳
>
> 📲 Borne de fidélité au comptoir
> 🎧 HACCP à la voix avec un chef 3D
> 💳 Caisse mobile pour les serveurs
> 📋 Menu digital sur tablette
> 🎮 FoodEatUp Rush, le jeu 3D
>
> Flutter + IA + MCP FoodEatUp. Prochaine étape : Google Play et App Store 🚀
>
> Comment c'est possible ? Demande en commentaire 👇
>
> #foodeatup #braindcode #restaurant #restauration #ia #flutter #foodtech #entrepreneur #buildinpublic #appmobile

## Contrôle final

- [x] Les quatre applications apparaissent : Fidélité 6,8 s, HACCP 16,6 s, Caisse 30,6 s, Tablette 41,4 s (dans la version courte aussi).
- [x] FoodEatUp Rush est montré avec de vraies images du jeu en ligne (56,6–68,6 s).
- [x] Les fonctions annoncées correspondent aux sources. NFC retiré (non livré) et « sondages » attribués à la borne de fidélité (voir § Ce qui a changé).
- [x] La vidéo précise que la publication sur Google Play et l'App Store reste à faire : à la voix (« prochaine étape ») et à l'écran (« Publication sur les stores : pas encore faite »).
- [x] La voix ne prétend ni à une durée de travail vérifiée, ni à une chronologie, ni à l'absence de bugs. « Mon dimanche à la maison » reste ton récit à la première personne, comme dans le brief.
- [x] Rien n'est publié sur les réseaux.

## À faire de ton côté (recommandé)

1. **Ta voix.** Le message est personnel. Enregistre le texte ci-dessus ou crée un clone ElevenLabs, puis remplace `audio/voix-off-noe.mp3`. Garde les mêmes respirations : les coupes du mixage sont dans `scripts/mix-82s.ffmpeg.txt` (le script de sous-titres `scripts/subs.py` est à recaler si le débit change).
2. **Un plan de toi à la maison** pour l'accroche (0–6 s). La bibliothèque Higgsfield du dépôt ne contient que des plans de restaurant (`hero-video/assets/video/`), aucun plan de domicile. Selon `CLAUDE.md`, je n'ai rien généré. Si tu veux ce plan en IA, voici le prompt à lancer toi-même dans Higgsfield, avec ton Reference Element personnage :
   > Plan vertical 9:16, 4 s, dimanche après-midi, lumière naturelle douce. Un entrepreneur à son bureau dans un salon, ordinateur portable ouvert sur du code, un smartphone et une tablette posés à côté. Il tape vite, sourit, attrape le téléphone. Léger travelling avant, ambiance chaleureuse, bleu et orange en touches de couleur.
3. Pour TikTok et Instagram, les sous-titres sont incrustés. Pour LinkedIn et Facebook, tu peux aussi charger `sous-titres/sous-titres-fr.srt`.

## Reconstruire

```bash
bash scripts/preparer-assets.sh           # dossier a/ (captures, séquences vidéo)
python3 -m http.server 8777 &             # depuis ce dossier, sert composition.html (copier en index.html)
node scripts/render.js frames 0 2460      # 82 s × 30 i/s, 1080×1920 (4 processus en parallèle : ~100 s)
ffmpeg -framerate 30 -i frames/%05d.jpg -i audio/mix-final.mp3 -vf ass=sous-titres/sous-titres-fr.ass \
  -c:v libx264 -crf 18 -pix_fmt yuv420p -c:a aac -b:a 192k -shortest renders/dimanche-4-apps-1-jeu_1080x1920.mp4
```

Le mixage (voix aux temps du storyboard, clip Jarvis, musique compressée sous la voix, normalisation −14 LUFS) est dans `scripts/mix-82s.ffmpeg.txt`, et la version courte dans `scripts/montage-30s.ffmpeg.txt`. ElevenLabs : flow `nwXcfCS1VCCkoDxiqcHC` (2 takes de voix, 2 musiques).
