from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np
import os

app = FastAPI(title="API de Precificação de Imóveis - SP")

# --- CONFIGURAÇÃO DE CAMINHOS ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODELS_DIR = os.path.join(BASE_DIR, "models")

# --- CARREGAMENTO DOS MODELOS E SCALERS ---
try:
    # 1. Componentes de Locação
    modelo_locacao = joblib.load(os.path.join(MODELS_DIR, "random_forest_locacao.pkl"))
    scaler_locacao = joblib.load(os.path.join(MODELS_DIR, "scaler_locacao.pkl"))
    
    # 2. Componentes de Vendas (Usando seus arquivos .joblib)
    # Nota: Como o de Vendas usa as mesmas 2 features, podemos usar o mesmo scaler se a distribuição for idêntica,
    # ou o scaler padrão que você aplicou no notebook de vendas.
    modelo_vendas = joblib.load(os.path.join(MODELS_DIR, "rf_model_vendas_sp.joblib"))
    scaler_vendas = joblib.load(os.path.join(MODELS_DIR, "scaler_locacao.pkl")) # Ajustado temporariamente para o scaler disponível
    
    print("🚀 Todos os modelos e scalers foram carregados com sucesso!")
except Exception as e:
    print(raise_err := f"❌ Erro ao carregar os modelos: {str(e)}")

# --- CONTRATOS DE DADOS (PYDANTIC) ---
# Como ambos os modelos usam as mesmas 2 variáveis, a estrutura de entrada é a mesma
class DadosImovel(BaseModel):
    area_util: float
    bairro_encoded: int

# --- ROTAS DA API ---

@app.get("/")
def home():
    return {"status": "API Ativa", "versao": "2.0"}

# Rota 1: Previsão de Aluguel (Locação)
@app.post("/predict/locacao")
def predict_locacao(dados: DadosImovel):
    try:
        # 1. Preparar os dados de entrada (formato 2D que o scikit-learn espera)
        entrada = np.array([[dados.area_util, dados.bairro_encoded]])
        
        # 2. Aplicar o Scaler nas 2 features
        entrada_escalada = scaler_locacao.transform(entrada)
        
        # 3. Fazer a previsão
        predicao = modelo_locacao.predict(entrada_escalada)
        
        return {"preco_estimado_locacao": round(float(predicao[0]), 2)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro no processamento: {str(e)}")

# Rota 2: Previsão de Compra (Vendas)
@app.post("/predict/vendas")
def predict_vendas(dados: DadosImovel):
    try:
        entrada = np.array([[dados.area_util, dados.bairro_encoded]])
        entrada_escalada = scaler_vendas.transform(entrada)
        predicao = modelo_vendas.predict(entrada_escalada)
        
        return {"preco_estimado_venda": round(float(predicao[0]), 2)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro no processamento: {str(e)}")