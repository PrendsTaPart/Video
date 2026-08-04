# Tutoriel — Retrouver l'historique de ses livraisons (Contrôle à réception) FoodEatUp

Module **HACCP**, sous-catégorie proposée « Contrôle à réception — historique » (⚠️ nom exact
du sous-dossier Drive à confirmer avec Michael, pas d'accès Drive depuis cet environnement).

Rush fourni : `assets/screen.mp4` (1920×828, 25 fps, 23,44 s) — page Historique HACCP.
Carte d'ouverture fournie : `assets/intro.jpg` (« RETROUVER MES LIVRAISONS HISTORIQUE »).
Carte de fin : `assets/outro.jpg` — identique (même md5) à celle déjà utilisée sur toute la
série (CTA « Passez à la restauration intelligente avec FoodEatUp »), réutilisée telle quelle.

## Déroulé du rush (analyse frame-by-frame, 1 img/s)

| t | Écran |
|---:|---|
| 0,2–1,4 s | Page « historique haccp », en-tête (Réception, Traçabilité, Production, Hygiène, Documents, Historique) |
| 2–4 s | Scroll vers les 7 cartes de modules HACCP (Températures, Traçabilité, Plan de nettoyage, Production, **Contrôle à réception** — 4 contrôles, Checklist Hygiène, Étiqueteuse) |
| 5–6 s | Hover puis clic sur la carte **Contrôle à réception** |
| 6–9 s | Liste filtrée : « Historique > Contrôle à réception », compteurs 4 Total / 4 Conforme(s) / 0 Non conforme(s), barre de filtres (Recherche, Date début, Date fin, État, bouton Filtrer), 4 cartes (Fournisseur, Date, Heure, badge Conforme, boutons Supprimer/Modifier) |
| 10 s | Clic sur **Modifier** (2ᵉ carte, fournisseur « louay ») |
| 10–13 s | Modal « Modifier le contrôle » : Date de contrôle, Heure de contrôle, Référence BL, Fournisseur, Catégorie(s) (Fruits & Légumes, Viandes & Poissons, Produits Laitiers, Surgelés, Épicerie sèche, Boissons, Plats préparés, Autres) |
| 14–17 s | Toggle **État de livraison** : clic sur « Non conforme » → apparition de la checklist « Type(s) de non-conformité » (horaire, date, prix, quantité, véhicule, emballage, autre), puis retour sur « Conforme » |
| 18–19 s | Scroll : Température produits frais (°C), Commentaires (« RAS »), boutons Annuler / Enregistrer — fermeture du modal (X) sans enregistrer |
| 20 s | Retour à la liste, clic sur **Supprimer** (2ᵉ carte) |
| 20–23 s | Modal de confirmation « Êtes-vous sûr(e) de vouloir supprimer cette carte ? Cette action est irréversible » → clic sur **Annuler** (rien n'est supprimé) |

## Outil MCP FoodEatUp correspondant

`mcp__FoodEatUp__create_haccp_reception(establishment_id, date_controle, heure_controle,
etat_livraison, fournisseur_nom?, reference_bl?, non_conformites?, temperature_produits_frais?,
commentaires?)` — couvre exactement les champs visibles dans le modal « Modifier le contrôle »
(seul un `update_haccp_reception` manque pour coller 1:1 à l'action « modifier » montrée à
l'écran ; `create_haccp_reception` permet en revanche d'enregistrer un nouveau contrôle à
réception directement depuis Claude, même bénéfice pour le restaurateur — mêmes champs).
`list_haccp_reception(establishment_id)` existe aussi (lecture seule, pas de `claudePrompt`
dédié pour la simple consultation, cohérent avec la règle déjà appliquée sur `regler-ses-unites`).

Séquence Claude à ajouter en fin de vidéo (avant la carte de fin), template partagé
`videos/_shared/claude_prompt_sequence.py`, réutilisé tel quel.

**Prompt (identique côté vidéo et côté fiche Lovable `claudePrompt`) :**

> Enregistre un contrôle à réception pour mon établissement FoodEatUp (ID [ID établissement]) :
> fournisseur [nom du fournisseur], livraison du [date] à [heure], état [conforme ou non conforme].

Réplique assistant (`CLAUDE_RESPONSE`) : « Bien sûr ! J'enregistre ce contrôle de réception
pour votre établissement… »

## Voix off proposée (9 lignes, voix Adam FR `TGAegA0zNRi8I6nUdq3i`) — **BROUILLON, PAS ENCORE VALIDÉ**

| # | Texte | Ancrage prévu |
|---|---|---|
| N0 | Retrouver l'historique de vos livraisons sur FoodEatUp ? Toutes vos réceptions sont regroupées en un seul endroit. | carte d'intro |
| N1 | Depuis l'onglet Historique, cliquez sur Contrôle à réception. | clic carte module |
| N2 | Filtrez par date, par fournisseur ou par état : conforme ou non conforme. | liste + barre de filtres |
| N3 | Une erreur sur une fiche ? Cliquez sur Modifier pour la corriger à tout moment. | clic Modifier |
| N4 | Date, fournisseur, catégories, température : tout reste ajustable, y compris le motif d'une non-conformité. | modal + toggle non conforme |
| N5 | Besoin de supprimer une fiche ? Une confirmation vous protège de toute erreur. | clic Supprimer + modal confirmation |
| N6 | Vous pouvez aussi enregistrer un contrôle à réception depuis Claude : copiez ce prompt, remplacez les crochets. | étage 1+2 (reveal + copié) |
| N7 | Collez-le dans la conversation : votre contrôle est enregistré en quelques secondes. | étage 3 (mockup chatbot) |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | carte de fin (CTA) |

N8 est la ligne CTA générique déjà utilisée sur toute la série — candidate à copier telle
quelle depuis un tuto précédent (`.mp3` réutilisable) une fois le script validé, comme documenté
dans `FOODEATUP-TUTORIELS-WORKFLOW.md` (règle « N8 est réutilisable tel quel »).

## Statut

**Script en attente de validation de Michael — aucune VO ElevenLabs générée, aucun montage
lancé** (règle « STOP obligatoire » de `FOODEATUP-TUTORIELS-WORKFLOW.md`, étape 3).
