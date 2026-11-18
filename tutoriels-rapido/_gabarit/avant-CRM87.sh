#!/usr/bin/env bash
# CRM87 (toute la communication d un client) : même jeu de données que CRM74 (boîte de réception et tickets remis à zéro).
cd /home/user/rapido-crm-film && php artisan tinker --execute="require '/home/user/video/tutoriels-rapido/_gabarit/tickets-demo.php';"
