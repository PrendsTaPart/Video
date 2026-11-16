# AGENT.md — Tutoriels et formations : tâches des agents IA (15/11/2026)

Méthode complète : `PLAN.md` (chaîne de production, règles, journal). Tâches humaines : `Ahmed.md`.

1. [x] CRM65 (rendu 76 s, 15/11 soir ; reste la publication RapidoCMS + Académie) : voix présente ; le tournage a échoué (TimeoutError Playwright) → essai à blanc, corriger le sélecteur dans `CRM65/tuto.json`,
       puis `bash _gabarit/file.sh CRM65` (après `bash _gabarit/serveurs.sh`). Ne jamais tourner pendant un rendu.
2. [~] CRM66–CRM69 : voix générées le 15/11 ; CRM66 rendu et vérifié (56 s) ; CRM69 en production ; CRM67–CRM68 en file après essai à blanc ; voix Adam (voice_id TGAegA0zNRi8I6nUdq3i, eleven_v4, une prise) après accord de Michael sur les crédits.
3. [~] CRM50–CRM69 (16/11, 2 h) : rendus et vérifiés CRM50, 51, 52 (retourné), 62, 65, 66, 67, 68, 69 ; en file : CRM59, 60, 61, 63 et 64 (retournés), 56, 58, 42 ; publication RapidoCMS + Académie en cours (lot 1 : CRM50, 51, 62, 65, 66, 68, 69). Restent à écrire : CRM53 (éditeur), CRM54 (éditeur sur téléphone), CRM55 (ventes : clé Stripe de test nécessaire, Ahmed.md), CRM57 (tunnel créé par Claude). CRM31 : pas d'écran (décision de Michael). Pièges : un `confirm()` JS se valide par `"eval": "window.confirm = () => true"` avant le clic ; `button.btn-primary` seul attrape souvent un autre bouton (préfixer par l'id du formulaire) ; titre de carte → `zone_closest: ".card"` ; deux scènes de même `at` avec `zone` : la dernière gagne.
4. [~] Formations F40–F43 : scripts, slides et voix faits le 16/11 (55–65 s), rendu en file (file12). Puis F03–F34.
5. [ ] Publier dans RapidoCMS et l'Académie comme les épisodes précédents (`_gabarit/preparer-publication.sh`, `enregistrer-publication.py`).
6. [ ] Cocher dans PLAN.md, compléter le journal, pousser la branche `tutoriels-rapido`.
Données de démo : `php artisan tinker` dans rapido-crm-film puis `require '…/_gabarit/cartes-demo.php'`.

Outils : `node _gabarit/essai-blanc.cjs <EP> http://127.0.0.1:8124` (avant toute voix) ; `node _gabarit/reperage.cjs http://127.0.0.1:8124 /chemin` (écrire un scénario).


## Reste (16/11, 2 h)
- RH13 (pointage), RH16 (modèles d'e-mails), RH33 (messagerie : narration dans scripts-rh.json, scènes à ajouter dans gen-rh.py ; dépend de la messagerie « demandes » de RapidoRH V2).
- CMS11–CMS23 : RapidoCMS n'est pas installé dans la session (disque insuffisant pour un composer depuis les sources) → après suppression de /home/user/Video.
