import requests
import streamlit as st

BASE_URL = "https://apifakedelivery.vercel.app"

def get_data(endpoint):
    try:
        response = requests.get(f"{BASE_URL}{endpoint}")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        st.error(f"Erro ao buscar dados: {e}")
        return []

def apply_custom_css():
    st.markdown("""
    <style>
        /* Background escuro */
        .stApp {
            background-color: #121212;
            color: #f0f0f0;
        }
        
        /* Botões e interativos */
        div.stButton > button {
            background-color: #FF4B4B !important;
            color: white !important;
            border: none !important;
            border-radius: 30px !important;
            padding: 10px 24px !important;
            font-weight: bold !important;
            transition: all 0.3s ease !important;
        }
        
        div.stButton > button:hover {
            background-color: #ff6b6b !important;
            transform: translateY(-2px) !important;
            box-shadow: 0 4px 12px rgba(255, 75, 75, 0.3) !important;
        }
        
        /* Cartões de produtos */
        .card {
            padding: 20px;
            border-radius: 15px;
            margin-bottom: 30px;  /* Aumentei a margem inferior */
            background-color: #1e1e1e;
            color: #f0f0f0;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            border: 1px solid #333;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            height: 200px !important;  /* Altura fixa para todos os cards */
            width: 100% !important;    /* Largura completa */
            overflow: visible;         /* Conteúdo visível mesmo se ultrapassar */
            display: flex;
            flex-direction: column;
            position: relative;        /* Para posicionamento absoluto de botões */
        }
        
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
        }
        
        .card h3 {
            color: #FF8C00;
            margin-bottom: 12px;
            font-size: 1.5rem;
        }
        
        .card p {
            color: #ddd;
            margin: 8px 0;
        }
        
        /* Cabeçalhos */
        .main-header {
            font-size: 3rem;
            font-weight: bold;
            color: #FF4B4B;
            margin-bottom: 10px;
        }
        
        .subheader {
            font-size: 1.8rem;
            color: #FF8C00;
            margin-bottom: 30px;
        }
        
        /* Banner promocional */
        .promo-banner {
            background: linear-gradient(135deg, #FF416C, #FF4B2B);
            padding: 20px;
            border-radius: 15px;
            margin: 30px 0;
            text-align: center;
            box-shadow: 0 6px 12px rgba(255, 65, 108, 0.2);
        }
        
        /* Categorias */
        .category-box {
            background-color: #1e1e1e;
            padding: 15px;
            border-radius: 12px;
            text-align: center;
            border: 1px solid #333;
            transition: all 0.3s ease;
            height: 180px !important;  /* Altura fixa para todas as categorias */
            width: 100% !important;    /* Largura completa */
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;   /* Centraliza o conteúdo verticalmente */
        }
        
        .category-box:hover {
            background-color: #FF4B4B;
            transform: translateY(-5px);
        }
        
        .category-box h4 {
            color: #FF8C00;
            margin: 10px 0;
            font-size: 1.3rem;
        }
        
        .category-box:hover h4 {
            color: white;
        }
        
        /* Estilo para os ícones de categoria */
        .category-box h1 {
            font-size: 3.5rem !important;
            margin-bottom: 15px !important;
        }
        
        /* Input de busca */
        .stTextInput input {
            background-color: #2d2d2d !important;
            color: white !important;
            border: 1px solid #444 !important;
            border-radius: 0px !important;  /* Remove o border-radius deixando quadrado */
            padding: 10px 20px !important;
        }
        
        .stTextInput input:focus {
            border-color: #FF4B4B !important;
            box-shadow: 0 0 0 1px #FF4B4B !important;
            border-radius: 0px !important;
        }

        /* Cards de restaurantes */
        .restaurant-card {
            height: 200px !important;  /* Mesma altura que .card */
            overflow: visible !important;  /* Alterado para visible para não cortar o conteúdo */
            padding-bottom: 35px !important; /* Mais espaço na parte inferior */
            margin-bottom: 40px !important; /* Margem adicional abaixo do card */
        }

        /* Estilo para botões de ação do usuário */
        .stSidebar div[data-testid="stButton"] > button {
            margin-bottom: 10px !important;
            font-size: 16px !important;
        }

        /* Ajustes para cabeçalho do menu */
        .stSidebar .block-container {
            padding-top: 20px !important;
        }

        /* Melhoria na visualização do menu lateral */
        section[data-testid="stSidebar"] {
            background-color: #1a1a1a !important;
            border-right: 1px solid #333 !important;
        }

        /* Menu hambúrguer como checkbox */
        .stCheckbox [data-testid="stCheckbox"] {
            height: 40px !important;
            width: 40px !important;
            cursor: pointer !important;
        }

        /* Esconder o label do checkbox mas manter visível o ícone */
        .stCheckbox label p {
            font-size: 24px !important;
            color: #FF4B4B !important;
            margin: 0 !important;
            padding: 5px !important;
        }

        /* Esconder o verdadeiro checkbox */
        .stCheckbox [data-testid="stCheckbox"] > div > div > div:first-child {
            display: none !important;
        }

        /* Esconder a mensagem "Press Enter to apply" */
        .stTextInput .st-by {
            display: none !important;
        }

        /* Também tornar o input de senha quadrado */
        div[data-baseweb="input"] {
            border-radius: 0 !important;
        }

        div[data-baseweb="base-input"] {
            border-radius: 0 !important;
        }

        /* Esconder os hints e mensagens auxiliares */
        div[data-testid="stTextInput"] label {
            visibility: hidden !important;
            height: 0 !important;
            position: absolute !important;
        }

        div[data-testid="stTextInput"] p {
            visibility: hidden !important;
            height: 0 !important;
            position: absolute !important;
        }

        /* Remover o "olho" do campo de senha */
        div[data-baseweb="input"] > div > div:last-child {
            display: none !important;
        }

        /* Corrigir campo de senha */
        [data-testid="stTextInput"] input[type="password"] {
            opacity: 1 !important;
            min-height: 40px !important;
            background-color: #2d2d2d !important;
            color: white !important;
            border: 1px solid #444 !important;
            border-radius: 0px !important;
            padding: 10px 20px !important;
            display: block !important;
            visibility: visible !important;
            width: 100% !important;
        }

        /* Garantir visibilidade do placeholder */
        [data-testid="stTextInput"] input::placeholder {
            color: #888 !important;
            opacity: 0.7 !important;
        }

        /* Certificar que o container do campo é visível */
        div[data-baseweb="base-input"] {
            opacity: 1 !important;
            visibility: visible !important;
            min-height: 40px !important;
        }

        /* Remover ocultar qualquer elemento do campo de senha */
        [data-testid="stTextInput"] > div {
            visibility: visible !important;
            opacity: 1 !important;
        }

        /* Forçar exibição do campo de senha */
        [data-testid="stTextInput"] [data-baseweb="input"] {
            display: block !important;
            visibility: visible !important;
            opacity: 1 !important;
        }

        /* Forçar altura mínima e visibilidade para todos os inputs */
        div[data-baseweb="base-input"] {
            height: auto !important;
            min-height: 40px !important;
            opacity: 1 !important;
        }

        /* Remover componentes que possivelmente ocultam o campo */
        [data-testid="stTextInput"] div[aria-hidden="true"] {
            display: none !important;
        }

        /* Esconder a navegação automática da sidebar */
        section[data-testid="stSidebarNav"] {
            display: none !important;
        }

        div.css-1ope8sv.e1fqkh3o4 {
            display: none !important;
        }

        .css-wjbhl0.e1fqkh3o10, .css-hied5v.e1fqkh3o10 {
            display: none !important;
        }

        /* Esconder qualquer elemento que tenha navegação de páginas */
        [data-testid="stSidebarNav"] {
            display: none !important;
        }

        /* Ajustar posição da sidebar para começar mais acima */
        section[data-testid="stSidebar"] > div {
            padding-top: 0 !important;
        }

        section[data-testid="stSidebar"] .block-container {
            padding-top: 1rem !important;
            padding-bottom: 1rem !important;
        }

        /* Reduzir o espaço no topo do primeiro elemento da sidebar */
        section[data-testid="stSidebar"] div:first-child {
            margin-top: 0 !important;
        }

        /* Ajustar o título principal da sidebar */
        section[data-testid="stSidebar"] h1 {
            margin-top: 0 !important;
            padding-top: 0 !important;
        }
    </style>
    """, unsafe_allow_html=True)

def add_to_cart(food_id):
    # Inicializa o carrinho se não existir
    if 'cart' not in st.session_state:
        st.session_state.cart = []
    
    # Obter detalhes do alimento usando a rota específica
    food_detail = get_data(f"/foods/{food_id}")
    
    if food_detail:
        # Verificar se este item já está no carrinho
        for item in st.session_state.cart:
            if item['id'] == food_id:
                item['quantity'] += 1
                return True
        
        # Se não está no carrinho, adiciona com quantidade 1
        food_detail['quantity'] = 1
        st.session_state.cart.append(food_detail)
        return True
    
    return False