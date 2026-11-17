#!/usr/bin/env bash
# Données de démo de la téléphonie (copie de tournage, mode simulé) : compte Twilio factice, historique d'appels.
cd /home/user/rapido-crm-film && php artisan tinker --execute="require '/home/user/video/tutoriels-rapido/_gabarit/telephonie-demo.php';"
