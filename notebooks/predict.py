import sys
import joblib

def prever_preco_imovel(area_util, bairro_encoded, modelo_escolhido='knn'):
    """
    Carrega o cérebro da IA persistido em disco e realiza a predição
    de preço para um novo imóvel em São Paulo.
    """
    # 1. Definir qual arquivo carregar com base na escolha do usuário
    if modelo_escolhido.lower() == 'rf':
        arquivo_modelo = 'notebooks/rf_model_vendas_sp.joblib'
        nome_modelo = "Random Forest (Campeão Estatístico)"
    else:
        arquivo_modelo = 'notebooks/knn_model_vendas_sp.joblib'
        nome_modelo = "KNN Regressor (Campeão de Negócio)"
    
    try:
        # 2. Carregar o modelo de forma ultra rápida usando joblib
        model = joblib.load(arquivo_modelo)
        
        # 3. O modelo espera receber uma lista de listas ou array 2D [[area, bairro]]
        dados_imovel = [[float(area_util), float(bairro_encoded)]]
        
        # 4. Realizar a predição
        preco_predito = model.predict(dados_imovel)[0]
        
        # 5. Exibir o resultado formatado como um relatório executivo
        print("\n" + "="*50)
        print("         SISTEMA DE PRECIFICAÇÃO IMOBILIÁRIA         ")
        print("="*50)
        print(f" -> Modelo Ativo: {nome_modelo}")
        print(f" -> Área Útil Informada: {area_util} m²")
        print(f" -> Código do Bairro: {bairro_encoded}")
        print("-" * 50)
        print(f"PREÇO ESTIMADO DE VENDA: R$ {preco_predito:,.2f}")
        print("="*50 + "\n")
        
    except FileNotFoundError:
        print(f"\n Erro: O arquivo '{arquivo_modelo}' não foi encontrado.")
        print("Certifique-se de que rodou o treino antes de executar este script.\n")

if __name__ == "__main__":
    # Exemplo de teste padrão se o script for executado direto
    # Imóvel fictício: 85m² em um bairro cujo encoding é 7200.50
    print("Executando simulação padrão com dados de teste...")
    prever_preco_imovel(area_util=85, bairro_encoded=7200.50, modelo_escolhido='knn')