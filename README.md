# 🛡️ VerSa (Verificación Segura)

> **Proyecto Académico** | Desarrollo de Aplicaciones Web (DAW)  
> *Herramienta de ingesta, sanitización de metadatos y análisis local con IA para investigación periodística.*

## 📌 Descripción
VerSa es una aplicación web local diseñada para proteger la identidad de las fuentes y agilizar el análisis de documentos sensibles. Permite subir archivos (PDF, imágenes), eliminar automáticamente sus metadatos y obtener un resumen estructurado con extracción de entidades utilizando **Inteligencia Artificial local** (Ollama + Qwen2.5), garantizando que ningún dato sale de la máquina del usuario.

## 🚀 Instalación y Uso
1. Instalar dependencias del sistema: `sudo apt install libimage-exiftool-perl`
2. Crear entorno virtual: `python3 -m venv venv && source venv/bin/activate`
3. Instalar paquetes: `pip install -r requirements.txt`
4. Iniciar IA local: `ollama pull qwen2.5:3b && ollama serve`
5. Ejecutar app: `streamlit run app.py`
