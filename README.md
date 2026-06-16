# 🏢 Inteligência Artificial para Precificação Imobiliária em São Paulo

Este projeto desenvolve um pipeline completo de Ciência de Dados e Inteligência Artificial para prever com alta precisão os preços de venda de imóveis na cidade de São Paulo. Utilizando uma base de dados realista com mais de 90 mil registros, o projeto foca em resolver desafios complexos de negócios, como o saneamento de outliers extremos e o tratamento de alta cardinalidade categórica.

---

## 🚀 Arquitetura do Projeto e Progresso Atual


O projeto foi estruturado seguindo as melhores práticas de Engenharia de Software e Data Science de nível Sênior. 

### 📁 Estrutura de Pastas do Repositório:

├── data/
│   ├── raw/                  # Base de dados original (housing_sp_city.csv)
│   └── processed/            # Bases limpas pós-saneamento
│       ├── vendas_sp_limpo.csv
│       └── locacao_sp_limpo.csv
├── models/                   # Modelos preditivos finais exportados (.joblib)
├── notebooks/
│   ├── 01_precificacao_vendas.ipynb   # Pipeline de Vendas
│   └── 02_precificacao_locacao.ipynb  # Pipeline de Locação (Fase 5 à 11)
├── src/                      # Código-fonte modularizado do projeto
│   ├── __init__.py           # Inicializador do pacote Python
│   ├── main.py               # Servidor FastAPI e Endpoints da API
│   └── utils.py              # Funções auxiliares de formatação e métricas
├── .gitignore                # Bloqueio de arquivos temporários e caches
├── Dockerfile                # Configuração de conteinerização da API de produção
├── requirements.txt          # Ambiente completo de desenvolvimento local (Jupyter, Gráficos)
├── requirements_docker.txt   # Dependências enxutas exclusivas para produção Docker
└── README.md                 # Documentação principal do projeto

* **`data/`**: Divisão entre dados brutos (`raw/`) e dados limpos prontos para modelagem (`processed/`).
* **`notebooks/`**: Arquivos Jupyter organizados e documentados passo a passo.

### 📈 Fases Concluídas do Desenvolvimento:

#### 🔹 Fase 1: Saneamento e Tratamento de Outliers

* Vendas: Remoção de ruídos grotescos (imóveis com 1 m² ou valores de metro quadrado irreais).
* Locação: Identificação de distorções severas no mercado de aluguel. Foram eliminados anúncios com valores espúrios (como aluguéis de R$ 70,00 ou extremos de R$ 11 milhões) que destruiriam a capacidade de aprendizado dos algoritmos, afunilando a base para a realidade comercial de São Paulo.

#### 🔹 Fase 2: Redução de Alta Cardinalidade (Regra de Pareto)

* Análise de consistência textual da coluna `bairro`, que apresentava 1.561 registros únicos devido a erros de digitação e problemas de codificação (*encoding*).
* Aplicação de um **Filtro de Frequência**, mantendo apenas bairros com no mínimo 30 imóveis cadastrados. Essa estratégia reduziu a cardinalidade para **395 bairros estáveis**, retendo **93% do volume original dos dados** (91.242 registros).

#### 🔹 Fase 3: Engenharia de Recursos (Feature Engineering)
* **Target Encoding (Mean Encoding):** Implementado na variável categórica `bairro`, substituindo o texto livre pela média do preço por metro quadrado da região. Isso permitiu capturar o peso socioeconômico da localização sem inflar a dimensionalidade do dataset (*One-Hot Encoding*).
* **Preparação para Modelos Lineares/KNN:** Separação e isolamento de matrizes escaladas via `StandardScaler` para garantir uma competição justa entre algoritmos sensíveis à escala de distância.

####  🔹 Fase 4: Deploy e Conteinerização (Production-Ready)

* FastAPI & Uvicorn: Desenvolvimento de uma API REST ágil e moderna com validação de tipos em tempo de execução via Pydantic.

* Otimização de Dependências: Separação das bibliotecas analíticas e de gráficos (requirements.txt) do ambiente de deploy (requirements_docker.txt), mantendo no container apenas os pacotes estritamente necessários para inferência.

* Isolamento com Docker: Criação de uma imagem baseada em python:3.11-slim, mitigando o erro clássico de compatibilidade de sistema operacional ao unificar o ambiente de execução Linux.

#### 5. Modelagem Preditiva e Arena de Algoritmos

* O projeto evitou a abordagem comum de testar apenas um algoritmo. Foi construída uma Arena de Modelos testando diferentes abordagens de 3 famílias matemáticas distintas (Modelos Lineares, Árvores/Ensembles e Proximidade Espacial). A base de dados foi dividida estritamente em 80% para Treino e 20% para Teste.O projeto evitou a abordagem comum de testar apenas um algoritmo. Foi construída uma Arena de Modelos testando diferentes abordagens de 3 famílias matemáticas distintas (Modelos Lineares, Árvores/Ensembles e Proximidade Espacial). A base de dados foi dividida estritamente em 80% para Treino e 20% para Teste.

### 📊 Placar Geral de Performance (Métricas de Teste)

