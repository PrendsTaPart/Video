#!/usr/bin/env bash
# Scores de démo (CRM64 modifie le barème et le seuil pendant le tournage) : remet le barème par défaut et rejoue les interactions.
cd /home/user/rapido-crm-film && php artisan tinker --execute="require '/home/user/video/tutoriels-rapido/_gabarit/score-demo.php';"
