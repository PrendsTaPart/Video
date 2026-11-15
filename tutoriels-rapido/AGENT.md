# AGENT.md — Tutoriels et formations : tâches des agents IA (15/11/2026)

Méthode complète : `PLAN.md` (chaîne de production, règles, journal). Tâches humaines : `Ahmed.md`.

1. [x] CRM65 (rendu 76 s, 15/11 soir ; reste la publication RapidoCMS + Académie) : voix présente ; le tournage a échoué (TimeoutError Playwright) → essai à blanc, corriger le sélecteur dans `CRM65/tuto.json`,
       puis `bash _gabarit/file.sh CRM65` (après `bash _gabarit/serveurs.sh`). Ne jamais tourner pendant un rendu.
2. [~] CRM66–CRM69 : voix générées le 15/11 ; CRM66 rendu et vérifié (56 s) ; CRM69 en production ; CRM67–CRM68 en file après essai à blanc ; voix Adam (voice_id TGAegA0zNRi8I6nUdq3i, eleven_v4, une prise) après accord de Michael sur les crédits.
3. [~] CRM50–CRM64 : CRM50 rendu et vérifié (60 s) ; CRM51, CRM52 en production ; CRM62, CRM63, CRM64 écrits, validés à blanc, voix générées (16/11), en file (`/tmp/claude-0/file4.sh`) ; CRM53–CRM61 à écrire. Pièges : un `confirm()` JS se valide par `"eval": "window.confirm = () => true"` avant le clic ; `button.btn-primary` seul attrape souvent un autre bouton (préfixer par l'id du formulaire).
4. [ ] Formations F40–F43 : `bash _gabarit/make-formation.sh F40` (scripts 60–90 s).
5. [ ] Publier dans RapidoCMS et l'Académie comme les épisodes précédents (`_gabarit/preparer-publication.sh`, `enregistrer-publication.py`).
6. [ ] Cocher dans PLAN.md, compléter le journal, pousser la branche `tutoriels-rapido`.
Données de démo : `php artisan tinker` dans rapido-crm-film puis `require '…/_gabarit/cartes-demo.php'`.

Outils : `node _gabarit/essai-blanc.cjs <EP> http://127.0.0.1:8124` (avant toute voix) ; `node _gabarit/reperage.cjs http://127.0.0.1:8124 /chemin` (écrire un scénario).
