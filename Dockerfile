FROM python:3.11-slim

WORKDIR /app

# Puxando o nosso arquivo de dependências limpo e rápido
COPY ./requirements_docker.txt ./requirements.txt

# Sintaxe corrigida com apenas um traço
RUN pip install --no-cache-dir -r requirements.txt

# Copiando os arquivos do seu modelo e da API de SP
COPY ./src ./src
COPY ./models ./models

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]