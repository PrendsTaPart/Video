# 🎬 Storyboard — RapidoCRM tutoriel (16:9, ~4:00)

Charte : fonds `#383838` · vert `#4CAF50` dominant · violet `#7E57C2` en titre de section · Arial → Liberation Sans.
Avatar Mika aux transitions · scène chat Claude pour les 3 « Astuces du Chef » (machine à écrire → coche → **l'oiseau vert clignote**).
Rendu local (HeyGen/Veo indispo → boucle Mika + `generate_image`). Substituts « Option B » : tunnel SMS = séquence des écrans réels.

| # | TC | Chapitre | Source | Animation | VO |
|---|-----|----------|--------|-----------|-----|
| 1 | 0:00–0:12 | HOOK | FLOW-01 substitut (`generate_image` : commercial noyé, tableur) | Zoom nerveux | « Vos prospects sont dans un tableur. Vos relances, dans votre tête. Et vos devis… quelque part. » |
| 2 | 0:12–0:15 | LOGO STING | sting-crm-in (3 oiseaux, vert en tête) | build-up + flash vert | *(son)* |
| 3 | 0:15–0:30 | Intro Mika | boucle Mika + fond `#383838`+halo vert | cut franc | « RapidoCRM, votre force de vente pilotée en parlant à votre IA. Guide administrateur… » |
| 4 | 0:30–0:55 | Compte & entreprise | crm-01 → crm-02 → crm-03 | enchaînement Ken Burns | « Inscription en deux temps : votre compte, puis votre entreprise — nom, email, SIRET. » |
| 5 | 0:55–1:25 | ⭐ Connexions | crm-04 (IMAP) → crm-05 (Stripe) → crm-06 (SMS) | 3 cards, lower-thirds violets | « Trois branchements : boîte mail, Stripe, Twilio. » |
| 6 | 1:25–1:55 | ⭐⭐ MCP | URL `https://crm.rapidosoftware.com/mcp` **≥6 s** + logos Claude/Mistral/OpenAI | cascade logos | « Ajoutez cette URL comme connecteur MCP. L'IA agit avec vos droits admin — accès réservé aux habilités. » |
| — | | Astuce 1 | chat Claude (crm-07) | machine à écrire → coche → oiseau vert | « Un message pour vérifier que tout est branché. » |
| 7 | 1:55–2:25 | Équipe | crm-09 (objectifs) → crm-08 (cards statut) | zoom 6 objectifs | « Chaque commercial reçoit son invitation par email. Vous fixez ses objectifs. » |
| — | | Astuce 2 | SR-CRM-01 substitut (chat Claude) | machine à écrire → coche | « Toute votre équipe en un message. » |
| 8 | 2:25–3:05 | ⭐⭐⭐ Campagne SMS | **tunnel réel** : crm-19/32 ciblage (10 touchés) → crm-33 modèle → crm-30 texte → crm-31 aperçu téléphone | séquence, cadre vert, zoom compteur | « Ciblez. Le compteur dit qui sera touché. Un modèle, vous validez. L'envoi part à l'heure prévue. » |
| 9 | 3:05–3:35 | Devis/factures/contrats | crm-28 (choix charte) → facture → crm-29 (template mail) | sélecteur couleurs animé | « Vos devis à vos couleurs. Le contrat part par email, depuis un modèle. » |
| — | | Astuce 3 | chat Claude | machine à écrire → coche → oiseau vert | « Facturez et contractualisez en parlant. » |
| 10 | 3:35–3:50 | Quotidien | crm-21 agenda → crm-23 prise RDV → crm-20 mail | carrousel | « Vos RDV, avec rappel. Votre boîte mail. Votre pipeline. » |
| 11 | 3:50–4:00 | STING SORTIE + HOOK FIN | sting-crm-out (oiseaux battent, vert pulse) | CTA vert | « Vous pilotez. L'IA exécute. Et ça, c'est juste le CRM — attendez de voir quand il parle à votre CMS et à votre RH. » |

## Lower-thirds techniques (crédibilité, outils MCP réels)
Connexions · MCP `list_commerciaux`/`list_entreprises` · Équipe `create_commercial`/`update_commercial_objectifs` · Campagne `create_campagne`/`lancer_campagne`/`schedule_sms` · Docs `create_facture`/`create_contrat`/`create_devis` · Quotidien `create_rdv`/`get_today_schedule`.

## Sound design
Bureau saturé (0-12 s) → cut net + silence au sting → nappe calme → frappe clavier → note de verrouillage à chaque validation → montée finale → battement d'ailes → coupe.

## Bonus (plan seulement) — 4 shorts verticaux
MCP + sécurité admin · campagne SMS en 3 étapes · facture/contrat en parlant · l'écosystème des 3 oiseaux.
