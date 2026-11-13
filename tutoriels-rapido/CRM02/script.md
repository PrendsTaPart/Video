# CRM02 — Visite guidée du tableau de bord (RapidoCRM)

Durée : 1 min 07 · Voix : ElevenLabs « Adam — Instructor » (`TGAegA0zNRi8I6nUdq3i`, eleven_v4) · Écran : RapidoCRM local, données fictives.

| Chapitre | Texte dit |
|---|---|
| Intro | Bienvenue dans RapidoCRM ! Dans ce tutoriel, on fait le tour de votre tableau de bord : l'écran qui vous dit, en un coup d'œil, comment va votre activité. |
| 1 · Statistique générale | Tout en haut, la statistique générale. À gauche, vos interactions des sept derniers jours : SMS, e-mails et newsletters envoyés. À droite, votre chiffre d'affaires, avec la part des factures payées et en attente. |
| 2 · Bloc CRM | Juste en dessous, le bloc CRM : vos clients, vos contacts, vos rendez-vous et vos événements. |
| 3 · Marketing | Le bloc Marketing compte les e-mails, les SMS et les newsletters que vous avez envoyés. |
| 4 · Commercial | Côté commercial, retrouvez vos factures payées et en attente, vos devis signés et en attente, vos dépenses, vos commerciaux et vos produits. |
| 5 · Segmentation | Enfin, la segmentation vous donne une vue globale de la prospection, du pipeline et de vos campagnes. |
| 6 · Menu | Un chiffre vous intrigue ? Le menu de gauche vous emmène directement vers vos clients, votre pipeline, vos factures ou vos campagnes. |
| Outro | Retrouvez tous les tutoriels RapidoCRM sur rapidosoftware point com. À tout de suite ! |

## Reproduire
1. Lancer RapidoCRM en local (SQLite) puis `php _gabarit/demo-crm.php <rapido-crm>/database/database.sqlite`.
2. `node CRM02/record.cjs http://127.0.0.1:8124 demo@rapido.test Demo-Rapido-2026 CRM02/paragraphes.json`
3. `ffmpeg -ss <voiceStartInCapture> -i captures/ecran.webm -t 60 -an -c:v libx264 -crf 18 -pix_fmt yuv420p -r 30 captures/ecran.mp4`
4. `python3 _gabarit/build-tutoriel.py CRM02 && cd CRM02 && npx hyperframes render --output ../../videos/tutoriels-rapido/CRM02.mp4`
5. Miniature : `node _gabarit/miniature.cjs --product crm --num CRM02 --title "Visite guidée du tableau de bord" --em "tableau de bord" --tag "1 min · Débutant" --shot CRM02/captures/fin.png --out CRM02/miniature.png`
