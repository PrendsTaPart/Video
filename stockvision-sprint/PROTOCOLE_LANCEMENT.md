# Protocole de lancement du développement — Sprint E-commerce/KDS/Jarvis

Décision d'exécution (revue senior du 2026-07-06). Ce document dit COMMENT on
lance, dans quel ordre, et ce qui bloque un merge.

## 0. Pré-requis d'accès (bloquant aujourd'hui)

Le développement se fait dans le repo **`stockvisionai-production`** — qui
n'est PAS accessible depuis la session Claude Code actuelle (scope limité à
`PrendsTaPart/Video`). Pour lancer réellement :

1. Ouvrir une session Claude Code **sur le repo `stockvisionai-production`**
   (ou ajouter ce repo au scope de l'environnement Claude Code web).
2. Y committer d'abord le Lot -1 (specs dans `/docs/specs/`, voir C2 des
   ajustements) : le CdC complet + les prompts corrigés + les schémas extraits.
3. Dérouler ensuite les lots dans l'ordre ci-dessous, un prompt = une session.

## 1. Ordre d'exécution décidé (dépendances réelles)

```
Lot -1 (specs) → Lot 0 (fondations)
  → Lot 1 (site) → Lot 2 (tunnel) → Lot 3 (agent) → Lot 4 (fidélité/leads)
  → Lot 5 (Cloudflare, parallélisable avec 3-4)
  → Lot 6 (KDS) → Lot 7 (QR table)
  → Lot 8 (Rapido, indépendant — bouche-trou idéal si un lot bloque)
  → Lot 9 (MCP scoping — exige lots 1-7 mergés) → Lot 10 (Jarvis)
  → Lot 11 (monétisation) → Lot 12 (durcissement + démo S4)
Sprint 2 : Lot 13 → 14 → 15. Puis phase caisse HubRise, puis NF525 (B1 d'abord).
```

Règles : ordre de merge = cet ordre ; rebase quotidien ; jamais de référence
aux migrations d'une branche non mergée.

## 2. Gates de qualité (aucun merge sans les 4)

1. Critères d'acceptation du lot démontrés (capture/log dans la PR).
2. Suite de tests COMPLÈTE verte (pas seulement les nouveaux tests).
3. Revue humaine de la PR (Soulayma) — l'agent ne s'auto-merge pas.
4. CLAUDE.md mis à jour (décisions, nouveaux packages justifiés).

Chaque PR contient : résumé, points de vigilance, grep secrets du diff,
migrations réversibles vérifiées.

## 3. Environnements

- **local/CI** : SQLite ou MySQL éphémère, `migrate:fresh --seed` +
  `DemoEstablishmentSeeder` (C14) — données de recette identiques pour tous.
- **staging** : clone prod + Stripe test + Twilio sandbox + zone Cloudflare de
  test. La démo S4/S7 se joue sur staging, jamais en local.
- **prod** : migrations additives uniquement pendant le sprint ; tout nouveau
  module derrière feature flag par établissement (C4) → rollback = toggle,
  pas revert.

## 4. Scénarios d'échec anticipés (et parade codée, pas improvisée)

| Scénario | Parade (lot) |
|---|---|
| Webhook Stripe perdu / rejoué | Idempotence + job réconciliation horaire (C5, Lot 2) |
| Deux commandes sur le dernier créneau | Lock atomique capacité, test de concurrence (Lot 2) |
| Prix falsifié côté client | Recalcul serveur systématique via quote (Lot 2) |
| Reverb down | Fallback polling KDS/suivi (Lots 2, 6) + offline-first D7 |
| Session Jarvis qui dépasse le quota en cours | Battements 60 s + fermeture propre (C6) |
| Deepgram/ElevenLabs down | Message vocal d'erreur pré-enregistré (C6) |
| Envoi marketing 20h30 depuis serveur UTC | Fenêtres légales évaluées en Europe/Paris + tests aux bords (C7) |
| Fuite données clients vers l'API IA | Allowlist de contexte + test payload (C8) |
| Token Cloudflare invalide / quota | Dégradation écran Domaine, module isolé (C9) |
| display_token KDS qui fuite | Token long, scope lecture+bump, throttle, noindex (C10) |
| Format date Rapido | H:i:s vérifié en prod réelle, doc de l'outil fausse (C11) |
| SSR sous charge SEO | Cache par page publiée + purge à l'édition (C12) |
| Abonnement expiré + domaine custom | Vitrine réduite, jamais 404 (Lot 11) |
| Lot en retard | Ordre de sacrifice pré-validé du CdC §13.5 — on coupe, on ne rallonge pas |

## 5. Suivi

- Un tableau de bord de sprint = la liste des PR par lot avec leur gate status.
- Jalons de démo : fin S4 (site → commande → KDS → Jarvis), fin S7 (campagne
  → CA attribué), fin S9 (ticket caisse), fin octobre (attestation NF525).
- Toute ambiguïté de spec = question posée dans la PR, jamais d'interprétation
  silencieuse (règle du CdC §1.1, elle prévaut).
