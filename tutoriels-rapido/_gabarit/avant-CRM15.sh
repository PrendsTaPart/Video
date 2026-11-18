#!/usr/bin/env bash
# CRM15 (contrats v2) : contrats de démonstration (à signer, signé, vu, refusé) et lien de signature signé.
cd /home/user/rapido-crm-film && php artisan tinker --execute="require '/home/user/video/tutoriels-rapido/_gabarit/contrats-demo.php';"
