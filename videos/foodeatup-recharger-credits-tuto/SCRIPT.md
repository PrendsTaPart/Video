# Tutoriel — Recharger ses crédits, Pack Com' (module Marketing, Fidélité & Iris)

Catalogue #11 du module `marketing-fidelite` (24 vidéos attendues), sous-catégorie
« WhatsApp, SMS & crédits ». Intrants fournis : carte d'intro `RECHARGER_TES_CREDITS.jpg`
(mascotte fondateur, 1281x721), carte de fin `page_fin_vid..jpg` (CTA générique, même
carte que le reste de la série) et rush `Achat_de_pack_de_crédit_SMS_Email_WhatsApp.mp4`
(1920x828, 25 fps, 13,52 s, H.264/AAC).

## Statut : produite sur autorisation directe (2026-08-05)

Même cas que `foodeatup-documents-nettoyage-tuto` et `foodeatup-resultats-sondages-tuto` :
structure, voix off, montage, vignette et publication (GitHub + RapidoCMS + Lovable)
explicitement redemandés en un seul message par l'utilisateur, consigne de publier
« une fois le montage terminé ». Le STOP de validation script/vidéo est levé pour
cette vidéo par cette autorisation explicite ; le fichier est quand même livré via
`SendUserFile` avant publication pour repérage immédiat si correction nécessaire.

## Ce que montre le rush

Rush court (13,52 s) — page d'upgrade d'abonnement ("Boostez votre gestion avec
stockvision"), déjà scrollée sur la section pertinente pour ce tutoriel :

| t (s) | Écran |
|---:|---|
| 0,0–5,5 | Haut de page (plans StockVision, hors sujet pour ce tutoriel — non utilisé dans le montage) |
| 5,5–8,5 | Carte **"Marketing & Commercial"** (99 €/mois, déjà **Activé**) : "Module Marketing unifié : campagnes email/SMS/WhatsApp/vocal ciblées RFM, agent IA, jeux concours et sondages — **1 500 crédits et 30 min audio/mois inclus** (mise en service 199 €, offerte en annuel)". Le curseur surligne la mention "email/SMS/WhatsApp/vocal" (démonstration, pas un clic — le bouton "Activé" est désactivé, curseur "interdit") |
| 8,5–13,4 | Scroll vers **"Options & modules"** : "À ajouter à votre pack principal — la souscription s'empile, votre plan actuel n'est pas remplacé." Cartes Éditeur de site IA (29€/mois), Jarvis — assistant vocal (49€/mois), Marketing & Commercial (99€/mois, Activé), puis Caroline — agent vocal téléphonique (79€/mois), PrediBot — assistant WhatsApp (49€/mois), PrediBot — établissement supplémentaire (39€/mois) |

Pas de bouton "recharger" isolé dans ce rush : les crédits SMS/Email/WhatsApp
sont inclus dans le Pack Marketing & Commercial (1 500/mois), et l'écran filmé
montre où les trouver / ce qu'ils couvrent, pas un flux d'achat de crédits à
l'unité — le montage suit fidèlement ce que montre l'écran, sans inventer
d'étape.

## Pas de séquence "Utiliser avec Claude"

Aucun outil `mcp__Foodeatup__*` ne couvre l'achat ou le suivi de crédits
SMS/Email/WhatsApp (facturation Stripe côté produit, pas un objet MCP). Pas de
prompt inventé ; section absente à la fois de la vidéo et de la fiche Lovable
(`claudePrompt` non renseigné).

## Voix off (5 lignes, voix Adam FR `TGAegA0zNRi8I6nUdq3i`)

| # | Texte | Ancrage |
|---|---|---|
| N0 | Où trouver et recharger vos crédits SMS, Email et WhatsApp sur FoodEatUp ? | carte d'intro |
| N1 | Le Pack Marketing et Commercial inclut 1500 crédits et 30 minutes audio chaque mois. | segment A — carte Marketing & Commercial |
| N2 | Ils couvrent vos campagnes email, SMS, WhatsApp et vocales, ciblées grâce au RFM. | segment A (suite) |
| N3 | Besoin de plus ? Complétez avec les options du pack, sans jamais remplacer votre abonnement actuel. | segment B — Options & modules |
| N4 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | carte de fin (CTA) — réutilisé tel quel depuis `foodeatup-dlc-tuto/vo/N8.mp3` |

N4 copié depuis un tutoriel précédent (texte générique identique) — zéro
crédit ElevenLabs dépensé sur cette ligne.

## Découpage prévu (durées cibles ajustées après mesure des VO)

| Seg | Source (rush) | Cible | Contenu |
|---|---|---:|---|
| intro | carte | ~6,5 s | RECHARGER TES CRÉDITS |
| A | 5,50–8,50 | ~9,0 s | Carte Marketing & Commercial, 1 500 crédits inclus |
| B | 8,50–13,40 | ~6,0 s | Scroll Options & modules |
| outro | carte | ~6,0 s | CTA (auto-étendu si nécessaire) |

Pas de zoom-punch (aucun clic dans le rush) : légères crops fixes + Ken Burns
doux sur A et B pour éviter un plan totalement statique. Transitions `fade`
partout (une seule vraie coupure de contenu, intro→A puis A→B en `fade`
également car c'est un scroll continu, pas une coupure de contexte).

## Compatibilité cible (checklist avant livraison)

H.264 High/yuv420p 1920x828 25fps, AAC LC 48 kHz stéréo, faststart (moov avant
mdat), true peak visé ≈ -7 dBFS sur le MP4 final, 0 erreur de décodage.

## Statut publication

En cours — voir tâches de la session : montage → QA → vignette → push GitHub →
upload RapidoCMS → fiche Lovable (module `marketing-fidelite`, sans
`claudePrompt`, avec `chefTip`) → mise à jour de `LOVABLE-FOODEATUP-DOCS.md` /
`PROGRESSION-157-TUTORIELS.md`.
