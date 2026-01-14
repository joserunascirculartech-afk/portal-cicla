import streamlit as st

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="Portal CICLA", page_icon="🔐", layout="centered")

# ==========================================
# 🔐 SISTEMA DE SEGURIDAD (EL PORTERO)
# ==========================================
def check_password():
    """Retorna True si el usuario ingresó la clave correcta."""
    
    # Si ya se validó antes, pase adelante
    if st.session_state.get("portal_access", False):
        return True

    # Pantalla de Login
    st.markdown("### 🔐 Portal Corporativo CICLA")
    st.write("Ingrese clave de acceso para ver las herramientas.")
    
    password_input = st.text_input("Clave de Acceso", type="password")
    
    if st.button("Entrar"):
        # Busca la clave en los Secrets (o usa "admin" si no la configuraste)
        clave_real = st.secrets.get("password_portal", "admin")
        
        if password_input == clave_real:
            st.session_state["portal_access"] = True
            st.rerun() # Recarga la página para mostrar el contenido
        else:
            st.error("❌ Clave incorrecta")

    return False

# 🛑 SI NO TIENE CLAVE, EL CÓDIGO SE DETIENE AQUÍ
if not check_password():
    st.stop()

# ==========================================
# 🚀 CONTENIDO DEL PORTAL (SOLO VISIBLE CON CLAVE)
# ==========================================

# CSS para botones bonitos
st.markdown("""
<style>
    div.stButton > a {
        text-decoration: none;
    }
    .stButton button {
        width: 100%;
        font-weight: bold !important;
        border-radius: 8px;
        border: 1px solid #ddd;
    }
</style>
""", unsafe_allow_html=True)

# Encabezado con Logo
col_logo, col_titulo = st.columns([1, 4])
with col_logo:
    st.image("https://cdn-icons-png.flaticon.com/512/2921/2921226.png", width=70)
with col_titulo:
    st.title("Portal CICLA 3D")
    st.success("✅ Acceso Autorizado") # Pequeña confirmación visual

st.write("Selecciona la herramienta o formulario:")
st.divider()

# --- COLUMNAS PRINCIPALES ---
col1, col2 = st.columns(2)

# === COLUMNA 1: SERVICIO TÉCNICO ===
with col1:
    st.header("🔧 Servicio Técnico")
    st.info("Gestión de reparaciones y recepción.")
    
    # Botón 1: App Gestión
    st.link_button(
        "🚀 ABRIR APP DE GESTIÓN", 
        "https://joserunascirculartech-afk-appserviciotecnico-jzfg7fwfxrmytk2u8.streamlit.app",
        type="primary"
    )
    
    # Botón 2: Formulario
    st.link_button(
        "📝 ABRIR FORMULARIO INGRESO", 
        "https://docs.google.com/forms/d/e/1FAIpQLSe98Z6PkrIJhHmO5ppWFFxiXvHk2QrsVZX3nWyAY6Tw8UZ12Q/viewform?usp=header"
    )

# === COLUMNA 2: TABLERO CICLA ===
with col2:
    st.header("📊 Tablero CICLA")
    st.info("Panel de control y registros.")
    
    # Botón 1: App Tablero
    st.link_button(
        "🚀 ABRIR TABLERO DIGITAL", 
        "https://tablero-cicla-943vm643tkgxdwrtld58yp.streamlit.app",
        type="primary"
    )
    
    # Botón 2: Formulario
    st.link_button(
        "📝 ABRIR FORMULARIO REGISTRO", 
        "https://docs.google.com/forms/d/e/1FAIpQLScY9Y9zsbNmmDkUmuLBf50NFjQEDFMbCsfqshna3gkxnabUhg/viewform?usp=header"
    )

st.divider()
if st.button("🔒 Cerrar Sesión"):
    st.session_state["portal_access"] = False
    st.rerun()
