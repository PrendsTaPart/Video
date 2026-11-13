#!/usr/bin/env bash
# CRM21 : segments de démo (copie de tournage uniquement).
G="$(cd "$(dirname "$0")" && pwd)"; DB=/home/user/rapido-crm-film/database/database.sqlite
php "$G/domaines-demo.php" "$DB"
cd /home/user/rapido-crm-film && php artisan tinker --execute="require '$G/segments-demo.php';"
