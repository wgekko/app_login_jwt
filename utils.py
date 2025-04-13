# utils.py
import streamlit as st
import time
from datetime import datetime
import os
import base64

def login_user(username, role):
    st.session_state.user = username
    st.session_state.role = role
    st.session_state.login_time = time.time()
    st.session_state.token = {
        "exp": time.time() + 300,
        "refresh": time.time() + 120,
    }

def refresh_token():
    if "token" in st.session_state:
        if time.time() < st.session_state.token["refresh"]:
            st.session_state.token["exp"] = time.time() + 300

def is_token_expired():
    return "token" not in st.session_state or time.time() > st.session_state.token["exp"]

def require_auth(roles):
    if "user" not in st.session_state or "role" not in st.session_state:
        st.stop()

    if is_token_expired():
        st.warning("Sesión expirada. Redirigiendo al login...", icon=":material/warning:")
        time.sleep(1)
        st.markdown("<meta http-equiv='refresh' content='2;url=/'>", unsafe_allow_html=True)
        st.stop()

    refresh_token()

    if st.session_state.get("role") not in roles:
        st.error("Acceso denegado: No tienes permiso para ver esta página.", icon=":material/error:")
        st.stop()

    with st.sidebar:
        st.markdown(f"**Usuario :** `{st.session_state.user}`")
        st.markdown(f"**Rol :** `{st.session_state.role}`")
        st.markdown(f"**Inicio Sesión :** `{datetime.fromtimestamp(st.session_state.login_time).strftime('%H:%M:%S')}`")
        st.markdown(f"**Sesión Expira :** `{datetime.fromtimestamp(st.session_state.token['exp']).strftime('%H:%M:%S')}`")
        if st.button("Cerrar sesión", icon=":material/logout:"):
            st.session_state.clear()
            st.markdown("<meta http-equiv='refresh' content='0;url=/'>", unsafe_allow_html=True)
            st.stop()
        st.write("---")    
        st.sidebar.image("img/main-page.jpg",use_container_width=True)
def apply_custom_style():
    css_file = "asset/style.css"
    try:
        with open(css_file) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"No se encontró el archivo de estilo: {css_file}", icon=":material/cancel:")

# LOGO SEGÚN ROL
def show_logo_by_role():
    if "role" not in st.session_state:
        return

    role = st.session_state.role
    logo_map = {
        "admin": "img/usuario-administrador.gif",
        "usuario1": "img/user1.gif",
        "usuario2": "img/user2.gif",
    }

    logo_path = logo_map.get(role)

    # Verifica si el archivo existe antes de mostrarlo
    if logo_path and os.path.exists(logo_path):
        st.image(logo_path, caption=None, width=60, use_column_width=None, clamp=False, channels="RGB", output_format="auto", use_container_width=False)
    else:
        st.warning("No se pudo cargar el logo para este rol.", icon=":material/warning:")

def show_logo():
    logo_path = "img/tareas.gif"  # Cambia por el nombre correcto de tu gif
    st.markdown(
        f"""
        <div style='text-align:center; margin-top: 20px; animation: fadeIn 2s ease-in-out;'>
            <img src='{logo_path}' style='width:200px; border-radius:15px;' />
        </div>
        """,
        unsafe_allow_html=True
    )

#""" imagen de background"""
#def add_local_background_image(image):
#  with open(image, "rb") as image:
#    encoded_string = base64.b64encode(image.read())
#    st.markdown(
#      f"""
#      <style>
#      .stApp{{
#        background-image: url(data:files/{"jpg"};base64,{encoded_string.decode()});
#      }}    
#      </style>
#      """,
#      unsafe_allow_html=True
#    )
#add_local_background_image("img/fondo.jpg")


#""" imagen de sidebar"""
#def add_local_sidebar_image(image):
#  with open(image, "rb") as image:
#    encoded_string = base64.b64encode(image.read())
#    st.markdown(
#      f"""
#      <style>
#      .stSidebar{{
#        background-image: url(data:files/{"jpg"};base64,{encoded_string.decode()});
#      }}    
#      </style>
#      """,
#      unsafe_allow_html=True
#    )
    

def show_login_logo():
    st.image("img/login-usuario.gif", caption=None, width=50, use_column_width=None, clamp=False, channels="RGB", output_format="auto", use_container_width=False)

def show_logo_red_neuronal():
    st.image("img/inteligencia-artificial.gif", caption=None, width=50, use_column_width=None, clamp=False, channels="RGB", output_format="auto", use_container_width=False)
        
def show_logo_arbol_decision():
    st.image("img/arbol-decision.gif", caption=None, width=50, use_column_width=None, clamp=False, channels="RGB", output_format="auto", use_container_width=False)

def show_logo_gaussiana():
    st.image("img/histograma.gif", caption=None, width=50, use_column_width=None, clamp=False, channels="RGB", output_format="auto", use_container_width=False)
                
def show_logo_calibracion():
    st.image("img/neuronal_1.gif", caption=None, width=50, use_column_width=None, clamp=False, channels="RGB", output_format="auto", use_container_width=False)
                
                                