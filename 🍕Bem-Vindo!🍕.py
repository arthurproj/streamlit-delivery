import streamlit as st
import pandas as pd
import requests
from utils.helpers import get_data, apply_custom_css


# Adicionar CSS para controlar a ordem da sidebar - DEVE ser o primeiro código executado
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
st.set_page_config(page_title="Fake Delivery", page_icon="🍔", layout="wide")
apply_custom_css()

# Verificar se já tem usuário logado
if "user_id" not in st.session_state:
    st.session_state.user_id = None
    st.session_state.user_name = None

# Coloque isto ANTES de qualquer outro código de UI
# Mover Minha Conta para cima da sidebar
with st.sidebar:
    # Título da seção de login com margin superior reduzida
    st.markdown('<h1 style="margin-top: 0px; padding-top: 0px;">Minha Conta</h1>', unsafe_allow_html=True)
    
    # Exibir formulário de login ou informações do usuário
    if st.session_state.user_id is None:
        with st.expander("🔐 Fazer Login", expanded=True):
            # Adicionando labels personalizados acima dos campos
            st.markdown('<p style="margin-bottom: 5px; color: #ddd;">Email:</p>', unsafe_allow_html=True)
            email_login = st.text_input("", key="email_input", label_visibility="collapsed")
            
            # Ajuste o campo de senha para garantir que apareça
            st.markdown('<p style="margin-bottom: 5px; margin-top: 10px; color: #ddd;">Senha:</p>', unsafe_allow_html=True)
            password = st.text_input("", type="password", key="password_input", label_visibility="collapsed")
            
            # Espaço adicional para separar do botão
            st.markdown('<div style="margin-top: 15px;"></div>', unsafe_allow_html=True)
            
            if st.button("Entrar"):
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
        if st.button("📋 Meus Pedidos", use_container_width=True):
            st.switch_page("pages/pedidos.py")
            
        if st.button("✏️ Editar Perfil", use_container_width=True):
            st.switch_page("pages/perfil.py")
            
        if st.button("🛒 Carrinho", use_container_width=True):
            st.switch_page("pages/carrinho.py")
        
        if st.button("🚪 Sair", use_container_width=True):
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
    if st.button("🍕 Bem-Vindo!", use_container_width=True):
        st.switch_page("🍕Bem-Vindo!🍕.py")
        
    # Botões para navegação principal
    if st.button("🍽️ Restaurantes", use_container_width=True):
        st.switch_page("pages/1_🍽️_Restaurantes.py")
        
    if st.button("🍔 Comidas", use_container_width=True):
        st.switch_page("pages/2_🍔_Comidas.py")
        
    if st.button("👤 Usuários", use_container_width=True):
        st.switch_page("pages/3_👤_Usuários.py")
        
    if st.button("➕ Adicionar Dados", use_container_width=True):
        st.switch_page("pages/4_➕_Adicionar_Dados.py")

# Banner promocional
st.markdown("""
<div class="promo-banner">
    <h2 style="color: white; margin: 0; font-size: 2rem;">🔥 SUPER PROMOÇÃO! 🔥</h2>
    <p style="color: white; margin: 10px 0; font-size: 1.2rem;">Peça qualquer pizza grande e ganhe uma coca-cola 2L! Válido para hoje.</p>
    <p style="color: white; font-size: 0.9rem;">*Consulte regras da promoção</p>
</div>
""", unsafe_allow_html=True)

# Separador no sidebar
# st.sidebar.markdown("---")  # Esta linha foi removida conforme instruções

# Categorias de comida
st.subheader("Categorias")
cat_cols = st.columns(5)

