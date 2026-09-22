"""Génère le classeur Excel de publipostage « Courrier augmentation tarifaire ».

Usage : python generer_courrier.py  ->  Courrier_augmentation_tarifaire.xlsx
"""
import math

from openpyxl import Workbook
from openpyxl.comments import Comment
from openpyxl.formatting.rule import FormulaRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.workbook.defined_name import DefinedName
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.utils import get_column_letter

SORTIE = "Courrier_augmentation_tarifaire.xlsx"
FONT = "Arial"

BLEU_SAISIE = "0000FF"
JAUNE = PatternFill("solid", fgColor="FFF2CC")
BLEU_FONCE = "1F3864"
ENTETE = PatternFill("solid", fgColor=BLEU_FONCE)
GRIS_CLAIR = PatternFill("solid", fgColor="F2F2F2")
fin = Side(style="thin", color="BFBFBF")
BORD = Border(left=fin, right=fin, top=fin, bottom=fin)
EUR = '#,##0" €";-#,##0" €";"—"'
PCT = '0.0%;-0.0%;"—"'


def f(size=10, bold=False, color="000000", italic=False):
    return Font(name=FONT, size=size, bold=bold, color=color, italic=italic)


wb = Workbook()

# ---------------------------------------------------------------- Paramètres
wp = wb.active
wp.title = "Paramètres"
wp.column_dimensions["A"].width = 34
wp.column_dimensions["B"].width = 110
wp["A1"] = "PARAMÈTRES DU COURRIER"
wp["A1"].font = f(14, True, BLEU_FONCE)
wp["A2"] = ("Cellules sur fond jaune / texte bleu = à personnaliser. "
            "Balises utilisables dans les textes : {cabinet} {societe} {date_effet} {hausse}")
wp["A2"].font = f(9, italic=True, color="7F7F7F")

