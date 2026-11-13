#!/usr/bin/env bash
# CRM24 : retire le formulaire « Demande de devis » d une prise précédente (copie de tournage uniquement).
php -r '$d = new PDO("sqlite:/home/user/rapido-crm-film/database/database.sqlite"); echo $d->exec("delete from forms_crm where user_id = 1 and nom = \"Demande de devis\""), " formulaire(s) retiré(s)\n";'
