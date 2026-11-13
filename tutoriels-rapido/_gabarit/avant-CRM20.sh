#!/usr/bin/env bash
# CRM20 : campagnes, modèles d'e-mail et domaines d'activité de démo (copie de tournage uniquement).
G="$(cd "$(dirname "$0")" && pwd)"; DB=/home/user/rapido-crm-film/database/database.sqlite
php "$G/contrats-demo.php" "$DB"; php "$G/domaines-demo.php" "$DB"; php "$G/campagnes-demo.php" "$DB"
