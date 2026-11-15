#!/usr/bin/env bash
# CRM59 montre l'adresse du serveur MCP : la copie de tournage affiche l'adresse de production le temps du tournage.
cd /home/user/rapido-crm-film && sed -i '/^MCP_HUB_URL=/d' .env && echo 'MCP_HUB_URL=https://crm.rapidosoftware.com/mcp' >> .env && echo "MCP_HUB_URL de production (tournage)"
