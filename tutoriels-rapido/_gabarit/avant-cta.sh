#!/usr/bin/env bash
# Données des tutoriels CTA (CRM48, CRM49) + site fictif servi sur le port 8131.
php "$(dirname "$0")/cta-demo.php" /home/user/rapido-crm-film/database/database.sqlite
if ! curl -s -o /dev/null http://127.0.0.1:8131/; then
  (cd "$(dirname "$0")/site-demo" && nohup python3 -m http.server 8131 --bind 127.0.0.1 > /tmp/claude-0/site-demo.log 2>&1 &)
  sleep 1
fi
