#!/usr/bin/env bash
# CRM73 (agent IA du site) : base réindexée, FAQ « horaires » retirée, simulations effacées.
cd /home/user/rapido-crm-film && php artisan tinker --execute="require '/home/user/video/tutoriels-rapido/_gabarit/agent-site-demo.php';"
