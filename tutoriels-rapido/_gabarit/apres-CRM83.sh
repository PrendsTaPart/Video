#!/usr/bin/env bash
# Après CRM83 : remet la démo dans son état initial (TVA vidée) pour un éventuel retournage.
cd /home/user/rapido-crm-film && php artisan tinker --execute="require '/home/user/video/tutoriels-rapido/_gabarit/facturx-demo.php';"
