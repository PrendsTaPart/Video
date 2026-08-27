# Lot Configuration V06–V13 — état de publication

## Publiés

| Tutoriel | Durée | Bibliothèque | Page Académie | LinkedIn | YouTube |
|---|---|---|---|---|---|
| V06 Configurer son IMAP | 80 s | ✅ 4 médias | ✅ en ligne | 29/08 16 h | **manquant** |
| V07 Configurer son IA | 82 s | ✅ 4 médias | ✅ en ligne | 30/08 07 h | **manquant** |
| V09 Configurer Stripe | 80 s | ✅ 4 médias | ✅ en ligne | 30/08 16 h | **manquant** |

Pages : `/tutoriel/01-configurer-son-imap`, `/tutoriel/01-configurer-son-ia`,
`/tutoriel/01-configurer-stripe` sur tutoriel.rapidocrm.com.

## Ce qu'il reste à faire

### YouTube — trois vidéos et trois Shorts

Le MCP YouTube s'est déconnecté en cours de session. Les six liens manquent
donc sur les pages. Une fois le connecteur rouvert :

1. `publish_video` sur le master 16:9 puis sur le 9:16, à partir des liens S3 ;
2. `enregistrer_youtube` sur chacun des trois slugs.

Rien d'autre n'est à refaire : les pages sont complètes par ailleurs.

### V10, V11, V13 — la voix manque

La synthèse ElevenLabs est tombée en cours de lot : après 27 blocs réussis,
tout revient en « Failed to generate audio », y compris sur des tentatives
isolées et espacées. L'estimation préalable passe sans erreur bloquante, donc
la configuration est saine — reste le solde de crédits du workspace, à
vérifier côté compte.

Manquent 26 blocs : 4 sur V10, 11 sur V11, 11 sur V13. Les textes sont dans
les `script.json`. `voix-sessions-lot2.json` garde la correspondance
bloc → session ; le cache mutualisé d'`assets/voix-cache/` empêche toute
resynthèse en double.

Une fois les voix déposées dans `voix/`, la suite est mécanique :
`npm run rendu`, `npm run vignette`, `npm run qa`, puis la publication.
