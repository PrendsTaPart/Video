# Tutoriel — Ajouter ses fournisseurs FoodEatUp

Dossier Drive « Configuration de ces fournisseurs ». Durée livrée : **39,8 s** —
H.264 High/yuv420p, AAC 48 kHz stéréo, faststart. Audio : true peak **-6,9 dBFS**.
Decode 0 erreur, moov avant mdat (faststart confirmé).

## Voix off (9 lignes)

| # | Texte | Durée | Ancrage |
|---|---|---:|---|
| N0 | Vos fournisseurs sur FoodEatUp : la base de vos commandes et de vos factures. | 4,00 s | carte d'intro |
| N1 | Cliquez sur Ajouter un fournisseur pour créer sa fiche. | 2,95 s | clic Ajouter un fournisseur |
| N2 | Renseignez son nom et son adresse complète. | 2,27 s | nom + adresse |
| N3 | Ajoutez son email et son téléphone, utiles pour vos commandes par email ou SMS. | 4,91 s | email + téléphone |
| N4 | Choisissez ses catégories de produits, la livraison et sa fiabilité. | 3,84 s | catégorie, livraison, étoiles |
| N5 | Cliquez sur Enregistrer : votre fournisseur est prêt. | 2,93 s | clic Enregistrer → succès |
| N6 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | 4,41 s | **étage 1+2** (réutilisé) |
| N7 | Collez-le dans la conversation : votre fournisseur est créé en quelques secondes. | 4,13 s | **étage 3** |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (CTA, réutilisé) |

N6/N8 réutilisés tels quels depuis `foodeatup-tva-tuto/vo/` (même voix, texte générique
qui s'applique à n'importe quel tutoriel — zéro crédit ElevenLabs dépensé sur ces deux
lignes). **Point de vigilance repéré et corrigé pendant cette passe** : une première
copie de N7 avait été faite par erreur depuis `foodeatup-tva-tuto` ("...votre taux de
TVA est créé...", contenu factuellement faux pour ce tutoriel) — repéré avant livraison,
régénéré avec un texte propre au fournisseur, rebuild complet, vérifié à l'image
(t=29,5 s) que le prompt et la réponse affichés disent bien "fournisseur", pas "TVA".
Leçon : les lignes N6/N8 sont assez génériques pour être copiées telles quelles d'une
vidéo à l'autre ; N7 ne l'est jamais (il nomme l'objet créé) et doit toujours être
régénéré pour chaque nouveau tutoriel.

## Découpage

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 3,00 s | AJOUTER SES FOURNISSEURS FOODEATUP |
| A | 0,20 → 1,60 | 2,20 s | liste des fournisseurs, état vide |
| B | 1,60 → 1,85 | 0,90 s | **zoom-punch** sur Ajouter un fournisseur (1621, 346) |
| C | 2,00 → 20,00 | 5,50 s | nom « Délice Holding » + adresse « berges de lac tunis tunisia » |
| D | 20,00 → 44,00 | 5,00 s | email « delice@contact.tn » + téléphone « +216 22 36 54 78 » |
| E | 44,00 → 54,00 | 4,50 s | catégorie Poissons, livraison cochée, fiabilité 4 étoiles |
| F | 55,60 → 55,85 | 0,90 s | **zoom-punch** sur Enregistrer (1034, 735) |
| G | 56,00 → 60,30 | 3,80 s | toast « Fournisseur ajouté avec succès » + carte fournisseur |
| claude1 | carte générée | 3,00 s | reveal — prompt en gros, fond crème |
| claude2 | carte générée | 2,30 s | confirmation « Copié dans le presse-papiers ! » |
| claude3 | carte générée | 5,30 s | mockup chatbot Claude |
| outro | carte | 6,20 s | CTA |

Coordonnées des boutons mesurées par seuillage colorimétrique sur les frames réelles
(script Python, pas à l'œil) — voir `build.py`.

## Séquence Claude — module partagé

`mcp__FoodEatUp__create_supplier(establishment_id, name, adresse, ville, pays,
code_postal, email, tel, website, type, livraison, reliability, status)` existe — schéma
vérifié avant rédaction du prompt, les champs correspondent à ce que montre le rush
(nom, adresse, email, tél, catégorie de produits, livraison) :

> Crée le fournisseur [nom] à [adresse], email [email], tél [téléphone], type
> [catégorie de produits], livraison [oui/non], pour mon établissement FoodEatUp
> (ID [ID établissement]).

Même texte côté fiche Lovable (`claudePrompt`).

## Astuce du chef (Lovable) — capacités non montrées dans ce rush

Michael a précisé, en déposant les rushs, que les fournisseurs servent aussi à :
- les affilier à des produits, pour passer des **commandes fournisseurs par email ou
  SMS directement depuis la liste de courses** ;
- **affilier ses factures par fournisseur** (suivi comptable) ;
- **ajouter une facture fournisseur via l'OCR (ou directement depuis Claude)** pour
  mettre à jour ses produits automatiquement.

Ces fonctionnalités ne sont pas visibles dans ce rush (qui montre uniquement la
création d'une fiche fournisseur) : elles sont documentées dans le champ `chefTip` de la
fiche Lovable plutôt qu'inventées dans la vidéo, pour rester fidèle à ce qui est montré
à l'écran.

## Animations

Mêmes principes que toute la série : Ken Burns sur les cartes, xfade (0,28 s), bandeaux
d'étape, encadré orange pulsant sur les 2 clics. Pas de clip avatar dans ce dossier.

## Statut publication

Vidéo à livrer à Michael pour validation (règle du 2026-08-02) — pas de publication
RapidoCMS/LinkedIn/Lovable avant retour explicite. **Point à vérifier avant publication** :
régénérer N7 avec un texte propre au fournisseur (voir note ci-dessus).
