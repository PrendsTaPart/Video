#!/usr/bin/env bash
# CRM07 : pipeline fictif remis à zéro (copie de tournage uniquement).
php "$(dirname "$0")/pipeline-demo.php" /home/user/rapido-crm-film/database/database.sqlite
