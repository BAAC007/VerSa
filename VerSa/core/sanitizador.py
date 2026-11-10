import os
import subprocess
import pikepdf
from pypdf import PdfReader, PdfWriter

def sanitizar_pdf(ruta_entrada: str, ruta_salida: str) -> bool:
    try:
        with pikepdf.open(ruta_entrada) as pdf:
            with pdf.open_metadata() as meta:
                meta.clear()
            pdf.save(ruta_salida)
        
        lector = PdfReader(ruta_salida)
        escritor = PdfWriter()
        for pagina in lector.pages:
            escritor.add_page(pagina)
        
        with open(ruta_salida, "wb") as f:
            escritor.write(f)
        return True
    except Exception as e:
        print(f"Error sanitizando PDF: {e}")
        return False

def sanitizar_imagen(ruta_entrada: str, ruta_salida: str) -> bool:
    try:
        subprocess.run(["exiftool", "-all=", "-overwrite_original", ruta_entrada], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        os.rename(ruta_entrada, ruta_salida)
        return True
    except Exception as e:
        print(f"Error sanitizando imagen: {e}")
        return False
