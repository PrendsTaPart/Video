#!/usr/bin/env bash
# Remet le site de démo sans sous-domaine d'envoi (CRM52 en configure un pendant le tournage).
cd /home/user/rapido-crm-film && php artisan tinker --execute='App\Models\Site::where("company_id", 1)->update(["email_domaine" => null, "email_statut" => "aucun", "email_selecteur" => null, "email_cle_privee" => null, "email_cle_publique" => null, "email_diagnostic" => null, "email_verifie_le" => null]); echo "site sans sous-domaine d envoi\n";'
