#!/usr/bin/env bash
# Retire l'adresse de production posée par avant-CRM59.sh.
cd /home/user/rapido-crm-film && sed -i '/^MCP_HUB_URL=/d' .env && echo "MCP_HUB_URL retiré"
