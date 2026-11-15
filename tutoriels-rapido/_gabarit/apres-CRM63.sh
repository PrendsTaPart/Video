#!/usr/bin/env bash
# Séquences de démo (CRM63 en crée une et inscrit les prospects chauds pendant le tournage) : remise à zéro.
cd /home/user/rapido-crm-film && php artisan tinker --execute="require '/home/user/video/tutoriels-rapido/_gabarit/sequences-demo.php';"
