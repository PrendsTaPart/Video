#!/usr/bin/env bash
# CRM14 : articles de dépense de démo (copie de tournage uniquement).
php "$(dirname "$0")/depenses-demo.php" /home/user/rapido-crm-film/database/database.sqlite
