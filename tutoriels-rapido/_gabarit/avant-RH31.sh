#!/bin/bash
# RH31 (suivre ses employés IA) : le planificateur éditorial est actif (bouton « Suspendre » visible). Aucun appel IA réel.
psql "postgresql://rapidorh_test:test_password@127.0.0.1/rapidorh_dev" -qAt -c "update agent_configs ac set agent_status='active', monthly_token_budget=200000 from agent_templates t where t.id=ac.agent_template_id and t.template_id='rrh-planificateur-editorial' and ac.company_id=(select company_id from users where email='camille@studio-demo.test')" >/dev/null
