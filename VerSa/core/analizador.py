import requests
from pypdf import PdfReader

def extraer_texto_pdf(ruta_archivo: str) -> str:
    try:
        lector = PdfReader(ruta_archivo)
        texto = ""
        for i, pagina in enumerate(lector.pages[:5]):
            texto += pagina.extract_text() or ""
        return texto[:4000]
    except Exception as e:
        return f"Error extrayendo texto: {e}"

def analizar_con_ia_local(texto: str, modelo: str = "qwen2.5:3b") -> str:
    if not texto.strip():
        return "No se pudo extraer texto del documento."
        
    prompt = f"""Eres un editor de investigación periodística experto en análisis de documentos sensibles.
IMPORTANTE: Extrae TODOS los datos concretos (nombres, siglas, fechas, cifras, formatos, roles, referencias legales). No generalices.

Analiza el siguiente texto con máximo detalle y devuelve SOLO:
1. 📌 RESUMEN EJECUTIVO (3-4 líneas): Idea central, contexto y relevancia periodística.
2. 👥 PERSONAS: Lista de nombres completos mencionados (si no hay, di "Ninguna identificada").
3. 🏢 ORGANIZACIONES: Empresas, instituciones, organismos mencionados.
4. 📅 FECHAS CLAVE: Fechas específicas o rangos temporales importantes.
5. 💰 DATOS ECONÓMICOS: Cifras, montos, presupuestos, contratos mencionados.
6. 🚨 ALERTAS DE INTERÉS: Cualquier dato sensible, contradictorio, sospechoso o que merezca seguimiento.
7. 🔍 PREGUNTAS DE INVESTIGACIÓN: 3 preguntas que un periodista debería hacer tras leer esto.

Si algún campo no tiene información, indícalo explícitamente. No inventes datos.

TEXTO A ANALIZAR:
{texto}
"""
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": modelo, "prompt": prompt, "stream": False},
            timeout=120
        )
        return response.json().get("response", "Error: La IA no devolvió respuesta.")
    except requests.exceptions.ConnectionError:
        return "❌ Error: No se pudo conectar con Ollama. Ejecuta 'ollama serve'."
    except Exception as e:
        return f"❌ Error en la IA: {e}"
