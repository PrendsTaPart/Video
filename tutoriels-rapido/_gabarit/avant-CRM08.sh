#!/usr/bin/env bash
# CRM08 : agent vocal non configuré au départ (copie de tournage uniquement).
php -r '$d=new PDO("sqlite:/home/user/rapido-crm-film/database/database.sqlite"); $d->exec("delete from agent_vocal_produits"); echo $d->exec("delete from agent_vocal_configs"), " configuration(s) retirée(s)\n";'
