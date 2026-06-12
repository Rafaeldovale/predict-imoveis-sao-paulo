import joblib
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel


# 1. Inicializa o aplicativo FastApi
app = FastAPI(
    title = "API de Precificação Imobiliária - SP",
    description = "Interface de alta performance para previsão de preços de Vendas e Locação",
    version = "1.0.0"
)

# 2. Carrega os modelos de IA e ferramentas salvos em disco
try:
    modelo_locacao = joblib.load("models/random_forest_locacao.pkl")
    scaler_locacao = joblib.load("models/scaler_locacao.pkl")
    print("Sucesso: Modulos e Scalers carregados com sucesso!")
except Exception as e:
    print(f'Erro ao carregar os modelos: {e}')

# 3. Definição do Contrato de Entrada de dados para Locação
class DadosLocacao(BaseModel):
    area: float
    quartos: int
    banheiros: int
    vagas: int
    bairro_encoded: float

# 4. Rota Raiz 
@app.get("/")
def read_root():
    return {
        "status" : "Online",
        "mensagem" : "Api de Precificação de Imóveis de SP operando com sucesso!",
        "desenvolvedor" : "Rafael Bezerra do Vale"
    }

# 5. Rota de Previsão de Preço de Locação (Módulo de Produção)
@app.post("/predict/locacao", summary="Prever preço de aluguel residencial")
def predict_locacao(dados: DadosLocacao):
    
    # A) Prepara a matriz com as APENAS 2 colunas que o seu treino utilizou
    # A ordem precisa ser exatamente a mesma do notebook (provavelmente area primeiro, depois bairro)
    input_dados = np.array([dados.area, dados.bairro_encoded]).reshape(1, -1)
    
    # B) Escala os dados (já que o scaler também espera essas mesmas 2 colunas)
    input_escalado = scaler_locacao.transform(input_dados)
    
    # C) Realiza a previsão com o modelo Random Forest Campeão (que espera 2 colunas)
    previsao_bruta = modelo_locacao.predict(input_escalado)
    preco_estimado = float(previsao_bruta[0])
    
    # D) Retorna a resposta final em JSON
    return {
        "status": "Sucesso",
        "preco_previso_raw": preco_estimado,
        "preco_previso_formatado": f"R$ {preco_estimado:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    }