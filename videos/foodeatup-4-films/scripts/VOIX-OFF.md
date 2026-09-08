# FoodEatUp — 4 films · scripts voix off

Voix ElevenLabs (bibliothèque, natives FR) :
- **Paul K** (`ecxPjiGTvAfpGEams6ec`) — voix pub/trailer : clip + commercial
- **Anaïs** (`5OnMHwgTFgvPVwE8jP6B`) — narratrice du film héros : présentation
- **Enrick** (`0xHziZolI8Tp6rLtUqh2`) — voix calme tutoriel : démo

Règles reprises de la charte : hook d'ouverture, hook de fin, tagline officielle
« Une infinité de solutions pour gérer votre restaurant ». Le clin d'œil du logo
ponctue chaque validation. Pas de chiffre d'essai dans la voix (7 vs 14 jours à
trancher) : la voix dit « essai gratuit, sans carte bancaire », l'URL est à l'écran.

---

## 1. CLIP « Une journée. Une app. » — 60 s · 9:16 · musique originale 123 BPM

La musique mène. Trois actes calés sur la structure du morceau :
chaos (0–30 s, coupes toutes les 1,5–2,5 s), break (30–45 s, plans calmes des
tablettes et de Jarvis), final (45–62 s, plans de joie, célébration, logo).

| Code | Timecode | Voix (Paul K) |
|---|---|---|
| C1 | 0:01 | Gérer un restaurant, c'est ça. |
| C2 | 0:30 | Et si tout ça… tenait dans une seule app ? |
| C3 | 0:46 | FoodEatUp. Une infinité de solutions pour gérer votre restaurant. |
| C4 | 0:56 | Essayez gratuitement. Sans carte bancaire. |

Cartons à l'écran (jamais de texte qui redit la voix) :
« LE STOCK » · « LES DLC » · « LE PLANNING » · « LES AVIS » · « LA COMPTA » ·
« LE CONTRÔLE » (sur les gags correspondants) puis « UNE SEULE APP » au break,
logo + « foodeatup.fr » au final.

---

## 2. FILM DE PRÉSENTATION « Le même restaurant » — ~95 s · 9:16 (+16:9)

| Code | Voix (Anaïs) |
|---|---|
| P1 | Un restaurant, c'est une cuisine, une salle, une direction. Et entre les trois, tout ce qui se perd : le stock que la caisse ne connaît pas, les températures notées sur un carnet, le planning refait trois fois, les appels manqués pendant le service. |
| P2 | FoodEatUp réunit tout ça dans une seule plateforme. Quatorze modules, huit boucles métier qui se referment toutes seules : chaque vente déstocke, chaque livraison est tracée, chaque facture met vos prix à jour. |
| P3 | Et pour que personne ne remplisse plus un tableau à la main, quatre agents d'intelligence artificielle travaillent avec vous. Jarvis, le commis vocal en cuisine. Caroline, qui répond à vos clients quand vous ne pouvez pas décrocher. PrediBot, qui prépare la nuit ce qu'il faudra produire et commander. Iris, qui transforme votre surstock en plat du jour sur les réseaux. |
| P4 | L'hygiène ? Températures, traçabilité, étiquettes DLC, nettoyage contrôlé par photo : le classeur HACCP s'écrit tout seul, pendant que vous cuisinez. |
| P5 | Et parce que votre restaurant doit vous appartenir, FoodEatUp se pilote aussi depuis Claude, Mistral, ChatGPT ou WhatsApp : cent soixante-dix-sept outils, une seule connexion. |
| P6 | Ce n'est pas la même journée. C'est le même restaurant. FoodEatUp. Une infinité de solutions pour gérer le vôtre. |

---

## 3. FILM COMMERCIAL « Le contrôleur » — ~40 s · 9:16 (+16:9)

| Code | Voix (Paul K) |
|---|---|
| A1 | Le contrôleur pousse la porte un mardi, à onze heures. Vous cherchez le classeur. Vous savez qu'il manque une semaine de températures. Lui aussi. |
| A2 | Avec FoodEatUp, tout est déjà là. Relevé, horodaté, exportable en un clic. Le stock, les DLC, le planning, les factures : une seule app, et des agents IA qui bossent pendant que vous cuisinez. |
| A3 | FoodEatUp. Une infinité de solutions pour gérer votre restaurant. |
| A4 | Essai gratuit, sans carte bancaire. Rendez-vous sur foodeatup point fr. |

