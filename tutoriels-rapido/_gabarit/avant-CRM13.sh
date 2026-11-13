#!/usr/bin/env bash
# CRM13 : lignes de devis/factures de démo (copie de tournage uniquement).
php "$(dirname "$0")/facturation-demo.php" /home/user/rapido-crm-film/database/database.sqlite
