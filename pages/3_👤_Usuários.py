import streamlit as st
from utils.helpers import get_data, apply_custom_css
from utils.sidebar import show_sidebar  # Importe a função da sidebar

# Verifique se o estado da sessão existe
if "user_id" not in st.session_state:
    st.session_state.user_id = None
    st.session_state.user_name = None

# Guardar nome da página atual (opcional para keys únicas)
st.session_state["_current_page"] = "usuarios"

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
st.set_page_config(page_title="Usuários - Fake Delivery", page_icon="👤", layout="wide")
apply_custom_css()

# Mostrar a sidebar compartilhada
with st.sidebar:
    show_sidebar()

# Título da página
st.markdown('<p class="main-header">🍕 Fake Delivery</p>', unsafe_allow_html=True)
st.markdown('<p class="subheader">👤 Lista de Usuários</p>', unsafe_allow_html=True)

# Adicionar busca
search_user = st.text_input("🔍 Buscar usuário pelo nome")

users = get_data("/users")

# Filtrar usuários pela busca
if search_user:
    users = [user for user in users if search_user.lower() in user['name'].lower()]

# Exibir usuários em cards
for user in users:
    with st.container():
        st.markdown(f"""
        <div class="card">
            <h3>{user['name']}</h3>
            <p>📧 Email: {user['email']}</p>
            <p>📍 Endereço: {user.get('address', 'Não informado')}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Botão para ver detalhes
        if st.button(f"Ver detalhes de {user['name']}", key=f"user_{user['id']}"):
            user_details = get_data(f"/users/{user['id']}")
            st.json(user_details)