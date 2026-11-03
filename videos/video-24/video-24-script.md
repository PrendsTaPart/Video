# Vidéo 24 — « J'ai créé mon propre logiciel de recrutement avec des agents IA ! »

Durée : 85 s · 1080×1920 · voix ElevenLabs Noé (eleven_v4) · sous-titres incrustés · musique + effets sonores de la série.

Le script du brief a été adapté au code réel. Les modules d'entretien sont présentés comme « codés, en test ». Le score est présenté comme une aide au tri, jamais comme une décision. Le canal WhatsApp n'est pas montré (régression signalée par la PR #8).

## Voix off

Aujourd'hui, je vais te montrer comment j'ai créé mon propre logiciel de recrutement avec l'intelligence artificielle.
Parce que quand tu gères plusieurs entreprises, recruter peut vite devenir compliqué.
Les offres, les CV, les entretiens, les relances… tout finit par être dispersé.
Alors, j'ai développé RapidoATS.
Imagine : je dois recruter un développeur pour BraindCode et un commercial pour FoodEatUp.
Les deux recrutements sont au même endroit, mais les données de chaque entreprise restent séparées.
Je renseigne le poste, les compétences et les missions, et l'IA m'aide à rédiger l'offre à partir de la base de connaissances de l'entreprise.
Quand un CV arrive, RapidoATS l'analyse, extrait les compétences et calcule un score d'aide à la présélection.
Ce score m'aide à trier. Il ne dit rien de la valeur d'une personne.
Je retrouve les candidats dans mon tableau de suivi : nouveau, en analyse, entretien, en attente, retenu ou refusé.
Et c'est toujours un humain qui décide.
Pour les entretiens, le code prévoit la planification, la transcription, un rapport, et même un entretien avec avatar.
Je les teste encore avant de les ouvrir à mes équipes.
Mais ce qui m'intéresse surtout, c'est l'architecture.
Le cerveau, c'est FastAPI et FastMCP. Les mains, ce sont les workflows n8n. Le cloud, c'est Supabase.
Mes agents IA passent par des outils MCP, et chaque écriture attend une confirmation.
Publier une offre ou lancer un onboarding ? Jamais sans mon accord.
Avant, je gérais mes recrutements avec plusieurs outils. Maintenant, je construis mon propre système de recrutement assisté par IA.
Et toi, tu laisserais une IA t'aider à organiser tes recrutements ?

## Écarts avec le brief

- « Présélectionné » n'existe pas dans le code : on montre les six statuts réels de `src/pages/Candidatures.tsx` (Nouveau, En analyse, Entretien, En attente, Retenu, Refusé).
- La publication Indeed/LinkedIn n'est pas présentée comme opérationnelle, car elle n'a pas été testée.
- L'onboarding RapidoRH n'est pas présenté comme automatisé (`RAPIDORH_MODE=pending`, file non drainée).
