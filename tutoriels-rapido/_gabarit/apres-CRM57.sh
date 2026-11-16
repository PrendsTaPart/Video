#!/usr/bin/env bash
# Tunnel de démo de CRM57 (créé par TunnelVenteService, comme l outil MCP creer_tunnel_de_vente) : recréé à l identique.
cd /home/user/rapido-crm-film && php artisan tinker --execute="require '/home/user/video/tutoriels-rapido/_gabarit/tunnel-demo.php';"
