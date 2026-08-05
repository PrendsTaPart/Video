# Tutoriel — Ciblage et Consentement clients (module Marketing, Fidélité & Iris)

Catalogue 157 tutoriels, module `marketing-fidelite` (item 09 : « Ciblage et
**Consentement** clients »), premier tutoriel produit pour ce module (0/24 avant
cette vidéo). Rush source : `assets/screen.mp4`, 1920x828, 25 fps, 28,24 s.
Intrants fournis par Michael : `assets/intro.jpg` (carte « CIBLAGE & CONSENTEMENT »),
`assets/outro.jpg` (carte CTA réutilisable, identique aux autres tutos).

## Ce que montre le rush

Pas de formulaire de création ici : c'est un écran de **lecture/pilotage** (segments
calculés automatiquement + gestion RGPD), montré par défilement continu.

1. `0-4s` — Page « Campagnes & automatisations » (menu Marketing), onglets
   Automations / Campagnes / Agent IA / Agenda / Templates WhatsApp / **Segments &
   consentements** → clic sur ce dernier onglet.
2. `4-9s` — Panneau **Segments dynamiques** : VIP (≥2 visites/mois et panier >35€),
   Réguliers (≥1 visite/mois depuis 3 mois), Nouveaux (1re commande <30j), À risque
   (habitués sans visite depuis +50% de leur rythme), Perdus (>90j sans visite), Gros
   paniers (panier moyen >50€) — calculés en direct depuis l'historique de commandes,
   « aucun tag manuel ». En vis-à-vis, panneau **Plafond mensuel par client** : curseur
   2/3/4/5/6 (réglé sur 4, « Recommandé : 4 »), fenêtre légale 8h→20h, pas le dimanche,
   dédup automatique par déclencheur.
3. `9-13s` — Défilement vers **Contacts & consentements (39)** : tableau contact / « Ce
   mois » (ex. 0/4) / canaux autorisés (email, SMS, WhatsApp, vocal — icônes actives ou
   grisées selon le consentement donné par canal) / bouton **STOP** par contact.
   Info-bulle vue au survol : « Plafond : X messages / client / mois ».
4. `13-22s` — Suite du tableau : un contact déjà arrêté apparaît grisé avec un bouton
   **Réactiver** à la place de STOP (ex. « Robert Ancien »). Info-bulle au survol d'un
   STOP déjà utilisé : « Contact exclu de tout marketing (STOP) ».
5. `22-27s` — Fin de liste + mention RGPD explicite : « un contact STOP est
   instantanément retiré de tous les ciblages. Chaque message envoyé contient la
   procédure de désinscription. »
6. `27-28,2s` — **Journal des 20 derniers envois** : historique horodaté par contact
   (ex. « Inès Moreau — Bonjour Inès, cela fait un moment ! -10% cette semaine avec le
   code RETOUR10... — 12/07 11:00 »).

## Séquence Claude — un outil MCP correspond (lecture)

`mcp__Foodeatup__list_rfm_segments(establishment_id)` retourne exactement les segments
RFM (champions/fidèles/prometteurs/à risque/perdus/nouveaux) affichés dans le panneau
« Segments dynamiques » du rush — avec leurs compteurs et leur logique, la cible des
campagnes. C'est un outil de lecture (comme `finance_summary` sur
`lire-ses-statistiques-par-module`) : le prompt vidéo est donc un prompt de
**consultation**, pas de création.

Le volet « Consentement » (bouton STOP par contact, canaux autorisés) n'a **pas**
d'outil MCP correspondant (`update_client` n'expose qu'un statut générique
Actif/Inactif/Suspendu, pas un opt-out marketing par canal) — pas de prompt inventé
pour cette partie, elle reste documentée uniquement en `howItWorks`/`chefTip` côté
Lovable, conformément à la règle du pipeline.

Second prompt (Lovable `claudePrompts[]` uniquement, pas dans la vidéo) :
`mcp__Foodeatup__create_campaign` — enchaîner directement sur le segment ciblé pour
créer le brouillon de campagne (email/sms/whatsapp/vocal).

## Voix off proposée (9 lignes) — À VALIDER AVANT GÉNÉRATION AUDIO

| # | Texte | Ancrage |
|---|---|---|
| N0 | Cibler vos clients tout en respectant leur consentement ? FoodEatUp s'en charge. | carte d'intro |
| N1 | Dans Marketing, ouvrez Campagnes et automatisations, puis l'onglet Segments et consentements. | navigation + clic onglet |
| N2 | Vos segments — VIP, réguliers, nouveaux, à risque — sont calculés automatiquement depuis l'historique de commandes, sans aucun tag manuel. | panneau Segments dynamiques |
| N3 | Réglez le plafond mensuel de messages par client pour rester dans la fenêtre légale, entre 8h et 20h. | panneau Plafond mensuel |
| N4 | Chaque contact garde la main : canaux autorisés au cas par cas, et un bouton STOP pour se retirer instantanément de tout ciblage. | tableau Contacts & consentements |
| N5 | Conformité RGPD garantie : un contact STOP disparaît aussitôt de vos campagnes, avec la procédure de désinscription dans chaque message envoyé. | mention RGPD + journal des envois |
| N6 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | étages Claude 1+2 (réutilisable tel quel, mp3 copié depuis un tuto existant) |
| N7 | Collez-le dans la conversation : vos segments RFM s'affichent en quelques secondes, prêts à cibler pour votre prochaine campagne. | étage Claude 3 |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | carte de fin (CTA, réutilisable tel quel, mp3 copié) |

N6 et N8 : texte strictement identique à `foodeatup-checklist-hygiene-tuto`, copie
directe des `.mp3` existants (0 crédit ElevenLabs). N0, N1, N2, N3, N4, N5, N7 sont
spécifiques à cette vidéo → 7 lignes à générer.

## Prompt Claude (vidéo, étages 1-3)

```
Quels segments RFM puis-je cibler pour ma prochaine campagne sur mon établissement
FoodEatUp (ID [ID établissement]), avec le nombre de clients et le pourquoi de chaque
segment ?
```

## Prompts Lovable (`claudePrompts[]`, 2 entrées)

1. **Consulter mes segments RFM** — prompt ci-dessus (`list_rfm_segments`).
2. **Lancer une campagne ciblée** — `Crée une campagne [email/sms/whatsapp/vocal] en
   brouillon nommée [nom de la campagne] pour le segment [champions/fideles/
   prometteurs/a_risque/perdus/nouveaux], avec le message [texte du message, incluant
   {prenom} {code} {lien} si besoin], le code promo [code promo] et le lien [URL], pour
   mon établissement FoodEatUp (ID [ID établissement]).` (`create_campaign`)

## Statut

Script validé par Michael le 2026-08-05. VO générée (7 lignes ElevenLabs, voix Adam FR
`TGAegA0zNRi8I6nUdq3i` ; N6/N8 copiées telles quelles depuis `foodeatup-checklist-hygiene-tuto`,
0 crédit). Montage terminé (`build.py`, ffmpeg) : **60,6 s**, dérive voix/image ≤0,1 s sur
toutes les lignes, pic audio final -7,17 dBFS. Vignette YouTube générée depuis
`assets/intro.jpg` (1280x720, 90 Ko, sans recadrage créatif). Livrables dans `out/`.

**STOP obligatoire toujours en vigueur avant publication** (Lovable/RapidoCMS/LinkedIn) :
en attente de validation explicite du montage final par Michael — voir
`LOVABLE-FOODEATUP-DOCS.md`, règle ajoutée le 2026-08-02.
