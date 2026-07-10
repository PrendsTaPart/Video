# Série « 30 routines pour faire tourner ta boîte » — usine de production

30 épisodes (3 saisons × 10), publication quotidienne LinkedIn + TikTok (compte **BraindCode**),
vertical 9:16 1080×1920, 45–60 s, avatar Mika en hook d'ouverture/clôture.

## Contenu de ce dossier
- `serie-30-episodes.md` — index des 30 épisodes (routine · prompt · cas d'usage · hook).
- `scripts/saison-1.md · saison-2.md · saison-3.md` — **les 30 scripts complets** (gabarit rempli,
  fil rouge « Léa ouvre son restaurant », CTA en rotation A/B/C, teasers chaînés). → **à valider (batch).**
- `mika-textes.md` — **60 textes Mika** (in/out) prêts pour le kit HeyGen vertical, en 3 lots de 20.
- `serie-etat.json` — état + budgets + comptes + kill-switch (`pause`).
- `R9-VIDEO-FACTORY.md` — spec de la routine quotidienne + déclenchement n8n + gouvernance.

## État d'avancement (pré-production — Partie 7 étape 1)
- ✅ Plan + index des 30 épisodes
- ✅ 30 scripts complets (saisons 1–3)
- ✅ 60 textes Mika (in/out) prêts pour HeyGen
- ✅ serie-etat.json + R9-VIDEO-FACTORY.md
- ✅ LinkedIn BraindCode confirmé : `101119080`

## ⛔ Bloquants à lever avant lancement
1. **TikTok non connecté au CMS** (réseaux vus : facebook/linkedin/instagram). → Connecter
   TikTok BraindCode dans RapidoCMS, puis renseigner `tiktok_account_id` dans serie-etat.json.
   Sans ça, seul LinkedIn peut être publié.
2. **Clips Mika** — 60 clips à produire par lots de 20 (kit HeyGen vertical, buste serré, fond
   vert #00B140). Textes = `mika-textes.md`. Upload en bibliothèque CMS (nommage `mika-e{N}-in/out`).
3. **Installation plugin** — R9 + workflows n8n vivent dans le dépôt **plugin (loop-engine-v2)**,
   PAS dans ce dépôt vidéo. À installer là-bas (voir R9-VIDEO-FACTORY.md).
4. **Paramètres à figer** : `date_debut`, budget rendu (`plafond_par_jour` / `plafond_total`).
5. **Pilote E1** à rendre et approuver, puis `pause:false` + `budget.rendu_autorise:true`.

## Checklist de lancement
1. ☐ Valider les 30 scripts (batch, par saison) — *ce dossier*
2. ☐ Produire le lot 1 des clips Mika (E1–E10, 20 clips) + upload CMS
3. ☐ Connecter TikTok BraindCode au CMS + renseigner l'account_id
4. ☐ Rendre & approuver le pilote E1 + écrire le budget dans serie-etat.json + `pause:false`
5. ☐ Activer les workflows n8n (07:00 / 08:15) — après accord explicite
6. ☐ Chaque week-end : produire le lot Mika suivant + relire les 10 scripts à venir

## Note
Ce dépôt (`PrendsTaPart/Video`) est le **studio vidéo**. La partie « installation de l'usine »
(routine R9 dans loop-engine-v2, workflows n8n, rapido-kb) doit être exécutée dans les dépôts
correspondants — non présents dans cette session. Les scripts, textes Mika et specs ci-dessus
sont directement réutilisables.
