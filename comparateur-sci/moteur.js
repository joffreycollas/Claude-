/* Moteur de calcul : SCI à l'IR ou à l'IS, de l'acquisition à la revente.
   Fonction pure, sans DOM : testable avec Node (node tests.js). */
const Moteur = (() => {
  const TAUX_2026 = {
    psFoncier: 0.172,      // PS sur revenus fonciers et PV immobilières (CSS L136-8 IV, taux maintenu par la LFSS 2026)
    csgDeductible: 0.068,  // part de CSG déductible du revenu global (revenus fonciers au barème)
    irPV: 0.19,            // IR sur plus-value immobilière des particuliers (CGI 200 B)
    pfu: 0.314,            // 12,8 % + 18,6 % sur dividendes à compter du 1er janvier 2026 (LFSS 2026, art. 12)
    isReduit: 0.15,        // CGI 219 I b
    isNormal: 0.25,
    isSeuil: 42500,
    plafondDeficit: 10700, // CGI 156 I 3°, par foyer fiscal
    forfaitFrais: 0.075,   // CGI 150 VB II 4°
    forfaitTravaux: 0.15,  // CGI 150 VB II 4°, détention > 5 ans
  };

  // Abattements pour durée de détention (CGI 150 VC I et CSS L136-7, BOI-RFPI-PVI-20-20)
  function abattementIR(ans) {
    if (ans <= 5) return 0;
    if (ans <= 21) return 0.06 * (ans - 5);
    return 1;
  }
  function abattementPS(ans) {
    if (ans <= 5) return 0;
    if (ans <= 21) return 0.0165 * (ans - 5);
    if (ans === 22) return 0.0165 * 16 + 0.016;
    return Math.min(1, 0.0165 * 16 + 0.016 + 0.09 * (ans - 22));
  }

  // Taxe sur les plus-values immobilières élevées (CGI 1609 nonies G), par associé
  function surtaxe(x) {
    if (x <= 50000) return 0;
    if (x <= 60000) return 0.02 * x - (60000 - x) / 20;
    if (x <= 100000) return 0.02 * x;
    if (x <= 110000) return 0.03 * x - (110000 - x) / 10;
    if (x <= 150000) return 0.03 * x;
    if (x <= 160000) return 0.04 * x - (160000 - x) * 0.15;
    if (x <= 200000) return 0.04 * x;
    if (x <= 210000) return 0.05 * x - (210000 - x) * 0.20;
    if (x <= 250000) return 0.05 * x;
    if (x <= 260000) return 0.06 * x - (260000 - x) * 0.25;
    return 0.06 * x;
  }

  // Tableau d'amortissement mensuel agrégé par année
  function pret(capital, tauxAnnuel, dureeAns, tauxAssurance) {
    const n = Math.round(dureeAns * 12), i = tauxAnnuel / 12;
    const annees = [];
    if (capital <= 0 || n <= 0) return { annees, mensualite: 0 };
    const m = i === 0 ? capital / n : capital * i / (1 - Math.pow(1 + i, -n));
    let crd = capital;
    for (let a = 0; a < Math.ceil(n / 12); a++) {
      let interets = 0, principal = 0;
      for (let k = 0; k < 12 && a * 12 + k < n; k++) {
        const int = crd * i;
        const pr = Math.min(crd, m - int);
        interets += int; principal += pr; crd -= pr;
      }
      annees.push({ interets, principal, assurance: capital * tauxAssurance, crd: Math.max(0, crd) });
    }
    return { annees, mensualite: m };
  }

  function impotSocietes(base, p, T) {
    if (base <= 0) return 0;
    if (!p.tauxReduit) return base * T.isNormal;
    return Math.min(base, T.isSeuil) * T.isReduit + Math.max(0, base - T.isSeuil) * T.isNormal;
  }

  function tri(flux) {
    const van = (r) => flux.reduce((s, f, t) => s + f / Math.pow(1 + r, t), 0);
    let lo = -0.99, hi = 1;
    if (van(lo) * van(hi) > 0) return null;
    for (let k = 0; k < 200; k++) {
      const mid = (lo + hi) / 2;
      if (van(lo) * van(mid) <= 0) hi = mid; else lo = mid;
    }
    return (lo + hi) / 2;
  }

  function simuler(p, tauxPerso) {
    const T = Object.assign({}, TAUX_2026, tauxPerso || {});
    const N = Math.max(1, Math.round(p.duree));
    const nbAss = Math.max(1, Math.round(p.nbAssocies));
    const travauxDeductiblesIR = p.typeTravaux !== 'construction';
    const emprunt = pret(p.emprunt, p.tauxEmprunt, p.dureeEmprunt, p.tauxAssurance);
    const prixVente = p.prixVente > 0 ? p.prixVente : p.prix * Math.pow(1 + p.revalorisation, N);
    const prixCession = prixVente - p.fraisCession;
    const apport = p.prix + p.frais + p.travaux - p.emprunt;
    const alertes = [];

    // ---------- IR ----------
    let reports = []; // { annee, montant } déficits reportables 10 ans sur revenus fonciers
    const ir = [];
    let dernierDeficitRG = 0;
    for (let t = 1; t <= N; t++) {
      const loyers = p.loyers * Math.pow(1 + p.indexLoyers, t - 1);
      const charges = p.charges * Math.pow(1 + p.indexCharges, t - 1);
      const e = emprunt.annees[t - 1] || { interets: 0, principal: 0, assurance: 0 };
      const interetsAss = e.interets + e.assurance;
      const travaux = t === 1 && travauxDeductiblesIR ? p.travaux : 0;
      const resultat = loyers - charges - interetsAss - travaux;
      reports = reports.filter((r) => t - r.annee <= 10 && r.montant > 0.005);
      let imposable = 0, imputeRG = 0, reporte = 0, utilise = 0;
      if (resultat >= 0) {
        let reste = resultat;
        for (const r of reports) { const u = Math.min(r.montant, reste); r.montant -= u; reste -= u; utilise += u; }
        imposable = reste;
      } else {
        const def = -resultat;
        const issuInterets = Math.min(def, Math.max(0, interetsAss - loyers));
        imputeRG = Math.min(T.plafondDeficit * nbAss, def - issuInterets);
        reporte = def - imputeRG;
        if (reporte > 0) reports.push({ annee: t, montant: reporte });
        if (imputeRG > 0) dernierDeficitRG = t;
      }
      const impotRevenu = imposable * p.tmi - imposable * T.csgDeductible * p.tmi - imputeRG * p.tmi;
      const ps = imposable * T.psFoncier;
      ir.push({ annee: t, loyers, charges, interets: interetsAss, travaux, resultat, utilise, imposable, imputeRG, reporte,
        impotRevenu, ps, impot: impotRevenu + ps, principal: e.principal, crd: e.crd ?? 0 });
    }
    if (dernierDeficitRG && N - dernierDeficitRG < 3)
      alertes.push("Revente moins de 3 ans après l'imputation d'un déficit foncier sur le revenu global : ce déficit serait remis en cause (CGI 156 I 3°). La simulation n'en tient pas compte.");

    // Plus-value des particuliers (associés de la SCI à l'IR)
    const fraisRetenus = Math.max(p.frais, p.prix * T.forfaitFrais);
    const travauxNonDeduits = travauxDeductiblesIR ? 0 : p.travaux;
    const travauxRetenus = N > 5 ? Math.max(travauxNonDeduits, p.prix * T.forfaitTravaux) : travauxNonDeduits;
    const prixAcqIR = p.prix + fraisRetenus + travauxRetenus;
    const pvBrute = Math.max(0, prixCession - prixAcqIR);
    const abIR = abattementIR(N), abPS = abattementPS(N);
    const pvImposableIR = pvBrute * (1 - abIR);
    const pvImposablePS = pvBrute * (1 - abPS);
    const pvIR = {
      prixCession, prixAcq: prixAcqIR, fraisRetenus, travauxRetenus, brute: pvBrute, abIR, abPS,
      imposableIR: pvImposableIR, imposablePS: pvImposablePS,
      impotIR: pvImposableIR * T.irPV, ps: pvImposablePS * T.psFoncier,
      surtaxe: surtaxe(pvImposableIR / nbAss) * nbAss,
    };
    pvIR.total = pvIR.impotIR + pvIR.ps + pvIR.surtaxe;

    // ---------- IS ----------
    const fraisImmobilises = p.fraisAuCout;
    const baseBien = p.prix + (fraisImmobilises ? p.frais : 0);
    const amortBatiAn = baseBien * (1 - p.partTerrain) / p.dureeAmortBati;
    const dureeTrav = p.typeTravaux === 'construction' ? p.dureeAmortBati : p.dureeAmortTravaux;
    const amortTravAn = p.travaux / dureeTrav;
    let stockDeficit = 0, reserves = 0, cumulAmort = 0;
    const is = [];
    let pvIS = null;
    for (let t = 1; t <= N; t++) {
      const loyers = p.loyers * Math.pow(1 + p.indexLoyers, t - 1);
      const charges = p.charges * Math.pow(1 + p.indexCharges, t - 1);
      const e = emprunt.annees[t - 1] || { interets: 0, principal: 0, assurance: 0 };
      const amort = (t <= p.dureeAmortBati ? amortBatiAn : 0) + (t <= dureeTrav ? amortTravAn : 0);
      cumulAmort += amort;
      const fraisCharge = t === 1 && !fraisImmobilises ? p.frais : 0;
      let resultat = loyers - charges - e.interets - e.assurance - amort - fraisCharge - p.honorairesIS;
      let pv = 0;
      if (t === N) {
        const vnc = baseBien + p.travaux - cumulAmort;
        pv = prixCession - vnc;
        pvIS = { prixCession, vnc, cumulAmort, pv };
        resultat += pv;
      }
      let base = resultat;
      if (resultat > 0 && stockDeficit > 0) {
        const imput = Math.min(stockDeficit, 1e6 + 0.5 * Math.max(0, resultat - 1e6), resultat);
        stockDeficit -= imput; base -= imput;
      } else if (resultat < 0) stockDeficit += -resultat;
      const impot = impotSocietes(Math.max(0, base), p, T);
      const net = resultat - impot;
      reserves += net;
      let distribue = 0;
      if (t === N && p.liquidation) distribue = Math.max(0, reserves);
      else distribue = Math.min(Math.max(0, reserves), p.tauxDistribution * Math.max(0, net));
      reserves -= distribue;
      const pfu = distribue * T.pfu;
      is.push({ annee: t, loyers, charges, interets: e.interets + e.assurance, amort, fraisCharge, pv, resultat, base, impot, net,
        distribue, pfu, reserves, principal: e.principal, crd: e.crd ?? 0 });
    }
    const impotPVdansIS = (() => { // part de l'IS de l'année de revente imputable à la plus-value
      const der = is[N - 1];
      const sansPV = impotSocietes(Math.max(0, der.base - der.pv), p, T);
      return der.impot - sansPV;
    })();
    if (!p.liquidation && reserves > 0)
      alertes.push(`Réserves laissées dans la SCI à l'IS : ${Math.round(reserves).toLocaleString('fr-FR')} €, avec un impôt latent au PFU de ${Math.round(reserves * T.pfu).toLocaleString('fr-FR')} € non compté.`);

    // ---------- Flux des associés ----------
    const crdFinal = (emprunt.annees[N - 1] && emprunt.annees[N - 1].crd) || 0;
    const fluxAvantImpot = [];
    for (let t = 1; t <= N; t++) {
      const r = ir[t - 1];
      fluxAvantImpot.push(r.loyers - r.charges - r.interets - r.principal);
    }
    const fluxIR = [-apport], fluxIS = [-apport];
    for (let t = 1; t <= N; t++) {
      const base = fluxAvantImpot[t - 1] + (t === N ? prixCession - crdFinal : 0);
      fluxIR.push(base - ir[t - 1].impot - (t === N ? pvIR.total : 0));
      fluxIS.push(base - p.honorairesIS - is[t - 1].impot - is[t - 1].pfu);
    }
    const somme = (a) => a.reduce((s, x) => s + x, 0);
    const synthese = {
      ir: {
        impotsDetention: somme(ir.map((r) => r.impot)),
        impotsRevente: pvIR.total,
        honoraires: 0,
      },
      is: {
        impotsDetention: somme(is.map((r) => r.impot)) - impotPVdansIS + somme(is.slice(0, N - 1).map((r) => r.pfu)),
        impotsRevente: impotPVdansIS + is[N - 1].pfu,
        honoraires: p.honorairesIS * N,
      },
    };
    for (const k of ['ir', 'is']) {
      const s = synthese[k], flux = k === 'ir' ? fluxIR : fluxIS;
      s.impotsTotal = s.impotsDetention + s.impotsRevente;
      s.enrichissement = somme(flux);
      s.tri = tri(flux);
      s.flux = flux;
    }
    // Impôts cumulés année par année (revente incluse la dernière année)
    let cIR = 0, cIS = 0;
    const cumul = [];
    for (let t = 1; t <= N; t++) {
      cIR += ir[t - 1].impot + (t === N ? pvIR.total : 0);
      cIS += is[t - 1].impot + is[t - 1].pfu;
      cumul.push({ annee: t, ir: cIR, is: cIS });
    }
    return { T, N, apport, prixVente, prixCession, crdFinal, mensualite: emprunt.mensualite, ir, is, pvIR, pvIS,
      impotPVdansIS, synthese, cumul, alertes, ecart: synthese.is.enrichissement - synthese.ir.enrichissement };
  }

  return { simuler, TAUX_2026, abattementIR, abattementPS, surtaxe, pret, tri };
})();
if (typeof module !== 'undefined') module.exports = Moteur;
