# Temel imaj
FROM python:3.9-slim

# Çalışma dizini
WORKDIR /app

# Gereksinimleri kopyala ve yükle
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama kodunu kopyala
COPY . .

# Uygulamayı çalıştır
CMD ["python", "app.py"]