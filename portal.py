import streamlit as st

# ==========================================
# 🎨 CONFIGURACIÓN DE TU MARCA (LINKS ACTUALIZADOS)
# ==========================================

# Hemos convertido tus links a formato "raw" para que funcionen:
URL_LOGO = "https://raw.githubusercontent.com/joserunascirculartech-afk/portal-cicla/main/logo%20tricolor.png" 
URL_BANNER = "https://raw.githubusercontent.com/joserunascirculartech-afk/portal-cicla/main/Color.jpeg"

# 2. COLORES DE CICLA (Extraídos de tu logo)
AZUL_CICLA = "#009FE3"   # Azul brillante
GRIS_TEXTO = "#666666"   # Gris oscuro para textos

# Usaremos el Azul CICLA como color principal
COLOR_PRINCIPAL = AZUL_CICLA 

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Portal CICLA 3D", page_icon=URL_LOGO, layout="centered")

# ==========================================
# 🔐 SISTEMA DE SEGURIDAD
# ==========================================
def check_password():
    if st.session_state.get("portal_access", False):
        return True

    # Login con estilo
    st.markdown("<br>", unsafe_allow_html=True)
    col_x, col_y, col_z = st.columns([1,2,1])
    with col_y:
        # Mostramos el logo en el login
        try: st.image(URL_LOGO, use_container_width=True)
        except: st.header("🔐 Acceso CICLA")
            
    st.markdown(f"<h3 style='text-align: center; color: {GRIS_TEXTO};'>Acceso Corporativo</h3>", unsafe_allow_html=True)
    
    password_input = st.text_input("Ingrese Clave", type="password")
    
    if st.button("Entrar"):
        clave_real = st.secrets.get("password_portal", "admin")
        if password_input == clave_real:
            st.session_state["portal_access"] = True
            st.rerun()
        else:
            st.error("❌ Clave incorrecta")
    return False

if not check_password():
    st.stop()

# ==========================================
# 🎨 ESTILOS CSS (DISEÑO MARCA)
# ==========================================
st.markdown(f"""
<style>
    /* Fondo de los botones grandes */
    .stButton button {{
        width: 100%;
        border-radius: 12px;
        font-weight: bold !important;
        border: 2px solid {COLOR_PRINCIPAL};
        color: {GRIS_TEXTO};
    }}
    
    /* Botones PRIMARIOS (Apps) llenos de color */
    button[kind="primary"] {{
        background: linear-gradient(90deg, {AZUL_CICLA} 0%, {AZUL_CICLA} 100%);
        color: white !important;
        border: none !important;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        transition: 0.3s;
    }}
    button[kind="primary"]:hover {{
        opacity: 0.9;
        transform: scale(1.02);
    }}
    
    /* Textos y Títulos */
    h1 {{ color: {GRIS_TEXTO}; }}
    h3 {{ color: {COLOR_PRINCIPAL}; }}
    
    /* Ajuste de imágenes */
    img {{ margin-bottom: 10px; }}
</style>
""", unsafe_allow_html=True)

# ==========================================
# 🚀 INTERFAZ VISUAL DEL PORTAL
# ==========================================

# 1. BANNER SUPERIOR (La ilustración Color.jpeg)
try:
    st.image(URL_BANNER, use_container_width=True)
except:
    pass 

st.markdown("<br>", unsafe_allow_html=True)

# 2. CABECERA CON LOGO
col_L1, col_L2 = st.columns([1, 4])
with col_L1:
    try: st.image(URL_LOGO, use_container_width=True)
    except: st.write("⚙️")
with col_L2:
    st.title("Portal CICLA 3D")
    st.write("Panel central de herramientas y gestión.")

st.divider()

# 3. BOTONES DE ACCESO
col1, col2 = st.columns(2)

# === COLUMNA 1: SERVICIO TÉCNICO ===
with col1:
    st.markdown(f"### 🔧 Servicio Técnico")
    st.info("Gestión de reparaciones y recepción.")
    
    st.link_button(
        "🚀 APP DE GESTIÓN", 
        "https://joserunascirculartech-afk-appserviciotecnico-jzfg7fwfxrmytk2u8.streamlit.app",
        type="primary"
    )
    
    st.link_button(
        "📝 FORMULARIO INGRESO", 
        "https://docs.google.com/forms/d/e/1FAIpQLScY9Y9zsbNmmDkUmuLBf50NFjQEDFMbCsfqshna3gkxnabUhg/viewform?usp=header"
    )

# === COLUMNA 2: TABLERO CICLA ===
with col2:
    st.markdown(f"### 📊 Tablero CICLA")
    st.info("Panel de control y registros.")
    
    st.link_button(
        "🚀 TABLERO DIGITAL", 
        "https://tablero-cicla-943vm643tkgxdwrtld58yp.streamlit.app",
        type="primary"
    )
    
    st.link_button(
        "📝 FORMULARIO REGISTRO", 
        "https://docs.google.com/forms/d/e/1FAIpQLScY9Y9zsbNmmDkUmuLBf50NFjQEDFMbCsfqshna3gkxnabUhg/viewform?usp=dialog"
    )

st.divider()

# Botón Salir
c1, c2, c3 = st.columns([2,1,2])
with c2:
    if st.button("🔒 Cerrar Sesión"):
        st.session_state["portal_access"] = False
        st.rerun()

st.markdown(f"<p style='text-align: center; color: grey; font-size: 12px;'>© 2026 CICLA 3D</p>", unsafe_allow_html=True)
