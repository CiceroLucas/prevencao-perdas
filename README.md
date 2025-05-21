# 🛒 Sistema de Previsão de Perdas em Supermercados com IA e FastAPI

Este projeto utiliza **Machine Learning com FastAPI** para prever o risco de perdas em produtos de supermercado e recomendar ações para evitá-las.

---

## 📌 Objetivo

Automatizar a **prevenção de perdas** em supermercados com base em dados como estoque, vendas e validade dos produtos. O sistema prevê o risco de perda e sugere ações para minimizar prejuízos, como promoções ou ajustes de compra.

---

## ⚙️ Tecnologias Utilizadas

- **FastAPI**: Backend e API
- **Scikit-learn**: Treinamento do modelo de IA (Random Forest)
- **Pandas / NumPy**: Manipulação de dados
- **Python 3.10+**

---

# 🚀 Como Rodar o Projeto

1. Clone o repositório
```
git clone https://github.com/CiceroLucas/prevencao-perdas
cd prevencao-perdas
```

2. Crie o ambiente e instale as dependências
```
python -m venv venv
source venv/bin/activate  # no Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Inicie o servidor
```
uvicorn main:app --reload
```

4. Acesse a documentação interativa
```
http://localhost:8000/docs
```
---
# Como a Previsão Funciona

1. O sistema recebe um arquivo .csv com dados dos produtos.

2. Um modelo de Machine Learning (RandomForestClassifier) analisa as variáveis:

    * Produto
  
    * Estoque
  
    * Vendas
  
    * Dias de validade

3. O modelo retorna uma previsão:

    * 0: Baixo risco de perda
  
    * 1: Alto risco de perda

4. A previsão é classificada como:

    * Baixo → Nenhuma ação
    
    * Médio → Reduzir compras
    
    * Alto → Colocar em promoção

---

# Exemplo de Saída da API
```
[
  {
    "produto": "Banana",
    "estoque": 50,
    "vendas": 10,
    "dias_validade": 2,
    "risco_classificado": "Alto",
    "recomendacao": "Colocar em promoção"
  },
  {
    "produto": "Arroz",
    "estoque": 200,
    "vendas": 180,
    "dias_validade": 120,
    "risco_classificado": "Baixo",
    "recomendacao": "Nenhuma ação necessária"
  }
]

```
---

# 🛠 Funcionalidades Futuras
 - Armazenamento em banco de dados (SQLite/PostgreSQL)

 - Dashboard com Streamlit ou React

 - Retraining do modelo com dados novos

 - Gestão de promoções automatizadas