params = [
    # (nom défini, libellé, valeur, format, commentaire)
    ("__titre", "Coordonnées du cabinet", None, None, None),
    ("Cab_Nom", "Nom du cabinet", "CABINET EXEMPLE EXPERTISE", None, None),
    ("Cab_Adr1", "Adresse", "12 rue de la République", None, None),
    ("Cab_CPVille", "Code postal et ville", "69002 LYON", None, None),
    ("Cab_Ville", "Ville (lieu de signature)", "Lyon", None, None),
    ("Cab_Contact", "Téléphone / e-mail", "Tél. 04 00 00 00 00  ·  contact@cabinet-exemple.fr", None, None),
    ("Cab_Mentions", "Mentions légales (pied de page)",
     "SAS au capital de 10 000 € · SIRET 000 000 000 00000 · Société d'expertise comptable inscrite "
     "au Tableau de l'Ordre de la région Auvergne-Rhône-Alpes", None, None),
    ("Signataire", "Nom du signataire", "Jean MARTIN", None, None),
    ("Signataire_Titre", "Fonction du signataire", "Expert-comptable associé", None, None),
    ("__titre", "Dates", None, None, None),
    ("Date_Courrier", "Date du courrier", "=TODAY()", "dd/mm/yyyy",
     "Par défaut : date du jour. Vous pouvez saisir une date fixe (ex. 01/12/2026)."),
    ("Date_Effet", "Date d'effet des nouveaux tarifs", "__DATE_EFFET", "dd/mm/yyyy", None),
    ("__titre", "Taux d'augmentation par défaut (par mission)", None, None, None),
    ("Taux_Compta", "Comptabilité", 0.035, "0.0%",
     "Taux appliqué à tous les clients, sauf taux personnalisé saisi dans l'onglet Clients."),
    ("Taux_Paye", "Paye / social", 0.04, "0.0%", None),
    ("Taux_Jur", "Juridique", 0.03, "0.0%", None),
    ("Taux_PA", "Plateforme agréée (facturation électronique)", 0.0, "0.0%", None),
    ("Pas_Arrondi", "Arrondi des nouveaux honoraires (en €)", 1, "0",
     "1 = à l'euro près, 5 = aux 5 € supérieurs, 10 = aux 10 € supérieurs…"),
    ("Nb_Mensualites", "Nombre d'échéances par an (mensualisation)", 12, "0",
     "Utilisé pour afficher le montant de la mensualité HT sous le tableau. 0 = ligne masquée."),
    ("Taux_TVA", "Taux de TVA", 0.2, "0.0%", None),
    ("__titre", "Libellés des missions (tels qu'imprimés dans le courrier)", None, None, None),
    ("Lib_Compta", "Mission 1", "Mission comptable (tenue, révision, bilan, liasse fiscale)", None, None),
    ("Lib_Paye", "Mission 2", "Mission sociale (bulletins de paie, DSN, déclarations sociales)", None, None),
    ("Lib_Jur", "Mission 3", "Mission juridique (approbation des comptes, secrétariat juridique)", None, None),
    ("Lib_PA", "Mission 4", "Plateforme agréée – facturation électronique", None, None),
    ("__titre", "Textes du courrier (modifiables — laissez vide pour supprimer un paragraphe)", None, None, None),
    ("Txt_Objet", "Objet", "Objet : révision de nos honoraires au {date_effet}", None, None),
    ("Txt_P1", "Paragraphe 1",
     "Nous tenons tout d'abord à vous remercier pour la confiance que vous accordez à {cabinet}. "
     "Comme chaque année, et conformément aux dispositions de votre lettre de mission, nous procédons "
     "à la révision de nos honoraires.", None, None),
    ("Txt_P2", "Paragraphe 2",
     "Cette révision, que nous avons souhaitée mesurée, tient compte de l'évolution de nos charges "
     "(rémunération et formation continue de nos collaborateurs, logiciels, sécurité informatique) "
     "ainsi que du renforcement constant des obligations comptables, fiscales, sociales et juridiques "
     "qui s'imposent à votre entreprise.", None, None),
    ("Txt_P3", "Paragraphe 3 (facturation électronique)",
     "L'année à venir est également marquée par la généralisation de la facturation électronique : "
     "depuis le 1er septembre 2026, toutes les entreprises doivent être en mesure de recevoir leurs "
     "factures électroniques via une plateforme agréée, et l'obligation d'émission s'étendra aux PME "
     "et micro-entreprises au 1er septembre 2027. Notre cabinet vous accompagne dans cette transition "
     "grâce à une solution de plateforme agréée directement intégrée à votre dossier.", None, None),
    ("Txt_P4", "Paragraphe 4 (avant le tableau)",
     "À compter du {date_effet}, vos honoraires annuels hors taxes évolueront ainsi "
     "(évolution globale : {hausse}) :", None, None),
    ("Txt_P5", "Paragraphe 5 (après le tableau)",
     "Les autres conditions de votre lettre de mission demeurent inchangées. Les nouveaux montants "
     "seront appliqués automatiquement sur vos prochaines factures et échéances de prélèvement.",
     None, None),
    ("Txt_P6", "Paragraphe 6",
     "Votre interlocuteur habituel reste à votre entière disposition pour répondre à vos questions "
     "et faire le point sur l'évolution de vos besoins.", None, None),
    ("Txt_Politesse", "Formule de politesse",
     "Nous vous prions d'agréer, {civilite}, l'expression de nos salutations distinguées.", None,
     "{civilite} est remplacé par Madame / Monsieur / Madame, Monsieur selon la civilité du client."),
]

r = 4
nom_vers_cellule = {}
for nom, lib, val, fmt, com in params:
    if nom == "__titre":
        r += 1
        wp.cell(r, 1, lib).font = f(11, True, "FFFFFF")
        wp.cell(r, 1).fill = ENTETE
        wp.cell(r, 2).fill = ENTETE
        r += 1
        continue
    wp.cell(r, 1, lib).font = f(10)
    c = wp.cell(r, 2)
    if val == "__DATE_EFFET":
        c.value = "=DATE(YEAR(Date_Courrier)+1,1,1)"
        c.comment = Comment("Par défaut : 1er janvier de l'année suivante. Saisissez une autre date si besoin.",
                            "Modèle")
    else:
        c.value = val
    c.font = f(10, color=BLEU_SAISIE)
    c.fill = JAUNE
    c.border = BORD
    c.alignment = Alignment(wrap_text=True, vertical="top", horizontal="left")
    if fmt:
        c.number_format = fmt
    if com:
        c.comment = Comment(com, "Modèle")
    if isinstance(val, str) and len(val) > 100:
        wp.row_dimensions[r].height = 13 * math.ceil(len(val) / 105) + 3
    wb.defined_names[nom] = DefinedName(nom, attr_text=f"'Paramètres'!$B${r}")
    nom_vers_cellule[nom] = f"'Paramètres'!$B${r}"
    r += 1

