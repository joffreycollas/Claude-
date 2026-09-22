"""Assemble l'application en un seul fichier HTML autonome (polices embarquées)."""
import base64
from pathlib import Path

ICI = Path(__file__).parent
POLICES = {
    "/*FONT_SANS*/": "HankenGrotesk-normal-latin.woff2",
    "/*FONT_SERIF*/": "SourceSerif4-normal-latin.woff2",
    "/*FONT_SERIF_ITALIC*/": "SourceSerif4-italic-latin.woff2",
}
out = (ICI / "index.src.html").read_text(encoding="utf-8")
for marque, fichier in POLICES.items():
    out = out.replace(marque, base64.b64encode((ICI / "fonts" / fichier).read_bytes()).decode())
dest = ICI.parent / "Courriers_ALTHO.html"
dest.write_text(out, encoding="utf-8")
print(f"{dest.name} : {len(out) // 1024} Ko")
