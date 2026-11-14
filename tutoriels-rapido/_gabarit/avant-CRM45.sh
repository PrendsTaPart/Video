#!/usr/bin/env bash
# CRM45 : pipeline de démo avec opportunités qui stagnent (copie de tournage uniquement).
G="$(cd "$(dirname "$0")" && pwd)"; DB=/home/user/rapido-crm-film/database/database.sqlite
php "$G/pipeline-demo.php" "$DB"; php "$G/pipeline-inactivite-demo.php" "$DB"
