"""Assemble l'application en un seul fichier HTML autonome (polices embarquées)."""
import base64
from pathlib import Path

ICI = Path(__file__).parent
POLICES = {
    "/*FONT_SANS*/": "HankenGrotesk-normal-latin.woff2",
    "/*FONT_SERIF*/": "SourceSerif4-normal-latin.woff2",
    "/*FONT_SERIF_ITALIC*/": "SourceSerif4-italic-latin.woff2",
}
IMAGES = {
    "/*IMG_ENTETE*/": ICI / "assets" / "entete.png",
    "/*IMG_PIED*/": ICI / "assets" / "pied.png",
    "/*IMG_LOGO*/": ICI / "assets" / "logo.png",
    "/*MODELE_XLSX*/": ICI.parent / "Modele_import_clients.xlsx",  # produit par modele_import.py
}
b64 = lambda chemin: base64.b64encode(chemin.read_bytes()).decode()
out = (ICI / "index.src.html").read_text(encoding="utf-8")
for marque, fichier in POLICES.items():
    out = out.replace(marque, b64(ICI / "fonts" / fichier))
for marque, chemin in IMAGES.items():
    assert marque in out, marque
    out = out.replace(marque, b64(chemin))
dest = ICI.parent / "Courriers_ALTHO.html"
dest.write_text(out, encoding="utf-8")
print(f"{dest.name} : {len(out) // 1024} Ko")
