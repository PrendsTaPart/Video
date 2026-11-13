#!/usr/bin/env bash
# CRM23 : workflows de démo (copie de tournage uniquement).
G="$(cd "$(dirname "$0")" && pwd)"
cd /home/user/rapido-crm-film && php artisan tinker --execute="require '$G/workflows-demo.php';"
