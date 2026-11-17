#!/usr/bin/env bash
# CRM86 (appels → analyse de réunion) : appels fictifs de l'agent vocal IA, réglages remis à zéro.
cd /home/user/rapido-crm-film && php artisan tinker --execute="require '/home/user/video/tutoriels-rapido/_gabarit/appels-ia-demo.php';"
