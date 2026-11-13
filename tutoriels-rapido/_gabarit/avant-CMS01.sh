#!/usr/bin/env bash
# CMS01 filme une inscription complète : on supprime le compte fictif de la prise précédente (base LOCALE).
php "$(dirname "$0")/reset-cms01.php" /home/user/rapido-cms/database/database.sqlite
