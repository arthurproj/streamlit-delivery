import streamlit as st
from utils.helpers import get_data, apply_custom_css
from utils.sidebar import show_sidebar  # Importe a função da sidebar

# Verifique se o estado da sessão existe
if "user_id" not in st.session_state:
    st.session_state.user_id = None
    st.session_state.user_name = None

# Guardar nome da página atual (opcional para keys únicas)
st.session_state["_current_page"] = "comidas"

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
st.set_page_config(page_title="Cardápio - Fake Delivery", page_icon="🍔", layout="wide")
apply_custom_css()

# Mostrar a sidebar compartilhada
with st.sidebar:
    show_sidebar()

# Título da página
st.markdown('<p class="main-header">🍕 Fake Delivery</p>', unsafe_allow_html=True)
st.markdown('<p class="subheader">🍔 Cardápio</p>', unsafe_allow_html=True)

# Adicionar filtros
col1, col2 = st.columns(2)
with col1:
    price_range = st.slider("Faixa de preço", 0.0, 100.0, (0.0, 100.0))
with col2:
    sort_option = st.selectbox("Ordenar por", ["Nome (A-Z)", "Nome (Z-A)", "Preço (menor-maior)", "Preço (maior-menor)"])

foods = get_data("/foods")

# Verificar se há uma categoria selecionada
categoria_selecionada = None
if 'categoria_selecionada' in st.session_state:
    categoria_selecionada = st.session_state.categoria_selecionada
    # Você pode mostrar isso em algum lugar
    st.write(f"Categoria selecionada: {categoria_selecionada}")

# E então filtrar os alimentos por categoria
if categoria_selecionada:
    # Filtrar os alimentos baseado na categoria
    foods = [food for food in foods if food.get('categoria', '').lower() == categoria_selecionada.lower()]
    # Se não encontrar nada, exibe todos
    if not foods:
        st.warning(f"Nenhum item encontrado na categoria {categoria_selecionada}.")
        foods = get_data("/foods")  # Carrega todos novamente

# Aplicar filtro de preço
foods = [food for food in foods if price_range[0] <= food['price'] <= price_range[1]]

# Aplicar ordenação
if sort_option == "Nome (A-Z)":
    foods = sorted(foods, key=lambda x: x['name'])
elif sort_option == "Nome (Z-A)":
    foods = sorted(foods, key=lambda x: x['name'], reverse=True)
elif sort_option == "Preço (menor-maior)":
    foods = sorted(foods, key=lambda x: x['price'])
elif sort_option == "Preço (maior-menor)":
    foods = sorted(foods, key=lambda x: x['price'], reverse=True)

# Exibir em grid
for food in foods:
    with st.container():
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"""
            <div class="card">
                <h3>{food['name']}</h3>
                <p>💰 Preço: R$ {food['price']}</p>
                <p>📄 Descrição: {food['description']}</p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.button("Adicionar ao Carrinho", key=f"add_{food['id']}")