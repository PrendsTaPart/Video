#!/usr/bin/env bash
# CRM44 : relances automatiques et suivi des devis de démo (copie de tournage uniquement).
G="$(cd "$(dirname "$0")" && pwd)"; DB=/home/user/rapido-crm-film/database/database.sqlite
php "$G/facturation-demo.php" "$DB"; php "$G/relances-demo.php" "$DB"
