FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN mkdir -p static

# Instalar git y limpiar archivos temporales para reducir el tamaño de la imagen
RUN apt-get update && \
    apt-get install -y git && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

ENV PYTHONPATH=/app/src

ENTRYPOINT ["python", "src/SensaCineScraper.py"]