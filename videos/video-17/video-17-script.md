# Vidéo 17 · Mon IA transforme mes posts en clients ! (inbound RapidoCMS → RapidoCRM)

Format vertical 1080 × 1920, 51 s. Voix Noé (ElevenLabs). Logo Claude et CTA à la fin. **Rien n'a été publié, créé ni envoyé : lecture seule.**

## Voix off

> Aujourd'hui, je vais te montrer comment j'ai construit ma stratégie pour attirer de nouveaux clients.
>
> Parce que publier sur les réseaux sociaux, c'est bien… Mais si personne ne devient client, à quoi ça sert ?
>
> Alors, j'ai connecté RapidoCMS et RapidoCRM à Claude grâce à mes MCP.
>
> RapidoCMS m'aide à créer les contenus, les visuels, et à organiser les publications.
>
> Attention : un like ne devient pas un client. C'est le formulaire de démo, avec le consentement, qui crée le contact dans RapidoCRM. Ensuite, je suis ses demandes, ses rendez-vous et ses opportunités.
>
> Mais le plus intéressant, c'est la boucle ! Claude peut analyser les performances, identifier ce qui fonctionne, et préparer la prochaine campagne.
>
> Avant, je publiais pour être visible. Maintenant, je construis un système pour transformer mon contenu en clients. Et tout ça, avec mes propres logiciels et mes agents IA !
>
> Si tu veux mon tunnel complet, écris TUNNEL en commentaire !

**Changements par rapport à ton script :**
- « j'ai **automatisé** ma stratégie » devient « j'ai **construit** », car aucun workflow n'a encore tourné ;
- ajout de la phrase sur le like et le formulaire, qui est le passage clé RapidoCMS → RapidoCRM ;
- ajout du CTA « TUNNEL », comme tu l'as demandé.

## La méthode suivie : FoodEatUp Formation

C'est le parcours **Marketing, mission G3 « La machine inbound, étape par étape »** :
1. Le contenu est rattaché à une campagne dans RapidoCMS (brouillons, planification, statistiques).
2. Un lead magnet résout un problème précis.
3. Chaque formulaire crée ou met à jour le contact **avec son consentement et sa source** dans RapidoCRM.
4. Le nurturing s'arrête dès que la personne répond ou prend rendez-vous.
5. Les contacts les plus chauds reçoivent une proposition de rendez-vous.
6. On mesure : visiteurs, téléchargements, contacts, rendez-vous, clients signés.
7. Garde-fous : activer une séquence est une décision humaine, et le statut « publié » d'un post ne veut pas dire qu'il a été diffusé.

**Répartition cible 55 % TOFU, 30 % MOFU, 10 % BOFU, 5 % fidélité** : confirmée par `get_editorial_gaps` et le brief éditorial. La mission G2 parle d'un départ à 60/30/10 ; j'ai retenu la cible du brief, plus récente.

## Disponible, configuré ou envisagé (26/10)

| Élément | État réel |
|---|---|
| MCP RapidoCMS : brouillons, campagnes, programmation, statistiques | ✅ disponible ; 85 posts programmés du 26/10 au 09/11 |
| Formulaires RapidoCRM (démo, aimants food cost et HACCP, rappel) | ✅ créés, **0 vue et 0 clic** à ce jour |
| Liaison post → contact | ✅ par le formulaire (lien du formulaire dans le post ou la page) ; **pas automatique depuis un like** |
| Workflows RapidoCRM | 3 actifs (onboarding J0/J7/J14, relance facture J+7, relance devis J+3), **0 exécution** ; « Bienvenue lead aimant » et « Relance devis après démo » **en brouillon** |
| Blocs du tunnel dans l'Academy (`list_tunnels`) | décrits ; `etat_workflow` vide partout |
| Calendrier de l'Academy | 0 publication prévue sur 2 semaines alors que RapidoCMS en a 85 : **les deux calendriers ne sont pas synchronisés** |
| Boucle d'analyse automatique par Claude | envisagée, non configurée |

**Le scénario « ruptures de stock » est une démonstration simulée**, signalée à l'écran. Le carrousel n'a pas été créé dans RapidoCMS, et aucun contact réel n'apparaît. **Aucun chiffre de conversion n'est cité.**

## Écart avec le brief

- **OpenAI.** Je n'ai trouvé aucune intégration OpenAI vérifiable dans les MCP consultés. Claude est montré comme orchestrateur.
- **Vidéo 16.** Elle n'existe ni dans le dépôt ni dans le projet Lovable.
