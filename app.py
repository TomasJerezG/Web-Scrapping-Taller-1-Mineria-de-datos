"""
============================================================================
TALLER 2 - MINERÍA DE DATOS · Nature Machine Intelligence Dashboard
app.py — punto de entrada (orquestador de navegación)
============================================================================

Esta app usa st.navigation (Streamlit ≥1.36) para tener una navegación
multi-página con sidebar. Cada página vive en pages_app/<nombre>.py y
comparte filtros vía st.session_state.

Ejecutar:
    streamlit run app.py
============================================================================
"""

import streamlit as st

import database as db

# ----------------------------------------------------------------------------
# Configuración de la página
# ----------------------------------------------------------------------------
st.set_page_config(
    page_title="Nature MI · Cyberpunk Dashboard",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ----------------------------------------------------------------------------
# Pre-flight check: la BD debe existir
# ----------------------------------------------------------------------------
if not db.db_exists():
    st.error(
        "⚠️ No se encontró el archivo `revista_q1_2025.sqlite` en la raíz "
        "del proyecto. Asegúrate de copiarlo desde el Taller 1."
    )
    st.stop()

# ----------------------------------------------------------------------------
# Definición de páginas (sección "desplegable" — st.navigation)
# ----------------------------------------------------------------------------
pages = {
    "": [
        st.Page("pages_app/home.py", title="Inicio",
                icon="🏠", default=True),
    ],
    "ANÁLISIS": [
        st.Page("pages_app/indicators.py", title="Indicadores", icon="📊"),
        st.Page("pages_app/visualizations.py", title="Visualizaciones", icon="📈"),
        st.Page("pages_app/explore.py", title="Explorar artículos", icon="🗂️"),
    ],
    "ACCIONES": [
        st.Page("pages_app/update_db.py", title="Actualizar BD", icon="🔄"),
        st.Page("pages_app/about.py", title="Acerca de", icon="ℹ️"),
    ],
}

# Navegación
nav = st.navigation(pages, position="sidebar", expanded=True)
nav.run()