# Liste des mois (pour écrire les dates en toutes lettres, indépendamment de la langue d'Excel)
r += 2
wp.cell(r, 1, "Mois (usage interne)").font = f(9, italic=True, color="7F7F7F")
mois = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août",
        "septembre", "octobre", "novembre", "décembre"]
for i, m in enumerate(mois):
    wp.cell(r + i, 2, m).font = f(9, color="7F7F7F")
wb.defined_names["Liste_Mois"] = DefinedName("Liste_Mois", attr_text=f"'Paramètres'!$B${r}:$B${r + 11}")
wp.freeze_panes = "A4"

# ---------------------------------------------------------------- Clients
wc = wb.create_sheet("Clients")
colonnes = [
    # (entête, largeur, type)  type: saisie / calc
    ("Code client", 12, "saisie"),         # A
    ("Civilité", 9, "saisie"),             # B
    ("Prénom", 13, "saisie"),              # C
    ("Nom", 16, "saisie"),                 # D
    ("Société", 28, "saisie"),             # E
    ("Adresse 1", 28, "saisie"),           # F
    ("Adresse 2", 18, "saisie"),           # G
    ("Code postal", 10, "saisie"),         # H
    ("Ville", 16, "saisie"),               # I
    ("Email", 26, "saisie"),               # J
    ("Compta actuel HT", 13, "saisie"),    # K
    ("Paye actuel HT", 13, "saisie"),      # L
    ("Juridique actuel HT", 13, "saisie"),  # M
    ("PA actuel HT", 13, "saisie"),        # N
    ("Taux perso (optionnel)", 12, "saisie"),  # O
    ("Compta nouveau HT", 13, "calc"),     # P
    ("Paye nouveau HT", 13, "calc"),       # Q
    ("Juridique nouveau HT", 13, "calc"),  # R
    ("PA nouveau HT", 13, "calc"),         # S
    ("Total actuel HT", 13, "calc"),       # T
    ("Total nouveau HT", 13, "calc"),      # U
    ("Écart HT", 11, "calc"),              # V
    ("Écart %", 9, "calc"),                # W
    ("À envoyer", 10, "saisie"),           # X
    ("Mode d'envoi", 12, "saisie"),        # Y
]
for i, (titre, larg, typ) in enumerate(colonnes, start=1):
    c = wc.cell(1, i, titre)
    c.font = f(10, True, "FFFFFF")
    c.fill = ENTETE if typ == "saisie" else PatternFill("solid", fgColor="548235")
    c.alignment = Alignment(wrap_text=True, horizontal="center", vertical="center")
    c.border = BORD
    wc.column_dimensions[get_column_letter(i)].width = larg
wc.row_dimensions[1].height = 32
wc.freeze_panes = "F2"

