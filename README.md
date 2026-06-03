# 🏢 Inteligência Artificial para Precificação Imobiliária em São Paulo

Este projeto desenvolve um pipeline completo de Ciência de Dados e Inteligência Artificial para prever com alta precisão os preços de venda de imóveis na cidade de São Paulo. Utilizando uma base de dados realista com mais de 90 mil registros, o projeto foca em resolver desafios complexos de negócios, como o saneamento de outliers extremos e o tratamento de alta cardinalidade categórica.

---

## 🚀 Arquitetura do Projeto e Progresso Atual


O projeto foi estruturado seguindo as melhores práticas de Engenharia de Software e Data Science de nível Sênior. 

### 📁 Estrutura de Pastas do Repositório:

preco-imoveis-sp/
├── data/
│   ├── raw/          # Base de dados original (housing_sp_city.csv)
│   └── processed/    # Base limpa (vendas_sp_limpo.csv) pós-saneamento
├── notebooks/
│   └── 01_precificacao_vendas.ipynb  # Pipeline da Fase 1 à Fase 4
├── src/              # Código-fonte modularizado do projeto
│   ├── __init__.py   # Inicializador do pacote Python
│   └── utils.py      # Funções auxiliares (como a de formatação de métricas)
├── .gitignore        # Bloqueio de arquivos temporários e caches
├── requirements.txt  # Bibliotecas necessárias (pandas, seaborn, etc.)
└── README.md         # Documentação principal do projeto


* **`data/`**: Divisão entre dados brutos (`raw/`) e dados limpos prontos para modelagem (`processed/`).
* **`notebooks/`**: Arquivos Jupyter organizados e documentados passo a passo.

### 📈 Fases Concluídas do Desenvolvimento:

#### 🔹 Fase 1: Saneamento e Tratamento de Outliers
* Identificação e remoção de ruídos grotescos na base de dados (ex: imóveis anunciados com área útil de 1 m² ou valores de metro quadrado irreais).
* Aplicação de filtros de consistência de mercado para garantir que o modelo aprenda com dados comerciais plausíveis.

#### 🔹 Fase 2: Redução de Alta Cardinalidade (Regra de Pareto)
* Análise de consistência textual da coluna `bairro`, que apresentava 1.561 registros únicos devido a erros de digitação e problemas de codificação (*encoding*).
* Aplicação de um **Filtro de Frequência**, mantendo apenas bairros com no mínimo 30 imóveis cadastrados. Essa estratégia reduziu a cardinalidade para **395 bairros estáveis**, retendo **93% do volume original dos dados** (91.242 registros).

#### 🔹 Fase 3: Análise Exploratória de Dados Visual (EDAV)
* Construção de histogramas de distribuição focados na densidade real do mercado (identificando que o grosso dos anúncios em SP orbita entre R$ 300k e R$ 450k, com áreas de 50m² a 100m²).
* Mapeamento de correlação utilizando o **Coeficiente de Pearson**, quantificando a força de associação entre a Área Útil e o Preço de Venda ($r = 0.73$, indicando uma relação positiva forte).

#### 🔹 Fase 4: Engenharia de Recursos (Feature Engineering)
* Implementação da técnica de **Target Encoding (Mean Encoding)** na variável categórica `bairro`. 
* Substituição do texto livre pela média do preço por metro quadrado da região, permitindo que os algoritmos compreendam o peso socioeconômico da localização em uma única dimensão numérica, evitando a inflação de colunas no dataset (*One-Hot Encoding*).

## 🤖 5. Modelagem Preditiva e Arena de Algoritmos

Para encontrar a melhor solução de precificação para o mercado imobiliário de São Paulo, o projeto evitou a abordagem comum de testar apenas um algoritmo. Foi construída uma **Arena de Modelos** testando 6 abordagens de 3 famílias matemáticas distintas (Modelos Lineares, Árvores/Ensembles e Proximidade Espacial).

A base de dados foi dividida estritamente em **80% para Treino (72.993 imóveis)** e **20% para Teste (18.249 imóveis)** para garantir a robustez da validação.

### 📊 Placar Geral de Performance (Métricas de Teste)

| Modelo | Família do Algoritmo | MAE (Erro Médio Absoluto) | $R^2$ Score (Poder de Explicação) | Resultado / Diagnóstico Técnico |
| :--- | :--- | :--- | :--- | :--- |
| **Regressão Linear** | Linear Pura | R$ 332,834.24 | 58.99% | *Baseline*. Errou feio em imóveis extremos e gerou preços negativos na base. |
| **Ridge Regression** | Linear com Regularização L2 | R$ 332,834.24 | 58.99% | Empate com a baseline. O dataset bem tratado não sofria de multicolinearidade. |
| **Árvore de Decisão** | Árvore Simples | R$ 221,732.21 | 66.41% | Corrigiu os preços negativos fatiando o mercado em regras lógicas não-lineares. |
| **XGBoost Regressor** | Boosting Sequencial | R$ 225,859.11 | 68.21% | Performance inferior às outras árvores devido à baixa dimensionalidade (poucas colunas) e sensibilidade a hiperparâmetros padrão. |
| **Random Forest** | Ensemble (Bagging) | R$ 210,723.36 | **74.38% (Campeão)** | **Melhor desempenho estatístico global**. A combinação de 100 árvores amaciou os erros e explicou melhor as variações do mercado. |
| **KNN Regressor** | Proximidade Espacial | **R$ 206,077.18 (Campeão)** | 73.59% | **Melhor desempenho de negócio**. Erra, em média, R$ 4.600,00 a menos por imóvel que o Random Forest ao espelhar o comportamento de um corretor humano. |

### 🏆 Decisão de Engenharia e Persistência

Diante do empate técnico com nuances de negócio, **ambos os modelos campeões (Random Forest e KNN Regressor) foram persistidos em disco utilizando a biblioteca `joblib`** (otimizada para grandes matrizes numéricas). 

A escolha final do modelo para o ambiente de produção dependerá da estratégia da empresa: priorizar a estabilidade estatística global (Random Forest) ou focar na redução do erro médio direto no bolso do cliente (KNN).
---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python
* **Manipulação de Dados:** Pandas, NumPy
* **Visualização Gráfica:** Matplotlib, Seaborn
* **Versionamento:** Git & GitHub

---
Análise desenvolvida por **Rafael Bezerra do Vale** [Acompanhe meu progresso no LinkedIn](https://www.linkedin.com/) _(Insira o link do seu perfil aqui)_
Developed by **Rafael Bezerra do Vale** Data Scientist | Machine Learning Specialist