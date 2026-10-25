"""Génère le rapport PDF du comparateur SCI IR / IS à partir d'un dossier JSON, sans ouvrir l'interface.

Usage :
    python comparateur-sci/generer_rapport.py dossier.json [sortie.pdf]

Le dossier JSON reprend les champs du formulaire (voir CHAMPS ci-dessous). Les champs
obligatoires manquants sont listés et le script s'arrête sans rien produire.
Affiche ensuite un résumé JSON (verdict, synthèse IR / IS) sur la sortie standard.

Prérequis : pip install playwright && python -m playwright install chromium
"""
import json
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
HTML = RACINE / "Comparateur_SCI_IR_IS.html"

# clé : (obligatoire, valeur par défaut, description)
CHAMPS = {
    "cabinet": (True, None, "AE (ALTHO EXPERTISE) ou ALTHO"),
    "client": (True, None, "Nom de la SCI ou des associés"),
    "prix": (True, None, "Prix du bien hors frais, en euros"),
    "frais": (True, None, "Frais d'acquisition (notaire, droits, garantie), en euros"),
    "travaux": (True, None, "Travaux initiaux, en euros (0 si aucun)"),
    "typeTravaux": (False, "amelioration", "amelioration ou construction"),
    "emprunt": (True, None, "Montant emprunté, en euros (0 si aucun crédit)"),
    "tauxEmprunt": (False, 0, "Taux du crédit, en % (obligatoire si emprunt > 0)"),
    "dureeEmprunt": (False, 0, "Durée du crédit, en années (obligatoire si emprunt > 0)"),
    "tauxAssurance": (False, 0, "Assurance emprunteur, en % du capital par an"),
    "loyers": (True, None, "Loyers annuels hors charges, année 1, en euros"),
    "charges": (True, None, "Charges annuelles déductibles non récupérables, en euros"),
    "duree": (True, None, "Durée de détention avant revente, en années (1 à 30)"),
    "tmi": (True, None, "Tranche marginale des associés : 0, 11, 30, 41 ou 45 (en %)"),
    "nbAssocies": (True, None, "Nombre d'associés (foyers fiscaux distincts, parts égales)"),
    "date": (False, None, "Date de l'étude AAAA-MM-JJ (défaut : aujourd'hui)"),
    "auteur": (False, "", "Préparé par"),
    "partTerrain": (False, 20, "Part du terrain, en %"),
    "indexLoyers": (False, 1.5, "Hausse annuelle des loyers, en %"),
    "indexCharges": (False, 2, "Hausse annuelle des charges, en %"),
    "revalorisation": (False, 1.5, "Revalorisation annuelle du bien, en %"),
    "prixVente": (False, "", "Prix de revente si connu, en euros"),
    "fraisCession": (False, 0, "Frais de cession à la charge du vendeur, en euros"),
    "dureeAmortBati": (False, 30, "Durée d'amortissement du bâti, en années"),
    "dureeAmortTravaux": (False, 15, "Durée d'amortissement des travaux, en années"),
    "fraisAuCout": (False, False, "true : frais d'acquisition immobilisés ; false : en charge l'année 1"),
    "tauxDistribution": (False, 0, "Part du bénéfice distribuée chaque année à l'IS, en %"),
    "honorairesIS": (False, 0, "Surcoût annuel d'honoraires lié à l'IS, en euros"),
    "tauxReduit": (False, True, "Taux réduit d'IS de 15 % applicable"),
    "liquidation": (False, True, "Toutes les réserves distribuées à la revente"),
    "taux": (False, {}, "Surcharge des taux 2026 (psFoncier, pfu, isReduit… en %)"),
}


def preparer(dossier: dict) -> dict:
    manquants = [f"{k} : {d}" for k, (obl, _, d) in CHAMPS.items() if obl and dossier.get(k) in (None, "")]
    if float(dossier.get("emprunt") or 0) > 0:
        for k in ("tauxEmprunt", "dureeEmprunt"):
            if dossier.get(k) in (None, "", 0):
                manquants.append(f"{k} : {CHAMPS[k][2]}")
    if manquants:
        print("Éléments obligatoires manquants :\n- " + "\n- ".join(manquants), file=sys.stderr)
        sys.exit(2)
    inconnus = sorted(set(dossier) - set(CHAMPS))
    if inconnus:
        print("Champs inconnus ignorés : " + ", ".join(inconnus), file=sys.stderr)
    cab = str(dossier["cabinet"]).upper().replace(" ", "")
    etat = {k: dossier.get(k, defaut) for k, (_, defaut, _) in CHAMPS.items() if k in dossier or defaut is not None}
    etat["cabinet"] = "ALTHO" if cab == "ALTHO" else "AE"
    tmi = round(float(str(dossier["tmi"]).replace(",", ".").rstrip("%")) * (1 if float(str(dossier["tmi"]).replace(",", ".").rstrip("%")) > 1 else 100))
    tranches = {0: "0", 11: "0.11", 30: "0.30", 41: "0.41", 45: "0.45"}
    if tmi not in tranches:
        print(f"Tranche marginale invalide : {dossier['tmi']} (attendu 0, 11, 30, 41 ou 45)", file=sys.stderr)
        sys.exit(2)
    etat["tmi"] = tranches[tmi]
    etat["fraisAuCout"] = "1" if dossier.get("fraisAuCout") else "0"
    etat["typeTravaux"] = "construction" if str(etat.get("typeTravaux", "")).startswith("constr") else "amelioration"
    return etat


def generer(dossier: dict, sortie: Path) -> dict:
    from playwright.sync_api import sync_playwright

    etat = preparer(dossier)
    with sync_playwright() as p:
        nav = p.chromium.launch()
        page = nav.new_page()
        erreurs = []
        page.on("pageerror", lambda e: erreurs.append(str(e)))
        page.add_init_script(f"localStorage.setItem('comparateur-sci-ir-is-v1', {json.dumps(json.dumps(etat))});")
        page.goto(HTML.as_uri())
        page.wait_for_selector(".verdict")
        page.evaluate("document.fonts.ready")
        if erreurs:
            raise RuntimeError("; ".join(erreurs))
        resume = page.evaluate(
            """() => {
              const r = Moteur.simuler(parametres(), tauxPerso()), S = r.synthese, k = (s) => ({
                impotsDetention: Math.round(s.impotsDetention), impotsRevente: Math.round(s.impotsRevente),
                honoraires: Math.round(s.honoraires), impotsTotal: Math.round(s.impotsTotal),
                enrichissement: Math.round(s.enrichissement), tri: s.tri == null ? null : Math.round(s.tri * 10000) / 100 });
              return { verdict: document.querySelector('.verdict p').innerText,
                       detail: document.querySelector('.verdict p.sub').innerText,
                       ir: k(S.ir), is: k(S.is), ecartIS_moins_IR: Math.round(r.ecart),
                       apport: Math.round(r.apport), prixRevente: Math.round(r.prixVente), alertes: r.alertes,
                       pages: document.querySelectorAll('.page').length };
            }"""
        )
        page.pdf(path=str(sortie), format="A4", print_background=True, prefer_css_page_size=True)
        nav.close()
    resume["pdf"] = str(sortie)
    return resume


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    source = Path(sys.argv[1])
    dossier = json.loads(source.read_text(encoding="utf-8"))
    sortie = Path(sys.argv[2]) if len(sys.argv) > 2 else source.with_suffix(".pdf")
    print(json.dumps(generer(dossier, sortie), ensure_ascii=False, indent=2))
