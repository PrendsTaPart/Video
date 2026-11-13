#!/usr/bin/env bash
# CMS08 : comptes de réseaux fictifs + liste de publications vide (base SQLite LOCALE).
php "$(dirname "$0")/reseaux-demo.php" /home/user/rapido-cms/database/database.sqlite ajouter
php -r '$d=new PDO("sqlite:/home/user/rapido-cms/database/database.sqlite"); echo $d->exec("delete from cms_posts where entreprise_id = 1"), " publication(s) de démo supprimée(s)\n";'
