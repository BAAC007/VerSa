# 🛡️ VerSa (Verificación Segura)

> **Proyecto Académico** | Desarrollo de Aplicaciones Web (DAW)  
> *Herramienta de ingesta, sanitización de metadatos y análisis local con IA para investigación periodística.*

## 📌 Descripción
VerSa es una aplicación web local diseñada para proteger la identidad de las fuentes y agilizar el análisis de documentos sensibles. Permite a periodistas o investigadores subir archivos (PDF, imágenes), eliminar automáticamente sus metadatos (EXIF, autor, ubicación) y obtener un resumen estructurado con extracción de entidades utilizando **Inteligencia Artificial local** (Ollama + Qwen2.5), garantizando que **ningún dato sale de la máquina del usuario**.

## ✨ Características Principales
- 🔒 **Sanitización automática**: Limpieza profunda de metadatos en PDFs (`pikepdf`, `pypdf`) e imágenes (`exiftool`).
- 🤖 **IA 100% Local**: Análisis de texto, extracción de entidades y generación de preguntas de investigación sin dependencia de APIs en la nube.
- 🐧 **Privacidad por diseño**: Arquitectura pensada para ejecutarse en entornos Linux autoalojados.
- ⚡ **Interfaz ligera**: Desarrollada con Streamlit para una interacción rápida y sencilla.

## 🛠️ Stack Tecnológico
- **Backend/Lógica**: Python 3.12+
- **Frontend**: Streamlit
- **Procesamiento de documentos**: `pypdf`, `pikepdf`, `Pillow`
- **IA Local**: Ollama (Modelo `qwen2.5` o `qwen2.5:3b`)
- **Herramientas del sistema**: `exiftool` (libimage-exiftool-perl)

## 🚀 Instalación y Uso

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/TU_USUARIO/VerSa.git
   cd VerSa

## Instalación de dependencias 

1. Instalación de dependencias del sistema:
   sudo apt update && sudo apt install libimage-exiftool-perl

2. Configurar entorno virtual Python:
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt

3. Preparar la IA Local (Requiere Ollama instalado):
   ollama pull qwen2.5:3b  # o qwen2.5 para mayor precisión si hay RAM suficiente
   ollama serve

4. Ejecutar la aplicación:
   streamlit run app.py
