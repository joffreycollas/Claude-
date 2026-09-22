"""Assemble l'application en un seul fichier HTML autonome (polices embarquées)."""
import base64
from pathlib import Path

ICI = Path(__file__).parent
src = (ICI / "index.src.html").read_text(encoding="utf-8")
b64 = lambda f: base64.b64encode((ICI / "fonts" / f).read_bytes()).decode()
out = (src.replace("/*FONT_REGULAR*/", b64("SourceSans3-latin.woff2"))
          .replace("/*FONT_ITALIC*/", b64("SourceSans3-Italic-latin.woff2")))
dest = ICI.parent / "Courriers_ALTHO.html"
dest.write_text(out, encoding="utf-8")
print(f"{dest.name} : {len(out) // 1024} Ko")
