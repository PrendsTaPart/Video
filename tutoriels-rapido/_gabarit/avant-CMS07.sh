#!/usr/bin/env bash
# CMS07 filme la génération d'une clé d'API : on part d'un tableau vide (base SQLite LOCALE).
php -r '$d=new PDO("sqlite:/home/user/rapido-cms/database/database.sqlite"); echo $d->exec("delete from cms_user_access_tokens"), " clé(s) de démo supprimée(s)\n";'
