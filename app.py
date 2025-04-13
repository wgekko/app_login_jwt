# app.py
import streamlit as st
import time
from auth import authenticate
from utils import login_user, apply_custom_style, show_login_logo
import base64
import streamlit.components.v1 as components
import warnings
warnings.simplefilter("ignore", category=FutureWarning)
# Suprimir advertencias ValueWarning
warnings.simplefilter("ignore")

st.set_page_config(page_title="App-Login", page_icon="img/logo3.png", layout="centered", initial_sidebar_state="collapsed")


#add_local_sidebar_image("img/fondo.jpg")

apply_custom_style()
show_login_logo()

if "user" in st.session_state:
    with st.spinner("Redirigiendo..."):
        time.sleep(1)
        st.switch_page("pages/1_Redes Neuronales.py")



st.title("🔐 Inicio de Sesión")

username = st.text_input("Usuario")
password = st.text_input("Contraseña", type="password")

if st.button("Iniciar sesión"):
    role = authenticate(username, password)
    if role:
        login_user(username, role)
        st.success("Login exitoso", icon=":material/check:")
        with st.spinner("Redirigiendo..."):
            time.sleep(1)
            st.switch_page("pages/1_Redes Neuronales.py")
    else:
        st.error("Credenciales inválidas", icon=":material/close:")
