streamlit-delivery
Projeto de consumo de API de delivery utilizando Python com Streamlit para frontend, proporcionando uma interface interativa e prática para visualização e manipulação dos dados da API.

#Descrição
Este projeto integra uma API de delivery já existente com uma interface frontend feita em Streamlit, permitindo a exibição dinâmica dos dados de pedidos, restaurantes e entregas. O objetivo é unir backend e frontend de forma simples e funcional para facilitar a experiência do usuário e demonstrar o consumo de APIs com Python.

#Funcionalidades
Consumo da API RESTful de delivery

Interface web interativa com Streamlit

Visualização de pedidos, status, restaurantes e entregadores

Interface simples para testes e demonstrações

#Tecnologias Utilizadas
Python 3.x

Streamlit

Requests (para consumir a API)

API RESTful de Delivery (externa)

Como rodar o projeto
Clone o repositório:

bash
Copiar
Editar
git clone https://github.com/arthurproj/streamlit-delivery.git
cd streamlit-delivery
Crie e ative um ambiente virtual (recomendado):

bash
Copiar
Editar
python -m venv venv
source venv/bin/activate     # Linux/Mac
venv\Scripts\activate        # Windows
Instale as dependências:

bash
Copiar
Editar
pip install -r requirements.txt
Execute a aplicação Streamlit:

bash
Copiar
Editar
streamlit run app.py
Acesse no navegador:

arduino
Copiar
Editar
http://localhost:8501
