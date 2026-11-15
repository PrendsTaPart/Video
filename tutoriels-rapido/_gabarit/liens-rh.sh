#!/bin/bash
# Écrit dans <EP>/ les chemins qui dépendent des identifiants de la base de démonstration (lus par record.cjs via goto_file).
EP="$1"; DB="postgresql://rapidorh_test:test_password@127.0.0.1/rapidorh_dev"
Q(){ psql "$DB" -tAc "$1"; }
CID=$(Q "select company_id from users where email='camille@studio-demo.test'")
P=$(Q "select id from projects where company_id=$CID and name='Boutique en ligne'")
A=$(Q "select id from users where company_id=$CID and first_name='Planificateur éditorial'")
cd "$(dirname "$0")/.."
echo "/projects/$P/tasks" > "$EP/boutique-taches.txt"
echo "/projects/$P/details" > "$EP/boutique-details.txt"
echo "/agents/$A" > "$EP/agent.txt"
