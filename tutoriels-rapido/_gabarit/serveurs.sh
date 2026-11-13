#!/usr/bin/env bash
# Relance les serveurs locaux de tournage (après un redémarrage du conteneur).
#   8124 : copie de tournage RapidoCRM recompilée (/home/user/rapido-crm-film, hors dépôt)
#   8125 : RapidoCMS ; 8126 : RapidoRH (si installé) ; 8199 : n8n simulé
up() { curl -s -o /dev/null -m 3 "http://127.0.0.1:$1/login" && return 0; [ -d "$2" ] || return 0
       (cd "$2" && nohup php artisan serve --port="$1" > "/tmp/claude-0/serve-$1.log" 2>&1 &); }
mkdir -p /tmp/claude-0
up 8124 /home/user/rapido-crm-film
up 8125 /home/user/rapido-cms
up 8126 /home/user/rapido-RH
up 8130 /home/user/rapido-software
pgrep -f mock-n8n.cjs >/dev/null || (nohup node "$(dirname "$0")/mock-n8n.cjs" > /tmp/claude-0/mock-n8n.log 2>&1 &)
sleep 4
for p in 8124 8125 8126; do echo "$p : $(curl -s -o /dev/null -m 5 -w '%{http_code}' http://127.0.0.1:$p/login)"; done
