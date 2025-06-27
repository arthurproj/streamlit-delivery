import streamlit as st
from utils.helpers import get_data, apply_custom_css
from utils.sidebar import show_sidebar  # Importe a função da sidebar

# Verifique se o estado da sessão existe
if "user_id" not in st.session_state:
    st.session_state.user_id = None
    st.session_state.user_name = None

# Guarde o nome da página atual para uso em keys únicas
st.session_state["_current_page"] = "perfil"

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

# Configuração da página - APENAS UMA VEZ
st.set_page_config(page_title="Meu Perfil - Fake Delivery", page_icon="👤", layout="wide")
apply_custom_css()

# Mostrar a sidebar compartilhada
with st.sidebar:
    show_sidebar()

# Título da página
st.markdown('<p class="main-header">🍕 Fake Delivery</p>', unsafe_allow_html=True)
st.markdown('<p class="subheader">👤 Meu Perfil</p>', unsafe_allow_html=True)

# Verificar se o usuário está logado
if "user_id" not in st.session_state or st.session_state.user_id is None:
    st.warning("Você precisa fazer login para acessar esta página.")
    if st.button("Ir para o Login"):
        st.switch_page("🍕Fake-Delivery.py")
else:
    # Obter dados do usuário usando a rota específica
    user_id = st.session_state.user_id
    user_detail = get_data(f"/users/{user_id}")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # Avatar do usuário
        st.image("https://cdn-icons-png.flaticon.com/512/4333/4333609.png", width=200)
        st.button("Alterar foto")
    
    with col2:
        # Informações do perfil
        st.subheader("Informações Pessoais")
        
        with st.form("profile_form"):
            nome = st.text_input("Nome", value=user_detail.get('name', ''))
            email = st.text_input("Email", value=user_detail.get('email', ''))
            telefone = st.text_input("Telefone", value=user_detail.get('phone', ''))
            
            st.subheader("Endereço")
            endereco = st.text_input("Endereço completo", value=user_detail.get('address', ''))
            
            if st.form_submit_button("Salvar alterações"):
                st.success("Perfil atualizado com sucesso!")
                # Normalmente aqui você enviaria os dados para atualizar na API
                # Como esta API é de leitura apenas, apenas simulamos o sucesso