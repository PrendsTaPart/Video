# Test de routage — gestion-marques / gestionnaire-marques

> Entrées à ajouter dans `tests/test-routage.md` du dépôt plugin
> (`PrendsTaPart/Plugin-Claude-MCP-BraindCode-`). Format : phrase utilisateur →
> skill/agent attendu. Adapter au gabarit exact du fichier cible si différent.

## Doivent router vers `gestion-marques` (+ agent `gestionnaire-marques`)

| # | Entrée utilisateur | Routage attendu |
|---|---|---|
| R1 | « Crée la marque FoodEatUp » | gestion-marques → create_brand |
| R2 | « Ajoute ce logo transparent à ma marque » | gestion-marques → upload_file_tool + add_asset |
| R3 | « Change les couleurs de la marque BraindCode » | gestion-marques → edit_brand |
| R4 | « Supprime la marque PronoClip » | gestion-marques → delete_brand (garde-destructif) |
| R5 | « Je gère plusieurs enseignes, comment on organise ça ? » | gestion-marques (multi-marques) |
| R6 | « C'est quoi la charte de RapidoSoftware ? » | gestion-marques → get_brand |
| R7 | « Mets à jour l'asset logo de FoodEatUp » | gestion-marques → remove_asset + add_asset |

## Doivent déclencher le garde-fou `gestionnaire-marques` (marque cible obligatoire)

| # | Entrée utilisateur | Comportement attendu |
|---|---|---|
| G1 | « Génère le post d'annonce » (≥ 2 marques) | l'agent DEMANDE la marque cible avant de générer |
| G2 | « Fais-moi un visuel » (nouveau projet sans marque) | propose de créer la marque manquante |
| G3 | « Publie ça sur nos réseaux » | vérifie couleurs/ton/logo officiel avant publication |

## Ne doivent PAS router vers gestion-marques (contre-exemples)

| # | Entrée utilisateur | Routage attendu (autre) |
|---|---|---|
| N1 | « Planifie mes posts du mois » | calendrier-editorial |
| N2 | « Écris un article SEO » | generation-article-blog |
| N3 | « Relance mes factures impayées » | invoice-chase |
| N4 | « Uploade cette vidéo dans ma bibliothèque » | (upload simple, pas de gestion de marque) |

## Points de vigilance du routeur
- « logo », « charte », « ma marque », « multi-enseignes », « couleurs de la marque » →
  signaux forts vers `gestion-marques`.
- Toute demande de **génération/publication de contenu** doit passer le **check marque cible**
  de l'agent `gestionnaire-marques` (même si le skill de contenu est un autre).
