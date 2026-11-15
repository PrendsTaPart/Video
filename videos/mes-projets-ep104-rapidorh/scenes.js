// Mes projets · épisode 104 — RapidoRH : humains et employés IA (vrais écrans des tutoriels RapidoRH, données de démonstration)
P.make({ep: 104, nom: "RapidoRH", url: "rh.rapidosoftware.com", src: '../mes-projets/src/rapidorh-v2.mp4', visuel: 'og.png', logo: '../_journal-63-72/commun/logo-rapidorh-officiel.png', duoLogo: 'logo-rapidorh-officiel.png',
  theme: {"bg": "#150E24", "bg2": "#0C0816", "bgc": "#2C1E52", "surf": "#1F1636", "line": "#33255A", "text": "#FFFFFF", "mute": "#b9afd1", "accent": "#7E57C2", "accent2": "#2FB37A", "hlbg": "#7E57C2", "hlfg": "#FFFFFF"},
  kw: ["modèle,", "valide.", "tâches,", "recrutement", "notée"], red: [], hookHl: ["même", "équipe."],
  labels: ["", "MON PROJET", "Un modèle, un projet", "L'IA prépare, je valide", "Réunion → tâches", "Recrutement suivi", "Tout est noté", ""],
  clips: [[0, 0.2], [1, 4.2], [2, 8.2], [3, 12.2], [4, 16.2], [5, 20.2], [6, 24.2]]});
// Logo officiel de l'application (vertical) : plus haut que les logos horizontaux.
document.head.insertAdjacentHTML('beforeend', '<style>img[src*="logo-rapidorh-officiel"]{height:100px!important}#dlogo img{height:64px!important}</style>');
// Mention honnête : écrans réels du logiciel, données fictives (masquée sur la carte finale).
document.body.insertAdjacentHTML('beforeend', '<div id="demo" style="position:absolute;left:0;right:0;top:1040px;text-align:center;font:600 24px Poppins,sans-serif;color:rgba(255,255,255,.55);letter-spacing:1px;z-index:50">Écrans réels · données de démonstration</div>');
{ const r0 = window.render, fin = window.CFG.lines[window.CFG.lines.length - 1].t0;
  window.render = t => { r0(t); document.getElementById('demo').style.display = t >= fin - .1 ? 'none' : ''; }; }
