import streamlit as st
import os
import sys

# Adicionar o diretório pai ao path para importar os módulos corretamente
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils.helpers import get_data, apply_custom_css
from utils.sidebar import show_sidebar  # Importe a função da sidebar

# Verifique se o estado da sessão existe
if "user_id" not in st.session_state:
    st.session_state.user_id = None
    st.session_state.user_name = None

# Guardar nome da página atual (opcional para keys únicas)
st.session_state["_current_page"] = "adicionar_dados"

# Adicionar CSS para controlar a ordem da sidebar - DEVE ser o primeiro código
st.markdown("""
<style>
/* Forçar ordem da sidebar */
section[data-testid="stSidebar"] > div:first-child {
    display: flex !important;
    flex-direction: column !important;
}

section[data-testid="stSidebar"] > div:first-child > div:first-child {
    order: -1 !important;
}
</style>
""", unsafe_allow_html=True)

# Configuração da página
st.set_page_config(page_title="Adicionar Dados - Fake Delivery", page_icon="➕", layout="wide")
apply_custom_css()

# Mostrar a sidebar compartilhada
with st.sidebar:
    show_sidebar()

# Título da página
st.markdown('<p class="main-header">🍕 Fake Delivery Dashboard</p>', unsafe_allow_html=True)
st.markdown('<p class="subheader">➕ Adicionar Novos Dados</p>', unsafe_allow_html=True)

add_option = st.selectbox("O que você deseja adicionar?", ["Usuário", "Restaurante", "Comida"])

if add_option == "Usuário":
    with st.form("add_user_form"):
        st.subheader("Adicionar Novo Usuário")
        name = st.text_input("Nome")
        email = st.text_input("Email")
        address = st.text_input("Endereço (opcional)")
        
        submitted = st.form_submit_button("Adicionar Usuário")
        if submitted:
            # Aqui você faria um POST request para a API
            # Como é uma API fake, vamos apenas simular o sucesso
            st.success(f"Usuário {name} adicionado com sucesso!")
            st.info("Nota: Esta é uma API somente leitura, então o usuário não foi realmente adicionado.")

elif add_option == "Restaurante":
    with st.form("add_restaurant_form"):
        st.subheader("Adicionar Novo Restaurante")
        name = st.text_input("Nome")
        location = st.text_input("Localização")
        rating = st.slider("Avaliação", 1.0, 5.0, 4.0, 0.5)
        
        submitted = st.form_submit_button("Adicionar Restaurante")
        if submitted:
            st.success(f"Restaurante {name} adicionado com sucesso!")
            st.info("Nota: Esta é uma API somente leitura, então o restaurante não foi realmente adicionado.")

elif add_option == "Comida":
    with st.form("add_food_form"):
        st.subheader("Adicionar Nova Comida")
        name = st.text_input("Nome")
        price = st.number_input("Preço (R$)", min_value=0.0, value=10.0, step=0.5)
        description = st.text_area("Descrição")
        
        submitted = st.form_submit_button("Adicionar Comida")
        if submitted:
            st.success(f"Comida {name} adicionada com sucesso!")
            st.info("Nota: Esta é uma API somente leitura, então a comida não foi realmente adicionada.")