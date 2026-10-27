# Vidéo 19 · Mon client pilote son site avec l'IA ! (Villa Beach)

Format vertical 1080 × 1920, 68 s. Voix Noé (ElevenLabs, eleven_v4). **Aucune modification du site, aucun événement publié, aucun message envoyé.**

## Voix off

> Aujourd'hui, je vais te montrer comment j'ai créé le site Internet d'un de mes clients avec Lovable.
>
> Voici Villa Beach : un restaurant festif, lounge et club, à Lisses.
>
> Mais je ne voulais pas simplement lui créer un beau site. Je voulais un site connecté à ses outils métier.
>
> Alors, sa carte est reliée à FoodEatUp, et ses demandes peuvent partir dans RapidoCRM. Pour Caroline, mon agent vocal, la place est prête… mais l'intégration reste à finaliser.
>
> Mais surtout, j'ai développé un MCP spécialement pour Villa Beach. Et là, ça change tout !
>
> Mon client peut demander à Claude ou ChatGPT de modifier ses pages, préparer ses événements, gérer ses formulaires ou consulter ses demandes.
>
> L'IA utilise les outils du site avec un compte administrateur : chaque appel est journalisé, et chaque suppression demande une confirmation.
>
> Et ses formulaires peuvent alimenter son tunnel commercial.
>
> Avant, mon client devait me demander de modifier son site. Maintenant, il peut simplement demander à son IA ! Et pour moi, c'est ça, la nouvelle génération de sites Internet.

## Changements par rapport à ton script

- « je l'ai relié à mon écosystème FoodEatUp » devient « sa carte est reliée à FoodEatUp, et ses demandes peuvent partir dans RapidoCRM » : ce sont les deux liaisons présentes dans le code.
- Caroline : « l'intégration reste à finaliser » (numéro vide dans `src/lib/contact-info.ts`, emplacement `caroline-widget` vide).
- « avec les autorisations nécessaires » devient concret : compte administrateur, journal `mcp_audit`, `confirmer=true` pour toute suppression.

## Vérifications

### Le MCP Villa Beach

Il n'est **pas branché** dans cette session de Claude Code : je n'ai donc pu appeler aucun outil, même en lecture. L'audit vient du code du projet Lovable (commit `a3654c4` du 16/10 ; le dépôt GitHub `villa-beach-luxe` s'arrête au 24/09 et n'a pas encore ces outils).

Il y a **deux serveurs** :

1. **`/mcp` « villa-beach-admin » 1.1.0** (OAuth Supabase, comptes administrateurs). Il contient les outils de ton brief, avec ces noms exacts : `voir_pages_site`, `ajouter_page_site`, `modifier_page_site`, `supprimer_page_site`, `voir_charte_graphique`, `modifier_charte_graphique`, `voir_navbar`, `configurer_navbar`, diaporamas, sliders, projets, `voir_evenements` / `ajouter_evenement` / `modifier_evenement` / `supprimer_evenement`, semaines, pages par occasion, avis, réservations, `voir_demandes`, contacts, photos, `voir_reglages_site`, `voir_connecteurs`, commandes, mur social (dont la synchronisation RapidoCMS), et les formulaires : `voir_formulaires`, `ajouter_formulaire`, `modifier_formulaire`, `configurer_champs_formulaire`, `configurer_enregistrement_formulaire`, `configurer_actions_formulaire`, `configurer_reservation_formulaire`, `tester_disponibilites_formulaire`, `supprimer_formulaire`, `voir_connexions_mcp`.
   - Chaque appel est journalisé dans `mcp_audit` (préfixe `admin:`).
   - Tout outil marqué destructif exige `confirmer=true`.
   - `ajouter_evenement` crée un événement **désactivé** sauf `is_published=true` ; `ajouter_formulaire` crée un formulaire **désactivé**.
2. **`/api/public/site-mcp` « villa-beach-site »** (jeton Bearer, 120 appels/min). Il contient 12 outils : `list_leads`, `get_lead`, `update_lead_status`, `add_lead_note`, `list_events`, `create_event` (publie par défaut), `update_event`, `publish_social_post`, `list_pending_photos`, `moderate_photo`, `update_persona_offer`, `get_stats`.

### La démonstration centrale

C'est une **démonstration** : les appels sont préparés d'après les schémas réels, mais aucun n'a été envoyé (pas d'accès administrateur, et pas de modification de la production). L'événement « Soirée du vendredi » est un exemple affiché en brouillon. La publication finale (`modifier_evenement(is_published: true)`) est montrée comme « après accord ». Les captures du formulaire sont celles du vrai formulaire Anniversaire.

### Le blog

Il n'y a **pas de module de blog**. Un article passerait par une page éditoriale (`ajouter_page_site`), comme l'indique la vidéo.

### FoodEatUp

`/carte` appelle `getMenu` : un cache de 10 min (`menu_cache`), puis le connecteur FoodEatUp (`list_dishes`, `list_categories`, établissement 46). La carte s'affiche bien sur le site. Je n'ai pas pu comparer avec FoodEatUp : mon compte voit les établissements 53 et 58, pas le 46. L'état d'authentification du connecteur (erreurs signalées) n'a pas pu être relu : `voir_connexions_mcp` est réservé à l'administrateur.

Dans le code, les réservations (`reservation_availability`, `create_reservation`) et les commandes passent aussi par FoodEatUp.

### RapidoCRM

`crm.server.ts` est codé ainsi :
1. dédoublonnage par email, puis par téléphone ;
2. création d'un contact, ou d'une entreprise pour les pages Entreprises et Formations ;
3. opportunité dans le pipeline de la page, à l'étape « Nouveau » ;
4. note avec le détail de la demande ;
5. tâche de relance à J+1.

En cas d'échec, la demande reste dans la file `crm_sync_queue`. Ce circuit **n'a pas été vérifié en production**.

### Caroline

Ce qui est en place : le bouton « Parler à Caroline » dans l'assistante du site, les mentions dans les emails, et l'emplacement `caroline-widget`. Ce qui manque : `carolineTel` et `carolineLabel` sont vides. Aucun appel n'a pu être démontré, d'où « à finaliser ».

### Formulaires et pages

Les pages par occasion existent : anniversaire, mariage, entreprises, formations et salles, restaurant, soirées, dimanche, mercredi, afterwork, ciné-dîner, fumoir. La « location de salle » est couverte par la page formations et salles. Il n'y a pas de page dédiée « repas de groupe ».

## Données personnelles

Aucune demande ni aucun contact n'a été lu ou affiché. Les captures viennent des pages publiques. J'ai évité la page Agenda, qui affiche une entrée de test (« eaazeaz ») à supprimer côté client.
