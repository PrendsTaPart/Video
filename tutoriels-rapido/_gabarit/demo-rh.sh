#!/bin/bash
# Réinitialise l'entreprise de démonstration fictive de RapidoRH (base LOCALE de développement uniquement) puis la recharge.
# Supprime toutes les lignes portant le company_id de « Studio Démo (fictif) » (contraintes suspendues le temps de la transaction).
set -e
DB="postgresql://rapidorh_test:test_password@127.0.0.1/rapidorh_dev"
case "$DB" in *127.0.0.1*) ;; *) echo "base non locale : refus"; exit 1;; esac
psql "$DB" -q -v ON_ERROR_STOP=1 <<'SQL'
BEGIN;
SET LOCAL session_replication_role = replica;
DO $$
DECLARE cid bigint[]; t text;
BEGIN
  SELECT array_agg(company_id) INTO cid FROM users WHERE (email = 'camille@studio-demo.test' OR email LIKE '%@atelier-demo.test') AND company_id IS NOT NULL;
  DELETE FROM users WHERE email LIKE '%@atelier-demo.test' AND company_id IS NULL; -- inscription interrompue (tutoriel 1)
  IF cid IS NULL THEN RETURN; END IF;
  DELETE FROM role_permission WHERE role_id IN (SELECT id FROM roles WHERE company_id = ANY(cid));
  DELETE FROM appointment_participants WHERE appointment_id IN (SELECT a.id FROM appointments a JOIN users u ON u.id = a.organizer_id WHERE u.company_id = ANY(cid));
  DELETE FROM appointments WHERE organizer_id IN (SELECT id FROM users WHERE company_id = ANY(cid));
  DELETE FROM leave_requests WHERE user_id IN (SELECT id FROM users WHERE company_id = ANY(cid));
  DELETE FROM daily_tasks WHERE daily_id IN (SELECT d.id FROM dailies d JOIN users u ON u.id = d.user_id WHERE u.company_id = ANY(cid));
  DELETE FROM dailies WHERE user_id IN (SELECT id FROM users WHERE company_id = ANY(cid));
  DELETE FROM tasks WHERE project_id IN (SELECT id FROM projects WHERE company_id = ANY(cid));
  DELETE FROM task_lists WHERE project_id IN (SELECT id FROM projects WHERE company_id = ANY(cid));
  FOR t IN SELECT table_name FROM information_schema.columns WHERE column_name = 'company_id' AND table_schema = 'public' AND table_name <> 'users' LOOP
    EXECUTE format('DELETE FROM %I WHERE company_id = ANY($1)', t) USING cid;
  END LOOP;
  DELETE FROM users WHERE company_id = ANY(cid);
  DELETE FROM companies WHERE id = ANY(cid);
END $$;
COMMIT;
SQL
HERE="$(dirname "$(readlink -f "$0")")"
cd /home/user/rapido-RH && php "$HERE/demo-rh.php"
