#!/bin/bash
# RH22 (routines) : l'employé IA coordinateur doit être actif (clé IA fictive, aucun appel réel pendant le tournage).
psql "postgresql://rapidorh_test:test_password@127.0.0.1/rapidorh_dev" -qAt -c "update agent_configs ac set agent_status='active', monthly_token_budget=500000 from agent_templates t where t.id=ac.agent_template_id and t.template_id='rrh-coordinateur' and ac.company_id=(select company_id from users where email='camille@studio-demo.test')" >/dev/null
