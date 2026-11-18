#!/usr/bin/env bash
# CRM53 (éditeur : sections et modèles) : retire le design enregistré lors d'une prise précédente.
cd /home/user/rapido-crm-film && php artisan tinker --execute="echo DB::table('mes_templates_crm')->where('name', 'La Table de Marius — site')->delete().' design(s) retiré(s)';"