exemples = [
    ["C001", "M.", "Pierre", "DURAND", "SARL DURAND BÂTIMENT", "5 avenue des Tilleuls", "", "69100",
     "Villeurbanne", "p.durand@exemple.fr", 3600, 1800, 600, 240, None, "Oui", "Courrier"],
    ["C002", "Mme", "Sophie", "LEROY", "SAS LEROY CONSEIL", "Parc d'activités du Moulin", "Bât. B – 3 allée Verte",
     "38000", "Grenoble", "s.leroy@exemple.fr", 5400, 0, 900, 0, 0.025, "Oui", "Email"],
    ["C003", "", "", "", "EURL LES JARDINS DE CLAIRE", "18 chemin des Vignes", "", "69400",
     "Villefranche-sur-Saône", "contact@jardins-claire.fr", 2400, 1200, 0, 180, None, "Non", "Courrier"],
]
NB_LIGNES = 500
TAUX = {"P": ("K", "Taux_Compta"), "Q": ("L", "Taux_Paye"), "R": ("M", "Taux_Jur"), "S": ("N", "Taux_PA")}
for ligne in range(2, NB_LIGNES + 2):
    ex = exemples[ligne - 2] if ligne - 2 < len(exemples) else None
    if ex:
        saisies = ex[:15] + [None] * 8 + ex[15:]
        for col, v in enumerate(saisies, start=1):
            if v is not None and v != "" and colonnes[col - 1][2] == "saisie":
                wc.cell(ligne, col, v)
    for col, (nouv, (act, taux)) in zip("PQRS", TAUX.items()):
        wc[f"{col}{ligne}"] = (
            f'=IF(OR($A{ligne}="",N({act}{ligne})=0),0,'
            f'CEILING({act}{ligne}*(1+IF($O{ligne}="",{taux},$O{ligne}))-0.005,Pas_Arrondi))')
    wc[f"T{ligne}"] = f'=IF($A{ligne}="","",SUM(K{ligne}:N{ligne}))'
    wc[f"U{ligne}"] = f'=IF($A{ligne}="","",SUM(P{ligne}:S{ligne}))'
    wc[f"V{ligne}"] = f'=IF($A{ligne}="","",U{ligne}-T{ligne})'
    wc[f"W{ligne}"] = f'=IF(OR($A{ligne}="",N(T{ligne})=0),"",V{ligne}/T{ligne})'
    for col in range(1, len(colonnes) + 1):
        c = wc.cell(ligne, col)
        typ = colonnes[col - 1][2]
        c.font = f(10, color=BLEU_SAISIE if typ == "saisie" else "000000")
        c.border = BORD
        if typ == "calc":
            c.fill = GRIS_CLAIR
        lettre = get_column_letter(col)
        if lettre in "KLMNPQRSTUV" and len(lettre) == 1:
            c.number_format = EUR
        elif lettre in ("O", "W"):
            c.number_format = PCT
        elif lettre == "H":
            c.number_format = "@"

dv_civ = DataValidation(type="list", formula1='"M.,Mme,M. et Mme"', allow_blank=True)
dv_oui = DataValidation(type="list", formula1='"Oui,Non"', allow_blank=True)
dv_mode = DataValidation(type="list", formula1='"Courrier,Email,Les deux"', allow_blank=True)
for dv, plage in ((dv_civ, "B"), (dv_oui, "X"), (dv_mode, "Y")):
    wc.add_data_validation(dv)
    dv.add(f"{plage}2:{plage}{NB_LIGNES + 1}")
wc.auto_filter.ref = f"A1:Y{NB_LIGNES + 1}"
wc["O1"].comment = Comment("Laisser vide pour appliquer les taux par défaut de l'onglet Paramètres. "
                           "Sinon, ce taux remplace tous les taux pour ce client (ex. 2,5 %).", "Modèle")
wc["N1"].comment = Comment("Honoraires annuels HT de la plateforme agréée (facturation électronique). "
                           "Laisser à 0 si le client n'y a pas souscrit.", "Modèle")
wb.defined_names["Codes_Clients"] = DefinedName("Codes_Clients",
                                                attr_text=f"Clients!$A$2:$A${NB_LIGNES + 1}")

# ---------------------------------------------------------------- Courrier
wl = wb.create_sheet("Courrier")
wl.sheet_view.showGridLines = False
for col, larg in {"A": 1.5, "B": 44, "C": 14, "D": 9, "E": 14, "F": 13, "G": 3,
                  "H": 3, "I": 22, "J": 16, "K": 12, "L": 12, "M": 6, "N": 6, "O": 6}.items():
    wl.column_dimensions[col].width = larg

# Zone de pilotage (hors zone d'impression)
wl["I2"] = "CLIENT À ÉDITER ▼"
wl["I2"].font = f(10, True, "C00000")
wl["I3"] = "C001"
wl["I3"].font = f(12, True, BLEU_SAISIE)
wl["I3"].fill = JAUNE
wl["I3"].border = BORD
wl["I3"].alignment = Alignment(horizontal="center")
dv_cli = DataValidation(type="list", formula1="=Codes_Clients", allow_blank=False)
wl.add_data_validation(dv_cli)
dv_cli.add("I3")
wb.defined_names["Client_Selectionne"] = DefinedName("Client_Selectionne", attr_text="Courrier!$I$3")
wl["I4"] = '=IFERROR(INDEX(Clients!$E$2:$E$501,MATCH(Client_Selectionne,Codes_Clients,0)),"Code introuvable")'
wl["I4"].font = f(9, italic=True)
wl["I6"] = ("Choisissez le code client dans la liste, puis :\n"
            "Fichier > Exporter > PDF (1 client)\nou Fichier > Imprimer.\n"
            "Pour tous les clients : macro de l'onglet « Macro PDF ».")