| Modelo | Família do Algoritmo | MAE (Erro Médio Absoluto) | $R^2$ Score (Poder de Explicação) | Resultado / Diagnóstico Técnico |
| :--- | :--- | :--- | :--- | :--- |
| **Regressão Linear** | Linear Pura | R$ 332,834.24 | 58.99% | *Baseline*. Errou feio em imóveis extremos e gerou preços negativos na base. |
| **Ridge Regression** | Linear com Regularização L2 | R$ 332,834.24 | 58.99% | Empate com a baseline. O dataset bem tratado não sofria de multicolinearidade. |
| **Árvore de Decisão** | Árvore Simples | R$ 221,732.21 | 66.41% | Corrigiu os preços negativos fatiando o mercado em regras lógicas não-lineares. |
| **XGBoost Regressor** | Boosting Sequencial | R$ 225,859.11 | 68.21% | Performance inferior às outras árvores devido à baixa dimensionalidade (poucas colunas) e sensibilidade a hiperparâmetros padrão. |
| **Random Forest** | Ensemble (Bagging) | R$ 210,723.36 | **74.38% (Campeão)** | **Melhor desempenho estatístico global**. A combinação de 100 árvores amaciou os erros e explicou melhor as variações do mercado. |
| **KNN Regressor** | Proximidade Espacial | **R$ 206,077.18 (Campeão)** | 73.59% | **Melhor desempenho de negócio**. Erra, em média, R$ 4.600,00 a menos por imóvel que o Random Forest ao espelhar o comportamento de um corretor humano. |

Decisão de Engenharia (Vendas): Ambos os modelos campeões (Random Forest e KNN Regressor) foram salvos em disco via joblib para avaliação de cenários em produção.

## 🏁 Painel Geral de Experimentos (Benchmarking de Modelos) -> Locação

Após testarmos individualmente diferentes famílias de algoritmos para o problema de precificação de locação, consolidamos os resultados na tabela abaixo, ordenados do melhor para o pior desempenho (baseado no R² Score):

| Posição | Modelo | Estratégia | MAE (Erro Médio) | R² Score (Explicação) |
| :---: | :--- | :--- | :--- | :--- |
| 🥇 **1º** | **Random Forest Regressor** | Bagging Ensemble | **R$ 1.753,04** | **0.7211** |
| 🥈 **2º** | XGBoost Regressor | Gradient Boosting | R$ 1.932,64 | 0.7124 |
| 🥉 **3º** | KNN Regressor | Vizinhança (Dados Escalados) | R$ 1.998,41 | 0.6817 |
| 4º | Árvore de Decisão Solo | Quebras Lógicas | R$ 2.012,06 | 0.6264 |
| 5º | Ridge Regression | Linear com Regularização L2 | R$ 3.402,02 | 0.2347 |
| 6º | Regressão Linear | Linear Simples (Baseline) | R$ 6.506,09 | -1.0343 |

### 🧠 Conclusões Técnicas do Experimento:

1. **Superioridade dos Ensembles:** Os modelos baseados em múltiplas árvores (Random Forest e XGBoost) dominaram o topo, provando que a combinação de estimadores reduz drasticamente o erro em dados complexos de mercado imobiliário.

2. **Fracasso Linear:** A incapacidade da Regressão Linear tradicional em modelar o problema (gerando R² negativo) confirma que a relação entre localização, área e preço em São Paulo é estritamente não-linear.

3. **Escolha Final:** O **Random Forest** foi eleito o modelo de produção por apresentar o menor erro absoluto médio (MAE), garantindo uma economia de quase R$ 180,00 por previsão em relação ao XGBoost.

## 🐳 Como Executar o Projeto via Docker
Graças ao isolamento por containers, não é necessário configurar ambientes virtuais locais (venv/conda) ou instalar o Python na sua máquina. Basta ter o Docker Desktop instalado.

1. Construir a Imagem Docker
No terminal, execute o comando na raiz do projeto para compilar a imagem oficial (a flag -t define o nome da tag):

```Bash
docker build -t predict-imoveis-sp .
```

2. Inicializar o Container
Inicialize a aplicação vinculando a porta 8000 do container com a porta 8000 da sua máquina host:

```Bash
docker run -d -p 8000:8000 --name api-imoveis predict-imoveis-sp
```

3. Acessando a Documentação Interativa
Com o container de pé, abra seu navegador de preferência e acesse a UI automatizada do Swagger:
👉 http://localhost:8000/docs

## 🌐 Endpoints da API Disponíveis

* GET /: Health Check para validação de integridade da API.

* POST /predict/vendas: Recebe os parâmetros estruturados e retorna o preço de venda estimado em Reais (R$).

* POST /predict/locacao: Recebe os parâmetros estruturados e retorna o preço de aluguel estimado em Reais (R$).

* Exemplo de Payload JSON (Entrada):
        JSON
        {
        "area_util": 75,
        "bairro_encoded": 2
        }
        Exemplo de Resposta do Modelo (Saída):
        JSON
        {
        "preco_estimado_venda": 115991.14
        }

## 🛠️ Tecnologias Utilizadas

* Linguagem: Python 3.11

* Manipulação de Dados: Pandas, NumPy

* Machine Learning: Scikit-Learn, XGBoost, Joblib

* API Framework: FastAPI, Uvicorn, Pydantic

* Conteinerização & Deploy: Docker / Docker Desktop Engine

* Visualização Gráfica: Matplotlib, Seaborn

* Versionamento: Git & GitHub

---
Developed by **Rafael Bezerra do Vale** Data Scientist | Machine Learning Specialist