import streamlit as st
from utils.helpers import get_data, apply_custom_css
from utils.sidebar import show_sidebar  # Importe a função da sidebar

# Verifique se o estado da sessão existe
if "user_id" not in st.session_state:
    st.session_state.user_id = None
    st.session_state.user_name = None

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
st.set_page_config(page_title="Restaurantes - Fake Delivery", page_icon="🍔", layout="wide")
apply_custom_css()

# Mostrar a sidebar compartilhada
with st.sidebar:
    show_sidebar()

st.markdown('<p class="main-header">🍕 Fake Delivery</p>', unsafe_allow_html=True)
st.markdown('<p class="subheader">🍽️ Restaurantes</p>', unsafe_allow_html=True)

# Seção de Restaurantes em Destaque
st.subheader("⭐ Restaurantes em Destaque")

# Imagens personalizadas para restaurantes em destaque
restaurant_images = {
    # Imagens de restaurantes - você pode personalizar estas URLs
    "pizza": "https://images.unsplash.com/photo-1513104890138-7c749659a591?auto=format&fit=crop&w=600&q=80",
    "burger": "https://images.unsplash.com/photo-1498837167922-ddd27525d352?auto=format&fit=crop&w=600&q=80",
    "sushi": "https://images.unsplash.com/photo-1579871494447-9811cf80d66c?auto=format&fit=crop&w=600&q=80",
    "italian": "https://images.unsplash.com/photo-1498579687545-d5a4fffb0a9e?auto=format&fit=crop&w=600&q=80",
    "mexican": "https://images.unsplash.com/photo-1551504734-5ee1c4a1479b?auto=format&fit=crop&w=600&q=80",
    "default": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?auto=format&fit=crop&w=600&q=80"
}

# Obter dados dos restaurantes
all_restaurants = get_data("/restaurants")

# Selecionar apenas 3 restaurantes para destaque (com as melhores avaliações)
featured_restaurants = []
for r in all_restaurants:
    try:
        r['rating'] = float(r.get('rating', 0))
        featured_restaurants.append(r)
    except (ValueError, TypeError):
        pass

# Ordenar por avaliação (do maior para o menor)
featured_restaurants = sorted(featured_restaurants, key=lambda x: x.get('rating', 0), reverse=True)[:3]

# Exibir restaurantes em destaque
featured_cols = st.columns(3)

for i, restaurant in enumerate(featured_restaurants):
    with featured_cols[i]:
        # Escolher uma imagem com base no nome do restaurante
        restaurant_name = restaurant['name'].lower()
        image_key = "default"
        
        # Tentar encontrar uma palavra-chave no nome do restaurante
        for key in restaurant_images.keys():
            if key in restaurant_name:
                image_key = key
                break
                
        # Exibir a imagem
        st.image(restaurant_images[image_key], use_container_width=True)
        
        # Exibir informações do restaurante
        st.markdown(f"""
        <div class="card">
            <h3>{restaurant['name']}</h3>
            <p>⭐ {restaurant.get('rating', 'N/A')}</p>
            <p>📍 {restaurant.get('location', 'Localização não informada')}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Botão de ação
        st.button(f"Ver cardápio", key=f"featured_{restaurant['id']}")

# Separador
st.markdown("---")

# Filtro por avaliação
st.subheader("Todos os Restaurantes")
min_rating = st.slider("Filtrar por avaliação mínima", 1.0, 5.0, 1.0, 0.5)

# Filtrar restaurantes pela avaliação
filtered_restaurants = []
for r in all_restaurants:
    try:
        rating = float(r.get('rating', 0))
        if rating >= min_rating:
            filtered_restaurants.append(r)
    except (ValueError, TypeError):
        # Ignora restaurantes com ratings que não podem ser convertidos para float
        pass
restaurants = filtered_restaurants

# Exibir em grid
cols = st.columns(2)
for i, restaurant in enumerate(restaurants):
    with cols[i % 2]:
        with st.container():
            rating = restaurant.get('rating', 'N/A')
            st.markdown(f"""
            <div class="card">
                <h3>{restaurant['name']} ⭐ {rating}</h3>
                <p>📍 Localização: {restaurant.get('location', 'Não informado')}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Botão para ver cardápio
            if st.button(f"Ver cardápio de {restaurant['name']}", key=f"rest_{restaurant['id']}"):
                # Buscar detalhes específicos do restaurante
                restaurant_detail = get_data(f"/restaurants/{restaurant['id']}")
                
                st.subheader(f"Cardápio de {restaurant['name']}")
                
                # Exibir detalhes adicionais do restaurante
                if restaurant_detail:
                    # Pode haver informações adicionais no endpoint específico
                    st.write(f"📞 Telefone: {restaurant_detail.get('phone', 'Não disponível')}")
                    st.write(f"🕒 Horário: {restaurant_detail.get('hours', 'Aberto todos os dias')}")
                    st.write(f"💳 Pagamento: {restaurant_detail.get('payment_methods', 'Aceita todos os cartões')}")
                
                foods = get_data("/foods")
                
                # Versão corrigida - evita problemas com tipos diferentes
                try:
                    # Tenta uma abordagem que não depende de conversões de tipos
                    restaurant_id = int(str(restaurant['id']).strip())
                    # Seleciona alimentos de forma mais segura
                    restaurant_foods = []
                    for food in foods:
                        try:
                            food_id = int(str(food['id']).strip())
                            if food_id % 3 == restaurant_id % 3:  # Associação simples baseada em módulo 3
                                restaurant_foods.append(food)
                        except (ValueError, TypeError):
                            continue
                except (ValueError, TypeError):
                    # Caso ainda haja erro, seleciona alguns alimentos aleatoriamente
                    restaurant_foods = foods[:5]  # Pega os primeiros 5 alimentos
                
                # Exibe os alimentos do restaurante
                if restaurant_foods:
                    for food in restaurant_foods:
                        price = food.get('price', 0)
                        if not isinstance(price, (int, float)):
                            try:
                                price = float(price)
                            except (ValueError, TypeError):
                                price = 29.90
                                
                        st.write(f"• {food['name']} - R$ {price:.2f}")
                else:
                    st.info("Nenhum item disponível no cardápio deste restaurante.")