wl["I6"].font = f(9, color="595959")
wl["I6"].alignment = Alignment(wrap_text=True, vertical="top")
wl.merge_cells("I6:L10")

# Cellules de calcul cachées (colonne J..O, lignes 1-4 et 30-33)
wl["J1"] = "Ligne client"
wl["K1"] = "=IFERROR(MATCH(Client_Selectionne,Codes_Clients,0),0)"


def cli(col):
    """Valeur de la colonne `col` de l'onglet Clients pour le client choisi."""
    return f'IF($K$1=0,"",INDEX(Clients!${col}$2:${col}$501,$K$1)&"")'


def cli_num(col):
    return f"IF($K$1=0,0,N(INDEX(Clients!${col}$2:${col}$501,$K$1)))"


wl["J2"] = "Civilité longue"
wl["K2"] = (f'=IF({cli("B")}="Mme","Madame",IF({cli("B")}="M.","Monsieur",'
            f'IF({cli("B")}="M. et Mme","Madame, Monsieur","Madame, Monsieur")))')
wl["J3"] = "Date effet texte"
wl["K3"] = '=DAY(Date_Effet)&IF(DAY(Date_Effet)=1,"er","")&" "&INDEX(Liste_Mois,MONTH(Date_Effet))&" "&YEAR(Date_Effet)'
wl["J4"] = "Hausse globale"


def balises(nom):
    """Texte paramétré avec remplacement des balises."""
    return (f'SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE({nom},'
            f'"{{cabinet}}",Cab_Nom),"{{societe}}",{cli("E")}),"{{date_effet}}",$K$3),'
            f'"{{hausse}}",$K$4),"{{civilite}}",$K$2)')


# Bloc expéditeur
wl["B2"] = "=Cab_Nom"
wl["B2"].font = f(15, True, BLEU_FONCE)
wl["B3"] = "=Cab_Adr1"
wl["B4"] = "=Cab_CPVille"
wl["B5"] = "=Cab_Contact"
for a in ("B3", "B4", "B5"):
    wl[a].font = f(9, color="404040")
wl.row_dimensions[2].height = 22
for rr in range(2, 6):
    wl.merge_cells(f"B{rr}:C{rr}")
wl["E2"] = '="Réf. client : "&Client_Selectionne'
wl["E2"].font = f(9, color="404040")
wl.merge_cells("E2:F2")
wl["E2"].alignment = Alignment(horizontal="right")
# filet sous l'en-tête
for col in "BCDEF":
    wl[f"{col}6"].border = Border(bottom=Side(style="medium", color=BLEU_FONCE))
wl.row_dimensions[6].height = 6

# Bloc destinataire (position fenêtre enveloppe DL/C5 à droite)
for rr in (7, 8, 9):
    wl.row_dimensions[rr].height = 14
dest = {
    10: f'={cli("E")}',
    11: f'=IF({cli("D")}="","","À l\'attention de "&TRIM({cli("B")}&" "&{cli("C")}&" "&{cli("D")}))',
    12: f'={cli("F")}',
    13: f'=IF({cli("G")}="",TRIM({cli("H")}&" "&UPPER({cli("I")})),{cli("G")})',
    14: f'=IF({cli("G")}="","",TRIM({cli("H")}&" "&UPPER({cli("I")})))',
}
for rr, formule in dest.items():
    wl[f"D{rr}"] = formule
    wl[f"D{rr}"].font = f(10.5, bold=(rr == 10))
    wl.merge_cells(f"D{rr}:F{rr}")
    wl.row_dimensions[rr].height = 15
wl.row_dimensions[15].height = 26

