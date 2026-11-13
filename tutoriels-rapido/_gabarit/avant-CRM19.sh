#!/usr/bin/env bash
# CRM19 : campagnes, domaines et modèles de newsletter de démo + vignettes (copie de tournage uniquement).
G="$(cd "$(dirname "$0")" && pwd)"; DB=/home/user/rapido-crm-film/database/database.sqlite
php "$G/domaines-demo.php" "$DB"; php "$G/campagnes-demo.php" "$DB"; php "$G/newsletters-demo.php" "$DB"; node "$G/vignettes-newsletter.cjs"
