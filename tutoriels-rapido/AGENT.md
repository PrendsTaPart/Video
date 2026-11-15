# AGENT.md — Tutoriels et formations : tâches des agents IA (15/11/2026)

Méthode complète : `PLAN.md` (chaîne de production, règles, journal). Tâches humaines : `Ahmed.md`.

1. [ ] CRM65 : voix présente ; le tournage a échoué (TimeoutError Playwright) → essai à blanc, corriger le sélecteur dans `CRM65/tuto.json`,
       puis `bash _gabarit/file.sh CRM65` (après `bash _gabarit/serveurs.sh`). Ne jamais tourner pendant un rendu.
2. [ ] CRM66–CRM69 : scénarios prêts ; voix Adam (voice_id TGAegA0zNRi8I6nUdq3i, eleven_v4, une prise) après accord de Michael sur les crédits.
3. [ ] CRM50–CRM64 : écrire les scénarios (lire vues et routes de rapido-crm), puis produire.
4. [ ] Formations F40–F43 : `bash _gabarit/make-formation.sh F40` (scripts 60–90 s).
5. [ ] Publier dans RapidoCMS et l'Académie comme les épisodes précédents (`_gabarit/preparer-publication.sh`, `enregistrer-publication.py`).
6. [ ] Cocher dans PLAN.md, compléter le journal, pousser la branche `tutoriels-rapido`.
Données de démo : `php artisan tinker` dans rapido-crm-film puis `require '…/_gabarit/cartes-demo.php'`.
