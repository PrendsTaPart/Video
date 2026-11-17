#!/usr/bin/env bash
# CRM83 (facture électronique Factur-X) : facture de démo complète, numéro de TVA de la société vidé.
cd /home/user/rapido-crm-film && php artisan tinker --execute="require '/home/user/video/tutoriels-rapido/_gabarit/facturx-demo.php';"
