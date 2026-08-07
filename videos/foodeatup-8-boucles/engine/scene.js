/* Moteur de composition « Les 8 boucles FoodEatUp ».
 *
 * Contrat : 100 % déterministe. `window.render(t)` doit produire exactement la
 * même image pour un même `t`, quel que soit l'ordre des appels. Donc aucun
 * Date.now(), aucun Math.random(), aucun setTimeout/setInterval, aucun rAF —
 * tout état visible est une fonction pure de `t`.
 *
 * Les données de la vidéo arrivent dans `window.__VIDEO` (injecté par
 * tools/build_html.py) : plans, minutages calés sur la durée réelle de la VO,
 * cascade, chiffres, assets en data: URI.
 */
(function () {
  "use strict";

  var V = window.__VIDEO;
  var stage = document.getElementById("stage");

  // ---------------------------------------------------------------- utilitaires

  function clamp01(x) { return x < 0 ? 0 : x > 1 ? 1 : x; }
  function lerp(a, b, p) { return a + (b - a) * p; }

  // Progression de `t` sur la fenêtre [a, b], bornée à [0,1].
  function span(t, a, b) { return b <= a ? (t >= b ? 1 : 0) : clamp01((t - a) / (b - a)); }

  var ease = {
    out: function (p) { return 1 - Math.pow(1 - p, 3); },          // power3.out
    snap: function (p) { return 1 - Math.pow(1 - p, 5); },         // power5.out
    inOut: function (p) { return p < 0.5 ? 4 * p * p * p : 1 - Math.pow(-2 * p + 2, 3) / 2; },
    // Léger dépassement, sans ressort infini (déterministe et borné).
    back: function (p) { var c = 1.70158, u = p - 1; return 1 + (c + 1) * u * u * u + c * u * u; }
  };

  function el(tag, cls, txt) {
    var n = document.createElement(tag);
    if (cls) n.className = cls;
    if (txt != null) n.textContent = txt;
    return n;
  }

  // Entrée standard : monte de `dy` en fondu. Utilisée partout pour que la
  // série ait un seul vocabulaire d'animation.
  function entree(node, p, dy, e) {
    var q = (e || ease.out)(p);
    node.style.opacity = q;
    node.style.transform = "translateY(" + ((1 - q) * (dy == null ? 34 : dy)) + "px)";
  }

  // Ajoute le personnage 3D du plan (librairie maison, détourée). `role` vaut
  // "probleme" ou "resultat" ; l'absence d'image n'est pas une erreur.
  function illustration(root, src) {
    if (!src) return null;
    var box = el("div", "illu");
    var img = document.createElement("img");
    img.src = src;
    box.appendChild(img);
    root.appendChild(box);
    return box;
  }

  // Pastille ronde de plat, à gauche d'une ligne qui nomme un plat. Les photos
  // sont pré-découpées en cercle par tools/prepare_assets.py — pas de
  // border-radius ici, dont le bord crénèle au rendu.
  function pastillePlat(nom) {
    var img = document.createElement("img");
    img.className = "pastille-plat";
    img.src = V.plats[nom];
    return img;
  }

  // Entrée du personnage : il glisse depuis la droite puis respire lentement.
  // La respiration est une fonction de `t`, donc reproductible au seek près.
  function majIllustration(box, t, dur) {
    if (!box) return;
    var p = ease.out(span(t, 0.35, 1.5));
    var flotte = Math.sin((t / 4.2) * Math.PI * 2) * 6;
    box.style.opacity = p;
    box.style.transform =
      "translate(" + ((1 - p) * 70).toFixed(1) + "px," + flotte.toFixed(2) + "px)";
  }

  // ------------------------------------------------------------------ plan 1

  function bâtirPlan1(root, d) {
    root.appendChild(el("div", "kicker", d.kicker || "Le problème"));
    var h = el("div", "titre");
    h.innerHTML = d.titre;
    root.appendChild(h);
    var wrap = el("div", "lignes-probleme");
    d.lignes.forEach(function (txt) { wrap.appendChild(el("div", "ligne", txt)); });
    root.appendChild(wrap);
    root._k = root.querySelector(".kicker");
    root._h = h;
    root._l = [].slice.call(wrap.children);
    root._illu = illustration(root, d.illu);
  }

  function majPlan1(root, t, dur) {
    entree(root._k, span(t, 0.15, 0.8), 18);
    entree(root._h, span(t, 0.3, 1.3), 44, ease.snap);
    root._l.forEach(function (n, i) {
      // Les phrases du problème tombent l'une après l'autre : le spectateur
      // doit sentir l'accumulation, pas lire un bloc.
      entree(n, span(t, 1.0 + i * 0.62, 1.7 + i * 0.62), 26);
    });
    majIllustration(root._illu, t, dur);
  }

  // ------------------------------------------------------------------ plan 2

  function bâtirPlan2(root, d) {
    if (d.agent) {
      var tag = el("div", "agent-tag");
      tag.appendChild(el("span", "pastille"));
      tag.appendChild(el("span", null, d.agent));
      root.appendChild(tag);
      root._tag = tag;
    }
    var b = el("div", "bulle");
    var texte = el("span");
    var caret = el("span", "caret");
    b.appendChild(texte); b.appendChild(caret);
    root.appendChild(b);
    root._b = b; root._txt = texte; root._caret = caret; root._phrase = d.phrase;
  }

  function majPlan2(root, t, dur) {
    if (root._tag) entree(root._tag, span(t, 0.1, 0.7), 14);
    var p = span(t, 0.25, 0.95);
    root._b.style.opacity = ease.out(p);
    root._b.style.transform = "translateY(" + ((1 - ease.back(p)) * 30).toFixed(2) + "px)";

    // Frappe : le nombre de caractères visibles est une fonction de t, donc
    // rejouable à l'identique en cas de seek.
    var s = root._phrase;
    var frappe = span(t, 0.7, Math.max(1.4, dur * 0.62));
    var n = Math.floor(ease.inOut(frappe) * s.length);
    root._txt.textContent = s.slice(0, n);
    // Le caret clignote sur une base entière de t : pas d'horloge externe.
    var fini = n >= s.length;
    root._caret.style.opacity = fini
      ? (Math.floor(t * 2) % 2 === 0 ? 1 : 0.15)
      : 1;
  }

  // ------------------------------------------------------------------ plan 3
  // Le plan pilier : la cascade, maillon par maillon.

  function bâtirPlan3(root, d) {
    root.appendChild(el("div", "kicker", "La donnée circule"));
    var grille = el("div", "grille-cascade");
    root.appendChild(grille);
    var col = el("div", "cascade");
    root._maillons = d.cascade.map(function (m, i) {
      var n = el("div", "maillon");
      n.appendChild(el("span", "puce"));
      n.appendChild(el("span", null, m.nom));
      if (m.valeur) n.appendChild(el("span", "valeur", m.valeur));
      if (i < d.cascade.length - 1) {
        var lien = el("div", "lien");
        lien.appendChild(el("i"));
        n.appendChild(lien);
        n._flux = lien.firstChild;
      }
      col.appendChild(n);
      return n;
    });
    grille.appendChild(col);

    if (d.fiches && d.fiches.length) {
      var f = el("div", "fiches");
      f.appendChild(el("div", "entete", "Ce que ça touche"));
      root._fiches = d.fiches.map(function (x) {
        var n = el("div", "fiche");
        if (x.photo) n.appendChild(pastillePlat(x.photo));
        n.appendChild(el("span", null, x.nom));
        n.appendChild(el("span", "cout", x.valeur));
        f.appendChild(n);
        return n;
      });
      grille.appendChild(f);
      root._entete = f.firstChild;
    } else {
      root._fiches = [];
    }

    var badge = el("div", "badge-mcp", d.preuve);
    root.appendChild(badge);
    root._badge = badge;
    root._k = root.querySelector(".kicker");
  }

  function majPlan3(root, t, dur) {
    entree(root._k, span(t, 0.1, 0.7), 14);

    var n = root._maillons.length;
    var t0 = 0.75;                       // le premier maillon s'allume ici
    var fin = Math.max(t0 + 2, dur - 2.4); // le dernier, avant la fin du plan
    var pas = (fin - t0) / n;

    root._maillons.forEach(function (m, i) {
      var a = t0 + i * pas;
      // Apparition de la boîte, puis allumage quand la valeur la traverse.
      entree(m, span(t, a - 0.42, a + 0.16), 20);
      var allume = span(t, a, a + 0.3);
      if (allume > 0.5) m.classList.add("on"); else m.classList.remove("on");
      // Petit à-coup au moment exact où la valeur entre dans le maillon.
      var kick = span(t, a, a + 0.34);
      var s = 1 + Math.sin(kick * Math.PI) * 0.022;
      m.style.transform = "translateY(" + ((1 - ease.out(span(t, a - 0.42, a + 0.16))) * 20).toFixed(2)
        + "px) scale(" + s.toFixed(4) + ")";
      // Le flux qui descend vers le maillon suivant.
      if (m._flux) {
        var f = span(t, a + 0.16, a + pas);
        m._flux.style.transform = "scaleY(" + ease.inOut(f).toFixed(4) + ")";
      }
    });

    // Les fiches touchées clignotent pendant la traversée « fiche technique ».
    if (root._entete) entree(root._entete, span(t, t0 + pas * 1.2, t0 + pas * 1.8), 12);
    var fenetreFiches = [t0 + pas * 1.6, t0 + pas * 4.2];
    root._fiches.forEach(function (f, i) {
      var a = fenetreFiches[0] + i * 0.34;
      entree(f, span(t, a - 0.3, a + 0.2), 16);
      // Trois battements nets, calés sur t — pas d'animation CSS auto.
      var w = span(t, a, fenetreFiches[1]);
      var bat = w > 0 && w < 1 ? Math.sin(w * Math.PI * 6) > 0 : false;
      if (bat || t > fenetreFiches[1]) f.classList.add("hot"); else f.classList.remove("hot");
    });

    root._badge.style.opacity = ease.out(span(t, dur - 3.2, dur - 2.4));
  }

  // ------------------------------------------------------------------ plan 4

  function bâtirPlan4(root, d) {
    var b = el("div", "bandeau");
    b.appendChild(el("span", null, "⚠"));
    b.appendChild(el("span", null, d.alerte));
    root.appendChild(b);
    root._bandeau = b;

    var c = el("div", "carte-proposition");
    c.appendChild(el("h4", null, d.proposition.titre));
    var lg = el("div", "lignes");
    d.proposition.lignes.forEach(function (l) {
      var r = el("div");
      if (l.photo) r.appendChild(pastillePlat(l.photo));
      r.appendChild(el("span", null, l.nom));
      r.appendChild(el("b", null, l.valeur));
      lg.appendChild(r);
    });
    c.appendChild(lg);

    var btns = el("div", "boutons");
    var ok = el("div", "btn valider", "Valider");
    var no = el("div", "btn ignorer", "Ignorer");
    btns.appendChild(ok); btns.appendChild(no);
    c.appendChild(btns);
    root.appendChild(c);
    root._carte = c; root._ok = ok;

    if (d.mention) {
      var m = el("div", "mention", d.mention);
      root.appendChild(m);
      root._mention = m;
    }

    // Curseur dessiné en SVG : pas d'asset externe, pas de glyphe système.
    var cur = el("div", "curseur");
    cur.innerHTML =
      '<svg viewBox="0 0 24 24" width="100%" height="100%">' +
      '<path d="M4 2 L4 20 L9 15.5 L12.2 22 L15.4 20.4 L12.2 14.2 L19 14 Z" ' +
      'fill="#0F1A23" stroke="#FCF9E6" stroke-width="1.4" stroke-linejoin="round"/></svg>';
    root.appendChild(cur);
    root._cur = cur;
  }

  function majPlan4(root, t, dur) {
    var pb = span(t, 0.15, 0.85);
    root._bandeau.style.opacity = ease.out(pb);
    root._bandeau.style.transform = "translateY(" + ((1 - ease.back(pb)) * -26).toFixed(2) + "px)";

    entree(root._carte, span(t, 0.8, 1.6), 34, ease.snap);
    if (root._mention) entree(root._mention, span(t, 1.6, 2.2), 14);

    // Le curseur part du coin bas-droit et va se poser sur « Valider ».
    var tArrivee = Math.max(2.4, dur - 2.6);
    var pc = span(t, tArrivee - 1.5, tArrivee);
    var cible = root._ok.getBoundingClientRect();
    var x0 = V.W * 0.86, y0 = V.H * 0.9;
    var x1 = cible.left + cible.width * 0.52, y1 = cible.top + cible.height * 0.62;
    var q = ease.inOut(pc);
    root._cur.style.opacity = ease.out(span(t, tArrivee - 1.7, tArrivee - 1.3));
    root._cur.style.transform =
      "translate(" + lerp(x0, x1, q).toFixed(1) + "px," + lerp(y0, y1, q).toFixed(1) + "px)";

    // Appui : le bouton s'enfonce brièvement une fois le curseur arrivé.
    var appui = span(t, tArrivee, tArrivee + 0.42);
    if (appui > 0 && appui < 1) root._ok.classList.add("presse");
    else root._ok.classList.remove("presse");
    root._ok.style.transform = "scale(" + (1 - Math.sin(appui * Math.PI) * 0.05).toFixed(4) + ")";
  }

  // ------------------------------------------------------------------ plan 5
  // Le ∞ : deux boucles, huit nœuds, les voisines s'allument.

  var NOEUDS = [
    // Boucle gestion — lobe GAUCHE, dans l'ordre des boucles 01 à 04.
    { id: "Configuration", court: "Config." }, { id: "Équipe", court: "Équipe" },
    { id: "StockVisionAI", court: "Stock" }, { id: "HACCP", court: "HACCP" },
    // Boucle vente — lobe DROIT, boucles 05 à 08.
    { id: "E-commerce", court: "E-com." }, { id: "Communication", court: "Commu." },
    { id: "Fidélité", court: "Fidélité" }, { id: "Comptabilité", court: "Compta." }
  ];

  // Lemniscate de Gerono — paramétrage stable, donc positions reproductibles.
  function pointInfini(a, rx, ry) {
    return { x: rx * Math.cos(a), y: ry * Math.sin(a) * Math.cos(a) };
  }

  // Angle du i-ème nœud. Le signe de cos(a) décide du lobe : répartir les huit
  // nœuds sur un tour complet les ferait sauter d'un lobe à l'autre à chaque
  // passage par le croisement central, et la boucle gestion se retrouverait à
  // cheval sur les deux — exactement ce que le schéma doit démentir. On cantonne
  // donc les quatre boucles de gestion à cos(a) < 0 (gauche) et les quatre de
  // vente à cos(a) > 0 (droite).
  function angleNoeud(i) {
    var rang = (i % 4 + 0.5) / 4;              // 0,125 · 0,375 · 0,625 · 0,875
    return i < 4
      ? Math.PI / 2 + rang * Math.PI          // lobe gauche  — gestion
      : -Math.PI / 2 + rang * Math.PI;        // lobe droit   — vente
  }

  function bâtirPlan5(root, d) {
    root.appendChild(el("div", "kicker", "Les boucles voisines"));
    var box = el("div", "infini");
    var rx = V.infiniRx, ry = V.infiniRy;
    var svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
    svg.setAttribute("width", rx * 2 + 240);
    svg.setAttribute("height", ry * 2 + 160);
    var cx = rx + 120, cy = ry + 80;

    var pts = [];
    for (var i = 0; i <= 240; i++) {
      var p = pointInfini((i / 240) * Math.PI * 2, rx, ry);
      pts.push((cx + p.x).toFixed(2) + "," + (cy + p.y).toFixed(2));
    }
    var trace = document.createElementNS("http://www.w3.org/2000/svg", "polyline");
    trace.setAttribute("points", pts.join(" "));
    trace.setAttribute("fill", "none");
    trace.setAttribute("stroke", "#0F1A23");
    trace.setAttribute("stroke-opacity", "0.14");
    trace.setAttribute("stroke-width", V.infiniTrait);
    svg.appendChild(trace);

    // Le trait bleu qui parcourt le ∞ : dash animé par render(t).
    var flux = document.createElementNS("http://www.w3.org/2000/svg", "polyline");
    flux.setAttribute("points", pts.join(" "));
    flux.setAttribute("fill", "none");
    flux.setAttribute("stroke", "#007BFF");
    flux.setAttribute("stroke-width", V.infiniTrait);
    flux.setAttribute("stroke-linecap", "round");
    svg.appendChild(flux);
    root._flux = flux;

    root._noeuds = NOEUDS.map(function (n, i) {
      var p = pointInfini(angleNoeud(i), rx, ry);
      var g = document.createElementNS("http://www.w3.org/2000/svg", "g");
      var c = document.createElementNS("http://www.w3.org/2000/svg", "circle");
      c.setAttribute("cx", cx + p.x); c.setAttribute("cy", cy + p.y);
      c.setAttribute("r", V.infiniNoeud);
      c.setAttribute("fill", "#FCF9E6");
      c.setAttribute("stroke", "#0F1A23");
      c.setAttribute("stroke-opacity", "0.2");
      c.setAttribute("stroke-width", "4");
      var tx = document.createElementNS("http://www.w3.org/2000/svg", "text");
      tx.setAttribute("x", cx + p.x);
      tx.setAttribute("y", cy + p.y + V.infiniNoeud + V.fsNoeud * 1.25);
      tx.setAttribute("text-anchor", "middle");
      tx.setAttribute("class", "noeud-label");
      tx.textContent = n.court;
      g.appendChild(c); g.appendChild(tx);
      svg.appendChild(g);
      return { g: g, cercle: c, texte: tx, nom: n.id };
    });

    box.appendChild(svg);
    root.appendChild(box);
    root._k = root.querySelector(".kicker");
    root._allumer = d.voisines || [];
    // Longueur du tracé, pour piloter le dash du flux. Repli analytique si le
    // SVG n'est pas encore rendu — la lemniscate mesure ~5,9 rx.
    var L = rx * 5.9;
    try { L = trace.getTotalLength() || L; } catch (e) { /* repli */ }
    root._longueur = L;
  }

  function majPlan5(root, t, dur) {
    entree(root._k, span(t, 0.1, 0.7), 14);

    // Le flux parcourt le ∞ une fois, sur toute la durée utile du plan.
    var L = root._longueur;
    var p = ease.inOut(span(t, 0.4, dur - 0.6));
    root._flux.setAttribute("stroke-dasharray", (L * 0.16) + " " + L);
    root._flux.setAttribute("stroke-dashoffset", (L * (1 - p * 1.16)).toFixed(1));

    root._noeuds.forEach(function (n, i) {
      var visible = span(t, 0.5 + i * 0.06, 1.0 + i * 0.06);
      n.g.setAttribute("opacity", ease.out(visible).toFixed(3));

      var vise = root._allumer.indexOf(n.nom) >= 0;
      if (!vise) {
        n.cercle.setAttribute("fill", "#FCF9E6");
        n.cercle.setAttribute("stroke-opacity", "0.2");
        n.cercle.setAttribute("stroke-width", "4");
        return;
      }
      // Les voisines s'allument l'une après l'autre, dans l'ordre du script.
      var rang = root._allumer.indexOf(n.nom);
      var a = 1.4 + rang * ((dur - 2.6) / Math.max(1, root._allumer.length));
      var on = span(t, a, a + 0.34);
      n.cercle.setAttribute("fill", on > 0.5 ? "#007BFF" : "#FCF9E6");
      n.cercle.setAttribute("stroke", "#007BFF");
      n.cercle.setAttribute("stroke-opacity", (0.2 + on * 0.8).toFixed(2));
      n.cercle.setAttribute("stroke-width", (4 + on * 5).toFixed(1));
      n.cercle.setAttribute("r", (V.infiniNoeud * (1 + Math.sin(on * Math.PI) * 0.16)).toFixed(1));
    });
  }

  // ------------------------------------------------------------------ plan 6

  function bâtirPlan6(root, d) {
    root.appendChild(el("div", "kicker", "Le résultat"));
    var box = el("div", "chiffres");
    // Au-delà de trois chiffres on passe sur deux rangées : quatre tuiles en
    // ligne deviennent illisibles, et une seule tuile orpheline sur la
    // deuxième rangée s'étirerait sur toute la largeur.
    var cols = d.chiffres.length > 3 ? 2 : d.chiffres.length;
    box.style.gridTemplateColumns = "repeat(" + cols + ", 1fr)";
    root._c = d.chiffres.map(function (c) {
      var n = el("div", "chiffre");
      var v = el("div", "v", c.valeur);
      n.appendChild(v);
      n.appendChild(el("div", "l", c.label));
      box.appendChild(n);
      n._v = v; n._cible = c.valeur;
      return n;
    });
    root.appendChild(box);
    root._k = root.querySelector(".kicker");
    root._illu = illustration(root, d.illu);
  }

  // Compte à rebours sur la partie numérique d'une valeur, en gardant son
  // habillage (« 4,38 € », « 68,7 % », « 4 à 10 % » reste tel quel).
  function compter(cible, p) {
    var m = /^(\D*)(\d+(?:[.,]\d+)?)(.*)$/.exec(cible);
    if (!m || /\bà\b/.test(cible)) return cible;
    var dec = (m[2].split(/[.,]/)[1] || "").length;
    var val = parseFloat(m[2].replace(",", ".")) * p;
    return m[1] + val.toFixed(dec).replace(".", ",") + m[3];
  }

  function majPlan6(root, t, dur) {
    entree(root._k, span(t, 0.1, 0.7), 14);
    root._c.forEach(function (n, i) {
      var a = 0.5 + i * 0.28;
      entree(n, span(t, a, a + 0.7), 40, ease.snap);
      var p = ease.out(span(t, a, a + 1.15));
      n._v.textContent = compter(n._cible, p);
      // Respiration décalée : les tuiles ne bougent pas en bloc.
      var y = Math.sin((t / 3.6 + i * 0.25) * Math.PI * 2) * 3;
      var e = ease.snap(span(t, a, a + 0.7));
      n.style.transform = "translateY(" + ((1 - e) * 40 + y).toFixed(2) + "px)";
    });
    majIllustration(root._illu, t, dur);
  }

  // ------------------------------------------------------------------ plan 7

  function bâtirPlan7(root, d) {
    root.appendChild(el("div", "kicker", "Si cette boucle est coupée"));
    var c = el("div", "coupure", d.coupure);
    root.appendChild(c);
    var cta = el("div", "cta", d.cta);
    root.appendChild(cta);
    if (d.logo) {
      var lg = el("div", "logo-fin");
      var img = document.createElement("img");
      img.src = d.logo;
      lg.appendChild(img);
      root.appendChild(lg);
      root._logo = lg;
    }
    root._k = root.querySelector(".kicker");
    root._c = c; root._cta = cta;
  }

  function majPlan7(root, t, dur) {
    entree(root._k, span(t, 0.1, 0.7), 14);
    entree(root._c, span(t, 0.4, 1.3), 34, ease.snap);
    var p = span(t, 1.1, 1.8);
    root._cta.style.opacity = ease.out(p);
    root._cta.style.transform = "translateY(" + ((1 - ease.back(p)) * 24).toFixed(2) + "px)";
    if (root._logo) entree(root._logo, span(t, 1.5, 2.2), 18);
  }

  // ------------------------------------------------------------ assemblage

  var CONSTRUCTEURS = {
    1: [bâtirPlan1, majPlan1], 2: [bâtirPlan2, majPlan2], 3: [bâtirPlan3, majPlan3],
    4: [bâtirPlan4, majPlan4], 5: [bâtirPlan5, majPlan5], 6: [bâtirPlan6, majPlan6],
    7: [bâtirPlan7, majPlan7]
  };

  var PLANS = V.plans.map(function (d) {
    var root = el("div", "plan plan-" + d.type);
    // Le plan rejoint le DOM AVANT d'être construit : plusieurs gabarits
    // interrogent la géométrie pendant la construction (longueur du tracé du ∞,
    // position du bouton Valider), et un élément détaché n'en a pas.
    stage.appendChild(root);
    var paire = CONSTRUCTEURS[d.type];
    paire[0](root, d);
    return { root: root, maj: paire[1], start: d.start, dur: d.dur, data: d };
  });

  // Fondu croisé court entre deux plans : le plan sortant s'efface pendant que
  // l'entrant monte. 0,35 s — assez pour ne pas faire saccade, assez court pour
  // que la VO reste calée sur son plan.
  var XF = 0.35;

  window.render = function (t) {
    for (var i = 0; i < PLANS.length; i++) {
      var P = PLANS[i];
      var local = t - P.start;
      var dedans = local >= -XF && local <= P.dur + XF;

      if (!dedans) {
        P.root.style.opacity = 0;
        P.root.style.visibility = "hidden";
        continue;
      }
      P.root.style.visibility = "visible";

      // Le plan est mis à jour avec un `local` borné : au-delà de sa fenêtre il
      // garde sa dernière image plutôt que de repartir à zéro pendant le fondu.
      P.maj(P.root, Math.max(0, Math.min(local, P.dur)), P.dur);

      var apparait = span(t, P.start, P.start + XF);
      var disparait = 1 - span(t, P.start + P.dur, P.start + P.dur + XF);
      var o = Math.min(i === 0 ? 1 : apparait, i === PLANS.length - 1 ? 1 : disparait);
      // `maj` a écrit l'opacité des enfants ; ici on pilote celle du plan entier.
      P.root.style.opacity = o;
    }
  };

  window.__duree = V.duree;
  window.render(0);
})();
