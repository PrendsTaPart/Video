#!/bin/bash
D="$(cd "$(dirname "$0")" && pwd)"  # dossier des sources (seed_demo.php, seed_v2_ui.cjs)
# Archive l'entreprise de démonstration fictive précédente (l'historique ATS est en ajout seul,
# on ne la supprime pas) puis recrée une démo neuve et les données des épisodes.
psql "postgresql://rapidorh_test:test_password@127.0.0.1/rapidorh_dev" -q -v ON_ERROR_STOP=1 <<SQL
BEGIN;
CREATE TEMP TABLE c AS SELECT company_id AS id FROM users WHERE email = 'camille@studio-demo.test';
UPDATE users SET email = 'archive-' || id || '-' || email WHERE company_id IN (SELECT id FROM c);
UPDATE ats_career_pages SET slug = 'archive-' || id || '-' || slug WHERE company_id IN (SELECT id FROM c);
UPDATE roles SET name = name || ' ' || company_id WHERE company_id IN (SELECT id FROM c);
UPDATE departments SET name = name || ' ' || company_id WHERE company_id IN (SELECT id FROM c);
UPDATE companies SET name = name || ' [archivée]' WHERE id IN (SELECT id FROM c);
COMMIT;
SQL
cd "${RAPIDORH_DIR:-/home/user/rapido-RH}" && php artisan cache:clear -q && php "$D"/seed_demo.php && node "$D"/seed_v2_ui.cjs http://127.0.0.1:8000
