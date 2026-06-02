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

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python
* **Manipulação de Dados:** Pandas, NumPy
* **Visualização Gráfica:** Matplotlib, Seaborn
* **Versionamento:** Git & GitHub

---

## 🔮 Próximos Passos (Fase 5)
* Divisão dos dados em conjuntos de Treino e Teste.
* Treinamento e validação cruzada de algoritmos de Regressão (Regressão Linear, Árvores de Decisão, Random Forest).
* Avaliação de performance utilizando métricas de mercado ($R^2$, MAE, RMSE).

---
Análise desenvolvida por **Rafael Bezerra do Vale** [Acompanhe meu progresso no LinkedIn](https://www.linkedin.com/) _(Insira o link do seu perfil aqui)_
Developed by **Rafael Bezerra do Vale** Data Scientist | Machine Learning Specialist