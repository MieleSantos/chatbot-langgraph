FROM python:3.12-slim

# Definir o diretório de trabalho dentro do container
WORKDIR /app

# Instalar dependências necessárias para compilar pacotes
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Instalar o Poetry
RUN curl -sSL https://install.python-poetry.org | python3 - \
    && ln -s /root/.local/bin/poetry /usr/local/bin/poetry

# Copiar os arquivos de dependências do projeto
COPY pyproject.toml poetry.lock* /app/

# Instalar as dependências do Poetry sem criar o ambiente virtual
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Copiar todo o código do projeto
COPY . /app