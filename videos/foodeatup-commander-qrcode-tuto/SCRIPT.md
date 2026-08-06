# Tutoriel — Commander par QR code

Rush fourni par Michael : `scanner_le_qrcode__de_la_table_pour_realiser_une_commande.mp4`
(75,96 s, 1920×828, 25 fps) + carte intro `COMMANDER_PAR_QR_CODE.jpg`. Carte outro
réutilisée telle quelle depuis `foodeatup-qrcode-tuto/assets/outro.jpg`. Durée livrée :
**49,24 s** — H.264 High/yuv420p, AAC 48 kHz stéréo, faststart. Audio : true peak
**-7,15 dBFS** (marge confortable). Sans avatar (même choix que `foodeatup-qrcode-tuto` :
une seule voix ElevenLabs cohérente sur toute la série).

Catalogue : module **7a. Service Multi-Canal** (`service-commande`), vidéo 02
« Commander sur Site & QR (ou agent vocal) » — `videos/CATALOGUE-157-TUTORIELS.md`.

Écran couvert : plan de salle (sélection table QA3, révélation du QR code) → page de
commande client « Goasushi démo — Table QA3 » (carte, panier, envoi en cuisine) → « Payer
l'addition » (répartition, carte bancaire, Stripe).

## Voix off (8 lignes, sans avatar)

| # | Texte | Durée | Segment |
|---|---|---:|---|
| N1 | Commander par QR code chez vous ? Chaque table FoodEatUp a le sien, généré depuis le plan de salle. | 5,67 s | A |
| N2 | Le client n'a qu'à le scanner avec son téléphone pour ouvrir votre carte, sans télécharger d'application. | 5,62 s | C |
| N3 | Il choisit ses plats et ses boissons, ajoute au panier, et valide sa commande en quelques clics. | 4,91 s | D |
| N4 | Elle part aussitôt en cuisine, sans aucune intervention de votre équipe en salle. | 4,60 s | E |
| N5 | Et pour finir, il peut régler l'addition directement depuis la table, par carte bancaire, en toute sécurité. | 6,22 s | F1 + clic F2 |
| N6 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | 4,41 s | étages 1+2 (réutilisée depuis `foodeatup-qrcode-tuto/vo/N6.mp3`) |
| N7 | Collez-le dans la conversation : la commande est enregistrée et transmise en cuisine en quelques secondes. | 5,67 s | étage 3 |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | 5,02 s | carte de fin (réutilisée depuis `foodeatup-qrcode-tuto/vo/N8.mp3`) |

N6/N8 réutilisés tels quels depuis `foodeatup-qrcode-tuto/vo/` (texte générique, cf. règle
du `FOODEATUP-TUTORIELS-WORKFLOW.md` : N6/N8 réutilisables, N7 toujours spécifique).

## Découpage

| Seg | Source | Sortie | Contenu |
|---|---|---:|---|
| intro | carte | 2,50 s | COMMANDER PAR QR CODE |
| A | 14,00 → 24,60 | 5,80 s | Plan de salle : sélection de la table QA3, panneau statut |
| B | 24,60 → 31,50 | 3,00 s | QR code généré pour la table (modal, lien copié) |
| C | 31,50 → 38,50 | 5,80 s | Scan (transition) → ouverture de la page de commande client |
| D | 38,50 → 43,70 | 5,20 s | Carte : ajout au panier (Dragon Roll, Pizza, California Roll, Gyoza, Edamame, Chirashi Saumon) |
| E | 43,70 → 46,50 | 4,80 s | Clic « Commander » → « Commande transmise en cuisine » |
| F1 | 46,50 → 70,80 | 6,40 s | Payer l'addition : total, répartition, sélection carte Visa |
| F2 | 70,80 → 71,60 | 0,80 s | **zoom-punch** sur « Payer 10,20 € » (949, 603) |
| claude1 | carte générée | 3,00 s | reveal — prompt en gros, fond crème |
| claude2 | carte générée | 2,30 s | confirmation « Copié dans le presse-papiers ! » |
| claude3 | carte générée | 5,30 s | mockup chatbot Claude |
| outro | carte | 7,36 s | CTA (étendue automatiquement pour laisser N8 se terminer) |

Coordonnées mesurées par extraction de frames pleine résolution (1920×828). Rush dense
(76 s, 3 écrans) : plan de salle et navigation compressées (segment A ×1,83), scan/transition
fortement accélérée (segment C couvre 7 s de rush en 5,8 s de sortie car la ligne N2 est
longue), flux de paiement très accéléré (F1 ×3,7, 24,3 s de rush en 6,4 s).

## Séquence Claude — module partagé

Seule action du rush avec un équivalent MCP direct : `create_order(establishment_id,
items[], table_id, service_mode="sur_place")` — crée la commande et génère automatiquement
facture + devis. La révélation du QR code (génération client-side d'un lien/QR pour la
table) et le paiement (Stripe côté client) n'ont pas d'équivalent MCP direct — pas de prompt
inventé pour ces étapes (cohérent avec le traitement du QR/flyers/cartes de visite sur
`foodeatup-qrcode-tuto`).

> Crée une commande sur place pour la table [numéro de table] avec [plat 1] x[quantité],
> [plat 2] x[quantité], pour mon établissement FoodEatUp (ID [ID établissement]).

Même texte côté fiche Lovable (`claudePrompt`).

## Animations

Mêmes principes que toute la série : Ken Burns sur les cartes, xfade (0,28 s), bandeaux
d'étape (`banner()`, version corrigée à clamp unique — pas de slide-out animé), encadré
orange pulsant sur le clic « Payer ». Pas de plan avatar sur cette vidéo.

## Vérifications effectuées

- Codec/pix_fmt/audio conformes (H.264 High yuv420p, AAC 48 kHz stéréo, faststart, moov
  avant mdat).
- Peak level vérifié sur le fichier final encodé : -7,15 dBFS (`astats`).
- Bandeaux d'étape et encadré de clic vérifiés visuellement par extraction de frames
  (pas seulement absence d'erreur ffmpeg — piège déjà rencontré sur la série).
- Dérive VO/visuel vérifiée (`offsets:` vs ancrages `S[...]`) : dérive maximale 1,2 s
  (sur N8, absorbée par l'extension automatique de la carte de sortie), toutes les autres
  lignes ≤ 0,82 s.

## Statut publication

Vidéo livrée à Michael pour validation avant publication RapidoCMS/LinkedIn/Lovable, selon
la règle du 2026-08-02 (`LOVABLE-FOODEATUP-DOCS.md` : ne pas publier sans validation
explicite au préalable).
