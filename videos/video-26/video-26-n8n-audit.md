# Vidéo 26 — Audit n8n

## Statut : non revérifié dans cette session

Le connecteur N8n est connecté au compte mais **pas activé dans cette conversation**. Aucun workflow n'a été lu, exécuté ni modifié. Les statuts ci-dessous viennent de **votre inspection précédente (brief)**, sans revérification.

| Workflow | ID | Statut annoncé | Remarque |
|---|---|---|---|
| PRONO_0_Fixtures_Today | E3ZXA8HpZpHZDQHx | actif | 5 nœuds (webhook → API-Football → filtre → liste) |
| WC2026_1_Match_Prediction | UmRn6ULKA64C7MVN | actif | Agent Gemini ; **valeurs de saison et de compétition fixes** pour certaines statistiques ; probabilités **non calibrées** |
| WC2026_2_Frame_Generator | oHewWw1ENJCYZYLe | actif | Prompts Gemini Flash → images début/fin → déclenche WC2026_3 |
| WC2026_3_Video_Generator | Dp4WiZpSjan5A6IV | actif | **Détail inaccessible** : moteur, coûts et stockage inconnus, non montré |
| WC2026_4_Squad_Sync | E3EweIRCb131vNeE | actif | Lundi 2 h UTC, délai entre appels |
| W10 — Pre-Match Odds Snapshot | UFFE4AMu0WySoHyQ | actif | cotes : **aucun pari** dans la vidéo |
| W6 — Auto Publish RapidoCMS | HhXt2cuPxhKmOLcQ | **inactif** | montré « inactif » |
| W7 — Video Assembly Worker | LXoQ5jpQb71aI92q | **inactif** | déploiement restant |
| W8 — Viral Trend Watcher | yayEz3y4Y9Fpck1u | **inactif** | credentials manquants |

## Sécurité — à traiter

- Le brief signale des **secrets visibles directement dans certaines configurations n8n**. Je n'ai pas pu les voir ni les vérifier. **À faire tourner** (clés API-Football, Gemini, tokens de synchronisation) et à déplacer dans les credentials n8n.
- **Webhooks** de PRONO_0 et WC2026_2 : vérifier qu'ils exigent une authentification (en-tête ou secret). Sinon, n'importe qui peut déclencher des appels API payants.
- Aucune URL de webhook, clé ni paramètre secret n'apparaît dans la vidéo.

## Testé / opérationnel

Rien n'a été testé dans cette session. Aucune exécution n'est montrée comme réelle.

## Pour compléter

Activer N8n dans cette conversation, puis :

1. relire les statuts et les dernières exécutions ;
2. ouvrir WC2026_3 ;
3. capturer les nœuds en masquant les secrets.