categorias = [
    {"nome": "Pizzas", "emoji": "🍕", "img": "https://images.unsplash.com/photo-1513104890138-7c749659a591"},
    {"nome": "Hambúrgueres", "emoji": "🍔", "img": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd"},
    {"nome": "Sushi", "emoji": "🍣", "img": "https://images.unsplash.com/photo-1579871494447-9811cf80d66c"},
    {"nome": "Bebidas", "emoji": "🥤", "img": "https://images.unsplash.com/photo-1551024709-8f23befc6f87"},
    {"nome": "Sobremesas", "emoji": "🍰", "img": "https://images.unsplash.com/photo-1551024506-0bccd828d307"},
]

for i, cat in enumerate(categorias):
    with cat_cols[i]:
        st.markdown(f"""
        <div class="category-box">
            <h1 style="font-size: 2rem; margin: 0;">{cat['emoji']}</h1>
            <h4>{cat['nome']}</h4>
        </div>
        """, unsafe_allow_html=True)
        
        # Quando clicar no botão, armazena a categoria e navega para a página de comidas
        if st.button(f"Ver mais", key=f"cat_{i}"):
            # Armazenar a categoria selecionada no estado da sessão
            st.session_state.categoria_selecionada = cat['nome']
            # Navegar para a página de comidas
            st.switch_page("pages/2_🍔_Comidas.py")

# Restaurantes em destaque
st.subheader("Restaurantes em Destaque")
restaurants = get_data("/restaurants")

# Filtrar apenas restaurantes com rating alto (simulado)
featured_restaurants = []
for r in restaurants:
    try:
        if float(r.get('rating', 0)) >= 4.5:
            featured_restaurants.append(r)
    except:
        pass

# Limitar a 3 restaurantes
featured_restaurants = featured_restaurants[:3]

# Se não tiver suficientes, adiciona restaurantes fictícios
while len(featured_restaurants) < 3:
    featured_restaurants.append({
        "id": len(featured_restaurants) + 100,
        "name": f"Restaurante Premium {len(featured_restaurants) + 1}",
        "rating": "5.0",
        "location": "Próximo a você"
    })

featured_cols = st.columns(3)

# Caminhos para as imagens locais - substitua pelos nomes reais das suas imagens
image_paths = [
    "images/xisvini.png",  # Substitua pelo nome real do seu arquivo
    "images/salpimenta.png",  # Substitua pelo nome real do seu arquivo
    "images/outback.png"   # Substitua pelo nome real do seu arquivo
]

for i, restaurant in enumerate(featured_restaurants):
    with featured_cols[i]:
        try:
            # Tenta carregar a imagem local
            st.image(image_paths[i], use_container_width=True)
        except:
            # Se falhar, usa uma imagem de backup da internet
            backup_images = [
                "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4",
                "https://images.unsplash.com/photo-1555396273-367ea4eb4db5",
                "https://images.unsplash.com/photo-1514933651103-005eec06c04b"
            ]
            st.image(backup_images[i % len(backup_images)], use_container_width=True)
            
        st.markdown(f"""
        <div class="card restaurant-card">  <!-- Adicionado a classe restaurant-card -->
            <h3>{restaurant['name']}</h3>
            <p>⭐ {restaurant.get('rating', '5.0')}</p>
            <p>📍 {restaurant.get('location', 'Próximo a você')}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Quando clicar no botão "Pedir agora", navega para a página de restaurantes
        if st.button(f"Pedir agora", key=f"rest_{i}"):
            # Armazenar o restaurante selecionado no estado da sessão (opcional)
            st.session_state.restaurante_selecionado = restaurant['name']
            # Navegar para a página de restaurantes
            st.switch_page("pages/1_🍽️_Restaurantes.py")

# Pratos populares
st.subheader("Pratos Populares")
foods = get_data("/foods")

# Simulação de preços e descrições se estiverem faltando
for food in foods:
    if 'price' not in food:
        food['price'] = 29.90
    if 'description' not in food:
        food['description'] = "Delicioso prato preparado com ingredientes selecionados."

# Limitar a 6 pratos
foods = foods[:6]

# Dividir em 2 linhas de 3
food_rows = [st.columns(3) for _ in range(2)]
for i, food in enumerate(foods):
    row = i // 3
    col = i % 3
    with food_rows[row][col]:
        st.markdown(f"""
        <div class="card">
            <h3>{food['name']}</h3>
            <p>💰 R$ {food['price']:.2f}</p>
            <p>📝 {food['description']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([1, 1])
        with col1:
            # Botão para adicionar ao carrinho
            st.button("Adicionar ao carrinho", key=f"food_{i}")
        
        with col2:
            # Novo botão para ver detalhes específicos do item
            if st.button("Ver detalhes", key=f"details_{i}"):
                # Usar a rota específica para obter detalhes do item
                food_details = get_data(f"/foods/{food['id']}")
                
                # Criar um modal com detalhes adicionais
                st.subheader(f"Detalhes do {food['name']}")
                
                # Exibir informações adicionais que podem vir no endpoint específico
                st.write(f"⭐ Avaliações: {food_details.get('rating', '4.7')}/5.0")
                st.write(f"⏱️ Tempo de preparo: {food_details.get('prep_time', '25-30')} minutos")
                st.write(f"🔥 Calorias: {food_details.get('calories', '450-600')} kcal")
                
                # Ingredientes (se disponíveis)
                ingredientes = food_details.get('ingredients', ['Não especificado'])
                if isinstance(ingredientes, list) and len(ingredientes) > 0:
                    st.write("🥗 Ingredientes:")
                    for ing in ingredientes:
                        st.write(f"  • {ing}")

# Call-to-action final
st.markdown("""
<div style="text-align: center; margin: 50px 0;">
    <h2 style="color: #FF8C00;">Está com fome?</h2>
    <p style="color: #ddd; margin-bottom: 20px;">Milhares de opções deliciosas a um clique de distância!</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,2,1])
with col2:
    # Quando clicar no botão PEDIR AGORA!, navega para a página de restaurantes
    if st.button("PEDIR AGORA!", key="cta_final", use_container_width=True):
        # Navegar para a página de restaurantes
        st.switch_page("pages/1_🍽️_Restaurantes.py")

# Rodapé
st.markdown("---")
st.markdown("© 2025 Fake Delivery | Termos de Uso | Política de Privacidade")
