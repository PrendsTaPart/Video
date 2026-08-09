# FoodEatUp — 30 scripts HeyGen « l'avatar présente le logiciel »

Généré le 2026-08-09 à partir de l'inventaire réel des assets disponibles :
- **89 vidéos logiciel** (`videos/foodeatup-*-tuto/assets/screen.mp4`) — rushes déjà tournés,
  contenu vérifié dans le `SCRIPT.md` de chaque projet.
- **17 plans Higgsfield** (`hero-video/assets/video/`) + **5 boucles d'ambiance**
  (`studio-video/assets/brand/loops/`) — bibliothèque existante, réutilisée conformément à
  la règle du dépôt (`CLAUDE.md` : ne pas générer de nouveaux plans Higgsfield).
- Structure validée sur la **vidéo 1 (fidélité)** : `v01-fidelite/`.

---

## ⚙️ Réglages HeyGen — À FAIRE UNE FOIS, IDENTIQUES POUR LES 30

**⚠️ L'erreur à ne pas refaire** (rencontrée 2 fois sur la vidéo 1) : ne PAS partir de la
galerie de **templates** HeyGen. Un template insère automatiquement une scène graphique
générique (fond bleu, photo stock), coupe l'avatar au bout de ~3 s et incruste logo +
sous-titres dans l'image — inutilisable, tout notre habillage est déjà fait de notre côté.

Créer chaque clip en **avatar seul / plan unique** :

```
Avatar        : Mika  (avatar_id bd56633302aa4790a8d526fe2ee6b63f — déclinaison verticale)
Format        : vertical 9:16, 1080 × 1920
Scène         : UNE seule scène, aucun template, aucun B-roll, aucune carte de fin
Fond          : cuisine professionnelle floutée (ou fond neutre — je compense au montage)
Voix          : française masculine, ton posé et direct, débit naturel, PAS de ton commercial
Sous-titres   : DÉSACTIVÉS  (ajoutés au montage)
Logo / texte  : AUCUN incrusté  (notre logo est déjà dans le hook et la punchline)
Durée cible   : 7 à 9 s — l'avatar parle du début à la fin, aucune coupe
```

## 🎬 Structure identique pour les 30 (validée sur la vidéo 1)

```
0 – 3 s      HOOK         Carton chiffré (déjà produit — voir ../motion/)
3 – 11 s     PROBLÈME     Plan Higgsfield, 8 s, ambiance seule, aucune voix
11 – 25 s    DÉMO         Logiciel EN BAS (pleine largeur, non recadré)
                          + AVATAR HeyGen PAR-DESSUS EN HAUT qui le présente (7-8 s)
                          puis l'avatar s'efface, le logiciel finit seul
25 – 30.2 s  PUNCHLINE    Carton logo + voix off (déjà produit — voir ../motion/)
```

**Le script HeyGen ci-dessous = uniquement la réplique de l'avatar du bloc DÉMO.**
Hook et punchline sont déjà rendus et ne changent pas d'une vidéo à l'autre.

## ✍️ La formule d'écriture (identique sur les 30)

3 temps, ~25-35 mots : **recadrage** (une phrase qui déplace le problème) → **mécanisme**
(ce que le logiciel fait, verbe actif) → **résultat concret** (un chiffre, une action, un
moment). Jamais d'adjectif marketing. Voir `SCRIPT.md` pour le détail de la méthode.

---

# LES 30 SCRIPTS

---

## MODULE — CONFIGURATION & CARTE

### 01 · Saisir ses ingrédients
- **Hook** : *Ton food cost ? « À peu près 30 %. »*
- **Higgsfield** : `hero-video/assets/video/hero-directeur-sept-onglets.mp4` *(réemploi)*
- **Logiciel** : `videos/foodeatup-ingredients-tuto/assets/screen.mp4` (104 s)

```
Chaque ingrédient saisi une fois, avec son prix fournisseur. C'est cette base qui calcule le coût de toutes vos recettes — et qui met à jour vos marges le jour où un tarif bouge.
```

### 02 · Monter ses recettes & fiches techniques
- **Hook** : *20 minutes par fiche technique. × 30 plats.*
- **Higgsfield** : `hero-video/assets/video/hero-chef-carnet-dlc.mp4` *(réemploi)*
- **Logiciel** : `videos/foodeatup-recettes-tuto/assets/screen.mp4` (93 s)

```
Une photo de votre plat, et l'IA remplit le nom, la description, la difficulté. Vous ajoutez vos ingrédients un par un : le coût de la recette se calcule à l'euro près, en direct.
```

