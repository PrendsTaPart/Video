#!/usr/bin/env bash
# CRM04 enregistre des établissements trouvés par la prospection Maps simulée : on retire ceux de la prise précédente
# (base SQLite de la COPIE DE TOURNAGE /home/user/rapido-crm-film, jamais le dépôt).
php -r '$d=new PDO("sqlite:/home/user/rapido-crm-film/database/database.sqlite");
$noms=["Le Fournil Gourmand","Boulangerie des Capucins","Maison Dorée","Au Pain de Saint-Michel","La Mie des Chartrons","Boulangerie du Jardin Public","L'"'"'Épi Bordelais","Pains & Merveilles","Le Pétrin de Bacalan","Fournée Chartronnaise","La Tradition du Pont","Douceurs de la Bastide"];
$st=$d->prepare("delete from entreprises where lower(nom)=lower(?)"); $n=0; foreach($noms as $x){$st->execute([$x]); $n+=$st->rowCount();} echo "$n établissement(s) de démo retiré(s)\n";'
pgrep -f mock-n8n.cjs >/dev/null || (nohup node "$(dirname "$0")/mock-n8n.cjs" > /tmp/claude-0/mock-n8n.log 2>&1 &)
