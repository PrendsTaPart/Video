#!/usr/bin/env python3
"""Génère <EP>/tuto.json pour la série RapidoRH à partir de scripts-rh.json (voix) et des scènes ci-dessous.

Usage : python3 _gabarit/gen-rh.py [EP ...]   (sans argument : tous les épisodes définis ici)
Les chemins qui dépendent des identifiants de la base (projet, agent) sont lus dans des fichiers
écrits par _gabarit/liens-rh.sh juste avant le tournage (goto_file).
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS = json.load(open(os.path.join(ROOT, '_gabarit', 'scripts-rh.json')))

M = '.modal.show'
MODAL = f'{M} .modal-content'
CAMILLE = 'camille@studio-demo.test'
HUGO = 'hugo@studio-demo.test'

# Ordre de la série (le CTA de fin annonce l'épisode suivant).
ORDRE = ['RH01', 'RH02', 'RH03', 'RH04', 'RH05', 'RH06', 'RH07', 'RH08', 'RH09', 'RH10', 'RH11', 'RH12', 'RH14',
         'RH17', 'RH18', 'RH19', 'RH26', 'RH28', 'RH29', 'RH30', 'RH31', 'RH15', 'RH32']
SUIVANT = {  # titre court de l'épisode suivant
    'RH01': 'le tableau de bord', 'RH02': 'ajouter ses collaborateurs', 'RH03': 'les départements',
    'RH04': 'rôles et permissions', 'RH05': 'créer un projet', 'RH06': 'le Kanban', 'RH07': "le détail d'une tâche",
    'RH08': 'documents et liens du projet', 'RH09': 'les dailies', 'RH10': "l'agenda", 'RH11': 'organiser un rendez-vous',
    'RH12': 'les congés', 'RH14': 'les notifications', 'RH17': 'votre abonnement', 'RH18': 'connecter RapidoRH à Claude',
    'RH19': 'les paramètres IA', 'RH26': 'découvrir vos employés IA', 'RH28': 'configurer un employé IA',
    'RH29': 'confier une tâche à un employé IA', 'RH30': 'suivre vos employés IA', 'RH31': "l'espace du collaborateur",
    'RH15': 'demander un congé', 'RH32': 'répondre dans la messagerie',
}

FERMER_MODALE = "document.querySelector('.modal.show .btn-close')?.click()"

EPISODES = {
    'RH01': dict(public=True, type_delay=18, start_path='/register', thumb_shot='fin.png', scenes=[
        dict(at='intro', wait=0.3, zone='form'),
        dict(at='compte', label='Le gérant', fill=[['input[name=first_name]', 'Julie'], ['input[name=last_name]', 'Moreau']],
             fill_now=[['input[name=email]', 'julie@atelier-demo.test'], ['input[name=password]', 'Demo-Tuto-2026!'],
             ['input[name=password_confirmation]', 'Demo-Tuto-2026!']], zone='form'),
        dict(at='entreprise', label="L'entreprise", click='button:has-text("Suivant")', fill=[['input[name=name]', 'Atelier Démo (fictif)']],
             fill_now=[['input[name=email]', 'contact@atelier-demo.test']], zone='form'),
        dict(at='offre', label="L'offre", click='form button[type=submit], button:has-text("Connexion")', wait=0.8, zone='.card:has-text("Essai Gratuit")'),
        dict(at='outro', hover='button:has-text("Commencer l\'essai gratuit")', zone='.card:has-text("Essai Gratuit")'),
    ]),
    'RH02': dict(start_path='/dashboard', scenes=[
        dict(at='intro', wait=0.3),
        dict(at='projets', label='Vos projets', zone=[380, 110, 1420, 230]),
        dict(at='equipe', label="L'équipe qui avance", zone=[380, 330, 1420, 210]),
        dict(at='taches', label='Répartition des tâches', select=[['select.form-select-sm', 'Boutique en ligne']], zone='Répartition des tâches'),
        dict(at='stats', label='Statistiques des projets', scroll='Statistique des projets', fill=[['input[placeholder="Chercher un projet..."]', 'Boutique']], zone='Statistique des projets'),
        dict(at='outro', top=True),
    ]),
    'RH03': dict(start_path='/users', type_delay=18, scenes=[
        dict(at='intro', wait=0.3, zone='table'),
        dict(at='liste', label='Humains et agents IA', click='button:has-text("Agents IA")', zone='table'),
        dict(at='liste', click='button:has-text("Humains")', wait=0.6),
        dict(at='ajouter', label='Ajouter un utilisateur', click='a:has-text("Ajouter un utilisateur")', fill=[
            [f'{M} input[placeholder="Entrer un nom"]', 'Robert'], [f'{M} input[placeholder="Entrer un prénom"]', 'Emma'],
            [f'{M} input[placeholder="Entrer une adresse e-mail"]', 'emma@studio-demo.test']],
            fill_now=[[f'{M} input[placeholder="Entrer un nom d\'utilisateur"]', 'emma.robert'], [f'{M} input[placeholder="Entrer un numéro de téléphone"]', '0600000000']],
            select=[[f'{M} select:has(option:text("Collaborateur"))', 'Collaborateur'], [f'{M} select:has(option:text("Marketing"))', 'Marketing']], zone=MODAL),
        dict(at='contrat', label='Heures, salaire, congés', fill_now=[[f'{M} input[placeholder="Entrer nombre d\'heures"]', '35'],
             [f'{M} input[placeholder="Entrer un salaire"]', '2400'], [f'{M} input[placeholder="Entrer nombre de jours"]', '25']], zone=MODAL),
        dict(at='outro', label="L'invitation", click=f'{M} button:has-text("Ajouter")', wait=1.2, zone='table'),
    ]),
    'RH04': dict(start_path='/departments', scenes=[
        dict(at='intro', wait=0.3, zone='table'),
        dict(at='liste', label='Vos départements', zone='table'),
        dict(at='ajouter', label='Ajouter un département', click='button:has-text("Ajouter un département")',
             fill=[[f'{M} input[placeholder="Entrer un nom"]', 'Service client']], zone=MODAL),
        dict(at='ajouter', click=f'{M} button:has-text("Ajouter")', wait=1.0),
        dict(at='ajouter', wait=0.6, zone='table'),
        dict(at='rattacher', label='Rattacher un collaborateur', goto='/users', click='tr:has-text("Hugo Martin") button.me-2'),
        dict(at='rattacher', click='.dropdown-menu.show a:has-text("Modifier")', wait=0.6),
        dict(at='rattacher', select=[[f'{M} select:has(option:text("Service client"))', 'Service client']], zone=MODAL),
        dict(at='outro', eval=FERMER_MODALE, wait=0.2),
    ]),
    'RH05': dict(start_path='/roles', scenes=[
        dict(at='intro', wait=0.3, zone='table'),
        dict(at='liste', label='Les rôles', zone='table'),
        dict(at='ajouter', label='Ajouter un rôle', click='button:has-text("Ajouter un rôle")', fill=[[f'{M} input[placeholder="Entrer un nom"]', 'Chef de projet']], zone=MODAL),
        dict(at='permissions', label='Les permissions', click=f'{M} label:has-text("Voir la liste des projets")'),
        dict(at='permissions', click=f'{M} label:has-text("Voir la liste des tâches")'),
        dict(at='permissions', click=f'{M} label:has-text("Voir la liste des congés")', zone=MODAL),
        dict(at='outro', click=f'{M} button:has-text("Ajouter")', wait=1.0, zone='table'),
    ]),
    'RH06': dict(start_path='/projects', scenes=[
        dict(at='intro', wait=0.3),
        dict(at='liste', label='Vos projets', hover='a:has-text("Créer un projet")', zone=[380, 110, 1420, 700]),
        dict(at='liste', click='a:has-text("Créer un projet")', wait=0.5),
        dict(at='infos', label='Les informations', fill=[['input[placeholder="Entrer un nom"]', 'Site vitrine 2027']], fill_now=[['input[placeholder="Entrer tarif du projet"]', '4500']],
             select=[['select:has(option:text("Sélectionner une priorité"))', {'index': 2}], ['select:has(option:text("Sélectionner une taille du projet"))', {'index': 2}]],
             zone='Information du projet'),
        dict(at='equipe', label="Dates et équipe", fill_now=[['input[type=date] >> nth=0', '2027-01-04'], ['input[type=date] >> nth=1', '2027-03-26']],
             select=[['select:has(option:text("Sélectionner un chef de projet"))', 'Camille Durand']], zone='Information de l’équipe responsable'),
        dict(at='equipe', fill=[['.tagify__input', 'Hugo']], wait=0.4),
        dict(at='equipe', click='.tagify__dropdown__item >> nth=0', wait=0.4),
        dict(at='outro', label='Enregistrer', click='button:has-text("Créer un projet")', wait=1.5, zone=[380, 110, 1420, 520]),
    ]),
    'RH07': dict(start_path='/projects', scenes=[
        dict(at='intro', goto_file='boutique-taches.txt', wait=0.3),
        dict(at='colonnes', label='Les colonnes', hover='button:has-text("Ajouter une colonne")', zone='.kanban-container'),
        dict(at='ajouter', label='Ajouter une tâche', click='.kanban-board:has-text("À faire") .kanban-board-header button',
             fill=[['textarea.add-new-item', 'Rédiger la page À propos']], zone='.kanban-board:has-text("À faire")'),
        dict(at='ajouter', click='.kanban-board button:has-text("Ajouter")', wait=0.8),
        dict(at='deplacer', label='Glisser-déposer', drag=['.kanban-item:has-text("Photos des produits phares")', '.kanban-board:has-text("En cours") .kanban-drag'], zone='.kanban-container'),
        dict(at='outro', wait=0.2, zone='.kanban-container'),
    ]),
    'RH08': dict(start_path='/projects', scenes=[
        dict(at='intro', goto_file='boutique-taches.txt', wait=0.3),
        dict(at='ouvrir', label='Ouvrir une tâche', click='.kanban-item:has-text("Maquette de la page")', zone=MODAL),
        dict(at='champs', label='Statut, priorité, dates', select=[[f'{M} select:has(option:text("Urgent"))', 'Urgent']], hover=f'{M} select:has(option:text("En cours"))', zone=MODAL),
        dict(at='fichiers', label='Description et fichiers', fill=[[f'{M} textarea[placeholder="Ecrire une description"]', 'Proposer deux variantes de la page d\'accueil, version mobile comprise.']],
             hover=f'{M} label:has-text("Parcourir")', zone=MODAL),
        dict(at='outro', label='Confier à un employé IA', hover=f'{M} select[id^=ai-mode]', zone=f'{M} select[id^=ai-mode]', zone_closest='.border, .card, div.mt-4'),
    ]),
    'RH09': dict(start_path='/projects', scenes=[
        dict(at='intro', wait=0.3),
        dict(at='details', label='Le détail du projet', hover='h5:has-text("Boutique en ligne")'),
        dict(at='details', goto_file='boutique-details.txt', wait=0.3),
        dict(at='documents', label='Documents', click='.btn-rect >> nth=0', fill=[[f'{M} input[placeholder="Entrer un nom..."]', 'Cahier des charges']],
             upload=[[f'{M} input[type=file]', 'assets/cahier-des-charges-fictif.pdf']], zone=MODAL),
        dict(at='documents', hover=f'{M} button:has-text("Ajouter")', wait=0.6),
        dict(at='liens', label='Liens utiles', eval=FERMER_MODALE, wait=0.5),
        dict(at='liens', click='.btn-rect >> nth=1', fill=[[f'{M} input[placeholder="Titre descriptif"]', 'Maquette de la page d\'accueil']],
             fill_now=[[f'{M} input[placeholder="https://www.site.com"]', 'https://maquette.studio-demo.test'], [f'{M} textarea[placeholder="Description du lien"]', 'Version 2, validée en réunion']], zone=MODAL),
        dict(at='liens', click=f'{M} button:has-text("Ajouter")', wait=1.0),
        dict(at='outro', zone=[860, 260, 940, 360]),
    ]),
    'RH10': dict(start_path='/dailies', scenes=[
        dict(at='intro', wait=0.3, zone='table'),
        dict(at='liste', label='Jour après jour', zone='table'),
        dict(at='detail', label="Le détail d'un daily", click='.btn-rect >> nth=0', zone=MODAL),
        dict(at='filtres', label='Filtres et recherche', eval=FERMER_MODALE, click='button:has-text("Filtres")', fill=[['input[placeholder="Chercher un projet"]', 'Boutique']], zone=[380, 110, 1420, 520]),
        dict(at='outro', wait=0.2),
    ]),
    'RH11': dict(start_path='/Agenda', scenes=[
        dict(at='intro', wait=0.3, zone='.fc'),
        dict(at='vues', label='Mois, semaine, jour, liste', click='.fc-timeGridWeek-button', wait=0.6),
        dict(at='vues', click='.fc-listWeek-button', wait=0.6),
        dict(at='vues', click='.fc-dayGridMonth-button', zone='.fc-header-toolbar'),
        dict(at='filtres', label='Filtrer par projet', click='.form-check:has-text("Salon Food") input', zone='Filtre par liste des projets', zone_closest='.card'),
        dict(at='naviguer', label='Naviguer', click='.fc-next-button', wait=0.6),
        dict(at='naviguer', click='.fc-today-button', zone='.fc-header-toolbar'),
        dict(at='outro', wait=0.2, zone='.fc'),
    ]),
    'RH12': dict(start_path='/rdv', scenes=[
        dict(at='intro', wait=0.3, zone='.fc'),
        dict(at='calendrier', label='Le calendrier', zone='.fc'),
        dict(at='ajouter', label='Créer un rendez-vous', click='.fc-day-future >> nth=4', fill=[[f'{M} input.form-control >> nth=0', 'Revue du site vitrine']],
             select=[[f'{M} select:has(option:text("Sélectionner un type"))', {'index': 1}]], zone=MODAL),
        dict(at='details', label='Les détails', eval=FERMER_MODALE, click='.fc-event:has-text("Point boutique")', zone='Détails du rendez-vous', zone_closest='.card, .col-lg-3, .col-md-4'),
        dict(at='outro', wait=0.2),
    ]),
    'RH14': dict(start_path='/conges', scenes=[
        dict(at='intro', wait=0.3, zone='table'),
        dict(at='liste', label='Les demandes', zone='table'),
        dict(at='decision', label='Approuver ou refuser', click='tr:has-text("En attente") button:has-text("Actions")', zone='tr:has-text("En attente")'),
        dict(at='decision', click='.dropdown-menu.show a[data-action=approve]', wait=1.2),
        dict(at='filtres', label='Filtrer', click='button:has-text("Filtrer")', zone=[380, 110, 1420, 400]),
        dict(at='outro', label='Jours restants', goto='/users', hover='tr:has-text("Lucas Petit")', zone='tr:has-text("Lucas Petit")'),
    ]),
    'RH17': dict(start_path='/dashboard', scenes=[
        dict(at='intro', wait=0.3),
        dict(at='cloche', label='La cloche', click='button:has(.ti-bell)', zone='.dropdown-menu.show'),
        dict(at='page', label='Toutes les notifications', goto='/notifications', zone=[380, 110, 1420, 600]),
        dict(at='actions', label='Lire ou supprimer', hover='.btn-rect >> nth=0', zone='.btn-rect >> nth=0', zone_closest='.card, li, .row'),
        dict(at='actions', click='.btn-rect >> nth=0', wait=0.8),
        dict(at='outro', wait=0.2),
    ]),
    'RH18': dict(start_path='/mon-abonnement', scenes=[
        dict(at='intro', wait=0.3),
        dict(at='offre', label='Offre en cours', zone='Offre en cours', zone_closest='.card'),
        dict(at='factures', label='Factures', zone='Factures', zone_closest='.card'),
        dict(at='changer', label='Changer d\'offre', click='a:has-text("Voir les offres")', wait=0.8),
        dict(at='outro', wait=0.2),
    ]),
    'RH19': dict(start_path='/tokens', scenes=[
        dict(at='intro', wait=0.3),
        dict(at='page', label='La page Tokens', zone=[380, 110, 1420, 360]),
        dict(at='generer', label='Générer un token', click='button:has-text("Générer un token")', fill=[['#tokenName', 'Claude - assistant']], zone=MODAL),
        dict(at='copier', label='Copier le token', click=f'{M} button:has-text("Générer")', wait=0.8,
             eval="document.querySelectorAll('.modal.show input, .modal.show code, .modal.show pre, .modal.show textarea').forEach(e=>{e.style.filter='blur(7px)'})", zone=MODAL),
        dict(at='outro', label='Révoquer', eval=FERMER_MODALE, wait=0.6, zone='table'),
    ]),
    'RH26': dict(start_path='/parametres-ia', scenes=[
        dict(at='intro', wait=0.3),
        dict(at='cle', label='Votre clé Anthropic', fill=[['#ai-key', 'sk-ant-exemple-fictif']], zone='#ai-key', zone_closest='.card'),
        dict(at='modele', label='Le modèle', select=[['#ai-model', {'index': 1}]], zone='#ai-model'),
        dict(at='tester', label='Enregistrer et tester', hover='button:has-text("Enregistrer")', wait=0.8),
        dict(at='tester', hover='button:has-text("Tester la connexion")', zone='button:has-text("Tester la connexion")'),
        dict(at='outro', wait=0.2),
    ]),
    'RH28': dict(start_path='/agents', scenes=[
        dict(at='intro', wait=0.3),
        dict(at='catalogue', label='Vos employés IA', zone=[380, 190, 1420, 600]),
        dict(at='filtres', label='Rechercher et filtrer', fill=[['#agent-search', 'projet']], select=[['#agent-status', 'En formation']], zone=[380, 120, 1420, 600]),
        dict(at='responsable', label='Un responsable humain', eval="(()=>{const s=document.querySelector('#agent-search');s.value='';s.dispatchEvent(new Event('input'))})()", wait=0.6,
             hover='text=Responsable : Camille Durand >> nth=0', zone='text=Responsable : Camille Durand >> nth=0', zone_closest='.card'),
        dict(at='outro', click='a[href^="/agents/"] >> nth=0', wait=0.5),
    ]),
    'RH29': dict(start_path='/agents', scenes=[
        dict(at='intro', goto_file='agent.txt', wait=0.3),
        dict(at='fiche', label='La fiche', zone=[380, 110, 1420, 520]),
        dict(at='fiche', click='#tab-outils', wait=0.6),
        dict(at='budget', label='Le budget', click='#tab-configuration', fill=[['#cfg-budget', '200000']], zone='#cfg-budget', zone_closest='.row, .card'),
        dict(at='prompt', label='Prompt versionné', click='button:has-text("Historique des versions")', wait=0.8),
        dict(at='activer', label='Activer', click='button:has-text("Enregistrer la configuration")', wait=0.6),
        dict(at='activer', top=True, click='button:has-text("Activer")', wait=1.0, zone=[380, 110, 1420, 300]),
        dict(at='outro', hover='button:has-text("Suspendre")'),
    ]),
    'RH30': dict(start_path='/projects', scenes=[
        dict(at='intro', goto_file='boutique-taches.txt', wait=0.3),
        dict(at='ouvrir', label='Le panneau Employé IA', click='.kanban-item:has-text("Rédiger les fiches produits")', wait=0.5),
        dict(at='ouvrir', hover=f'{M} select[id^=ai-mode]', zone=f'{M} select[id^=ai-mode]', zone_closest='.border, .card, div.mt-4'),
        dict(at='mode', label='Mode et instructions', select=[[f'{M} select[id^=ai-mode]', {'index': 1}]], wait=0.6),
        dict(at='mode', select=[[f'{M} select[id^=ai-agent]', {'index': 1}]],
             fill_now=[[f'{M} textarea[id^=ai-instr]', 'Rédige 6 fiches produits de 80 mots pour la boutique, ton chaleureux, à valider par Hugo.']]),
        dict(at='outils', label='Outils en lecture', click=f'{M} input[id^=ai-tool] >> nth=0', zone=f'{M} input[id^=ai-tool] >> nth=0', zone_closest='.border, .card, div.mt-4'),
        dict(at='outro', hover=f'{M} button:has-text("Enregistrer le mode IA")'),
    ]),
    'RH31': dict(start_path='/agents', scenes=[
        dict(at='intro', goto_file='agent.txt', wait=0.3),
        dict(at='journal', label='Le journal', click='#tab-journal', zone=[380, 290, 1420, 520]),
        dict(at='daily', label='Son daily', goto='/dailies', zone='table'),
        dict(at='validation', label='Centre de validation', goto='/validations', zone=[380, 110, 1420, 600]),
        dict(at='outro', label='Suspendre', goto_file='agent.txt', hover='button:has-text("Suspendre")', zone=[1200, 180, 600, 80]),
    ]),
    'RH15': dict(login=HUGO, start_path='/dashboard', scenes=[
        dict(at='intro', wait=0.3),
        dict(at='menu', label='Son menu', zone=[0, 0, 262, 1080]),
        dict(at='projets', label='Ses projets', goto='/projects', wait=1.2, zone=[380, 110, 1420, 560]),
        dict(at='taches', label='Ses tâches', goto_file='boutique-taches.txt', wait=0.3),
        dict(at='taches', drag=['.kanban-item:has-text("Maquette de la page")', '.kanban-board:has-text("Terminé") .kanban-drag'], zone='.kanban-container'),
        dict(at='outro', wait=0.2),
    ]),
    'RH32': dict(login=HUGO, start_path='/conges', scenes=[
        dict(at='intro', wait=0.3),
        dict(at='ouvrir', label='Faire une demande', click='a:has-text("Faire une demande de congé")', zone=MODAL),
        dict(at='formulaire', label='Le formulaire', select=[[f'{M} select:has(option:text("Congés annuels"))', 'Congés annuels']],
             fill=[[f'{M} input[type=date] >> nth=0', '2027-02-15'], [f'{M} input[type=date] >> nth=1', '2027-02-19'],
                   [f'{M} textarea', 'Vacances d\'hiver en famille.']], zone=MODAL),
        dict(at='suivi', label='Le suivi', click=f'{M} button:has-text("Créer la demande")', wait=1.2, zone='table'),
        dict(at='outro', wait=0.2),
    ]),
}


def build(ep):
    s, e = SCRIPTS[ep], EPISODES[ep]
    cfg = {
        'id': ep, 'product': 'rh', 'kicker': 'Tutoriel RapidoRH', 'title': s['title'], 'em': s['em'], 'tag': s['tag'],
        'profil': s['profil'], 'login_as': e.get('login', CAMILLE), 'intro': 3.0, 'outro': 4.5,
        'voice': 'audio/voix.mp3', 'transcript': 'audio/transcript.json', 'capture': 'captures/ecran.mp4',
        'start_path': e['start_path'], 'type_delay': e.get('type_delay', 35), 'fixes': {'Contrôle K': 'Ctrl + K'},
        'end_cta': f"Prochain épisode : {SUIVANT[ep]}" if ep in SUIVANT else "Retrouvez tous les tutoriels sur rapidosoftware.com",
        'paragraphs': [{'key': k, 'text': t} for k, t in s['paragraphs']],
        'scenes': e['scenes'], 'thumb_shot': e.get('thumb_shot', 'fin.png'),
    }
    if e.get('public'):
        cfg['public'] = True
    keys = {p['key'] for p in cfg['paragraphs']}
    bad = [sc['at'] for sc in cfg['scenes'] if sc['at'] not in keys]
    assert not bad, f'{ep}: scènes sans paragraphe {bad}'
    os.makedirs(os.path.join(ROOT, ep), exist_ok=True)
    with open(os.path.join(ROOT, ep, 'tuto.json'), 'w') as f:
        json.dump(cfg, f, ensure_ascii=False, indent=1)
    return ep


if __name__ == '__main__':
    for ep in (sys.argv[1:] or ORDRE):
        print(build(ep))