### 03 · Ajouter ses fournisseurs
- **Hook** : *Trois fournisseurs. Trois carnets différents.*
- **Higgsfield** : `hero-video/assets/video/hero-directeur-sept-onglets.mp4` *(réemploi)*
- **Logiciel** : `videos/foodeatup-fournisseurs-tuto/assets/screen.mp4` (61 s)

```
Vos fournisseurs enregistrés une fois : coordonnées, conditions, catalogue. Ensuite chaque commande et chaque facture se rattachent toutes seules au bon compte, sans que vous cherchiez.
```

### 04 · Mes commandes — QR, site, agent vocal
- **Hook** : *4 canaux. 2 commandes perdues samedi.*
- **Higgsfield** : `hero-video/assets/video/hero-serveur-trois-tablettes.mp4` *(réemploi — le plan montre littéralement le jonglage multi-écrans)*
- **Logiciel** : `videos/foodeatup-mes-commandes-tuto/assets/screen.mp4` (56 s)

```
QR code de table, site web, agent vocal, livraison. Peu importe d'où vient la commande, elle tombe ici, dans le même ordre d'arrivée. Un seul écran à surveiller pendant le rush.
```

### 05 · Brancher son MCP sur Claude
- **Hook** : *Et si tu parlais à ton restaurant ?*
- **Higgsfield** : `hero-video/assets/video/hero-directeur-bureau-matin.mp4` *(réemploi)*
- **Logiciel** : `videos/foodeatup-mcp-tuto/assets/screen.mp4` (49 s)

```
Vous branchez FoodEatUp sur Claude une seule fois. Ensuite vous parlez à votre restaurant en langage normal — et il répond avec vos vraies données, pas avec des généralités.
```

---

## MODULE — ÉQUIPE & PLANNING

### 06 · Ajouter ses employés
- **Hook** : *Nouveau serveur. 3 jours pour lui donner ses accès.*
- **Higgsfield** : `hero-video/assets/video/hero-brigade-deux-langues.mp4` *(réemploi)*
- **Logiciel** : `videos/foodeatup-employes-tuto/assets/screen.mp4` (56 s)

```
Vous ajoutez l'employé, son rôle et ses permissions. Il reçoit ses accès dans la foulée, et il voit exactement ce qu'il doit voir. Ni plus, ni moins que son poste.
```

### 07 · Établir un contrat et son salaire
- **Hook** : *Les majorations dimanche, tu les calcules comment ?*
- **Higgsfield** : `hero-video/assets/video/hero-directeur-sept-onglets.mp4` *(réemploi)*
- **Logiciel** : `videos/foodeatup-contrat-tuto/assets/screen.mp4` (66 s)

```
Le contrat et le salaire se saisissent une fois. Les heures, les majorations de nuit et du dimanche se calculent ensuite toutes seules, jusqu'à l'export pour votre comptable.
```

### 08 · Imprimer son planning par poste
- **Hook** : *3 heures chaque dimanche. Pour un planning.*
- **Higgsfield** : `hero-video/assets/video/hero-salle-vide-matin.mp4` *(réemploi)*
- **Logiciel** : `videos/foodeatup-planning-poste-tuto/assets/screen.mp4` (83 s)

```
Vous construisez le planning par poste, vous publiez. Chacun reçoit le sien sur son téléphone. Et vous l'imprimez par poste pour l'afficher en cuisine, comme avant.
```

### 09 · Assigner les tâches sur le planning
- **Hook** : *« Je croyais que c'était lui qui devait le faire. »*
- **Higgsfield** : `hero-video/assets/video/hero-brigade-deux-langues.mp4` *(réemploi)*
- **Logiciel** : `videos/foodeatup-taches-tuto/assets/screen.mp4` (85 s)

```
Vous accrochez une tâche à un créneau du planning. L'employé la voit en arrivant, la coche quand c'est fait. Vous savez qui a fait quoi, et à quelle heure.
```

### 10 · Générer le QR code de pointage
- **Hook** : *Les heures de ton équipe. Sur un cahier.*
- **Higgsfield** : `hero-video/assets/video/hero-serveur-place-client.mp4` *(réemploi)*
- **Logiciel** : `videos/foodeatup-qrcode-pointage-tuto/assets/screen.mp4` (57 s)

```
Un QR code affiché à l'entrée. L'équipe pointe en arrivant, en pause, en partant. Les heures remontent seules dans le planning, puis dans la paie. Vous ne recopiez rien.
```

