FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libpq-dev \
    wget \
    netcat-traditional \
    && wget -q https://github.com/eficode/wait-for/releases/download/v2.2.3/wait-for \
    && chmod +x wait-for \
    && mv wait-for /usr/local/bin/ \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["sh", "-c", "wait-for db:5432 -- python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]