wl["D16"] = ('=Cab_Ville&", le "&DAY(Date_Courrier)&IF(DAY(Date_Courrier)=1,"er","")&" "'
             '&INDEX(Liste_Mois,MONTH(Date_Courrier))&" "&YEAR(Date_Courrier)')
wl.merge_cells("D16:F16")
wl.row_dimensions[17].height = 20

wl["B18"] = "=" + balises("Txt_Objet")
wl["B18"].font = f(10.5, True)
wl.merge_cells("B18:F18")
wl.row_dimensions[19].height = 14

wl["B20"] = "=$K$2&\",\""
wl.row_dimensions[21].height = 6

LARGEUR_CAR = 118  # caractères par ligne sur la largeur B:F


def paragraphe(ligne, nom, marge_apres=True):
    c = wl[f"B{ligne}"]
    c.value = "=" + balises(nom)
    c.alignment = Alignment(wrap_text=True, vertical="top", horizontal="justify")
    wl.merge_cells(f"B{ligne}:F{ligne}")
    texte = next(p[2] for p in params if p[0] == nom)
    nb = max(1, math.ceil(len(texte) / LARGEUR_CAR))
    wl.row_dimensions[ligne].height = 13 * nb + (11 if marge_apres else 0)


paragraphe(22, "Txt_P1")
paragraphe(23, "Txt_P2")
paragraphe(24, "Txt_P3")
paragraphe(25, "Txt_P4")
wl.row_dimensions[26].height = 4

# Tableau des honoraires
entetes = {"B": "Mission", "C": "Actuel HT", "D": "Évol.", "E": "Nouveau HT", "F": "Écart HT"}
for col, t in entetes.items():
    c = wl[f"{col}27"]
    c.value = t
    c.font = f(9.5, True, "FFFFFF")
    c.fill = ENTETE
    c.border = BORD
    c.alignment = Alignment(horizontal="left" if col == "B" else "center", vertical="center")
wl.row_dimensions[27].height = 18

# Calculs cachés des 4 missions (colonnes J à O, lignes 28-31)
missions = [("Lib_Compta", "K", "P"), ("Lib_Paye", "L", "Q"), ("Lib_Jur", "M", "R"), ("Lib_PA", "N", "S")]
wl["J27"], wl["K27"], wl["L27"], wl["M27"], wl["N27"], wl["O27"] = (
    "Libellé", "Actuel", "Nouveau", "Actif", "Rang", "k")
for i, (lib, act, nouv) in enumerate(missions):
    rr = 28 + i
    wl[f"J{rr}"] = f"={lib}"
    wl[f"K{rr}"] = "=" + cli_num(act)
    wl[f"L{rr}"] = "=" + cli_num(nouv)
    wl[f"M{rr}"] = f"=IF(OR(K{rr}<>0,L{rr}<>0),1,0)"
    wl[f"N{rr}"] = f'=IF(M{rr}=1,SUM($M$28:M{rr}),"")'
    wl[f"O{rr}"] = i + 1
    # Lignes visibles : k-ième mission souscrite (les missions à 0 disparaissent)
    idx = f"MATCH($O{rr},$N$28:$N$31,0)"
    wl[f"B{rr}"] = f'=IFERROR(INDEX($J$28:$J$31,{idx}),"")'
    wl[f"C{rr}"] = f'=IFERROR(INDEX($K$28:$K$31,{idx}),"")'
    wl[f"E{rr}"] = f'=IFERROR(INDEX($L$28:$L$31,{idx}),"")'
    wl[f"F{rr}"] = f'=IF(E{rr}="","",E{rr}-C{rr})'
    wl[f"D{rr}"] = f'=IF(OR(E{rr}="",N(C{rr})=0),"",E{rr}/C{rr}-1)'
    for col in "BCDEF":
        c = wl[f"{col}{rr}"]
        c.font = f(9.5)
        c.alignment = Alignment(horizontal="left" if col == "B" else "right", vertical="center",
                                wrap_text=(col == "B"))
    for col in "CEF":
        wl[f"{col}{rr}"].number_format = EUR
    wl[f"D{rr}"].number_format = '+0.0%;-0.0%;"—"'
    wl.row_dimensions[rr].height = 17