### 11 · Brancher Jarvis, l'assistant vocal
- **Hook** : *Sortir 3 kilos de saumon. Sans toucher un écran.*
- **Higgsfield** : `hero-video/assets/video/hero-brigade-deux-langues.mp4` *(réemploi — le plan EST la scène de la brigade qui parle en cuisine)*
- **Logiciel** : `videos/foodeatup-jarvis-tuto/assets/screen.mp4` (45 s)

```
Vous générez le jeton, et Jarvis écoute la cuisine. Vos équipes annoncent à voix haute ce qu'elles sortent — le stock se met à jour sans que personne pose son couteau.
```

---

## MODULE — HACCP & HYGIÈNE

### 12 · Déclarer ses équipements
- **Hook** : *Combien de frigos dans ton dossier HACCP ?*
- **Higgsfield** : `studio-video/assets/brand/loops/hero-loop-chambre-froide.mp4` *(boucle d'ambiance)*
- **Logiciel** : `videos/foodeatup-equipements-tuto/assets/screen.mp4` (42 s)

```
Vous déclarez vos frigos, congélateurs et chambres froides une fois, avec leurs seuils. Ensuite chaque relevé se rattache automatiquement au bon équipement, sans que vous choisissiez.
```

### 13 · Relever une température d'équipement
- **Hook** : *Relevé de 14h. Noté à 19h. De mémoire.*
- **Higgsfield** : `studio-video/assets/brand/loops/hero-loop-chambre-froide.mp4` *(boucle d'ambiance)*
- **Logiciel** : `videos/foodeatup-temperature-tuto/assets/screen.mp4` (20 s)

```
Vous ouvrez, vous saisissez, c'est tracé. Dix secondes par relevé. Et si la température sort du seuil, l'alerte part tout de suite au lieu d'être découverte au contrôle.
```

### 14 · Contrôler la température de ses productions
- **Hook** : *Ton plat est descendu en dessous de 63°C. Quand ?*
- **Higgsfield** : `hero-video/assets/video/hero-kds-mural.mp4` *(réemploi)*
- **Logiciel** : `videos/foodeatup-temperatures-tuto/assets/screen.mp4` (73 s)

```
Vous contrôlez la température de vos plats en sortie de production. Chaque relevé s'archive avec l'heure, le plat concerné et la personne qui l'a fait. C'est daté, c'est signé.
```

### 15 · Poser une DLC sur ses productions
- **Hook** : *Une date au marqueur. Effacée au deuxième lavage.*
- **Higgsfield** : `hero-video/assets/video/hero-chef-carnet-dlc.mp4` *(réemploi — le plan montre exactement ce geste)*
- **Logiciel** : `videos/foodeatup-dlc-tuto/assets/screen.mp4` (42 s)

```
La DLC est déjà calculée depuis votre fiche produit. Vous vérifiez, vous validez. Fini la date au marqueur qu'on ne relit plus la semaine suivante.
```

### 16 · Imprimer ses étiquettes
- **Hook** : *Les 14 allergènes. Écrits à la main.*
- **Higgsfield** : `hero-video/assets/video/hero-chef-scan-carton.mp4` *(réemploi)*
- **Logiciel** : `videos/foodeatup-etiquettes-tuto/assets/screen.mp4` (46 s)

```
Vente ou stockage, l'étiquette se génère depuis la fiche produit : dénomination, allergènes, DLC, code-barres. Vous imprimez, vous collez. Rien n'est réécrit à la main.
```

### 17 · Créer sa check-list hygiène
- **Hook** : *Contrôle surprise. 3 mois de relevés manquants.*
- **Higgsfield** : `hero-video/assets/video/hero-fermeture-lumieres.mp4` *(réemploi)*
- **Logiciel** : `videos/foodeatup-checklist-hygiene-tuto/assets/screen.mp4` (67 s)

```
Vous montez votre check-list une fois. L'équipe la coche depuis son téléphone, service après service. Le jour du contrôle, l'historique est déjà là — vous n'avez rien à reconstituer.
```

### 18 · Une photo, l'IA contrôle le nettoyage
- **Hook** : *« C'est propre. » Prouve-le.*
- **Higgsfield** : `hero-video/assets/video/hero-fermeture-lumieres.mp4` *(réemploi)*
- **Logiciel** : `videos/foodeatup-nettoyage-ia-tuto/assets/screen.mp4` (35 s)

```
Vous photographiez la zone, l'IA contrôle le nettoyage et pointe ce qui ne va pas. Le contrôle prend le temps d'une photo — et il reste dans le dossier.
```

### 19 · Exporter tout son classeur HACCP
- **Hook** : *L'inspecteur est là. Ton classeur aussi ?*
- **Higgsfield** : `hero-video/assets/video/hero-chef-carnet-dlc.mp4` *(réemploi)*
- **Logiciel** : `videos/foodeatup-haccp-export-tuto/assets/screen.mp4` (58 s)

```
Le classeur s'est rempli tout seul pendant que vous cuisiniez. Le jour du contrôle, vous sortez douze mois d'historique signé et horodaté. En trois secondes, pas en trois soirées.
```

---

## MODULE — STOCKVISION AI

### 20 · Tenir sa liste de courses
- **Hook** : *La commande du mardi. Faite de tête.*
- **Higgsfield** : `hero-video/assets/video/hero-cuisine-vide-matin.mp4` *(réemploi)*
- **Logiciel** : `videos/foodeatup-liste-courses-tuto/assets/screen.mp4` (60 s)

```
Votre liste de courses se remplit depuis vos stocks réels et vos productions prévues. Vous ajustez les quantités si besoin, et elle est prête à partir. Vous ne devinez plus.
```

### 21 · Commander et envoyer au fournisseur
- **Hook** : *Un appel. Un SMS. Un post-it. Une commande oubliée.*
- **Higgsfield** : `hero-video/assets/video/hero-directeur-bureau-matin.mp4` *(réemploi)*
- **Logiciel** : `videos/foodeatup-commande-fournisseur-tuto/assets/screen.mp4` (31 s)

```
Vous envoyez la liste au fournisseur directement depuis FoodEatUp. La commande part, la livraison est attendue, et la facture retombera toute seule sur le bon compte.
```

### 22 · Contrôler à réception
- **Hook** : *Carton reçu à 7h. Contrôlé… jamais.*
- **Higgsfield** : `hero-video/assets/video/hero-chef-scan-carton.mp4` *(réemploi — le plan EST le geste de scan à réception)*
- **Logiciel** : `videos/foodeatup-reception-tuto/assets/screen.mp4` (34 s)

```
À réception, vous contrôlez produit par produit : température, quantité, code-barres, DLC. Tout est tracé avant même que le carton parte en chambre froide.
```

### 23 · Lire ses mouvements de stock
- **Hook** : *Il te reste combien de saumon ? Vraiment ?*
- **Higgsfield** : `hero-video/assets/video/hero-chef-scan-carton.mp4` *(réemploi)*
- **Logiciel** : `videos/foodeatup-mouvements-stock-tuto/assets/screen.mp4` (24 s)

```
Chaque entrée et chaque sortie laisse une trace datée. Vous savez ce qui est entré, ce qui est sorti et ce qui reste — sans recompter les cartons un par un.
```

### 24 · Sortir ses ingrédients du stock
- **Hook** : *Tu produis. Ton stock, lui, ne bouge pas.*
- **Higgsfield** : `hero-video/assets/video/hero-kds-mural.mp4` *(réemploi)*
- **Logiciel** : `videos/foodeatup-sortie-stock-tuto/assets/screen.mp4` (51 s)

```
Vous validez la production, les ingrédients sortent du stock automatiquement, à la quantité de la recette. Votre stock théorique suit enfin ce que vous produisez vraiment.
```

### 25 · Prédire ses commandes avec PrediBot
- **Hook** : *12 kilos jetés dimanche soir. Encore.*
- **Higgsfield** : `hero-video/assets/video/hero-directeur-bureau-matin.mp4` *(réemploi)*
- **Logiciel** : `videos/foodeatup-predibot-tuto/assets/screen.mp4` (12 s) + `videos/foodeatup-predibot-suggestions-tuto/assets/screen.mp4` (42 s)

```
Trois ans de ventes, jour par jour, météo comprise. PrediBot vous dit combien vous allez vendre cette semaine, plat par plat. Vous produisez ce que vous allez vendre.
```

---

## MODULE — COMPTABILITÉ & ACHATS

### 26 · Scanner sa facture (OCR)
- **Hook** : *Ton fournisseur a augmenté. Tu l'as su quand ?*
- **Higgsfield** : `hero-video/assets/video/hero-directeur-sept-onglets.mp4` *(réemploi)*
- **Logiciel** : `videos/foodeatup-facture-ocr-tuto/assets/screen.mp4` (48 s)

```
Vous scannez la facture. L'OCR lit chaque ligne, met vos prix d'achat à jour et répercute l'écart sur vos marges. Vous ne retapez pas un seul chiffre.
```

### 27 · Créer une facture
- **Hook** : *Facturer le traiteur de samedi. Sur Word.*
- **Higgsfield** : `studio-video/assets/brand/loops/hero-loop-cuisine-laptop.mp4` *(boucle d'ambiance)*
- **Logiciel** : `videos/foodeatup-factures-tuto/assets/screen.mp4` (80 s)

```
Vous sélectionnez le client, les lignes, la TVA. La facture part numérotée et conforme, et elle se retrouve dans votre comptabilité au même instant. Sans deuxième saisie.
```

### 28 · Créer un devis
- **Hook** : *Un devis perdu, c'est un mariage perdu.*
- **Higgsfield** : `studio-video/assets/brand/loops/hero-loop-cuisine-laptop.mp4` *(boucle d'ambiance)*
- **Logiciel** : `videos/foodeatup-creer-devis-tuto/assets/screen.mp4` (99 s)

```
Le devis se monte depuis vos produits et vos prix réels. Vous l'envoyez, le client accepte, et il bascule en facture sans que vous ressaisissiez une ligne.
```

### 29 · Suivre ses dépenses fournisseur
- **Hook** : *Quel fournisseur te coûte le plus ? Devine.*
- **Higgsfield** : `hero-video/assets/video/hero-caisse-ticket-z.mp4` *(réemploi)*
- **Logiciel** : `videos/foodeatup-depenses-fournisseur-tuto/assets/screen.mp4` (79 s)

```
Chaque dépense se rattache à son fournisseur et à sa livraison. À la fin du mois, vous savez ce que chacun vous a réellement coûté — pas ce que vous croyiez.
```

### 30 · Déclarer son e-reporting
- **Hook** : *Facturation électronique. C'est pour bientôt.*
- **Higgsfield** : `hero-video/assets/video/hero-fermeture-lumieres.mp4` *(réemploi)*
- **Logiciel** : `videos/foodeatup-ereporting-tuto/assets/screen.mp4` (51 s)

```
Vos factures sont archivées légalement, au format attendu par l'administration. L'e-reporting se déclare depuis FoodEatUp — vous n'avez pas un logiciel de plus à acheter.
```

---

## Récapitulatif de réutilisation Higgsfield

Aucun nouveau plan Higgsfield n'est nécessaire pour ces 30 vidéos — tout est couvert par la
bibliothèque existante, conformément à la règle du dépôt.

| Plan | Réutilisé sur |
|---|---|
| `hero-directeur-sept-onglets.mp4` | 01, 03, 07, 26 |
| `hero-chef-carnet-dlc.mp4` | 02, 15, 19 |
| `hero-brigade-deux-langues.mp4` | 06, 09, 11 |
| `hero-chef-scan-carton.mp4` | 16, 22, 23 |
| `hero-directeur-bureau-matin.mp4` | 05, 21, 25 |
| `hero-fermeture-lumieres.mp4` | 17, 18, 30 |
| `hero-kds-mural.mp4` | 14, 24 |
| `hero-loop-chambre-froide.mp4` | 12, 13 |
| `hero-loop-cuisine-laptop.mp4` | 27, 28 |
| `hero-serveur-trois-tablettes.mp4` | 04 |
| `hero-salle-vide-matin.mp4` | 08 |
| `hero-serveur-place-client.mp4` | 10 |
| `hero-cuisine-vide-matin.mp4` | 20 |
| `hero-caisse-ticket-z.mp4` | 29 |

**Limite à connaître** : `hero-directeur-sept-onglets` sert 4 fois et 5 autres plans servent
3 fois. Publiées à une par jour, ces répétitions se remarqueront peu ; publiées en rafale,
elles se verront. Si tu veux diversifier, ce sont les 4 plans compta (01/03/07/26) qui
gagneraient le plus à avoir un plan dédié — dis-le-moi et je te donne les prompts à générer
manuellement dans Higgsfield.

## Ordre de publication conseillé

Alterner les douleurs d'argent et les douleurs de temps pour éviter l'effet catalogue :

> 25 (gaspillage) · 08 (planning) · 26 (OCR prix) · 19 (HACCP contrôle) · 04 (commandes
> perdues) · 11 (Jarvis) · 02 (food cost) · 10 (pointage) · 29 (dépenses) · 17 (checklist)
> · 20 (liste courses) · 07 (paie) · 22 (réception) · 05 (MCP Claude) · 15 (DLC) · 27
> (facture) · 24 (sortie stock) · 09 (tâches) · 13 (température) · 28 (devis) · 23 (stock)
> · 06 (employés) · 16 (étiquettes) · 21 (commande) · 12 (équipements) · 01 (ingrédients)
> · 18 (nettoyage IA) · 03 (fournisseurs) · 14 (température prod) · 30 (e-reporting)
