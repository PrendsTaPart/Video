# Vidéo 15 · Mon IA gère mes clients ? (RapidoCRM × Claude)

Format vertical 1080 × 1920, 47 s. Voix Noé (ElevenLabs). **Rien n'a été publié ni envoyé. Lecture seule sur le CRM.**

## Voix off (ton script, sans modification)

> Aujourd'hui, je vais te montrer comment je gère mes clients.
>
> Parce qu'entre les prospects, les rendez-vous, les devis, les factures et les relances… j'avais presque besoin d'un deuxième cerveau !
>
> Alors j'ai développé RapidoCRM. Et je l'ai connecté à Claude grâce à mon MCP.
>
> Maintenant, je peux simplement lui demander : quels clients je dois rappeler ? Quels devis attendent une réponse ? Quelles factures dois-je suivre ?
>
> Claude consulte mon CRM, analyse les informations et me prépare les prochaines actions.
>
> Et si je veux prospecter, organiser mes rendez-vous ou préparer mes relances, il peut aussi m'aider.
>
> Avant, je travaillais pour mon CRM. Maintenant, mon CRM travaille avec mon IA.
>
> Et toi, tu gères encore tes clients à la main ?

La punchline est dite en entier et affichée à l'écran.

## La démonstration (MCP RapidoCRM, lecture seule, 26/10)

Les entrées de test (« [TEST-QA] », « ZZ… », « TEST », « sad », « hello ») sont **exclues de tous les chiffres**. Les noms des clients sont remplacés par « Client A » et « Client B ».

| Scène | Appel | Ce qui est réel |
|---|---|---|
| A · le matin | `get_dashboard_kpis`, `get_stats_pipeline_global`, `get_today_schedule` | 70 prospects (69 nouveaux, 1 en qualification), aucun rendez-vous cette semaine |
| B · clients à suivre | `list_devis`, `list_factures` | **1 seul devis réel en attente** (Client A, 1 200 €, depuis le 21/07), distinct des devis **expirés**, qui sont tous des tests. 2 factures réelles en attente (Client B 1 428 €, Client A 600 €) |
| C · relances | aucun appel d'envoi | Deux **brouillons** à l'écran avec les montants et dates vérifiés : « Rien n'est envoyé sans mon accord » |
| D · prospection | `list_segments` | 7 segments métiers ; écrans « Prospecter » et « Résultat ». **Aucune prospection lancée** |
| E · pilotage | synthèse | Priorité 1 : relancer Client A (devis et facture) ; le planning de la semaine est vide |

Ce qui n'est **pas** montré :
- le chiffre d'affaires du tableau de bord (4 913 €), qui inclut des factures de test ;
- les statistiques de campagnes, toutes à zéro ;
- le taux de conversion par canal.

Les écrans du logiciel viennent de la bibliothèque de marque du MCP Formation : écrans réels et maquettes Figma du logiciel.

## Continuité

- **Vidéo 14** : mes agents testent mes logiciels.
- **Vidéo 15** : j'utilise l'un d'eux, RapidoCRM, pour piloter mes clients.
- **Vidéo 17** : le marketing (RapidoCMS) qui alimente ce CRM.
