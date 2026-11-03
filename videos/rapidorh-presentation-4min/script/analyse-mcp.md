# Analyse du MCP RapidoRH — outils réels par famille

**Serveur** : `https://rh.rapidosoftware.com/mcp/rapidorh` · company_id 321.
**Compatible IA** : Claude · Mistral · OpenAI (connecteur MCP neutre).
⚠️ **Sécurité** : l'IA agit avec **vos droits d'administrateur** → réserver l'accès MCP aux personnes habilitées.
Interface **admin** (cette vidéo) ≠ interface **collaborateur** (daily, congés, agenda, pointage sur son périmètre).

## 1) Organisation (rôles · permissions · départements)
- `get-roles-list-tool` — 4 profils de base (Admin/Chef/Membre/Client) + rôles personnalisés
- `get-permissions-list-tool` — permissions par module
- `create-role-tool` — créer un rôle (Manager/RH/Comptable…)
- `get-departments-list-tool` — **lecture seule** (départements créés sur le **web**, l'IA les consulte)

## 2) Équipe (utilisateurs)
- `create-user-tool` (envoi **automatique** de l'invitation email) · `update-user-tool` · `delete-user-tool` · `get-users-list-tool`

## 3) Projets
- `create-project-tool` · `get-projects-list-tool`
- `create-project-link-tool` · `update-project-link-tool` · `delete-project-link-tool` · `get-project-links-tool`
- `get-project-documents-tool` · `get-project-tasks-tool`

## 4) Tâches & Kanban
- `create-task-tool` (priorité, dates, membre) · `move-task-tool` (Todo→Doing→Done)
- `create-task-list-tool` · `get-task-lists-tool` — colonnes Kanban générées automatiquement

## 5) Quotidien
- `create-daily-tool` · `get-dailies-tool`
- *Congés & pointages* : renseignés par les **collaborateurs** depuis leur interface ; l'admin supervise.

---
**Lower-thirds (fonctionnalité · outils)** :
Organisation → `get-roles-list-tool · create-role-tool` · Équipe → `create-user-tool` ·
Projets → `create-project-tool` · Kanban → `create-task-tool · move-task-tool` · Quotidien → `create-daily-tool · get-dailies-tool`.
