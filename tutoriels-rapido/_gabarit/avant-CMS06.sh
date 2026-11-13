#!/usr/bin/env bash
# CMS06 filme la création d'une marque : on part d'une liste vide (base SQLite LOCALE, entreprise de démo n° 1).
php -r '$d=new PDO("sqlite:/home/user/rapido-cms/database/database.sqlite"); echo $d->exec("delete from cms_marque where entreprise_id = 1"), " marque(s) de démo supprimée(s)\n";'
