#!/usr/bin/env bash
# CRM13 (factures) : lignes et échéances fictives, relances des factures désactivées avant le tournage.
cd /home/user/rapido-crm-film && php artisan tinker --execute="require '/home/user/video/tutoriels-rapido/_gabarit/factures-demo.php';"
