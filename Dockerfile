From python:3.10-slim

WORKDIR /app

COPY requerements.txt

RUN pip install --no--cache--dir -r requerements.txt

COPY ./src ./src
COPY ./models ./models

EXPOSE 8000

CMD ['uvicorn', 'src.main:app', "--host", "0.0.0.0", "--port", "8000"]
