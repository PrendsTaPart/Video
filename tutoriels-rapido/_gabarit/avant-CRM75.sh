#!/usr/bin/env bash
# CRM75 : aucune carte au départ (l'épisode crée la sienne depuis un modèle).
cd /home/user/rapido-crm-film && php artisan tinker --execute="\$mode = 'CRM75'; require '/home/user/video/tutoriels-rapido/_gabarit/marketing-map-demo.php';"
