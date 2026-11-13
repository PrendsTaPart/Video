#!/usr/bin/env bash
# CRM15 : contrats envoyés + modèles d'e-mail de démo, et lien signé de la page de signature
# (copie de tournage uniquement).
G="$(cd "$(dirname "$0")" && pwd)"; F=/home/user/rapido-crm-film
php "$G/contrats-demo.php" "$F/database/database.sqlite"
cd "$F" && php artisan tinker --execute="URL::forceRootUrl('http://127.0.0.1:8124'); echo parse_url(\$u = URL::temporarySignedRoute('admin.contrat.signature', now()->addDays(2), ['id' => 9003, 'entreprise_id' => 3]), PHP_URL_PATH).'?'.parse_url(\$u, PHP_URL_QUERY);" > "$G/../CRM15/lien-signature.txt"
cat "$G/../CRM15/lien-signature.txt"
