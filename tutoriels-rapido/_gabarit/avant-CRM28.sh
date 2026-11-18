#!/usr/bin/env bash
# CRM28 (sondages v2) : sondage de démonstration avec réponses fictives, sondage de la prise précédente retiré.
cd /home/user/rapido-crm-film && php artisan tinker --execute="require '/home/user/video/tutoriels-rapido/_gabarit/sondages-demo.php';"
