#!/usr/bin/env bash
# Doublons de démo (CRM62 fusionne pendant le tournage) : recrée les doublons et remet les fiches d'origine.
cd /home/user/rapido-crm-film && php artisan tinker --execute="require '/home/user/video/tutoriels-rapido/_gabarit/doublons-demo.php';"
