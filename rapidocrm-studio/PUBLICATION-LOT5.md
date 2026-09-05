# Lot Contrat, CRM & Marketing, Campagne — état au 04/09

Dix enregistrements confiés dans la nuit. Deux sont publiés de bout en bout, un
est écarté, sept sont écrits ou analysés et attendent une facture ElevenLabs.

| Module | Tutoriel | Analyse | Fiche | Script | Voix | Rendu | Biblio | YouTube | Page |
|---|---|---|---|---|---|---|---|---|---|
| 04-contrat | Page de couverture d'un contrat | ✅ | ✅ | 149 mots | ✅ | 53 s | ✅ | ✅ | ✅ **en ligne** |
| 04-contrat | Historique des contrats | ✅ | ✅ | 148 mots | ✅ | 50 s | ✅ | ✅ | ✅ **en ligne** |
| 06-crm-marketing | Importer un fichier Excel entreprise | ✅ | ✅ | 141 mots | ⛔ | — | — | — | — |
| 06-crm-marketing | Prospecter une entreprise par SIRET | ✅ | ⏳ | ⏳ | ⛔ | — | — | — | — |
| 06-crm-marketing | Ajouter/Modifier un employé | ✅ | ⏳ | ⏳ | ⛔ | — | — | — | — |
| 06-crm-marketing | Importer un fichier Excel contact | ✅ | ⏳ | ⏳ | ⛔ | — | — | — | — |
| 06-crm-marketing | Ajouter/Modifier un contact | ⛔ | — | — | — | — | — | — | — |
| 12-campagne | Créer une campagne email | ✅ | ⏳ | ⏳ | ⛔ | — | — | — | — |
| 12-campagne | Créer une campagne SMS | ✅ | ⏳ | ⏳ | ⛔ | — | — | — | — |
| 12-campagne | Créer une campagne newsletters | ✅ | ⏳ | ⏳ | ⛔ | — | — | — | — |

## Les deux tutoriels en ligne

    Page de couverture d'un contrat
      page   https://tutoriel.rapido-crm.com/tutoriel/04-ajouter-une-page-de-couverture-a-un-contrat
      vidéo  https://www.youtube.com/watch?v=RZc1MmMjklE
      short  https://www.youtube.com/watch?v=FqNjQV0r_JM

    Historique des contrats
      page   https://tutoriel.rapido-crm.com/tutoriel/04-historique-des-templates-de-contrat
      vidéo  https://www.youtube.com/watch?v=IOR9fPAAHtU
      short  https://www.youtube.com/watch?v=obg6ZYbLdeo

Les deux pages sont remplies entièrement : accroche, « comment ça marche »,
étapes, prérequis, astuces, cas d'usage, prompt Claude et son outil MCP,
transcription et chapitres, SEO, vignette, vidéo, vidéo verticale, lien YouTube,
et les instructions de l'agent de la page.

## Ce qui bloque

**Le compte ElevenLabs a un impayé.** Vérifié à 08 h 13, la synthèse échoue
encore :

> Your subscription has a failed or incomplete payment. Complete the latest
> invoice to continue usage.

Les seize blocs des deux tutoriels Contrat sont passés juste avant la coupure —
c'est pour cela qu'eux seuls sont montés. Les sept autres s'arrêtent là : sans
voix, pas de rendu, donc pas de publication. Il n'y a rien à corriger dans le
code ; il faut régler la facture.

**Le connecteur YouTube, lui, n'était pas fermé.** Les cinq chaînes du compte
répondent. La chaîne active était RapidoCMS, pas RapidoCRM : `switch_channel`
vers `UCXyptH13bJF7AVr2TZJWA-Q` a suffi. Les quatre pages Comptabilité qui
attendaient un lien YouTube peuvent donc partir de la même façon.

**Un enregistrement est inexploitable.** « Ajouter/Modifier un contact » ne
montre aucun formulaire de contact : la liste des clients défile, puis une page
Entreprise vide, puis « S'il vous plaît, attendez… » jusqu'à la fin des 23
secondes. Il est à refaire — le reste du module n'en dépend pas.

## Deux choses vues à l'écran qui méritent un regard

**L'éditeur de la campagne email affiche un avertissement technique** par-dessus
le texte du message : « This ckeditor 4.22.1 (full) version is not secure,
consider upgrading to the latest one, 4.25.2-lts ». Il est visible par
l'utilisateur, pas seulement par un développeur. La zone est déclarée en zone
sensible et sera floutée au montage, mais l'avertissement reste dans le produit.

**Deux enregistrements montrent la barre du navigateur** avec `127.0.0.1:8000`
— prospection par SIRET et campagne newsletter. Le montage les replace dans un
mockup de navigateur : on verra donc un navigateur dans un navigateur. Sans
conséquence sur le fond, mais moins propre que les captures plein écran des
autres tutoriels.

## Deux sessions sur la même branche

Une seconde session Claude a travaillé `claude/rapidocrm-video-pipeline-t02imi`
en parallèle toute la nuit, sur le module Comptabilité et sur seize
enregistrements de CRM & Marketing. Nous avons corrigé les mêmes défauts chacun
de notre côté avant de nous en apercevoir : les noms de champs de
`configurer_agent_tutoriel`, le logo de fin absent du dépôt, les seuils calibrés
sur l'ancien format long. La fusion retient sa version sur les quatre fichiers
en conflit. Aucun numéro de tutoriel ne se chevauche.

À trancher : faire travailler les deux sessions sur des branches séparées, ou
sur des modules disjoints.