# Filet sous chaque ligne de mission uniquement si elle est remplie
wl.conditional_formatting.add("B28:F31", FormulaRule(formula=['$B28<>""'], border=Border(bottom=fin)))
wl["K4"] = '=IF(SUM($K$28:$K$31)=0,"",FIXED((SUM($L$28:$L$31)/SUM($K$28:$K$31)-1)*100,1)&" %")'

rt = 32
wl[f"B{rt}"] = "Total annuel HT"
wl[f"C{rt}"] = "=SUM(K28:K31)"
wl[f"E{rt}"] = "=SUM(L28:L31)"
wl[f"F{rt}"] = f"=E{rt}-C{rt}"
wl[f"D{rt}"] = f'=IF(N(C{rt})=0,"",E{rt}/C{rt}-1)'
for col in "BCDEF":
    c = wl[f"{col}{rt}"]
    c.font = f(10, True)
    c.fill = PatternFill("solid", fgColor="D9E1F2")
    c.border = Border(top=Side(style="thin", color=BLEU_FONCE), bottom=Side(style="thin", color=BLEU_FONCE))
    c.alignment = Alignment(horizontal="left" if col == "B" else "right", vertical="center")
for col in "CEF":
    wl[f"{col}{rt}"].number_format = EUR
wl[f"D{rt}"].number_format = '+0.0%;-0.0%;"—"'
wl.row_dimensions[rt].height = 18

wl["B33"] = ('=IF(N(Nb_Mensualites)=0,"","Soit "&FIXED(E32/Nb_Mensualites,2)&" € HT par échéance ("'
             '&Nb_Mensualites&" échéances), "&FIXED(E32/Nb_Mensualites*(1+Taux_TVA),2)&" € TTC.")')
wl["B33"].font = f(9, italic=True, color="404040")
wl.merge_cells("B33:F33")
wl.row_dimensions[34].height = 8

paragraphe(35, "Txt_P5")
paragraphe(36, "Txt_P6")
paragraphe(37, "Txt_Politesse")

wl["D39"] = "=Signataire"
wl["D39"].font = f(10.5, True)
wl["D40"] = "=Signataire_Titre"
wl["D40"].font = f(9.5, italic=True)
wl.merge_cells("D39:F39")
wl.merge_cells("D40:F40")
for rr in (41, 42, 43, 44):
    wl.row_dimensions[rr].height = 16

wl["B45"] = "=Cab_Mentions"
wl["B45"].font = f(7.5, color="7F7F7F")
wl["B45"].alignment = Alignment(horizontal="center", wrap_text=True, vertical="bottom")
wl.merge_cells("B45:F45")
wl.row_dimensions[45].height = 24
for col in "BCDEF":
    wl[f"{col}45"].border = Border(top=Side(style="thin", color="BFBFBF"))

# Police par défaut pour toutes les cellules du courrier sans style explicite
for row in wl.iter_rows(min_row=1, max_row=45, min_col=2, max_col=6):
    for c in row:
        if c.font.name != FONT:
            c.font = f(10)
for row in wl.iter_rows(min_row=1, max_row=31, min_col=10, max_col=15):
    for c in row:
        c.font = f(8, color="A6A6A6")
for a in ("B20", "D16"):
    wl[a].font = f(10)

# Mise en page A4
wl.print_area = "A1:G45"
wl.page_setup.paperSize = wl.PAPERSIZE_A4
wl.page_setup.orientation = "portrait"
wl.page_setup.fitToWidth = 1
wl.page_setup.fitToHeight = 1
wl.sheet_properties.pageSetUpPr.fitToPage = True
wl.print_options.horizontalCentered = True
wl.page_margins.left = wl.page_margins.right = 0.6
wl.page_margins.top = 0.5
wl.page_margins.bottom = 0.5
wl.page_margins.header = wl.page_margins.footer = 0.2