---

## 4. FILM DÉMO « Un tour du logiciel » — ~2 min 10 · 16:9

Screencasts réels du dépôt (`videos/foodeatup-*-tuto/assets/screen.mp4`).
Ouverture avec l'avatar HeyGen existant du chef FoodEatUp (`foodeatup-qrcode-tuto/assets/avatar.mp4`).

| Code | Écran | Voix (Enrick) |
|---|---|---|
| D1 | avatar HeyGen + tableau de bord | Bienvenue dans FoodEatUp. En deux minutes, faisons le tour de ce que vous verrez chaque jour. Dès la connexion, le tableau de bord résume l'activité : ventes, stock, équipe et alertes. |
| D2 | fiche plat / carte | Votre carte se construit en quelques clics. Pour chaque plat, la recette calcule le coût matière et vous propose un prix de vente selon la marge visée. Un menu en PDF ? L'intelligence artificielle l'importe entièrement. |
| D3 | réception livraison + mouvements de stock | À la réception d'une livraison, vous scannez : lot, DLC, température. Le stock se met à jour en temps réel, et chaque vente en caisse déstocke automatiquement. |
| D4 | températures + traçabilité + export HACCP | Côté hygiène, les températures, la traçabilité et les étiquettes sont saisies sur place, horodatées. Le classeur HACCP s'exporte en PDF en un clic, prêt pour le contrôle. |
| D5 | planning poste + QR pointage | Votre équipe a son planning par poste, ses congés et son pointage par QR code. Chaque employé accède seulement à ce qui le concerne. |
| D6 | facture OCR + statuts | Photographiez une facture fournisseur : l'OCR lit les lignes, met à jour vos prix d'achat et suit le paiement jusqu'au règlement. |
| D7 | boutique / vitrine | Votre site de commande en ligne est généré à partir de votre carte, à vos couleurs, sans commission de plateforme. |
| D8 | Jarvis + PrediBot | En cuisine, Jarvis exécute vos ordres à la voix et trace chaque sortie. La nuit, PrediBot prépare la production du lendemain et la commande fournisseur. |
| D9 | MCP + abonnement | Enfin, FoodEatUp se connecte à Claude, ChatGPT ou WhatsApp par MCP. Essayez gratuitement, sans carte bancaire : FoodEatUp, une infinité de solutions pour gérer votre restaurant. |

---

## 5. SIX SHORTS THÉMATIQUES — ~25 s chacun · 9:16 (+16:9) · voix Paul K

Même structure partout : problème (2 plans) → solution (2 plans) → signature (C3) → carton
final (C4). Les durées de plan sont calculées à partir de la durée réelle de chaque voix off,
donc un short se re-rend sans retoucher les timecodes.

| Short | Code | Ligne « problème » | Ligne « solution » |
|---|---|---|---|
| HACCP — « Le contrôle » | SH1 | Vos températures ? Elles sont sur un post-it. Quelque part. | Avec FoodEatUp, elles sont relevées, horodatées, et votre classeur HACCP s'exporte en un clic. |
| Stock — « L'inventaire » | SH2 | Douze bouteilles. Onze. Quinze. L'inventaire, chaque semaine, à la main. | Avec FoodEatUp, chaque vente déstocke toute seule, et PrediBot vous prévient avant la rupture. |
| Équipe — « Le planning » | SH3 | Trois demandes de congé pour le même samedi. Et un planning refait à la main. | Avec FoodEatUp, planning par poste, congés et pointage par QR code. Chacun voit ce qui le concerne. |
| Compta — « L'addition » | SH4 | Une table de douze qui paie séparément. Et vous, la calculette à la main. | Avec FoodEatUp, la caisse partage l'addition, l'OCR lit vos factures et le ticket Z part tout seul. |
| Réservations — « La double réservation » | SH5 | Deux clients. Une table. La même heure. Vous avez réservé deux fois. | Avec FoodEatUp, le plan de salle est à jour, et Caroline répond même quand vous ne décrochez pas. |
| Avis — « L'avis du soir » | SH6 | Service parfait. Et le soir, une étoile. Pour une livraison en retard. | Avec FoodEatUp, chaque avis remonte, la réponse se prépare toute seule, et Iris publie à votre place. |

Signature commune : C3 « FoodEatUp. Une infinité de solutions pour gérer votre restaurant. »
puis C4 « Essayez gratuitement. Sans carte bancaire. » sur le carton final.
