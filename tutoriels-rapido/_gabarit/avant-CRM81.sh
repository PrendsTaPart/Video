#!/usr/bin/env bash
# CRM81 (portail client) : données fictives de Maison Lafitte et lien magique signé.
mkdir -p /home/user/video/tutoriels-rapido/CRM81
cd /home/user/rapido-crm-film && php artisan tinker --execute="require '/home/user/video/tutoriels-rapido/_gabarit/portail-demo.php';"