# ---------------------------------------------------------------- Mode d'emploi
wm = wb.create_sheet("Mode d'emploi", 0)
wm.sheet_view.showGridLines = False
wm.column_dimensions["A"].width = 3
wm.column_dimensions["B"].width = 110
lignes = [
    ("COURRIER D'AUGMENTATION TARIFAIRE — PUBLIPOSTAGE", f(16, True, BLEU_FONCE)),
    ("Compta · Paye · Juridique · Plateforme agréée", f(11, italic=True, color="595959")),
    ("", None),
    ("1. Onglet « Paramètres »", f(11, True)),
    ("Renseignez les coordonnées du cabinet, le signataire, la date d'effet, les taux d'augmentation par mission "
     "et, si besoin, adaptez les textes du courrier. Les balises {cabinet}, {societe}, {date_effet}, {hausse} "
     "et {civilite} sont remplacées automatiquement.", f(10)),
    ("", None),
    ("2. Onglet « Clients »", f(11, True)),
    ("Une ligne par client. Colonnes bleues = saisie ; colonnes vertes = calcul automatique (ne pas modifier). "
     "Saisissez les honoraires ANNUELS HT actuels par mission (0 ou vide si la mission n'est pas souscrite : "
     "elle n'apparaîtra pas dans le courrier). « Taux perso » remplace les taux par défaut pour ce client. "
     "Les 3 lignes d'exemple (C001 à C003) sont à remplacer par vos clients.", f(10)),
    ("", None),
    ("3. Onglet « Courrier » — un client à la fois", f(11, True)),
    ("Choisissez le code client dans la cellule jaune I3 : le courrier se remplit tout seul. "
     "Puis Fichier > Exporter > Créer un PDF (ou Enregistrer sous > PDF) pour l'envoi par e-mail, "
     "ou Fichier > Imprimer pour l'envoi postal. La mise en page A4 est déjà réglée (1 page, "
     "adresse du destinataire positionnée pour une enveloppe à fenêtre à droite).", f(10)),
    ("", None),
    ("4. Tous les clients d'un coup — macro « Macro PDF »", f(11, True)),
    ("Enregistrez le fichier au format .xlsm (Classeur Excel prenant en charge les macros), ouvrez l'éditeur VBA "
     "(Alt + F11), Insertion > Module, collez le code de l'onglet « Macro PDF » (ou importez le fichier "
     "Module_Courriers.bas). Lancez ensuite (Alt + F8) :\n"
     "  • ExporterTousLesPDF : un PDF par client dont « À envoyer » = Oui, dans le dossier Courriers_PDF\n"
     "  • ExporterUnSeulPDF : un seul PDF regroupant tous les courriers (pratique pour un envoi en masse)\n"
     "  • ImprimerCourriersPostaux : impression des clients « À envoyer » = Oui et mode Courrier / Les deux", f(10)),
    ("", None),
    ("5. Alternative : publipostage Word", f(11, True)),
    ("L'onglet « Clients » (en-têtes en ligne 1) peut aussi servir de source de données à un publipostage "
     "Word (Publipostage > Sélection des destinataires > Utiliser une liste existante).", f(10)),
    ("", None),
    ("Légende des couleurs", f(11, True)),
    ("Texte bleu sur fond jaune = cellule à renseigner  ·  Fond gris = formule  ·  "
     "Colonnes grises à droite du courrier (J à O) = calculs internes, non imprimés.", f(10)),
]
for i, (txt, police) in enumerate(lignes, start=2):
    c = wm.cell(i, 2, txt)
    if police:
        c.font = police
    c.alignment = Alignment(wrap_text=True, vertical="top")
    if len(txt) > 110 or "\n" in txt:
        wm.row_dimensions[i].height = 14 * (math.ceil(len(txt) / 120) + txt.count("\n")) + 4

# ---------------------------------------------------------------- Macro PDF
wv = wb.create_sheet("Macro PDF")
wv.column_dimensions["A"].width = 120
wv["A1"] = "Code VBA à coller dans un module (Alt + F11 > Insertion > Module), fichier enregistré en .xlsm"
wv["A1"].font = f(11, True, BLEU_FONCE)
with open("Module_Courriers.bas", encoding="utf-8") as fh:
    code = fh.read().splitlines()
for i, l in enumerate(code[1:], start=3):  # saute la ligne Attribute VB_Name
    c = wv.cell(i, 1, l)
    c.font = Font(name="Consolas", size=9)
    c.number_format = "@"
    if l.startswith("="):
        c.value = "'" + l

wb.active = 3  # ouvre sur le Courrier
wb.save(SORTIE)
print("OK ->", SORTIE)
