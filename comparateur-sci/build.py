"""Assemble le comparateur en un seul fichier HTML autonome (moteur, polices et images embarqués).

Usage : python comparateur-sci/build.py  ->  Comparateur_SCI_IR_IS.html à la racine du dépôt.
Polices et papier à en-tête repris de l'application Courriers (dossier app/).
"""
import base64
from pathlib import Path

ICI = Path(__file__).parent
APP = ICI.parent / "app"
b64 = lambda chemin: base64.b64encode(chemin.read_bytes()).decode()
REMPLACEMENTS = {
    "/*FONT_SANS*/": b64(APP / "fonts" / "HankenGrotesk-normal-latin.woff2"),
    "/*FONT_SERIF*/": b64(APP / "fonts" / "SourceSerif4-normal-latin.woff2"),
    "/*FONT_SERIF_ITALIC*/": b64(APP / "fonts" / "SourceSerif4-italic-latin.woff2"),
    "/*IMG_ENTETE*/": b64(APP / "assets" / "entete.png"),
    "/*IMG_PIED*/": b64(APP / "assets" / "pied.png"),
    "/*MOTEUR*/": (ICI / "moteur.js").read_text(encoding="utf-8").replace("</", "<\\/"),
}
out = (ICI / "index.src.html").read_text(encoding="utf-8")
for marque, contenu in REMPLACEMENTS.items():
    assert marque in out, marque
    out = out.replace(marque, contenu)
dest = ICI.parent / "Comparateur_SCI_IR_IS.html"
dest.write_text(out, encoding="utf-8")
print(f"{dest.name} : {len(out) // 1024} Ko")
