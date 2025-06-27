# Crie este novo arquivo

import streamlit as st
from utils.helpers import get_data

def show_sidebar():
    """Função para exibir a sidebar consistente em todas as páginas"""
    
    # Título da seção de login com margin superior reduzida
    st.markdown('<h1 style="margin-top: 0px; padding-top: 0px;">Minha Conta</h1>', unsafe_allow_html=True)
    
    # Exibir formulário de login ou informações do usuário
    if st.session_state.user_id is None:
        with st.expander("🔐 Fazer Login", expanded=True):
            # Adicionando labels personalizados acima dos campos
            st.markdown('<p style="margin-bottom: 5px; color: #ddd;">Email:</p>', unsafe_allow_html=True)
            email_login = st.text_input("", key=f"email_input_{st.session_state.get('_current_page', 'default')}", label_visibility="collapsed")
            
            # Ajuste o campo de senha para garantir que apareça
            st.markdown('<p style="margin-bottom: 5px; margin-top: 10px; color: #ddd;">Senha:</p>', unsafe_allow_html=True)
            password = st.text_input("", type="password", key=f"password_input_{st.session_state.get('_current_page', 'default')}", label_visibility="collapsed")
            
            # Espaço adicional para separar do botão
            st.markdown('<div style="margin-top: 15px;"></div>', unsafe_allow_html=True)
            
            if st.button("Entrar", key=f"login_button_{st.session_state.get('_current_page', 'default')}"):
                # Simular login - normalmente verificaria no backend
                users = get_data("/users")
                for user in users:
                    if user.get('email', '').lower() == email_login.lower():
                        # Buscar detalhes específicos do usuário
                        user_detail = get_data(f"/users/{user['id']}")
                        
                        st.session_state.user_id = user['id']
                        st.session_state.user_name = user['name']
                        st.session_state.user_email = user['email']
                        st.session_state.user_info = user_detail
                        
                        st.success(f"Bem-vindo(a), {user['name']}!")
                        st.rerun()
                        break
                else:
                    st.error("Email ou senha incorretos.")
    else:
        # Exibir informações do usuário logado
        st.markdown(f"### 👤 Olá, {st.session_state.user_name}!")
        st.markdown(f"📧 {st.session_state.user_email}")
        
        # Exibir endereço de entrega se disponível
        if 'user_info' in st.session_state and 'address' in st.session_state.user_info:
            st.write(f"🏠 Endereço: {st.session_state.user_info['address']}")
        
        # Botões específicos para usuário logado - AÇÕES DE CONTA
        if st.button("📋 Meus Pedidos", use_container_width=True, key="sidebar_pedidos"):
            st.switch_page("pages/pedidos.py")
            
        if st.button("✏️ Editar Perfil", use_container_width=True, key="sidebar_perfil"):
            st.switch_page("pages/perfil.py")
            
        if st.button("🛒 Carrinho", use_container_width=True, key="sidebar_carrinho"):
            st.switch_page("pages/carrinho.py")
        
        if st.button("🚪 Sair", use_container_width=True, key="sidebar_logout"):
            st.session_state.user_id = None
            st.session_state.user_name = None
            st.session_state.user_email = None
            st.session_state.user_info = None
            st.rerun()
    
    # Separador entre "Minha Conta" e navegação
    st.markdown("<hr style='margin: 20px 0;'>", unsafe_allow_html=True)
    
    # Navegação principal abaixo
    st.markdown("### 📱 Navegação")
    
    # Botão para a página inicial
    if st.button("🍕 Bem-Vindo!", use_container_width=True, key="sidebar_home"):
        st.switch_page("🍕Bem-Vindo!🍕.py")
        
    # Botões para navegação principal
    if st.button("🍽️ Restaurantes", use_container_width=True, key="sidebar_restaurantes"):
        st.switch_page("pages/1_🍽️_Restaurantes.py")
        
    if st.button("🍔 Comidas", use_container_width=True, key="sidebar_comidas"):
        st.switch_page("pages/2_🍔_Comidas.py")
        
    if st.button("👤 Usuários", use_container_width=True, key="sidebar_usuarios"):
        st.switch_page("pages/3_👤_Usuários.py")
        
    if st.button("➕ Adicionar Dados", use_container_width=True, key="sidebar_add_dados"):
        st.switch_page("pages/4_➕_Adicionar_Dados.py")