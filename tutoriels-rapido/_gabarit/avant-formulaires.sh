#!/usr/bin/env bash
# Données des tutoriels formulaires (CRM24, CRM46, CRM47) + site fictif servi sur le port 8131.
php "$(dirname "$0")/formulaires-demo.php" /home/user/rapido-crm-film/database/database.sqlite "${1:-}"
if ! curl -s -o /dev/null http://127.0.0.1:8131/; then
  (cd "$(dirname "$0")/site-demo" && nohup python3 -m http.server 8131 --bind 127.0.0.1 > /tmp/claude-0/site-demo.log 2>&1 &)
  sleep 1
fi
