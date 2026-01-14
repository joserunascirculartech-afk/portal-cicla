import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Portal CICLA", page_icon="🌐", layout="centered")

# CSS para estilizar los botones y hacerlos grandes
st.markdown("""
<style>
    div.stButton > a {
        text-decoration: none;
    }
    .stButton button {
        width: 100%;
        height: 70px;
        font-size: 22px !important;
        font-weight: bold !important;
        border-radius: 10px;
        border: 2px solid #f0f2f6;
    }
</style>
""", unsafe_allow_html=True)

# Encabezado
st.image("https://cdn-icons-png.flaticon.com/512/2921/2921226.png", width=80)
st.title("🌐 Portal de Aplicaciones CICLA")
st.write("Bienvenido al panel central. Selecciona una herramienta:")

st.divider()

# --- COLUMNAS PARA LOS PROGRAMAS ---
col1, col2 = st.columns(2)

with col1:
    st.header("🔧 Servicio Técnico")
    st.info("Gestión de tickets, estados, repuestos y comunicación con clientes.")
    
    # ENLACE 1: App de Servicio Técnico
    st.link_button("🚀 ABRIR TALLER", "https://joserunascirculartech-afk-appserviciotecnico-jzfg7fwfxrmytk2u8.streamlit.app")

with col2:
    st.header("📊 Tablero CICLA")
    st.info("Panel de control, métricas y otras herramientas de gestión.")
    
    # ENLACE 2: App Tablero
    st.link_button("🚀 ABRIR TABLERO", "https://tablero-cicla-943vm643tkgxdwrtld58yp.streamlit.app")

st.divider()
st.caption("© 2026 CICLA 3D - Acceso Corporativo")
