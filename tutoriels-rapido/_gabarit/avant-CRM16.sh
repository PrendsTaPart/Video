#!/usr/bin/env bash
# CRM16 : retire le modèle « Contrat de shooting photo » créé par une prise précédente (copie de tournage uniquement).
php -r '$d = new PDO("sqlite:/home/user/rapido-crm-film/database/database.sqlite"); echo $d->exec("delete from contrat_crm where user_id = 1 and titre in ('"'"'Contrat de shooting photo'"'"', '"'"'Shooting photo'"'"')"), " modèle(s) de prise précédente retiré(s)\n";'
