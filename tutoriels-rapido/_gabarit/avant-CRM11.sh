#!/usr/bin/env bash
# CRM11 : taux de TVA de démo (copie de tournage uniquement).
php "$(dirname "$0")/tva-demo.php" /home/user/rapido-crm-film/database/database.sqlite
