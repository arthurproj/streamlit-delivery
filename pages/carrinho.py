import streamlit as st
from utils.helpers import get_data, apply_custom_css
from utils.sidebar import show_sidebar  # Importe a função da sidebar

# Verifique se o estado da sessão existe
if "user_id" not in st.session_state:
    st.session_state.user_id = None
    st.session_state.user_name = None

# Guarde o nome da página atual para uso em keys únicas
st.session_state["_current_page"] = "carrinho"

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
st.set_page_config(page_title="Meu Carrinho - Fake Delivery", page_icon="🛒", layout="wide")
apply_custom_css()

# Mostrar a sidebar compartilhada
with st.sidebar:
    show_sidebar()

# Título da página
st.markdown('<p class="main-header">🍕 Fake Delivery</p>', unsafe_allow_html=True)
st.markdown('<p class="subheader">🛒 Meu Carrinho</p>', unsafe_allow_html=True)

# Inicializa o carrinho se não existir
if 'cart' not in st.session_state:
    st.session_state.cart = []

if not st.session_state.cart:
    st.info("Seu carrinho está vazio!")
    if st.button("Continuar Comprando"):
        st.switch_page("🍕Fake-Delivery.py")
else:
    # Exibir itens do carrinho
    total = 0
    
    for i, item in enumerate(st.session_state.cart):
        col1, col2, col3 = st.columns([3, 1, 1])
        
        with col1:
            st.markdown(f"### {item['name']}")
            st.write(f"R$ {item.get('price', 0):.2f} x {item.get('quantity', 1)}")
            
        with col2:
            # Botões para ajustar quantidade
            col_minus, col_qty, col_plus = st.columns([1, 1, 1])
            
            with col_minus:
                if st.button("-", key=f"minus_{i}"):
                    if item['quantity'] > 1:
                        item['quantity'] -= 1
                    else:
                        st.session_state.cart.remove(item)
                    st.rerun()
                    
            with col_qty:
                st.write(f"{item.get('quantity', 1)}")
                
            with col_plus:
                if st.button("+", key=f"plus_{i}"):
                    item['quantity'] += 1
                    st.rerun()
        
        with col3:
            # Remover item
            if st.button("🗑️", key=f"remove_{i}"):
                st.session_state.cart.remove(item)
                st.rerun()
        
        # Calcular subtotal
        subtotal = item.get('price', 0) * item.get('quantity', 1)
        total += subtotal
        
        st.write(f"Subtotal: R$ {subtotal:.2f}")
        st.markdown("---")
    
    # Total e finalização
    st.subheader(f"Total: R$ {total:.2f}")
    
    # Entrega
    st.write("Endereço de Entrega:")
    if "user_info" in st.session_state and st.session_state.user_info and "address" in st.session_state.user_info:
        endereco = st.text_area("Endereço", value=st.session_state.user_info["address"])
    else:
        endereco = st.text_area("Endereço")
    
    # Método de pagamento
    metodo = st.selectbox("Forma de Pagamento", ["Cartão de Crédito", "Pix", "Dinheiro"])
    
    # Finalizar pedido
    if st.button("Finalizar Pedido", use_container_width=True):
        st.balloons()
        st.success("Pedido realizado com sucesso! Em breve sua comida chegará no endereço informado.")
        # Normalmente aqui você enviaria os dados do pedido para a API
        # Limpar o carrinho
        st.session_state.cart = []