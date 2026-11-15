#!/usr/bin/env bash
# Remet le site de démo « Studio Lumière » sans domaine personnel (CRM51 en ajoute un pendant le tournage).
cd /home/user/rapido-crm-film && php artisan tinker --execute='App\Models\Site::where("company_id", 1)->update(["domaine" => null, "domaine_statut" => "aucun", "domaine_jeton" => null, "domaine_hebergeur" => null, "domaine_diagnostic" => null, "domaine_verifie_le" => null]); echo "site sans domaine\n";'
