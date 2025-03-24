FROM python:3.11

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости
COPY req.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r req.txt

# Копируем код приложения
COPY . .

# Запускаем приложение
CMD ["python3", "-m", "src.main"]