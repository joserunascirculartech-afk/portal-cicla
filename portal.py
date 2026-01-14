import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Portal CICLA", page_icon="🌐", layout="centered")

# CSS para estilizar los botones y el título
st.markdown("""
<style>
    div.stButton > button {
        width: 100%;
        height: 60px;
        font-size: 20px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Encabezado
st.title("🌐 Portal de Aplicaciones CICLA")
st.write("Selecciona la herramienta que deseas utilizar:")

st.write("---")

# --- COLUMNAS PARA LOS PROGRAMAS ---
col1, col2 = st.columns(2)

with col1:
    st.image("https://cdn-icons-png.flaticon.com/512/2921/2921226.png", width=100) # Icono de herramienta
    st.header("Servicio Técnico")
    st.info("Gestión de tickets, estados, repuestos y correos a clientes.")
    
    # ⚠️ AQUÍ PEGAS EL LINK DE TU APP DE TÉCNICO
    st.link_button("🚀 ABRIR PROGRAMA", "https://appserviciotecnico-kfwyym9liv6pt9qgdctj5b.streamlit.app")

with col2:
    st.image("https://cdn-icons-png.flaticon.com/512/265/265682.png", width=100) # Icono de archivo/programa
    st.header("Otro Programa")
    st.info("Descripción breve de tu segundo programa (ej: Calculadora, Stock, etc).")
    
    # ⚠️ AQUÍ PEGAS EL LINK DE TU OTRO PROGRAMA
    st.link_button("🚀 ABRIR PROGRAMA", "https://tu-otro-link.streamlit.app")

st.write("---")
st.caption("© 2026 CICLA 3D - Panel de Control Interno")