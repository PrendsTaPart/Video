# Tutoriel — Exporter tout son classeur HACCP (historique) FoodEatUp

Module HACCP, établissement de test GoSushi (ID 26) — mêmes données réelles que le
reste de la série (`responsable_enregistrement: "Soulayma"` confirmé via
`mcp__FoodEatUp__list_haccp_temperatures`). Rush : `Retrouver et exporter les
Historique du module HACCP.mp4`, 1920x828, 25fps, 58,4 s, exploitable en entier
(pas de rush corrompu cette fois — pipeline `build.py` standard, pas la variante
scène HTML de `foodeatup-rapport-historique-tuto`).

**Statut : DRAFT — en attente de validation avant génération VO (STOP obligatoire,
voir FOODEATUP-TUTORIELS-WORKFLOW.md étape 3).**

## Déroulé observé dans le rush (extraction de frames toutes les 2s + frames ciblées)

1. `t≈0-8s` — Hub "Historique HACCP" : 7 cartes (Températures 330 relevés,
   Traçabilité 90 éléments, Plan de nettoyage 38 actions, Production 14 productions,
   Contrôle à réception 4 contrôles, Checklist Hygiène 2 validations, Étiqueteuse 24
   étiquettes).
2. `t≈8-12s` — Historique > Températures : stats réelles (19 911 total relevés,
   14 504 conformes, 1 694 attention, 95 non conformes, 24 équipements, 26 plats),
   toggle Équipements/Plats, bouton **Exporter CSV**, détail "Frigo 1" 13,0°C.
3. `t≈12-16s` — Historique traçabilité : tableau (entrée "Abricot", congelé, date/heure,
   utilisateur Soulayma, actions Modifier/Supprimer).
4. `t≈16-20s` — Historique > Contrôle à réception : tableau fournisseurs (Les Jardins
   Douceurs, etc.), filtres date début/fin + statut.
5. `t≈20-24s` — Historique étiquettes : liste (fabriqué / expiré, journal d'audit,
   bouton Exporter).
6. `t≈24-28s` — Historique des validations (Checklist Hygiène) : bouton **Exporter
   l'historique** + menu déroulant **Exporter ▾** (Export Rapide / Export Email /
   Export Multiformat), stats (2 total, 1 conforme, 100% score moyen).
7. `t≈40-42s` — Toast succès **"Export standard généré avec succès"** + indicateur
   "PDF généré avec succès" à côté du bouton Exporter.
8. Passages secondaires : page stats Production (205 productions, 8438 portions,
   tendance 6 derniers mois).

## Voix off proposée (9 lignes, voix Adam FR `TGAegA0zNRi8I6nUdq3i`)

| # | Texte | Ancrage |
|---|---|---|
| N0 | Retrouver et exporter l'historique de votre module HACCP ? Suivez le guide. | carte d'intro |
| N1 | Ouvrez Historique : températures, traçabilité, nettoyage — chaque module a le sien. | hub, 7 cartes |
| N2 | Dans Températures, filtrez par date ou équipement, puis exportez tout en CSV. | stats + bouton Exporter CSV |
| N3 | Traçabilité et Contrôle à réception gardent la trace de chaque produit, entrée par entrée. | tableaux traçabilité + réception |
| N4 | Sur Checklist Hygiène, cliquez sur Exporter l'historique : rapide, par email, ou multi-format. | zoom-punch clic "Exporter l'historique" / menu déroulant |
| N5 | Votre classeur HACCP reste toujours prêt : un contrôle sanitaire peut arriver sans prévenir. | astuce du chef, toast "Export généré avec succès" |
| N6 | Vous pouvez aussi le faire depuis Claude : copiez ce prompt, remplacez les crochets. | **réutilisé tel quel** depuis `foodeatup-fournisseurs-tuto/vo/N6.mp3` — étages 1+2 |
| N7 | Collez-le dans la conversation : l'historique de vos températures s'affiche en quelques secondes. | étage 3 (mockup chatbot) |
| N8 | Passez à la restauration intelligente avec FoodEatUp. Essayez gratuitement dès aujourd'hui ! | **réutilisé tel quel** depuis `foodeatup-fournisseurs-tuto/vo/N8.mp3` — carte de fin CTA |

N6/N8 copiés directement (texte générique identique au reste de la série, zéro
crédit ElevenLabs). N0-N5 et N7 à générer pour ce tutoriel une fois le script validé.

## Séquence Claude — module partagé

`mcp__FoodEatUp__list_haccp_temperatures(establishment_id, start_date?, end_date?,
equipment_id?, type?)` — correspond exactement à "sortir l'historique températures",
donnée réelle affichée à l'écran (stats + détail Frigo 1). Prompt (identique côté
vidéo et côté fiche Lovable `claudePrompt`) :

> Sors-moi l'historique des relevés de température de mon établissement FoodEatUp
> (ID [ID établissement]) du [date début] au [date fin].

Réponse assistant (étage 3, mockup) : "Bien sûr ! Sur cette période : 19 911 relevés,
14 504 conformes, 95 non conformes. Le Frigo 1 est actuellement à 13,0 °C…" — reprend
les vraies données affichées dans le rush, pas des chiffres inventés.

Second cas d'usage possible en `claudePrompts[]` (fiche Lovable uniquement, pas
d'étage vidéo dédié — pattern `saisir-ses-ingredients`) :
`mcp__FoodEatUp__list_haccp_tracabilite(establishment_id, status?)` :

> Sors-moi l'historique de traçabilité de mon établissement FoodEatUp
> (ID [ID établissement]).

Pas d'équivalent MCP en lecture pour l'export "Checklist Hygiène" lui-même (seul
`list_hygiene_checklists` existe, lit les modèles pas l'historique des validations) —
cette action reste donc illustrée à l'écran mais hors séquence Claude, comme pour
d'autres tutos où une capacité UI n'a pas d'outil MCP correspondant.

## Astuce du chef (Lovable, `chefTip`)

"Exportez votre historique HACCP régulièrement (température, traçabilité, réception,
nettoyage) : en cas de contrôle sanitaire, vous sortez un classeur complet et à jour
en quelques clics, au lieu de chercher vos papiers la veille."

## Cas d'usage (Lovable, `howItWorks` / `whatItsFor`)

- **Comment ça marche** : Ouvrez Historique depuis le menu principal → choisissez le
  module (Températures, Traçabilité, Contrôle à réception, Plan de nettoyage,
  Checklist Hygiène, Étiqueteuse, Production) → filtrez par date/équipement/statut si
  besoin → cliquez sur Exporter (CSV, PDF rapide, email, ou multi-format selon le
  module) → votre export est généré en quelques secondes.
- **À quoi ça sert** : centraliser tout l'historique HACCP de l'établissement et
  pouvoir le sortir en un clic pour un contrôle sanitaire, un audit interne, ou pour
  garder une trace archivée sans ressaisie papier.

## Statut publication

DRAFT — script à valider avant génération VO (ElevenLabs) et montage. Une fois
validé : build.py (calibration zoom-punch/bandeaux sur coordonnées mesurées),
livraison `SendUserFile` pour validation finale, puis (après OK) RapidoCMS +
LinkedIn + Lovable (`foodeatup-haccp-export-tuto`, module `haccp`, slug
`exporter-son-classeur-haccp`).
