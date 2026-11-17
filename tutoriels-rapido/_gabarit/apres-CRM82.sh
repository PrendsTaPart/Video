#!/usr/bin/env bash
# CRM82 : la double authentification activée pendant le tournage est retirée du compte de démonstration
# (sinon les tournages suivants ne peuvent plus se connecter).
cd /home/user/rapido-crm-film && php artisan tinker --execute='App\Models\User::where("email", "demo@rapido.test")->update(["deux_facteurs_secret" => null, "deux_facteurs_codes_secours" => null, "deux_facteurs_active_le" => null]); echo "2FA retirée\n";'
