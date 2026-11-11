# Pont MCP

Les serveurs MCP sont des outils de **Claude Code**, pas des dépendances Node.
Un script `tsx` ne peut donc pas les appeler lui-même. Le pipeline utilise un
protocole de fichiers, dans `content/<module>/<Vxx>/mcp/` :

```
<serveur>.<outil>.<cle>.demande.json   ← écrit par le pipeline, décrit l'appel
<serveur>.<outil>.<cle>.reponse.json   ← écrit par Claude Code, contient le résultat
```

Quand une réponse manque, la commande s'arrête avec le message
`Appel MCP requis — <serveur> › <outil>` et le chemin des deux fichiers.
Claude Code exécute l'outil, dépose le JSON brut dans le fichier de réponse, puis
relance la même commande : elle reprend sans refaire ce qui est déjà fait.

Chaque réponse est validée par un schéma zod avant usage — une réponse
inattendue arrête le pipeline plutôt que de contaminer la fiche ou le script.

## Serveurs

| Serveur | Outils utilisés |
|---|---|
| `RapidoCRM` | inventaire des outils, schémas de paramètres, `list_*` / `get_*` en lecture seule |
| `RapidoCMS` | `upload_file_tool`, `list_all_files` |
| `YouTube` | `get_channel_status`, `switch_channel`, `publish_video`, `get_video_status`, `retry_video` |
| `RapidoCMS tutoriels` | `creer_tutoriel`, `enregistrer_*`, `ajouter_*`, `configurer_agent_tutoriel`, `publier_tutoriel`, `tutoriels_incomplets` |

## Rappel

Aucune écriture dans RapidoCRM depuis ce pipeline. Les appels au serveur
`RapidoCRM` servent à **comprendre** le logiciel, jamais à le modifier.
