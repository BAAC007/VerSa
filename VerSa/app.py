import streamlit as st
import os
from core.sanitizador import sanitizar_pdf, sanitizar_imagen
from core.analizador import extraer_texto_pdf, analizar_con_ia_local

st.set_page_config(page_title="VerSa | Investigación Segura", page_icon="🛡️", layout="centered")

st.title("🛡️ VerSa")
st.markdown("### Ingesta, Sanitización y Análisis Local")
st.info("Los archivos se procesan en tu máquina. Nada sale a la nube.")

uploaded_file = st.file_uploader("Arrastra un PDF o Imagen aquí", type=["pdf", "jpg", "png", "jpeg"])

if uploaded_file is not None:
    dir_uploads = "uploads"
    dir_sanitized = "sanitized"
    os.makedirs(dir_uploads, exist_ok=True)
    os.makedirs(dir_sanitized, exist_ok=True)
    
    nombre_original = uploaded_file.name
    ruta_cruda = os.path.join(dir_uploads, nombre_original)
    ruta_limpia = os.path.join(dir_sanitized, f"sanitized_{nombre_original}")
    
    with open(ruta_cruda, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    with st.spinner("🔒 Sanitizando metadatos..."):
        if nombre_original.lower().endswith('.pdf'):
            exito = sanitizar_pdf(ruta_cruda, ruta_limpia)
        else:
            exito = sanitizar_imagen(ruta_cruda, ruta_limpia)
            
    if exito:
        st.success("✅ Documento sanitizado correctamente.")
        
        if nombre_original.lower().endswith('.pdf'):
            with st.spinner("🤖 Qwen2.5 está analizando el contenido..."):
                texto = extraer_texto_pdf(ruta_limpia)
                analisis = analizar_con_ia_local(texto)
                
            st.markdown("### 📝 Análisis de VerSa")
            st.markdown(analisis.replace("\n", "  \n"))
            
        with open(ruta_limpia, "rb") as f:
            st.download_button(
                label="⬇️ Descargar archivo seguro",
                data=f,
                file_name=f"SEGUR0_{nombre_original}",
                mime="application/octet-stream"
            )
            
        if os.path.exists(ruta_cruda):
            os.remove(ruta_cruda)
    else:
        st.error("❌ Falló el proceso de sanitización.")
